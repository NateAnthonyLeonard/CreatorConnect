import json
import pytest

# import app
from run_server import app

@pytest.fixture
def client():
    # Set testing mode
    app.config['TESTING'] = True

    # Start testing
    with app.test_client() as client:
        yield client


def test_site_root(client):
    """Test if the app runs."""

    rv = client.get('/')
    assert b'Success' in rv.data


def test_user_data(client):
    """Test if the returns user data."""

    rv = client.get('/api/users')
    res = json.loads(rv.data)
    assert len(res['data']) == 10


def test_user_pagination(client):
    """Test if the returns user data."""

    rv = client.get('/api/users/page/1')
    res = json.loads(rv.data)
    assert len(res['data']) == 9
