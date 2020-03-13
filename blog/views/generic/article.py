from blog.models import Article
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages

# some_app/views.py
from django.views.generic import ListView, DetailView
from blog.forms.comment import CommentForm
from blog.models.comment import Comment


class ArticleListView(ListView):
    template_name = "main/article_list.html"

    model = Article
    # paginate_by = 1  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


IndexView = ArticleListView


class ArticleDetailView(DetailView):
    template_name = "main/article.html"
    model = Article
    slug_field = "title"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article"] = self.object
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get("pk"))
        comment = Comment(article=article, content=request.POST.get("comment"))
        comment.save()
        messages.add_message(request, messages.INFO, "添加评论成功!")
        return redirect(f"/article/{article.id}")
