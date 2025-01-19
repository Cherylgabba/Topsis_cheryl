from setuptools import setup, find_packages

DESCRIPTION = 'Implementation of Topsis'

try:
    with open('README.md', 'r', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

VERSION = '1.0.3'

setup(
    name="Topsis-Cheryl-102217206",
    version=VERSION,
    author="Cheryl",
    author_email="cgabba_be22@thapar.edu",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    project_urls={
        'Project Link': 'https://github.com/Cherylgabba/Topsis_cheryl'
    },
    keywords=['Topsis', 'Topsis-Cheryl-102217206', 'Cheryl', 'Topsis-Cheryl', '102217206'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)
