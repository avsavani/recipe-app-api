from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@londonappdev.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(
			email=email,
			password=password
		)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        email="test@Example.com"
        user= get_user_model().objects.create_user(email,'123abc')
        self.assertEqual(user.email, email.lower())

    def tse_new_user_invalid_email(self):
        """"test creating user with no email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')

    def test_create_new_super_user(self):

        user = get_user_model().objects.create_superuser(
        'abc@example.com',
        'test123'
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
