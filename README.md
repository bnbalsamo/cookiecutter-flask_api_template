A cookiecutter template for a Flask RESTful API
v0.0.1

# Whats it get me?
- [Github](https://github.com/) integration
- [TravisCI](https://travis-ci.org/) integration
- [Coveralls](https://coveralls.io/) integration
- Preconfigured [bumpversion](https://github.com/peritus/bumpversion)
- A solid code template (in my opinion)
- [Dockerization](https://www.docker.com/)
- A debug launch script
- A minimal README

# Quickstart

- Requirements For These Instructions
    - [virtualenv](https://virtualenv.pypa.io/en/stable/)
    - [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
        - Properly configured for Project Management
    - [Github](https://github.com/) account
    - [TravisCI](https://travis-ci.org/) account
    - [Coveralls](https://coveralls.io/) account
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

Inspiration (and some code) taken from [audreyr's pypackage template](https://github.com/audreyr/cookiecutter-pypackage)
