## UserSettings APIs

In addition to the JSON file format, new in release 4.50.0 is the support of INI files.

This file format is a little different than JSON.  INI Files have a concept of "Sections" where JSON does not.  In PySimpleGUI the UserSettings API calls and use of the `UserSettings` object are very similar. 

This demo shows how to use the UserSettings obiject to interface with these INI files.  It's as easy as this to write a setting value:

```python
settings = sg.UserSettings(use_config_file=True)
settings['Section']['setting'] = 'Some Value'
```

And reading is just as easy:

```python
value = settings['Section']['setting']
```



<iframe src='https://trinket.io/embed/pygame/56be5635d8?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>


