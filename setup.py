import os
import subprocess

from setuptools import setup, find_packages
from setuptools.command.install import install


class BinaryInstall(install):

    def run(self):
        """Install binary dependencies from Makefile"""
        subprocess.Popen(["make"], stdout=subprocess.PIPE)
        install.run(self)


setup(
    name="chromehead",
    version="0.0.1",
    description="Headless chrome setup with aws lambda",
    long_description="Headless chrome base class, binaries for chromium, all installable from git",
    url="https://github.com/bibsian/chromehead",

    author="Andrew Bibian",

    classifiers=[
        "Intended Audience :: Data Engineers",
        "Programming Language :: Python :: 3.6",
    ],

    packages=find_packages(exclude=["tests"]),
    install_requires=["selenium==2.53.6"],
    cmdclass={"install": BinaryInstall} 

)
