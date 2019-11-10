from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

from blog.models import Category
from blog.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
