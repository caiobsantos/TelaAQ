# Generated by Django 4.1 on 2022-12-06 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('troca', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trocahistorico',
            name='data_fim',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
