import unittest
from os import environ

# Defer configuration to the tests setUp()
environ['{{ cookiecutter.slug_name|upper }}_DEFER_CONFIG'] = True


class Tests(unittest.TestCase):
    def testFail(self):
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
