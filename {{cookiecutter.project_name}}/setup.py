#!/usr/bin/env python
from setuptools import find_namespace_packages, setup

package_name = "dbt-{{ cookiecutter.directory_name }}"
# make sure this always matches dbt/adapters/{adapter}/__version__.py
package_version = "{{cookiecutter.project_version}}"
description = """The {{ cookiecutter.directory_name }} adapter plugin for dbt"""

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=description,
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.author_email }}",
    url="{{ cookiecutter.github_url }}",
    packages=find_namespace_packages(include=["dbt", "dbt.*"]),
    include_package_data=True,
    install_requires=[
        "dbt-core~={{ cookiecutter.dbt_version }}.",
    ],
)
