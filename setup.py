from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Logic_Package",
    version="0.0.1",
    author="Guilherme",
    author_email="guiclovisi@gmail.com",
    description="A logic package for parsing, evaluating, classifying, and displaying logical expressions.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lovisi23/logpack",  # replace with your GitHub repo
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
