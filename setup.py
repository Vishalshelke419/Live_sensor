from setuptools import find_packages,setup
# from typing import List
# from typing import List

def get_requirements()->list[str]:
    requirement_list = list[str] =[]
    return requirement_list





setup(
name = 'sensor',
version='0.0.1',
author ='Vishal',
author_email='vishalshelke419@gmail.com',
packages = find_packages(),
install_requires =get_requirements()#["pymongo"]

)