# Generated by Django 4.1 on 2022-10-28 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historico', '0005_alter_decomolhistorico_data_liberacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decomolhistorico',
            name='data_liberacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
