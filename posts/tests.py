from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.

class NiceModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text="just a test")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        exp_name = f"{post.text}"
        self.assertEqual(exp_name, "just a test")



class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text="this is another test")
    
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code,200)

    def test_view_uses_correct_templates(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home.html")