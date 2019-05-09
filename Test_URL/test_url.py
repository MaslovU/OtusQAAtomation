"""Urls"""
URLS = ["https://ya.ru", "https://google.com", "https://mail.ru"]


def web_site(address):
    """Address"""
    if address == URLS:
        address = address
    else:
        assert address in URLS
    return address


def test_urls(address):
    """Test URLS"""
    print(address)
