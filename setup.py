"""
Create a machine learning application as a package with deployment,
and up the meta-data of our project.
"""
from typing import List
from setuptools import find_packages, setup

HYPHEN_E_DOT="-e ."
def get_requirements(file_path: str) -> List:
    """Fetch the necessary list of requirements from the specified file path."""

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)   
    return requirements


setup(
    name="ML_project",
    version="0.0.1",
    author="Serine",
    author_email="serine_md@hotmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
