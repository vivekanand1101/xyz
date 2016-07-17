from setuptools import setup

import os

with open('requirements.txt', 'r') as f:
    packages = f.readlines()

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='xyz',
      version='1.0',
      description='My portfolio',
      author='Vivek Anand',
      author_email='vivekanand1101@gmail.com',
      url='https://github.com/vivekanand1101/xyz',
      install_requires=packages,
)

