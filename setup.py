# File: setup.py
# Date: 8-Mar-2020
#
# Update:

#
import re

from setuptools import find_packages
from setuptools import setup

packages = []
thisPackage = "rcsb.app.template"

with open("rcsb/app/template/__init__.py", "r") as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("Cannot find version information")

setup(
    name=thisPackage,
    version=version,
    description="RCSB Application Template",
    long_description="See:  README.md",
    author="John Westbrook",
    author_email="john.westbrook@rcsb.org",
    url="https://github.com/rcsb/py-rcsb_app_template",
    #
    license="Apache 2.0",
    classifiers=(
        "Development Status :: 3 - Alpha",
        # 'Development Status :: 5 - Production/Stable',
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ),
    entry_points={"console_scripts": []},
    #
    install_requires=["gunicorn >= 20.0.4", "uvicorn >= 0.11.5", "fastapi[all] >= 0.55.1", "aiofiles >= 0.5.0", "uvicorn >= 0.11.5", "pydantic >= 1.4", "rcsb.utils.io >= 0.76"],
    packages=find_packages(exclude=["rcsb.app.tests-*", "tests.*"]),
    package_data={
        # If any package contains *.md or *.rst ...  files, include them:
        "": ["*.md", "*.rst", "*.txt", "*.cfg"]
    },
    #
    test_suite="rcsb.app.tests-template",
    tests_require=["tox"],
    #
    # Not configured ...
    extras_require={"dev": ["check-manifest"], "test": ["coverage"]},
    # Added for
    command_options={"build_sphinx": {"project": ("setup.py", thisPackage), "version": ("setup.py", version), "release": ("setup.py", version)}},
    # This setting for namespace package support -
    zip_safe=False,
)
