# -*- coding: utf-8 -*-
from django.db import models


class Education(models.Model):
    org_name = models.CharField(max_length=100, help_text='org_name', null=False)
    name_degree = models.CharField(max_length=100, help_text='title_name', null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.org_name
