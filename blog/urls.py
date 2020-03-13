from blog.views.generic.article import IndexView, ArticleDetailView
from blog.views.generic.comment import ArticleCommentView
from blog.views.generic.category import CategoryListView, CategoryDetailView
from django.urls import include, path
from rest_framework import routers

from . import views

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(r"article/<str:slug>", ArticleDetailView.as_view(), name="article"),
    path(r"categories", CategoryListView.as_view(), name="categories"),
    path(
        r"category/<str:slug>", CategoryDetailView.as_view(), name="category"
    ),
    path(
        r"article/<int:pk>/comments",
        ArticleCommentView.as_view(),
        name="comment",
    ),
]


router = routers.DefaultRouter()
router.register(r"article", views.ArticleViewSet)
router.register(r"category", views.CategoryViewSet)
router.register(r"users", views.UserViewSet)


urlpatterns += [
    path("api/v1/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
