"""OpenBrewerydb"""
import pytest

ENDPOINT1 = 'https://api.openbrewerydb.org/breweries'
"""FILTER_BREWERIES_BY_STATE"""
ENDPOINT2 = 'https://api.openbrewerydb.org/breweries?by_state=new_york'
"""Filter breweries by name"""
ENDPOINT3 = 'https://api.openbrewerydb.org/breweries?by_name=cooper'
"""Filter breweries by a tag"""
ENDPOINT4 = 'https://api.openbrewerydb.org/breweries?by_tag=patio'
"""Filter breweries by name and state"""
ENDPOINT5 = 'https://api.openbrewerydb.org/breweries?by_name=cooper&by_state=new_york'
"""Filter breweries by state and sort by type then by name in decending order"""
ENDPOINT6 = 'https://api.openbrewerydb.org/breweries?by_state=ohio&sort=type,-name'
"""Pagination & Per Page (default per page is 20; max per page is 50)"""
ENDPOINT7 = 'https://api.openbrewerydb.org/breweries?page=2&per_page=30'
"""GET_A_BREWERY"""
ENDPOINT8 = 'https://api.openbrewerydb.org/breweries/5494'
"""AUTOCOMPLETE"""
ENDPOINT9 = 'https://api.openbrewerydb.org/breweries/autocomplete?query=dog'
"""SEARCH"""
ENDPOINT10 = 'https://api.openbrewerydb.org/breweries/search?query=dog'
ENDPOINTS = [ENDPOINT1, ENDPOINT2, ENDPOINT3, ENDPOINT4, ENDPOINT5,
             ENDPOINT6, ENDPOINT7, ENDPOINT8, ENDPOINT9, ENDPOINT10]


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


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_headers_content_type(client, endpoint):
    """Content type"""
    response = client.do_get(endpoint)
    assert response.headers['Content-type'] == 'application/json; charset=utf-8'


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
    """Json"""
    j_s = client.do_json(endpoints)
    assert j_s[0]['id'] == 2
    assert j_s[0]['name'] == 'Avondale Brewing Co'
    assert j_s[0]['city'] != 'Moscow'


@pytest.mark.parametrize('endpoints', [ENDPOINT2])
def test_json_id_2(client, endpoints):
    """Json breweries?by_state=new_york"""
    j_s = client.do_json(endpoints)
    assert j_s[0]['id'] == 4581
    assert j_s[0]['name'] == 'Adirondack Toboggan Company Microbrewery'
    assert j_s[0]['state'] == 'New York'


@pytest.mark.parametrize('endpoints', [ENDPOINT3])
def test_json_id_3(client, endpoints):
    """Json breweries?by_name=cooper"""
    j_s = client.do_json(endpoints)
    assert j_s[0]['id'] == 58
    assert j_s[0]['name'] == 'Cooper Landing Brewing Company, LLC.'
    assert j_s[0]['state'] == 'Alaska'


@pytest.mark.parametrize('endpoints', [ENDPOINT4])
def test_json_id_4(client, endpoints):
    """Json breweries?by_tag=patio"""
    j_s = client.do_json(endpoints)
    assert j_s[0]['id'] == 5494
    assert j_s[0]['name'] == 'MadTree Brewing'
    assert j_s[0]['tag_list'] == ['patio']


@pytest.mark.parametrize('endpoints', [ENDPOINT5])
def test_json_id_5(client, endpoints):
    """Json by_name=cooper&by_state=new_york"""
    j_s = client.do_json(endpoints)
    assert j_s[0]['id'] == 4674
    assert j_s[0]['name'] == 'Coopers Cave Ale Co'
    assert j_s[0]['state'] == 'New York'


@pytest.mark.parametrize('endpoints', [ENDPOINT6])
def test_json_id_6(client, endpoints):
    """Json by name in decending order for example W->V"""
    j_s = client.do_json(endpoints)
    assert j_s[0]['name'] == 'Willoughby Brewing Co'
    assert j_s[1]['name'] == 'Weasel Boy Brewing Co  LLC'
    assert j_s[2]['name'] == 'Wadsworth Brewing Company'
    assert j_s[3]['name'] == 'Valley Vineyards Winery & Cellar Dweller Brewing'


@pytest.mark.parametrize('endpoints', [ENDPOINT8])
def test_json_id_7(client, endpoints):
    """Json '/breweries/5494'"""
    j_s = client.do_json(endpoints)
    assert j_s['id'] == 5494
    assert j_s['brewery_type'] == 'regional'


@pytest.mark.parametrize('endpoints', [ENDPOINT9])
def test_json_id_8(client, endpoints):
    """Json autocomplete?query=dog"""
    j_s = client.do_json(endpoints)
    name1 = j_s[0]['name']
    name3 = j_s[10]['name']
    assert 'Dog' in name1, name3


@pytest.mark.parametrize('endpoints', [ENDPOINT9])
def test_json_id_9(client, endpoints):
    """Json autocomplete?query=dog2"""
    names = []
    j_s = client.do_json(endpoints)
    for i in (0, 14):
        name = j_s[i]['name']
        names.append(name)
    for name in names:
        assert 'Dog' in name


@pytest.mark.parametrize('endpoints', [ENDPOINT10])
def test_json_id_10(client, endpoints):
    """Json query=dog"""
    j_s = client.do_json(endpoints)
    name = j_s[0]['name']
    assert 'Dog' in name
    assert j_s[0]['id'] == 530
