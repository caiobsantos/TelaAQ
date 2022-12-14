# Generated by Django 4.1 on 2022-08-11 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Decomol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producao', models.CharField(max_length=50)),
                ('data_liberacao', models.DateTimeField(auto_now_add=True)),
                ('resultado_cor', models.CharField(blank=True, max_length=50)),
                ('sensorial', models.CharField(blank=True, max_length=100)),
                ('brix', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('ph', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
                ('liberado', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]
