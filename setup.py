from setuptools import setup, find_packages

setup(
    name="pyfirebasehandler",
    version="0.1.0",
    description="A Python module for handling a Firebase database",
    author="OGENRWOTH JIM FRANK",
    author_email="ogenrwoth.frank@email.com",
    packages=find_packages(),
    install_requires=[
        "firebase-admin",
    ],
)
