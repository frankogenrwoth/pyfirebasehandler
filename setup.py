from setuptools import setup, find_packages

setup(
    name="your_module",
    version="0.1.0",
    description="A Python module for handling a Firebase database",
    author="Your Name",
    author_email="your@email.com",
    packages=find_packages(),
    install_requires=[
        "firebase-admin",
    ],
)
