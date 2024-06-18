from setuptools import setup, find_packages
from os import path

__version__ = "0.0.1"

setup(
    name="diaux",
    version=__version__,
    description="",
    license="MIT",
    py_modules=[],
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
    author="Tom Röschinger",
    author_email="tom@roeschinger.de",
    include_package_data=True,
    package_data={"ecoli_gene_dict":["package_data/coli_gene_dict.pkl"]},
    zip_safe=False,
)