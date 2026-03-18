from setuptools import setup, find_packages

setup(
    name="rebin-cli",   
    version="1.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "rebin=rebin.cli:main",
        ],
    },
    author="Mehmet",
    description="Terminal Trash Tool with ASCII UI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
)