# Generated by Django 3.0.5 on 2020-04-18 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20200418_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
