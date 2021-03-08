import os
from setuptools import setup, find_packages


with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = f.readlines()

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="pytappium",
    install_requires=requirements
)

