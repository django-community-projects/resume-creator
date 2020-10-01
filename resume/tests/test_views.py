from django.test import TestCase
from django.urls import reverse


class ViewsTest(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('resume:index'))
        self.assertEqual(response.status_code, 404)
