from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

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
    entry_points={"console_scripts": ["tmple=tmple.main:main"],},
    include_package_data=True,
)