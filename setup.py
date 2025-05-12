from setuptools import setup, find_packages

setup(
    name="misweb",
    version="0.0.1",
    description="Pentest websites according to owasp guidelines",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="kcancurly",
    url="https://github.com/kcancurly/misweb",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "bs4",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    entry_points={
        "console_scripts": [
            "misweb=misweb.main:main",
        ],
    },
)
