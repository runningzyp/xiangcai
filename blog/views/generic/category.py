from blog.models import Category

# some_app/views.py
from django.views.generic import ListView, DetailView


class CategoryListView(ListView):
    template_name = "main/category_list.html"
    model = Category
    # paginate_by = 1  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoryDetailView(DetailView):
    template_name = "main/category.html"
    model = Category
    slug_field = "name"
    # paginate_by = 1  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article_list"] = self.object and self.object.articles.all()
        context["category_list"] = Category.objects.all()
        return context
