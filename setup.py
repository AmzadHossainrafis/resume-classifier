from setuptools import setup, find_packages
from typing import List

def get_requirements(filename): 
    '''
    args: 
        filename: name of the file containing the list of requirements
    returns:
        list of requirements
    summary: 
        reads the file and returns the list of requirements         
    
    '''
    requirements = [] 
    with open(filename, 'r') as f:
        for line in f.readlines():
            requirements.append(line.strip())
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements



setup(  
    name='resume classification',
    version='0.0.1',
    author='Amzad Hossein',
    author_email= 'amzad.rafi@northsouth.edu',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)