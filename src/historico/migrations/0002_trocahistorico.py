# Generated by Django 4.1 on 2022-09-29 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrocaHistorico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decomol', models.CharField(max_length=50)),
                ('data_troca', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
