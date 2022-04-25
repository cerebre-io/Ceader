from setuptools import find_packages, setup

setup(
    name="ceader",
    version="0.0.1",
    license="MIT",
    author="Kamil Jankowski",
    author_email="kamil@cerebre.io",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/cerebre-io/ceader",
    keywords="Header",
    install_requires=[],
    python_requiers=">=3.8",
)

# python setup.py sdist
