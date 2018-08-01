
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_user_can_CRUD_a_post(self):
        # User enters blog web page
        self.browser.get('http://localhost:8000')
        # The blog page's title and header contains Django blog
        self.assertIn('Django blog', self.browser.title)
        self.assertIn('Django blog', 
            self.browser.find_element_by_tag_name('h1').text
        )

        # She sees a link to the form for creating new blog posts
        self.assertTrue(
            self.browser.find_element_by_link_text(
                '+ New Blog Post'
            )
            .is_displayed()
        )

        # She enters the form to create a new blog post
        self.browser.find_element_by_link_text(
            '+ New Blog Post'
        ).click()

        # She enters a blog post text
        inputbox = self.browser.find_element_by_ID('id_title')
        inputbox.send_keys("Just Another Blog Post")
        scrolldown = self.browser.find_element_by_name('')
        Select(scrolldown).select_by_value('1')
        
        # She submits the form
        inputbox.find_element_by_xpath("//input[@value='Submit']").click()

        # She sees the new post on the main page


        # She sees the post details

        # She updates the post from the details page

        # She sees the updates on the main page

        # ... and on the details page

        # She deletes the post

if __name__ == '__main__':
    unittest.main(warnings='ignore')
