# Generated by Django 5.1.3 on 2024-12-01 15:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0003_alter_estudent_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
