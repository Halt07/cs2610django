from django.contrib import admin

from .models import Question, PageCount

admin.site.register(Question)
admin.site.register(PageCount)
