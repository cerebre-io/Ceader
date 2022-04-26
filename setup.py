from setuptools import find_packages, setup

setup(
    name="ceader",
    version="0.0.1",
    license="MIT",
    author="Kamil Jankowski",
    author_email="kamil@cerebre.io",
    packages=find_packages(),
    url="https://github.com/cerebre-io/ceader",
    keywords="Header",
    python_requiers=">=3.8",
    py_modules=["ceader"],  # Name of the python package
    package_dir={"": "ceader"},
)

# python setup.py sdist
