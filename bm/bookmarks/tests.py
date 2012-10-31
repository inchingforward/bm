from django.test import TestCase


class BookmarksViewTestCase(TestCase):
    def test_index(self):
        """
        Sanity test to make sure the bookmarks index page is working.
        """
        response = self.client.get('/bookmarks/')
        self.assertEqual(response.status_code, 200)
