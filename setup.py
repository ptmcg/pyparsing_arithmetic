# setup.py
from setuptools import setup, find_packages
from plusminus import __version__ as pm_version

setup(
    name="plusminus",
    version=pm_version,
    packages=find_packages(),

    install_requires=["pyparsing >= 2.4.6"],

    # metadata to display on PyPI
    author="Paul McGuire",
    author_email="ptmcg@austin.rr.com",
    description="""/
        plusminus is a module that builds on the pyparsing infixNotation helper method to build easy-to-code and 
        easy-to-use parsers for parsing and evaluating infix arithmetic expressions. plusminus's ArithmeticParser 
        class includes separate parse and evaluate methods, handling operator precedence, override with parentheses, 
        presence or absence of whitespace, built-in functions, and pre-defined and user-defined variables, functions, 
        and operators.
    """,
    keywords="infix notation arithmetic safe eval",
    url="http://example.com/HelloWorld/",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://bugs.example.com/HelloWorld/",
        "Documentation": "https://docs.example.com/HelloWorld/",
        "Source Code": "https://code.example.com/HelloWorld/",
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: General",
        "Topic :: Utilities",
    ]

)