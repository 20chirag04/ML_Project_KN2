from setuptools import find_packages,setup
from typing import List 

def get_requirements() -> List[str]:
    '''
        This Function will return the list of requirements
    '''
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
        ## Read lines from the files
            lines = file.readlines()
            ## process each line
            for line in lines:
                requirement = line.strip()
                ## Ignore empty lines and -e .
                if requirement and requirement != '-e .' :
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirement.txt does not found')
    
    return requirement_lst
    
setup(
    name = "NetworkSecurity",
    version="0.0.1",
    author="Chirag Sharma",
    author_email="20chiragsharma04@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)