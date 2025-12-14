import pytest
import requests_mock
from .. import api_client

@pytest.fixture
def mock_api():
    with requests_mock.Mocker() as m:
        yield m

def test_post_user_createWithArray_success(mock_api):
    endpoint = 'https://example.com/user/createWithArray'
    mock_api.post(endpoint, json={'status': 'ok'}, status_code=200)
    payload = {}
    response = api_client.post_user_createWithArray(payload)
    assert response.status_code == 200
    assert mock_api.called

def test_post_user_createWithArray_retry(mock_api):
    endpoint = 'https://example.com/user/createWithArray'
    mock_api.post(endpoint, [
        {'status_code': 500},
        {'status_code': 200}
    ])
    payload = {}
    response = api_client.post_user_createWithArray(payload)
    assert response.status_code == 200
    assert mock_api.call_count == 2
