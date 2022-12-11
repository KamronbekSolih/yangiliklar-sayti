from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Mavzu', text = 'yangilik matni')
        Post.objects.create(title = 'Mavzu 2', text = 'yangilik matni 2')

    def test_text_content(self):

        post = Post.objects.get(id=1)
        expected_object_title = f'{post.title}'
        expected_object_text = f'{post.text}'
        self.assertEqual(expected_object_title, 'Mavzu')
        self.assertEqual(expected_object_text,'yangilik matni')

        post = Post.objects.get(id=2)
        expected_object_title = f'{post.title}'
        expected_object_text = f'{post.text}'
        self.assertEqual(expected_object_title, 'Mavzu 2')
        self.assertEqual(expected_object_text,'yangilik matni 2')

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title = 'Marokash ertagi', text = 'Postugali ustidan g\'alaba qozondi')

    def test_views_url_exists_in_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    # def test_view_url_by_name(self):
    #     resp = self.client.get(reverse('home'))
    #     self.assertEqual(resp.status_code, 200)