from blog.models import Article
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages

# some_app/views.py
from django.views.generic import View
from blog.models.comment import Comment


class ArticleCommentView(View):
    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get("pk"))
        content = self.request.POST.get("comment")
        if not content:
            messages.add_message(
                self.request, messages.ERROR, "请输入内容 !", extra_tags="danger"
            )
            return redirect(f"/article/{article.title}")
        comment = Comment(article=article, content=content)
        comment.save()
        messages.add_message(self.request, messages.INFO, "添加评论成功 !")
        return redirect(f"/article/{article.title}")
