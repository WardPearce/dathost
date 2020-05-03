import os
import re

from setuptools import setup


def get_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


def get_long_description():
    with open("README.md", encoding="utf8") as f:
        return f.read()


def get_version(package):
    with open(os.path.join(package, "__init__.py")) as f:
        return re.search(
            "__version__ = ['\"]([^'\"]+)['\"]", f.read()
        ).group(1)


setup(
    name='aiodathost',
    version=get_version("aiodathost"),
    url="https://github.com/WardPearce/aiodathost",
    description='Asynchronous dathost API wrapper.',
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author='WardPearce',
    author_email="wardpearce@protonmail.com",
    install_requires=get_requirements(),
    license='GPL v3',
    packages=['aiodathost'],
    python_requires='>=3.6',
    include_package_data=True,
    zip_safe=False
)
