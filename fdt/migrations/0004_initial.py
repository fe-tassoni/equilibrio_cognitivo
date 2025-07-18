# Generated by Django 5.2.3 on 2025-07-02 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fdt', '0003_delete_normafdt'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorrecaoFDT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Tempos', 'Tempos'), ('Erros', 'Erros')], max_length=10)),
                ('fase', models.CharField(choices=[('Leitura', 'Leitura'), ('Contagem', 'Contagem'), ('Escolha', 'Escolha'), ('Alternância', 'Alternância'), ('Inibição', 'Inibição'), ('Flexibilidade', 'Flexibilidade')], max_length=20)),
                ('faixa_etaria_min', models.IntegerField()),
                ('faixa_etaria_max', models.IntegerField()),
                ('media', models.FloatField()),
                ('dp', models.FloatField()),
                ('pc_95', models.FloatField()),
                ('pc_75', models.FloatField()),
                ('pc_50', models.FloatField()),
                ('pc_25', models.FloatField()),
                ('pc_5', models.FloatField()),
            ],
        ),
    ]
