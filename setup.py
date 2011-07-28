from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pywhois',
      version=version,
      description="Whois querying and parsing of domain registration information.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='whois',
      author='Andrey Petrov',
      author_email='andrey.petrov@shazow.net',
      url='http://code.google.com/p/pywhois/',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
