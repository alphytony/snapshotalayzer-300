from setuptools import setup

setup(
    name='snapshotalayzer-300',
    version='0.1',
    author="AM",
    author_email="am@gmail.com",
    decription="Snapshotalayzer 300 is a tool to manage AWS EC2 snapshots",
    packages=['alphy'],
    url="https://github.com/alphytony/snapshotalayzer-300",
    install_requires=['click','boto3'],
    entrypoints='''
    [console_scripts]
    alphy=alphy.file1:cli
    ''',

)