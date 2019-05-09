"""Argparse"""
import argparse

PARSER = argparse.ArgumentParser(description='Test URL throw Argparse')
PARSER.add_argument('--address',
                    dest='address',
                    action='store',
                    default=["https://ya.ru", "https://google.com", "https://mail.ru"],
                    help='urls = "https://ya.ru", "https://google.com", "https://mail.ru"')
ARGS = PARSER.parse_args()
URLS_ADDR = ARGS.address
URLS = ["https://ya.ru", "https://google.com", "https://mail.ru"]

if URLS_ADDR == URLS:
    print(URLS_ADDR)
else:
    assert URLS_ADDR in URLS
    print(URLS_ADDR)
