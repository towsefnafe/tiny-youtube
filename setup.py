import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    #Here is the module name.
    name="tinyyoutube",
 
    #version of the module
    version="0.0.3",
 
    #Name of Author
    author="Towsef Hassan Nafe",
 
    #your Email address
    author_email="towsef.nafe@nafe.com",
 
    #Small Description about module
    description="Extract data from youtube",
 
    long_description=long_description,
 
    #Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",
 
    #Any link to reach this module, if you have any webpage or github profile
    url="https://github.com/towsefnafe/tinyyoutube",
    packages=setuptools.find_packages(),
 
    #classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)