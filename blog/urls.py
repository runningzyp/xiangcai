from blog.views.general.article import IndexView, AtricleDetailView
from django.urls import include, path
from rest_framework import routers

from . import views

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(r"article/<int:pk>", AtricleDetailView.as_view(), name="article"),
]


router = routers.DefaultRouter()
router.register(r"article", views.ArticleViewSet)
router.register(r"category", views.CategoryViewSet)
router.register(r"users", views.UserViewSet)


urlpatterns += [
    path("api/v1/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
