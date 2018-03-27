# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-27 16:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotes', models.CharField(max_length=255)),
                ('quoteBy', models.CharField(max_length=255)),
                ('quoteMessage', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='userquote',
            name='favQuotes',
            field=models.ManyToManyField(related_name='favUsers', to='quotesapp.UserRegistration'),
        ),
        migrations.AddField(
            model_name='userquote',
            name='userFav',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favQuotes', to='quotesapp.UserRegistration'),
        ),
        migrations.AddField(
            model_name='userquote',
            name='userQuote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='quotesapp.UserRegistration'),
        ),
    ]