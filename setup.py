import setuptools

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except IOError:
        return ''


setuptools.setup(
    name="PySimpleGUI",
    version="4.60.4",
    author="PySimpleGUI",
    author_email="PySimpleGUI@PySimpleGUI.org",
    description="Python GUIs for Humans. Launched in 2018. It's 2022 & PySimpleGUI is an ACTIVE & supported project. Super-simple to create custom GUI's. 325+ Demo programs & Cookbook for rapid start. Extensive documentation. Main docs at www.PySimpleGUI.org. Fun & your success are the focus. Examples using Machine Learning (GUI, OpenCV Integration), Rainmeter Style Desktop Widgets, Matplotlib + Pyplot, PIL support, add GUI to command line scripts, PDF & Image Viewers. Great for beginners & advanced GUI programmers.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="GUI UI tkinter Qt WxPython Remi wrapper simple easy beginner novice student graphics progressbar progressmeter",
    url="https://github.com/PySimpleGUI/PySimpleGUI",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Topic :: Multimedia :: Graphics",
        "Operating System :: OS Independent"
    ),
    entry_points={
        'gui_scripts': [
            'psgissue=PySimpleGUI.PySimpleGUI:main_open_github_issue',
            'psgmain=PySimpleGUI.PySimpleGUI:_main_entry_point',
            'psgupgrade=PySimpleGUI.PySimpleGUI:_upgrade_entry_point',
            'psghelp=PySimpleGUI.PySimpleGUI:main_sdk_help',
            'psgver=PySimpleGUI.PySimpleGUI:main_get_debug_data',
            'psgsettings=PySimpleGUI.PySimpleGUI:main_global_pysimplegui_settings',
        ],},
)