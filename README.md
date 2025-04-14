
<p align="center">
    <img height="250" src="https://pysimplegui.net/images/logos/Logo_Full_Transparent_Cropped.png">
  
</p>

![](https://PySimpleGUI.net/images/emojis/news_112.png)

# Two Important updates about PySimpleGUI 

![](https://PySimpleGUI.net/images/emojis/search_56.png)

## 1. New Package Location 

We were recently informed by PyPI that PySimpleGUI does not meet updated PyPI Terms of Service, that it needs to be removed, and hosted on a private server.  As a result, you’ll need to add a parameter to your pip install commands in order to access the PySimpleGUI private PyPI server.
The parameter to add is:  

`--extra-index-url https://PySimpleGUI.net/install `

### To force a reinstall of PySimpleGUI from new server

`python -m pip install --force-reinstall --extra-index-url https://PySimpleGUI.net/install PySimpleGUI`


### Performing an upgrade

This command will also install needed modules like rsa from PyPI automatically

The basic install/upgrade command **was**: 

`python -m pip install –-upgrade PySimpleGUI`  

or for Linux/Mac  

`python3 -m pip install –-upgrade PySimpleGUI`

The **new command** with the new parameter is:  

`python -m pip install --upgrade --extra-index-url https://PySimpleGUI.net/install  PySimpleGUI`

### Uninstall May Be Needed If Error

If you're getting errors, please uninstall PySimpleGUI entirely and install again using the new parameter.


### BUG - Commercial Key Expiration - Upgrade to 5.0.10

There is a bug in versions of PySimpleGUI older than 5.0.10 that causes an erroneous expired error when using a Commercial Developer key.  These keys do not expire and shouldn't not be generating the error.

A fix was released in version 5.0.10 on 2-Apr-2025.  **Please upgrade to version 5.0.10** so that your key doesn't generate an expiration error.

![](https://PySimpleGUI.net/images/emojis/wave_56.png)


## 2. PySimpleGUI Shutdown 

We gave it our best shot…. After 7 years of attempting to make the PySimpleGUI project sustainable, we are stopping the PySimpleGUI project.  

If you've followed the project over the years, you'll have read about the difficulties that all open-source projects face in generating enough income to pay for the project, seen the requests for sponsorships, and attempts to generate income via a Udemy course. There was not enough income to cover the costs of running a business and, of course, wasn’t able to generate any income for our small team.  This isn’t a sustainable situation.

## One Year Update PySimpleGUI 5 

It's been a little over a year since the release of PySimpleGUI 5.  Of the 100,000’s of Version 5 users, 10,000's of which were large corporate users, only 600 people paid the $99 for a commercial license.  

## End of PySimpleGUI Project

The revenue generated was not enough to cover the basic costs, so we've made the difficult decision to end the PySimpleGUI project.

## Support for Commercial Users 

Unlike traditional software companies, where stopping business means support ends immediately, we thought it would be classier to go the extra mile by continuing to provide support to Commercial License users this year as a way of saying "thank you" for your help in trying to give the project a viable future.  Please provide your Priority Support code or your submission will be automatically blocked.  We'll do the best we can to help with the limited resources we've got.

Your license doesn’t expire so you’ll be able to continue to run your applications at the end of the year we’re providing maintenance and beyond.  We’ll be distributing an offline version of the documentation so that you’ll have it for the future.

## Hobbyists

Hobbyists can continue to use PySimpleGUI 5 until their keys expire.  After that you'll need to switch to version 4, which you'll find 1,000s of copies on GitHub with at least 1 being community supported.

If you wish to use PySimpleGUI without the key expiring or want support, then you can buy a Commercial License which is good perpetually.

## Websites Availability

The PySimpleGUI registration and documentation websites will continue to operate for a couple of months to give commercial customers an opportunity to create distribution keys.  No new Hobbyist keys will be available.
 
![](https://PySimpleGUI.net/images/emojis/pray_56.png)
 
## Thank you to everyone 

PySimpleGUI has been an experience of a lifetime, and we’ve 
enjoyed watching & helping people create incredible applications.  

## Business Partnership Inquires 

If you're a business with a serious partnership that you wish to discuss, email mike@PySimpleGUI.com. 


