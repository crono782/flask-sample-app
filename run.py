"""Application entrypoint module"""
import os

from app import create_app

app = create_app(os.environ.get("FLASK_CONFIG", "default"))


@app.shell_context_processor
def make_shell_context():
    """Function to create usable shell context

    Returns:
        dict: Dictionary of objects to import into shell context
    """
    # pylint: disable=use-dict-literal
    return dict()


@app.cli.command()
def deploy():
    """CLI function to do app deployment stuff"""
    print('deploy stuff')
