
fromm setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='htmltojson',
    version='0.1.0',
    author='Eszter Bolla',
    author_email='bolla.eszter@gmail.com',
    description='A utility for convert rss and atom links from html to json',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bollae/htmltojason',
    packages=find_packages('src')
)
