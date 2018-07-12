
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_user_can_CRUD_a_post(self):
        # User enters blog web page
        self.browser.get('http://localhost:8000')
        # The blog page's title contains Django blog
        self.assertIn('Django blog', self.browser.title)

        # She enters the form to create a new blog post

        # She submits the form

        # She sees the new post on the main page

        # She sees the post details

        # She updates the post from the details page

        # She sees the updates on the main page

        # ... and on the details page

        # She deletes the post

if __name__ == '__main__':
    unittest.main(warnings='ignore')
