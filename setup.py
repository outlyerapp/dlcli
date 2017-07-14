"""
Command line utility for Dataloop.IO
"""

import os
import re
from setuptools import find_packages, setup


def fread(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version():
    version_path = "dlcli/_version.py"
    version_line = fread(version_path).strip()
    regex_pattern = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(regex_pattern, version_line, re.M)
    if mo:
        version = mo.group(1)
    else:
        raise RuntimeError("Unable to find version string in %s." % version_path)
    return version


dependencies = ['click', 'requests', 'pyyaml', 'terminaltables', 'termcolor', 'pysparklines', 'tqdm']

setup(
    name='dlcli',
    version=get_version(),
    url='https://github.com/dataloop/dlcli',
    download_url="https://github.com/dataloop/dlcli/tarball/v" + get_version(),
    license="Apache License, Version 2.0",
    author='Todd Radel',
    author_email='todd.radel@outlyer.com',
    description='Command line utility for Outlyer',
    long_description=fread('README.rst'),
    keywords="dataloop monitoring",
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'dlcli = dlcli.dlcli:main',
        ],
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
    ])
