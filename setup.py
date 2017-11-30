from setuptools import setup, find_packages

setup(
    name='MessagingDispacher',
    keywords=['messaging', 'aws', 'pubsub'],
    description='A process engine to dispatch messages to various AWS services.',
    license='Apache License 2.0',
    install_requires=['boto3', 'pymysql', 'requests', 'ably'],
    version='0.0.0.2',
    author='CarPal Fleet',
    author_email='nick@carpal.me',
    packages=find_packages(),
    platforms='any',
)