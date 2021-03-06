# Generated by Django 3.1.1 on 2020-09-13 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0002_auto_20200909_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='career',
            field=models.ManyToManyField(blank=True, to='portfolioapp.Career'),
        ),
        migrations.AlterField(
            model_name='user',
            name='education',
            field=models.ManyToManyField(blank=True, to='portfolioapp.Education'),
        ),
        migrations.AlterField(
            model_name='user',
            name='project',
            field=models.ManyToManyField(blank=True, to='portfolioapp.Project'),
        ),
    ]
