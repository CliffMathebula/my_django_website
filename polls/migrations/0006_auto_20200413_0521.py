# Generated by Django 3.0.5 on 2020-04-13 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20200413_0518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='content',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='date',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='name',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='slug',
        ),
    ]