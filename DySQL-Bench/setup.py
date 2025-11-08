# Copyright Sierra

from setuptools import find_packages, setup

setup(
    name="dysql_bench",
    version="0.1.0",
    description="The DySQL-Bench package",
    long_description=open("README.md").read(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "sqlparse"
    ],
)
