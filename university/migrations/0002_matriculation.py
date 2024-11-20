# Generated by Django 5.1.3 on 2024-11-20 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matriculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('M', 'Morning'), ('V', 'Evening'), ('N', 'Night')], default='M', max_length=1)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.course')),
                ('estudent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.estudent')),
            ],
        ),
    ]
