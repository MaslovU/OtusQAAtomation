"""Dogs-API"""
import pytest


ENDPOINT1 = 'https://dog.ceo/api/breeds/list/all'
ENDPOINT2 = 'https://dog.ceo/api/breeds/image/random'
ENDPOINT3 = 'https://dog.ceo/api/breed/hound/images'
ENDPOINT4 = 'https://dog.ceo/api/breed/hound/list'
ENDPOINTS = [ENDPOINT1,
             ENDPOINT2,
             ENDPOINT3,
             ENDPOINT4
             ]


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_endpoints_post(client, endpoint):
    """POST"""
    response = client.do_post(endpoint)
    assert response.status_code != 300


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_endpoints_encoding(client, endpoint):
    """Encoding"""
    response = client.do_get(endpoint)
    assert isinstance(response.text, str)


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_status_code(client, endpoint):
    """Status Code"""
    response = client.do_get(endpoint)
    assert response.status_code == 200


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_headers(client, endpoint):
    """Headers"""
    response = client.do_get(endpoint)
    assert response.headers['Date']


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_headers_content_type(client, endpoint):
    """Content type"""
    response = client.do_get(endpoint)
    assert response.headers['Content-type'] == 'application/json'


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_headers_connection(client, endpoint):
    """Connection"""
    response = client.do_get(endpoint)
    assert response.headers['Connection'] == 'keep-alive'


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_reason(client, endpoint):
    """Reason"""
    response = client.do_get(endpoint)
    assert response.reason == 'OK'


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_cookies(client, endpoint):
    """Cookies"""
    response = client.do_get(endpoint)
    assert response.cookies


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_url(client, endpoint):
    """Url"""
    response = client.do_get(endpoint)
    assert response.url


@pytest.mark.parametrize('endpoints', ENDPOINTS)
def test_endpoint_json(client, endpoints):
    """Json"""
    j_s = client.do_json(endpoints)
    assert j_s['status'] == 'success'


@pytest.mark.parametrize('endpoint1', [ENDPOINT1])
def test_endpoint1_json(client, endpoint1):
    """Endpoint1"""
    j_s = client.do_json(endpoint1)
    assert j_s['message']['corgi'] == ['cardigan']
    assert j_s['message']['collie'] != ['borde']


@pytest.mark.parametrize('endpoint3', [ENDPOINT3])
def test_endpoint3_json(client, endpoint3):
    """Endpoint3"""
    j_s = client.do_json(endpoint3)
    assert j_s['message'][0] == 'https://images.dog.ceo/breeds/hound-afghan/n02088094_1003.jpg'


@pytest.mark.parametrize('endpoint4', [ENDPOINT4])
def test_endpoint4_json(client, endpoint4):
    """Endpoint4"""
    j_s = client.do_json(endpoint4)
    assert len(j_s['message']) == 6
