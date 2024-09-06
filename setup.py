from setuptools import setup, find_packages

setup(
    name="frieren",
    version="0.1.0",
    description="A package for file management operations with abstract base classes.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="nodashin",
    author_email="nodashin.jpn@gmail.com",
    url="https://github.com/nodashin6/frieren",
    packages=find_packages(),
    install_requires=[
        "pytest",
    ],
    extras_require={
        "dev": [
            "pytest",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
)
