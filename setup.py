from setuptools import setup

setup(
    name="hisabkitab",
    version="1.0.0",
    description="A simple CLI tool to keep track of your payment dues",
    author="Taseng Mancheykhun",
    author_email="taseng9@gmail.com",
    url="https://github.com/TasengMancheykhun/hisabkitab",
    py_modules=["hisabkitab"],
    entry_points={
        "console_scripts": [
            "hisabkitab=hisabkitab:main",
        ],
    },
    install_requires=[
        "tabulate",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
