from django.contrib import admin
from .models import Article, Category
from django import forms
from django.db import models


class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            "widget": forms.Textarea(attrs={"id": "project_update_textarea"})
        },
    }


# Register your models here.

admin.site.register(Category, MyModelAdmin)
admin.site.register(Article, MyModelAdmin)
