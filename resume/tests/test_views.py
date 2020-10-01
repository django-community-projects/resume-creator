from django.test import TestCase


class ViewsTest(TestCase):
    def test_index_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
