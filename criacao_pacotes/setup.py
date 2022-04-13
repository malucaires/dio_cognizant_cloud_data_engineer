from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

setup(
    name="fatorial",
    version="0.0.1",
    author="malucaires",
    author_email="malucairess@gmail.com",
    description="Calcula um fatorial de um número",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/malucaires/dio_cognizant_cloud_data_engineer/tree/main/criacao_pacotes",
    packages=find_packages(),
    python_requires='>=3.8',
)