from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article


# Not sure what this doing
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email"]


class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author', read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
