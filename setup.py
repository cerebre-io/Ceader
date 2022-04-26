from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ceader",
    version="0.0.1",
    license="MIT",
    author="Kamil Jankowski",
    author_email="kamil@cerebre.io",
    packages=find_packages(where="./ceader", exclude=("./tests",)),
    url="https://github.com/cerebre-io/ceader",
    keywords="Header",
    python_requiers=">=3.8",
    py_modules=["ceader"],  # Name of the python package
    package_dir={"": "ceader"},
    description="Tool for automatically adding a header to files in the form of a comment.",
    long_description=long_description,
    entry_points={
        "console_scripts": [
            "ceader=ceader.__main__:main",
        ]
    },
)

# python setup.py sdist
