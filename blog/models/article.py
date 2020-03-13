from django.db import models
from django.contrib.auth.models import User

from .category import Category
import markdown


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
    body = models.TextField("文章")
    body_html = models.TextField("转码文章", null=True, blank=True)
    body_toc = models.TextField("文章目录", null=True, blank=True)
    create_time = models.DateTimeField(auto_now=True)
    modify_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        md = markdown.Markdown(
            extensions=[
                # "markdown.extensions.extra",
                # "markdown.extensions.codehilite",
                "markdown.extensions.toc"
            ],
            extension_configs={"markdown.extensions.toc": {"toc_depth": 3}},
        )
        self.body_html = md.convert(self.body)
        self.body_toc = md.toc
        super(Article, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"

    def __str__(self):
        return self.title
