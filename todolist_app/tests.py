from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Todo, Priority


# Create your tests here.
class TestLogin(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="martin")
        self.user.set_password("123456")
        self.user.save()
        self.p = Priority.objects.create(name="Urgent", order=3)

    def test_home_after_login_status_code_200(self):
        self.client.login(username='martin', password='123456')
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_home_redirects_to_login_status_code_302(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 302)

    def test_login_incorrect(self):
        response = self.client.post("/login/?next=/", {"username": 'martin', "password": 'ppp'})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)

    def test_login_correct_redirects_to_home(self):
        response = self.client.post("/login/?next=/", {"username": 'martin', "password": '123456'}, follow=True)
        self.assertRedirects(response, "/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)


class TestCreateTodo(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="martin")
        self.user.set_password("123456")
        self.user.save()
        self.p = Priority.objects.create(name="Urgent", order=3)

    def test_create_todo_redirects_to_details(self):
        self.client.login(username='martin', password='123456')
        response = self.client.post("/create/", {"title": 'create_todo', "description": 'kaka', 'done': True, 'priority': self.p.id}, follow=True)
        id = response.context["object"].id
        self.assertRedirects(response, f"/todo/{id}")
        self.assertEqual(response.status_code, 200)
