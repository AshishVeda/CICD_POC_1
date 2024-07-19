from django.test import TestCase
from .models import MyModel  # Replace with your actual model

class MyModelTest(TestCase):
    def test_str(self):
        my_model = MyModel(name="Test")
        
        self.assertEqual(str(my_model), "Test")
