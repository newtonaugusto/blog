
from django.urls import reverse

from rest_framework.test import APITransactionTestCase, APIClient

from accounts.models import User

URL = reverse("business:articles")
URL_LOGIN = reverse("accounts:login")


class ArticlePostTestCase(APITransactionTestCase):

    """
        Teste de cadastro de artigos

        Caminho do teste:
            business.tests.test_article.test_post.ArticlePostTestCase

            obs.:
                Para rodar somente este teste digite o comando:
                python manage.py test 'caminho'

        O que será testado:
            1 - Cadastro com sucesso
            2 - Campos incorretos

    """

    def setUp(self):

        self.credentials = {
            'email': 'test@test.com.br',
            'password': 'S3cretP@ssword'
        }

        self.success_object = {
            "title": "Lorem Ipsum 2",
            "subtitle": "Neque porro quisquam...",
            "type": 0,
            "content": "Vivamus rutrum mi lacinia nisi commodo consectetur. ",
            "status": 1,
            "keyword_set": [
                {
                    "name": "Lorem"
                },
                {
                    "name": "Ipsum"
                }
            ]
        }

        self.wrong_object = {
            "t3itle": "Lorem Ipsum 2",
            "suubtitle": "Neque porro quisquam...",
            "type": "sas",
            "content": "Vivamus rutrum mi lacinia nisi commodo consectetur. ",
            "status": 1,
            "keyword_set": [
                {
                    "name": "Lorem"
                },
                {
                    "name": "Ipsum"
                }
            ]
        }

        self.c = APIClient()

        User.objects.create_superuser(**self.credentials)
        response = self.c.post(
            URL_LOGIN,
            {
                'email': 'test@test.com.br',
                'password': 'S3cretP@ssword'
            })
        self.c.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['jwt'])

    def test_create_article_success(self):
        # Deve criar artigo
        response = self.c.post(URL, self.success_object)

        self.assertEqual(
            response.status_code, 201, "Objeto correto, deve criar.")

    def test_create_article_failure(self):
        # Não deve criar o artigo
        response = self.c.post(URL, self.wrong_object)
        self.assertEqual(
            response.status_code, 400, "Objeto incorreto, deve retornar 400.")
