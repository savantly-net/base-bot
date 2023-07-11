from setuptools import setup, find_packages

setup(
    name='langchain-demo',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==1.1.2',
        'psycopg2==2.9.1',
        'langchain==0.1'
    ],
)
