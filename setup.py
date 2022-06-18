import re
from setuptools import find_packages, setup
from typing import List





#Declaring variables for setup functions
PROJECT_NAME="housing_predictor"
VERSION="0.0.4"
AUTHOR="Manas"
DESCRIPTION="This is First FSDS project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirements
    mention in requirements.txt.

    return: This function is going to return a list which contains name of libraies 
    mentione din requirements.txt file.
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")
    


setup(
name =PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires = get_requirements_list()

)

if __name__=="__main__":
    print(get_requirements_list())