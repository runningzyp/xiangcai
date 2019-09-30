from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'article', views.ArticleViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
