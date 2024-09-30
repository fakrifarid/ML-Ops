from setuptools import find_packages, setup
from typing import List

HYP_E_DOT = '-e .'

def get_req(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    with open(file_path) as f_obj:
        req = f_obj.readlines()
        req = [r.strip() for r in req] 

    if HYP_E_DOT in req:
        req.remove(HYP_E_DOT)
    
    return req

setup(
    name='MLOps-Project',
    version='0.0.1',
    author='Fakri',
    author_email='fakrifarid@gmail.com',
    packages=find_packages(),
    install_requires=get_req('requirements.txt'),
)