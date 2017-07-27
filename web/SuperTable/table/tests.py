from django.test import TestCase
from django.urls import resolve
from table.views import index
# Create your tests here.

class IndexPageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)
