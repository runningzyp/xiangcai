from django.db import models
from django.contrib.auth.models import User

from .category import Category


class Article(models.Model):
    owner = models.ForeignKey(
        User,
        related_name="articles",
        related_query_name="articles",
        on_delete=models.CASCADE,
        default=1,
    )
    category = models.ForeignKey(
        Category,
        verbose_name="所属分类",
        related_name="articles",
        related_query_name="articles",
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField("标题", max_length=200)
    body = models.TextField()
    create_time = models.TimeField(auto_now=True)
    modify_time = models.TimeField(auto_now_add=True)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"

    def __str__(self):
        return self.title
