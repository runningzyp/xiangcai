from django.db import models
from blog.models import Article


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        verbose_name="评论主体",
        related_name="comments",
        related_query_name="comments",
        on_delete=models.SET_NULL,
        null=True,
    )
    content = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    modify_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"

    def __str__(self):
        return self.content
