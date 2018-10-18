import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysimplegui-exemaker",
    version="1.0.0",
    author="PySimpleGUI.org",
    author_email="info@PySimpleGUI.org",
    description="A GUI Front-end to PyInstaller",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['PyInstaller', 'pysimplegui'],
    url="https://github.com/MikeTheWatchGuy/PySimpleGUI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows ",
    ],
)