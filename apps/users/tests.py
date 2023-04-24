from django.test import TestCase
from validate_email import validate_email

from apps.users.factories import UserFactory
from apps.users.models import User


class UserModelTestCase(TestCase):
    def test_create_user(self):
        user = UserFactory.create()
        self.assertIsInstance(user, User)
        self.assertTrue(validate_email(user.email))
        self.assertTrue(user.check_password('password'))