from setuptools import setup, find_packages

"""
You can install the module some_module_proj/setup.py and some_module.py
with
pip install ./tasks_proj/

 -> then, you can use the module in python interactive shell
 from tasks import some_func

 Caution!!!!!
You may meet situation with NoModuleFound error.
This is occured maybe...
1. Because of Pipfile.lock...
   When I delete Pipfile, I can pip install the module and NoModule error disappeared


"""
"""Minimal setup file for tasks project."""


setup(
    name='tasks',
    version='0.1.0',
    license='proprietary',
    description='Minimal Project Task Management',

    author='Brian Okken',
    author_email='Please use pythontesting.net contact form.',
    url='https://pragprog.com/book/bopytest',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=['click', 'tinydb', 'six'],
    extras_require={'mongo': 'pymongo'},

    entry_points={
        'console_scripts': [
            'tasks = tasks.cli:tasks_cli',
        ]
    },
)
