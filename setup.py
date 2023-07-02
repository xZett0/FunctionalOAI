from setuptools import setup, find_packages
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text()

VERSION = '0.0.3'
DESCRIPTION = 'A package that helps users easily create functions to feed to GPT function calling API'
# Setting up
setup(
    name="funcOAI",
    version=VERSION,
    author="x5up0 aka.ryan",
    author_email="x5up0sbu@gmail.com",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[],
    keywords=['python', "OpenAI", "ChatGPT", "GPT API", "function calling API", "functions", "openai-gpt"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
