from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_margin_app/__init__.py
from custom_margin_app import __version__ as version

setup(
    name="custom_margin_app",
    version=version,
    description="An app to apply custom margin rate on items",
    author="ma7mod7osam",
    author_email="ma7mod7osam@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
