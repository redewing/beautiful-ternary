from unittest import TestCase
from ternary import tif


class TestTernary(TestCase):
    def test_true(self):
        self.assertTrue(tif(True, True, False))

    def test_false(self):
        self.assertFalse(tif(False, True, False))
