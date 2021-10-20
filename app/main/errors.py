"""main blueprint errors module"""
from flask import render_template

from app.main import bp


@bp.app_errorhandler(404)
def err_not_found(err):
    """404 not found error handler

    Returns:
        string: Rendered index view
    """
    return render_template("errors/404.html", err=err), 404
