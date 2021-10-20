"""main blueprint views package"""
from flask import render_template

from app.main import bp


@bp.route("/")
def index():
    """Index route view

    Returns:
        string: Rendered index view
    """
    return render_template("index.html", title="Index")
