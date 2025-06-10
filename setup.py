from setuptools import setup, find_packages

setup(
    name="ri-excel",
    version="0.1.0",
    author="Ravetta Stefano",
    author_email="s.ravetta94@gmail.com",
    description="Utilities for excel management.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ShikaruAriki/ri-excel",
    packages=find_packages(),
    install_requires=[
        "build==1.2.2",
        "dataclass-wizard==0.35.0",
        "deepdiff==8.5.0",
        "openpyxl==3.1.5",
        "pytest==8.4.0",
        "setuptools==80.9.0",
        "tox==4.26.0",
        "twine==6.1.0",
        "wheel==0.46.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10.12',
    license="Apache-2.0",
)
