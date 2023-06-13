from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyfirebasehandler",
    version="9.9.9",
    description="A Python module for handling a Firebase database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="OGENRWOTH JIM FRANK",
    author_email="ogenrwoth.frank@email.com",
    packages=find_packages(),
    install_requires=[
        "firebase-admin",
        "google-cloud-firestore",
    ],
)
