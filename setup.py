import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='etl_package',
    version='0.1',
    scripts=['etl_package'] ,
    author="Jose Mari De Jesus",
    author_email="josemaribdejesus@gmail.com",
    description="An ETL pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/javatechy/dokr",
    packages=setuptools.find_packages(),
    classifiers=[
     "Programming Language :: Python :: 3",
     "License :: OSI Approved :: MIT License",
     "Operating System :: OS Independent",
    ]
)
