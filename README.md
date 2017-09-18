# cookiecutter-flask_api_template

v0.3.2

[![Build Status](https://travis-ci.org/bnbalsamo/cookiecutter-flask_api_template.svg?branch=master)](https://travis-ci.org/bnbalsamo/cookiecutter-flask_api_template)

My cookiecutter template for flask APIs

# Whats it get me?
- [Github](https://github.com/) integration
- [TravisCI](https://travis-ci.org/) integration
- [Coveralls](https://coveralls.io/) integration
- [Dockerization](https://www.docker.com/)
- A minimal README
- A virtual environment (python >= 3.3)
- A reasonable code template
- A flask API project setup with...
    - flask
    - flask_env
    - flask_restful
- Packages for common development tasks
    - [pip](https://pip.pypa.io/en/latest/)
    - [bumpversion](https://github.com/peritus/bumpversion)
    - [wheel](http://pythonwheels.com/)
    - [flake8](http://flake8.pycqa.org/en/latest/)
    - [coverage](https://coverage.readthedocs.io/en/coverage-4.4.1/)
    - [pytest](https://docs.pytest.org/en/latest/)
    - [twine](https://pypi.python.org/pypi/twine)
    - [check-manifest](https://github.com/mgedmin/check-manifest)

# Quickstart

- Requirements For These Instructions
    - [Cookiecutter](https://github.com/audreyr/cookiecutter)
    - [Github](https://github.com/) account
    - [TravisCI](https://travis-ci.org/) account
    - [Coveralls](https://coveralls.io/) account
- Steps
    - Create a github repo named $YOUR_PROJECT_NAME
    - Enable repository monitoring on Travis
    - Enable repository monitoring on coveralls
    - ```$ cookiecutter https://github.com/bnbalsamo/cookiecutter-flask_api_template```
    - Fill in the prompts
    - ```$ cd $YOUR_PROJECT_NAME```
    - ```$ source venv/bin/activate```
        - if python < 3.3 create your own venv here
    - ```$ pip install -r requirements_dev.txt```
    - ```$ git init```
    - ```$ git add */.*```
    - ```$ git commit -m "first commit"```
    - ```$ git remote add origin $YOUR_REPO_ADDRESS```
    - ```$ git push -u origin master```
    - Begin developing your api!

# Package Layout
- ```$slug_name/__init__.py``` 
    - Defines the "app" callable and handles injecting
        configuration via environmental variables and
        mounting the blueprint to an application object.
- ```$slug_name/blueprint/__init___.py```
    - Defines the application blueprint, endpoints,
        startup configuration (via the ```record``` decorated function),
        etc. Where the majority of the logic for the application
        resides.
- ```$slug_name/blueprint/exceptions.py```
    - Defines errors/exceptions that will be handled
        by the blueprints errorhandler decorated function.

## Why bother with a blueprint?

For more information about blueprints see [here](http://flask.pocoo.org/docs/0.12/blueprints/).

Formatting the API as a blueprint means that in the future anybody's application callable
can use ```Flask.register_blueprint()``` to run your API in concert with other blueprints,
if required.

# Functionalities

Any of the following can be run off the bat from the project root

* ```./quick_test.sh```: Run tests, generate coverage stats, run flake8
* ```py.test```: Run tests
* ```bumpversion $PART```: Bump the version number of the project
    * ```git push && git push --tags``` to upload/release to git
* ```autopep8 .```: Automatically fix some pep8 errors
* ``` check-manifest .```: Check that your manifest file is correct
    * the ```-c``` option will create one, if it doesn't exist
    * the ```-u``` option will update an existing file, or create one

## Uploading to pypi

I'll not hazard a short answer here, as there are too many options.

[This](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/) blog
entry provides a good breakdown of uploading a package to pypi. All of the referenced
tools should be installed by a ```pip -r requirements_dev.txt``` in your project
virtualenv.



Inspiration (and some code) taken from [audreyr's pypackage template](https://github.com/audreyr/cookiecutter-pypackage)

For a more general template for any python package see [bnbalsamo/cookiecutter-pypackage](https://github.com/bnbalsamo/cookiecutter-pypackage)
