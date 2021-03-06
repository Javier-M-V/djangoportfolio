# Generated by Django 3.1.1 on 2020-09-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0003_auto_20200913_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='career',
            field=models.ManyToManyField(null=True, to='portfolioapp.Career'),
        ),
        migrations.AlterField(
            model_name='user',
            name='education',
            field=models.ManyToManyField(null=True, to='portfolioapp.Education'),
        ),
        migrations.AlterField(
            model_name='user',
            name='project',
            field=models.ManyToManyField(null=True, to='portfolioapp.Project'),
        ),
    ]
