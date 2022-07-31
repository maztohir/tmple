from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

path = os.path.dirname(os.path.realpath(__file__))
requirements_path = path + '/requirements.txt'

# Load main requirements file
if os.path.isfile(requirements_path):
    with open(requirements_path) as f:
        install_requires = f.read().splitlines()

setup(
    name="tmple",
    version="0.1.0",
    author="Muhamad Tohir",
    author_email="maztohir@gmail.com",
    description="General files or content generator, using template and data/variables.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maztohir/tmple",
    project_urls={
        "Bug Tracker": "https://github.com/maztohir/tmple/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Code Generators"
    ],
    packages=find_packages(exclude=['examples', 'tests']),
    python_requires=">=3.5",
    entry_points={"console_scripts": ["tmple=tmple.main:main"], },
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False
)