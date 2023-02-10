"""Main application module"""
import connexion
from flask import Flask

from config import get_environment_config_object
from database import db
from dependencies import ma
from routes.booking_route import booking_control, booking_manipulation
from routes.product_route import product_control, product_manipulation
from routes.user_route import user_control, user_manipulation


def create_app() -> Flask:
    """Factory method for Flask provider"""

    connexion_app = connexion.App(
        "__name__", specification_dir="./openapi/", options={'swagger_ui': True},
    )
    connexion_app.add_api("swagger.yml")

    application = connexion_app.app
    application.config.from_object(get_environment_config_object())

    db.init_app(application)
    ma.init_app(application)

    with application.app_context():
        db.create_all()
        return application


def add_routes(application: Flask) -> None:
    """Add routes for objects management purposes"""

    application.add_url_rule("/booking", methods=['GET', 'POST'], view_func=booking_control)
    application.add_url_rule(
        "/booking/<int:booking_id>", methods=['GET', 'PUT', 'DELETE'], view_func=booking_manipulation
    )

    application.add_url_rule("/product", methods=['GET', 'POST'], view_func=product_control)
    application.add_url_rule(
        "/product/<int:product_id>", methods=['GET', 'PUT', 'DELETE'], view_func=product_manipulation
    )

    application.add_url_rule("/user", methods=['GET', 'POST'], view_func=user_control)
    application.add_url_rule("/user/<int:user_id>", methods=['GET', 'PUT', 'DELETE'], view_func=user_manipulation)


app = create_app()

if __name__ == "__main__":
    """Entry point"""
    add_routes(app)
    app.run()
