import unittest
import json
from os import environ
from os import urandom

# Defer any configuration to the tests setUp()
environ['{{ cookiecutter.slug_name|upper }}_DEFER_CONFIG'] = "True"

import {{ cookiecutter.slug_name }}


# Set up TESTING and DEBUG env vars to be picked up by Flask
{{ cookiecutter.slug_name }}.app.config['DEBUG'] = True
{{ cookiecutter.slug_name }}.app.config['TESTING'] = True
# Set a random secret key for testing
{{ cookiecutter.slug_name }}.app.config['SECRET_KEY'] = str(urandom(32))

# Duplicate app config settings into the bp, like the register would
{{ cookiecutter.slug_name }}.blueprint.BLUEPRINT.config['DEBUG'] = True
{{ cookiecutter.slug_name }}.blueprint.BLUEPRINT.config['TESTING'] = True
{{ cookiecutter.slug_name }}.blueprint.BLUEPRINT.config['SECRET_KEY'] = \
    {{ cookiecutter.slug_name }}.app.config['SECRET_KEY']


class Tests(unittest.TestCase):
    def setUp(self):
        # Perform any setup that should occur
        # before every test
        self.app = {{ cookiecutter.slug_name}}.app.test_client()


    def tearDown(self):
        # Perform any tear down that should
        # occur after every test
        del self.app

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
