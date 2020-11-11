# -*- coding: utf-8 -*-
from django.db import models


class Career(models.Model):

    company = models.CharField(max_length=100, help_text='org_name', null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=100, help_text='position_or_job')
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.company

    @property
    def is_current(self):
        return False if self.end_date is None else True
