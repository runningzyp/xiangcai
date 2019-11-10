from django.contrib.auth.models import User, Group

from rest_framework import serializers

from .models import Category, Article


class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "body",
            "create_time",
            "modify_time",
            "category",
            "owner",
        ]


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Category
        fields = ["id", "name", "owner", "articles"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "last_login", "groups", "articles"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
