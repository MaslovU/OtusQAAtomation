"""Urls"""
URLS = ["https://ya.ru", "https://google.com", "https://mail.ru"]


def test_urls(address):
    """Test URLS"""
    if address == URLS:
        print(address)
    else:
        assert address in URLS
        print(address)
