from django.test import SimpleTestCase
from django.urls import reverse

class HomePageTest(SimpleTestCase):
    # test homepage status code
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    #test homepage url name
    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    #test homepage template 
    def test_homepage_template(self):
        response = self.client.get('/')
        print(response)
        self.assertTemplateUsed(response,'home.html')