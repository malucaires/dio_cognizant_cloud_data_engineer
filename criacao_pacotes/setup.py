from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="fatorial",
    version="0.0.1",
    author="malucaires",
    author_email="malucairess@gmail.com",
    description="Calcula um fatorial de um número",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link"
    packages=find_packages(),
    python_requires='>=3.8',
)