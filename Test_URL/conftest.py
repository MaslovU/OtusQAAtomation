"""Conf test for URLS"""
import pytest


def pytest_addoption(parser):
    """Addoption"""
    parser.addoption(
        "--address",
        action="store",
        default=["https://ya.ru", "https://google.com", "https://mail.ru"]
    )


@pytest.fixture
def address(request):
    """Address"""
    return request.config.getoption("--address")
