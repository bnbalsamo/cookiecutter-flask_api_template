import unittest
import json
from os import environ

# Defer any configuration to the tests setUp()
environ['{{ cookiecutter.slug_name|upper }}_DEFER_CONFIG'] = "True"

import {{ cookiecutter.slug_name }}


class Tests(unittest.TestCase):
    def setUp(self):
        # Perform any setup that should occur
        # before every test
        self.app = {{ cookiecutter.slug_name}}.app.test_client()

    def tearDown(self):
        # Perform any tear down that should
        # occur after every test
        pass

    def testPass(self):
        self.assertEqual(True, True)

    def testVersionAvailable(self):
        x = getattr({{ cookiecutter.slug_name }}, "__version__", None)
        self.assertTrue(x is not None)

    def testVersion(self):
        version_response = self.app.get("/version")
        self.assertEqual(version_response.status_code, 200)
        version_json = json.loads(version_response.data.decode())
        api_reported_version = version_json['version']
        self.assertEqual(
            {{ cookiecutter.slug_name }}.blueprint.__version__,
            api_reported_version
        )


if __name__ == "__main__":
    unittest.main()
