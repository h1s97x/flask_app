from setuptools import setup, find_packages

setup(
    name='sayhello',
    version='0.1.0',
    author='h1s97x',
    description='Hello World example for Flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'initdb = sayhello.commands.commands:initdb',
            'forge = sayhello.commands.commands:forge',
        ],
    },
)