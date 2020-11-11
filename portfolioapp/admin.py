# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import User, Career, Project, Education, Knowledge


admin.site.register(User)
admin.site.register(Career)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Knowledge)

