"""Conftest"""
import json
import pytest
import requests


class APIClient:
    """APIClient"""
    def __init__(self, address=''):
        self.address = address

    @staticmethod
    def do_get(endpoint, verify_ssl=False):
        """Get-method"""
        url = '/'.join([endpoint])
        return requests.get(url, verify=verify_ssl)

    @staticmethod
    def do_post(endpoint, data=None, verify_ssl=False):
        """POST-method"""
        url = '/'.join([endpoint])
        return requests.post(url, data, verify=verify_ssl)

    @staticmethod
    def do_json(endpoint, verify_ssl=False):
        """JSON-method"""
        url = '/'.join([endpoint])
        req = requests.get(url, verify=verify_ssl)
        return json.loads(req.text)


def pytest_addoption(parser):
    """parser"""
    parser.addoption('--address', action='store')


@pytest.fixture
def client(request):
    """client"""
    return APIClient(request.config.getoption('--address'))
