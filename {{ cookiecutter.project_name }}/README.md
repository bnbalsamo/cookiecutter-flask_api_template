{% set has_docs_folder = cookiecutter.create_docs_folder == 'y' -%}


# {{cookiecutter.project_name}} [![v{{ cookiecutter.version }}](https://img.shields.io/badge/version-{{ cookiecutter.version }}-blue.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/releases)

[![Build Status](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}) [![Coverage Status](https://coveralls.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/badge.svg?branch=master)](https://coveralls.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}?branch=master){% if has_docs_folder %} [![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.github_repo_name }}/badge/?version=latest)](http://{{ cookiecutter.github_repo_name }}.readthedocs.io/en/latest/?badge=latest){% endif %}

{{ cookiecutter.short_description }}

{% if has_docs_folder %}
See the full documentation at https://{{cookiecutter.github_repo_name }}.readthedocs.io
{% endif %}

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
### GET
#### Parameters
* None
#### Returns
* JSON: {"status": "Not broken!"}

# Environmental Variables
* None

# Author
{{ cookiecutter.author }} <{{ cookiecutter.email }}>
