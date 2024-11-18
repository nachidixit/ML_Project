from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]

        # Debug print statements to check the requirements list
        print("Requirements before removing '-e .':", requirements)
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
        # Final requirements list
        print("Requirements after processing:", requirements)
        
    return requirements

setup(
    name='mlproject_1',
    versions='0.0.1',
    author='Nachiket Dixit',
    author_email='erdnachiket@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('Requirements.txt')
)
