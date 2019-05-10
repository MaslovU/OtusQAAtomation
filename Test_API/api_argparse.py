"""ARGPARSE"""
import argparse
import subprocess
ALL_SITE = 'python -m pytest -s -v /home/yury/PycharmProjects/Otus/Test_API'
DOG = 'python -m pytest -s -v /home/yury/PycharmProjects/Otus/Test_API/test_api_dogs.py'
OPENDB = 'python -m pytest -s -v /home/yury/PycharmProjects/Otus/Test_API/test_api_openbrewerydb.py'
CDNJS = 'python -m pytest -s -v /home/yury/PycharmProjects/Otus/Test_API/test_cdnjs_com.py'

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
    subprocess.run(ALL_SITE, shell=True)
else:
    assert URLS_ADDR in WEBSITES
    if URLS_ADDR == 'dog':
        subprocess.run(DOG, shell=True)
    if URLS_ADDR == 'openbrewerydb':
        subprocess.run(OPENDB, shell=True)
    if URLS_ADDR == 'cdnjs':
        subprocess.run(CDNJS, shell=True)
