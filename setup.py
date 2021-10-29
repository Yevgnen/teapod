# -*- coding: utf-8 -*-

import os
import re

from setuptools import find_packages, setup


def find_version(*paths):
    with open(os.path.join(os.path.dirname(__file__), *paths)) as f:
        text = f.read()
        match = re.search(
            r'^__version__ = (?P<quote>["\'])(?P<ver>[^"\']+)(?P=quote)', text, re.M
        )
        if not match:
            raise RuntimeError("Unable to find version string.")

        return match.group("ver")


VERSION = find_version("teapod", "__init__.py")


setup(
    name="teapod",
    description="Teapod.",
    version=VERSION,
    url="https://github.com/Yevgnen/teapod",
    author="Yevgnen Koh",
    author_email="wherejoystarts@gmail.com",
    packages=find_packages(exclude=("tests", "tests.*")),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "information=teapod.scripts.information:main",
            "poetry-add-latest=teapod.scripts.poetry_add_latest:main",
            "pip-update-all=teapod.scripts.pip_update_all:main",
            "org-import=teapod.scripts.org_import:main",
            "surge-to-ss=teapod.scripts.surge_to_ss:main",
        ],
    },
    install_requires=[
        "pytoml",
        "resworb",
        "rich",
    ],
    test_suite="tests",
    zip_safe=False,
)
