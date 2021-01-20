import unittest

from boyes_moore_substring import BoyesMooreSubstring


class Tests(unittest.TestCase):

    def test(self):
        txt = BoyesMooreSubstring("Ukraine has not died yet, neither glory, nor will,For us, brothers of the youth, we will laugh at our share!")
        self.assertEqual(txt.search(","), [24, 39, 49, 56, 79])
        self.assertEqual(txt.search("Ukraine"), [0])

        txt = BoyesMooreSubstring("Great teeth, Great mouth - that's how I call my teacher...")
        self.assertEqual(txt.search("Great"), [0, 13])
        self.assertEqual(txt.search("e"), [2, 7, 8, 15, 49, 53])




if __name__ == '__main__':
    unittest.main()