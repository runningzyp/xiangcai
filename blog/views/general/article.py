from blog.models import Article
from django.shortcuts import get_object_or_404

# some_app/views.py
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get(self, request, *args, **kwargs):
        context = {}
        context["articles"] = Article.objects.all()[:5]
        return self.render_to_response(context)


class AtricleDetailView(TemplateView):
    template_name = "main/article.html"

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get("pk"))
        context = {}
        context["article"] = article
        return self.render_to_response(context)
