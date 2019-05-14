"""Package setup and distribution module"""

# standard lib.
import setuptools


with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="stress-yo-api",
    version="0.0.1",
    author="oagutu",
    description="A python packaging tool to help stress test, and analyse APIs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oagutu/sya",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)