"""Module to store environment configs"""

import os
from typing import Literal, Final, Type

_EnvT = Literal['DEVELOPMENT', 'TESTING']


class Config:
    """Parent file for environment configs"""

    ENV: Final[_EnvT] = os.getenv("ENV", default='DEVELOPMENT')
    CSRF_ENABLED: Final = True
    SECRET_KEY: Final = "this_is_a_secret_key"
    SQLALCHEMY_TRACK_MODIFICATIONS: Final = False


class DevelopmentConfig(Config):
    DEBUG: Final = True
    SQLALCHEMY_DATABASE_URI: Final = "sqlite:///dev.db"


class TestingConfig(Config):
    DEBUG: Final = True
    SQLALCHEMY_DATABASE_URI: Final = "sqlite:///test.db"


def get_environment_config_object() -> Type[Config]:
    """To supports several environments"""
    match Config.ENV:
        case 'DEVELOPMENT':
            return DevelopmentConfig
        case 'TESTING':
            return TestingConfig
