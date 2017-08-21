A cookiecutter template for a Flask RESTful API

# Quickstart

- Requirements For These Instructions
    - virtualenv
    - virtualenvwrapper
        - Properly configured for Project Management
    - Github account
    - TravisCI account
    - Coveralls account
- Steps
    - Create a github repo named $YOUR_PROJECT_NAME
    - Enable repository monitoring on Travis
    - Enable repository monitoring on coveralls
    - ```$ mkproject $YOUR_PROJECT_NAME```
    - ```$ pip install cookiecutter```
    - ```$ cookiecutter gh:https://github.com/bnbalsamo/cookiecutter-flask_api_template.git```
    - Fill in the prompts, be sure $YOUR_PROJECT_NAME matches the Github repository name
    - ```$ cd $YOUR_PROJECT_NAME```
    - ```$ git init```
    - ```$ git add *```
    - ```$ git commit -m "first commit"```
    - ```$ git push```

Inspiration (and some code) taken from https://github.com/audreyr/cookiecutter-pypackage
