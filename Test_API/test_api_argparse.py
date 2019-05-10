"""ARGPARSE"""
import argparse
DOG = 'python -m pytest -s -v /home/yury/PycharmProjects/Otus/Test_API/test_api_dogs.py'
OPENDB = 'python -m pytest -s -v /home/yury/PycharmProjects/Otus/Test_API/test_api_openbrewerydb.py'
CDNJS = '(venv) yury@yury-Aspire-ES1-523:~/PycharmProjects/Otus$ python Test_API/test_cdnjs_com.py'
ALL_SITE = 'python -m pytest -s -v /home/yury/PycharmProjects/Otus/Test_API'

PARSER = argparse.ArgumentParser(description='Test API throw Argparse')
PARSER.add_argument('--site',
                    dest='site',
                    action='store',
                    default=["dog", "openbrewerydb", "cdnjs"],
                    help='websites: "dog", "openbrewerydb", "cdnjs"')
ARGS = PARSER.parse_args()
URLS_ADDR = ARGS.site
WEBSITES = ["dog", "openbrewerydb", "cdnjs"]


if URLS_ADDR == WEBSITES:
    print(ALL_SITE)
else:
    assert URLS_ADDR in WEBSITES
    if URLS_ADDR == 'dog':
        print(DOG)
    if URLS_ADDR == 'openbrewerydb':
        print(OPENDB)
    if URLS_ADDR == 'cdnjs':
        input(CDNJS)
