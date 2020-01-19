#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from sphinx.setup_command import BuildDoc

cmdclass = {"build_sphinx": BuildDoc}

name = "open-cv-test"
version = "0.2"

setup(
    name=name,
    version=version,
    install_requires=['opencv-contrib-python',
                      'sphinx',
                      'numpy',
                      'scipy',
                      'matplotlib',
                      'imutils',
                      'scikit-image'],
    packages=find_packages(),
    url="https://github.com/adjiap/open-cv-test",
    license="MIT License",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Win32 (MS Windows)",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
    ],
    author="Adji Arioputro",
    maintainer="Adji Arioputro",
    description="Test for running Machine Learning on Image Processing using OpenCV",
    command_options={
        "build_sphinx": {
            "project": ("setup.py", name),
            "version": ("setup.py", version),
        }
    },
)
