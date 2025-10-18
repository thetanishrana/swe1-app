from django.test import TestCase


class BasicTest(TestCase):
    def test_basic(self):
        """Basic test to ensure test suite works"""
        self.assertEqual(1, 1)
