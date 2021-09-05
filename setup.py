"""
Module for installing application.
"""
import setuptools


def read_requiremets():
    """
    Function for reading project requirements.
    return:
        Massive project requirements
    """
    with open('requirements.txt') as file_req:
        return file_req.readlines()


setuptools.setup(
    name='department_app',
    version='0.1',
    packages=setuptools.find_packages(),
    description='department_app',
    install_requires=read_requiremets(),
    python_requires='>=3.7.9'
)