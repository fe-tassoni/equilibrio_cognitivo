from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from .forms import CadastroForm, LoginForm, PasswordResetRequestForm, ProfileUpdateForm
import logging

logger = logging.getLogger(__name__)

def cadastro(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Conta criada com sucesso! Você já pode fazer login.')
            logger.info(f'Novo usuário cadastrado: {user.username}')
            return redirect('account_login')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = CadastroForm()

    return render(request, 'usuarios/cadastro.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # Verificar se deve lembrar do usuário
            remember_me = form.cleaned_data.get('remember_me')
            if remember_me:
                request.session.set_expiry(1209600)  # 2 semanas
            else:
                request.session.set_expiry(0)  # Fechar ao fechar o navegador
            
            messages.success(request, f'Bem-vindo de volta, {user.first_name or user.username}!')
            logger.info(f'Usuário logado: {user.username}')
            
            # Redirecionar para a página solicitada ou dashboard
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Nome de usuário ou senha incorretos.')
    else:
        form = LoginForm()

    return render(request, 'usuarios/login.html', {'form': form})

@login_required
def logout_view(request):
    username = request.user.username
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso.')
    logger.info(f'Usuário deslogado: {username}')
    return redirect('home')

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            
            # Gerar token de reset
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            
            # Criar link de reset
            reset_link = request.build_absolute_uri(
                reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
            )
            
            # Enviar e-mail (em produção, configure o backend de e-mail)
            try:
                send_mail(
                    'Redefinição de Senha - Equilíbrio Cognitivo',
                    f'Clique no link para redefinir sua senha: {reset_link}',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
                messages.success(request, 'E-mail de redefinição enviado! Verifique sua caixa de entrada.')
                logger.info(f'E-mail de reset enviado para: {email}')
            except Exception as e:
                messages.error(request, 'Erro ao enviar e-mail. Tente novamente mais tarde.')
                logger.error(f'Erro ao enviar e-mail de reset: {e}')
            
            return redirect('account_login')
    else:
        form = PasswordResetRequestForm()
    
    return render(request, 'usuarios/password_reset.html', {'form': form})

def password_reset_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            
            if password1 and password1 == password2:
                user.set_password(password1)
                user.save()
                messages.success(request, 'Senha redefinida com sucesso! Você já pode fazer login.')
                logger.info(f'Senha redefinida para usuário: {user.username}')
                return redirect('account_login')
            else:
                messages.error(request, 'As senhas não coincidem.')
        
        return render(request, 'usuarios/password_reset_confirm.html', {'validlink': True})
    else:
        messages.error(request, 'Link de redefinição inválido ou expirado.')
        return render(request, 'usuarios/password_reset_confirm.html', {'validlink': False})

@login_required
def profile_view(request):
    return render(request, 'usuarios/profile.html', {'user': request.user})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            logger.info(f'Perfil atualizado: {request.user.username}')
            return redirect('profile')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = ProfileUpdateForm(instance=request.user, user=request.user)
    
    return render(request, 'usuarios/profile_edit.html', {'form': form})

@login_required
def dashboard(request):
    # Estatísticas básicas do usuário
    context = {
        'total_pacientes': 0,  # Será implementado quando o modelo de pacientes estiver pronto
        'total_testes': 0,     # Será implementado quando os testes estiverem prontos
        'testes_recentes': [], # Lista de testes recentes
    }
    return render(request, 'usuarios/dashboard.html', context)

