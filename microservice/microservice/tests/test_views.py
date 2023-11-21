from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class SignUpViewTests(TestCase):
    def test_signup_page_status_code(self):
        response = self.client.get('/accounts/signup/')
        self.assertEquals(response.status_code, 200)

    def test_signup_form(self):
        response = self.client.post('/accounts/signup/', data={
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertEquals(response.status_code, 302)  # Redirect on success

class ChatViewTests(TestCase):
    def setUp(self):
        User.objects.create_user(username='testuser', password='testpassword123')

    def test_chat_view_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('chat'))
        self.assertRedirects(response, f"{reverse('signup')}?next={reverse('chat')}")

    def test_chat_view(self):
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('chat'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat.html')