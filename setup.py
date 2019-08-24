
from setuptools import setup

setup(name='example',
      version='0.1',
      description='Example',
      url='http://github.com/.../...',
      author='Example',
      author_email='example@example.com',
      license='...',
      packages=['example'],
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'example = example.thecode:main'
          ]}
      )
