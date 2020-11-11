# -*- coding: utf-8 -*-
from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=200, help_text='name_of_project', null=False)
    description = models.CharField(max_length=600, help_text='project_description', null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.project_name
