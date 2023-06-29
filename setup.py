from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A package that helps users easily create functions to feed to GPT function calling API'

# Setting up
setup(
    name="funcOAI",
    version=VERSION,
    author="x5up0 aka.ryan",
    author_email="x5up0sbu@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', "OpenAI", "ChatGPT", "GPT API", "function calling API", "functions", "openai-gpt"],
    classifiers=[
        "Development Status :: 1 - production",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
