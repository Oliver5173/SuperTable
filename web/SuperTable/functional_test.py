from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()  

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Check out homepage
        self.browser.get('http://localhost:8000')

        # Notices the page title
        self.assertIn('SuperTable', self.browser.title)
        # self.fail("Finish the test!")

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    
