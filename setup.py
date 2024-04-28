from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='DiffieHellmanProtocol',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/Bart3kD/Diffie-Hellman/',
    license='MIT',
    author='Bartek',
    author_email='bartolini.160608@gmail.com',
    description='A simple diffie hellman protocol adaptation using sockets',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
    ],
)