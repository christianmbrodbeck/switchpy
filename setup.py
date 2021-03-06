'''

To install, run::

    >>> python setup.py install

Then, run with::

    $ switchpy


Created on Jan 28, 2012
@author: Christian Brodbeck
christianmbrodbeck@gmail.com

'''

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup

setup(name='switchpy',
      version='0.2',
      description="Single script to change the default Python version",
      author="Christian Brodbeck",
      author_email="christianmbrodbeck@gmail.com",
      scripts=['switchpy'],
      )
