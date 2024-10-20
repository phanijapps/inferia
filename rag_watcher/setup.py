from setuptools import setup, find_packages

setup(
    name='rag_watcher',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'common_util',
        'watchdog',
        'PyPDF2'
    ],
)

