try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config={
    'description':'season ticket breaker in Python',
    'author': 'Joe Zhou',
    'url': 'https://github.com/joezhouOxford/points.git',
    'download_url':'https://github.com/joezhouOxford/points.git',
    'author_email': 'joezhou.contact@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['points'],
    'scripts': [],
    'name': 'points'
}

setup(**config)