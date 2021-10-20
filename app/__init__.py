"""Main Application package"""
from flask import Flask

from config import config


def create_app(config_name):
    """App factory function

    Args:
        config_name (string): App configuration to use

    Returns:
        class: Instance of Flask application
    """
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    from app.main import bp as main_bp

    app.register_blueprint(main_bp)

    return app
