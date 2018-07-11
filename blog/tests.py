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
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'post_detail.html')
        self.assertContains(response,'Blog post body')

    def test_post_create_form_view(self):
        response = self.client.get(reverse('post_new'),{
            'title': 'New title',
            'body': 'New text',
            'author': self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')
        self.assertContains(response, self.user)

    def test_post_update_form_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Ipdated title',
            'body': 'Updated body',
            })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.get(
            reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 200)

    @skip
    def test_blog_post_on_admin_page(self):
        response = self.client.get('/admin', follow=True)
        print(response)
        self.assertContains(response,'Posts')
