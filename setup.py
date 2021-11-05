import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


setup(
    name="python_svg",
    version="0.0.3",
    description="Create Dynamic SVGs using Python3",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/KrishnaKanth1729/PySVG",
    author="KrishnaKanth1729",
    author_email="rkrishnakanth1729@gmail.com",
    packages=find_packages(),
    keywords=['python', 'svg'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)