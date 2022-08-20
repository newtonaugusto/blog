
from django.urls import reverse

from rest_framework.test import APITransactionTestCase
from rest_framework import status

from accounts.models import User

URL = reverse("accounts:login")


class AuthenticationTestCase(APITransactionTestCase):

    """
        Teste de autenticação

        Caminho do teste:
            accounts.tests.test_login.test_authentication.AuthenticationTestCase

            obs.:
                Para rodar somente este teste digite o comando:
                python manage.py test 'caminho'

        O que será testado:
            1 - Login com sucesso
            2 - Senha incorreta
            3 - Username incorreto

    """

    def setUp(self):
        self.credentials = {
            'username': 'test@test.com.br',
            'password': 'S3cretP@ssword'
        }
        self.login_data = {
            'email': 'test@test.com.br',
            'password': 'S3cretP@ssword'
        }

        User.objects.create_user(**self.credentials)

    def test_login_success(self):
        # Deve logar
        response = self.client.post(URL, self.login_data)
        self.assertEqual(
            response.status_code, 201, "Senha correta, deveria logar.")

    def test_login_failure_password(self):
        # Não deve logar
        wrong_credentials = self.login_data
        wrong_credentials["password"] = "SenhaErrada@!123"
        response = self.client.post(URL, self.login_data)
        self.assertEqual(
            response.status_code, 401, "Senha incorreta, não deve logar.")

    def test_login_failure_username(self):
        # Não deve logar
        wrong_credentials = self.login_data
        wrong_credentials["email"] = "wrong.email@email.com.br"
        response = self.client.post(URL, self.login_data)
        self.assertEqual(
            response.status_code, 401, "Username incorreto, não deve logar.")
