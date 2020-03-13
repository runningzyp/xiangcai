from django.contrib import admin
from .models import Article, Category, Comment
from django import forms
from django.db import models


class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            "widget": forms.Textarea(attrs={"id": "project_update_textarea"})
        }
    }


class ArticleAdmin(admin.ModelAdmin):
    # exclude = ("body_html",)
    pass


# Register your models here.

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
# admin.site.register(Category, MyModelAdmin)
# admin.site.register(Article, MyModelAdmin)
# admin.site.register(Comment, MyModelAdmin)
