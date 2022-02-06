import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="issuudl-saperoi",
    version="0.1.0",
    author="Saperoi",
    author_email="uesugi.sapero@gmail.com",
    description="A python-based individual page downloader for Issuu.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saperoi/issuudl-py",
    project_urls={
        "Bug Tracker": "https://github.com/saperoi/issuudl-py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPL 3 License",
        "Operating System :: OS Independent",
    ],
    packages=['issuudl'],
    python_requires=">=3.6",
)