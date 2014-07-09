import unittest

import util


class TestUtil(unittest.TestCase):
    def test_image_path(self):
        image_path = util.image_path("sample")
        print(image_path)
        self.assertTrue(image_path.endswith("img/sample.png"))


if __name__ == "__main__":
    unittest.main()
