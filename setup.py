# Create our machine learning application as a package with deployment
# Setting up the meta-data of our project

from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List:
    """Fetch the necessary list of requirements"""

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]


setup(
    name="ML_project",
    version="0.0.1",
    author="Serine",
    author_email="serine_md@hotmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),

)

