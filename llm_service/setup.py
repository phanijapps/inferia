from setuptools import setup, find_packages

setup(
    name='inferia-llm-service',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'llma_cpp'
    ],
)

