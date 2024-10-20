from setuptools import setup, find_packages

setup(
    name='rag_watcher',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'watchdog',
        'PyPDF2'
    ],
)

