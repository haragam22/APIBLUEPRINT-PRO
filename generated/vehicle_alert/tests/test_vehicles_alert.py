import pytest
import requests_mock
from .. import api_client

@pytest.fixture
def mock_api():
    with requests_mock.Mocker() as m:
        yield m

def test_post_vehicles_alert_success(mock_api):
    endpoint = 'https://example.com/vehicles/alert'
    mock_api.post(endpoint, json={'status': 'ok'}, status_code=200)
    payload = {}
    response = api_client.post_vehicles_alert(payload)
    assert response.status_code == 200
    assert mock_api.called

def test_post_vehicles_alert_retry(mock_api):
    endpoint = 'https://example.com/vehicles/alert'
    mock_api.post(endpoint, [
        {'status_code': 500},
        {'status_code': 200}
    ])
    payload = {}
    response = api_client.post_vehicles_alert(payload)
    assert response.status_code == 200
    assert mock_api.call_count == 2
