# Generated by Django 4.1.3 on 2022-12-06 06:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('catagory_id', models.SlugField(max_length=20, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')], verbose_name='Catagory id')),
                ('catagory_name', models.CharField(blank=True, max_length=200)),
                ('catagory_definition', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equipment_id', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True, verbose_name='Equipment id')),
                ('equipment_name', models.CharField(max_length=200)),
                ('equiment_description', models.TextField(blank=True, max_length=9000)),
                ('date_obtained', models.DateTimeField(auto_now_add=True)),
                ('catagory_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Equipment.catagory')),
            ],
        ),
    ]
