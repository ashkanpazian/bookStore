from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class SignUp(TestCase) :
    def test_signUp(self) :
        response = self.client.get(reverse('signup'))
