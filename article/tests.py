from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


from .models import Article

class ArticleTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass"
        )
        testuser1.save()

        test_thing = Article.objects.create(
            title="rake",
            author=testuser1,
            content="Better for collecting leaves than a shovel.",
            reference="Better for collecting leaves than a shovel.",

        )
        test_thing.save()

    def setUp(self):
        self.client.login(username='testuser1', password="pass")

    def test_get_articles_list_model(self):
        article= Article.objects.get(id=1)
        actual_owner = str(article.author)
        actual_name = str(article.title)
        actual_description = str(article.content)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_description, "Better for collecting leaves than a shovel."
        )

    def test_get_articles_list(self):
        url = reverse("articles_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        articles = response.data
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0]["author"], "rake")

    def test_auth_required(self):
        self.client.logout()
        url = reverse("articles_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_owner_can_delete(self):
        self.client.logout()
        self.client.login(username='testuser2', password="pass")
        url = reverse("article_detail", args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)