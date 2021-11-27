import io, sys
import pytest
import json
from flask import g, session

sys.path.append("..")
from src.app.tasks.tasks import example_task


def test_celery_task():
    example_task("example")
