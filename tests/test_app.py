import io
import pytest
import json
from flask import g, session


def test_example(client):

    result = client.get(
        '/hello/example',
    )
    assert result.status_code == 200
    data = result.get_data(as_text=True)
