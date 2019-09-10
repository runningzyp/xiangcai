from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name="类别", max_length=50, default="默认")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"

    def __str__(self):
        return self.name
