from unittest import TestCase
from . import iterable_tools as it


class TestIterableTools(TestCase):
    def test_sliced_iter(self):
        otp = list(it.sliced_iter(range(5), slice_len=2))
        self.assertEqual(otp, [[0, 1], [2, 3], [4]])

        otp = list(it.sliced_iter(range(5), slice_len=2, allow_smaller_final_slice=False))
        self.assertEqual(otp, [[0, 1], [2, 3]])

        otp = list(it.sliced_iter(range(5), slice_len=1))
        self.assertEqual(otp, list([[el] for el in range(5)]))
