from flask import Flask, jsonify
from .blueprint import BLUEPRINT, __version__, __email__, __author__
from .blueprint.exceptions import Error
from flask_env import MetaFlaskEnv


class Configuration(metaclass=MetaFlaskEnv):
    ENV_PREFIX = '{{ cookiecutter.slug_name|upper }}_'
    DEBUG = False
    DEFER_CONFIG = False


app = Flask(__name__)


@app.errorhandler(Error)
def handle_errors(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


app.config.from_object(Configuration)

app.register_blueprint(BLUEPRINT)
