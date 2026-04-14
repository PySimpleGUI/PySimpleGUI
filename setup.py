import setuptools


def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except IOError:
        return ''


setuptools.setup(
    name="pysimplegui",
    version="6.0",
    author="PySimpleGUI",
    author_email="PySimpleGUI@PySimpleGUI.org",
    description="Python GUIs for Humans. Launched in 2018. NEW LGPL3 Version 6 released in 2026.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="GUI UI tkinter Qt WxPython Remi wrapper simple easy beginner novice student graphics progressbar progressmeter",
    url="https://github.com/PySimpleGUI/PySimpleGUI",
    packages=setuptools.find_packages(),
    install_requires=[ ],
    python_requires='>=3.6',
    license='GNU Lesser General Public License v3 (LGPLv3)',
    classifiers=[   "Development Status :: 5 - Production/Stable",
                    "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
                    "Intended Audience :: Developers",
                    "Operating System :: OS Independent",
                    "Framework :: PySimpleGUI",
                    "Programming Language :: Python :: 3",
                    "Programming Language :: Python :: 3.6",
                    "Programming Language :: Python :: 3.7",
                    "Programming Language :: Python :: 3.8",
                    "Programming Language :: Python :: 3.9",
                    "Programming Language :: Python :: 3.10",
                    "Programming Language :: Python :: 3.11",
                    "Programming Language :: Python :: 3.12",
                    "Programming Language :: Python :: 3.13",
                    "Programming Language :: Python :: 3.14",
                    "Programming Language :: Python :: 3.15",
                    "Topic :: Multimedia :: Graphics",
                    "Topic :: Software Development :: User Interfaces",],
    entry_points={'gui_scripts': [  'psgmain=PySimpleGUI.PySimpleGUI:_main_entry_point',
                                    'psghome=PySimpleGUI.PySimpleGUI:_main_entry_point',
                                    'psghelp=PySimpleGUI.PySimpleGUI:main_sdk_help',
                                    'psgver=PySimpleGUI.PySimpleGUI:main_get_debug_data',
                                    'psgsettings=PySimpleGUI.PySimpleGUI:main_global_pysimplegui_settings',], },
)
