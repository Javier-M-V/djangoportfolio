# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Knowledge(models.Model):
    knowledge_name = models.CharField(max_length=100, null=False)
    level = models.PositiveIntegerField(max_length=4, default=1,
                                        validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return self.knowledge_name
