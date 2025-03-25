from setuptools import setup, find_packages

setup(
    name="find-replace-tool",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "find-replace=find_replace.main:main",
        ],
    },
    install_requires=[],
    author="nothader",
    author_email="h10xmous@gmail.coom",
    description="A command-line tool to find and replace words in all files within a folder.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nothader/replace",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
