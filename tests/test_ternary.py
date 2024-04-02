from unittest import TestCase
from ternary import tif, tlif


class TestTernary(TestCase):
    def test_true(self):
        self.assertTrue(tif(True, True, False))

    def test_false(self):
        self.assertFalse(tif(False, True, False))

    def test_lazy_true(self):
        self.assertTrue(tlif(True, lambda: True, lambda: False))

    def test_lazy_false(self):
        self.assertFalse(tlif(False, lambda: True, lambda: False))

    def test_lazyness(self):
        self.mutable = []

        def false():
            self.mutable.append(1)

        def true():
            self.mutable.append(2)

        self.assertTrue(sum(self.mutable) == 0)

        tlif(True, true, false)
        self.assertTrue(sum(self.mutable) == 2)

        tlif(False, true, false)
        self.assertTrue(sum(self.mutable) == 3)

    def test_boolish_type(self):
        self.assertTrue(tif("1", True, False))
        self.assertFalse(tif("", True, False))
