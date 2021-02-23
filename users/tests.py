from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from .models import User


class UserModelTests(TestCase):
    """
    longtime_no_see() returns True for user whose last_login is more than 30 days ago
    """

    def test_longtime_no_see(self):
        last_login = timezone.now() - timedelta(days=40)
        test_user = User(last_login=last_login)
        self.assertIs(test_user.longtime_no_see(), True)

        last_login = timezone.now() - timedelta(days=20)
        test_user = User(last_login=last_login)
        self.assertIs(test_user.longtime_no_see(), False)
