try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Plurk OAuth API',
    'author': 'Cheng-Lung Sung',
    'url': 'https://github.com/clsung/plurk-oauth',
    'download_url': 'Where to download it.',
    'author_email': 'clsung@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'oauth2', 'json', 'httplib', 'urlparse'],
    'packages': ['plurk-oauth'],
    'scripts': ['bin/get_own_profile.py'],
    'name': 'plurk-oauth'
}

setup(**config)
