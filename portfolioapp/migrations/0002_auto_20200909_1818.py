# Generated by Django 3.1.1 on 2020-09-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]