"""CdnJs"""
import pytest

# Without any query parameters it will return the name and main file URL of every library on cdnjs
ENDPOINT1 = 'https://api.cdnjs.com/libraries'
# """To search, use"""
ENDPOINT2 = 'https://api.cdnjs.com/libraries?search=[1140]'
# """You can also "select" a certain library if you already know its name on CDNJS, e.g"""
ENDPOINT3 = 'https://api.cdnjs.com/libraries/6px'
# """ if you want to specify the info you want (recommended), use "fields" query"""
ENDPOINT4 = 'https://api.cdnjs.com/libraries/jquery?fields=name,filename,version'
# API will return minified result by default, if you wanna have a human readable result,
# try output=human like so
ENDPOINT5 = 'https://api.cdnjs.com/libraries?output=human'
ENDPOINT6 = 'https://api.cdnjs.com/libraries?search=[query]&output=human'
# """If you would like more data, use the fields parameter which takes comma-separated values"""
ENDPOINT7 = 'https://api.cdnjs.com/libraries?search=[query]&fields=version,description'
# """To get a list of all files for that library, use the assets field"""
ENDPOINT8 = 'https://api.cdnjs.com/libraries?search=[query]&fields=assets'
ENDPOINTS = [ENDPOINT1, ENDPOINT2, ENDPOINT3, ENDPOINT4, ENDPOINT5, ENDPOINT6, ENDPOINT7, ENDPOINT8]
ENDPOINTSCONTTYPE1 = [ENDPOINT1, ENDPOINT2, ENDPOINT3, ENDPOINT4, ENDPOINT7, ENDPOINT8]
ENDPOINTSCONTTYPE2 = [ENDPOINT5, ENDPOINT6]


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
    response = client.do_post(endpoint)
    assert response.headers['Date']


@pytest.mark.parametrize('endpoint', ENDPOINTSCONTTYPE1)
def test_headers_content_type1(client, endpoint):
    """Content type"""
    response = client.do_get(endpoint)
    assert response.headers['Content-type'] == 'application/json; charset=utf-8'


@pytest.mark.parametrize('endpoint', ENDPOINTSCONTTYPE2)
def test_headers_content_type2(client, endpoint):
    """Content type"""
    response = client.do_get(endpoint)
    assert response.headers['Content-type'] == 'text/html; charset=utf-8'


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


@pytest.mark.parametrize('endpoints', [ENDPOINT1])
def test_json_id(client, endpoints):
    """Json1"""
    j_s = client.do_json(endpoints)
    assert j_s['total'] == 3437
    assert j_s['results'][0]['name'] == '1140'
    assert j_s['results'][4]['name'] == '3Dmol'


@pytest.mark.parametrize('endpoints', [ENDPOINT2])
def test_json_name(client, endpoints):
    """Json2 Name '1140'"""
    j_s = client.do_json(endpoints)
    assert j_s['results'][0]['name'] == '1140'


@pytest.mark.parametrize('endpoints', [ENDPOINT3])
def test_json_library(client, endpoints):
    """Json3 you already know name of library"""
    j_s = client.do_json(endpoints)
    assert j_s['name'] == '6px'
    assert j_s['version'] == '1.0.3'
    assert j_s['repository']['url'] == 'https://github.com/6px-io/6px-js.git'


@pytest.mark.parametrize('endpoints', [ENDPOINT4])
def test_json_query(client, endpoints):
    """Json4 use "fields" query"""
    j_s = client.do_json(endpoints)
    assert j_s['name'] == 'jquery'
    assert j_s['version'] == '3.4.1'
    assert j_s['filename'] == 'jquery.min.js'


@pytest.mark.parametrize('endpoints', [ENDPOINT7])
def test_json_7(client, endpoints):
    """Json7"""
    j_s = client.do_json(endpoints)
    assert j_s['results'][0]['name'] == 'query-result'
    assert j_s['results'][0]['description'] == 'Rethinking the $'
    assert j_s['results'][0]['version'] == '0.2.0'


@pytest.mark.parametrize('endpoints', [ENDPOINT8])
def test_json_8(client, endpoints):
    """Json8"""
    j_s = client.do_json(endpoints)
    assert j_s['results']
    assert j_s['results'][0]['name'] == 'query-result'
    assert j_s['results'][0]['assets'][0]['version'] == '0.2.0'
    assert j_s['results'][0]['assets'][0]['files'][0] == 'query-result.amd.js'
    assert j_s['results'][0]['assets'][0]['files'][1] == 'query-result.js'
