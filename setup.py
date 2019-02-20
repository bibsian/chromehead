import os
from codecs import open
import subprocess

from setuptools import setup, find_packages
from setuptools.command.install import install


with open(os.path.join(os.getcwd(), "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


class BinaryInstall(install):

    def run(self):
        """Install binary dependencies from Makefile"""
        subprocess.Popen(["make"], stdout=subprocess.PIPE)
        install.run(self)


setup(
    name="chromehead",
    version="0.0.1",
    description="Headless chrome setup with aws lambda",
    long_description=long_description,
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
