import pytest
import requests_mock
from .. import api_client

@pytest.fixture
def mock_api():
    with requests_mock.Mocker() as m:
        yield m

def test_call_user_{username}_success(mock_api):
    endpoint = 'https://example.com/user/{username}'
    mock_api.delete(endpoint, json={'status': 'ok'}, status_code=200)
    payload = {}
    response = api_client.call_user_{username}(payload)
    assert response.status_code == 200
    assert mock_api.called

def test_call_user_{username}_retry(mock_api):
    endpoint = 'https://example.com/user/{username}'
    mock_api.delete(endpoint, [
        {'status_code': 500},
        {'status_code': 200}
    ])
    payload = {}
    response = api_client.call_user_{username}(payload)
    assert response.status_code == 200
    assert mock_api.call_count == 2
