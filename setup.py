import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='git-apis',  
     version='0.6',
     scripts=['git-apis'] ,
     author="LakshmiSowmyaG",
     author_email="sowmyalakshmi35@gmail.com",
     description="A GitHub api utility package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Lakshmisowmya/git_apis_cli",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
