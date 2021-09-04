import os

from setuptools import setup

VERSION = "0.2"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="instapaper-to-sqlite",
    description="Save data from Instapaper to a SQLite database",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Benjamin Congdon",
    author_email="me@bcon.gdn",
    url="https://github.com/bcongdon/instapaper-to-sqlite",
    project_urls={
        "Source": "https://github.com/bcongdon/instapaper-to-sqlite",
        "Issues": "https://github.com/bcongdon/instapaper-to-sqlite/issues",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Database",
    ],
    keywords="instapaper sqlite export dogsheep",
    version=VERSION,
    packages=["instapaper_to_sqlite"],
    entry_points="""
        [console_scripts]
        instapaper-to-sqlite=instapaper_to_sqlite.cli:cli
    """,
    install_requires=[
        "click",
        "requests",
        "sqlite-utils~=3.17",
        "pyinstapaper @ git+https://github.com/bcongdon/pyinstapaper#egg=pyinstapaper",
    ],
    extras_require={"test": ["pytest"]},
    tests_require=["instapaper-to-sqlite[test]"],
)
