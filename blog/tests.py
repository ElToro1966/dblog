from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from unittest import skip
from .models import Post

class PostModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='Blog post title',
            author=self.user,
            body='Blog post body'
        )

    def test_blog_post_string_presentation(self):
        post=Post(title='Sample title')
        self.assertEqual(str(post), post.title)

    def test_blog_post_content(self):
        post=Post.objects.get(id=1)
        self.assertEqual(f'{post.title}', 'Blog post title')
        self.assertEqual(f'{post.author}', 'testuser') 
        self.assertEqual(f'{post.body}', 'Blog post body')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Blog post body')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/1000000/')
        self.assertEqual(response.status_code, 200)
        self-assertEqual(no_response.status_code, 400)

    @skip
    def test_blog_post_on_admin_page(self):
        response = self.client.get('/admin', follow=True)
        print(response)
        self.assertContains(response,'Posts')
