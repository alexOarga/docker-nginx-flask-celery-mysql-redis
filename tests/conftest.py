
import os, sys
import pytest
from os.path import join, dirname
from dotenv import load_dotenv

DOTENV_FILENAME = ".test.env"

sys.path.append("..")

dotenv_path = join(dirname(__file__), DOTENV_FILENAME)
load_dotenv(dotenv_path)

from src.app.app import app as _app
from src.app.database import db as _db

@pytest.fixture
def client():
    _app.config.from_object('src.app.config.TestingConfig')

    with _app.test_client() as client:
        _db.init_app(_app)
        with _app.app_context():
            _db.create_all()
        yield client
        with _app.app_context():
            _db.session.remove()
            _db.drop_all()

