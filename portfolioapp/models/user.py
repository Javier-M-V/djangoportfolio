# -*- coding: utf-8 -*-
from django.db import models


class User(models.Model):

    username = models.CharField(max_length=100, help_text='user_name')
    surname = models.CharField(max_length=100, help_text='user_surname')
    city = models.CharField(max_length=100, blank=True, null=True)
    birthdate = models.DateField()
    phone = models.PositiveIntegerField(help_text='phone_number')
    mail = models.EmailField(help_text='email_account')
    project = models.ManyToManyField('Project', blank=True, null=True)
    education = models.ManyToManyField('Education', blank=True, null=True)
    career = models.ManyToManyField('Career', blank=True, null=True)
    knowledge = models.ManyToManyField('Knowledge', blank=True, null=True)

    def __str__(self):
        return self.username


