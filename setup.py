try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Plurk OAuth API',
    'author': 'Cheng-Lung Sung',
    'url': 'https://github.com/clsung/plurk-oauth',
    'download_url': 'http://pypi.python.org/pypi/plurk-oauth',
    'author_email': 'clsung@gmail.com',
    'version': '0.6.0',
    'install_requires': ['nose', 'oauth2'],
    'packages': ['plurk_oauth'],
    'scripts': ['bin/get_own_profile.py', 'bin/post_to_plurk.py'],
    'name': 'plurk-oauth'
}

setup(**config)
