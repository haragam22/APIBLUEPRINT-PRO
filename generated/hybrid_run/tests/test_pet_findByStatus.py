import pytest
import requests_mock
from .. import api_client

@pytest.fixture
def mock_api():
    with requests_mock.Mocker() as m:
        yield m

def test_call_pet_findByStatus_success(mock_api):
    endpoint = 'https://example.com/pet/findByStatus'
    mock_api.get(endpoint, json={'status': 'ok'}, status_code=200)
    payload = {}
    response = api_client.call_pet_findByStatus(payload)
    assert response.status_code == 200
    assert mock_api.called

def test_call_pet_findByStatus_retry(mock_api):
    endpoint = 'https://example.com/pet/findByStatus'
    mock_api.get(endpoint, [
        {'status_code': 500},
        {'status_code': 200}
    ])
    payload = {}
    response = api_client.call_pet_findByStatus(payload)
    assert response.status_code == 200
    assert mock_api.call_count == 2
