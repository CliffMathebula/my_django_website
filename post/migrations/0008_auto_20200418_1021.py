# Generated by Django 3.0.5 on 2020-04-18 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20200418_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='email_address',
        ),
        migrations.RemoveField(
            model_name='post',
            name='password',
        ),
        migrations.RemoveField(
            model_name='post',
            name='username',
        ),
        migrations.AlterField(
            model_name='post',
            name='surname',
            field=models.TextField(),
        ),
    ]
