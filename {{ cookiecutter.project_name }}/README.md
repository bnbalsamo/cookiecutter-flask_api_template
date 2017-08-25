# {{cookiecutter.project_name}}

v{{ cookiecutter.version }}

[![Build Status](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.slug_name }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.slug_name }}) [![Coverage Status](https://coveralls.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.slug_name }}/badge.svg?branch=master)](https://coveralls.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.slug_name }}?branch=master) 
{{ cookiecutter.short_description }}

# Debug Quickstart
Set environmental variables appropriately
```
./debug.sh
```

# Docker Quickstart
Inject environmental variables appropriately at either buildtime or runtime
```
# docker build . -t {{ cookiecutter.slug_name }}
# docker run -p 5000:80 {{ cookiecutter.slug_name }} --name my_{{ cookiecutter.slug_name }}
```

# Endpoints
## /
### Parameters
* None
### Returns
* JSON: {"status": "Not broken!"}

# Environmental Variables
* None

# Author
{{ cookiecutter.author }} <{{ cookiecutter.email }}>
