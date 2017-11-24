# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 08:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(max_length=20)),
                ('shift', models.CharField(choices=[('DE', 'délelőtt'), ('DU', 'délután'), ('NO', 'nem')], default='NO', max_length=10)),
                ('hours', models.SmallIntegerField(choices=[(6, 6), (8, 8)], default=6)),
            ],
        ),
        migrations.CreateModel(
            name='LateRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(max_length=20)),
                ('shift', models.CharField(choices=[('DE', 'délelőtt'), ('DU', 'délután'), ('NO', 'nem')], default='NO', max_length=10)),
                ('hours', models.SmallIntegerField(choices=[(6, 6), (8, 8)], default=6)),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.SmallIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='laterequest',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.WeeklyRequest'),
        ),
        migrations.AddField(
            model_name='dailyrequest',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.WeeklyRequest'),
        ),
        migrations.AlterUniqueTogether(
            name='weeklyrequest',
            unique_together=set([('user', 'week')]),
        ),
        migrations.AlterUniqueTogether(
            name='laterequest',
            unique_together=set([('week', 'day')]),
        ),
        migrations.AlterUniqueTogether(
            name='dailyrequest',
            unique_together=set([('week', 'day')]),
        ),
    ]
