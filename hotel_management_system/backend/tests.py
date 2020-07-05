from rest_framework.test import APITestCase
from rest_framework.test import APIClient

# Create your tests here.
class TestApis(APITestCase):

	def test_create_visitor(self):
		response = self.client.get('http://localhost:8000/backend/abc/')
		self.assertEqual(response.status_code, 200)
		response = self.client.post('http://localhost:8000/backend/visitor/', {'name': 'PAPPY', 'email': "ABC@gmail.com"})
		self.assertEqual(response.status_code, 201)