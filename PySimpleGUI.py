#!/usr/bin/python3

version = __version__ = "4.18.0.2  Unreleased - Print and MLine.Print fixed sep char handling, popup_get_date"

port = 'PySimpleGUI'

#  888888ba           .d88888b  oo                     dP           .88888.  dP     dP dP
#  88    `8b          88.    "'                        88          d8'   `88 88     88 88
# a88aaaa8P' dP    dP `Y88888b. dP 88d8b.d8b. 88d888b. 88 .d8888b. 88        88     88 88
#  88        88    88       `8b 88 88'`88'`88 88'  `88 88 88ooood8 88   YP88 88     88 88
#  88        88.  .88 d8'   .8P 88 88  88  88 88.  .88 88 88.  ... Y8.   .88 Y8.   .8P 88
#  dP        `8888P88  Y88888P  dP dP  dP  dP 88Y888P' dP `88888P'  `88888'  `Y88888P' dP
#                 .88                         88
#                 .88                         88
#             d8888P                          dP


#  __                                      __
# /  |                                    /  |
# $$ |        ______    ______    ______  $$ |
# $$ |       /      \  /      \  /      \ $$ |
# $$ |      /$$$$$$  |/$$$$$$  | $$$$$$  |$$ |
# $$ |      $$    $$ |$$ |  $$ | /    $$ |$$ |
# $$ |_____ $$$$$$$$/ $$ \__$$ |/$$$$$$$ |$$ |
# $$       |$$       |$$    $$ |$$    $$ |$$ |
# $$$$$$$$/  $$$$$$$/  $$$$$$$ | $$$$$$$/ $$/
#                     /  \__$$ |
#                     $$    $$/
#                      $$$$$$/


"""
Copyright 2018, 2019, 2020 PySimpleGUI.org

OK, let's get the bullshit out of the way

This software is available for your use under a MODIFIED LGPL3+ license

This notice, these first 100 lines of code shall remain unchanged

 #     #                                        
 ##   ##  ####  #####  # ###### # ###### #####  
 # # # # #    # #    # # #      # #      #    # 
 #  #  # #    # #    # # #####  # #####  #    # 
 #     # #    # #    # # #      # #      #    # 
 #     # #    # #    # # #      # #      #    # 
 #     #  ####  #####  # #      # ###### #####  


888      .d8888b.  8888888b.  888      .d8888b.          
888     d88P  Y88b 888   Y88b 888     d88P  Y88b         
888     888    888 888    888 888          .d88P         
888     888        888   d88P 888         8888"    888   
888     888  88888 8888888P"  888          "Y8b. 8888888 
888     888    888 888        888     888    888   888   
888     Y88b  d88P 888        888     Y88b  d88P         
88888888 "Y8888P88 888        88888888 "Y8888P"          


And just what is that?  Well, it's LPGL3+ and these FOUR simple stipulations.
1. These and all comments are to remain in this document
2. You will not post this software in a repository or a location for others to download from:
   A. Unless you have made 10 lines of changes
   B. A notice is posted with the code that it is not the original code but instead derived from an original
3. Forking is OK and does NOT require any changes as long as it is obvious forked and stated on the page
   where your software is being hosted.  For example, GitHub does a fantastic job of indicating if a repository
   is the result of a fork.
4. The "Official" version of PySimpleGUI and the associated documentation lives on two (and **only** two) places:
       1. GitHub - (http://www.PySimpleGUI.com) currently pointing at:
          https://github.com/PySimpleGUI/PySimpleGUI
       2. PyPI - pip install PySimpleGUI is the customary way of obtaining the latest release

       THE official documentation location is:
          Read the Docs (via http://www.PySimpleGUI.org).  Currently is pointed at: 
          https://pysimplegui.readthedocs.io/en/latest/
   If you've obtained this software in any other way, then those listed here, then SUPPORT WILL NOT BE PROVIDED.

-----------------------------------------------------------------------------------------------------------------

How about having FUN with this package??  Terrible note to begin this journey of actually having fun making
GUI based applications so I'll try to make it up to you.

The first bit of good news for you is that literally 100s of pages of documentation await you.  And nearly 200
Demo Programs have been written as a "jump start" mechanism to get your running as quickly as possible.

Some general bits of advice:
Upgrade your software!  pip install --upgrade --no-cache-dir PySimpleGUI
If you're thinking of filing an Issue or posting a problem, Upgrade your software first
There are constantly something new and interesting coming out of this project so stay current if you can 

The FASTEST WAY to learn PySimpleGUI is to begin to play with it, and to read the documentation.
http://www.PySimpleGUI.org
http://Cookbook.PySimpleGUI.org

The User Manual and the Cookbook are both designed to paint some nice looking GUIs on your screen within 5 minutes of you deciding to PySimpleGUI out.

"""

# do the Python 2 or 3 check so the right tkinter stuff can get pulled in
import sys

if sys.version_info[0] >= 3:
    import tkinter as tk
    from tkinter import filedialog
    from tkinter.colorchooser import askcolor
    from tkinter import ttk
    import tkinter.scrolledtext as tkst
    import tkinter.font
else:  # Do NOT remove any of these regardless of what your IDE or lint says. They are transformed in the 3 to 2 process
    import Tkinter as tk
    import tkFileDialog
    import ttk
    import tkColorChooser
    import tkFont
    import ScrolledText

import datetime
import time
import pickle
import calendar
import textwrap
import inspect
# from typing import List, Any, Union, Tuple, Dict    # because this code has to run on 2.7 can't use real type hints.  Must do typing only in comments
from random import randint
import warnings
from math import floor
from math import fabs
from functools import wraps
from subprocess import run, PIPE
from threading import Thread
import calendar as cal
import itertools
import os

warnings.simplefilter('always', UserWarning)

g_time_start = 0
g_time_end = 0
g_time_delta = 0


# These timer routines are to help you quickly time portions of code.  Please this TimerStart call at the point
# you want to start timing and the TimerStop at the end point. As you can see, TimerStop prints the time delta in ms.
def TimerStart():
    """ Time your code easily.... start the timer. """
    global g_time_start

    g_time_start = time.time()


def TimerStop():
    """ Time your code easily.... stop the timer and print the number of ms since the timer start """
    global g_time_delta, g_time_end

    g_time_end = time.time()
    g_time_delta = g_time_end - g_time_start
    print((g_time_delta * 1000))



def _timeit(func):
    """
    Put @_timeit as a decorator to a function to get the time spent in that function printed out

    :param func: Decorated function
    :return: Execution time for the decorated function
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('{} executed in {:.4f} seconds'.format( func.__name__, end - start))
        return result

    return wrapper

_timeit_counter = 0
MAX_TIMEIT_COUNT = 1000
_timeit_total = 0

def _timeit_summary(func):
    """
    Same as the timeit decorator except that the value is shown as an averave
    Put @_timeit_summary as a decorator to a function to get the time spent in that function printed out

    :param func: Decorated function
    :return: Execution time for the decorated function
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        global _timeit_counter, _timeit_total

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        _timeit_counter += 1
        _timeit_total += end - start
        if _timeit_counter > MAX_TIMEIT_COUNT:
            print('{} executed in {:.4f} seconds'.format( func.__name__, _timeit_total/MAX_TIMEIT_COUNT))
            _timeit_counter = 0
            _timeit_total = 0
        return result

    return wrapper


"""
    Welcome to the "core" PySimpleGUI code....

    It's a mess.... really... it's a mess internally... it's the external-facing interfaces that
    are not a mess.  The Elements and the methods for them are well-designed.
    PEP8 - this code is far far from PEP8 compliant. 
    It was written PRIOR to learning that PEP8 existed. 

    I'll be honest.... started learning Python in Nov 2017, started writing PySimpleGUI in Feb 2018.
    Released PySimpleGUI in July 2018.  I knew so little about Python that my parameters were all named
    using CamelCase.  DOH!  Someone on Reddit set me straight on that.  So overnight I renamed all of the
    parameters to lower case.  Unfortunately, the internal naming conventions have been set.  Mixing them
    with PEP8 at this moment would be even MORE confusing.

    Code I write now, outside PySimpleGUI, IS PEP8 compliant.  

    The variable and function naming in particular are not compliant.  There is
    liberal use of CamelVariableAndFunctionNames, but for anything externally facing, there are aliases
    available for all functions.  If you've got a serious enough problem with 100% PEP8 compliance
    that you'll pass on this package, then that's your right and I invite you to do so.  However, if
    perhaps you're a practical thinker where it's the results that matter, then you'll have no
    trouble with this code base.  There is consisency however.  

    I truly hope you get a lot of enjoyment out of using PySimpleGUI.  It came from good intentions.
"""

# ----====----====----==== Constants the user CAN safely change ====----====----====----#

# Base64 encoded GIF file
DEFAULT_BASE64_ICON = b'R0lGODlhIQAgAPcAAAAAADBpmDBqmTFqmjJrmzJsnDNtnTRrmTZtmzZumzRtnTdunDRunTRunjVvnzdwnzhwnjlxnzVwoDZxoTdyojhzozl0ozh0pDp1pjp2pjp2pzx0oj12pD52pTt3qD54pjt4qDx4qDx5qTx5qj16qj57qz57rD58rT98rkB4pkJ7q0J9rEB9rkF+rkB+r0d9qkZ/rEl7o0h8p0x9pk5/p0l+qUB+sEyBrE2Crk2Er0KAsUKAskSCtEeEtUWEtkaGuEiHuEiHukiIu0qKu0mJvEmKvEqLvk2Nv1GErVGFr1SFrVGHslaHsFCItFSIs1COvlaPvFiJsVyRuWCNsWSPsWeQs2SQtGaRtW+Wt2qVuGmZv3GYuHSdv3ievXyfvV2XxGWZwmScx2mfyXafwHikyP7TPP/UO//UPP/UPf/UPv7UP//VQP/WQP/WQf/WQv/XQ//WRP7XSf/XSv/YRf/YRv/YR//YSP/YSf/YSv/ZS//aSv/aS/7YTv/aTP/aTf/bTv/bT//cT/7aUf/cUP/cUf/cUv/cU//dVP/dVf7dVv/eVv/eV//eWP/eWf/fWv/fW/7cX/7cYf7cZP7eZf7dav7eb//gW//gXP/gXf/gXv/gX//gYP/hYf/hYv/iYf/iYv7iZP7iZf/iZv/kZv7iaP/kaP/ka//ma//lbP/lbv/mbP/mbv7hdP7lcP/ncP/nc//ndv7gef7gev7iff7ke/7kfv7lf//ocf/ocv/odP/odv/peP/pe//ofIClw4Ory4GszoSszIqqxI+vyoSv0JGvx5OxyZSxyZSzzJi0y5m2zpC10pi715++16C6z6a/05/A2qHC3aXB2K3I3bLH2brP4P7jgv7jh/7mgf7lhP7mhf7liv/qgP7qh/7qiP7rjf7sjP7nkv7nlv7nmP7pkP7qkP7rkv7rlv7slP7sl/7qmv7rnv7snv7sn/7un/7sqv7vq/7vrf7wpv7wqf7wrv7wsv7wtv7ytv7zvP7zv8LU48LV5c3a5f70wP7z0AAAACH5BAEAAP8ALAAAAAAhACAAAAj/AP8JHEiwoMGDCA1uoYIF4bhK1vwlPOjlQICLApwVpFTGzBk1siYSrCLgoskFyQZKMsOypRyR/GKYnBkgQbF/s8603KnmWkIaNIMaw6lzZ8tYB2cIWMo0KIJj/7YV9XgGDRo14gpOIUBggNevXpkKGCDsXySradSoZcMmDsFnDxpEKEC3bl2uXCFQ+7emjV83bt7AgTNroJINAq0wWBxBgYHHdgt0+cdnMJw5c+jQqYNnoARkAx04kPEvS4PTqBswuPIPUp06duzcuYMHT55wAjkwEahsQgqBNSQIHy582D9BePTs2dOnjx8/f1gJ9GXhRpTqApFQoDChu3cOAps///9D/g+gQvYGjrlw4cU/fUnYX6hAn34HgZMABQo0iJB/Qoe8UxAXOQiEg3wIXvCBQLUU4mAhh0R4SCLqJOSEBhhqkAEGHIYgUDaGICIiIoossogj6yBUTQ4htNgiCCB4oIJAtJTIyI2MOOLIIxMtQQIJIwQZpAgwCKRNI43o6Igll1ySSTsI7dOECSaUYOWVKwhkiyVMYuJlJpp0IpA6oJRTkBQopHnCmmu2IBA2mmQi5yZ0fgJKPP+0IwoooZwzkDQ2uCCoCywUyoIW/5DDyaKefOLoJ6LU8w87pJgDTzqmDNSMDpzqYMOnn/7yTyiglBqKKKOMUopA7JgCy0DdeMEjUDM71GqrrcH8QwqqqpbiayqToqJKLwN5g45A0/TAw7LL2krGP634aoopp5yiiiqrZLuKK+jg444uBIHhw7g+MMsDFP/k4wq22rririu4xItLLriAUxAQ5ObrwzL/0PPKu7fIK3C8uxz0w8EIIwzMP/cM7HC88hxEzBBCBGGxxT8AwQzDujws7zcJQVMEEUKUbPITAt1D78OSivSFEUXEXATKA+HTscC80CPSQNGEccQRYhjUDzfxcjPPzkgnLVBAADs='

DEFAULT_BASE64_LOADING_GIF = b'R0lGODlhQABAAKUAAAQCBJyenERCRNTS1CQiJGRmZLS2tPTy9DQyNHR2dAwODKyqrFRSVNze3GxubMzKzPz6/Dw6PAwKDKSmpExKTNza3CwqLLy+vHx+fBQWFLSytAQGBKSipERGRNTW1CQmJGxqbLy6vPT29DQ2NHx6fBQSFKyurFRWVOTi5HRydPz+/Dw+PP7+/gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQJCQAsACwAAAAAQABAAAAG/kCWcEgsGo/IpHLJbDqf0CjxwEmkJgepdrvIAL6A0mJLdi7AaMC4zD4eSmlwKduuCwNxdMDOfEw4D0oOeWAOfEkmBGgEJkgphF8ph0cYhCRHeJB7SCgJAgIJKFpnkGtTCoQKdEYGEmgSBlEqipAEEEakcROcqGkSok8PkGCBRhNwcrtICYQJUJnDm0YHASkpAatHK4Qrz8Nf0mTbed3B3wDFZY95kk8QtIS2bQ29r8BPE8PKbRquYBuxpJCwdKhBghUrQpFZAA8AgX2T7DwIACiixYsYM2rc+OSAhwrZOEa5QGHDlw0dLoiEAqEAoQK3VjJxCQmEzCUhzgXciOKE/gIFJ+4NEXBOAEcPyL6UqEBExLkvIjYyiMOAyICnAAZs9IdGgVWsWjWaTON1yAGsUTVOTUOhyLhh5TQi7cqUyIVzKjmiYCBBQtAjNAnZvKmk5cuYhJVc6DAWZd7ETTx6CAm5suXLRQY4sPDTQoqwmIlAADE2DYi0oUUQhbQC8WUQ5wZf9oDVA58KdaPAflqgTgMEXxA0iPIB64c6I9AgiFL624Y2FeLkbtJ82HM2tNPYfmLBOHLlUQJ/6z0POADhUa4+3V7HA/vw58gfEaFBA+qMIt6Su9/UPAL+F4mwWxwwJZGLGitp9kFfHzgAGhIHmhKaESIkB8AIrk1YBAQmDJiQoYYghijiiFAEAQAh+QQJCQApACwAAAAAQABAAIUEAgSEgoREQkTU0tRkYmQ0MjSkpqTs6ux0cnQUEhSMjozc3ty0trT09vRUUlRsamw8OjwMCgxMSkx8fnwcGhyUlpTk5uS8vrz8/vwEBgSMioxERkTc2txkZmQ0NjS0srT08vR0dnQUFhSUkpTk4uS8urz8+vxsbmw8Pjz+/v4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG/sCUcEgsGo/IpHLJbDqf0Kh0Sl0aPACAx1DtOh/ZMODhLSMNYjHXzBZi01lPm42BizHz5CAk2YQGSSYZdll4eUUYCHAhJkhvcAWHRiGECGeEa0gNAR4QEw1TA4RZgEcdcB1KBwViBQdSiqOWZ6wABZlIE3ATUhujAAJsj2FyUQK/wWbDcVInvydsumm8UaKjpWWrra+whNBtDRMeHp9UJs5pJ4aSXgMnGxsI2Oz09fb3+Pn6+/xEJh8KRjBo1M/JiARiEowoyIQAIQIMk1T4tXAfBw6aEI5KAArfgjcFFhj58CsLg3zDIhXRUBKABnwc4GAkoqDly3vWxMxLQbLk/kl8tbKoJAJCIyGO+RbUCnlkxC8F/DjsLOLQDsSISRREEBMBKlYlDRgoUMCg49ezaNOqVQJCqtm1Qy5IGAQgw4YLcFOYOGWnA8G0fAmRSVui5c+zx0omM2NBgwYLUhq0zPKWSIMFHCojsUAhiwjIUHKWnPpBAF27H5YEEBOg2mQA80A4ICQBRBJpWVpDAfHabAMUv1BoFkJChGcSUoCXREGEUslZRxoHAB3lQku8Qg7Q/ZWB26HAdgYLmTi5Aru9hPwSqdryKrsLG07fNTJ7soN7IAZwsH2EfUn3ETk1WUVYWbDdKBlQh1Usv0D3VQPLpOHBcAyBIAFt/K31AQrbBqGQWhtBAAAh+QQJCQAyACwAAAAAQABAAIUEAgSEgoTEwsREQkTk4uQsLiykoqRkYmQUEhTU0tRUUlT08vS0srSMjox8enwMCgzMysw8OjwcGhxcWlz8+vy8urxMSkzs6uysqqxsamzc2tyUlpQEBgSMiozExsTk5uQ0NjSkpqRkZmQUFhRUVlT09vS0trSUkpR8fnwMDgzMzsw8PjwcHhxcXlz8/vy8vrxMTkzc3tz+/v4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG/kCZcEgsGo/IpHLJbDqf0Kh0Sq1ar8nEgMOxqLBgZCIFKAMeibB6aDGbB2u1i+Muc1xxJSWmoSwpdHUcfnlGJSgIZSkoJUptdXCFRRQrdQArhEcqD24PX0wUmVMOlmUOSiqPXkwLLQ8PLQtTFCOlAAiiVyRuJFMatmVpYIB1jVEJwADCWCWBdsZQtLa4artmvaO2p2oXrhyxVCWVdSvQahR4ViUOZAApDuaSVhQaGvHy+Pn6+/z9/v8AAzrxICJCBBEeBII6YOnAPYVDWthqAfGIgGQC/H3o0OEDEonAKPL7IKHMCI9GQCQD0S+AmwBHVAJjyQ/FyyMgJ/YjUAvA/ggCFjFqDNAxSc46IitOOlqmRS6lQwSIABHhwAuoWLNq3cq1ogcHLVqgyFiFAoMGJ0w8teJBphsQCaWcaFcGwYkwITiV4hAiCsNSB7B4cLYXwpMNye5WcVEgWZkC6ZaUSAQMwUMnFRybqdCEgWYTVUhpBrBtSQfNHZC48BDCgIfIRKxpxrakAWojLjaUNCNhA2wZsh3TVuLZMWgiJRTYgiFKtObSShbQLZUinohkIohkHs25yYnERVRo/iSDQmPHBdYi+Wsp6ZDrjrNH1Uz2SYPpKRocOZ+sQJEQhLnBgQFTlHBWAyZcxoJmEhjRliVw4cMfMP4ZQYEADpDQggMvJ/yWB3zYYQWBZnFBxV4p8mFVAgzLqacQBSf0ZNIJLla0mgGu1ThFEAAh+QQJCQAqACwAAAAAQABAAIUEAgSUkpRERkTMyswkIiTs6uy0trRkZmQ0MjTU1tQcGhykpqRUVlT09vTEwsQsKix8enwMCgycnpzU0tS8vrw8Ojzc3txcXlz8/vwEBgSUlpRMSkzMzswkJiT08vS8urxsamw0NjTc2twcHhysqqz8+vzExsQsLix8fnxkYmT+/v4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG/kCVcEgsGo/IpHLJbDqf0Kh0Sq1ar8tEAstdWk4AwMnSLRfBYbF5nUint+tu2w2Ax5OFghMdPt2TBg9hDwZMImgnIn9HH3QAhUxaTw0LCw1WHY4dax6CAA8eVAWOYXplEm4SoqQApl2oaapUmXSbZgW0HaFUBo6QZpQLu1UGub+LWHnIy8zNzs/Q0dLTzSYQFxcoDtRMAwiOCCZJDRwDl88kGawZC0YlEOoAGRDnywPx6wNEHnxpJ8N/SvRjdaLEkAOsDiyjwMrRByEe8NHJADAOhIZ0IAgZgFHcIgYY3TAQYqIjMpAhw4xUEXFdxTUXUwLQKAQhKYXIGsl8CHGg/piXa0p4wvgAA5EG8MLMq4esZEiPRRoMMMGU2QKJbthxQ2LiG51wW5NgcACBwQUIFIyGXcu2bdgGGjZ06LBBQ1UoJg5UqHAAKhcTBByN8OukRApHKe5OcYA1TQbCTC6wuoClQeCGIxQjcYBxm5UAKQM8kdyQshUBKQU8CYERwZURKUc88crKNZIJZRlAmIAEdkjZTkhPPtLAppsDd1GHVO2Ec0PPREoodyTAIBHQIUWPHm5EA0btQxoowKgAaJISwtNcsF7ENyvgRCg0Vgq5iYMDISqkoIDEQkoyRZjgXhojQHcHRyHpYwRcAhBAgAB2LeNfSACyNaBgbqngXUPgGLElHSvVZahCA4fRcYFma3GQGwQciAhNEAAh+QQJCQAwACwAAAAAQABAAIUEAgSEgoTEwsRERkTk4uQkIiSkpqRsamwUEhTU0tT08vSUkpRUUlQ0MjS0trQMCgzMyszs6ux8enwcGhzc2tz8+vyMioxMTkysrqw8OjwEBgSEhoTExsRMSkzk5uQkJiSsqqxsbmwUFhTU1tT09vSUlpRUVlQ0NjS8vrwMDgzMzszs7ux8fnwcHhzc3tz8/vz+/v4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG/kCYcEgsGo/IpHLJbDqf0Kh0Sq1ar9hs1sNiebRgowsBACBczJcKA1K9wkxWucxSVgKTOUC0qcCTcnN1SBEnenoZX39iZAApaEcVhod6J35SFSgoJE4EXYpHFpSUAVIqBWUFKlkVIqOHIpdOJHlzE5xXEK+UHFAClChYBruHBlAowMLEesZPtHoiuFa6y2W9UBAtZS2rWK3VsVIkmtJYosuDi1Ekk68n5epPhe4R8VR3rnN8svZTLxAg2vDrR7CgwYMItZAo0eHDhw4l4CVMwgHVoRbXjrygMOLNQQEaXmnISARErQnNCFbQtqsFPBCUUtpbUG0BkRe19EzwaG9A/rUBREa8GkHQIrEWRCgMJcjyKJFvsHjG87kMaMmYBWkus1nEwEmZ9p7tmqBA44gRA/uhCDlq5MQlHJrOaSHgLZOFAwoUGBDRrt+/gAMLhkMiwYiyV0iogCARCwUTbDWYoHBPQmQJjak4eEDpgQMpKxpQarAiCwXOox4QhXLg1YEsDIgxgKKALSUNiKvUXpb5CLVXJKeoqNatCQdiwY2QyH0kAfEnu9syJ0Jiw4dUGxorqNb7SOtRr4+saDeH9BETsqOEHl36yIVXF46MQN15NRQSlstowIzk+K7kMGzW2WdUKAABB90FQEwp8l1g2wX2xfOda0oolkB3YWyw4GBCIfgHHIdCvDdKByAKsd4h5pUIAwkBsNRCdioWoUB7MRoUBAAh+QQJCQAuACwAAAAAQABAAIUEAgSEhoTMzsxMSkykpqQcHhz08vRkYmQUEhSUlpS0trTc3twsLixsbmwMCgzU1tSsrqz8+vycnpyMjoxUUlQkJiRsamwcGhy8vrw0NjR0dnQEBgTU0tSsqqz09vRkZmQUFhScmpy8urzk5uQ0MjR0cnQMDgzc2ty0srT8/vykoqSUkpRUVlQsKiz+/v4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG/kCXcEgsGo8RRWlAaSgix6h0Sp2KKoCstiKqer/fkHasTYDP6KFoQ25303BqBNsmV6DxvBFSr0P0gEMNfW0WgYEDhGQDRwsTFhYTC4dTiYpajEQeB2xjBx6URxaXWoZDHiR9JKChRHykAH9DB4oHcQIlJQJRc6R3Qwukk2gcnRscUSKkb0ITpBNpo6VSCZ11ZkS0l7Zo0lmmUQp0YxUKRtq1aQLGyFNJDUxOeEXOl9DqDbqhJ6QnrYDo6nD7l8cDgz4MWBHMYyBglgMGFh46MeHDhwn+JGrcyLGjx48gO3rg8CBiSDQnWBhjkfFkFQUO2jgwF8UACgUmPz6IWcfB/oMjGBBkQYABJAVFFIwYMDEGQc6NBqz1USjk1RhZHAWQ2kUERRsUHrVe4jpk6RgTTzV6IEVVCAamAEwU/XiUUNIjNlGk5bizj0+XVGDKpAl4yoO6WSj8LOzFgwAObRlLnky5suXLEg2o0FCCwF40KU48SEGwg1AtCDrk6XAhywUCrTr0UZ1GNhnYhwycbuMUdGsyF0gHkqBIApoHfRYDKqGoAcrkhzQoKoEmAog2IIRHSSEiQAAR84wQJ2Qcje0xuKOcaDGmhfIiZuughUPg9+spI66TATEiyvnbeaTwwAPhidLHB1IQsBsACKS3kX7YTWGABLlI8BlBEShSIGUQIO6HmRDekIHgh/lh19+HLjzA3hbvfZiEdwpoh+KMjAUBACH5BAkJACYALAAAAABAAEAAhQQCBISGhMzKzERCRDQyNKSmpOzq7GRiZBQSFHRydJyanNTW1LS2tPz6/Dw6PAwODLSytPTy9GxubBweHHx6fKSipNze3AQGBIyKjMzOzExOTDQ2NKyqrOzu7GRmZBQWFHR2dJyenNza3Ly+vPz+/Dw+PP7+/gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAb+QJNwSCwaj8ikcslsmjoYx+fjwHSc2KyS8QF4vwiGdjxmXL5or5jMXnYQ6TTi2q4bA/F4wM60UDZTGxQWRw55aRt8SSQUhyAkRQ+HaA+KRw0akwAaDUSSmgCVRg0hA1MDCp1ZIKAACUQbrYlFBrGIBlgirV4LQ3ige0QNtnEbqkwSuwASQ2+aD3RDCpoKTgTKBEQMmmtEhpMlTp+tokMMcGkP3UToh+VL46DvQh0BGwgIGwHRkc/W2HW+HQrXJNkuZm2mTarWZIGyXm2GHTKGhRWoV3ZqFcOFBZMmTooaKCiBr0SqMQ0sxgFxzJIiESAI4CMAQoTLmzhz6tzJs6f+z59Ah0SoACJBgQhByXDoAoZD0iwcDjlFIuDAAQFPOzCNM+dIhjMALmRIGkJTiCMe0BxIavAQwiIH1CZNoAljka9exJI1iySDVaxJneV5gPQpk6h5Chh2UqAdAASKFzvpEKJoCH6SM2vezLmz58+gQ7fhsOHCBQeR20SAwKDwzbZf3o4ZgQ7BiJsFDqXOEiFeV0sCEZGBEGcqHxKaIGkhngaCJRJg41xQnkWwF8IuiQknM+LTg9tMBAQIADhJ7sRtOrDGfIRE3C8HWhqB7UV2Twx6lhQofWHDbp8TxDGBaEIgl4d8nwWYxoAEmvALGsEQ6J5aCIYmHnkNZqghgUEBAAAh+QQJCQAnACwAAAAAQABAAIUEAgSEgoRERkTEwsTk4uRkYmQ0MjQUFhRUVlTU1tT08vSkpqQMCgxMTkzMysxsbmz8+vzs6uwcHhxcXlzc3tysrqwEBgSEhoRMSkzExsRkZmQ8OjwcGhxcWlzc2tz09vSsqqwMDgxUUlTMzsx0dnT8/vzs7uz+/v4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG/sCTcEgsGo/IpHLJbA5NjozJSa02RxiAFiAYWb/g08Ky3VoW4TRzxCiXLV613Jh1lwVzJ4RCgCQjdnZTeUkZImQAFiIZRxmBbgOERyUkjyQlRQOPZZFIFCAVHmGVmyRFgJtag0UUAncUVpqpAJ1Drpt4RhQHdgewVHWpGEUOiHZwR7d2uU0fbbMWfkRjx2hGHqkJTtizWqLEylwOSAup1kzc3d9GERlSShWpIE4fxpvRaumB2k7BuHPh7lSRlapWml29flEhZYkQARF31lGBwNANCWmEPIAAwS9MhgaILDQwKEnSHgoYS6pcqRJCSpZzMhTgBeBAAZIwrXzo8AjB/oecXxQYSGVgFdAmCLohODoEhAELFjacE+KoGy2mD+w8IJLU6lKgIB6d42C15tENjwwMKatFQc4SqTCdYAvALcwS9t7IpdntwNGhgdQK4en1aNhA5wjOwrkyq5utXJUyFbLgqQUDU4UIJWp3MhMFXe0gMOqZyYAJZAFwmMC4dBMIP13Lnk27tu3buHPnSYABKoaOYRwUKMBIZYJnWhgAtzIiZBxJ/rQw+6KhTIGSEPImkvulgPWSeI+9pNJcC7KS0bmoGTFhwnNJx8sod10BAYIKTRLcErD86IUyAeiGhAn2WECagCeMYMd7CJ5A4BsHIhgAgA0eUd99FWao4YYcAy4RBAA7OEloRWRqYW9jdzhOTjdUeHV4MTVCcmpRRWxDKzdGSWtiWnV5UUlCY0t5QTlKYmUzU25OM3ArSDd0K3JOMEtOTw=='

PSG_DEBUGGER_LOGO = b'R0lGODlhMgAtAPcAAAAAADD/2akK/4yz0pSxyZWyy5u3zZ24zpW30pG52J250J+60aC60KS90aDC3a3E163F2K3F2bPI2bvO3rzP3qvJ4LHN4rnR5P/zuf/zuv/0vP/0vsDS38XZ6cnb6f/xw//zwv/yxf/1w//zyP/1yf/2zP/3z//30wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAyAC0AAAj/AP8JHEiwoMGDCBMqXMiwoUOFAiJGXBigYoAPDxlK3CigwUGLIAOEyIiQI8cCBUOqJFnQpEkGA1XKZPlPgkuXBATK3JmRws2bB3TuXNmQw8+jQoeCbHj0qIGkSgNobNoUqlKIVJs++BfV4oiEWalaHVpyosCwJidw7Sr1YMQFBDn+y4qSbUW3AiDElXiWqoK1bPEKGLixr1jAXQ9GuGn4sN22Bl02roo4Kla+c8OOJbsQM9rNPJlORlr5asbPpTk/RP2YJGu7rjWnDm2RIQLZrSt3zgp6ZmqwmkHAng3ccWDEMe8Kpnw8JEHlkXnPdh6SxHPILaU/dp60LFUP07dfRq5aYntohAO0m+c+nvT6pVMPZ3jv8AJu8xktyNbw+ATJDtKFBx9NlA20gWU0DVQBYwZhsJMICRrkwEYJJGRCSBtEqGGCAQEAOw=='

DEFAULT_WINDOW_ICON = DEFAULT_BASE64_ICON

DEFAULT_ELEMENT_SIZE = (45, 1)  # In CHARACTERS
DEFAULT_BUTTON_ELEMENT_SIZE = (10, 1)  # In CHARACTERS
DEFAULT_MARGINS = (10, 5)  # Margins for each LEFT/RIGHT margin is first term
DEFAULT_ELEMENT_PADDING = (5, 3)  # Padding between elements (row, col) in pixels
DEFAULT_AUTOSIZE_TEXT = True
DEFAULT_AUTOSIZE_BUTTONS = True
DEFAULT_FONT = ("Helvetica", 10)
DEFAULT_TEXT_JUSTIFICATION = 'left'
DEFAULT_BORDER_WIDTH = 1
DEFAULT_AUTOCLOSE_TIME = 3  # time in seconds to show an autoclose form
DEFAULT_DEBUG_WINDOW_SIZE = (80, 20)
DEFAULT_WINDOW_LOCATION = (None, None)
MAX_SCROLLED_TEXT_BOX_HEIGHT = 50
DEFAULT_TOOLTIP_TIME = 400
DEFAULT_TOOLTIP_OFFSET = (0, -20)
TOOLTIP_BACKGROUND_COLOR = "#ffffe0"
#################### COLOR STUFF ####################
BLUES = ("#082567", "#0A37A3", "#00345B")
PURPLES = ("#480656", "#4F2398", "#380474")
GREENS = ("#01826B", "#40A860", "#96D2AB", "#00A949", "#003532")
YELLOWS = ("#F3FB62", "#F0F595")
TANS = ("#FFF9D5", "#F4EFCF", "#DDD8BA")
NICE_BUTTON_COLORS = ((GREENS[3], TANS[0]),
                      ('#000000', '#FFFFFF'),
                      ('#FFFFFF', '#000000'),
                      (YELLOWS[0], PURPLES[1]),
                      (YELLOWS[0], GREENS[3]),
                      (YELLOWS[0], BLUES[2]))

COLOR_SYSTEM_DEFAULT = '1234567890'  # A Magic Number kind of signal to PySimpleGUI that the color should not be set at all
DEFAULT_BUTTON_COLOR = ('white', BLUES[0])  # Foreground, Background (None, None) == System Default
OFFICIAL_PYSIMPLEGUI_BUTTON_COLOR = ('white', BLUES[0])

CURRENT_LOOK_AND_FEEL = 'DarkBlue3'


DEFAULT_ERROR_BUTTON_COLOR = ("#FFFFFF", "#FF0000")
DEFAULT_BACKGROUND_COLOR = None
DEFAULT_ELEMENT_BACKGROUND_COLOR = None
DEFAULT_ELEMENT_TEXT_COLOR = COLOR_SYSTEM_DEFAULT
DEFAULT_TEXT_ELEMENT_BACKGROUND_COLOR = None
DEFAULT_TEXT_COLOR = COLOR_SYSTEM_DEFAULT
DEFAULT_INPUT_ELEMENTS_COLOR = COLOR_SYSTEM_DEFAULT
DEFAULT_INPUT_TEXT_COLOR = COLOR_SYSTEM_DEFAULT
DEFAULT_SCROLLBAR_COLOR = None
# DEFAULT_BUTTON_COLOR = (YELLOWS[0], PURPLES[0])    # (Text, Background) or (Color "on", Color) as a way to remember
# DEFAULT_BUTTON_COLOR = (GREENS[3], TANS[0])    # Foreground, Background (None, None) == System Default
# DEFAULT_BUTTON_COLOR = (YELLOWS[0], GREENS[4])    # Foreground, Background (None, None) == System Default
# DEFAULT_BUTTON_COLOR = ('white', 'black')    # Foreground, Background (None, None) == System Default
# DEFAULT_BUTTON_COLOR = (YELLOWS[0], PURPLES[2])    # Foreground, Background (None, None) == System Default
# DEFAULT_PROGRESS_BAR_COLOR = (GREENS[2], GREENS[0])     # a nice green progress bar
# DEFAULT_PROGRESS_BAR_COLOR = (BLUES[1], BLUES[1])     # a nice green progress bar
# DEFAULT_PROGRESS_BAR_COLOR = (BLUES[0], BLUES[0])     # a nice green progress bar
# DEFAULT_PROGRESS_BAR_COLOR = (PURPLES[1],PURPLES[0])    # a nice purple progress bar

# A transparent button is simply one that matches the background
# TRANSPARENT_BUTTON = 'This constant has been depricated. You must set your button background = background it is on for it to be transparent appearing'

TRANSPARENT_BUTTON = ('#F0F0F0', '#F0F0F0')  # Use (sg.theme_background_color(), sg.theme_background_color()) instead!!!

# --------------------------------------------------------------------------------
# Progress Bar Relief Choices
RELIEF_RAISED = 'raised'
RELIEF_SUNKEN = 'sunken'
RELIEF_FLAT = 'flat'
RELIEF_RIDGE = 'ridge'
RELIEF_GROOVE = 'groove'
RELIEF_SOLID = 'solid'

# These are the spepific themes that tkinter offers
THEME_DEFAULT = 'default'
THEME_WINNATIVE = 'winnative'
THEME_CLAM = 'clam'
THEME_ALT = 'alt'
THEME_CLASSIC = 'classic'
THEME_VISTA = 'vista'
THEME_XPNATIVE = 'xpnative'
THEME_LIST = ('default', 'winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative')

# The theme to use by default for all windows
DEFAULT_TTK_THEME = THEME_DEFAULT
USE_TTK_BUTTONS = None

DEFAULT_PROGRESS_BAR_COLOR = (GREENS[0], '#D0D0D0')  # a nice green progress bar
DEFAULT_PROGRESS_BAR_COLOR_OFFICIAL = (GREENS[0], '#D0D0D0')  # a nice green progress bar
DEFAULT_PROGRESS_BAR_SIZE = (20, 20)  # Size of Progress Bar (characters for length, pixels for width)
DEFAULT_PROGRESS_BAR_BORDER_WIDTH = 1
DEFAULT_PROGRESS_BAR_RELIEF = RELIEF_GROOVE
PROGRESS_BAR_STYLES = ('default', 'winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative')
DEFAULT_PROGRESS_BAR_STYLE = DEFAULT_TTK_THEME
DEFAULT_METER_ORIENTATION = 'Horizontal'
DEFAULT_SLIDER_ORIENTATION = 'vertical'
DEFAULT_SLIDER_BORDER_WIDTH = 1
DEFAULT_SLIDER_RELIEF = tk.FLAT
DEFAULT_FRAME_RELIEF = tk.GROOVE

DEFAULT_LISTBOX_SELECT_MODE = tk.SINGLE
SELECT_MODE_MULTIPLE = tk.MULTIPLE
LISTBOX_SELECT_MODE_MULTIPLE = 'multiple'
SELECT_MODE_BROWSE = tk.BROWSE
LISTBOX_SELECT_MODE_BROWSE = 'browse'
SELECT_MODE_EXTENDED = tk.EXTENDED
LISTBOX_SELECT_MODE_EXTENDED = 'extended'
SELECT_MODE_SINGLE = tk.SINGLE
LISTBOX_SELECT_MODE_SINGLE = 'single'

TABLE_SELECT_MODE_NONE = tk.NONE
TABLE_SELECT_MODE_BROWSE = tk.BROWSE
TABLE_SELECT_MODE_EXTENDED = tk.EXTENDED
DEFAULT_TABLE_SECECT_MODE = TABLE_SELECT_MODE_EXTENDED

TITLE_LOCATION_TOP = tk.N
TITLE_LOCATION_BOTTOM = tk.S
TITLE_LOCATION_LEFT = tk.W
TITLE_LOCATION_RIGHT = tk.E
TITLE_LOCATION_TOP_LEFT = tk.NW
TITLE_LOCATION_TOP_RIGHT = tk.NE
TITLE_LOCATION_BOTTOM_LEFT = tk.SW
TITLE_LOCATION_BOTTOM_RIGHT = tk.SE

TEXT_LOCATION_TOP = tk.N
TEXT_LOCATION_BOTTOM = tk.S
TEXT_LOCATION_LEFT = tk.W
TEXT_LOCATION_RIGHT = tk.E
TEXT_LOCATION_TOP_LEFT = tk.NW
TEXT_LOCATION_TOP_RIGHT = tk.NE
TEXT_LOCATION_BOTTOM_LEFT = tk.SW
TEXT_LOCATION_BOTTOM_RIGHT = tk.SE
TEXT_LOCATION_CENTER = tk.CENTER

# ----====----====----==== Constants the user should NOT f-with ====----====----====----#
ThisRow = 555666777  # magic number

# DEFAULT_WINDOW_ICON = ''
MESSAGE_BOX_LINE_WIDTH = 60

# "Special" Key Values.. reserved
# Key representing a Read timeout
TIMEOUT_KEY = '__TIMEOUT__'
# Key indicating should not create any return values for element
WRITE_ONLY_KEY = '__WRITE ONLY__'

MENU_DISABLED_CHARACTER = '!'
MENU_KEY_SEPARATOR = '::'

ENABLE_TK_WINDOWS = False


# ====================================================================== #
# One-liner functions that are handy as f_ck                             #
# ====================================================================== #
def RGB(red, green, blue):
    """
    Given integer values of Red, Green, Blue, return a color string "#RRGGBB"
    :param red:  Red portion from 0 to 255
    :type red: (int)
    :param green:  Green portion from 0 to 255
    :type green: (int)
    :param blue:  Blue portion from 0 to 255
    :type  blue: (int)
    :return:  A single RGB String in the format "#RRGGBB" where each pair is a hex number.
    :rtype: (str)
    """
    red = min(int(red),255) if red > 0 else 0
    blue = min(int(blue),255) if blue > 0 else 0
    green = min(int(green),255) if green > 0 else 0
    return '#%02x%02x%02x' % (red, green, blue)


# ====================================================================== #
# Enums for types                                                        #
# ====================================================================== #
# -------------------------  Button types  ------------------------- #
# todo Consider removing the Submit, Cancel types... they are just 'RETURN' type in reality
# uncomment this line and indent to go back to using Enums
BUTTON_TYPE_BROWSE_FOLDER = 1
BUTTON_TYPE_BROWSE_FILE = 2
BUTTON_TYPE_BROWSE_FILES = 21
BUTTON_TYPE_SAVEAS_FILE = 3
BUTTON_TYPE_CLOSES_WIN = 5
BUTTON_TYPE_CLOSES_WIN_ONLY = 6
BUTTON_TYPE_READ_FORM = 7
BUTTON_TYPE_REALTIME = 9
BUTTON_TYPE_CALENDAR_CHOOSER = 30
BUTTON_TYPE_COLOR_CHOOSER = 40
BUTTON_TYPE_SHOW_DEBUGGER = 50

BROWSE_FILES_DELIMITER = ';'  # the delimeter to be used between each file in the returned string

# -------------------------  Element types  ------------------------- #

ELEM_TYPE_TEXT = 'text'
ELEM_TYPE_INPUT_TEXT = 'input'
ELEM_TYPE_INPUT_COMBO = 'combo'
ELEM_TYPE_INPUT_OPTION_MENU = 'option menu'
ELEM_TYPE_INPUT_RADIO = 'radio'
ELEM_TYPE_INPUT_MULTILINE = 'multiline'
ELEM_TYPE_INPUT_CHECKBOX = 'checkbox'
ELEM_TYPE_INPUT_SPIN = 'spind'
ELEM_TYPE_BUTTON = 'button'
ELEM_TYPE_IMAGE = 'image'
ELEM_TYPE_CANVAS = 'canvas'
ELEM_TYPE_FRAME = 'frame'
ELEM_TYPE_GRAPH = 'graph'
ELEM_TYPE_TAB = 'tab'
ELEM_TYPE_TAB_GROUP = 'tabgroup'
ELEM_TYPE_INPUT_SLIDER = 'slider'
ELEM_TYPE_INPUT_LISTBOX = 'listbox'
ELEM_TYPE_OUTPUT = 'output'
ELEM_TYPE_COLUMN = 'column'
ELEM_TYPE_MENUBAR = 'menubar'
ELEM_TYPE_PROGRESS_BAR = 'progressbar'
ELEM_TYPE_BLANK = 'blank'
ELEM_TYPE_TABLE = 'table'
ELEM_TYPE_TREE = 'tree'
ELEM_TYPE_ERROR = 'error'
ELEM_TYPE_SEPARATOR = 'separator'
ELEM_TYPE_STATUSBAR = 'statusbar'
ELEM_TYPE_PANE = 'pane'
ELEM_TYPE_BUTTONMENU = 'buttonmenu'

# STRETCH == ERROR ELEMENT as a filler

# -------------------------  Popup Buttons Types  ------------------------- #
POPUP_BUTTONS_YES_NO = 1
POPUP_BUTTONS_CANCELLED = 2
POPUP_BUTTONS_ERROR = 3
POPUP_BUTTONS_OK_CANCEL = 4
POPUP_BUTTONS_OK = 0
POPUP_BUTTONS_NO_BUTTONS = 5


# ------------------------------------------------------------------------- #
#                       ToolTip used by the Elements                        #
# ------------------------------------------------------------------------- #

class ToolTip:
    """
    Create a tooltip for a given widget
    (inspired by https://stackoverflow.com/a/36221216)
    This is an INTERNALLY USED only class.  Users should not refer to this class at all.
    """

    def __init__(self, widget, text, timeout=DEFAULT_TOOLTIP_TIME):
        """
        :param widget: The tkinter widget
        :type widget: widget type varies
        :param text: text for the tooltip. It can inslude \n
        :type text: str
        :param timeout: Time in milliseconds that mouse must remain still before tip is shown
        :type timeout: int
        """
        self.widget = widget
        self.text = text
        self.timeout = timeout
        # self.wraplength = wraplength if wraplength else widget.winfo_screenwidth() // 2
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)

    def enter(self, event=None):
        """
        Called by tkinter when mouse enters a widget
        :param event:  from tkinter.  Has x,y coordinates of mouse

        """
        self.x = event.x
        self.y = event.y
        self.schedule()

    def leave(self, event=None):
        """
        Called by tktiner when mouse exits a widget
        :param event:  from tkinter.  Event info that's not used by function.

        """
        self.unschedule()
        self.hidetip()

    def schedule(self):
        """
        Schedule a timer to time how long mouse is hovering
        """
        self.unschedule()
        self.id = self.widget.after(self.timeout, self.showtip)

    def unschedule(self):
        """
        Cancel timer used to time mouse hover
        """
        if self.id:
            self.widget.after_cancel(self.id)
        self.id = None

    def showtip(self):
        """
        Creates a topoltip window with the tooltip text inside of it
        """
        if self.tipwindow:
            return
        x = self.widget.winfo_rootx() + self.x + DEFAULT_TOOLTIP_OFFSET[0]
        y = self.widget.winfo_rooty() + self.y + DEFAULT_TOOLTIP_OFFSET[1]
        self.tipwindow = tk.Toplevel(self.widget)
        self.tipwindow.wm_overrideredirect(True)
        self.tipwindow.wm_geometry("+%d+%d" % (x, y))
        self.tipwindow.wm_attributes("-topmost", 1)

        label = ttk.Label(self.tipwindow, text=self.text, justify=tk.LEFT,
                          background=TOOLTIP_BACKGROUND_COLOR, relief=tk.SOLID, borderwidth=1)
        label.pack()

    def hidetip(self):
        """
        Destroy the tooltip window
        """
        if self.tipwindow:
            self.tipwindow.destroy()
        self.tipwindow = None


# ---------------------------------------------------------------------- #
# Cascading structure.... Objects get larger                             #
#   Button                                                               #
#       Element                                                          #
#           Row                                                          #
#               Form                                                     #
# ---------------------------------------------------------------------- #
# ------------------------------------------------------------------------- #
#                       Element CLASS                                       #
# ------------------------------------------------------------------------- #
class Element():
    """
    The base class for all Elements.
    Holds the basic description of an Element like size and colors
    """

    def __init__(self, type, size=(None, None), auto_size_text=None, font=None, background_color=None, text_color=None, key=None, pad=None, tooltip=None,
                 visible=True, metadata=None):
        """
        Element base class. Only used internally.  User will not create an Element object by itself

        :param type: The type of element. These constants all start with "ELEM_TYPE_"
        :type type: (int) (could be enum)
        :param size: w=characters-wide, h=rows-high
        :type size: Tuple[int, int]  (width, height)
        :param auto_size_text: True if the Widget should be shrunk to exactly fit the number of chars to show
        :type auto_size_text: bool
        :param font: specifies the font family, size, etc (see docs for exact formats)
        :type font: Union[str, Tuple[str, int]]
        :param background_color: color of background. Can be in #RRGGBB format or a color name "black"
        :type background_color: (str)
        :param text_color: element's text color. Can be in #RRGGBB format or a color name "black"
        :type text_color: (str)
        :param key: Identifies an Element. Should be UNIQUE to this window.
        :type key: (Any)
        :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element (Default = True)
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """
        self.Size = size
        self.Type = type
        self.AutoSizeText = auto_size_text
        self.Pad = pad
        self.Font = font

        self.TKStringVar = None
        self.TKIntVar = None
        self.TKText = None
        self.TKEntry = None
        self.TKImage = None

        self.ParentForm = None  # type: Window
        self.ParentContainer = None  # will be a Form, Column, or Frame element
        self.TextInputDefault = None
        self.Position = (0, 0)  # Default position Row 0, Col 0
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_ELEMENT_BACKGROUND_COLOR
        self.TextColor = text_color if text_color is not None else DEFAULT_ELEMENT_TEXT_COLOR
        self.Key = key  # dictionary key for return values
        self.Tooltip = tooltip
        self.TooltipObject = None
        self.Visible = visible
        self.TKRightClickMenu = None
        self.Widget = None  # Set when creating window. Has the main tkinter widget for element
        self.Tearoff = False
        self.ParentRowFrame = None  # type tk.Frame
        self.metadata = metadata  # type: Any
        self.user_bind_dict = {}  # Used when user defines a tkinter binding using bind method - convert bind string to key modifier
        self.user_bind_event = None  # Used when user defines a tkinter binding using bind method - event data from tkinter
        self.pad_used    = (0,0)        # the amount of pad used when was inserted into the layout



    def _RightClickMenuCallback(self, event):
        """
        Callback function that's called when a right click happens. Shows right click menu as result

        :param event: information provided by tkinter about the event including x,y location of click

        """
        self.TKRightClickMenu.tk_popup(event.x_root, event.y_root, 0)
        self.TKRightClickMenu.grab_release()

    def _MenuItemChosenCallback(self, item_chosen):  # TEXT Menu item callback
        """
        Callback function called when user chooses a menu item from menubar, Button Menu or right click menu

        :param item_chosen: String holding the value chosen.
        :type item_chosen: str

        """
        # print('IN MENU ITEM CALLBACK', item_chosen)
        self.MenuItemChosen = item_chosen.replace('&', '')
        self.ParentForm.LastButtonClicked = self.MenuItemChosen
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

    def _FindReturnKeyBoundButton(self, form):
        """
        Searches for which Button has the flag Button.BindReturnKey set.  It is called recursively when a
        "Container Element" is encountered. Func has to walk entire window including these "sub-forms"

        :param form: the Window object to search
        :return: Union[Button, None] Button Object if a button is found, else None if no button found
        :rtype: Button Object if a button is found, else None if no button found
        """
        for row in form.Rows:
            for element in row:
                if element.Type == ELEM_TYPE_BUTTON:
                    if element.BindReturnKey:
                        return element
                if element.Type == ELEM_TYPE_COLUMN:
                    rc = self._FindReturnKeyBoundButton(element)
                    if rc is not None:
                        return rc
                if element.Type == ELEM_TYPE_FRAME:
                    rc = self._FindReturnKeyBoundButton(element)
                    if rc is not None:
                        return rc
                if element.Type == ELEM_TYPE_TAB_GROUP:
                    rc = self._FindReturnKeyBoundButton(element)
                    if rc is not None:
                        return rc
                if element.Type == ELEM_TYPE_TAB:
                    rc = self._FindReturnKeyBoundButton(element)
                    if rc is not None:
                        return rc
                if element.Type == ELEM_TYPE_PANE:
                    rc = self._FindReturnKeyBoundButton(element)
                    if rc is not None:
                        return rc
        return None

    def _TextClickedHandler(self, event):
        """
        Callback that's called when a text element is clicked on with events enabled on the Text Element.
        Result is that control is returned back to user (quits mainloop).

        :param event:

        """
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = self.DisplayText
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

    def _ReturnKeyHandler(self, event):
        """
        Internal callback for the ENTER / RETURN key. Results in calling the ButtonCallBack for element that has the return key bound to it, just as if button was clicked.

        :param event:

        """
        MyForm = self.ParentForm
        button_element = self._FindReturnKeyBoundButton(MyForm)
        if button_element is not None:
            button_element.ButtonCallBack()

    def _ListboxSelectHandler(self, event):
        """
        Internal callback function for when a listbox item is selected

        :param event: Information from tkinter about the callback

        """
        # first, get the results table built
        # modify the Results table in the parent FlexForm object
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

    def _ComboboxSelectHandler(self, event):
        """
        Internal callback function for when an entry is selected in a Combobox.
        :param event: Event data from tkinter (not used)

        """
        # first, get the results table built
        # modify the Results table in the parent FlexForm object
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

    def _RadioHandler(self):
        """
        Internal callback for when a radio button is selected and enable events was set for radio
        """
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()

    def _CheckboxHandler(self):
        """
        Internal callback for when a checkbnox is selected and enable events was set for checkbox
        """
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()

    def _TabGroupSelectHandler(self, event):
        """
        Internal callback for when a Tab is selected and enable events was set for TabGroup

        :param event: Event data passed in by tkinter (not used)
        """
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()

    def _KeyboardHandler(self, event):
        """
        Internal callback for when a key is pressed andd return keyboard events was set for window

        :param event: Event data passed in by tkinter (not used)
        """
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()

    def _ClickHandler(self, event):
        """
        Internal callback for when a mouse was clicked... I think.

        :param event: Event data passed in by tkinter (not used)
        """
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()

    def _user_bind_callback(self, bind_string, event):
        """
        Used when user binds a tkinter event directly to an element

        :param bind_string: The event that was bound so can lookup the key modifier
        :param event: Event data passed in by tkinter (not used)
        """
        key_suffix = self.user_bind_dict.get(bind_string, '')
        self.user_bind_event = event
        if self.Key is not None:
            if isinstance(self.Key, str):
                self.ParentForm.LastButtonClicked = self.Key + str(key_suffix)
            else:
                self.ParentForm.LastButtonClicked = (self.Key, key_suffix)
        else:
            self.ParentForm.LastButtonClicked = bind_string
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()

    def bind(self, bind_string, key_modifier):
        """
        Used to add tkinter events to an Element.
        The tkinter specific data is in the Element's member variable user_bind_event
        :param bind_string: The string tkinter expected in its bind function
        :param key_modifier: Additional data to be added to the element's key when event is returned
        """
        self.Widget.bind(bind_string, lambda evt: self._user_bind_callback(bind_string, evt))
        self.user_bind_dict[bind_string] = key_modifier


    def unbind(self, bind_string):
        """
        Removes a previously bound tkinter event from an Element.
        :param bind_string: The string tkinter expected in its bind function
        """
        self.Widget.unbind(bind_string)
        self.user_bind_dict.pop(bind_string, None)



    def ButtonReboundCallback(self, event):
        """
        *** DEPRICATED ***
        Use Element.bind instead

        :param event: (unknown) Not used in this function.
        """
        # print(f'Button callback event = {event}, {other}')
        try:
            self.ButtonCallBack()
        except:
            print('** ButtonReboundCallback - warning your element does not have a ButtonCallBack method **')

    def SetTooltip(self, tooltip_text):
        """
        Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

        :param tooltip_text: the text to show in tooltip.
        :type tooltip_text: str
        """
        self.TooltipObject = ToolTip(self.Widget, text=tooltip_text, timeout=DEFAULT_TOOLTIP_TIME)

    def SetFocus(self, force=False):
        """
        Sets the current focus to be on this element

        :param force: if True will call focus_force otherwise calls focus_set
        :type force: bool
        """

        try:
            if force:
                self.Widget.focus_force()
            else:
                self.Widget.focus_set()
        except:
            print('Was unable to set focus.  The Widget passed in was perhaps not present in this element?  Check your elements .Widget property')

    def set_size(self, size=(None, None)):
        """
        Changes the size of an element to a specific size.
        It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

        :param size: The size in characters, rows typically. In some cases they are pixels
        :type size: Tuple[int, int]
        """
        try:
            if size[0] != None:
                self.Widget.config(width=size[0])
        except:
            print('Warning, error setting width on element with key=', self.Key)
        try:
            if size[1] != None:
                self.Widget.config(height=size[1])
        except:
            try:
                self.Widget.config(length=size[1])
            except:
                print('Warning, error setting height on element with key=', self.Key)

    def get_size(self):
        """
        Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.
        :return: width and height of the element
        :rtype: Tuple[int, int]
        """
        try:
            w = self.Widget.winfo_width()
            h = self.Widget.winfo_height()
        except:
            print('Warning, error getting size of element', self.Key)
            w = h = None
        return w, h

    def hide_row(self):
        """
        Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container
        """
        try:
            self.ParentRowFrame.pack_forget()
        except:
            print('Warning, error hiding element row for key =', self.Key)

    def unhide_row(self):
        """
        Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.
        """
        try:
            self.ParentRowFrame.pack()
        except:
            print('Warning, error hiding element row for key =', self.Key)

    def expand(self, expand_x=False, expand_y=False, expand_row=True):
        """
        Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

        :param expand_x: (Bool) If True Element will expand in the Horizontal directions
        :param expand_y:  (Bool) If True Element will expand in the Vertical directions
        :param expand_row:  (Bool) If True the row containing the element will also expand. Without this your element is "trapped" within the row
        """
        if expand_x and expand_y:
            fill = tk.BOTH
        elif expand_x:
            fill = tk.X
        elif expand_y:
            fill = tk.Y
        else:
            return

        self.Widget.pack(expand=True, fill=fill)
        self.ParentRowFrame.pack(expand=expand_row, fill=fill)


    def set_cursor(self,cursor):
        """
        Sets the cursor for the current Element.
        :param cursor: (str) The tkinter cursor name
        """
        try:
            self.Widget.config(cursor=cursor)
        except Exception as e:
            print('Warning bad cursor specified ', cursor)
            print(e)


    def __call__(self, *args, **kwargs):
        """
        Makes it possible to "call" an already existing element.  When you do make the "call", it actually calls
        the Update method for the element.
        Example:    If this text element was in yoiur layout:
                    sg.Text('foo', key='T')
                    Then you can call the Update method for that element by writing:
                    window.FindElement('T')('new text value')
        """
        return self.Update(*args, **kwargs)

    button_rebound_callback = ButtonReboundCallback
    set_tooltip = SetTooltip
    set_focus = SetFocus


# ---------------------------------------------------------------------- #
#                           Input Class                                  #
# ---------------------------------------------------------------------- #
class InputText(Element):
    """
    Display a single text input field.  Based on the tkinter Widget `Entry`
    """

    def __init__(self, default_text='', size=(None, None), disabled=False, password_char='',
                 justification=None, background_color=None, text_color=None, font=None, tooltip=None,

                 change_submits=False, enable_events=False, do_not_clear=True, key=None, focus=False, pad=None,
                 use_readonly_for_disable=True, right_click_menu=None, visible=True, metadata=None):
        """
        :param default_text: Text initially shown in the input box as a default value(Default value = '')
        :type default_text: (str)
        :param size: w=characters-wide, h=rows-high
        :type size: Tuple[int, int]  (width, height)
        :param disabled: set disable state for element (Default = False)
        :type disabled: (bool)
        :param password_char: Password character if this is a password field (Default value = '')
        :type password_char: (char)
        :param justification: justification for data display. Valid choices - left, right, center
        :type justification: (str)
        :param background_color: color of background in one of the color formats
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param change_submits: * DEPRICATED DO NOT USE! Same as enable_events
        :type change_submits: (bool)
        :param enable_events: If True then changes to this element are immediately reported as an event. Use this instead of change_submits (Default = False)
        :type enable_events: (bool)
        :param do_not_clear: If False then the field will be set to blank after ANY event (button, any event) (Default = True)
        :type do_not_clear: (bool)
        :param key: Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
        :type key: (any)
        :param focus: Determines if initial focus should go to this element.
        :type focus: (bool)
        :param pad: . Amount of padding to put around element. Normally (horizontal pixels, vertical pixels) but can be split apart further into ((horizontal left, horizontal right), (vertical above, vertical below))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param use_readonly_for_disable: If True (the default) tkinter state set to 'readonly'. Otherwise state set to 'disabled'
        :type use_readonly_for_disable: (bool)
        :param right_click_menu: A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
        :type right_click_menu: List[List[Union[List[str],str]]]
        :param visible: set visibility state of the element (Default = True)
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """
        self.DefaultText = default_text
        self.PasswordCharacter = password_char
        bg = background_color if background_color is not None else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR
        self.Focus = focus
        self.do_not_clear = do_not_clear
        self.Justification = justification
        self.Disabled = disabled
        self.ChangeSubmits = change_submits or enable_events
        self.RightClickMenu = right_click_menu
        self.UseReadonlyForDisable = use_readonly_for_disable
        self.TKEntry = self.Widget = None  # type: tk.Entry
        super().__init__(ELEM_TYPE_INPUT_TEXT, size=size, background_color=bg, text_color=fg, key=key, pad=pad,
                         font=font, tooltip=tooltip, visible=visible, metadata=metadata)

    def Update(self, value=None, disabled=None, select=None, visible=None, text_color=None, background_color=None, move_cursor_to='end'):
        """
        Changes some of the settings for the Input Element. Must call `Window.Read` or `Window.Finalize` prior

        :param value: new text to display as default text in Input field
        :type value: (str)
        :param disabled: disable or enable state of the element (sets Entry Widget to readonly or normal)
        :type disabled: (bool)
        :param select: if True, then the text will be selected
        :type select: (bool)
        :param visible: change visibility of element
        :type visible: (bool)
        :param text_color: change color of text being typed
        :type text_color: (str)
        :param background_color: change color of the background
        :type background_color: (str)
        :param move_cursor_to: Moves the cursor to a particular offset. Defaults to 'end'
        :type move_cursor_to: Union[int, str]
        """
        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if disabled is True:
            self.TKEntry['state'] = 'readonly' if self.UseReadonlyForDisable else 'disabled'
        elif disabled is False:
            self.TKEntry['state'] = 'normal'
        if background_color is not None:
            self.TKEntry.configure(background=background_color)
        if text_color is not None:
            self.TKEntry.configure(fg=text_color)
        if value is not None:
            try:
                self.TKStringVar.set(value)
            except:
                pass
            self.DefaultText = value
            if move_cursor_to == 'end':
                self.TKEntry.icursor(tk.END)
            elif move_cursor_to is not None:
                self.TKEntry.icursor(move_cursor_to)
        if select:
            self.TKEntry.select_range(0, 'end')
        if visible is False:
            self.TKEntry.pack_forget()
        elif visible is True:
            self.TKEntry.pack(padx=self.pad_used[0], pady=self.pad_used[1])

    def Get(self):
        """
        Read and return the current value of the input element. Must call `Window.Read` or `Window.Finalize` prior

        :return: current value of Input field or '' if error encountered
        :rtype: (str)
        """
        try:
            text = self.TKStringVar.get()
        except:
            text = ''
        return text

    get = Get
    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update


# -------------------------  INPUT TEXT Element lazy functions  ------------------------- #
In = InputText
Input = InputText
I = InputText


# ---------------------------------------------------------------------- #
#                           Combo                                        #
# ---------------------------------------------------------------------- #
class Combo(Element):
    """
    ComboBox Element - A combination of a single-line input and a drop-down menu. User can type in their own value or choose from list.
    """

    def __init__(self, values, default_value=None, size=(None, None), auto_size_text=None, background_color=None,
                 text_color=None, change_submits=False, enable_events=False, disabled=False, key=None, pad=None,
                 tooltip=None, readonly=False, font=None, visible=True, metadata=None):
        """
        :param values: values to choose. While displayed as text, the items returned are what the caller supplied, not text
        :type values: List[Any]
        :param default_value: Choice to be displayed as initial value. Must match one of values variable contents
        :type default_value: (Any)
        :param size: width = characters-wide, height = rows-high
        :type size: Tuple[int, int] (width, height)
        :param auto_size_text: True if element should be the same size as the contents
        :type auto_size_text: (bool)
        :param background_color: color of background
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param change_submits: DEPRICATED DO NOT USE. Use `enable_events` instead
        :type change_submits: (bool)
        :param enable_events: Turns on the element specific events. Combo event is when a choice is made
        :type enable_events: (bool)
        :param disabled: set disable state for element
        :type disabled: (bool)
        :para key: Used with window.FindElement and with return values to uniquely identify this element
        :type key: (Any)
        :param:  Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :para tooltip: text that will appear when mouse hovers over this element
        :type tooltip: (str)
        :par readonly: make element readonly (user can't change). True means user cannot change
        :type readonly: (bool)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """
        self.Values = values
        self.DefaultValue = default_value
        self.ChangeSubmits = change_submits or enable_events
        self.Widget = self.TKCombo = None  # type: ttk.Combobox
        self.Disabled = disabled
        self.Readonly = readonly
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR

        super().__init__(ELEM_TYPE_INPUT_COMBO, size=size, auto_size_text=auto_size_text, background_color=bg,
                         text_color=fg, key=key, pad=pad, tooltip=tooltip, font=font or DEFAULT_FONT, visible=visible, metadata=metadata)

    def Update(self, value=None, values=None, set_to_index=None, disabled=None, readonly=None, font=None, visible=None):
        """
        Changes some of the settings for the Combo Element. Must call `Window.Read` or `Window.Finalize` prior
        :param value: change which value is current selected hased on new list of previous list of choices
        :type value: (Any)
        :param values: change list of choices
        :type values: List[Any]
        :param set_to_index: change selection to a particular choice starting with index = 0
        :type set_to_index: (int)
        :param disabled: disable or enable state of the element
        :type disabled: (bool)
        :param readonly: if True make element readonly (user cannot change any choices)
        :type readonly: (bool)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param visible: control visibility of element
        :type visible: (bool)
        """

        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if values is not None:
            try:
                self.TKCombo['values'] = values
                self.TKCombo.current(0)
            except:
                pass
            self.Values = values
        if value is not None:
            if value not in self.Values:
                self.TKCombo.set(value)
            else:
                for index, v in enumerate(self.Values):
                    if v == value:
                        try:
                            self.TKCombo.current(index)
                        except:
                            pass
                        self.DefaultValue = value
                        break
        if set_to_index is not None:
            try:
                self.TKCombo.current(set_to_index)
                self.DefaultValue = self.Values[set_to_index]
            except:
                pass
        if readonly:
            self.Readonly = True
            self.TKCombo['state'] = 'readonly'
        elif readonly is False:
            self.Readonly = False
            self.TKCombo['state'] = 'enable'
        if disabled == True:
            self.TKCombo['state'] = 'disable'
        elif disabled == False:
            self.TKCombo['state'] = 'enable'
        if font is not None:
            self.TKCombo.configure(font=font)
        if visible is False:
            self.TKCombo.pack_forget()
        elif visible is True:
            self.TKCombo.pack(padx=self.pad_used[0], pady=self.pad_used[1])

    def Get(self):
        """
        Returns the current (right now) value of the Combo.  DO NOT USE THIS AS THE NORMAL WAY OF READING A COMBO!
        You should be using values from your call to window.Read instead.  Know what you're doing if you use it.

        :return: Returns the value of what is currently chosen
        :rtype: Union[Any, None]
        """
        try:
            if self.TKCombo.current() == -1:  # if the current value was not in the original list
                value = self.TKCombo.get()  # then get the value typed in by user
            else:
                value = self.Values[self.TKCombo.current()]  # get value from original list given index
        except:
            value = None  # only would happen if user closes window
        return value

    get = Get
    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update


# -------------------------  INPUT COMBO Element lazy functions  ------------------------- #
InputCombo = Combo
DropDown = InputCombo
Drop = InputCombo
DD = Combo


# ---------------------------------------------------------------------- #
#                           Option Menu                                  #
# ---------------------------------------------------------------------- #
class OptionMenu(Element):
    """
    Option Menu is an Element available ONLY on the tkinter port of PySimpleGUI.  It's is a widget that is unique
    to tkinter.  However, it looks much like a ComboBox.  Instead of an arrow to click to pull down the list of
    choices, another little graphic is shown on the widget to indicate where you click.  After clicking to activate,
    it looks like a Combo Box that you scroll to select a choice.
    """

    def __init__(self, values, default_value=None, size=(None, None), disabled=False, auto_size_text=None,
                 background_color=None, text_color=None, key=None, pad=None, tooltip=None, visible=True, metadata=None):
        """
        :param values: Values to be displayed
        :type values: List[Any]
        :param default_value: the value to choose by default
        :type default_value: (Any)
        :param size: size in characters (wide) and rows (high)
        :type size: Tuple[int, int] (width, height)
        :param disabled: control enabled / disabled
        :type disabled: (bool)
        :param auto_size_text: True if size of Element should match the contents of the items
        :type auto_size_text: (bool)
        :param background_color: color of background
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param key: Used with window.FindElement and with return values to uniquely identify this element
        :type key: (Any)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param tooltip: (str) text that will appear when mouse hovers over this element
        :type tooltip: (str)
        :param visible: (bool) set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        """
        self.Values = values
        self.DefaultValue = default_value
        self.Widget = self.TKOptionMenu = None  # type: tk.OptionMenu
        self.Disabled = disabled
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR

        super().__init__(ELEM_TYPE_INPUT_OPTION_MENU, size=size, auto_size_text=auto_size_text, background_color=bg,
                         text_color=fg, key=key, pad=pad, tooltip=tooltip, visible=visible, metadata=metadata)

    def Update(self, value=None, values=None, disabled=None, visible=None):
        """
        Changes some of the settings for the OptionMenu Element. Must call `Window.Read` or `Window.Finalize` prior
        :param value: the value to choose by default
        :type value: (Any)
        :param values: Values to be displayed
        :type values: List[Any]
        :param disabled: disable or enable state of the element
        :type disabled: (bool)
        :param visible: control visibility of element
        :type visible: (bool)
        """

        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if values is not None:
            self.Values = values
            self.TKOptionMenu['menu'].delete(0, 'end')

            # Insert list of new options (tk._setit hooks them up to var)
            self.TKStringVar.set(self.Values[0])
            for new_value in self.Values:
                self.TKOptionMenu['menu'].add_command(label=new_value, command=tk._setit(self.TKStringVar, new_value))

        if self.Values is not None:
            for index, v in enumerate(self.Values):
                if v == value:
                    try:
                        self.TKStringVar.set(value)
                    except:
                        pass
                    self.DefaultValue = value
                    break
        if disabled == True:
            self.TKOptionMenu['state'] = 'disabled'
        elif disabled == False:
            self.TKOptionMenu['state'] = 'normal'
        if visible is False:
            self.TKOptionMenu.pack_forget()
        elif visible is True:
            self.TKOptionMenu.pack(padx=self.pad_used[0], pady=self.pad_used[1])

    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update


# -------------------------  OPTION MENU Element lazy functions  ------------------------- #
InputOptionMenu = OptionMenu


# ---------------------------------------------------------------------- #
#                           Listbox                                      #
# ---------------------------------------------------------------------- #
class Listbox(Element):
    """
    A List Box.  Provide a list of values for the user to choose one or more of.   Returns a list of selected rows
    when a window.Read() is executed.
    """

    def __init__(self, values, default_values=None, select_mode=None, change_submits=False, enable_events=False,
                 bind_return_key=False, size=(None, None), disabled=False, auto_size_text=None, font=None, no_scrollbar=False,
                 background_color=None, text_color=None, key=None, pad=None, tooltip=None, right_click_menu=None,
                 visible=True, metadata=None):
        """
        :param values: list of values to display. Can be any type including mixed types as long as they have __str__ method
        :type values: List[Any]
        :param default_values: which values should be initially selected
        :type default_values: List[Any]
        :param select_mode: Select modes are used to determine if only 1 item can be selected or multiple and how they can be selected.   Valid choices begin with "LISTBOX_SELECT_MODE_" and include: LISTBOX_SELECT_MODE_SINGLE LISTBOX_SELECT_MODE_MULTIPLE LISTBOX_SELECT_MODE_BROWSE LISTBOX_SELECT_MODE_EXTENDED
        :type select_mode: [enum]
        :param change_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type change_submits: (bool)
        :param enable_events: Turns on the element specific events. Listbox generates events when an item is clicked
        :type enable_events: (bool)
        :param bind_return_key: If True, then the return key will cause a the Listbox to generate an event
        :type bind_return_key: (bool)
        :param size: width = characters-wide, height = rows-high
        :type size: Tuple(int, int) (width, height)
        :param disabled: set disable state for element
        :type disabled: (bool)
        :param auto_size_text: True if element should be the same size as the contents
        :type auto_size_text: (bool)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param background_color: color of background
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param key: Used with window.FindElement and with return values to uniquely identify this element
        :type key: (Any)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param right_click_menu: A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
        :type right_click_menu: List[List[Union[List[str],str]]]
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """
        self.Values = values
        self.DefaultValues = default_values
        self.TKListbox = None
        self.ChangeSubmits = change_submits or enable_events
        self.BindReturnKey = bind_return_key
        self.Disabled = disabled
        if select_mode == LISTBOX_SELECT_MODE_BROWSE:
            self.SelectMode = SELECT_MODE_BROWSE
        elif select_mode == LISTBOX_SELECT_MODE_EXTENDED:
            self.SelectMode = SELECT_MODE_EXTENDED
        elif select_mode == LISTBOX_SELECT_MODE_MULTIPLE:
            self.SelectMode = SELECT_MODE_MULTIPLE
        elif select_mode == LISTBOX_SELECT_MODE_SINGLE:
            self.SelectMode = SELECT_MODE_SINGLE
        else:
            self.SelectMode = DEFAULT_LISTBOX_SELECT_MODE
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR
        self.RightClickMenu = right_click_menu
        self.vsb = None  # type: tk.Scrollbar
        self.TKListbox = self.Widget = None  # type: tk.Listbox
        self.NoScrollbar = no_scrollbar
        super().__init__(ELEM_TYPE_INPUT_LISTBOX, size=size, auto_size_text=auto_size_text, font=font,
                         background_color=bg, text_color=fg, key=key, pad=pad, tooltip=tooltip, visible=visible, metadata=metadata)

    def Update(self, values=None, disabled=None, set_to_index=None, scroll_to_index=None, select_mode=None, visible=None):
        """
        Changes some of the settings for the Listbox Element. Must call `Window.Read` or `Window.Finalize` prior
        :param values: new list of choices to be shown to user
        :type values: List[Any]
        :param disabled: disable or enable state of the element
        :type disabled: (bool)
        :param set_to_index: highlights the item(s) indicated. If parm is an int one entry will be set. If is a list, then each entry in list is highlighted
        :type set_to_index: Union[int, list, tuple]
        :param scroll_to_index: scroll the listbox so that this index is the first shown
        :type scroll_to_index: (int)
        :param mode: changes the select mode according to tkinter's listbox widget
        :type mode: (str)
        :param visible: control visibility of element
        :type visible: (bool)
        """

        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if disabled == True:
            self.TKListbox.configure(state='disabled')
        elif disabled == False:
            self.TKListbox.configure(state='normal')
        if values is not None:
            self.TKListbox.delete(0, 'end')
            for item in values:
                self.TKListbox.insert(tk.END, item)
            # self.TKListbox.selection_set(0, 0)
            self.Values = values
        if set_to_index is not None:
            self.TKListbox.selection_clear(0, len(self.Values))  # clear all listbox selections
            if type(set_to_index) in (tuple, list):
                for i in set_to_index:
                    try:
                        self.TKListbox.selection_set(i, i)
                    except:
                        warnings.warn('* Listbox Update selection_set failed with index {}*'.format(set_to_index))
            else:
                try:
                    self.TKListbox.selection_set(set_to_index, set_to_index)
                except:
                    warnings.warn('* Listbox Update selection_set failed with index {}*'.format(set_to_index))
        if visible is False:
            self.TKListbox.pack_forget()
            if not self.NoScrollbar:
                self.vsb.pack_forget()
        elif visible is True:
            self.TKListbox.pack(padx=self.pad_used[0], pady=self.pad_used[1])
            if not self.NoScrollbar:
                self.vsb.pack()
        if scroll_to_index is not None and len(self.Values):
            self.TKListbox.yview_moveto(scroll_to_index / len(self.Values))
        if select_mode is not None:
            try:
                self.TKListbox.config(selectmode=select_mode)
            except:
                print('Listbox.update error trying to change mode to: ', select_mode)

    def SetValue(self, values):
        """
        Set listbox highlighted choices

        :param values: new values to choose based on previously set values
        :type values: List[Any]

        """
        for index, item in enumerate(self.Values):
            try:
                if item in values:
                    self.TKListbox.selection_set(index)
                else:
                    self.TKListbox.selection_clear(index)
            except:
                pass
        self.DefaultValues = values

    def GetListValues(self):
        # type: (Listbox) -> List[Any]
        """
        Returns list of Values provided by the user in the user's format

        :return: List of values. Can be any / mixed types -> []
        :rtype: List[Any]
        """
        return self.Values

    def GetIndexes(self):
        """
        Returns the items currently selected as a list of indexes

        :return: A list of offsets into values that is currently selected
        :rtype: List[int]
        """
        return self.TKListbox.curselection()


    def get(self):
        """
        Returns the list of items currently selected in this listbox.  It should be identical
        to the value you would receive when performing a window.read() call.

        :return: The list of currently selected items. The actual items are returned, not the indexes
        :rtype: List[Any]
        """
        try:
            items = self.TKListbox.curselection()
            value = [self.Values[int(item)] for item in items]
        except:
            value = []
        return value



    get_indexes = GetIndexes
    get_list_values = GetListValues
    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    set_value = SetValue
    update = Update


LBox = Listbox
LB = Listbox


# ---------------------------------------------------------------------- #
#                           Radio                                        #
# ---------------------------------------------------------------------- #
class Radio(Element):
    """
    Radio Button Element - Used in a group of other Radio Elements to provide user with ability to select only
    1 choice in a list of choices.
    """

    def __init__(self, text, group_id, default=False, disabled=False, size=(None, None), auto_size_text=None,
                 background_color=None, text_color=None, font=None, key=None, pad=None, tooltip=None,
                 change_submits=False, enable_events=False, visible=True, metadata=None):
        """
        :param text: Text to display next to button
        :type text: (str)
        :param group_id: Groups together multiple Radio Buttons. Any type works
        :type group_id: (Any)
        :param default: Set to True for the one element of the group you want initially selected
        :type default: (bool)
        :param disabled: set disable state
        :type disabled: (bool)
        :param size: int] (width, height) width = characters-wide, height = rows-high
        :type size: Tuple[int,
        :param auto_size_text: if True will size the element to match the length of the text
        :type auto_size_text: (bool)
        :param background_color: color of background
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param key: Used with window.FindElement and with return values to uniquely identify this element
        :type key: (Any)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param change_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type change_submits: (bool)
        :param enable_events: Turns on the element specific events. Radio Button events happen when an item is selected
        :type enable_events: (bool)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.InitialState = default
        self.Text = text
        self.TKRadio = None
        self.GroupID = group_id
        self.Value = None
        self.Disabled = disabled
        self.TextColor = text_color if text_color else theme_text_color()
        # ---- compute color of circle background ---
        try:          # something in here will fail if a color is not specified in Hex
            text_hsl = _hex_to_hsl(self.TextColor)
            background_hsl = _hex_to_hsl(background_color if background_color else theme_background_color())
            l_delta = abs(text_hsl[2] - background_hsl[2])/10
            if text_hsl[2] > background_hsl[2]:      # if the text is "lighter" than the background then make background darker
                bg_rbg = _hsl_to_rgb(background_hsl[0], background_hsl[1], background_hsl[2]-l_delta)
            else:
                bg_rbg = _hsl_to_rgb(background_hsl[0], background_hsl[1],background_hsl[2]+l_delta)
            self.CircleBackgroundColor = RGB(*bg_rbg)
        except:
            self.CircleBackgroundColor = background_color if background_color else theme_background_color()
        self.ChangeSubmits = change_submits or enable_events
        self.EncodedRadioValue = None
        super().__init__(ELEM_TYPE_INPUT_RADIO, size=size, auto_size_text=auto_size_text, font=font,
                         background_color=background_color, text_color=self.TextColor, key=key, pad=pad,
                         tooltip=tooltip, visible=visible, metadata=metadata)

    def Update(self, value=None, disabled=None, visible=None):
        """
        Changes some of the settings for the Radio Button Element. Must call `Window.Read` or `Window.Finalize` prior
        :param value: if True change to selected and set others in group to unselected
        :type value: (bool)
        :param disabled: disable or enable state of the element
        :type disabled: (bool)
        :param visible: control visibility of element
        :type visible: (bool)
        """

        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if value is not None:
            try:
                if value:
                    self.TKIntVar.set(self.EncodedRadioValue)
            except:
                pass
            self.InitialState = value
        if disabled == True:
            self.TKRadio['state'] = 'disabled'
        elif disabled == False:
            self.TKRadio['state'] = 'normal'
        if visible is False:
            self.TKRadio.pack_forget()
        elif visible is True:
            self.TKRadio.pack(padx=self.pad_used[0], pady=self.pad_used[1])

    def ResetGroup(self):
        """
        Sets all Radio Buttons in the group to not selected
        """
        self.TKIntVar.set(0)

    def Get(self):
        # type: (Radio) -> bool
        """
        A snapshot of the value of Radio Button -> (bool)

        :return: True if this radio button is selected
        :rtype: (bool)
        """
        return self.TKIntVar.get() == self.EncodedRadioValue

    get = Get
    reset_group = ResetGroup
    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update


R = Radio
Rad = Radio


# ---------------------------------------------------------------------- #
#                           Checkbox                                     #
# ---------------------------------------------------------------------- #
class Checkbox(Element):
    """
    Checkbox Element - Displays a checkbox and text next to it
    """

    def __init__(self, text, default=False, size=(None, None), auto_size_text=None, font=None, background_color=None,
                 text_color=None, change_submits=False, enable_events=False, disabled=False, key=None, pad=None,
                 tooltip=None, visible=True, metadata=None):
        """
        :param text: Text to display next to checkbox
        :type text: (str)
        :param default: Set to True if you want this checkbox initially checked
        :type default: (bool)
        :param size: (width, height) width = characters-wide, height = rows-high
        :type size: Tuple[int, int]
        :param auto_size_text: if True will size the element to match the length of the text
        :type auto_size_text: (bool)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param background_color: color of background
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param change_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type change_submits: (bool)
        :param enable_events: Turns on the element specific events. Checkbox events happen when an item changes
        :type enable_events: (bool)
        :param disabled: set disable state
        :type disabled: (bool)
        :param key: Used with window.FindElement and with return values to uniquely identify this element
        :type key: (Any)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.Text = text
        self.InitialState = default
        self.Value = None
        self.TKCheckbutton = self.Widget = None  # type: tk.Checkbutton
        self.Disabled = disabled
        self.TextColor = text_color if text_color else theme_text_color()
        # ---- compute color of circle background ---
        try:        # something in here will fail if a color is not specified in Hex
            text_hsl = _hex_to_hsl(self.TextColor)
            background_hsl = _hex_to_hsl(background_color if background_color else theme_background_color())
            # print(f'backgroundHSL = {background_hsl}')
            l_delta = abs(text_hsl[2] - background_hsl[2])/10
            if text_hsl[2] > background_hsl[2]:      # if the text is "lighter" than the background then make background darker
                bg_rbg = _hsl_to_rgb(background_hsl[0], background_hsl[1], background_hsl[2]-l_delta)
            else:
                bg_rbg = _hsl_to_rgb(background_hsl[0], background_hsl[1],background_hsl[2]+l_delta)
            self.CheckboxBackgroundColor = RGB(*bg_rbg)
        except:
            self.CheckboxBackgroundColor = background_color if background_color else theme_background_color()

        self.ChangeSubmits = change_submits or enable_events

        super().__init__(ELEM_TYPE_INPUT_CHECKBOX, size=size, auto_size_text=auto_size_text, font=font,
                         background_color=background_color, text_color=self.TextColor, key=key, pad=pad,
                         tooltip=tooltip, visible=visible, metadata=metadata)

    def Get(self):
        # type: (Checkbox) -> bool
        """
        Return the current state of this checkbox

        :return: Current state of checkbox
        :rtype: (bool)
        """
        return self.TKIntVar.get()

    def Update(self, value=None, text=None, background_color=None, text_color=None, disabled=None, visible=None):
        """
        Changes some of the settings for the Checkbox Element. Must call `Window.Read` or `Window.Finalize` prior.
        Note that changing visibility may cause element to change locations when made visible after invisible
        :param value: if True checks the checkbox, False clears it
        :type value: (bool)
        :param text: Text to display next to checkbox
        :type text: (str)
        :param background_color: color of background
        :type background_color: (str)
        :param text_color: color of the text. Note this also changes the color of the checkmark
        :type text_color: (str)
        :param disabled: disable or enable element
        :type disabled: (bool)
        :param visible: control visibility of element
        :type visible: (bool)
        """

        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if value is not None:
            try:
                self.TKIntVar.set(value)
                self.InitialState = value
            except:
                print('Checkbox update failed')
        if disabled == True:
            self.TKCheckbutton.configure(state='disabled')
        elif disabled == False:
            self.TKCheckbutton.configure(state='normal')
        if text is not None:
            self.Text = str(text)
            self.TKCheckbutton.configure(text=self.Text)
        if background_color is not None:
            self.TKCheckbutton.configure(background=background_color)
            self.BackgroundColor = background_color
        if text_color is not None:
            self.TKCheckbutton.configure(fg=text_color)
            self.TextColor = text_color
        if self.TextColor is not None and self.BackgroundColor is not None and self.TextColor.startswith('#') and self.BackgroundColor.startswith('#'):
            # ---- compute color of circle background ---
            # try:        # something in here will fail if a color is not specified in Hex
            text_hsl = _hex_to_hsl(self.TextColor)
            background_hsl = _hex_to_hsl(self.BackgroundColor if self.BackgroundColor else theme_background_color())
            # print(f'backgroundHSL = {background_hsl}')
            l_delta = abs(text_hsl[2] - background_hsl[2])/10
            if text_hsl[2] > background_hsl[2]:      # if the text is "lighter" than the background then make background darker
                bg_rbg = _hsl_to_rgb(background_hsl[0], background_hsl[1], background_hsl[2]-l_delta)
            else:
                bg_rbg = _hsl_to_rgb(background_hsl[0], background_hsl[1],background_hsl[2]+l_delta)
            self.CheckboxBackgroundColor = RGB(*bg_rbg)
            # except Exception as e:
            #     self.CheckboxBackgroundColor = self.BackgroundColor if self.BackgroundColor else theme_background_color()
            #     print(f'Update exception {e}')
            # print(f'Setting checkbox background = {self.CheckboxBackgroundColor}')
            self.TKCheckbutton.configure(selectcolor=self.CheckboxBackgroundColor)  # The background of the checkbox

        if visible is False:
            self.TKCheckbutton.pack_forget()
        elif visible is True:
            self.TKCheckbutton.pack(padx=self.pad_used[0], pady=self.pad_used[1])

    get = Get
    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update


# -------------------------  CHECKBOX Element lazy functions  ------------------------- #
CB = Checkbox
CBox = Checkbox
Check = Checkbox


# ---------------------------------------------------------------------- #
#                           Spin                                         #
# ---------------------------------------------------------------------- #

class Spin(Element):
    """
    A spinner with up/down buttons and a single line of text. Choose 1 values from list
    """

    def __init__(self, values, initial_value=None, disabled=False, change_submits=False, enable_events=False,
                 size=(None, None), auto_size_text=None, font=None, background_color=None, text_color=None, key=None,
                 pad=None, tooltip=None, visible=True, metadata=None):
        """
        :param values: List of valid values
        :type values: List[Any]
        :param initial_value: Initial item to show in window. Choose from list of values supplied
        :type initial_value: (Any)
        :param disabled: set disable state
        :type disabled: (bool)
        :param change_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type change_submits: (bool)
        :param enable_events: Turns on the element specific events. Spin events happen when an item changes
        :type enable_events: (bool)
        :param size: (width, height) width = characters-wide, height = rows-high
        :type size: Tuple[int, int]
        :param auto_size_text: if True will size the element to match the length of the text
        :type auto_size_text: (bool)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param background_color: color of background
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param key: Used with window.FindElement and with return values to uniquely identify this element
        :type key: (Any)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.Values = values
        self.DefaultValue = initial_value
        self.ChangeSubmits = change_submits or enable_events
        self.TKSpinBox = self.Widget = None  # type: tk.Spinbox
        self.Disabled = disabled
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR

        super().__init__(ELEM_TYPE_INPUT_SPIN, size, auto_size_text, font=font, background_color=bg, text_color=fg,
                         key=key, pad=pad, tooltip=tooltip, visible=visible, metadata=metadata)
        return

    def Update(self, value=None, values=None, disabled=None, visible=None):
        """
        Changes some of the settings for the Spin Element. Must call `Window.Read` or `Window.Finalize` prior
        :param value: set the current value from list of choices
        :type value: (Any)
        :param values: set available choices
        :type values: List[Any]
        :param disabled: disable or enable state of the element
        :type disabled: (bool)
        :param visible: control visibility of element
        :type visible: (bool)
        """

        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if values != None:
            old_value = self.TKStringVar.get()
            self.Values = values
            self.TKSpinBox.configure(values=values)
            self.TKStringVar.set(old_value)
        if value is not None:
            try:
                self.TKStringVar.set(value)
            except:
                pass
        self.DefaultValue = value
        if disabled is not None:
            self.TKSpinBox.configure(state='disabled' if disabled else 'normal')
        # if disabled == True:
        #     self.TKSpinBox.configure(state='disabled')
        # elif disabled == False:
        #     self.TKSpinBox.configure(state='normal')
        if visible is False:
            self.TKSpinBox.pack_forget()
        elif visible is True:
            self.TKSpinBox.pack(padx=self.pad_used[0], pady=self.pad_used[1])

    def _SpinChangedHandler(self, event):
        """
        Callback function. Used internally only. Called by tkinter when Spinbox Widget changes.  Results in Window.Read() call returning

        :param event: passed in from tkinter
        """
        # first, get the results table built
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

    def Get(self):
        """
        Return the current chosen value showing in spinbox.
        This value will be the same as what was provided as list of choices.  If list items are ints, then the
        item returned will be an int (not a string)

        :return: The currently visible entry
        :rtype: (Any)
        """
        return self.TKStringVar.get()

    get = Get
    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update


# ---------------------------------------------------------------------- #
#                           Multiline                                    #
# ---------------------------------------------------------------------- #
class Multiline(Element):
    """
    Multiline Element - Display and/or read multiple lines of text.  This is both an input and output element.
    Other PySimpleGUI ports have a separate MultilineInput and MultilineOutput elements.  May want to split this
    one up in the future too.
    """

    def __init__(self, default_text='', enter_submits=False, disabled=False, autoscroll=False, border_width=None,
                 size=(None, None), auto_size_text=None, background_color=None, text_color=None, change_submits=False,
                 enable_events=False, do_not_clear=True, key=None, focus=False, font=None, pad=None, tooltip=None,
                 right_click_menu=None, visible=True, metadata=None):
        """
        :param default_text: Initial text to show
        :type default_text: (str)
        :param enter_submits: if True, the Window.Read call will return is enter key is pressed in this element
        :type enter_submits: (bool)
        :param disabled: set disable state
        :type disabled: (bool)
        :param autoscroll: If True the contents of the element will automatically scroll as more data added to the end
        :type autoscroll: (bool)
        :param border_width: width of border around element in pixels
        :type border_width: (int)
        :param size: int] (width, height) width = characters-wide, height = rows-high
        :type size: Tuple[int,
        :param auto_size_text: if True will size the element to match the length of the text
        :type auto_size_text: (bool)
        :param background_color: color of background
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param chfange_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type chfange_submits: (bool)
        :param enable_events: Turns on the element specific events. Spin events happen when an item changes
        :type enable_events: (bool)
        :param do_not_clear: if False the element will be cleared any time the Window.Read call returns
        :type do_not_clear: bool
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param focus: if True initial focus will go to this element
        :type focus: (bool)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param right_click_menu: A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
        :type right_click_menu: List[List[Union[List[str],str]]]
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.DefaultText = default_text
        self.EnterSubmits = enter_submits
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        self.Focus = focus
        self.do_not_clear = do_not_clear
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR
        self.Autoscroll = autoscroll
        self.Disabled = disabled
        self.ChangeSubmits = change_submits or enable_events
        self.RightClickMenu = right_click_menu
        self.BorderWidth = border_width if border_width is not None else DEFAULT_BORDER_WIDTH
        self.TagCounter = 0
        self.TKText = self.Widget = None  # type: tkst.ScrolledText
        super().__init__(ELEM_TYPE_INPUT_MULTILINE, size=size, auto_size_text=auto_size_text, background_color=bg,
                         text_color=fg, key=key, pad=pad, tooltip=tooltip, font=font or DEFAULT_FONT, visible=visible, metadata=metadata)
        return

    def Update(self, value=None, disabled=None, append=False, font=None, text_color=None, background_color=None, text_color_for_value=None,
               background_color_for_value=None, visible=None, autoscroll=None):
        """
        Changes some of the settings for the Multiline Element. Must call `Window.Read` or `Window.Finalize` prior
        :param value: new text to display
        :type value: (str)
        :param disabled: disable or enable state of the element
        :type disabled: (bool)
        :param append: if True then new value will be added onto the end of the current value. if False then contents will be replaced.
        :type append: (bool)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param text_color: color of the text
        :type text_color: (str)
        :param background_color: color of background
        :type background_color: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param autoscroll: if True then contents of element are scrolled down when new text is added to the end
        :type autoscroll: (bool)
        """
        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if autoscroll is not None:
            self.Autoscroll = autoscroll
        # Multicolored text
        if text_color_for_value is not None:
            self.TKText.tag_configure(str(self.TagCounter), foreground=text_color_for_value)
        if background_color_for_value is not None:
            self.TKText.tag_configure(str(self.TagCounter), background=background_color_for_value)

        if value is not None:
            value = str(value)
            if self.Disabled:
                self.TKText.configure(state='normal')
            try:
                if not append:
                    self.TKText.delete('1.0', tk.END)
                if text_color_for_value is not None or background_color_for_value is not None:
                    self.TKText.insert(tk.END, value, str(self.TagCounter))
                else:
                    self.TKText.insert(tk.END, value)
            except:
                pass
            if self.Disabled:
                self.TKText.configure(state='disabled')
            self.DefaultText = value
        if self.Autoscroll:
            self.TKText.see(tk.END)
        if disabled is True:
            self.TKText.configure(state='disabled')
        elif disabled is False:
            self.TKText.configure(state='normal')
        if background_color is not None:
            self.TKText.configure(background=background_color)
        if text_color is not None:
            self.TKText.configure(fg=text_color)
        if font is not None:
            self.TKText.configure(font=font)
        if visible is False:
            self.TKText.pack_forget()
        elif visible is True:
            self.TKText.pack(padx=self.pad_used[0], pady=self.pad_used[1])
        self.TagCounter += 1  # doesn't matter if the counter is bumped every call

    def Get(self):
        """
        Return current contents of the Multiline Element

        :return: current contents of the Multiline Element (used as an input type of Multiline
        :rtype: (str)
        """

        return self.TKText.get(1.0, tk.END)



    def print(self, *args, end=None, sep=None, text_color=None, background_color=None):
        """
        Print like Python normally prints except route the output to a multline element and also add colors if desired

        :param args: The arguments to print
        :type args: List[Any]
        :param end: The end char to use just like print uses
        :type end: (str)
        :param sep: The separation character like print uses
        :type sep: (str)
        :param text_color: The color of the text
        :type text_color: (str)
        :param background_color: The background color of the line
        :type background_color: (str)
        """
        _print_to_element(self, *args, end=end, sep=sep, text_color=text_color, background_color=background_color)



    get = Get
    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update


ML = Multiline
MLine = Multiline


# ---------------------------------------------------------------------- #
#                                       Text                             #
# ---------------------------------------------------------------------- #
class Text(Element):
    """
    Text - Display some text in the window.  Usually this means a single line of text.  However, the text can also be multiple lines.  If multi-lined there are no scroll bars.
    """

    def __init__(self, text='', size=(None, None), auto_size_text=None, click_submits=False, enable_events=False,
                 relief=None, font=None, text_color=None, background_color=None, border_width=None, justification=None, pad=None, key=None,
                 right_click_menu=None, tooltip=None, visible=True, metadata=None):
        """
        :param text: The text to display. Can include /n to achieve multiple lines
        :type text: (str)
        :param size: (width, height) width = characters-wide, height = rows-high
        :type size: Tuple[int, int]
        :param auto_size_text: if True size of the Text Element will be sized to fit the string provided in 'text' parm
        :type auto_size_text: (bool)
        :param click_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type click_submits: (bool)
        :param enable_events: Turns on the element specific events. Text events happen when the text is clicked
        :type enable_events: (bool)
        :param relief: relief style around the text. Values are same as progress meter relief values. Should be a constant that is defined at starting with "RELIEF_" - `RELIEF_RAISED, RELIEF_SUNKEN, RELIEF_FLAT, RELIEF_RIDGE, RELIEF_GROOVE, RELIEF_SOLID`
        :type relief: (str/enum)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param text_color: color of the text
        :type text_color: (str)
        :param background_color: color of background
        :type background_color: (str)
        :param border_width: number of pixels for the border (if using a relief)
        :type border_width: (int)
        :param justification: how string should be aligned within space provided by size. Valid choices = `left`, `right`, `center`
        :type justification: (str)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param right_click_menu: A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
        :type right_click_menu: List[List[Union[List[str],str]]]
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.DisplayText = str(text)
        self.TextColor = text_color if text_color else DEFAULT_TEXT_COLOR
        self.Justification = justification
        self.Relief = relief
        self.ClickSubmits = click_submits or enable_events
        if background_color is None:
            bg = DEFAULT_TEXT_ELEMENT_BACKGROUND_COLOR
        else:
            bg = background_color
        self.RightClickMenu = right_click_menu
        self.TKRightClickMenu = None
        self.BorderWidth = border_width

        super().__init__(ELEM_TYPE_TEXT, size, auto_size_text, background_color=bg, font=font if font else DEFAULT_FONT,
                         text_color=self.TextColor, pad=pad, key=key, tooltip=tooltip, visible=visible, metadata=metadata)

    def Update(self, value=None, background_color=None, text_color=None, font=None, visible=None):
        """
        Changes some of the settings for the Text Element. Must call `Window.Read` or `Window.Finalize` prior
        :param value: new text to show
        :type value: (str)
        :param background_color: color of background
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param visible: set visibility state of the element
        :type visible: (bool)
        """

        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if value is not None:
            self.DisplayText = str(value)
            self.TKStringVar.set(str(value))
        if background_color is not None:
            self.TKText.configure(background=background_color)
        if text_color is not None:
            self.TKText.configure(fg=text_color)
        if font is not None:
            self.TKText.configure(font=font)
        if visible is False:
            self.TKText.pack_forget()
        elif visible is True:
            self.TKText.pack(padx=self.pad_used[0], pady=self.pad_used[1])

    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update


# -------------------------  Text Element lazy functions  ------------------------- #

Txt = Text  # type: Text
T = Text  # type: Text


# ---------------------------------------------------------------------- #
#                                       StatusBar                        #
# ---------------------------------------------------------------------- #
class StatusBar(Element):
    """
    A StatusBar Element creates the sunken text-filled strip at the bottom. Many Windows programs have this line
    """

    def __init__(self, text, size=(None, None), auto_size_text=None, click_submits=None, enable_events=False,
                 relief=RELIEF_SUNKEN, font=None, text_color=None, background_color=None, justification=None, pad=None,
                 key=None, tooltip=None, visible=True, metadata=None):
        """
        :param text: Text that is to be displayed in the widget
        :type text: (str)
        :param size: (w,h) w=characters-wide, h=rows-high
        :type size: Tuple[(int), (int)]
        :param auto_size_text: True if size should fit the text length
        :type auto_size_text: (bool)
        :param click_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type click_submits: (bool)
        :param enable_events: Turns on the element specific events. StatusBar events occur when the bar is clicked
        :type enable_events: (bool)
        :param relief: relief style. Values are same as progress meter relief values.  Can be a constant or a string: `RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID`
        :type relief: (enum)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param text_color: color of the text
        :type text_color: (str)
        :param background_color: color of background
        :type background_color: (str)
        :param justification: how string should be aligned within space provided by size. Valid choices = `left`, `right`, `center`
        :type justification: (str)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.DisplayText = text
        self.TextColor = text_color if text_color else DEFAULT_TEXT_COLOR
        self.Justification = justification
        self.Relief = relief
        self.ClickSubmits = click_submits or enable_events
        if background_color is None:
            bg = DEFAULT_TEXT_ELEMENT_BACKGROUND_COLOR
        else:
            bg = background_color
        self.TKText = self.Widget = None  # type: tk.Label
        super().__init__(ELEM_TYPE_STATUSBAR, size=size, auto_size_text=auto_size_text, background_color=bg,
                         font=font or DEFAULT_FONT, text_color=self.TextColor, pad=pad, key=key, tooltip=tooltip,
                         visible=visible, metadata=metadata)
        return

    def Update(self, value=None, background_color=None, text_color=None, font=None, visible=None):
        """
        Changes some of the settings for the Status Bar Element. Must call `Window.Read` or `Window.Finalize` prior
        :param value: new text to show
        :type value: (str)
        :param background_color: color of background
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param visible: set visibility state of the element
        :type visible: (bool)
        """

        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if value is not None:
            self.DisplayText = value
            stringvar = self.TKStringVar
            stringvar.set(value)
        if background_color is not None:
            self.TKText.configure(background=background_color)
        if text_color is not None:
            self.TKText.configure(fg=text_color)
        if font is not None:
            self.TKText.configure(font=font)
        if visible is False:
            self.TKText.pack_forget()
        elif visible is True:
            self.TKText.pack(padx=self.pad_used[0], pady=self.pad_used[1])

    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update


# ---------------------------------------------------------------------- #
#                       TKProgressBar                                    #
#  Emulate the TK ProgressBar using canvas and rectangles
# ---------------------------------------------------------------------- #

class TKProgressBar():

    def __init__(self, root, max, length=400, width=DEFAULT_PROGRESS_BAR_SIZE[1], style=DEFAULT_TTK_THEME,
                 relief=DEFAULT_PROGRESS_BAR_RELIEF, border_width=DEFAULT_PROGRESS_BAR_BORDER_WIDTH,
                 orientation='horizontal', BarColor=(None, None), key=None):
        """
        :param root: The root window bar is to be shown in
        :type root: Union[tk.Tk, tk.TopLevel]
        :param max: Maximum value the bar will be measuring
        :type max: (int)
        :param length: length in pixels of the bar
        :type length: (int)
        :param width: width in pixels of the bar
        :type width: (int)
        :param style: Progress bar style defined as one of these 'default', 'winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative'
        :type style: (str)
        :param relief: relief style. Values are same as progress meter relief values.  Can be a constant or a string: `RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID` (Default value = DEFAULT_PROGRESS_BAR_RELIEF)
        :type relief: (str)
        :param border_width: The amount of pixels that go around the outside of the bar
        :type border_width: (int)
        :param orientation: 'horizontal' or 'vertical' ('h' or 'v' work) (Default value = 'vertical')
        :type orientation: (str)
        :param BarColor: The 2 colors that make up a progress bar. One is the background, the other is the bar
        :type BarColor: Tuple[str, str]
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        """

        self.Length = length
        self.Width = width
        self.Max = max
        self.Orientation = orientation
        self.Count = None
        self.PriorCount = 0

        if orientation.lower().startswith('h'):
            s = ttk.Style()
            s.theme_use(style)
            if BarColor != COLOR_SYSTEM_DEFAULT:
                s.configure(str(key) + "my.Horizontal.TProgressbar", background=BarColor[0], troughcolor=BarColor[1],
                            troughrelief=relief, borderwidth=border_width, thickness=width)
            else:
                s.configure(str(key) + "my.Horizontal.TProgressbar", troughrelief=relief, borderwidth=border_width,
                            thickness=width)

            self.TKProgressBarForReal = ttk.Progressbar(root, maximum=self.Max,
                                                        style=str(key) + 'my.Horizontal.TProgressbar', length=length,
                                                        orient=tk.HORIZONTAL, mode='determinate')
        else:
            s = ttk.Style()
            s.theme_use(style)
            if BarColor != COLOR_SYSTEM_DEFAULT:
                s.configure(str(key) + "my.Vertical.TProgressbar", background=BarColor[0],
                            troughcolor=BarColor[1], troughrelief=relief, borderwidth=border_width, thickness=width)
            else:
                s.configure(str(key) + "my.Vertical.TProgressbar", troughrelief=relief,
                            borderwidth=border_width, thickness=width)
            self.TKProgressBarForReal = ttk.Progressbar(root, maximum=self.Max,
                                                        style=str(key) + 'my.Vertical.TProgressbar',
                                                        length=length, orient=tk.VERTICAL, mode='determinate')

    def Update(self, count=None, max=None):
        """
        Update the current value of the bar and/or update the maximum value the bar can reach
        :param count: current value
        :type count: (int)
        :param max: the maximum value
        :type max: (int)
        """
        if max is not None:
            self.Max = max
            try:
                self.TKProgressBarForReal.config(maximum=max)
            except:
                return False
        if count is not None:
            try:
                self.TKProgressBarForReal['value'] = count
            except:
                return False
        return True


# ---------------------------------------------------------------------- #
#                           TKOutput                                     #
#   New Type of TK Widget that's a Text Widget in disguise               #
#       Note that it's inherited from the TKFrame class so that the      #
#       Scroll bar will span the length of the frame                     #
# ---------------------------------------------------------------------- #
class TKOutput(tk.Frame):
    """
    tkinter style class. Inherits Frame class from tkinter. Adds a tk.Text and a scrollbar together.
    Note - This is NOT a user controlled class. Users should NOT be directly using it unless making an extention
    to PySimpleGUI by directly manipulating tkinter.
    """

    def __init__(self, parent, width, height, bd, background_color=None, text_color=None, font=None, pad=None):
        """
        :param parent: The "Root" that the Widget will be in
        :type parent: Union[tk.Tk, tk.Toplevel]
        :param width: Width in characters
        :type width: (int)
        :param height: height in rows
        :type height: (int)
        :param bd: Border Depth.  How many pixels of border to show
        :type bd: (int)
        :param background_color: color of background
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        """
        self.frame = tk.Frame(parent)
        tk.Frame.__init__(self, self.frame)
        self.output = tk.Text(self.frame, width=width, height=height, bd=bd, font=font)
        if background_color and background_color != COLOR_SYSTEM_DEFAULT:
            self.output.configure(background=background_color)
            self.frame.configure(background=background_color)
        if text_color and text_color != COLOR_SYSTEM_DEFAULT:
            self.output.configure(fg=text_color)
        self.vsb = tk.Scrollbar(self.frame, orient="vertical", command=self.output.yview)
        self.output.configure(yscrollcommand=self.vsb.set)
        self.output.pack(side="left", fill="both", expand=True)
        self.vsb.pack(side="left", fill="y", expand=False)
        self.frame.pack(side="left", padx=pad[0], pady=pad[1], expand=True, fill='y')
        self.previous_stdout = sys.stdout
        self.previous_stderr = sys.stderr

        sys.stdout = self
        sys.stderr = self
        self.pack()

    def write(self, txt):
        """
        Called by Python (not tkinter?) when stdout or stderr wants to write

        :param txt: text of output
        :type txt: (str)
        """
        try:
            self.output.insert(tk.END, str(txt))
            self.output.see(tk.END)
        except:
            pass

    def Close(self):
        """
        Called when wanting to restore the old stdout/stderr
        """
        sys.stdout = self.previous_stdout
        sys.stderr = self.previous_stderr

    def flush(self):
        """
        This doesn't look right.  This restores stdout and stderr to their old values
        """
        sys.stdout = self.previous_stdout
        sys.stderr = self.previous_stderr

    def __del__(self):
        """
        If this Widget is deleted, be sure and restore the old stdout, stderr
        """
        sys.stdout = self.previous_stdout
        sys.stderr = self.previous_stderr


# ---------------------------------------------------------------------- #
#                           Output                                       #
#  Routes stdout, stderr to a scrolled window                            #
# ---------------------------------------------------------------------- #
class Output(Element):
    """
    Output Element - a multi-lined text area where stdout and stderr are re-routed to.
    """

    def __init__(self, size=(None, None), background_color=None, text_color=None, pad=None, font=None, tooltip=None,
                 key=None, right_click_menu=None, visible=True, metadata=None):
        """
        :param size: (width, height) w=characters-wide, h=rows-high
        :type size: Tuple[int, int]
        :param background_color: color of background
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param right_click_menu: A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
        :type right_click_menu: List[List[Union[List[str],str]]]
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self._TKOut = self.Widget = None  # type: TKOutput
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR
        self.RightClickMenu = right_click_menu

        super().__init__(ELEM_TYPE_OUTPUT, size=size, background_color=bg, text_color=fg, pad=pad, font=font,
                         tooltip=tooltip, key=key, visible=visible, metadata=metadata)

    @property
    def TKOut(self):
        """
        Returns the TKOutput object used to create the element

        :return: The TKOutput object
        :rtype: (TKOutput)
        """
        if self._TKOut is None:
            print('*** Did you forget to call Finalize()? Your code should look something like: ***')
            print('*** form = sg.Window("My Form").Layout(layout).Finalize() ***')
        return self._TKOut

    def Update(self, value=None, visible=None):
        """
        Changes some of the settings for the Output Element. Must call `Window.Read` or `Window.Finalize` prior

        :param value: string that will replace current contents of the output area
        :type value: (str)
        :param visible: control visibility of element
        :type visible: (bool)
        """
        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if value is not None:
            self._TKOut.output.delete('1.0', tk.END)
            self._TKOut.output.insert(tk.END, value)
        if visible is False:
            self._TKOut.frame.pack_forget()
        elif visible is True:
            self._TKOut.frame.pack(padx=self.pad_used[0], pady=self.pad_used[1])

    def Get(self):
        """
        Returns the current contents of the output.  Similar to Get method other Elements
        :return: the current value of the output
        :rtype: (str)
        """
        return self._TKOut.output.get(1.0, tk.END)

    def expand(self, expand_x=False, expand_y=False, expand_row=True):
        """
        Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

        :param expand_x: If True Element will expand in the Horizontal directions
        :type expand_x: (Bool)
        :param expand_y: If True Element will expand in the Vertical directions
        :type expand_y: (Bool)
        """

        if expand_x and expand_y:
            fill = tk.BOTH
        elif expand_x:
            fill = tk.X
        elif expand_y:
            fill = tk.Y
        else:
            return

        self._TKOut.output.pack(expand=True, fill=fill)
        self._TKOut.frame.pack(expand=True, fill=fill)
        self.ParentRowFrame.pack(expand=expand_row, fill=fill)

    def __del__(self):
        """
        Delete this element. Normally Elements do not have their delete method specified, but for this one
        it's important that the underlying TKOut object get deleted so that the stdout will get restored properly
        """
        self._TKOut.__del__()

    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    tk_out = TKOut
    update = Update


# ---------------------------------------------------------------------- #
#                           Button Class                                 #
# ---------------------------------------------------------------------- #
class Button(Element):
    """
    Button Element - Defines all possible buttons. The shortcuts such as Submit, FileBrowse, ... each create a Button
    """

    def __init__(self, button_text='', button_type=BUTTON_TYPE_READ_FORM, target=(None, None), tooltip=None,
                 file_types=(("ALL Files", "*.*"),), initial_folder=None, disabled=False, change_submits=False,
                 enable_events=False, image_filename=None, image_data=None, image_size=(None, None),
                 image_subsample=None, border_width=None, size=(None, None), auto_size_button=None, button_color=None, disabled_button_color=None,
                 use_ttk_buttons=None,
                 font=None, bind_return_key=False, focus=False, pad=None, key=None, visible=True, metadata=None):
        """
        :param button_text: Text to be displayed on the button
        :type button_text: (str)
        :param button_type: You  should NOT be setting this directly. ONLY the shortcut functions set this
        :type button_type: (int)
        :param target: key or (row,col) target for the button. Note that -1 for column means 1 element to the left of this one. The constant ThisRow is used to indicate the current row. The Button itself is a valid target for some types of button
        :type target: Union[str, Tuple[int, int]]
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param file_types: the filetypes that will be used to match files. To indicate all files: (("ALL Files", "*.*"),).  Note - NOT SUPPORTED ON MAC
        :type file_types: Tuple[Tuple[str, str], ...]
        :param initial_folder: starting path for folders and files
        :type initial_folder: (str)
        :param disabled: If True button will be created disabled
        :type disabled: (bool)
        :param click_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type click_submits: (bool)
        :param enable_events: Turns on the element specific events. If this button is a target, should it generate an event when filled in
        :type enable_events: (bool)
        :param image_filename: image filename if there is a button image. GIFs and PNGs only.
        :type image_filename: (str)
        :param image_data: Raw or Base64 representation of the image to put on button. Choose either filename or data
        :type image_data: Union[bytes, str]
        :param image_size: Size of the image in pixels (width, height)
        :type image_size: Tuple[int, int]
        :param image_subsample: amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc
        :type image_subsample: (int)
        :param border_width: width of border around button in pixels
        :type border_width: (int)
        :param size: (width, height) of the button in characters wide, rows high
        :type size: Tuple[int, int]
        :param auto_size_button: if True the button size is sized to fit the text
        :type auto_size_button: (bool)
        :param button_color: (text color, background color) of button. Easy to remember which is which if you say "ON" between colors. "red" on "green".
        :type button_color: Tuple[str, str]
        :param disabled_button_color: colors to use when button is disabled (text, background). Use None for a color if don't want to change. Only ttk buttons support both text and background colors. tk buttons only support changing text color
        :type disabled_button_color: Tuple[str, str]
        :param use_ttk_buttons: True = use ttk buttons. False = do not use ttk buttons.  None (Default) = use ttk buttons only if on a Mac and not with button images
        :type use_ttk_buttons: (bool)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param bind_return_key: If True the return key will cause this button to be pressed
        :type bind_return_key: (bool)
        :param focus: if True, initial focus will be put on this button
        :type focus: (bool)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.AutoSizeButton = auto_size_button
        self.BType = button_type
        self.FileTypes = file_types
        self.Widget = self.TKButton = None  # type: tk.Button
        self.Target = target
        self.ButtonText = str(button_text)
        self.ButtonColor = button_color if button_color != None else DEFAULT_BUTTON_COLOR
        self.DisabledButtonColor = disabled_button_color if disabled_button_color is not None else (None, None)
        self.ImageFilename = image_filename
        self.ImageData = image_data
        self.ImageSize = image_size
        self.ImageSubsample = image_subsample
        self.UserData = None
        self.BorderWidth = border_width if border_width is not None else DEFAULT_BORDER_WIDTH
        self.BindReturnKey = bind_return_key
        self.Focus = focus
        self.TKCal = None
        self.CalendarCloseWhenChosen = None
        self.DefaultDate_M_D_Y = (None, None, None)
        self.InitialFolder = initial_folder
        self.Disabled = disabled
        self.ChangeSubmits = change_submits or enable_events
        self.UseTtkButtons = use_ttk_buttons
        if sys.platform.startswith('darwin'):
            self.UseTtkButtons = True
        # if image_filename or image_data:
        #     self.UseTtkButtons = False              # if an image is to be displayed, then force the button to not be a TTK Button
        super().__init__(ELEM_TYPE_BUTTON, size=size, font=font, pad=pad, key=key, tooltip=tooltip, visible=visible, metadata=metadata)
        return

    # Realtime button release callback
    def ButtonReleaseCallBack(self, parm):
        """
        Not a user callable function.  Called by tkinter when a "realtime" button is released

        :param parm: the event info from tkinter

        """
        self.LastButtonClickedWasRealtime = False
        self.ParentForm.LastButtonClicked = None

    # Realtime button callback
    def ButtonPressCallBack(self, parm):
        """
        Not a user callable method. Callback called by tkinter when a "realtime" button is pressed

        :param parm: Event info passed in by tkinter

        """
        self.ParentForm.LastButtonClickedWasRealtime = True
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = self.ButtonText
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick out of loop if read was called

    # -------  Button Callback  ------- #
    def ButtonCallBack(self):
        """
        Not user callable! Called by tkinter when a button is clicked.  This is where all the fun begins!
        """
        # global _my_windows

        # print('Button callback')

        # print(f'Button Callback - Parent = {self.ParentForm}   Position = {self.Position}')
        # Buttons modify targets or return from the form
        # If modifying target, get the element object at the target and modify its StrVar
        target = self.Target
        target_element = None
        if target[0] == ThisRow:
            target = [self.Position[0], target[1]]
            if target[1] < 0:
                target[1] = self.Position[1] + target[1]
        strvar = None
        should_submit_window = False
        if target == (None, None):
            strvar = self.TKStringVar
        else:
            if not isinstance(target, str):
                if target[0] < 0:
                    target = [self.Position[0] + target[0], target[1]]
                target_element = self.ParentContainer._GetElementAtLocation(target)
            else:
                target_element = self.ParentForm.FindElement(target)
            try:
                strvar = target_element.TKStringVar
            except:
                pass
            try:
                if target_element.ChangeSubmits:
                    should_submit_window = True
            except:
                pass
        filetypes = (("ALL Files", "*.*"),) if self.FileTypes is None else self.FileTypes
        if self.BType == BUTTON_TYPE_BROWSE_FOLDER:
            folder_name = tk.filedialog.askdirectory(initialdir=self.InitialFolder, parent=self.ParentForm.TKroot)  # show the 'get folder' dialog box
            if folder_name:
                try:
                    strvar.set(folder_name)
                    self.TKStringVar.set(folder_name)
                except:
                    pass
        elif self.BType == BUTTON_TYPE_BROWSE_FILE:
            if sys.platform == 'darwin':
                file_name = tk.filedialog.askopenfilename(
                    initialdir=self.InitialFolder)  # show the 'get file' dialog box
            else:
                file_name = tk.filedialog.askopenfilename(filetypes=filetypes,
                                                          initialdir=self.InitialFolder, parent=self.ParentForm.TKroot)  # show the 'get file' dialog box
            if file_name:
                strvar.set(file_name)
                self.TKStringVar.set(file_name)
        elif self.BType == BUTTON_TYPE_COLOR_CHOOSER:
            color = tk.colorchooser.askcolor()  # show the 'get file' dialog box
            color = color[1]  # save only the #RRGGBB portion
            strvar.set(color)
            self.TKStringVar.set(color)
        elif self.BType == BUTTON_TYPE_BROWSE_FILES:
            if sys.platform == 'darwin':
                file_name = tk.filedialog.askopenfilenames(initialdir=self.InitialFolder)
            else:
                file_name = tk.filedialog.askopenfilenames(filetypes=filetypes, initialdir=self.InitialFolder, parent=self.ParentForm.TKroot)
            if file_name:
                file_name = BROWSE_FILES_DELIMITER.join(file_name)  # normally a ';'
                strvar.set(file_name)
                self.TKStringVar.set(file_name)
        elif self.BType == BUTTON_TYPE_SAVEAS_FILE:
            if sys.platform == 'darwin':
                file_name = tk.filedialog.asksaveasfilename(
                    initialdir=self.InitialFolder)  # show the 'get file' dialog box
            else:
                file_name = tk.filedialog.asksaveasfilename(filetypes=filetypes,
                                                            initialdir=self.InitialFolder, parent=self.ParentForm.TKroot)  # show the 'get file' dialog box
            if file_name:
                strvar.set(file_name)
                self.TKStringVar.set(file_name)
        elif self.BType == BUTTON_TYPE_CLOSES_WIN:  # this is a return type button so GET RESULTS and destroy window
            # first, get the results table built
            # modify the Results table in the parent FlexForm object
            if self.Key is not None:
                self.ParentForm.LastButtonClicked = self.Key
            else:
                self.ParentForm.LastButtonClicked = self.ButtonText
            self.ParentForm.FormRemainedOpen = False
            self.ParentForm._Close()
            if self.ParentForm.CurrentlyRunningMainloop:
                self.ParentForm.TKroot.quit()
            if self.ParentForm.NonBlocking:
                self.ParentForm.TKroot.destroy()
                Window._DecrementOpenCount()
        elif self.BType == BUTTON_TYPE_READ_FORM:  # LEAVE THE WINDOW OPEN!! DO NOT CLOSE
            # first, get the results table built
            # modify the Results table in the parent FlexForm object
            if self.Key is not None:
                self.ParentForm.LastButtonClicked = self.Key
            else:
                self.ParentForm.LastButtonClicked = self.ButtonText
            self.ParentForm.FormRemainedOpen = True
            if self.ParentForm.CurrentlyRunningMainloop:  # if this window is running the mainloop, kick out
                self.ParentForm.TKroot.quit()  # kick the users out of the mainloop
        elif self.BType == BUTTON_TYPE_CLOSES_WIN_ONLY:  # special kind of button that does not exit main loop
            self.ParentForm._Close()
            if self.ParentForm.NonBlocking:
                self.ParentForm.TKroot.destroy()
                Window._DecrementOpenCount()
        elif self.BType == BUTTON_TYPE_CALENDAR_CHOOSER:  # this is a return type button so GET RESULTS and destroy window
            should_submit_window = False
            root = tk.Toplevel()
            root.title('Calendar Chooser')
            root.wm_attributes("-topmost", 1)
            self.TKCal = TKCalendar(master=root, firstweekday=calendar.SUNDAY, target_element=target_element,
                                    close_when_chosen=self.CalendarCloseWhenChosen, default_date=self.DefaultDate_M_D_Y,
                                    locale=self.CalendarLocale, format=self.CalendarFormat)
            self.TKCal.pack(expand=1, fill='both')
            root.update()

            if type(Window._user_defined_icon) is bytes:
                calendar_icon = tkinter.PhotoImage(data=Window._user_defined_icon)
            else:
                calendar_icon = tkinter.PhotoImage(data=DEFAULT_BASE64_ICON)
            try:
                root.tk.call('wm', 'iconphoto', root._w, calendar_icon)
            except:
                pass
        elif self.BType == BUTTON_TYPE_SHOW_DEBUGGER:
            if self.ParentForm.DebuggerEnabled:
                _Debugger.debugger._build_floating_window()
                # show_debugger_window()

        if should_submit_window:
            self.ParentForm.LastButtonClicked = target_element.Key
            self.ParentForm.FormRemainedOpen = True
            if self.ParentForm.CurrentlyRunningMainloop:
                self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

        return

    def Update(self, text=None, button_color=(None, None), disabled=None, image_data=None, image_filename=None,
               visible=None, image_subsample=None, disabled_button_color=(None, None), image_size=None):
        """
        Changes some of the settings for the Button Element. Must call `Window.Read` or `Window.Finalize` prior
        :param text: sets button text
        :type text: (str)
        :param button_color: (text color, background color) of button. Easy to remember which is which if you say "ON" between colors. "red" on "green"
        :type button_color: Tuple[str, str]
        :param disabled: disable or enable state of the element
        :type disabled: (bool)
        :param image_data: Raw or Base64 representation of the image to put on button. Choose either filename or data
        :type image_data: Union[bytes, str]
        :param image_filename: image filename if there is a button image. GIFs and PNGs only.
        :type image_filename: (str)
        :param disabled_button_color: colors to use when button is disabled (text, background). Use None for a color if don't want to change. Only ttk buttons support both text and background colors. tk buttons only support changing text color
        :type disabled_button_color: Tuple[str, str]
        :param visible: control visibility of element
        :type visible: (bool)
        :param image_subsample: amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc
        :type image_subsample: (int)
        :param image_size: Size of the image in pixels (width, height)
        :type image_size: Tuple[int, int]
        """

        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if self.UseTtkButtons:
            style_name = str(self.Key) + 'custombutton.TButton'
            button_style = ttk.Style()
        if text is not None:
            self.TKButton.configure(text=text)
            self.ButtonText = text
        if button_color != (None, None):
            if self.UseTtkButtons:
                if button_color[0] is not None:
                    button_style.configure(style_name, foreground=button_color[0])
                if button_color[1]:
                    button_style.configure(style_name, background=button_color[1])
            else:
                if button_color[0]:
                    self.TKButton.config(foreground=button_color[0])
                if button_color[1]:
                    self.TKButton.config(background=button_color[1], activebackground=button_color[1])
            self.ButtonColor = (button_color[0] if button_color[0] is not None else self.ButtonColor[0],
                                button_color[1] if button_color[1] is not None else self.ButtonColor[1])
        if disabled == True:
            self.TKButton['state'] = 'disabled'
        elif disabled == False:
            self.TKButton['state'] = 'normal'
        if image_data is not None:
            image = tk.PhotoImage(data=image_data)
            if image_size is not None:
                width, height = image_size
            else:
                width, height = image.width(), image.height()
            if image_subsample:
                image = image.subsample(image_subsample)
            if self.UseTtkButtons:
                button_style.configure(style_name, image=image, width=width, height=height)
            else:
                self.TKButton.config(image=image, width=width, height=height)
            self.TKButton.image = image
        if image_filename is not None:
            image = tk.PhotoImage(file=image_filename)
            if image_size is not None:
                width, height = image_size
            else:
                width, height = image.width(), image.height()
            if image_subsample:
                image = image.subsample(image_subsample)
            if self.UseTtkButtons:
                button_style.configure(style_name, image=image, width=width, height=height)
            else:
                self.TKButton.config(highlightthickness=0, image=image, width=width, height=height)
            self.TKButton.image = image
        if visible is False:
            self.TKButton.pack_forget()
        elif visible is True:
            self.TKButton.pack(padx=self.pad_used[0], pady=self.pad_used[1])
        if disabled_button_color != (None, None):
            if not self.UseTtkButtons:
                self.TKButton['disabledforeground'] = disabled_button_color[0]
            else:
                if disabled_button_color[0] is not None:
                    button_style.map(style_name, foreground=[('disabled', disabled_button_color[0])])
                if disabled_button_color[1] is not None:
                    button_style.map(style_name, background=[('disabled', disabled_button_color[1])])
            self.DisabledButtonColor = (disabled_button_color[0] if disabled_button_color[0] is not None else self.DisabledButtonColor[0],
                                        disabled_button_color[1] if disabled_button_color[1] is not None else self.DisabledButtonColor[1])

    def GetText(self):
        """
        Returns the current text shown on a button

        :return: The text currently displayed on the button
        :rtype: (str)
        """
        return self.ButtonText

    def Click(self):
        """
        Generates a click of the button as if the user clicked the button
        Calls the tkinter invoke method for the button
        """
        try:
            self.TKButton.invoke()
        except:
            print('Exception clicking button')

    click = Click
    get_text = GetText
    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update


# -------------------------  Button lazy functions  ------------------------- #
B = Button
Btn = Button


# ---------------------------------------------------------------------- #
#                           ButtonMenu Class                             #
# ---------------------------------------------------------------------- #
class ButtonMenu(Element):
    """
    The Button Menu Element.  Creates a button that when clicked will show a menu similar to right click menu
    """

    def __init__(self, button_text, menu_def, tooltip=None, disabled=False,
                 image_filename=None, image_data=None, image_size=(None, None), image_subsample=None, border_width=None,
                 size=(None, None), auto_size_button=None, button_color=None, font=None, pad=None, key=None,
                 tearoff=False, visible=True, metadata=None):
        """
        :param button_text: Text to be displayed on the button
        :type button_text: (str)
        :param menu_def: A list of lists of Menu items to show when this element is clicked. See docs for format as they are the same for all menu types
        :type menu_def: List[List[str]]
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param disabled: If True button will be created disabled
        :type disabled: (bool)
        :param image_filename: image filename if there is a button image. GIFs and PNGs only.
        :type image_filename: (str)
        :param image_data: Raw or Base64 representation of the image to put on button. Choose either filename or data
        :type image_data: Union[bytes, str]
        :param image_size: Size of the image in pixels (width, height)
        :type image_size: Tuple[int, int]
        :param image_subsample: amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc
        :type image_subsample: (int)
        :param border_width: width of border around button in pixels
        :type border_width: (int)
        :param size:(width, height) of the button in characters wide, rows high
        :type size: Tuple[int, int]
        :param auto_size_button: if True the button size is sized to fit the text
        :type auto_size_button: (bool)
        :param button_color: (text color, background color) of button. Easy to remember which is which if you say "ON" between colors. "red" on "green"
        :type button_color: Tuple[str, str]
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param tearoff: Determines if menus should allow them to be torn off
        :type tearoff: (bool)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.MenuDefinition = menu_def
        self.AutoSizeButton = auto_size_button
        self.ButtonText = button_text
        self.ButtonColor = button_color if button_color else DEFAULT_BUTTON_COLOR
        self.TextColor = self.ButtonColor[0]
        self.BackgroundColor = self.ButtonColor[1]
        self.BorderWidth = border_width
        self.ImageFilename = image_filename
        self.ImageData = image_data
        self.ImageSize = image_size
        self.ImageSubsample = image_subsample
        self.Disabled = disabled
        self.IsButtonMenu = True
        self.MenuItemChosen = None
        self.Tearoff = tearoff
        self.TKButtonMenu = None  # type: tk.Menubutton
        self.TKMenu = None  # type: tk.Menu
        # self.temp_size = size if size != (NONE, NONE) else

        super().__init__(ELEM_TYPE_BUTTONMENU, size=size, font=font, pad=pad, key=key, tooltip=tooltip,
                         text_color=self.TextColor, background_color=self.BackgroundColor, visible=visible, metadata=metadata)
        return

    def _MenuItemChosenCallback(self, item_chosen):  # ButtonMenu Menu Item Chosen Callback
        """
        Not a user callable function.  Called by tkinter when an item is chosen from the menu.

        :param item_chosen: The menu item chosen.
        :type item_chosen: (str)
        """
        # print('IN MENU ITEM CALLBACK', item_chosen)
        self.MenuItemChosen = item_chosen.replace('&', '')
        self.ParentForm.LastButtonClicked = self.Key
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

    def Update(self, menu_definition, visible=None):
        """
        Changes some of the settings for the ButtonMenu Element. Must call `Window.Read` or `Window.Finalize` prior

        :param menu_definition: (New menu definition (in menu definition format)
        :type menu_definition: List[List]
        :param visible: control visibility of element
        :type visible: (bool)
        """

        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        self.MenuDefinition = menu_definition
        if menu_definition is not None:
            self.TKMenu = tk.Menu(self.TKButtonMenu, tearoff=self.Tearoff)  # create the menubar
            AddMenuItem(self.TKMenu, menu_definition[1], self)
        self.TKButtonMenu.configure(menu=self.TKMenu)
        if visible is False:
            self.TKButtonMenu.pack_forget()
        elif visible is True:
            self.TKButtonMenu.pack(padx=self.pad_used[0], pady=self.pad_used[1])

    def Click(self):
        """
        Generates a click of the button as if the user clicked the button
        Calls the tkinter invoke method for the button
        """
        try:
            self.TKMenu.invoke(1)
        except:
            print('Exception clicking button')

    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update


BMenu = ButtonMenu


# ---------------------------------------------------------------------- #
#                           ProgreessBar                                 #
# ---------------------------------------------------------------------- #
class ProgressBar(Element):
    """
    Progress Bar Element - Displays a colored bar that is shaded as progress of some operation is made
    """

    def __init__(self, max_value, orientation=None, size=(None, None), auto_size_text=None, bar_color=(None, None), style=None, border_width=None, relief=None,
                 key=None, pad=None, visible=True, metadata=None):
        """
        :param max_value: max value of progressbar
        :type max_value: (int)
        :param orientation: 'horizontal' or 'vertical'
        :type orientation: (str)
        :param size: Size of the bar.  If horizontal (chars wide, pixels high), vert (pixels wide, rows high)
        :type size: Tuple[int, int]
        :param auto_size_text: Not sure why this is here
        :type auto_size_text: (bool)
        :param bar_color: The 2 colors that make up a progress bar. One is the background, the other is the bar
        :type bar_color: Tuple[str, str]
        :param style: Progress bar style defined as one of these 'default', 'winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative'
        :type style: (str)
        :param border_width: The amount of pixels that go around the outside of the bar
        :type border_width: (int)
        :param relief: relief style. Values are same as progress meter relief values.  Can be a constant or a string: `RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID` (Default value = DEFAULT_PROGRESS_BAR_RELIEF)
        :type relief: (str)
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.MaxValue = max_value
        self.TKProgressBar = None  # type: TKProgressBar
        self.Cancelled = False
        self.NotRunning = True
        self.Orientation = orientation if orientation else DEFAULT_METER_ORIENTATION
        self.BarColor = bar_color
        self.BarStyle = style if style else DEFAULT_TTK_THEME
        self.BorderWidth = border_width if border_width else DEFAULT_PROGRESS_BAR_BORDER_WIDTH
        self.Relief = relief if relief else DEFAULT_PROGRESS_BAR_RELIEF
        self.BarExpired = False
        super().__init__(ELEM_TYPE_PROGRESS_BAR, size=size, auto_size_text=auto_size_text, key=key, pad=pad,
                         visible=visible, metadata=metadata)

    # returns False if update failed
    def UpdateBar(self, current_count, max=None):
        """
        Change what the bar shows by changing the current count and optionally the max count

        :param current_count: sets the current value
        :type current_count: (int)
        :param max: changes the max value
        :type max: (int)
        """

        if self.ParentForm.TKrootDestroyed:
            return False
        self.TKProgressBar.Update(current_count, max=max)
        try:
            self.ParentForm.TKroot.update()
        except:
            Window._DecrementOpenCount()
            # _my_windows.Decrement()
            return False
        return True

    def Update(self, visible=None):
        """
        Changes some of the settings for the ProgressBar Element. Must call `Window.Read` or `Window.Finalize` prior

        :param visible: control visibility of element
        :type visible: (bool)
        """
        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if visible is False:
            self.TKProgressBar.TKProgressBarForReal.pack_forget()
        elif visible is True:
            self.TKProgressBar.TKProgressBarForReal.pack(padx=self.pad_used[0], pady=self.pad_used[1])

    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update
    update_bar = UpdateBar


PBar = ProgressBar
Prog = ProgressBar


# ---------------------------------------------------------------------- #
#                           Image                                        #
# ---------------------------------------------------------------------- #
class Image(Element):
    """
    Image Element - show an image in the window. Should be a GIF or a PNG only
    """

    def __init__(self, filename=None, data=None, background_color=None, size=(None, None), pad=None, key=None,
                 tooltip=None, right_click_menu=None, visible=True, enable_events=False, metadata=None):
        """
        :param filename: image filename if there is a button image. GIFs and PNGs only.
        :type filename: (str)
        :param data: Raw or Base64 representation of the image to put on button. Choose either filename or data
        :type data: Union[bytes, str]
        :param background_color: color of background
        :type background_color:
        :param size: (width, height) size of image in pixels
        :type size: Tuple[int, int]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param right_click_menu: A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
        :type right_click_menu: List[List[Union[List[str],str]]]
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param enable_events: Turns on the element specific events. For an Image element, the event is "image clicked"
        :type enable_events: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.Filename = filename
        self.Data = data
        self.tktext_label = None
        self.BackgroundColor = background_color
        if data is None and filename is None:
            self.Filename = ''
        self.EnableEvents = enable_events
        self.RightClickMenu = right_click_menu
        self.AnimatedFrames = None
        self.CurrentFrameNumber = 0
        self.TotalAnimatedFrames = 0
        self.LastFrameTime = 0
        self.Source = filename if filename is not None else data

        super().__init__(ELEM_TYPE_IMAGE, size=size, background_color=background_color, pad=pad, key=key,
                         tooltip=tooltip, visible=visible, metadata=metadata)
        return

    def Update(self, filename=None, data=None, size=(None, None), visible=None):
        """
        Changes some of the settings for the Image Element. Must call `Window.Read` or `Window.Finalize` prior
        :param filename: filename to the new image to display.
        :type filename: (str)
        :param data: Base64 encoded string OR a tk.PhotoImage object
        :type data: Union[str, tkPhotoImage]
        :param size: size of a image (w,h) w=characters-wide, h=rows-high
        :type size: Tuple[int,int]
        :param visible: control visibility of element
        :type visible: (bool)
        """

        image = None
        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if filename is not None:
            image = tk.PhotoImage(file=filename)
        elif data is not None:
            # if type(data) is bytes:
            try:
                image = tk.PhotoImage(data=data)
            except Exception as e:
                image = data
                # return  # an error likely means the window has closed so exit
        else:
            return
        if image is not None:
            if type(image) is not bytes:
                width, height = size[0] or image.width(), size[1] or image.height()
            else:
                width, height = size
            try:  # sometimes crashes if user closed with X
                self.tktext_label.configure(image=image, width=width, height=height)
            except:
                pass
            self.tktext_label.image = image
        if visible is False:
            self.tktext_label.pack_forget()
        elif visible is True:
            self.tktext_label.pack(padx=self.pad_used[0], pady=self.pad_used[1])

    def UpdateAnimation(self, source, time_between_frames=0):
        """
        Show an Animated GIF. Call the function as often as you like. The function will determine when to show the next frame and will automatically advance to the next frame at the right time.
        NOTE - does NOT perform a sleep call to delay
        :param source: Filename or Base64 encoded string containing Animated GIF
        :type source: Union[str,bytes]
        :param time_between_frames: Number of milliseconds to wait between showing frames
        :type time_between_frames: (int)
        """

        if self.Source != source:
            self.AnimatedFrames = None
            self.Source = source

        if self.AnimatedFrames is None:
            self.TotalAnimatedFrames = 0
            self.AnimatedFrames = []
            for i in range(1000):
                if type(source) is not bytes:
                    try:
                        self.AnimatedFrames.append(tk.PhotoImage(file=source, format='gif -index %i' % (i)))
                    except:
                        break
                else:
                    try:
                        self.AnimatedFrames.append(tk.PhotoImage(data=source, format='gif -index %i' % (i)))
                    except:
                        break
                self.TotalAnimatedFrames += 1
            self.LastFrameTime = time.time()
            self.CurrentFrameNumber = 0
        # show the frame

        now = time.time()

        if time_between_frames:
            if (now - self.LastFrameTime) * 1000 > time_between_frames:
                self.LastFrameTime = now
                self.CurrentFrameNumber = self.CurrentFrameNumber + 1 if self.CurrentFrameNumber + 1 < self.TotalAnimatedFrames else 0
            else:  # don't reshow the frame again if not time for new frame
                return
        else:
            self.CurrentFrameNumber = self.CurrentFrameNumber + 1 if self.CurrentFrameNumber + 1 < self.TotalAnimatedFrames else 0
        image = self.AnimatedFrames[self.CurrentFrameNumber]
        try:  # needed in case the window was closed with an "X"
            self.tktext_label.configure(image=image, width=image.width(), heigh=image.height())
        except:
            pass



    def update_animation_no_buffering(self, source, time_between_frames=0):
        """
        Show an Animated GIF. Call the function as often as you like. The function will determine when to show the next frame and will automatically advance to the next frame at the right time.
        NOTE - does NOT perform a sleep call to delay
        :param source: Filename or Base64 encoded string containing Animated GIF
        :type source: Union[str,bytes]
        :param time_between_frames: Number of milliseconds to wait between showing frames
        :type time_between_frames: (int)
        """

        if self.Source != source:
            self.AnimatedFrames = None
            self.Source = source
            self.frame_num = 0

        # read a frame
        while True:
            if type(source) is not bytes:
                try:
                    self.image = tk.PhotoImage(file=source, format='gif -index %i' % (self.frame_num))
                    self.frame_num += 1
                except:
                    self.frame_num = 0
            else:
                try:
                    self.image = tk.PhotoImage(data=source, format='gif -index %i' % (self.frame_num))
                    self.frame_num += 1
                except:
                    self.frame_num = 0
            if self.frame_num:
                break

        now = time.time()

        if time_between_frames:
            if (now - self.LastFrameTime) * 1000 > time_between_frames:
                self.LastFrameTime = now
            else:  # don't reshow the frame again if not time for new frame
                return

        try:  # needed in case the window was closed with an "X"
            self.tktext_label.configure(image=self.image, width=self.image.width(), heigh=self.image.height())

        except:
            pass





    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update
    update_animation = UpdateAnimation


# ---------------------------------------------------------------------- #
#                           Canvas                                       #
# ---------------------------------------------------------------------- #
class Canvas(Element):

    def __init__(self, canvas=None, background_color=None, size=(None, None), pad=None, key=None, tooltip=None,
                 right_click_menu=None, visible=True, metadata=None):
        """
        :param canvas: Your own tk.Canvas if you already created it. Leave blank to create a Canvas
        :type canvas: (tk.Canvas)
        :param background_color: color of background
        :type background_color: (str)
        :param size: (width in char, height in rows) size in pixels to make canvas
        :type size: Tuple[int,int]
        :param pad:  Amount of padding to put around element
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param key: Used with window.FindElement and with return values to uniquely identify this element
        :type key: (Any)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param right_click_menu: A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
        :type right_click_menu: List[List[Union[List[str],str]]]
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self._TKCanvas = canvas
        self.RightClickMenu = right_click_menu

        super().__init__(ELEM_TYPE_CANVAS, background_color=background_color, size=size, pad=pad, key=key,
                         tooltip=tooltip, visible=visible, metadata=metadata)
        return

    @property
    def TKCanvas(self):
        """
        Returns the underlying tkiner Canvas widget

        :return: The tkinter canvas widget
        :rtype: (tk.Canvas)
        """
        if self._TKCanvas is None:
            print('*** Did you forget to call Finalize()? Your code should look something like: ***')
            print('*** window = sg.Window("My Form", layout, finalize=True) ***')
        return self._TKCanvas

    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    tk_canvas = TKCanvas


# ---------------------------------------------------------------------- #
#                           Graph                                        #
# ---------------------------------------------------------------------- #
class Graph(Element):
    """
    Creates an area for you to draw on.  The MAGICAL property this Element has is that you interact
    with the element using your own coordinate system.  This is an important point!!  YOU define where the location
    is for (0,0).  Want (0,0) to be in the middle of the graph like a math 4-quadrant graph?  No problem!  Set your
    lower left corner to be (-100,-100) and your upper right to be (100,100) and you've got yourself a graph with
    (0,0) at the center.
    One of THE coolest of the Elements.
    You can also use float values. To do so, be sure and set the float_values parameter.
    Mouse click and drag events are possible and return the (x,y) coordinates of the mouse
    Drawing primitives return an "id" that is referenced when you want to operation on that item (e.g. to erase it)
    """

    def __init__(self, canvas_size, graph_bottom_left, graph_top_right, background_color=None, pad=None,
                 change_submits=False, drag_submits=False, enable_events=False, key=None, tooltip=None,
                 right_click_menu=None, visible=True, float_values=False, metadata=None):
        """
        :param canvas_size: (width, height) size of the canvas area in pixels
        :type canvas_size: Tuple[int, int]
        :param graph_bottom_left: (x,y) The bottoms left corner of your coordinate system
        :type graph_bottom_left: Tuple[int, int]
        :param graph_top_right: (x,y) The top right corner of  your coordinate system
        :type graph_top_right: Tuple[int, int]
        :param background_color: background color of the drawing area
        :type background_color: (str)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param change_submits: * DEPRICATED DO NOT USE! Same as enable_events
        :type change_submits: (bool)
        :param drag_submits: if True and Events are enabled for the Graph, will report Events any time the mouse moves while button down
        :type drag_submits: (bool)
        :param enable_events: If True then clicks on the Graph are immediately reported as an event. Use this instead of change_submits
        :type enable_events: (bool)
        :param key: Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
        :type key: (any)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param right_click_menu: A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
        :type right_click_menu: List[List[Union[List[str],str]]]
        :param visible: set visibility state of the element (Default = True)
        :type visible: (bool)
        :param float_values: If True x,y coordinates are returned as floats, not ints
        :type float_values: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.CanvasSize = canvas_size
        self.BottomLeft = graph_bottom_left
        self.TopRight = graph_top_right
        # self._TKCanvas = None               # type: tk.Canvas
        self._TKCanvas2 = self.Widget = None  # type: tk.Canvas
        self.ChangeSubmits = change_submits or enable_events
        self.DragSubmits = drag_submits
        self.ClickPosition = (None, None)
        self.MouseButtonDown = False
        self.Images = {}
        self.RightClickMenu = right_click_menu
        self.FloatValues = float_values

        super().__init__(ELEM_TYPE_GRAPH, background_color=background_color, size=canvas_size, pad=pad, key=key,
                         tooltip=tooltip, visible=visible, metadata=metadata)
        return

    def _convert_xy_to_canvas_xy(self, x_in, y_in):
        """
        Not user callable.  Used to convert user's coordinates into the ones used by tkinter
        :param x_in: The x coordinate to convert
        :type x_in: Union[int, float]
        :param y_in: The y coordinate to convert
        :type y_in: Union[int, float]
        :return: Tuple[int, int] The converted canvas coordinates
        :rtype: Tuple[int, int]
        """
        if None in (x_in, y_in):
            return None, None
        try:
            scale_x = (self.CanvasSize[0] - 0) / (self.TopRight[0] - self.BottomLeft[0])
            scale_y = (0 - self.CanvasSize[1]) / (self.TopRight[1] - self.BottomLeft[1])
        except:
            scale_x = scale_y = 0

        new_x = 0 + scale_x * (x_in - self.BottomLeft[0])
        new_y = self.CanvasSize[1] + scale_y * (y_in - self.BottomLeft[1])
        return new_x, new_y

    def _convert_canvas_xy_to_xy(self, x_in, y_in):
        """
        Not user callable.  Used to convert tkinter Canvas coords into user's coordinates

        :param x_in: (int) The x coordinate in canvas coordinates
        :type x_in: (int)
        :param y_in: (int) The y coordinate in canvas coordinates
        :type y_in: (int)
        :return: The converted USER coordinates
        :rtype: Union[Tuple[int, int], Tuple[float, float]]
        """
        if None in (x_in, y_in):
            return None, None
        scale_x = (self.CanvasSize[0] - 0) / (self.TopRight[0] - self.BottomLeft[0])
        scale_y = (0 - self.CanvasSize[1]) / (self.TopRight[1] - self.BottomLeft[1])

        new_x = x_in / scale_x + self.BottomLeft[0]
        new_y = (y_in - self.CanvasSize[1]) / scale_y + self.BottomLeft[1]
        if self.FloatValues:
            return new_x, new_y
        else:
            return floor(new_x), floor(new_y)

    def DrawLine(self, point_from, point_to, color='black', width=1):
        """
        Draws a line from one point to another point using USER'S coordinates. Can set the color and width of line
        :param point_from: Starting point for line
        :type point_from: Union[Tuple[int, int], Tuple[float, float]]
        :param point_to: Ending point for line
        :type point_to: Union[Tuple[int, int], Tuple[float, float]]
        :param color: Color of the line
        :type color: (str)
        :param width: width of line in pixels
        :type width: (int)
        :return: id returned from tktiner or None if user closed the window. id is used when you
        :rtype: Union[int, None]
        """
        if point_from == (None, None):
            return
        converted_point_from = self._convert_xy_to_canvas_xy(point_from[0], point_from[1])
        converted_point_to = self._convert_xy_to_canvas_xy(point_to[0], point_to[1])
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        try:  # in case window was closed with an X
            id = self._TKCanvas2.create_line(converted_point_from, converted_point_to, width=width, fill=color)
        except:
            id = None
        return id

    def DrawPoint(self, point, size=2, color='black'):
        """
        Draws a "dot" at the point you specify using the USER'S coordinate system
        :param point: Center location using USER'S coordinate system
        :type point: Union [Tuple[int, int], Tuple[float, float]]
        :param size: Radius? (Or is it the diameter?) in user's coordinate values.
        :type size: Union[int, float]
        :param color: color of the point to draw
        :type color: (str)
        :return: id returned from tkinter that you'll need if you want to manipulate the point
        :rtype: Union[int, None]
        """
        if point == (None, None):
            return
        converted_point = self._convert_xy_to_canvas_xy(point[0], point[1])
        size_converted = self._convert_xy_to_canvas_xy(point[0]+size, point[1])
        size = size_converted[0]-converted_point[0]
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        try:  # needed in case window was closed with an X
            point1 = converted_point[0] - size // 2, converted_point[1] - size // 2
            point2 = converted_point[0] + size // 2, converted_point[1] + size // 2
            # print(f'point size = {size} points = {point1} and {point2}')
            id = self._TKCanvas2.create_oval(point1[0], point1[1],
                                             point2[0], point2[1],
                                             width=0,
                                             fill=color,
                                             outline=color)
        except:
            id = None
        return id

    def DrawCircle(self, center_location, radius, fill_color=None, line_color='black', line_width=1):
        """
        Draws a circle, cenetered at the location provided.  Can set the fill and outline colors
        :param center_location: Center location using USER'S coordinate system
        :type center_location: Union [Tuple[int, int], Tuple[float, float]]
        :param radius: Radius in user's coordinate values.
        :type radius: Union[int, float]
        :param fill_color: color of the point to draw
        :type fill_color: (str)
        :param line_color: color of the outer line that goes around the circle (sorry, can't set thickness)
        :type line_color: (str)
        :param line_width: width of the line around the circle, the outline, in pixels
        :type line_width: (int)
        :return: id returned from tkinter that you'll need if you want to manipulate the circle
        :rtype: Union[int, None]
        """
        if center_location == (None, None):
            return
        converted_point = self._convert_xy_to_canvas_xy(center_location[0], center_location[1])
        radius_converted = self._convert_xy_to_canvas_xy(center_location[0]+radius, center_location[1])
        radius = radius_converted[0]-converted_point[0]
        # radius = radius_converted[1]-5
        # print(f'center = {converted_point} radius converted = {radius_converted}')
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        # print('Oval parms', int(converted_point[0]) - int(radius), int(converted_point[1]) - int(radius),
        #                                      int(converted_point[0]) + int(radius), int(converted_point[1]) + int(radius))
        try:  # needed in case the window was closed with an X
            id = self._TKCanvas2.create_oval(int(converted_point[0]) - int(radius), int(converted_point[1]) - int(radius),
                                             int(converted_point[0]) + int(radius), int(converted_point[1]) + int(radius), fill=fill_color,
                                             outline=line_color, width=line_width)
        except:
            id = None
        return id

    def DrawOval(self, top_left, bottom_right, fill_color=None, line_color=None, line_width=1):
        """
        Draws an oval based on coordinates in user coordinate system. Provide the location of a "bounding rectangle"
        :param top_left: the top left point of bounding rectangle
        :type top_left: Union[Tuple[int, int], Tuple[float, float]]
        :param bottom_right: the bottom right point of bounding rectangle
        :type bottom_right: Union[Tuple[int, int], Tuple[float, float]]
        :param fill_color: color of the interrior
        :type fill_color: (str)
        :param line_color: color of outline of oval
        :type line_color: (str)
        :param line_width: width of the line around the oval, the outline, in pixels
        :type line_width: (int)
        :return: id returned from tkinter that you'll need if you want to manipulate the oval
        :rtype: Union[int, None]
        """
        converted_top_left = self._convert_xy_to_canvas_xy(top_left[0], top_left[1])
        converted_bottom_right = self._convert_xy_to_canvas_xy(bottom_right[0], bottom_right[1])
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        try:  # in case windows close with X
            id = self._TKCanvas2.create_oval(converted_top_left[0], converted_top_left[1], converted_bottom_right[0],
                                             converted_bottom_right[1], fill=fill_color, outline=line_color, width=line_width )
        except:
            id = None

        return id

    def DrawArc(self, top_left, bottom_right, extent, start_angle, style=None, arc_color='black', line_width=1):
        """
        Draws different types of arcs.  Uses a "bounding box" to define location
        :param top_left: the top left point of bounding rectangle
        :type top_left: Union[Tuple[int, int], Tuple[float, float]]
        :param bottom_right: the bottom right point of bounding rectangle
        :type bottom_right: Union[Tuple[int, int], Tuple[float, float]]
        :param extent: Andle to end drawing. Used in conjunction with start_angle
        :type extent: (float)
        :param start_angle: Angle to begin drawing. Used in conjunction with extent
        :type start_angle: (float)
        :param style: Valid choices are One of these Style strings- 'pieslice', 'chord', 'arc', 'first', 'last', 'butt', 'projecting', 'round', 'bevel', 'miter'
        :type style: (str)
        :param arc_color: color to draw arc with
        :type arc_color: (str)
        :return: id returned from tkinter that you'll need if you want to manipulate the arc
        :rtype: Union[int, None]
        """
        converted_top_left = self._convert_xy_to_canvas_xy(top_left[0], top_left[1])
        converted_bottom_right = self._convert_xy_to_canvas_xy(bottom_right[0], bottom_right[1])
        tkstyle = tk.PIESLICE if style is None else style
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        try:  # in case closed with X
            id = self._TKCanvas2.create_arc(converted_top_left[0], converted_top_left[1], converted_bottom_right[0],
                                            converted_bottom_right[1], extent=extent, start=start_angle, style=tkstyle,
                                            outline=arc_color, width=line_width)
        except:
            id = None
        return id

    def DrawRectangle(self, top_left, bottom_right, fill_color=None, line_color=None, line_width=None):
        """
        Draw a rectangle given 2 points. Can control the line and fill colors

        :param top_left: the top left point of rectangle
        :type top_left: Union[Tuple[int, int], Tuple[float, float]]
        :param bottom_right: the bottom right point of rectangle
        :type bottom_right: Union[Tuple[int, int], Tuple[float, float]]
        :param fill_color: color of the interior
        :type fill_color: (str)
        :param line_color: color of outline
        :type line_color: (str)
        :param line_width: width of the line in pixels
        :type line_width: (int)
        :return: Union[int, None] id returned from tkinter that you'll need if you want to manipulate the rectangle
        :rtype: Union[int, None]
        """

        converted_top_left = self._convert_xy_to_canvas_xy(top_left[0], top_left[1])
        converted_bottom_right = self._convert_xy_to_canvas_xy(bottom_right[0], bottom_right[1])
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        if line_width is None:
            line_width = 1
        try:  # in case closed with X
            id = self._TKCanvas2.create_rectangle(converted_top_left[0], converted_top_left[1],
                                                  converted_bottom_right[0],
                                                  converted_bottom_right[1], fill=fill_color, outline=line_color, width=line_width)
        except:
            id = None
        return id


    def DrawPolygon(self, points, fill_color=None, line_color=None, line_width=None):
        """
        Draw a rectangle given 2 points. Can control the line and fill colors

        :param points: list of points that define the polygon
        :type points: List[Union[Tuple[int, int], Tuple[float, float]]]
        :param fill_color: color of the interior
        :type fill_color: (str)
        :param line_color: color of outline
        :type line_color: (str)
        :param line_width: width of the line in pixels
        :type line_width: (int)
        :return: id returned from tkinter that you'll need if you want to manipulate the rectangle
        :rtype: Union[int, None]
        """

        converted_points = [self._convert_xy_to_canvas_xy(point[0], point[1]) for point in points]
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        try:  # in case closed with X
            id = self._TKCanvas2.create_polygon(converted_points, fill=fill_color, outline=line_color, width=line_width)
        except:
            id = None
        return id



    def DrawText(self, text, location, color='black', font=None, angle=0, text_location=TEXT_LOCATION_CENTER):
        """
        Draw some text on your graph.  This is how you label graph number lines for example

        :param text: text to display
        :type text: (str)
        :param location: location to place first letter
        :type location: Union[Tuple[int, int], Tuple[float, float]]
        :param color: text color
        :type color: (str)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param angle: Angle 0 to 360 to draw the text.  Zero represents horizontal text
        :type angle: (float)
        :param text_location: "anchor" location for the text. Values start with TEXT_LOCATION_
        :type text_location: (enum)
        :return: id returned from tkinter that you'll need if you want to manipulate the text
        :rtype: Union[int, None]
        """
        text = str(text)
        if location == (None, None):
            return
        converted_point = self._convert_xy_to_canvas_xy(location[0], location[1])
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        try:  # in case closed with X
            id = self._TKCanvas2.create_text(converted_point[0], converted_point[1], text=text, font=font, fill=color, angle=angle, anchor=text_location)
        except:
            id = None
        return id

    def DrawImage(self, filename=None, data=None, location=(None, None), color='black', font=None, angle=0):
        """
        Places an image onto your canvas.  It's a really important method for this element as it enables so much

        :param filename: if image is in a file, path and filename for the image. (GIF and PNG only!)
        :type filename: (str)
        :param data: if image is in Base64 format or raw? format then use instead of filename
        :type data: Union[str, bytes]
        :param location: the (x,y) location to place image's top left corner
        :type location: Union[Tuple[int, int], Tuple[float, float]]
        :param color: text color
        :type color: (str)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param angle: Angle 0 to 360 to draw the text.  Zero represents horizontal text
        :type angle: (float)
        :return: id returned from tkinter that you'll need if you want to manipulate the image
        :rtype: Union[int, None]
        """
        if location == (None, None):
            return
        if filename is not None:
            image = tk.PhotoImage(file=filename)
        elif data is not None:
            # if type(data) is bytes:
            try:
                image = tk.PhotoImage(data=data)
            except:
                return None  # an error likely means the window has closed so exit
        converted_point = self._convert_xy_to_canvas_xy(location[0], location[1])
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        try:  # in case closed with X
            id = self._TKCanvas2.create_image(converted_point, image=image, anchor=tk.NW)
            self.Images[id] = image
        except:
            id = None
        return id

    def Erase(self):
        """
        Erase the Graph - Removes all figures previously "drawn" using the Graph methods (e.g. DrawText)
        """
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        self.Images = {}
        try:  # in case window was closed with X
            self._TKCanvas2.delete('all')
        except:
            pass

    def DeleteFigure(self, id):
        """
        Remove from the Graph the figure represented by id. The id is given to you anytime you call a drawing primitive

        :param id: the id returned to you when calling one of the drawing methods
        :type id: (int)
        """
        try:
            self._TKCanvas2.delete(id)
        except:
            print('DeleteFigure - bad ID {}'.format(id))
        try:
            del self.Images[id]  # in case was an image. If wasn't an image, then will get exception
        except:
            pass

    def Update(self, background_color=None, visible=None):
        """
        Changes some of the settings for the Graph Element. Must call `Window.Read` or `Window.Finalize` prior

        :param background_color: color of background
        :type background_color: ???
        :param visible: control visibility of element
        :type visible: (bool)
        """
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return
        if background_color is not None and background_color != COLOR_SYSTEM_DEFAULT:
            self._TKCanvas2.configure(background=background_color)
        if visible is False:
            self._TKCanvas2.pack_forget()
        elif visible is True:
            self._TKCanvas2.pack(padx=self.pad_used[0], pady=self.pad_used[1])

    def Move(self, x_direction, y_direction):
        """
        Moves the entire drawing area (the canvas) by some delta from the current position.  Units are indicated in your coordinate system indicated number of ticks in your coordinate system

        :param x_direction: how far to move in the "X" direction in your coordinates
        :type x_direction: Union[int, float]
        :param y_direction: how far to move in the "Y" direction in your coordinates
        :type y_direction: Union[int, float]
        """
        zero_converted = self._convert_xy_to_canvas_xy(0, 0)
        shift_converted = self._convert_xy_to_canvas_xy(x_direction, y_direction)
        shift_amount = (shift_converted[0] - zero_converted[0], shift_converted[1] - zero_converted[1])
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        self._TKCanvas2.move('all', shift_amount[0], shift_amount[1])

    def MoveFigure(self, figure, x_direction, y_direction):
        """
        Moves a previously drawn figure using a "delta" from current position

        :param figure: Previously obtained figure-id. These are returned from all Draw methods
        :type figure: (id)
        :param x_direction: delta to apply to position in the X direction
        :type x_direction: Union[int, float]
        :param y_direction: delta to apply to position in the Y direction
        :type y_direction: Union[int, float]
        """
        zero_converted = self._convert_xy_to_canvas_xy(0, 0)
        shift_converted = self._convert_xy_to_canvas_xy(x_direction, y_direction)
        shift_amount = (shift_converted[0] - zero_converted[0], shift_converted[1] - zero_converted[1])
        if figure is None:
            print('*** WARNING - Your figure is None. It most likely means your did not Finalize your Window ***')
            print('Call Window.Finalize() prior to all graph operations')
            return None
        self._TKCanvas2.move(figure, shift_amount[0], shift_amount[1])

    def RelocateFigure(self, figure, x, y):
        """
        Move a previously made figure to an arbitrary (x,y) location. This differs from the Move methods because it
        uses absolute coordinates versus relative for Move

        :param figure: Previously obtained figure-id. These are returned from all Draw methods
        :type figure: (id)
        :param x: location on X axis (in user coords) to move the upper left corner of the figure
        :type x: Union[int, float]
        :param y: location on Y axis (in user coords) to move the upper left corner of the figure
        :type y: Union[int, float]
        """

        zero_converted = self._convert_xy_to_canvas_xy(0, 0)
        shift_converted = self._convert_xy_to_canvas_xy(x, y)
        shift_amount = (shift_converted[0] - zero_converted[0], shift_converted[1] - zero_converted[1])
        if figure is None:
            print('*** WARNING - Your figure is None. It most likely means your did not Finalize your Window ***')
            print('Call Window.Finalize() prior to all graph operations')
            return None
        xy = self._TKCanvas2.coords(figure)
        self._TKCanvas2.move(figure, shift_converted[0] - xy[0], shift_converted[1] - xy[1])

    def SendFigureToBack(self, figure):
        """
        Changes Z-order of figures on the Graph.  Sends the indicated figure to the back of all other drawn figures

        :param figure: value returned by tkinter when creating the figure / drawing
        :type figure: (int)
        """
        self.TKCanvas.tag_lower(figure)  # move figure to the "bottom" of all other figure

    def BringFigureToFront(self, figure):
        """
        Changes Z-order of figures on the Graph.  Brings the indicated figure to the front of all other drawn figures

        :param figure: value returned by tkinter when creating the figure / drawing
        :type figure: (int)
        """
        self.TKCanvas.tag_raise(figure)  # move figure to the "top" of all other figures


    def GetFiguresAtLocation(self, location):
        """
        Returns a list of figures located at a particular x,y location within the Graph

        :param location: point to check
        :type location: Union[Tuple[int, int], Tuple[float, float]]
        :return: a list of previously drawn "Figures" (returned from the drawing primitives)
        :rtype: List[int]
        """
        x, y = self._convert_xy_to_canvas_xy(location[0], location[1])
        ids = self.TKCanvas.find_overlapping(x,y,x,y)
        return ids

    def GetBoundingBox(self, figure):
        """
        Given a figure, returns the upper left and lower right bounding box coordinates

        :param figure: a previously drawing figure
        :type figure: object
        :return: upper left x, upper left y, lower right x, lower right y
        :rtype: Union[Tuple[int, int, int, int], Tuple[float, float, float, float]]
        """
        box = self.TKCanvas.bbox(figure)
        top_left = self._convert_canvas_xy_to_xy(box[0], box[1])
        bottom_right = self._convert_canvas_xy_to_xy(box[2], box[3])
        return top_left,bottom_right


    def change_coordinates(self, graph_bottom_left, graph_top_right):
        """
        Changes the corrdinate system to a new one.  The same 2 points in space are used to define the coorinate
        system - the bottom left and the top right values of your graph.

        :param graph_bottom_left: The bottoms left corner of your coordinate system
        :type graph_bottom_left: Tuple[int, int] (x,y)
        :param graph_top_right: The top right corner of  your coordinate system
        :type graph_top_right: Tuple[int, int]  (x,y)
        """
        self.BottomLeft = graph_bottom_left
        self.TopRight = graph_top_right


    @property
    def TKCanvas(self):
        """
        Returns the underlying tkiner Canvas widget

        :return: The tkinter canvas widget
        :rtype: (tk.Canvas)
        """
        if self._TKCanvas2 is None:
            print('*** Did you forget to call Finalize()? Your code should look something like: ***')
            print('*** form = sg.Window("My Form").Layout(layout).Finalize() ***')
        return self._TKCanvas2

    # button release callback
    def ButtonReleaseCallBack(self, event):
        """
        Not a user callable method.  Used to get Graph click events. Called by tkinter when button is released

        :param event: (event) event info from tkinter. Note not used in this method
        """
        if not self.DragSubmits:  # only report mouse up for drag operations
            return
        self.ClickPosition = self._convert_canvas_xy_to_xy(event.x, event.y)
        self.LastButtonClickedWasRealtime = not self.DragSubmits
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = '__GRAPH__'  # need to put something rather than None
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()
        if self.DragSubmits:
            self.ParentForm.LastButtonClicked += '+UP'
        self.MouseButtonDown = False

    # button callback
    def ButtonPressCallBack(self, event):
        """
        Not a user callable method.  Used to get Graph click events. Called by tkinter when button is released

        :param event: (event) event info from tkinter. Contains the x and y coordinates of a click
        """

        self.ClickPosition = self._convert_canvas_xy_to_xy(event.x, event.y)
        self.ParentForm.LastButtonClickedWasRealtime = self.DragSubmits
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = '__GRAPH__'  # need to put something rather than None
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick out of loop if read was called
        self.MouseButtonDown = True

    # button callback
    def MotionCallBack(self, event):
        """
        Not a user callable method.  Used to get Graph mouse motion events. Called by tkinter when mouse moved

        :param event: (event) event info from tkinter. Contains the x and y coordinates of a mouse
        """

        if not self.MouseButtonDown:
            return
        self.ClickPosition = self._convert_canvas_xy_to_xy(event.x, event.y)
        self.ParentForm.LastButtonClickedWasRealtime = self.DragSubmits
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = '__GRAPH__'  # need to put something rather than None
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick out of loop if read was called

    bring_figure_to_front = BringFigureToFront
    button_press_call_back = ButtonPressCallBack
    button_release_call_back = ButtonReleaseCallBack
    delete_figure = DeleteFigure
    draw_arc = DrawArc
    draw_circle = DrawCircle
    draw_image = DrawImage
    draw_line = DrawLine
    draw_oval = DrawOval
    draw_point = DrawPoint
    draw_polygon = DrawPolygon
    draw_rectangle = DrawRectangle
    draw_text = DrawText
    get_figures_at_location = GetFiguresAtLocation
    get_bounding_box = GetBoundingBox
    erase = Erase
    motion_call_back = MotionCallBack
    move = Move
    move_figure = MoveFigure
    relocate_figure = RelocateFigure
    send_figure_to_back = SendFigureToBack
    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    tk_canvas = TKCanvas
    update = Update


# ---------------------------------------------------------------------- #
#                           Frame                                        #
# ---------------------------------------------------------------------- #
class Frame(Element):
    """
    A Frame Element that contains other Elements. Encloses with a line around elements and a text label.
    """

    def __init__(self, title, layout, title_color=None, background_color=None, title_location=None,
                 relief=DEFAULT_FRAME_RELIEF, size=(None, None), font=None, pad=None, border_width=None, key=None,
                 tooltip=None, right_click_menu=None, visible=True, element_justification='left', metadata=None):
        """
        :param title: text that is displayed as the Frame's "label" or title
        :type title: (str)
        :param layout: The layout to put inside the Frame
        :type layout: List[List[Elements]]
        :param title_color: color of the title text
        :type title_color: (str)
        :param background_color: background color of the Frame
        :type background_color: (str)
        :param title_location: location to place the text title.  Choices include: TITLE_LOCATION_TOP TITLE_LOCATION_BOTTOM TITLE_LOCATION_LEFT TITLE_LOCATION_RIGHT TITLE_LOCATION_TOP_LEFT TITLE_LOCATION_TOP_RIGHT TITLE_LOCATION_BOTTOM_LEFT TITLE_LOCATION_BOTTOM_RIGHT
        :type title_location: (enum)
        :param relief: relief style. Values are same as other elements with reliefs. Choices include RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID
        :type relief: (enum)
        :param size: (width, height) (note this parameter may not always work)
        :type size: Tuple[int, int]
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param border_width: width of border around element in pixels
        :type border_width: (int)
        :param key: Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
        :type key: (any)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param right_click_menu: A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
        :type right_click_menu: List[List[Union[List[str],str]]]
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param element_justification: All elements inside the Frame will have this justification 'left', 'right', 'center' are valid values
        :type element_justification: (str)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.UseDictionary = False
        self.ReturnValues = None
        self.ReturnValuesList = []
        self.ReturnValuesDictionary = {}
        self.DictionaryKeyCounter = 0
        self.ParentWindow = None
        self.Rows = []
        # self.ParentForm = None
        self.TKFrame = None
        self.Title = title
        self.Relief = relief
        self.TitleLocation = title_location
        self.BorderWidth = border_width
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.RightClickMenu = right_click_menu
        self.ContainerElemementNumber = Window._GetAContainerNumber()
        self.ElementJustification = element_justification
        self.Layout(layout)

        super().__init__(ELEM_TYPE_FRAME, background_color=background_color, text_color=title_color, size=size,
                         font=font, pad=pad, key=key, tooltip=tooltip, visible=visible, metadata=metadata)
        return

    def AddRow(self, *args):
        """
        Not recommended user call.  Used to add rows of Elements to the Frame Element.

        :param *args: The list of elements for this row
        :type *args: List[Element]
        """
        NumRows = len(self.Rows)  # number of existing rows is our row number
        CurrentRowNumber = NumRows  # this row's number
        CurrentRow = []  # start with a blank row and build up
        # -------------------------  Add the elements to a row  ------------------------- #
        for i, element in enumerate(args):  # Loop through list of elements and add them to the row
            if type(element) == list:
                PopupError('Error creating Frame layout',
                           'Layout has a LIST instead of an ELEMENT',
                           'This means you have a badly placed ]',
                           'The offensive list is:',
                           element,
                           'This list will be stripped from your layout',
                            keep_on_top=True
                           )
                continue
            elif callable(element) and not isinstance(element, Element):
                PopupError('Error creating Frame layout',
                           'Layout has a FUNCTION instead of an ELEMENT',
                           'This likely means you are missing () from your layout',
                           'The offensive list is:',
                           element,
                           'This item will be stripped from your layout',
                           keep_on_top=True)
                continue
            if element.ParentContainer is not None:
                warnings.warn('*** YOU ARE ATTEMPTING TO RESUSE AN ELEMENT IN YOUR LAYOUT! Once placed in a layout, an element cannot be used in another layout. ***', UserWarning)
                PopupError('Error creating Frame layout',
                           'The layout specified has already been used',
                           'You MUST start witha "clean", unused layout every time you create a window',
                           'The offensive Element = ',
                           element,
                           'and has a key = ', element.Key,
                           'This item will be stripped from your layout',
                           'Hint - try printing your layout and matching the IDs "print(layout)"',
                           obj_to_string_single_obj(element), keep_on_top=True)
                continue
            element.Position = (CurrentRowNumber, i)
            element.ParentContainer = self
            CurrentRow.append(element)
            if element.Key is not None:
                self.UseDictionary = True
        # -------------------------  Append the row to list of Rows  ------------------------- #
        self.Rows.append(CurrentRow)

    def Layout(self, rows):
        """
        Can use like the Window.Layout method, but it's better to use the layout parameter when creating

        :param rows: The rows of Elements
        :type rows: List[List[Element]]
        :return: Used for chaining
        :rtype: (Frame)
        """

        for row in rows:
            try:
                iter(row)
            except TypeError:
                PopupError('Error creating Frame layout',
                           'Your row is not an iterable (e.g. a list)',
                           'Instead of a list, the type found was {}'.format(type(row)),
                           'The offensive row = ',
                           row,
                           'This item will be stripped from your layout', keep_on_top=True)
                continue
            self.AddRow(*row)
        return self

    def _GetElementAtLocation(self, location):
        """
        Not user callable. Used to find the Element at a row, col position within the layout

        :param location: (row, column) position of the element to find in layout
        :type location: Tuple[int, int]
        :return: (Element) The element found at the location
        :rtype: (Element)
        """

        (row_num, col_num) = location
        row = self.Rows[row_num]
        element = row[col_num]
        return element

    def Update(self, value=None, visible=None):
        """
        Changes some of the settings for the Frame Element. Must call `Window.Read` or `Window.Finalize` prior

        :param value: New text value to show on frame
        :type value: (Any)
        :param visible: control visibility of element
        :type visible: (bool)
        """
        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if visible is False:
            self.TKFrame.pack_forget()
        elif visible is True:
            self.TKFrame.pack(padx=self.pad_used[0], pady=self.pad_used[1])
        if value is not None:
            self.TKFrame.config(text=str(value))

    add_row = AddRow
    layout = Layout
    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update


# ---------------------------------------------------------------------- #
#                           Vertical Separator                           #
# ---------------------------------------------------------------------- #
class VerticalSeparator(Element):
    """
    Vertical Separator Element draws a vertical line at the given location. It will span 1 "row". Usually paired with
    Column Element if extra height is needed
    """

    def __init__(self, pad=None):
        """
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        """

        self.Orientation = 'vertical'  # for now only vertical works

        super().__init__(ELEM_TYPE_SEPARATOR, pad=pad)

    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip


VSeperator = VerticalSeparator
VSep = VerticalSeparator


# ---------------------------------------------------------------------- #
#                           Tab                                          #
# ---------------------------------------------------------------------- #
class Tab(Element):
    """
    Tab Element is another "Container" element that holds a layout and displays a tab with text. Used with TabGroup only
    Tabs are never placed directly into a layout.  They are always "Contained" in a TabGroup layout
    """

    def __init__(self, title, layout, title_color=None, background_color=None, font=None, pad=None, disabled=False,
                 border_width=None, key=None, tooltip=None, right_click_menu=None, visible=True, element_justification='left', metadata=None):
        """
        :param title: text to show on the tab
        :type title: (str)
        :param layout: The element layout that will be shown in the tab
        :type layout: List[List[Element]]
        :param title_color: color of the tab text (note not currently working on tkinter)
        :type title_color: (str)
        :param background_color: color of background of the entire layout
        :type background_color: (str)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param disabled: If True button will be created disabled
        :type disabled: (bool)
        :param border_width: width of border around element in pixels
        :type border_width: (int)
        :param key: Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
        :type key: (any)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param right_click_menu: A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
        :type right_click_menu: List[List[Union[List[str],str]]]
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param element_justification: All elements inside the Tab will have this justification 'left', 'right', 'center' are valid values
        :type element_justification: (str)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.UseDictionary = False
        self.ReturnValues = None
        self.ReturnValuesList = []
        self.ReturnValuesDictionary = {}
        self.DictionaryKeyCounter = 0
        self.ParentWindow = None
        self.Rows = []
        self.TKFrame = None
        self.Title = title
        self.BorderWidth = border_width
        self.Disabled = disabled
        self.ParentNotebook = None
        self.TabID = None
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.RightClickMenu = right_click_menu
        self.ContainerElemementNumber = Window._GetAContainerNumber()
        self.ElementJustification = element_justification

        self.Layout(layout)

        super().__init__(ELEM_TYPE_TAB, background_color=background_color, text_color=title_color, font=font, pad=pad,
                         key=key, tooltip=tooltip, visible=visible, metadata=metadata)
        return

    def AddRow(self, *args):
        """
        Not recommended use call.  Used to add rows of Elements to the Frame Element.

        :param *args: The list of elements for this row
        :type *args: List[Element]
        """
        NumRows = len(self.Rows)  # number of existing rows is our row number
        CurrentRowNumber = NumRows  # this row's number
        CurrentRow = []  # start with a blank row and build up
        # -------------------------  Add the elements to a row  ------------------------- #
        for i, element in enumerate(args):  # Loop through list of elements and add them to the row
            if type(element) == list:
                PopupError('Error creating Tab layout',
                           'Layout has a LIST instead of an ELEMENT',
                           'This means you have a badly placed ]',
                           'The offensive list is:',
                           element,
                           'This list will be stripped from your layout' , keep_on_top=True
                           )
                continue
            elif callable(element) and not isinstance(element, Element):
                PopupError('Error creating Tab layout',
                           'Layout has a FUNCTION instead of an ELEMENT',
                           'This likely means you are missing () from your layout',
                           'The offensive list is:',
                           element,
                           'This item will be stripped from your layout', keep_on_top=True)
                continue
            if element.ParentContainer is not None:
                warnings.warn('*** YOU ARE ATTEMPTING TO RESUSE AN ELEMENT IN YOUR LAYOUT! Once placed in a layout, an element cannot be used in another layout. ***', UserWarning)
                PopupError('Error creating Tab layout',
                           'The layout specified has already been used',
                           'You MUST start witha "clean", unused layout every time you create a window',
                           'The offensive Element = ',
                           element,
                           'and has a key = ', element.Key,
                           'This item will be stripped from your layout',
                           'Hint - try printing your layout and matching the IDs "print(layout)"', keep_on_top=True)
                continue
            element.Position = (CurrentRowNumber, i)
            element.ParentContainer = self
            CurrentRow.append(element)
            if element.Key is not None:
                self.UseDictionary = True
        # -------------------------  Append the row to list of Rows  ------------------------- #
        self.Rows.append(CurrentRow)

    def Layout(self, rows):
        """
        Not user callable.  Use layout parameter instead. Creates the layout using the supplied rows of Elements

        :param rows: List[List[Element]] The list of rows
        :return: (Tab) used for chaining
        """

        for row in rows:
            try:
                iter(row)
            except TypeError:
                PopupError('Error creating Tab layout',
                           'Your row is not an iterable (e.g. a list)',
                           'Instead of a list, the type found was {}'.format(type(row)),
                           'The offensive row = ',
                           row,
                           'This item will be stripped from your layout', keep_on_top=True)
                continue
            self.AddRow(*row)
        return self


    def Update(self, disabled=None, visible=None):  # TODO Disable / enable of tabs is not complete
        """
        Changes some of the settings for the Tab Element. Must call `Window.Read` or `Window.Finalize` prior

        :param disabled: disable or enable state of the element
        :type disabled: (bool)
        :param visible: control visibility of element
        :type visible: (bool)
        """
        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        state = 'normal'
        if disabled is not None:
            self.Disabled = disabled
            if disabled:
                state = 'disabled'
        if visible is False:
            state = 'hidden'
        self.ParentNotebook.tab(self.TabID, state=state)
        # if visible is False:
        #     self.ParentNotebook.pack_forget()
        # elif visible is True:
        #     self.ParentNotebook.pack()
        return self

    def _GetElementAtLocation(self, location):
        """
        Not user callable. Used to find the Element at a row, col position within the layout

        :param location: (row, column) position of the element to find in layout
        :type location: Tuple[int, int]
        :return:  The element found at the location
        :rtype: (Element)
        """

        (row_num, col_num) = location
        row = self.Rows[row_num]
        element = row[col_num]
        return element

    def Select(self):
        """
        Create a tkinter event that mimics user clicking on a tab. Must have called window.Finalize / Read first!

        """
        # Use a try in case the window has been destoyed
        try:
            self.ParentNotebook.select(self.TabID)
        except Exception as e:
            print('Exception Selecting Tab {}'.format(e))

    add_row = AddRow
    layout = Layout
    select = Select
    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update


# ---------------------------------------------------------------------- #
#                           TabGroup                                     #
# ---------------------------------------------------------------------- #
class TabGroup(Element):
    """
    TabGroup Element groups together your tabs into the group of tabs you see displayed in your window
    """

    def __init__(self, layout, tab_location=None, title_color=None, tab_background_color=None, selected_title_color=None, selected_background_color=None,
                 background_color=None,
                 font=None, change_submits=False, enable_events=False, pad=None, border_width=None, theme=None,
                 key=None, tooltip=None, visible=True, metadata=None):
        """
        :param layout: Layout of Tabs. Different than normal layouts. ALL Tabs should be on first row
        :type layout: List[List[Tab]]
        :param tab_location: location that tabs will be displayed. Choices are left, right, top, bottom, lefttop, leftbottom, righttop, rightbottom, bottomleft, bottomright, topleft, topright
        :type tab_location: (str)
        :param title_color: color of text on tabs
        :type title_color: (str)
        :param tab_background_color: color of all tabs that are not selected
        :type tab_background_color: (str)
        :param selected_title_color: color of tab text when it is selected
        :type selected_title_color: (str)
        :param selected_background_color: color of tab when it is selected
        :type selected_background_color: (str)
        :param background_color: color of background area that tabs are located on
        :type background_color: (str)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param change_submits: * DEPRICATED DO NOT USE! Same as enable_events
        :type change_submits: (bool)
        :param enable_events: If True then switching tabs will generate an Event
        :type enable_events: (bool)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param border_width: width of border around element in pixels
        :type border_width: (int)
        :param theme: DEPRICATED - You can only specify themes using set options or when window is created. It's not possible to do it on an element basis
        :type theme: (enum)
        :param key: Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
        :type key: (any)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.UseDictionary = False
        self.ReturnValues = None
        self.ReturnValuesList = []
        self.ReturnValuesDictionary = {}
        self.DictionaryKeyCounter = 0
        self.ParentWindow = None
        self.SelectedTitleColor = selected_title_color if selected_title_color is not None else LOOK_AND_FEEL_TABLE[CURRENT_LOOK_AND_FEEL]['TEXT']
        self.SelectedBackgroundColor = selected_background_color if selected_background_color is not None else LOOK_AND_FEEL_TABLE[CURRENT_LOOK_AND_FEEL][
            'BACKGROUND']
        title_color = title_color if title_color is not None else LOOK_AND_FEEL_TABLE[CURRENT_LOOK_AND_FEEL]['TEXT_INPUT']
        self.TabBackgroundColor = tab_background_color if tab_background_color is not None else LOOK_AND_FEEL_TABLE[CURRENT_LOOK_AND_FEEL]['INPUT']
        self.Rows = []
        self.TKNotebook = None  # type: ttk.Notebook
        self.Widget = None  # type: ttk.Notebook
        self.TabCount = 0
        self.BorderWidth = border_width
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.ChangeSubmits = change_submits or enable_events
        self.TabLocation = tab_location
        self.ElementJustification = 'left'

        self.Layout(layout)

        super().__init__(ELEM_TYPE_TAB_GROUP, background_color=background_color, text_color=title_color, font=font,
                         pad=pad, key=key, tooltip=tooltip, visible=visible, metadata=metadata)
        return

    def AddRow(self, *args):
        """
        Not recommended user call.  Used to add rows of Elements to the Frame Element.

        :param *args:  The list of elements for this row
        :typeparam *args: List[Element]
        """

        NumRows = len(self.Rows)  # number of existing rows is our row number
        CurrentRowNumber = NumRows  # this row's number
        CurrentRow = []  # start with a blank row and build up
        # -------------------------  Add the elements to a row  ------------------------- #
        for i, element in enumerate(args):  # Loop through list of elements and add them to the row
            if type(element) == list:
                PopupError('Error creating Tab layout',
                           'Layout has a LIST instead of an ELEMENT',
                           'This means you have a badly placed ]',
                           'The offensive list is:',
                           element,
                           'This list will be stripped from your layout' , keep_on_top=True
                           )
                continue
            elif callable(element) and not isinstance(element, Element):
                PopupError('Error creating Tab layout',
                           'Layout has a FUNCTION instead of an ELEMENT',
                           'This likely means you are missing () from your layout',
                           'The offensive list is:',
                           element,
                           'This item will be stripped from your layout', keep_on_top=True)
                continue
            if element.ParentContainer is not None:
                warnings.warn('*** YOU ARE ATTEMPTING TO RESUSE AN ELEMENT IN YOUR LAYOUT! Once placed in a layout, an element cannot be used in another layout. ***', UserWarning)
                PopupError('Error creating Tab layout',
                           'The layout specified has already been used',
                           'You MUST start witha "clean", unused layout every time you create a window',
                           'The offensive Element = ',
                           element,
                           'and has a key = ', element.Key,
                           'This item will be stripped from your layout',
                           'Hint - try printing your layout and matching the IDs "print(layout)"', keep_on_top=True)
                continue
            element.Position = (CurrentRowNumber, i)
            element.ParentContainer = self
            CurrentRow.append(element)
            if element.Key is not None:
                self.UseDictionary = True
        # -------------------------  Append the row to list of Rows  ------------------------- #
        self.Rows.append(CurrentRow)

    def Layout(self, rows):
        """
        Can use like the Window.Layout method, but it's better to use the layout parameter when creating

        :param rows: The rows of Elements
        :type rows: List[List[Element]]
        :return: Used for chaining
        :rtype: (Frame)
        """
        for row in rows:
            try:
                iter(row)
            except TypeError:
                PopupError('Error creating Tab layout',
                           'Your row is not an iterable (e.g. a list)',
                           'Instead of a list, the type found was {}'.format(type(row)),
                           'The offensive row = ',
                           row,
                           'This item will be stripped from your layout', keep_on_top=True)
                continue
            self.AddRow(*row)
        return self


    def _GetElementAtLocation(self, location):
        """
        Not user callable. Used to find the Element at a row, col position within the layout

        :param location: (row, column) position of the element to find in layout
        :type location: Tuple[int, int]
        :return: The element found at the location
        :rtype: (Element)
        """

        (row_num, col_num) = location
        row = self.Rows[row_num]
        element = row[col_num]
        return element

    def FindKeyFromTabName(self, tab_name):
        """
        Searches through the layout to find the key that matches the text on the tab. Implies names should be unique

        :param tab_name: name of a tab
        :type tab_name: str
        :return: Returns the key or None if no key found
        :rtype: Union[key, None]
        """
        for row in self.Rows:
            for element in row:
                if element.Title == tab_name:
                    return element.Key
        return None

    def Get(self):
        """
        Returns the current value for the Tab Group, which will be the currently selected tab's KEY or the text on
        the tab if no key is defined.  Returns None if an error occurs.
        Note that this is exactly the same data that would be returned from a call to Window.Read. Are you sure you
        are using this method correctly?

        :return:  The key of the currently selected tab or the tab's text if it has no key
        :rtype: Union[Any, None]
        """

        try:
            value = self.TKNotebook.tab(self.TKNotebook.index('current'))['text']
            tab_key = self.FindKeyFromTabName(value)
            if tab_key is not None:
                value = tab_key
        except:
            value = None
        return value

    add_row = AddRow
    find_key_from_tab_name = FindKeyFromTabName
    get = Get
    layout = Layout
    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip


# ---------------------------------------------------------------------- #
#                           Slider                                       #
# ---------------------------------------------------------------------- #
class Slider(Element):
    """
    A slider, horizontal or vertical
    """

    def __init__(self, range=(None, None), default_value=None, resolution=None, tick_interval=None, orientation=None,
                 disable_number_display=False, border_width=None, relief=None, change_submits=False,
                 enable_events=False, disabled=False, size=(None, None), font=None, background_color=None,
                 text_color=None, key=None, pad=None, tooltip=None, visible=True, metadata=None):
        """
        :param range: slider's range (min value, max value)
        :type range: Union[Tuple[int, int], Tuple[float, float]]
        :param default_value: starting value for the slider
        :type default_value: Union[int, float]
        :param resolution: the smallest amount the slider can be moved
        :type resolution: Union[int, float]
        :param tick_interval: how often a visible tick should be shown next to slider
        :type tick_interval: Union[int, float]
        :param orientation: 'horizontal' or 'vertical' ('h' or 'v' also work)
        :type orientation: (str)
        :param disable_number_display: if True no number will be displayed by the Slider Element
        :type disable_number_display: (bool)
        :param border_width: width of border around element in pixels
        :type border_width: (int)
        :param relief: relief style. RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID
        :type relief: (enum)
        :param change_submits: * DEPRICATED DO NOT USE! Same as enable_events
        :type change_submits: (bool)
        :param enable_events: If True then moving the slider will generate an Event
        :type enable_events: (bool)
        :param disabled: set disable state for element
        :type disabled: (bool)
        :param size: (w=characters-wide, h=rows-high)
        :type size: Tuple[int, int]
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param background_color: color of slider's background
        :type background_color: (str)
        :param text_color: color of the slider's text
        :type text_color: (str)
        :param key: Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
        :type key: (any)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.TKScale = self.Widget = None  # type: tk.Scale
        self.Range = (1, 10) if range == (None, None) else range
        self.DefaultValue = self.Range[0] if default_value is None else default_value
        self.Orientation = orientation if orientation else DEFAULT_SLIDER_ORIENTATION
        self.BorderWidth = border_width if border_width else DEFAULT_SLIDER_BORDER_WIDTH
        self.Relief = relief if relief else DEFAULT_SLIDER_RELIEF
        self.Resolution = 1 if resolution is None else resolution
        self.ChangeSubmits = change_submits or enable_events
        self.Disabled = disabled
        self.TickInterval = tick_interval
        self.DisableNumericDisplay = disable_number_display
        self.TroughColor = DEFAULT_SCROLLBAR_COLOR
        temp_size = size
        if temp_size == (None, None):
            temp_size = (20, 20) if self.Orientation.startswith('h') else (8, 20)

        super().__init__(ELEM_TYPE_INPUT_SLIDER, size=temp_size, font=font, background_color=background_color,
                         text_color=text_color, key=key, pad=pad, tooltip=tooltip, visible=visible, metadata=metadata)
        return

    def Update(self, value=None, range=(None, None), disabled=None, visible=None):
        """
        Changes some of the settings for the Slider Element. Must call `Window.Read` or `Window.Finalize` prior

        :param value: sets current slider value
        :type value: Union[int, float]
        :param range: Sets a new range for slider
        :type range: Union[Tuple[int, int], Tuple[float, float]
        :param disabled: disable or enable state of the element
        :type disabled: (bool)
        :param visible: control visibility of element
        :type visible: (bool)
        """
        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if value is not None:
            try:
                self.TKIntVar.set(value)
            except:
                pass
            self.DefaultValue = value
        if disabled == True:
            self.TKScale['state'] = 'disabled'
        elif disabled == False:
            self.TKScale['state'] = 'normal'
        if visible is False:
            self.TKScale.pack_forget()
        elif visible is True:
            self.TKScale.pack(padx=self.pad_used[0], pady=self.pad_used[1])
        if range != (None, None):
            self.TKScale.config(from_=range[0], to_=range[1])

    def _SliderChangedHandler(self, event):
        """
        Not user callable.  Callback function for when slider is moved.

        :param event: (event) the event data provided by tkinter. Unknown format. Not used.
        """

        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update


# ---------------------------------------------------------------------- #
#                          TkFixedFrame (Used by Column)                 #
# ---------------------------------------------------------------------- #
class TkFixedFrame(tk.Frame):
    """
    A tkinter frame that is used with Column Elements that do not have a scrollbar
    """

    def __init__(self, master, **kwargs):
        """
        :param master: (tk.Widget) The parent widget
        :type master: (tk.Widget)
        :param **kwargs: The keyword args
        """
        tk.Frame.__init__(self, master, **kwargs)

        self.canvas = tk.Canvas(self)

        self.canvas.pack(side="left", fill="both", expand=True)

        # reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.TKFrame = tk.Frame(self.canvas, **kwargs)
        self.frame_id = self.canvas.create_window(0, 0, window=self.TKFrame, anchor="nw")
        self.canvas.config(borderwidth=0, highlightthickness=0)
        self.TKFrame.config(borderwidth=0, highlightthickness=0)
        self.config(borderwidth=0, highlightthickness=0)


# ---------------------------------------------------------------------- #
#                          TkScrollableFrame (Used by Column)            #
# ---------------------------------------------------------------------- #
class TkScrollableFrame(tk.Frame):
    """
    A frame with one or two scrollbars.  Used to make Columns with scrollbars
    """

    def __init__(self, master, vertical_only, **kwargs):
        """
        :param master: The parent widget
        :type master: (tk.Widget)
        :param vertical_only: if True the only a vertical scrollbar will be shown
        :type vertical_only: (bool)
        """
        tk.Frame.__init__(self, master, **kwargs)
        # create a canvas object and a vertical scrollbar for scrolling it
        self.vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.vscrollbar.pack(side='right', fill="y", expand="false")

        if not vertical_only:
            self.hscrollbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)
            self.hscrollbar.pack(side='bottom', fill="x", expand="false")
            self.canvas = tk.Canvas(self, yscrollcommand=self.vscrollbar.set, xscrollcommand=self.hscrollbar.set)
        else:
            self.canvas = tk.Canvas(self, yscrollcommand=self.vscrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)

        self.vscrollbar.config(command=self.canvas.yview)
        if not vertical_only:
            self.hscrollbar.config(command=self.canvas.xview)

        # reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.TKFrame = tk.Frame(self.canvas, **kwargs)
        self.frame_id = self.canvas.create_window(0, 0, window=self.TKFrame, anchor="nw")
        self.canvas.config(borderwidth=0, highlightthickness=0)
        self.TKFrame.config(borderwidth=0, highlightthickness=0)
        self.config(borderwidth=0, highlightthickness=0)

        # scrollbar = tk.Scrollbar(frame)
        # scrollbar.pack(side=tk.RIGHT, fill='y')
        # scrollbar.config(command=treeview.yview)
        # self.vscrollbar.config(command=self.TKFrame.yview)
        # self.TKFrame.configure(yscrollcommand=self.vscrollbar.set)

        self.bind('<Configure>', self.set_scrollregion)

        self.canvas.bind("<MouseWheel>", self.yscroll)  # THIS IS IT! The line of code that enables the column to be scrolled with the mouse!
        self.canvas.bind("<Shift-MouseWheel>", self.xscroll)  # THIS IS IT! The line of code that enables the column to be scrolled with the mouse!

        # def _on_mousewheel(self, event):
        #     self.canv.yview_scroll(int(-1 * (event.delta / 120)), "units")

        # self.bind_mouse_scroll(self.canvas, self.yscroll)
        # if not vertical_only:
        #     self.bind_mouse_scroll(self.hscrollbar, self.xscroll)
        # self.bind_mouse_scroll(self.vscrollbar, self.yscroll)
        # self.bind_mouse_scroll(self.TKFrame, self.yscroll)
        # self.bind_mouse_scroll(self, self.yscroll)

    def resize_frame(self, e):
        self.canvas.itemconfig(self.frame_id, height=e.height, width=e.width)

    def yscroll(self, event):
        if event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "unit")
        elif event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "unit")

    def xscroll(self, event):
        if event.num == 5 or event.delta < 0:
            self.canvas.xview_scroll(1, "unit")
        elif event.num == 4 or event.delta > 0:
            self.canvas.xview_scroll(-1, "unit")

    def bind_mouse_scroll(self, parent, mode):
        # ~~ Windows only
        parent.bind("<MouseWheel>", mode)
        # ~~ Unix only
        parent.bind("<Button-4>", mode)
        parent.bind("<Button-5>", mode)

    def set_scrollregion(self, event=None):
        """ Set the scroll region on the canvas """
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))


# ---------------------------------------------------------------------- #
#                           Column                                       #
# ---------------------------------------------------------------------- #
class Column(Element):
    """
    A container element that is used to create a layout within your window's layout
    """

    def __init__(self, layout, background_color=None, size=(None, None), pad=None, scrollable=False,
                 vertical_scroll_only=False, right_click_menu=None, key=None, visible=True, justification='left', element_justification='left', metadata=None):
        """
        :param layout: Layout that will be shown in the Column container
        :type layout: List[List[Element]]
        :param background_color: color of background of entire Column
        :type background_color: (str)
        :param size: (width, height) size in pixels (doesn't work quite right, sometimes only 1 dimension is set by tkinter
        :type size: Tuple[int, int]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param scrollable: if True then scrollbars will be added to the column
        :type scrollable: (bool)
        :param vertical_scroll_only: if Truen then no horizontal scrollbar will be shown
        :type vertical_scroll_only: (bool)
        :param right_click_menu: A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
        :type right_click_menu: List[List[Union[List[str],str]]]
        :param key: Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
        :type key: (any)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param justification: set justification for the Column itself. Note entire row containing the Column will be affected
        :type justification: (str)
        :param element_justification: All elements inside the Column will have this justification 'left', 'right', 'center' are valid values
        :type element_justification: (str)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.UseDictionary = False
        self.ReturnValues = None
        self.ReturnValuesList = []
        self.ReturnValuesDictionary = {}
        self.DictionaryKeyCounter = 0
        self.ParentWindow = None
        self.ParentPanedWindow = None
        self.Rows = []
        self.TKFrame = None
        self.TKColFrame = None
        self.Scrollable = scrollable
        self.VerticalScrollOnly = vertical_scroll_only
        self.RightClickMenu = right_click_menu
        bg = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.ContainerElemementNumber = Window._GetAContainerNumber()
        self.ElementJustification = element_justification
        self.Justification = justification
        self.Layout(layout)

        super().__init__(ELEM_TYPE_COLUMN, background_color=bg, size=size, pad=pad, key=key, visible=visible, metadata=metadata)
        return

    def AddRow(self, *args):
        """
        Not recommended user call.  Used to add rows of Elements to the Column Element.

        :param *args: The list of elements for this row
        :type *args: List[Element]
        """

        NumRows = len(self.Rows)  # number of existing rows is our row number
        CurrentRowNumber = NumRows  # this row's number
        CurrentRow = []  # start with a blank row and build up
        # -------------------------  Add the elements to a row  ------------------------- #
        for i, element in enumerate(args):  # Loop through list of elements and add them to the row
            if type(element) == list:
                PopupError('Error creating Column layout',
                           'Layout has a LIST instead of an ELEMENT',
                           'This means you have a badly placed ]',
                           'The offensive list is:',
                           element,
                           'This list will be stripped from your layout' , keep_on_top=True
                           )
                continue
            elif callable(element) and not isinstance(element, Element):
                PopupError('Error creating Column layout',
                           'Layout has a FUNCTION instead of an ELEMENT',
                           'This likely means you are missing () from your layout',
                           'The offensive list is:',
                           element,
                           'This item will be stripped from your layout', keep_on_top=True)
                continue
            if element.ParentContainer is not None:
                warnings.warn('*** YOU ARE ATTEMPTING TO RESUSE AN ELEMENT IN YOUR LAYOUT! Once placed in a layout, an element cannot be used in another layout. ***', UserWarning)
                PopupError('Error creating Column layout',
                           'The layout specified has already been used',
                           'You MUST start witha "clean", unused layout every time you create a window',
                           'The offensive Element = ',
                           element,
                           'and has a key = ', element.Key,
                           'This item will be stripped from your layout',
                           'Hint - try printing your layout and matching the IDs "print(layout)"', keep_on_top=True)
                continue
            element.Position = (CurrentRowNumber, i)
            element.ParentContainer = self
            CurrentRow.append(element)
            if element.Key is not None:
                self.UseDictionary = True
        # -------------------------  Append the row to list of Rows  ------------------------- #
        self.Rows.append(CurrentRow)

    def Layout(self, rows):
        """
        Can use like the Window.Layout method, but it's better to use the layout parameter when creating

        :param rows: The rows of Elements
        :type rows: List[List[Element]]
        :return: Used for chaining
        :rtype: (Column)
        """

        for row in rows:
            try:
                iter(row)
            except TypeError:
                PopupError('Error creating Column layout',
                           'Your row is not an iterable (e.g. a list)',
                           'Instead of a list, the type found was {}'.format(type(row)),
                           'The offensive row = ',
                           row,
                           'This item will be stripped from your layout', keep_on_top=True)
                continue
            self.AddRow(*row)
        return self


    def _GetElementAtLocation(self, location):
        """
        Not user callable. Used to find the Element at a row, col position within the layout

        :param location: (row, column) position of the element to find in layout
        :typeparam location: Tuple[int, int]
        :return: The element found at the location
        :rtype: (Element)
        """

        (row_num, col_num) = location
        row = self.Rows[row_num]
        element = row[col_num]
        return element

    def Update(self, visible=None):
        """
        Changes some of the settings for the Column Element. Must call `Window.Read` or `Window.Finalize` prior

        :param visible: control visibility of element
        :type visible: (bool)
        """
        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if visible is False:
            if self.TKColFrame:
                self.TKColFrame.pack_forget()
            if self.ParentPanedWindow:
                self.ParentPanedWindow.remove(self.TKColFrame)
        elif visible is True:
            if self.TKColFrame:
                self.TKColFrame.pack(padx=self.pad_used[0], pady=self.pad_used[1])
            if self.ParentPanedWindow:
                self.ParentPanedWindow.add(self.TKColFrame)

    add_row = AddRow
    layout = Layout
    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update


Col = Column


# ---------------------------------------------------------------------- #
#                           Pane                                         #
# ---------------------------------------------------------------------- #
class Pane(Element):
    """
    A sliding Pane that is unique to tkinter.  Uses Columns to create individual panes
    """

    def __init__(self, pane_list, background_color=None, size=(None, None), pad=None, orientation='vertical',
                 show_handle=True, relief=RELIEF_RAISED, handle_size=None, border_width=None, key=None, visible=True, metadata=None):
        """
        :param pane_list: Must be a list of Column Elements. Each Column supplied becomes one pane that's shown
        :type pane_list: List[Column]
        :param background_color: color of background
        :type background_color: (str)
        :param size: (width, height) w=characters-wide, h=rows-high How much room to reserve for the Pane
        :type size: Tuple[int, int]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param orientation: 'horizontal' or 'vertical' or ('h' or 'v'). Direction the Pane should slide
        :type orientation: (str)
        :param show_handle: if True, the handle is drawn that makes it easier to grab and slide
        :type show_handle: (bool)
        :param relief: relief style. Values are same as other elements that use relief values. RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID
        :type relief: (enum)
        :param handle_size: Size of the handle in pixels
        :type handle_size: (int)
        :param border_width: width of border around element in pixels
        :type border_width: (int)
        :param key: Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
        :type key: (any)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.UseDictionary = False
        self.ReturnValues = None
        self.ReturnValuesList = []
        self.ReturnValuesDictionary = {}
        self.DictionaryKeyCounter = 0
        self.ParentWindow = None
        self.Rows = []
        self.TKFrame = None
        self.PanedWindow = None
        self.Orientation = orientation
        self.PaneList = pane_list
        self.ShowHandle = show_handle
        self.Relief = relief
        self.HandleSize = handle_size or 8
        self.BorderDepth = border_width
        bg = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR

        self.Rows = [pane_list]

        super().__init__(ELEM_TYPE_PANE, background_color=bg, size=size, pad=pad, key=key, visible=visible, metadata=metadata)
        return

    def Update(self, visible=None):
        """
        Changes some of the settings for the Pane Element. Must call `Window.Read` or `Window.Finalize` prior

        :param visible: control visibility of element
        :type visible: (bool)
        """
        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if visible is False:
            self.PanedWindow.pack_forget()
        elif visible is True:
            self.PanedWindow.pack(padx=self.pad_used[0], pady=self.pad_used[1])

    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update


# ---------------------------------------------------------------------- #
#                           Calendar                                     #
# ---------------------------------------------------------------------- #
class TKCalendar(ttk.Frame):
    """
    This code was shamelessly lifted from moshekaplan's repository - moshekaplan/tkinter_components
    NONE of this code is user callable.  Stay away!
    """
    # XXX ToDo: cget and configure

    datetime = calendar.datetime.datetime
    timedelta = calendar.datetime.timedelta

    def __init__(self, master=None, target_element=None, close_when_chosen=True, default_date=(None, None, None), **kw):
        """WIDGET-SPECIFIC OPTIONS: locale, firstweekday, year, month, selectbackground, selectforeground """
        self._TargetElement = target_element
        default_mon, default_day, default_year = default_date
        # remove custom options from kw before initializating ttk.Frame
        fwday = kw.pop('firstweekday', calendar.MONDAY)
        year = kw.pop('year', default_year or self.datetime.now().year)
        month = kw.pop('month', default_mon or self.datetime.now().month)
        locale = kw.pop('locale', None)
        sel_bg = kw.pop('selectbackground', '#ecffc4')
        sel_fg = kw.pop('selectforeground', '#05640e')
        self.format = kw.pop('format')
        if self.format is None:
            self.format = '%Y-%m-%d %H:%M:%S'

        self._date = self.datetime(year, month, default_day or 1)
        self._selection = None  # no date selected
        self._master = master
        self.close_when_chosen = close_when_chosen
        ttk.Frame.__init__(self, master, **kw)

        # instantiate proper calendar class
        if locale is None:
            self._cal = calendar.TextCalendar(fwday)
        else:
            self._cal = calendar.LocaleTextCalendar(fwday, locale)

        self.__setup_styles()  # creates custom styles
        self.__place_widgets()  # pack/grid used widgets
        self.__config_calendar()  # adjust calendar columns and setup tags
        # configure a canvas, and proper bindings, for selecting dates
        self.__setup_selection(sel_bg, sel_fg)

        # store items ids, used for insertion later
        self._items = [self._calendar.insert('', 'end', values='')
                       for _ in range(6)]
        # insert dates in the currently empty calendar
        self._build_calendar()

    def __setitem__(self, item, value):
        if item in ('year', 'month'):
            raise AttributeError("attribute '%s' is not writeable" % item)
        elif item == 'selectbackground':
            self._canvas['background'] = value
        elif item == 'selectforeground':
            self._canvas.itemconfigure(self._canvas.text, item=value)
        else:
            ttk.Frame.__setitem__(self, item, value)

    def __getitem__(self, item):
        if item in ('year', 'month'):
            return getattr(self._date, item)
        elif item == 'selectbackground':
            return self._canvas['background']
        elif item == 'selectforeground':
            return self._canvas.itemcget(self._canvas.text, 'fill')
        else:
            r = ttk.tclobjs_to_py({item: ttk.Frame.__getitem__(self, item)})
            return r[item]

    def __setup_styles(self):
        # custom ttk styles
        style = ttk.Style(self.master)
        arrow_layout = lambda dir: (
            [('Button.focus', {'children': [('Button.%sarrow' % dir, None)]})]
        )
        style.layout('L.TButton', arrow_layout('left'))
        style.layout('R.TButton', arrow_layout('right'))

    def __place_widgets(self):
        # header frame and its widgets
        hframe = ttk.Frame(self)
        lbtn = ttk.Button(hframe, style='L.TButton', command=self._prev_month)
        rbtn = ttk.Button(hframe, style='R.TButton', command=self._next_month)
        self._header = ttk.Label(hframe, width=15, anchor='center')
        # the calendar
        self._calendar = ttk.Treeview(self, show='', selectmode='none', height=7)

        # pack the widgets
        hframe.pack(in_=self, side='top', pady=4, anchor='center')
        lbtn.grid(in_=hframe)
        self._header.grid(in_=hframe, column=1, row=0, padx=12)
        rbtn.grid(in_=hframe, column=2, row=0)
        self._calendar.pack(in_=self, expand=1, fill='both', side='bottom')

    def __config_calendar(self):
        cols = self._cal.formatweekheader(3).split()
        self._calendar['columns'] = cols
        self._calendar.tag_configure('header', background='grey90')
        self._calendar.insert('', 'end', values=cols, tag='header')
        # adjust its columns width
        font = tkinter.font.Font()
        maxwidth = max(font.measure(col) for col in cols)
        for col in cols:
            self._calendar.column(col, width=maxwidth, minwidth=maxwidth,
                                  anchor='e')

    def __setup_selection(self, sel_bg, sel_fg):
        self._font = tkinter.font.Font()
        self._canvas = canvas = tk.Canvas(self._calendar,
                                          background=sel_bg, borderwidth=0, highlightthickness=0)
        canvas.text = canvas.create_text(0, 0, fill=sel_fg, anchor='w')

        canvas.bind('<ButtonPress-1>', lambda evt: canvas.place_forget())
        self._calendar.bind('<Configure>', lambda evt: canvas.place_forget())
        self._calendar.bind('<ButtonPress-1>', self._pressed)

    def __minsize(self, evt):
        width, height = self._calendar.master.geometry().split('x')
        height = height[:height.index('+')]
        self._calendar.master.minsize(width, height)

    def _build_calendar(self):
        year, month = self._date.year, self._date.month

        # update header text (Month, YEAR)
        header = self._cal.formatmonthname(year, month, 0)
        self._header['text'] = header.title()

        # update calendar shown dates
        cal = self._cal.monthdayscalendar(year, month)
        for indx, item in enumerate(self._items):
            week = cal[indx] if indx < len(cal) else []
            fmt_week = [('%02d' % day) if day else '' for day in week]
            self._calendar.item(item, values=fmt_week)

    def _show_selection(self, text, bbox):
        """ Configure canvas for a new selection. """
        x, y, width, height = bbox

        textw = self._font.measure(text)

        canvas = self._canvas
        canvas.configure(width=width, height=height)
        canvas.coords(canvas.text, width - textw, height / 2 - 1)
        canvas.itemconfigure(canvas.text, text=text)
        canvas.place(in_=self._calendar, x=x, y=y)

    # Callbacks

    def _pressed(self, evt):
        """ Clicked somewhere in the calendar. """
        x, y, widget = evt.x, evt.y, evt.widget
        item = widget.identify_row(y)
        column = widget.identify_column(x)

        if not column or not item in self._items:
            # clicked in the weekdays row or just outside the columns
            return

        item_values = widget.item(item)['values']
        if not len(item_values):  # row is empty for this month
            return

        text = item_values[int(column[1]) - 1]
        if not text:  # date is empty
            return

        bbox = widget.bbox(item, column)
        if not bbox:  # calendar not visible yet
            return

        # update and then show selection
        text = '%02d' % text
        self._selection = (text, item, column)
        self._show_selection(text, bbox)
        year, month = self._date.year, self._date.month
        now = self.datetime.now()
        try:
            self._TargetElement.Update(
                self.datetime(year, month, int(self._selection[0]), now.hour, now.minute, now.second).strftime(
                    self.format))
            if self._TargetElement.ChangeSubmits:
                self._TargetElement.ParentForm.LastButtonClicked = self._TargetElement.Key
                self._TargetElement.ParentForm.FormRemainedOpen = True
                self._TargetElement.ParentForm.TKroot.quit()  # kick the users out of the mainloop
        except:
            pass
        if self.close_when_chosen:
            self._master.destroy()

    def _prev_month(self):
        """Updated calendar to show the previous month."""
        self._canvas.place_forget()

        self._date = self._date - self.timedelta(days=1)
        self._date = self.datetime(self._date.year, self._date.month, 1)
        self._build_calendar()  # reconstuct calendar

    def _next_month(self):
        """Update calendar to show the next month."""
        self._canvas.place_forget()

        year, month = self._date.year, self._date.month
        self._date = self._date + self.timedelta(
            days=calendar.monthrange(year, month)[1] + 1)
        self._date = self.datetime(self._date.year, self._date.month, 1)
        self._build_calendar()  # reconstruct calendar

    # Properties

    @property
    def selection(self):
        if not self._selection:
            return None

        year, month = self._date.year, self._date.month
        return self.datetime(year, month, int(self._selection[0]))


# ---------------------------------------------------------------------- #
#                           Menu                                         #
# ---------------------------------------------------------------------- #
class Menu(Element):
    """
    Menu Element is the Element that provides a Menu Bar that goes across the top of the window, just below titlebar.
    Here is an example layout.  The "&" are shortcut keys ALT+key.
    Is a List of -  "Item String" + List
    Where Item String is what will be displayed on the Menubar itself.
    The List that follows the item represents the items that are shown then Menu item is clicked
    Notice how an "entry" in a mennu can be a list which means it branches out and shows another menu, etc. (resursive)
    menu_def = [['&File', ['!&Open', '&Save::savekey', '---', '&Properties', 'E&xit']],
                ['!&Edit', ['!&Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['&Debugger', ['Popout', 'Launch Debugger']],
                ['&Toolbar', ['Command &1', 'Command &2', 'Command &3', 'Command &4']],
                ['&Help', '&About...'], ]
    Finally, "keys" can be added to entries so make them unique.  The "Save" entry has a key associated with it. You
    can see it has a "::" which signifies the beginning of a key.  The user will not see the key portion when the
    menu is shown.  The key portion is returned as part of the event.
    """

    def __init__(self, menu_definition, background_color=None, size=(None, None), tearoff=False, font=None, pad=None, key=None,
                 visible=True, metadata=None):
        """
        :param menu_definition: ???
        :type menu_definition: List[List[Tuple[str, List[str]]]
        :param background_color: color of the background
        :type background_color: (str)
        :param size: Not used in the tkinter port
        :type size: Tuple[int, int]
        :param tearoff: if True, then can tear the menu off from the window ans use as a floating window. Very cool effect
        :type tearoff: (bool)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param key: Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
        :type key: (any)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.MenuDefinition = menu_definition
        self.Widget = self.TKMenu = None  # type: tk.Menu
        self.Tearoff = tearoff
        self.MenuItemChosen = None

        super().__init__(ELEM_TYPE_MENUBAR, background_color=background_color, size=size, pad=pad, key=key,
                         visible=visible, font=font, metadata=metadata)
        return

    def _MenuItemChosenCallback(self, item_chosen):  # Menu Menu Item Chosen Callback
        """
        Not user callable.  Called when some end-point on the menu (an item) has been clicked.  Send the information back to the application as an event.  Before event can be sent

        :param item_chosen: the text that was clicked on / chosen from the menu
        :type item_chosen: (str)
        """
        # print('IN MENU ITEM CALLBACK', item_chosen)
        self.MenuItemChosen = item_chosen
        self.ParentForm.LastButtonClicked = item_chosen
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

    def Update(self, menu_definition=None, visible=None):
        """
        Update a menubar - can change the menu definition and visibility.  The entire menu has to be specified

        :param menu_definition: ???
        :type menu_definition: List[List[Tuple[str, List[str]]]
        :param visible: control visibility of element
        :type visible: (bool)
        """
        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if menu_definition is not None:
            self.MenuDefinition = menu_definition
            self.TKMenu = tk.Menu(self.ParentForm.TKroot, tearoff=self.Tearoff)  # create the menubar
            menubar = self.TKMenu
            for menu_entry in menu_definition:
                # print(f'Adding a Menubar ENTRY {menu_entry}')
                baritem = tk.Menu(menubar, tearoff=self.Tearoff)
                pos = menu_entry[0].find('&')
                # print(pos)
                if pos != -1:
                    if pos == 0 or menu_entry[0][pos - 1] != "\\":
                        menu_entry[0] = menu_entry[0][:pos] + menu_entry[0][pos + 1:]
                if menu_entry[0][0] == MENU_DISABLED_CHARACTER:
                    menubar.add_cascade(label=menu_entry[0][len(MENU_DISABLED_CHARACTER):], menu=baritem, underline=pos)
                    menubar.entryconfig(menu_entry[0][len(MENU_DISABLED_CHARACTER):], state='disabled')
                else:
                    menubar.add_cascade(label=menu_entry[0], menu=baritem, underline=pos)

                if len(menu_entry) > 1:
                    AddMenuItem(baritem, menu_entry[1], self)

        if visible == False:
            self.ParentForm.TKroot.configure(menu=[])  # this will cause the menubar to disappear
        elif self.TKMenu is not None:
            self.ParentForm.TKroot.configure(menu=self.TKMenu)

    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update


MenuBar = Menu  # another name for Menu to make it clear it's the Menu Bar


# ---------------------------------------------------------------------- #
#                           Table                                        #
# ---------------------------------------------------------------------- #
class Table(Element):

    def __init__(self, values, headings=None, visible_column_map=None, col_widths=None, def_col_width=10,
                 auto_size_columns=True, max_col_width=20, select_mode=None, display_row_numbers=False, num_rows=None,
                 row_height=None, font=None, justification='right', text_color=None, background_color=None,
                 alternating_row_color=None, header_text_color=None, header_background_color=None, header_font=None, row_colors=None, vertical_scroll_only=True, hide_vertical_scroll=False,
                 size=(None, None), change_submits=False, enable_events=False, bind_return_key=False, pad=None,
                 key=None, tooltip=None, right_click_menu=None, visible=True, metadata=None):
        """
        :param values: ???
        :type values: List[List[Union[str, int, float]]]
        :param headings: The headings to show on the top line
        :type headings: List[str]
        :param visible_column_map: One entry for each column. False indicates the column is not shown
        :type visible_column_map: List[bool]
        :param col_widths: Number of characters that each column will occupy
        :type col_widths: List[int]
        :param def_col_width: Default column width in characters
        :type def_col_width: (int)
        :param auto_size_columns: if True columns will be sized automatically
        :type auto_size_columns: (bool)
        :param max_col_width: Maximum width for all columns in characters
        :type max_col_width: (int)
        :param select_mode: Select Mode. Valid values start with "TABLE_SELECT_MODE_".  Valid values are: TABLE_SELECT_MODE_NONE TABLE_SELECT_MODE_BROWSE TABLE_SELECT_MODE_EXTENDED
        :type select_mode: (enum)
        :param display_row_numbers: if True, the first column of the table will be the row #
        :type display_row_numbers: (bool)
        :param num_rows: The number of rows of the table to display at a time
        :type num_rows: (int)
        :param row_height: height of a single row in pixels
        :type row_height: (int)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param justification: 'left', 'right', 'center' are valid choices
        :type justification: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param background_color: color of background
        :type background_color: (str)
        :param alternating_row_color: if set then every other row will have this color in the background.
        :type alternating_row_color: (str)
        :param header_text_color: sets the text color for the header
        :type header_text_color: (str)
        :param header_background_color: sets the background color for the header
        :type header_background_color: (str)
        :param header_font: specifies the font family, size, etc
        :type header_font: Union[str, Tuple[str, int]]
        :param row_colors: list of tuples of (row, background color) OR (row, foreground color, background color). Sets the colors of listed rows to the color(s) provided (note the optional foreground color)
        :type row_colors: List[Union[Tuple[int, str], Tuple[Int, str, str]]
        :param vertical_scroll_only: if True only the vertical scrollbar will be visible
        :type vertical_scroll_only: (bool)
        :param hide_vertical_scroll: if True vertical scrollbar will be hidden
        :type hide_vertical_scroll: (bool)
        :param size: DO NOT USE! Use num_rows instead
        :type size: Tuple[int, int]
        :param change_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type change_submits: (bool)
        :param enable_events: Turns on the element specific events. Table events happen when row is clicked
        :type enable_events: (bool)
        :param bind_return_key: if True, pressing return key will cause event coming from Table, ALSO a left button double click will generate an event if this parameter is True
        :type bind_return_key: (bool)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param right_click_menu: A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
        :type right_click_menu: List[List[Union[List[str],str]]]
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.Values = values
        self.ColumnHeadings = headings
        self.ColumnsToDisplay = visible_column_map
        self.ColumnWidths = col_widths
        self.MaxColumnWidth = max_col_width
        self.DefaultColumnWidth = def_col_width
        self.AutoSizeColumns = auto_size_columns
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.TextColor = text_color
        self.HeaderTextColor = header_text_color if header_text_color is not None else LOOK_AND_FEEL_TABLE[CURRENT_LOOK_AND_FEEL]['TEXT_INPUT']
        self.HeaderBackgroundColor = header_background_color if header_background_color is not None else LOOK_AND_FEEL_TABLE[CURRENT_LOOK_AND_FEEL]['INPUT']
        self.HeaderFont = header_font
        self.Justification = justification
        self.InitialState = None
        self.SelectMode = select_mode
        self.DisplayRowNumbers = display_row_numbers
        self.NumRows = num_rows if num_rows is not None else size[1]
        self.RowHeight = row_height
        self.Widget = self.TKTreeview = None  # type: ttk.Treeview
        self.AlternatingRowColor = alternating_row_color
        self.VerticalScrollOnly = vertical_scroll_only
        self.HideVerticalScroll = hide_vertical_scroll
        self.SelectedRows = []
        self.ChangeSubmits = change_submits or enable_events
        self.BindReturnKey = bind_return_key
        self.StartingRowNumber = 0  # When displaying row numbers, where to start
        self.RowHeaderText = 'Row'
        self.RightClickMenu = right_click_menu
        self.RowColors = row_colors
        self.tree_ids = []  # ids returned when inserting items into table - will use to delete colors
        super().__init__(ELEM_TYPE_TABLE, text_color=text_color, background_color=background_color, font=font,
                         size=size, pad=pad, key=key, tooltip=tooltip, visible=visible, metadata=metadata)
        return

    def Update(self, values=None, num_rows=None, visible=None, select_rows=None, alternating_row_color=None, row_colors=None):
        """
        Changes some of the settings for the Table Element. Must call `Window.Read` or `Window.Finalize` prior

        :param values: A new 2-dimensional table to show
        :type values: List[List[Union[str, int, float]]]
        :param num_rows: How many rows to display at a time
        :type num_rows: (int)
        :param visible: if True then will be visible
        :type visible: (bool)
        :param select_rows: List of rows to select as if user did
        :type select_rows: List[int]
        :param alternating_row_color: the color to make every other row
        :type alternating_row_color: (str)
        :param row_colors: list of tuples of (row, background color) OR (row, foreground color, background color). Changes the colors of listed rows to the color(s) provided (note the optional foreground color)
        :type row_colors: List[Union[Tuple[int, str], Tuple[Int, str, str]]
        """
        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if values is not None:
            for id in self.tree_ids:
                self.TKTreeview.item(id, tags=())
                if self.BackgroundColor is not None and self.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    self.TKTreeview.tag_configure(id, background=self.BackgroundColor)
                else:
                    self.TKTreeview.tag_configure(id, background='#FFFFFF', foreground='#000000')
                if self.TextColor is not None and self.TextColor != COLOR_SYSTEM_DEFAULT:
                    self.TKTreeview.tag_configure(id, foreground=self.TextColor)
                else:
                    self.TKTreeview.tag_configure(id, foreground='#000000')

            children = self.TKTreeview.get_children()
            for i in children:
                self.TKTreeview.detach(i)
                self.TKTreeview.delete(i)
            children = self.TKTreeview.get_children()

            self.tree_ids = []
            for i, value in enumerate(values):
                if self.DisplayRowNumbers:
                    value = [i + self.StartingRowNumber] + value
                id = self.TKTreeview.insert('', 'end', text=value, iid=i + 1, values=value, tag=i)
                if self.BackgroundColor is not None and self.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    self.TKTreeview.tag_configure(id, background=self.BackgroundColor)
                else:
                    self.TKTreeview.tag_configure(id, background='#FFFFFF')
                self.tree_ids.append(id)
            self.Values = values
            self.SelectedRows = []
        if visible is False:
            self.TKTreeview.pack_forget()
        elif visible is True:
            self.TKTreeview.pack(padx=self.pad_used[0], pady=self.pad_used[1])
        if num_rows is not None:
            self.TKTreeview.config(height=num_rows)
        if select_rows is not None:
            rows_to_select = [i + 1 for i in select_rows]
            self.TKTreeview.selection_set(rows_to_select)

        if alternating_row_color is not None:  # alternating colors
            self.AlternatingRowColor = alternating_row_color

        if self.AlternatingRowColor is not None:
            for row in range(0, len(self.Values), 2):
                self.TKTreeview.tag_configure(row, background=self.AlternatingRowColor)
        if row_colors is not None:  # individual row colors
            self.RowColors = row_colors
            for row_def in self.RowColors:
                if len(row_def) == 2:  # only background is specified
                    self.TKTreeview.tag_configure(row_def[0], background=row_def[1])
                else:
                    self.TKTreeview.tag_configure(row_def[0], background=row_def[2], foreground=row_def[1])

    def _treeview_selected(self, event):
        """
        Not user callable.  Callback function that is called when something is selected from Table.
        Stores the selected rows in Element as they are being selected. If events enabled, then returns from Read

        :param event: (unknown) event information from tkinter
        """
        selections = self.TKTreeview.selection()
        self.SelectedRows = [int(x) - 1 for x in selections]
        if self.ChangeSubmits:
            if self.Key is not None:
                self.ParentForm.LastButtonClicked = self.Key
            else:
                self.ParentForm.LastButtonClicked = ''
            self.ParentForm.FormRemainedOpen = True
            if self.ParentForm.CurrentlyRunningMainloop:
                self.ParentForm.TKroot.quit()

    def _treeview_double_click(self, event):
        """
        Not user callable.  Callback function that is called when something is selected from Table.
        Stores the selected rows in Element as they are being selected. If events enabled, then returns from Read

        :param event: (unknown) event information from tkinter
        """
        selections = self.TKTreeview.selection()
        self.SelectedRows = [int(x) - 1 for x in selections]
        if self.BindReturnKey:  # Signifies BOTH a return key AND a double click
            if self.Key is not None:
                self.ParentForm.LastButtonClicked = self.Key
            else:
                self.ParentForm.LastButtonClicked = ''
            self.ParentForm.FormRemainedOpen = True
            if self.ParentForm.CurrentlyRunningMainloop:
                self.ParentForm.TKroot.quit()

    def Get(self):
        """
        Dummy function for tkinter port.  In the Qt port you can read back the values in the table in case they were
        edited.  Don't know yet how to enable editing of a Tree in tkinter so just returning the values provided by
        user when Table was created or Updated.

        :return: the current table values (for now what was originally provided up updated)
        :rtype: List[List[Any]]
        """
        return self.Values

    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update
    get = Get


# ---------------------------------------------------------------------- #
#                           Tree                                         #
# ---------------------------------------------------------------------- #
class Tree(Element):
    """
    Tree Element - Presents data in a tree-like manner, much like a file/folder browser.  Uses the TreeData class
    to hold the user's data and pass to the element for display.
    """

    def __init__(self, data=None, headings=None, visible_column_map=None, col_widths=None, col0_width=10,
                 def_col_width=10, auto_size_columns=True, max_col_width=20, select_mode=None, show_expanded=False,
                 change_submits=False, enable_events=False, font=None, justification='right', text_color=None,
                 background_color=None, header_text_color=None, header_background_color=None, header_font=None, num_rows=None, row_height=None, pad=None, key=None, tooltip=None,
                 right_click_menu=None, visible=True, metadata=None):
        """
        :param data: The data represented using a PySimpleGUI provided TreeData class
        :type data: (TreeData)
        :param headings: List of individual headings for each column
        :type headings: List[str]
        :param visible_column_map: Determines if a column should be visible. If left empty, all columns will be shown
        :type visible_column_map: List[bool]
        :param col_widths: List of column widths so that individual column widths can be controlled
        :type col_widths: List[int]
        :param col0_width: Size of Column 0 which is where the row numbers will be optionally shown
        :type col0_width: (int)
        :param def_col_width: default column width
        :type def_col_width: (int)
        :param auto_size_columns: if True, the size of a column is determined  using the contents of the column
        :type auto_size_columns: (bool)
        :param max_col_width: the maximum size a column can be
        :type max_col_width: (int)
        :param select_mode: Use same values as found on Table Element.  Valid values include: TABLE_SELECT_MODE_NONE TABLE_SELECT_MODE_BROWSE TABLE_SELECT_MODE_EXTENDED
        :type select_mode: (enum)
        :param show_expanded: if True then the tree will be initially shown with all nodes completely expanded
        :type show_expanded: (bool)
        :param change_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type change_submits: (bool)
        :param enable_events: Turns on the element specific events. Tree events happen when row is clicked
        :type enable_events: (bool)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param justification: 'left', 'right', 'center' are valid choices
        :type justification: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param background_color: color of background
        :type background_color: (str)
        :param header_text_color: sets the text color for the header
        :type header_text_color: (str)
        :param header_background_color: sets the background color for the header
        :type header_background_color: (str)
        :param header_font: specifies the font family, size, etc
        :type header_font: Union[str, Tuple[str, int]]
        :param num_rows: The number of rows of the table to display at a time
        :type num_rows: (int)
        :param row_height: height of a single row in pixels
        :type row_height: (int)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param right_click_menu: [Union[List[str],str]]] A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
        :type right_click_menu: List[List
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.TreeData = data
        self.ColumnHeadings = headings
        self.ColumnsToDisplay = visible_column_map
        self.ColumnWidths = col_widths
        self.MaxColumnWidth = max_col_width
        self.DefaultColumnWidth = def_col_width
        self.AutoSizeColumns = auto_size_columns
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.TextColor = text_color
        self.HeaderTextColor = header_text_color if header_text_color is not None else LOOK_AND_FEEL_TABLE[CURRENT_LOOK_AND_FEEL]['TEXT_INPUT']
        self.HeaderBackgroundColor = header_background_color if header_background_color is not None else LOOK_AND_FEEL_TABLE[CURRENT_LOOK_AND_FEEL]['INPUT']
        self.HeaderFont = header_font
        self.Justification = justification
        self.InitialState = None
        self.SelectMode = select_mode
        self.ShowExpanded = show_expanded
        self.NumRows = num_rows
        self.Col0Width = col0_width
        self.TKTreeview = None
        self.SelectedRows = []
        self.ChangeSubmits = change_submits or enable_events
        self.RightClickMenu = right_click_menu
        self.RowHeight = row_height
        self.IconList = {}
        self.IdToKey = {'': ''}
        self.KeyToID = {'': ''}

        super().__init__(ELEM_TYPE_TREE, text_color=text_color, background_color=background_color, font=font, pad=pad,
                         key=key, tooltip=tooltip, visible=visible, metadata=metadata)
        return

    def _treeview_selected(self, event):
        """
        Not a user function.  Callback function that happens when an item is selected from the tree.  In this
        method, it saves away the reported selections so they can be properly returned.

        :param event: An event parameter passed in by tkinter.  Not used
        :type event: (Any)
        """

        selections = self.TKTreeview.selection()
        # self.SelectedRows = [x for x in selections]
        self.SelectedRows = [self.IdToKey[x] for x in selections]
        if self.ChangeSubmits:
            MyForm = self.ParentForm
            if self.Key is not None:
                self.ParentForm.LastButtonClicked = self.Key
            else:
                self.ParentForm.LastButtonClicked = ''
            self.ParentForm.FormRemainedOpen = True
            if self.ParentForm.CurrentlyRunningMainloop:
                self.ParentForm.TKroot.quit()

    def add_treeview_data(self, node):
        """
        Not a user function.  Recursive method that inserts tree data into the tkinter treeview widget.

        :param node: The node to insert.  Will insert all nodes from starting point downward, recursively
        :type node: (TreeData)
        """
        if node.key != '':
            if node.icon:
                try:
                    if type(node.icon) is bytes:
                        photo = tk.PhotoImage(data=node.icon)
                    else:
                        photo = tk.PhotoImage(file=node.icon)
                    node.photo = photo
                    id = self.TKTreeview.insert(self.KeyToID[node.parent], 'end', iid=None, text=node.text,
                                                values=node.values, open=self.ShowExpanded, image=node.photo)
                    self.IdToKey[id] = node.key
                    self.KeyToID[node.key] = id
                except:
                    self.photo = None
            else:
                id = self.TKTreeview.insert(self.KeyToID[node.parent], 'end', iid=None, text=node.text,
                                            values=node.values, open=self.ShowExpanded)
                self.IdToKey[id] = node.key
                self.KeyToID[node.key] = id

        for node in node.children:
            self.add_treeview_data(node)

    def Update(self, values=None, key=None, value=None, text=None, icon=None, visible=None):
        """
        Changes some of the settings for the Tree Element. Must call `Window.Read` or `Window.Finalize` prior

        :param values: Representation of the tree
        :type values: (TreeData)
        :param key: identifies a particular item in tree to update
        :type key: (Any)
        :param value: sets the node identified by key to a particular value
        :type value: (Any)
        :param text: sets the node identified by ket to this string
        :type text: (str)
        :param icon: can be either a base64 icon or a filename for the icon
        :type icon: Union[bytes, str]
        :param visible: control visibility of element
        :type visible: (bool)
        """
        if self.Widget is None:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            return
        if values is not None:
            children = self.TKTreeview.get_children()
            for i in children:
                self.TKTreeview.detach(i)
                self.TKTreeview.delete(i)
            children = self.TKTreeview.get_children()
            self.TreeData = values
            self.IdToKey = {'': ''}
            self.KeyToID = {'': ''}
            self.add_treeview_data(self.TreeData.root_node)
            self.SelectedRows = []
        if key is not None:
            for id in self.IdToKey.keys():
                if key == self.IdToKey[id]:
                    break
            else:
                id = None
                print('** Key not found **')
        else:
            id = None
        if id:
            # item = self.TKTreeview.item(id)
            if value is not None:
                self.TKTreeview.item(id, values=value)
            if text is not None:
                self.TKTreeview.item(id, text=text)
            if icon is not None:
                try:
                    if type(icon) is bytes:
                        photo = tk.PhotoImage(data=icon)
                    else:
                        photo = tk.PhotoImage(file=icon)
                    self.TKTreeview.item(id, image=photo)
                    self.IconList[key] = photo  # save so that it's not deleted (save reference)
                except:
                    pass
            # item = self.TKTreeview.item(id)
        if visible is False:
            self.TKTreeview.pack_forget()
        elif visible is True:
            self.TKTreeview.pack(padx=self.pad_used[0], pady=self.pad_used[1])
        return self

    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update


class TreeData(object):
    """
    Class that user fills in to represent their tree data. It's a very simple tree representation with a root "Node"
    with possibly one or more children "Nodes".  Each Node contains a key, text to display, list of values to display
    and an icon.  The entire tree is built using a single method, Insert.  Nothing else is required to make the tree.
    """

    class Node(object):
        """
        Contains information about the individual node in the tree
        """

        def __init__(self, parent, key, text, values, icon=None):
            """
            :param parent: The parent Node
            :type parent: (TreeData.Node)
            :param key: Used to uniquely identify this node
            :type key: (Any)
            :param text: The text that is displayed at this node's location
            :type text: (str)
            :param values: The list of values that are displayed at this node
            :type values: List[Any]
            :param icon: just a icon
            :type icon: Union[str, bytes]
            """

            self.parent = parent  # type: TreeData.Node
            self.children = []  # type: List[TreeData.Node]
            self.key = key  # type: str
            self.text = text  # type: str
            self.values = values  # type: List[Any]
            self.icon = icon  # type: Union[str, bytes]

        def _Add(self, node):
            self.children.append(node)

    def __init__(self):
        """
        Instantiate the object, initializes the Tree Data, creates a root node for you
        """
        self.tree_dict = {}  # type: Dict[str : TreeData.Node]
        self.root_node = self.Node("", "", 'root', [], None)  # The root node
        self.tree_dict[""] = self.root_node  # Start the tree out with the root node

    def _AddNode(self, key, node):
        """
        Adds a node to tree dictionary (not user callable)

        :param key: Uniquely identifies this Node
        :type key: (str)
        :param node: Node being added
        :type node: (TreeData.Node)
        """
        self.tree_dict[key] = node

    def Insert(self, parent, key, text, values, icon=None):
        """
        Inserts a node into the tree. This is how user builds their tree, by Inserting Nodes
        This is the ONLY user callable method in the TreeData class

        :param parent: the parent Node
        :type parent: (Node)
        :param key: Used to uniquely identify this node
        :type key: (Any)
        :param text: The text that is displayed at this node's location
        :type text: (str)
        :param values: The list of values that are displayed at this node
        :type values: List[Any]
        :param icon: icon
        :type icon: Union[str, bytes]
        """

        node = self.Node(parent, key, text, values, icon)
        self.tree_dict[key] = node
        parent_node = self.tree_dict[parent]
        parent_node._Add(node)

    def __repr__(self):
        """
        Converts the TreeData into a printable version, nicely formatted

        :return: (str) A formatted, text version of the TreeData
        """
        return self._NodeStr(self.root_node, 1)

    def _NodeStr(self, node, level):
        """
        Does the magic of converting the TreeData into a nicely formatted string version

        :param node:  The node to begin printing the tree
        :type node: (TreeData.Node)
        :param level: The indentation level for string formatting
        :type level: (int)
        """
        return '\n'.join(
            [str(node.key) + ' : ' + str(node.text)] +
            [' ' * 4 * level + self._NodeStr(child, level + 1) for child in node.children])

    insert = Insert


# ---------------------------------------------------------------------- #
#                           Error Element                                #
# ---------------------------------------------------------------------- #
class ErrorElement(Element):
    """
    A "dummy Element" that is returned when there are error conditions, like trying to find an element that's invalid
    """

    def __init__(self, key=None, metadata=None):
        """
        :param key:  Used with window.FindElement and with return values to uniquely identify this element
        """
        self.Key = key

        super().__init__(ELEM_TYPE_ERROR, key=key, metadata=metadata)

    def Update(self, silent_on_error=True, *args, **kwargs):
        """
        Update method for the Error Element, an element that should not be directly used by developer

        :param silent_on_error: if False, then a Popup window will be shown
        :type silent_on_error: (bool)
        :param *args:  meant to "soak up" any normal parameters passed in
        :type *args: (Any)
        :param **kwargs:  meant to "soak up" any keyword parameters that were passed in
        :type **kwargs: (Any)
        :return:  returns 'self' so call can be chained
        :rtype: (ErrorElement)
        """
        if not silent_on_error:
            PopupError('Key error in Update',
                       'You need to stop this madness and check your spelling',
                       'Bad key = {}'.format(self.Key),
                       'Your bad line of code may resemble this:',
                       'window.FindElement("{}")'.format(self.Key),
                       'or window["{}"]'.format(self.Key), keep_on_top=True
                       )
        return self

    def Get(self):
        """
        One of the method names found in other Elements. Used here to return an error string in case it's called

        :return:  A warning text string.
        :rtype: (str)
        """
        return 'This is NOT a valid Element!\nSTOP trying to do things with it or I will have to crash at some point!'

    get = Get
    set_focus = Element.SetFocus
    set_tooltip = Element.SetTooltip
    update = Update


# ---------------------------------------------------------------------- #
#                           Stretch Element                              #
# ---------------------------------------------------------------------- #
# This is for source code compatibility with tkinter version. No tkinter equivalent
Stretch = ErrorElement


# ------------------------------------------------------------------------- #
#                       Window CLASS                                        #
# ------------------------------------------------------------------------- #
class Window:
    """
    Represents a single Window
    """
    NumOpenWindows = 0
    _user_defined_icon = None
    hidden_master_root = None
    _animated_popup_dict = {}
    _container_element_counter = 0  # used to get a number of Container Elements (Frame, Column, Tab)
    _read_call_from_debugger = False

    def __init__(self, title, layout=None, default_element_size=DEFAULT_ELEMENT_SIZE,
                 default_button_element_size=(None, None),
                 auto_size_text=None, auto_size_buttons=None, location=(None, None), size=(None, None),
                 element_padding=None, margins=(None, None), button_color=None, font=None,
                 progress_bar_color=(None, None), background_color=None, border_depth=None, auto_close=False,
                 auto_close_duration=DEFAULT_AUTOCLOSE_TIME, icon=None, force_toplevel=False,
                 alpha_channel=1, return_keyboard_events=False, use_default_focus=True, text_justification=None,
                 no_titlebar=False, grab_anywhere=False, keep_on_top=False, resizable=False, disable_close=False,
                 disable_minimize=False, right_click_menu=None, transparent_color=None, debugger_enabled=True,
                 finalize=False, element_justification='left', ttk_theme=None, use_ttk_buttons=None, metadata=None):
        """
        :param title: The title that will be displayed in the Titlebar and on the Taskbar
        :type title: (str)
        :param layout: The layout for the window. Can also be specified in the Layout method
        :type layout: List[List[Elements]]
        :param default_element_size: (width, height) size in characters (wide) and rows (high) for all elements in this window
        :type default_element_size: Tuple[int, int]
        :param default_button_element_size: (width, height) size in characters (wide) and rows (high) for all Button elements in this window
        :type default_button_element_size: Tuple[int, int]
        :param auto_size_text: True if Elements in Window should be sized to exactly fir the length of text
        :type auto_size_text: (bool)
        :param auto_size_buttons: True if Buttons in this Window should be sized to exactly fit the text on this.
        :type auto_size_buttons: (bool)
        :param location: (x,y) location, in pixels, to locate the upper left corner of the window on the screen. Default is to center on screen.
        :type location: Tuple[int, int]
        :param size: (width, height) size in pixels for this window. Normally the window is autosized to fit contents, not set to an absolute size by the user
        :type size: Tuple[int, int]
        :param element_padding: Default amount of padding to put around elements in window (left/right, top/bottom) or ((left, right), (top, bottom))
        :type element_padding: Tuple[int, int] or ((int, int),(int,int))
        :param margins: (left/right, top/bottom) Amount of pixels to leave inside the window's frame around the edges before your elements are shown.
        :type margins: Tuple[int, int]
        :param button_color: (text color, button color) Default button colors for all buttons in the window
        :type button_color: Tuple[str, str]
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param progress_bar_color: (bar color, background color) Sets the default colors for all progress bars in the window
        :type progress_bar_color: Tuple[str, str]
        :param background_color: color of background
        :type background_color: (str)
        :param border_depth: Default border depth (width) for all elements in the window
        :type border_depth: (int)
        :param auto_close: If True, the window will automatically close itself
        :type auto_close: (bool)
        :param auto_close_duration: Number of seconds to wait before closing the window
        :type auto_close_duration: (int)
        :param icon: Can be either a filename or Base64 value. For Windows if filename, it MUST be ICO format. For Linux, must NOT be ICO
        :type icon: Union[str, str]
        :param force_toplevel: If True will cause this window to skip the normal use of a hidden master window
        :type force_toplevel: (bool)
        :param alpha_channel: Sets the opacity of the window. 0 = invisible 1 = completely visible. Values bewteen 0 & 1 will produce semi-transparent windows in SOME environments (The Raspberry Pi always has this value at 1 and cannot change.
        :type alpha_channel: (float)
        :param return_keyboard_events: if True key presses on the keyboard will be returned as Events from Read calls
        :type return_keyboard_events: (bool)
        :param use_default_focus: If True will use the default focus algorithm to set the focus to the "Correct" element
        :type use_default_focus: (bool)
        :param text_justification: Union ['left', 'right', 'center'] Default text justification for all Text Elements in window
        :type text_justification: (str)
        :param no_titlebar: If true, no titlebar nor frame will be shown on window. This means you cannot minimize the window and it will not show up on the taskbar
        :type no_titlebar: (bool)
        :param grab_anywhere: If True can use mouse to click and drag to move the window. Almost every location of the window will work except input fields on some systems
        :type grab_anywhere: (bool)
        :param keep_on_top: If True, window will be created on top of all other windows on screen. It can be bumped down if another window created with this parm
        :type keep_on_top: (bool)
        :param resizable: If True, allows the user to resize the window. Note the not all Elements will change size or location when resizing.
        :type resizable: (bool)
        :param disable_close: If True, the X button in the top right corner of the window will no work.  Use with caution and always give a way out toyour users
        :type disable_close: (bool)
        :param disable_minimize: if True the user won't be able to minimize window.  Good for taking over entire screen and staying that way.
        :type disable_minimize: (bool)
        :param right_click_menu: A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
        :type right_click_menu: List[List[Union[List[str],str]]]
        :param transparent_color: Any portion of the window that has this color will be completely transparent. You can even click through these spots to the window under this window.
        :type transparent_color: (str)
        :param debugger_enabled: If True then the internal debugger will be enabled
        :type debugger_enabled: (bool)
        :param finalize: If True then the Finalize method will be called. Use this rather than chaining .Finalize for cleaner code
        :type finalize: (bool)
        :param element_justification: All elements in the Window itself will have this justification 'left', 'right', 'center' are valid values
        :type element_justification: (str)
        :param ttk_theme: Set the tkinter ttk "theme" of the window.  Default = DEFAULT_TTK_THEME.  Sets all ttk widgets to this theme as their default
        :type ttk_theme: (str)
        :param use_ttk_buttons: Affects all buttons in window. True = use ttk buttons. False = do not use ttk buttons.  None = use ttk buttons only if on a Mac
        :type use_ttk_buttons: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """

        self.AutoSizeText = auto_size_text if auto_size_text is not None else DEFAULT_AUTOSIZE_TEXT
        self.AutoSizeButtons = auto_size_buttons if auto_size_buttons is not None else DEFAULT_AUTOSIZE_BUTTONS
        self.Title = str(title)
        self.Rows = []  # a list of ELEMENTS for this row
        self.DefaultElementSize = default_element_size
        self.DefaultButtonElementSize = default_button_element_size if default_button_element_size != (
            None, None) else DEFAULT_BUTTON_ELEMENT_SIZE
        self.Location = location
        self.ButtonColor = button_color if button_color else DEFAULT_BUTTON_COLOR
        self.BackgroundColor = background_color if background_color else DEFAULT_BACKGROUND_COLOR
        self.ParentWindow = None
        self.Font = font if font else DEFAULT_FONT
        self.RadioDict = {}
        self.BorderDepth = border_depth
        if icon:
            self.WindowIcon = icon
        elif Window._user_defined_icon is not None:
            self.WindowIcon = Window._user_defined_icon
        else:
            self.WindowIcon = DEFAULT_WINDOW_ICON
        self.AutoClose = auto_close
        self.NonBlocking = False
        self.TKroot = None  # type: tk.Tk
        self.TKrootDestroyed = False
        self.CurrentlyRunningMainloop = False
        self.FormRemainedOpen = False
        self.TKAfterID = None
        self.ProgressBarColor = progress_bar_color
        self.AutoCloseDuration = auto_close_duration
        self.RootNeedsDestroying = False
        self.Shown = False
        self.ReturnValues = None
        self.ReturnValuesList = []
        self.ReturnValuesDictionary = {}
        self.DictionaryKeyCounter = 0
        self.LastButtonClicked = None
        self.LastButtonClickedWasRealtime = False
        self.UseDictionary = False
        self.UseDefaultFocus = use_default_focus
        self.ReturnKeyboardEvents = return_keyboard_events
        self.LastKeyboardEvent = None
        self.TextJustification = text_justification
        self.NoTitleBar = no_titlebar
        self.GrabAnywhere = grab_anywhere
        self.KeepOnTop = keep_on_top
        self.ForceTopLevel = force_toplevel
        self.Resizable = resizable
        self._AlphaChannel = alpha_channel
        self.Timeout = None
        self.TimeoutKey = TIMEOUT_KEY
        self.TimerCancelled = False
        self.DisableClose = disable_close
        self.DisableMinimize = disable_minimize
        self._Hidden = False
        self._Size = size
        self.XFound = False
        self.ElementPadding = element_padding or DEFAULT_ELEMENT_PADDING
        self.RightClickMenu = right_click_menu
        self.Margins = margins if margins != (None, None) else DEFAULT_MARGINS
        self.ContainerElemementNumber = Window._GetAContainerNumber()
        self.AllKeysDict = {}
        self.TransparentColor = transparent_color
        self.UniqueKeyCounter = 0
        self.DebuggerEnabled = debugger_enabled
        self.WasClosed = False
        self.ElementJustification = element_justification
        self.FocusSet = False
        self.metadata = metadata
        self.TtkTheme = ttk_theme or DEFAULT_TTK_THEME
        self.UseTtkButtons = use_ttk_buttons if use_ttk_buttons is not None else USE_TTK_BUTTONS
        self.user_bind_dict = {}  # Used when user defines a tkinter binding using bind method - convert bind string to key modifier
        self.user_bind_event = None  # Used when user defines a tkinter binding using bind method - event data from tkinter

        if layout is not None and type(layout) not in (list, tuple):
            warnings.warn('Your layout is not a list or tuple... this is not good!')

        if layout is not None:
            self.Layout(layout)
            if finalize:
                self.Finalize()

        if CURRENT_LOOK_AND_FEEL == 'Default':
            print("Window will be a boring gray. Try adding call to change_look_and_feel('Dark Blue 3') before your layout definition\n",
                  "If you seriously want this gray window and no more nagging, add  change_look_and_feel('DefaultNoMoreNagging') ")

    @classmethod
    def _GetAContainerNumber(cls):
        """
        Not user callable!
        :return: A simple counter that makes each container element unique
        """
        cls._container_element_counter += 1
        return cls._container_element_counter

    @classmethod
    def _IncrementOpenCount(self):
        """
        Not user callable!  Increments the number of open windows
        Note - there is a bug where this count easily gets out of sync. Issue has been opened already. No ill effects
        """
        self.NumOpenWindows += 1
        # print('+++++ INCREMENTING Num Open Windows = {} ---'.format(Window.NumOpenWindows))

    @classmethod
    def _DecrementOpenCount(self):
        """
        Not user callable!  Decrements the number of open windows
        """
        self.NumOpenWindows -= 1 * (self.NumOpenWindows != 0)  # decrement if not 0
        # print('----- DECREMENTING Num Open Windows = {} ---'.format(Window.NumOpenWindows))

    @classmethod
    def get_screen_size(self):
        """
        Returns the size of the "screen" as determined by tkinter.  This can vary depending on your operating system and the number of monitors installed on your system.  For Windows, the primary monitor's size is returns. On some multi-monitored Linux systems, the monitors are combined and the total size is reported as if one screen.

        :return: Tuple[int, int] - Size of the screen in pixels as determined by tkinter
        """
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()  # get window info to move to middle of screen
        screen_height = root.winfo_screenheight()
        root.destroy()
        return screen_width, screen_height

    # ------------------------- Add ONE Row to Form ------------------------- #
    def AddRow(self, *args):
        """
        Adds a single row of elements to a window's self.Rows variables.
        Generally speaking this is NOT how users should be building Window layouts.
        Users, create a single layout (a list of lists) and pass as a parameter to Window object, or call Window.Layout(layout)

        :param *args: List[Elements]
        """
        NumRows = len(self.Rows)  # number of existing rows is our row number
        CurrentRowNumber = NumRows  # this row's number
        CurrentRow = []  # start with a blank row and build up
        # -------------------------  Add the elements to a row  ------------------------- #
        for i, element in enumerate(args):  # Loop through list of elements and add them to the row
            if type(element) == list:
                PopupError('Error creating Window layout',
                           'Layout has a LIST instead of an ELEMENT',
                           'This means you have a badly placed ]',
                           'The offensive list is:',
                           element,
                           'This list will be stripped from your layout' , keep_on_top=True
                           )
                continue
            elif callable(element) and not isinstance(element, Element):
                PopupError('Error creating Window layout',
                           'Layout has a FUNCTION instead of an ELEMENT',
                           'This likely means you are missing () from your layout',
                           'The offensive list is:',
                           element,
                           'This item will be stripped from your layout', keep_on_top=True)
                continue
            if element.ParentContainer is not None:
                warnings.warn('*** YOU ARE ATTEMPTING TO RESUSE AN ELEMENT IN YOUR LAYOUT! Once placed in a layout, an element cannot be used in another layout. ***', UserWarning)
                PopupError('Error creating Window layout',
                           'The layout specified has already been used',
                           'You MUST start witha "clean", unused layout every time you create a window',
                           'The offensive Element = ',
                           element,
                           'and has a key = ', element.Key,
                           'This item will be stripped from your layout',
                           'Hint - try printing your layout and matching the IDs "print(layout)"', keep_on_top=True)
                continue
            element.Position = (CurrentRowNumber, i)
            element.ParentContainer = self
            CurrentRow.append(element)
        # -------------------------  Append the row to list of Rows  ------------------------- #
        self.Rows.append(CurrentRow)

    # ------------------------- Add Multiple Rows to Form ------------------------- #
    def AddRows(self, rows):
        """
        Loops through a list of lists of elements and adds each row, list, to the layout.
        This is NOT the best way to go about creating a window.  Sending the entire layout at one time and passing
        it as a parameter to the Window call is better.

        :param rows: List[List[Elements]] A list of a list of elements

        """
        for row in rows:
            try:
                iter(row)
            except TypeError:
                PopupError('Error creating Window layout',
                           'Your row is not an iterable (e.g. a list)',
                           'Instead of a list, the type found was {}'.format(type(row)),
                           'The offensive row = ',
                           row,
                           'This item will be stripped from your layout', keep_on_top=True)
                continue
            self.AddRow(*row)

    def Layout(self, rows):
        """
        Second of two preferred ways of telling a Window what its layout is. The other way is to pass the layout as
        a parameter to Window object.  The parameter method is the currently preferred method. This call to Layout
        has been removed from examples contained in documents and in the Demo Programs. Trying to remove this call
        from history and replace with sending as a parameter to Window.

        :param rows: Your entire layout
        :type rows: List[List[Elements]]
        :return: self so that you can chain method calls
        :rtype: (Window)
        """
        self.AddRows(rows)
        self._BuildKeyDict()
        return self


    def extend_layout(self, container,  rows):
        """
        Adds new rows to an existing container element inside of this window

        :param container: (Union[Frame, Column, Tab]) - The container Element the layout will be placed inside of
        :type container: (Union[Frame, Column, Tab])
        :param rows: (List[List[Element]]) - The layout to be added
        :type rows: (List[List[Element]])
        :return: (Window) self so could be chained
        :rtype: (Window)
        """
        column = Column(rows, pad=(0,0))
        if self == container:
            frame = self.TKroot
        else:
            frame = container.Widget
        PackFormIntoFrame(column, frame, self)
        # sg.PackFormIntoFrame(col, window.TKroot, window)
        self.AddRow(column)
        self.AllKeysDict = self._BuildKeyDictForWindow(self, column, self.AllKeysDict)
        return self

    def LayoutAndRead(self, rows, non_blocking=False):
        """
        Deprecated!!  Now your layout your window's rows (layout) and then separately call Read.

        :param rows:  The layout of the window
        :type rows: List[List[Element]]
        :param non_blocking:  if True the Read call will not block
        :type non_blocking: (bool)
        """
        raise DeprecationWarning(
            'LayoutAndRead is no longer supported... change your call window.Layout(layout).Read()\nor window(title, layout).Read()')
        # self.AddRows(rows)
        # self._Show(non_blocking=non_blocking)
        # return self.ReturnValues

    def LayoutAndShow(self, rows):
        """
        Deprecated - do not use any longer.  Layout your window and then call Read.  Or can add a Finalize call before the Read
        """
        raise DeprecationWarning('LayoutAndShow is no longer supported... ')

    def _Show(self, non_blocking=False):
        """
        NOT TO BE CALLED BY USERS.  INTERNAL ONLY!
        It's this method that first shows the window to the user, collects results

        :param non_blocking: (bool) if True, this is a non-blocking call
        :return: Tuple[Any, Dict] The event, values turple that is returned from Read calls
        """
        self.Shown = True
        # Compute num rows & num cols (it'll come in handy debugging)
        self.NumRows = len(self.Rows)
        self.NumCols = max(len(row) for row in self.Rows)
        self.NonBlocking = non_blocking

        # Search through entire form to see if any elements set the focus
        # if not, then will set the focus to the first input element
        found_focus = False
        for row in self.Rows:
            for element in row:
                try:
                    if element.Focus:
                        found_focus = True
                except:
                    pass
                try:
                    if element.Key is not None:
                        self.UseDictionary = True
                except:
                    pass

        if not found_focus and self.UseDefaultFocus:
            self.UseDefaultFocus = True
        else:
            self.UseDefaultFocus = False
        # -=-=-=-=-=-=-=-=- RUN the GUI -=-=-=-=-=-=-=-=- ##
        StartupTK(self)
        # If a button or keyboard event happened but no results have been built, build the results
        if self.LastKeyboardEvent is not None or self.LastButtonClicked is not None:
            return _BuildResults(self, False, self)
        return self.ReturnValues

    # ------------------------- SetIcon - set the window's fav icon ------------------------- #
    def SetIcon(self, icon=None, pngbase64=None):
        """
        Changes the icon that is shown on the title bar and on the task bar.
        NOTE - The file type is IMPORTANT and depends on the OS!
        Can pass in:
        * filename which must be a .ICO icon file for windows, PNG file for Linux
        * bytes object
        * BASE64 encoded file held in a variable

        :param icon: Filename or bytes object
        :type icon: (str)
        :param pngbase64: Base64 encoded image
        :type pngbase64: (str)
        """
        if type(icon) is bytes or pngbase64 is not None:
            wicon = tkinter.PhotoImage(data=icon if icon is not None else pngbase64)
            try:
                self.TKroot.tk.call('wm', 'iconphoto', self.TKroot._w, wicon)
            except:
                wicon = tkinter.PhotoImage(data=DEFAULT_BASE64_ICON)
                try:
                    self.TKroot.tk.call('wm', 'iconphoto', self.TKroot._w, wicon)
                except:
                    pass
            self.WindowIcon = wicon
            return

        wicon = icon
        try:
            self.TKroot.iconbitmap(icon)
        except:
            try:
                wicon = tkinter.PhotoImage(file=icon)
                self.TKroot.tk.call('wm', 'iconphoto', self.TKroot._w, wicon)
            except:
                try:
                    wicon = tkinter.PhotoImage(data=DEFAULT_BASE64_ICON)
                    try:
                        self.TKroot.tk.call('wm', 'iconphoto', self.TKroot._w, wicon)
                    except:
                        pass
                except:
                    pass
        self.WindowIcon = wicon

    def _GetElementAtLocation(self, location):
        """
        Given a (row, col) location in a layout, return the element located at that position

        :param location: Tuple[int, int] Return the element located at (row, col) in layout
        :return:  (Element) The Element located at that position in this window
        """

        (row_num, col_num) = location
        row = self.Rows[row_num]
        element = row[col_num]
        return element

    def _GetDefaultElementSize(self):
        """
        Returns the default elementSize

        :return:  (width, height) of the default element size
        :rtype: Tuple[int, int]
        """

        return self.DefaultElementSize

    def _AutoCloseAlarmCallback(self):
        """
        Function that's called by tkinter when autoclode timer expires.  Closes the window

        """
        try:
            window = self
            if window:
                if window.NonBlocking:
                    self.CloseNonBlockingForm()
                else:
                    window._Close()
                    self.TKroot.quit()
                    self.RootNeedsDestroying = True
        except:
            pass

    def _TimeoutAlarmCallback(self):
        """
        Read Timeout Alarm callback. Will kick a mainloop call out of the tkinter event loop and cause it to return
        """
        # first, get the results table built
        # modify the Results table in the parent FlexForm object
        # print('TIMEOUT CALLBACK')
        if self.TimerCancelled:
            # print('** timer was cancelled **')
            return
        self.LastButtonClicked = self.TimeoutKey
        self.FormRemainedOpen = True
        self.TKroot.quit()  # kick the users out of the mainloop

    # @_timeit_summary
    def Read(self, timeout=None, timeout_key=TIMEOUT_KEY, close=False):
        # type: (int, Any, bool) -> Tuple[Any, Union[Dict, List]]
        """
        THE biggest deal method in the Window class! This is how you get all of your data from your Window.
            Pass in a timeout (in milliseconds) to wait for a maximum of timeout milliseconds. Will return timeout_key
            if no other GUI events happen first.

        :param timeout: Milliseconds to wait until the Read will return IF no other GUI events happen first
        :type timeout: (int)
        :param timeout_key: The value that will be returned from the call if the timer expired
        :type timeout_key: (Any)
        :param close: if True the window will be closed prior to returning
        :type close: (bool)
        :return:  (event, values)
        :rtype: Tuple[(Any), Union[Dict[Any:Any]], List[Any], None]
        """
        # ensure called only 1 time through a single read cycle
        if not Window._read_call_from_debugger:
            _refresh_debugger()
        results = self._read(timeout=timeout, timeout_key=timeout_key)
        if close:
            self.close()

        return results


    # @_timeit
    def _read(self, timeout=None, timeout_key=TIMEOUT_KEY):
        # type: (int, Any) -> Tuple[Any, Union[Dict, List]]
        """
        THE biggest deal method in the Window class! This is how you get all of your data from your Window.
            Pass in a timeout (in milliseconds) to wait for a maximum of timeout milliseconds. Will return timeout_key
            if no other GUI events happen first.

        :param timeout: Milliseconds to wait until the Read will return IF no other GUI events happen first
        :type timeout: (int)
        :param timeout_key: The value that will be returned from the call if the timer expired
        :type timeout_key: (Any)
        :return: (event, values) (event or timeout_key or None, Dictionary of values or List of values from all elements in the Window)
        :rtype: Tuple[(Any), Union[Dict[Any:Any]], List[Any], None]
        """

        timeout = int(timeout) if timeout is not None else None
        if timeout == 0:  # timeout of zero runs the old readnonblocking
            event, values = self._ReadNonBlocking()
            if event is None:
                event = timeout_key
            if values is None:
                event = None
            return event, values  # make event None if values was None and return
        # Read with a timeout
        self.Timeout = timeout
        self.TimeoutKey = timeout_key
        self.NonBlocking = False
        if self.TKrootDestroyed:
            return None, None
        if not self.Shown:
            self._Show()
        else:
            # if already have a button waiting, the return previously built results
            if self.LastButtonClicked is not None and not self.LastButtonClickedWasRealtime:
                # print(f'*** Found previous clicked saved {self.LastButtonClicked}')
                results = _BuildResults(self, False, self)
                self.LastButtonClicked = None
                return results
            InitializeResults(self)
            # if the last button clicked was realtime, emulate a read non-blocking
            # the idea is to quickly return realtime buttons without any blocks until released
            if self.LastButtonClickedWasRealtime:
                self.LastButtonClickedWasRealtime = False  # stops from generating events until something changes

                # print(f'RTime down {self.LastButtonClicked}' )
                try:
                    rc = self.TKroot.update()
                except:
                    self.TKrootDestroyed = True
                    Window._DecrementOpenCount()
                    # _my_windows.Decrement()
                    # print('ROOT Destroyed')
                results = _BuildResults(self, False, self)
                if results[0] != None and results[0] != timeout_key:
                    return results
                else:
                    pass

                # else:
                #     print("** REALTIME PROBLEM FOUND **", results)

            if self.RootNeedsDestroying:
                # print('*** DESTROYING really late***')
                try:
                    self.TKroot.destroy()
                except:
                    pass
                # _my_windows.Decrement()
                self.LastButtonClicked = None
                return None, None

            # normal read blocking code....
            if timeout != None:
                self.TimerCancelled = False
                self.TKAfterID = self.TKroot.after(timeout, self._TimeoutAlarmCallback)
            self.CurrentlyRunningMainloop = True
            # print(f'In main {self.Title} {self.TKroot}')
            # self.TKroot.protocol("WM_DESTROY_WINDOW", self._OnClosingCallback)
            # self.TKroot.protocol("WM_DELETE_WINDOW", self._OnClosingCallback)
            self.TKroot.mainloop()
            # print('Out main')
            self.CurrentlyRunningMainloop = False
            # if self.LastButtonClicked != TIMEOUT_KEY:
            #     print(f'Window {self.Title} Last button clicked = {self.LastButtonClicked}')
            try:
                self.TKroot.after_cancel(self.TKAfterID)
                del self.TKAfterID
            except:
                pass
                # print('** tkafter cancel failed **')
            self.TimerCancelled = True
            if self.RootNeedsDestroying:
                # print('*** DESTROYING LATE ***')
                try:
                    self.TKroot.destroy()
                except:
                    pass
                Window._DecrementOpenCount()
                # _my_windows.Decrement()
                self.LastButtonClicked = None
                return None, None
            # if form was closed with X
            if self.LastButtonClicked is None and self.LastKeyboardEvent is None and self.ReturnValues[0] is None:
                Window._DecrementOpenCount()
                # _my_windows.Decrement()
        # Determine return values
        if self.LastKeyboardEvent is not None or self.LastButtonClicked is not None:
            results = _BuildResults(self, False, self)
            if not self.LastButtonClickedWasRealtime:
                self.LastButtonClicked = None
            return results
        else:
            if not self.XFound and self.Timeout != 0 and self.Timeout is not None and self.ReturnValues[
                0] is None:  # Special Qt case because returning for no reason so fake timeout
                self.ReturnValues = self.TimeoutKey, self.ReturnValues[1]  # fake a timeout
            elif not self.XFound and self.ReturnValues[0] is None:  # TODO HIGHLY EXPERIMENTAL... added due to tray icon interaction
                # print("*** Faking timeout ***")
                self.ReturnValues = self.TimeoutKey, self.ReturnValues[1]  # fake a timeout
            return self.ReturnValues

    def _ReadNonBlocking(self):
        """
        Should be NEVER called directly by the user.  The user can call Window.Read(timeout=0) to get same effect

        :return: Tuple[(Any), Union[Dict[Any:Any], List[Any], None] (event, values)
                 (event or timeout_key or None, Dictionary of values or List of values from all elements in the Window
        """
        if self.TKrootDestroyed:
            try:
                self.TKroot.quit()
                self.TKroot.destroy()
            except:
                pass
                # print('DESTROY FAILED')
            return None, None
        if not self.Shown:
            self._Show(non_blocking=True)
        try:
            rc = self.TKroot.update()
        except:
            self.TKrootDestroyed = True
            Window._DecrementOpenCount()
            # _my_windows.Decrement()
            # print("read failed")
            # return None, None
        if self.RootNeedsDestroying:
            # print('*** DESTROYING LATE ***', self.ReturnValues)
            self.TKroot.destroy()
            Window._DecrementOpenCount()
            # _my_windows.Decrement()
            self.Values = None
            self.LastButtonClicked = None
            return None, None
        return _BuildResults(self, False, self)

    def Finalize(self):
        """
        Use this method to cause your layout to built into a real tkinter window.  In reality this method is like
        Read(timeout=0).  It doesn't block and uses your layout to create tkinter widgets to represent the elements.
        Lots of action!

        :return:  Returns 'self' so that method "Chaining" can happen (read up about it as it's very cool!)
        :rtype: (Window)
        """

        if self.TKrootDestroyed:
            return self
        self.Read(timeout=1)
        return self
        # OLD CODE FOLLOWS
        if not self.Shown:
            self._Show(non_blocking=True)
        try:
            rc = self.TKroot.update()
        except:
            self.TKrootDestroyed = True
            Window._DecrementOpenCount()
            print('** Finalize failed **')
            # _my_windows.Decrement()
            # return None, None
        return self

    def Refresh(self):
        """
        Refreshes the window by calling tkroot.update().  Can sometimes get away with a refresh instead of a Read.
        Use this call when you want something to appear in your Window immediately (as soon as this function is called).
        Without this call your changes to a Window will not be visible to the user until the next Read call

        :return: `self` so that method calls can be easily "chained"
        :rtype: (Window)
        """

        if self.TKrootDestroyed:
            return self
        try:
            rc = self.TKroot.update()
        except:
            pass
        return self

    def Fill(self, values_dict):
        """
        Fill in elements that are input fields with data based on a 'values dictionary'

        :param values_dict: {Element key : value} pairs
        :type values_dict: (Dict[Any:Any])
        :return: returns self so can be chained with other methods
        :rtype: (Window)
        """

        FillFormWithValues(self, values_dict)
        return self

    def FindElement(self, key, silent_on_error=False):
        """
        Find element object associated with the provided key.
        THIS METHOD IS NO LONGER NEEDED to be called by the user

        You can perform the same operation by writing this statement:
        element = window[key]

        You can drop the entire "FindElement" function name and use [ ] instead.

        Typically used in combination with a call to element's Update method (or any other element method!):
        window[key].Update(new_value)

        Versus the "old way"
        window.FindElement(key).Update(new_value)

        This call can be abbreviated to any of these:
        FindElement == Element == Find
        Rememeber that this call will return None if no match is found which may cause your code to crash if not
        checked for.

        :param key: Used with window.FindElement and with return values to uniquely identify this element
        :type key: (Any)
        :param silent_on_error: If True do not display popup nor print warning of key errors
        :type silent_on_error: (bool)
        :return:  Return value can be: the Element that matches the supplied key if found; an Error Element if silent_on_error is False; None if silent_on_error True;
        :rtype: Union[Element, Error Element, None]
        """
        try:
            element = self.AllKeysDict[key]
        except KeyError:
            element = None
            if not silent_on_error:
                warnings.warn(
                    "*** WARNING = FindElement did not find the key. Please check your key's spelling. key = %s ***" % key, UserWarning)
                PopupError('Key error in FindElement Call',
                           'Bad key = {}'.format(key),
                           'Your bad line of code may resemble this:',
                           'window.FindElement("{}")'.format(key),
                           'or window["{}"]'.format(key), keep_on_top=True
                           )
                element = ErrorElement(key=key)
        return element

    Element = FindElement  # Shortcut function
    Find = FindElement  # Shortcut function, most likely not used by many people.
    Elem = FindElement  # NEW for 2019!  More laziness... Another shortcut

    def FindElementWithFocus(self):
        """
        Returns the Element that currently has focus as reported by tkinter. If no element is found None is returned!
        :return: An Element if one has been found with focus or None if no element found
        :rtype: Union[Element, None]
        """
        element = _FindElementWithFocusInSubForm(self)
        return element

    def _BuildKeyDict(self):
        """
        Used internally only! Not user callable
        Builds a dictionary containing all elements with keys for this window.
        """
        dict = {}
        self.AllKeysDict = self._BuildKeyDictForWindow(self, self, dict)
        # print(f'keys built = {self.AllKeysDict}')

    def _BuildKeyDictForWindow(self, top_window, window, key_dict):
        """
        Loop through all Rows and all Container Elements for this window and create the keys for all of them.
        Note that the calls are recursive as all pathes must be walked

        :param top_window: (Window) The highest level of the window
        :param window: Union[Column, Frame, TabGroup, Pane, Tab] The "sub-window" (container element) to be searched
        :param key_dict: The dictionary as it currently stands.... used as part of recursive call
        :return: (dict) Dictionary filled with all keys in the window
        """
        for row_num, row in enumerate(window.Rows):
            for col_num, element in enumerate(row):
                if element.Type == ELEM_TYPE_COLUMN:
                    key_dict = self._BuildKeyDictForWindow(top_window, element, key_dict)
                if element.Type == ELEM_TYPE_FRAME:
                    key_dict = self._BuildKeyDictForWindow(top_window, element, key_dict)
                if element.Type == ELEM_TYPE_TAB_GROUP:
                    key_dict = self._BuildKeyDictForWindow(top_window, element, key_dict)
                if element.Type == ELEM_TYPE_PANE:
                    key_dict = self._BuildKeyDictForWindow(top_window, element, key_dict)
                if element.Type == ELEM_TYPE_TAB:
                    key_dict = self._BuildKeyDictForWindow(top_window, element, key_dict)
                if element.Key is None:  # if no key has been assigned.... create one for input elements
                    if element.Type == ELEM_TYPE_BUTTON:
                        element.Key = element.ButtonText
                    elif element.Type == ELEM_TYPE_TAB:
                        element.Key = element.Title
                    if element.Type in (ELEM_TYPE_MENUBAR, ELEM_TYPE_BUTTONMENU, ELEM_TYPE_CANVAS,
                                        ELEM_TYPE_INPUT_SLIDER, ELEM_TYPE_GRAPH, ELEM_TYPE_IMAGE,
                                        ELEM_TYPE_INPUT_CHECKBOX, ELEM_TYPE_INPUT_LISTBOX, ELEM_TYPE_INPUT_COMBO,
                                        ELEM_TYPE_INPUT_MULTILINE, ELEM_TYPE_INPUT_OPTION_MENU, ELEM_TYPE_INPUT_SPIN,
                                        ELEM_TYPE_INPUT_RADIO, ELEM_TYPE_INPUT_TEXT, ELEM_TYPE_PROGRESS_BAR,
                                        ELEM_TYPE_TAB_GROUP):
                        element.Key = top_window.DictionaryKeyCounter
                        top_window.DictionaryKeyCounter += 1
                if element.Key is not None:
                    if element.Key in key_dict.keys():
                        print('*** Duplicate key found in your layout {} ***'.format(
                            element.Key)) if element.Type != ELEM_TYPE_BUTTON else None
                        element.Key = str(element.Key) + str(self.UniqueKeyCounter)
                        self.UniqueKeyCounter += 1
                        print('*** Replaced new key with {} ***'.format(
                            element.Key)) if element.Type != ELEM_TYPE_BUTTON else None
                    key_dict[element.Key] = element
        return key_dict


    def element_list(self):
        """
        Returns a list of all elements in the window

        :return:  List of all elements in the window and container elements in the window
        :rtype: List[Element]
        """
        return self._build_element_list()


    def _build_element_list(self):
        """
        Used internally only! Not user callable
        Builds a dictionary containing all elements with keys for this window.
        """
        elem_list = []
        elem_list = self._build_element_list_for_form(self, self, elem_list)
        return elem_list

    def _build_element_list_for_form(self, top_window, window, elem_list):
        """
        Loop through all Rows and all Container Elements for this window and create a list
        Note that the calls are recursive as all pathes must be walked

        :param top_window: The highest level of the window
        :type top_window: (Window)
        :param window: The "sub-window" (container element) to be searched
        :type window: Union[Column, Frame, TabGroup, Pane, Tab]
        :param elem_list: The element list as it currently stands.... used as part of recursive call
        :type elem_list: ???
        :return:  List of all elements in this sub-window
        :rtype: List[Element]
        """
        for row_num, row in enumerate(window.Rows):
            for col_num, element in enumerate(row):
                elem_list.append(element)
                if element.Type in (ELEM_TYPE_COLUMN, ELEM_TYPE_FRAME, ELEM_TYPE_TAB_GROUP, ELEM_TYPE_PANE, ELEM_TYPE_TAB):
                    elem_list = self._build_element_list_for_form(top_window, element, elem_list)
        return elem_list



    def SaveToDisk(self, filename):
        """
        Saves the values contained in each of the input areas of the form. Basically saves what would be returned
        from a call to Read.  It takes these results and saves them to disk using pickle

        :param filename: Filename to save the values to in pickled form
        :type filename: (str)
        """
        try:
            event, values = _BuildResults(self, False, self)
            remove_these = []
            for key in values:
                if self.Element(key).Type == ELEM_TYPE_BUTTON:
                    remove_these.append(key)
            for key in remove_these:
                del values[key]
            with open(filename, 'wb') as sf:
                pickle.dump(values, sf)
        except:
            print('*** Error saving Window contents to disk ***')

    def LoadFromDisk(self, filename):
        """
        Restore values from a previous call to SaveToDisk which saves the returned values dictionary in Pickle format

        :param filename: Pickle Filename to load
        :type filename: (str)
        """
        try:
            with open(filename, 'rb') as df:
                self.Fill(pickle.load(df))
        except:
            print('*** Error loading form to disk ***')

    def GetScreenDimensions(self):
        """
        Get the screen dimensions.  NOTE - you must have a window already open for this to work (blame tkinter not me)

        :return: Tuple containing width and height of screen in pixels
        :rtype: Union[Tuple[None, None], Tuple[width, height]]
        """
        if self.TKrootDestroyed:
            return Window.get_screen_size()
        screen_width = self.TKroot.winfo_screenwidth()  # get window info to move to middle of screen
        screen_height = self.TKroot.winfo_screenheight()
        return screen_width, screen_height

    def Move(self, x, y):
        """
        Move the upper left corner of this window to the x,y coordinates provided
        :param x: x coordinate in pixels
        :type x: (int)
        :param y: y coordinate in pixels
        :type y: (int)
        """
        try:
            self.TKroot.geometry("+%s+%s" % (x, y))
        except:
            pass

    def Minimize(self):
        """
        Minimize this window to the task bar
        """
        self.TKroot.iconify()

    def Maximize(self):
        """
        Maximize the window. This is done differently on a windows system versus a linux or mac one.  For non-Windows
        the root attribute '-fullscreen' is set to True.  For Windows the "root" state is changed to "zoomed"
        The reason for the difference is the title bar is removed in some cases when using fullscreen option
        """
        if sys.platform != 'linux':
            self.TKroot.state('zoomed')
        else:
            self.TKroot.attributes('-fullscreen', True)
        # this method removes the titlebar too
        # self.TKroot.attributes('-fullscreen', True)

    def Normal(self):
        """
        Restore a window to a non-maximized state.  Does different things depending on platform.  See Maximize for more.
        """
        if self.TKroot.state() == 'iconic':
            self.TKroot.deiconify()
        else:
            if sys.platform != 'linux':
                self.TKroot.state('normal')
            else:
                self.TKroot.attributes('-fullscreen', False)

    def _StartMove(self, event):
        """
        Used by "Grab Anywhere" style windows. This function is bound to mouse-down. It marks the beginning of a drag.
        :param event: event information passed in by tkinter. Contains x,y position of mouse
        :type event: (event)
        """
        try:
            self.TKroot.x = event.x
            self.TKroot.y = event.y
        except:
            pass
        # print('Start move {},{}'.format(event.x,event.y))

    def _StopMove(self, event):
        """
        Used by "Grab Anywhere" style windows. This function is bound to mouse-up. It marks the ending of a drag.
        Sets the position of the window to this final x,y coordinates
        :param event: event information passed in by tkinter. Contains x,y position of mouse
        :type event: (event)
        """
        try:
            self.TKroot.x = None
            self.TKroot.y = None
        except:
            pass
        # print('-Stop- move {},{}'.format(event.x,event.y))

    def _OnMotion(self, event):
        """
        Used by "Grab Anywhere" style windows. This function is bound to mouse motion. It actually moves the window
        :param event: event information passed in by tkinter. Contains x,y position of mouse
        :type event: (event)
        """
        try:
            deltax = event.x - self.TKroot.x
            deltay = event.y - self.TKroot.y
            x = self.TKroot.winfo_x() + deltax
            y = self.TKroot.winfo_y() + deltay
            self.TKroot.geometry("+%s+%s" % (x, y))  # this is what really moves the window
            # print('{},{}'.format(x,y))
        except:
            pass

    def _KeyboardCallback(self, event):
        """
        Window keyboard callback. Called by tkinter.  Will kick user out of the tkinter event loop. Should only be
        called if user has requested window level keyboard events

        :param event: object provided by tkinter that contains the key information
        :type event: (event)
        """
        self.LastButtonClicked = None
        self.FormRemainedOpen = True
        if event.char != '':
            self.LastKeyboardEvent = event.char
        else:
            self.LastKeyboardEvent = str(event.keysym) + ':' + str(event.keycode)
        if not self.NonBlocking:
            _BuildResults(self, False, self)
        if self.CurrentlyRunningMainloop:  # quit if this is the current mainloop, otherwise don't quit!
            self.TKroot.quit()

    def _MouseWheelCallback(self, event):
        """
        Called by tkinter when a mouse wheel event has happened. Only called if keyboard events for the window
        have been enabled

        :param event: object sent in by tkinter that has the wheel direction
        :type event: (event)
        """
        self.LastButtonClicked = None
        self.FormRemainedOpen = True
        self.LastKeyboardEvent = 'MouseWheel:Down' if event.delta < 0 else 'MouseWheel:Up'
        if not self.NonBlocking:
            _BuildResults(self, False, self)
        if self.CurrentlyRunningMainloop:  # quit if this is the current mainloop, otherwise don't quit!
            self.TKroot.quit()

    def _Close(self):
        """
        The internal close call that does the real work of building. This method basically sets up for closing
        but doesn't destroy the window like the User's version of Close does
        """
        try:
            self.TKroot.update()
        except:
            pass
        if not self.NonBlocking:
            _BuildResults(self, False, self)
        if self.TKrootDestroyed:
            return
        self.TKrootDestroyed = True
        self.RootNeedsDestroying = True
        return

    def Close(self):
        """
        Closes window.  Users can safely call even if window has been destroyed.   Should always call when done with
        a window so that resources are properly freed up within your thread.
        """
        try:
            self.TKroot.update()    # On Linux must call update if the user closed with X or else won't actually close the window
        except:
            pass
        if self.TKrootDestroyed:
            return
        try:
            self.TKroot.destroy()
            Window._DecrementOpenCount()
        except:
            pass
        # if down to 1 window, try and destroy the hidden window, if there is one
        if Window.NumOpenWindows == 1:
            try:
                Window.hidden_master_root.destroy()
                Window.NumOpenWindows = 0  # if no hidden window, then this won't execute
            except:
                pass
        self.TKrootDestroyed = True
        del self.TKroot
        del self.Rows

    # IT FINALLY WORKED! 29-Oct-2018 was the first time this damned thing got called
    def _OnClosingCallback(self):
        """
        Internally used method ONLY. Not sure callable.  tkinter calls this when the window is closed by clicking X
        """
        # global _my_windows
        # print('Got closing callback', self.DisableClose)
        if self.DisableClose:
            return
        self.XFound = True
        if self.CurrentlyRunningMainloop:  # quit if this is the current mainloop, otherwise don't quit!
            self.TKroot.quit()  # kick the users out of the mainloop
            self.TKroot.destroy()  # kick the users out of the mainloop
            self.RootNeedsDestroying = True
            self.TKrootDestroyed = True
        else:
            self.TKroot.destroy()  # kick the users out of the mainloop
            self.RootNeedsDestroying = True
        self.RootNeedsDestroying = True

    def Disable(self):
        """
        Disables window from taking any input from the user
        """
        self.TKroot.attributes('-disabled', 1)
        # self.TKroot.grab_set_global()

    def Enable(self):
        """
        Re-enables window to take user input after having it be Disabled previously
        """
        self.TKroot.attributes('-disabled', 0)
        # self.TKroot.grab_release()

    def Hide(self):
        """
        Hides the window from the screen and the task bar
        """
        self._Hidden = True
        self.TKroot.withdraw()

    def UnHide(self):
        """
        Used to bring back a window that was previously hidden using the Hide method
        """
        if self._Hidden:
            self.TKroot.deiconify()
            self._Hidden = False

    def Disappear(self):
        """
        Causes a window to "disappear" from the screen, but remain on the taskbar. It does this by turning the alpha
        channel to 0.  NOTE that on some platforms alpha is not supported. The window will remain showing on these
        platforms.  The Raspberry Pi for example does not have an alpha setting
        """
        self.TKroot.attributes('-alpha', 0)

    def Reappear(self):
        """
        Causes a window previously made to "Disappear" (using that method). Does this by restoring the alpha channel
        """
        self.TKroot.attributes('-alpha', 255)

    def SetAlpha(self, alpha):
        """
        Sets the Alpha Channel for a window.  Values are between 0 and 1 where 0 is completely transparent

        :param alpha: 0 to 1. 0 is completely transparent.  1 is completely visible and solid (can't see through)
        :type alpha: (float)
        """
        # Change the window's transparency
        # :param alpha: From 0 to 1 with 0 being completely transparent
        self._AlphaChannel = alpha
        self.TKroot.attributes('-alpha', alpha)

    @property
    def AlphaChannel(self):
        """
        A property that changes the current alpha channel value (internal value)
        :return: (float) the current alpha channel setting according to self, not read directly from tkinter
        """
        return self._AlphaChannel

    @AlphaChannel.setter
    def AlphaChannel(self, alpha):
        """
        The setter method for this "property".
        Planning on depricating so that a Set call is always used by users. This is more in line with the SDK
        :param alpha: 0 to 1. 0 is completely transparent.  1 is completely visible and solid (can't see through)
        :type alpha: (float)
        """
        self._AlphaChannel = alpha
        self.TKroot.attributes('-alpha', alpha)

    def BringToFront(self):
        """
        Brings this window to the top of all other windows (perhaps may not be brought before a window made to "stay
        on top")
        """
        if sys.platform.startswith('win'):
            try:
                self.TKroot.wm_attributes("-topmost", 0)
                self.TKroot.wm_attributes("-topmost", 1)
                if not self.KeepOnTop:
                    self.TKroot.wm_attributes("-topmost", 0)
            except:
                pass
        else:
            try:
                self.TKroot.lift()
            except:
                pass

    def SendToBack(self):
        """
        Pushes this window to the bottom of the stack of windows. It is the opposite of BringToFront
        """
        try:
            self.TKroot.lower()
        except:
            pass

    def CurrentLocation(self):
        """
        Get the current location of the window's top left corner

        :return: The x and y location in tuple form (x,y)
        :rtype: Tuple[(int), (int)]
        """
        return int(self.TKroot.winfo_x()), int(self.TKroot.winfo_y())

    @property
    def Size(self):
        """
        Return the current size of the window in pixels

        :return: (width, height) of the window
        :rtype: Tuple[(int), (int)]
        """
        win_width = self.TKroot.winfo_width()
        win_height = self.TKroot.winfo_height()
        return win_width, win_height

    @Size.setter
    def Size(self, size):
        """
        Changes the size of the window, if possible

        :param size: (width, height) of the desired window size
        :type size: Tuple[int, int]
        """
        try:
            self.TKroot.geometry("%sx%s" % (size[0], size[1]))
            self.TKroot.update_idletasks()
        except:
            pass

    def VisibilityChanged(self):
        """
        Not used in tkinter, but supplied becuase it is used in Qt. Want to remain source code compatible so that if
        you are making this call in your PySimpleGUIQt code, you can switch to PySimpleGUI and it will not complain
        about a missing method.  Just know that in this version of PySimpleGUI, it does nothing
        """
        # A dummy function.  Needed in Qt but not tkinter
        return

    def SetTransparentColor(self, color):
        """
        Set the color that will be transparent in your window. Areas with this color will be SEE THROUGH.

        :param color: Color string that defines the transparent color
        :type color: (str)
        """
        try:
            self.TKroot.attributes('-transparentcolor', color)
        except:
            print('Transparent color not supported on this platform (windows only)')

    def GrabAnyWhereOn(self):
        """
        Turns on Grab Anywhere functionality AFTER a window has been created.  Don't try on a window that's not yet
        been Finalized or Read.
        """
        self.TKroot.bind("<ButtonPress-1>", self._StartMove)
        self.TKroot.bind("<ButtonRelease-1>", self._StopMove)
        self.TKroot.bind("<B1-Motion>", self._OnMotion)

    def GrabAnyWhereOff(self):
        """
        Turns off Grab Anywhere functionality AFTER a window has been created.  Don't try on a window that's not yet
        been Finalized or Read.
        """
        self.TKroot.unbind("<ButtonPress-1>")
        self.TKroot.unbind("<ButtonRelease-1>")
        self.TKroot.unbind("<B1-Motion>")

    def _user_bind_callback(self, bind_string, event):
        """
        Used when user binds a tkinter event directly to an element

        :param bind_string: The event that was bound so can lookup the key modifier
        :param event: Event data passed in by tkinter (not used)
        """

        key = self.user_bind_dict.get(bind_string, '')
        self.user_bind_event = event
        if key is not None:
            self.LastButtonClicked = key
        else:
            self.LastButtonClicked = bind_string
        self.FormRemainedOpen = True
        if self.CurrentlyRunningMainloop:
            self.TKroot.quit()

    def bind(self, bind_string, key):
        """
        Used to add tkinter events to a Window.
        The tkinter specific data is in the Window's member variable user_bind_event
        :param bind_string: The string tkinter expected in its bind function
        :type bind_string: (str)
        :param key: The event that will be generated when the tkinter event occurs
        :type key: Any
        """
        self.TKroot.bind(bind_string, lambda evt: self._user_bind_callback(bind_string, evt))
        self.user_bind_dict[bind_string] = key

    def _callback_main_debugger_window_create_keystroke(self, event):
        """
        Called when user presses the key that creates the main debugger window

        :param event: (event) not used. Passed in event info
        """
        _Debugger.debugger._build_main_debugger_window()

    def _callback_popout_window_create_keystroke(self, event):
        """
        Called when user presses the key that creates the floating debugger window

        :param event: (event) not used. Passed in event info
        """
        _Debugger.debugger._build_floating_window()

    def EnableDebugger(self):
        """
        Enables the internal debugger. By default, the debugger IS enabled
        """
        self.TKroot.bind('<Cancel>', self._callback_main_debugger_window_create_keystroke)
        self.TKroot.bind('<Pause>', self._callback_popout_window_create_keystroke)
        self.DebuggerEnabled = True

    def DisableDebugger(self):
        """
        Disable the internal debugger. By default the debugger is ENABLED
        """
        self.TKroot.unbind("<Cancel>")
        self.TKroot.unbind("<Pause>")
        self.DebuggerEnabled = False

    def VisibilityChanged(self):
        """
        This is a completely dummy method that does nothing. It is here so that PySimpleGUIQt programs can make this
        call and then have that same source run on plain PySimpleGUI.
        :return:
        """
        return

    # def __enter__(self):
    #     """
    #     WAS used with context managers which are no longer needed nor advised.  It is here for legacy support and
    #     am afraid of removing right now
    #     :return: (window)
    #     """
    #     return self

    def __getitem__(self, key):
        """
        Returns Element that matches the passed in key.
        This is "called" by writing code as thus:
        window['element key'].Update

        :param key: The key to find
        :type key: (Any)
        :return: The element found or None if no element was found
        :rtype: Union[Element, None]
        """
        try:
            return self.FindElement(key)
        except Exception as e:
            warnings.warn('The key you passed in is no good. Key = {}*'.format(key))
            return None

    def __call__(self, *args, **kwargs):
        """
        Call window.Read but without having to type it out.
        window() == window.Read()
        window(timeout=50) == window.Read(timeout=50)

        :return: The famous event, values that Read returns.
        :rtype: Tuple[Any, Dict[Any:Any]]
        """
        return self.Read(*args, **kwargs)

    add_row = AddRow
    add_rows = AddRows
    alpha_channel = AlphaChannel
    bring_to_front = BringToFront
    close = Close
    current_location = CurrentLocation
    disable = Disable
    disable_debugger = DisableDebugger
    disappear = Disappear
    elem = Elem
    element = Element
    enable = Enable
    enable_debugger = EnableDebugger
    fill = Fill
    finalize = Finalize
    find = Find
    find_element = FindElement
    find_element_with_focus = FindElementWithFocus
    get_screen_dimensions = GetScreenDimensions
    grab_any_where_off = GrabAnyWhereOff
    grab_any_where_on = GrabAnyWhereOn
    hide = Hide
    layout = Layout
    load_from_disk = LoadFromDisk
    maximize = Maximize
    minimize = Minimize
    move = Move
    normal = Normal
    read = Read
    reappear = Reappear
    refresh = Refresh
    save_to_disk = SaveToDisk
    send_to_back = SendToBack
    set_alpha = SetAlpha
    set_icon = SetIcon
    set_transparent_color = SetTransparentColor
    size = Size
    un_hide = UnHide
    visibility_changed = VisibilityChanged

    #
    # def __exit__(self, *a):
    #     """
    #     WAS used with context managers which are no longer needed nor advised.  It is here for legacy support and
    #     am afraid of removing right now
    #     :param *a: (?) Not sure what's passed in.
    #     :return: Always returns False which was needed for context manager to work
    #     """
    #     self.__del__()
    #     return False
    #
    # def __del__(self):
    #     # print('DELETING WINDOW')
    #     for row in self.Rows:
    #         for element in row:
    #             element.__del__()


# -------------------------------- PEP8-ify the Window Class USER Interfaces -------------------------------- #


FlexForm = Window
Window.CloseNonBlockingForm = Window.Close
Window.CloseNonBlocking = Window.Close


# ------------------------------------------------------------------------- #
#                       SystemTray - class for implementing a psyeudo tray  #
# ------------------------------------------------------------------------- #

# -------------------------------- System Tray Begins Here -------------------------------- #
# Feb 2020 - Just starting on this so code commented out for now. Basing on PySimpleGUIQt's implementation / call format


# -------------------------------------------------------------------
# fade in/out info and default window alpha
SYSTEM_TRAY_WIN_MARGINS = 160, 60        # from right edge of screen, from bottom of screen
SYSTEM_TRAY_MESSAGE_MAX_LINE_LENGTH = 50
# colors
SYSTEM_TRAY_MESSAGE_WIN_COLOR = "#282828"
SYSTEM_TRAY_MESSAGE_TEXT_COLOR = "#ffffff"

SYSTEM_TRAY_MESSAGE_DISPLAY_DURATION_IN_MILLISECONDS = 3000  # how long to display the window
SYSTEM_TRAY_MESSAGE_FADE_IN_DURATION = 1000  # how long to fade in / fade out the window

EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED = '__DOUBLE_CLICKED__'
EVENT_SYSTEM_TRAY_ICON_ACTIVATED = '__ACTIVATED__'
EVENT_SYSTEM_TRAY_MESSAGE_CLICKED = '__MESSAGE_CLICKED__'



# Base64 Images to use as icons in the window
_tray_icon_error = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADlAAAA5QGP5Zs8AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAIpQTFRF////20lt30Bg30pg4FJc409g4FBe4E9f4U9f4U9g4U9f4E9g31Bf4E9f4E9f4E9f4E9f4E9f4FFh4Vdm4lhn42Bv5GNx5W575nJ/6HqH6HyI6YCM6YGM6YGN6oaR8Kev9MPI9cbM9snO9s3R+Nfb+dzg+d/i++vt/O7v/fb3/vj5//z8//7+////KofnuQAAABF0Uk5TAAcIGBktSYSXmMHI2uPy8/XVqDFbAAAA8UlEQVQ4y4VT15LCMBBTQkgPYem9d9D//x4P2I7vILN68kj2WtsAhyDO8rKuyzyLA3wjSnvi0Eujf3KY9OUP+kno651CvlB0Gr1byQ9UXff+py5SmRhhIS0oPj4SaUUCAJHxP9+tLb/ezU0uEYDUsCc+l5/T8smTIVMgsPXZkvepiMj0Tm5txQLENu7gSF7HIuMreRxYNkbmHI0u5Hk4PJOXkSMz5I3nyY08HMjbpOFylF5WswdJPmYeVaL28968yNfGZ2r9gvqFalJNUy2UWmq1Wa7di/3Kxl3tF1671YHRR04dWn3s9cXRV09f3vb1fwPD7z9j1WgeRgAAAABJRU5ErkJggg=='
_tray_icon_success = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAEKAAABCgEWpLzLAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAHJQTFRF////ZsxmbbZJYL9gZrtVar9VZsJcbMRYaMZVasFYaL9XbMFbasRZaMFZacRXa8NYasFaasJaasFZasJaasNZasNYasJYasJZasJZasJZasJZasJZasJYasJZasJZasJZasJZasJaasJZasJZasJZasJZ2IAizQAAACV0Uk5TAAUHCA8YGRobHSwtPEJJUVtghJeYrbDByNjZ2tvj6vLz9fb3/CyrN0oAAADnSURBVDjLjZPbWoUgFIQnbNPBIgNKiwwo5v1fsQvMvUXI5oqPf4DFOgCrhLKjC8GNVgnsJY3nKm9kgTsduVHU3SU/TdxpOp15P7OiuV/PVzk5L3d0ExuachyaTWkAkLFtiBKAqZHPh/yuAYSv8R7XE0l6AVXnwBNJUsE2+GMOzWL8k3OEW7a/q5wOIS9e7t5qnGExvF5Bvlc4w/LEM4Abt+d0S5BpAHD7seMcf7+ZHfclp10TlYZc2y2nOqc6OwruxUWx0rDjNJtyp6HkUW4bJn0VWdf/a7nDpj1u++PBOR694+Ftj/8PKNdnDLn/V8YAAAAASUVORK5CYII='
_tray_icon_halt = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAANswNuMPDO8HBO8FCe0HCu4IBu4IB+oLDeoLDu8JC+wKCu4JDO4LDOwKEe4OEO4OEeUQDewQDe0QDucVEuYcG+ccHOsQFuwWHe4fH/EGAvMEBfMFBvAHBPMGBfEGBvYCAfYDAvcDA/cDBPcDBfUDBvYEAPYEAfYEAvYEA/QGAPQGAfQGAvYEBPUEBvYFB/QGBPQGBfQHB/EFCvIHCPMHCfIHC/IFDfMHDPQGCPQGCfQGCvEIBPIIBfAIB/UIB/QICPYICfoBAPoBAfoBAvsBA/kCAPkCAfkCAvkCA/oBBPkCBPkCBfkCBvgCB/gEAPkEAfgEAvkEA/gGAfkGAvkEBPgEBfkEBv0AAP0AAfwAAvwAA/wCAPwCAfwCAvwCA/wABP0ABfwCBfwEAPwFA/ASD/ESFPAUEvAUE/EXFvAdH+kbIOobIeofIfEfIOcmKOohIukgJOggJesiKuwiKewoLe0tLO0oMOQ3OO43Oew4OfAhIPAhIfAiIPEiI+dDRe9ES+lQTOdSWupSUOhTUehSV+hUVu1QUO1RUe1SV+tTWe5SWOxXWOpYV+pZWelYXexaW+xaXO9aX+lZYeNhYOxjZ+lna+psbOttbehsbupscepucuxtcuxucep3fet7e+p/ffB6gOmKiu2Iie2Sk+2Qle2QluySlOyTleuYmvKFivCOjgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIxGNZsAAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAAA7DAAAOwwHHb6hkAAACVElEQVQ4T22S93PTMBhADQdl791SSsuRARTKKHsn+STZBptAi6zIacous+w9yyxl7z1T1h8ptHLhrrzLD5+/987R2XZElZ/39tZsbGg42NdvF4pqcGMs4XEcozAB/oQeu6wGr5fkAZcKOUIIRgQXR723wgaXt/NSgcwlO1r3oARkATfhbmNMMCnlMZdz5J8RN9fVhglS5JA/pJUOJiYXoShCkz/flheDvpzlBCBmya5KcDG1sMSB+r/VQtG+YoFXlwN0Us4yeBXujPmWCOqNlVwX5zHntLH5iQ420YiqX9pqTZFSCrBGBc+InBUDAsbwLRlMC40fGJT8YLRwfnhY3v6/AUtDc9m5z0tRJBOAvHUaFchdY6+zDzEghHv1tUnrNCaIOw84Q2WQmkeO/Xopj1xFBREFr8ZZjuRhA++PEB+t05ggwBucpbH8i/n5C1ZU0EEEmRZnSMxoIYcarKigA0Cb1zpHAyZnGj21xqICAA9dcvo4UgEdZ41FBZSTzEOn30f6QeE3Vhl0gLN+2RGDzZPMHLHKoAO3MFy+ix4sDxFlvMXfrdNgFezy7qrXPaaJg0u27j5nneKrCjJ4pf4e3m4DVMcjNNNKxWnpo6jtnfnkunExB4GbuGKk5FNanpB1nJCjCsThJPAAJ8lVdSF5sSrklM2ZqmYdiC40G7Dfnhp57ZsQz6c3hylEO6ZoZQJxqiVgbhoQK3T6AIgU4rbjxthAPF6NAwAOAcS+ixlp/WBFJRDi0fj2RtcjWRwif8Qdu/w3EKLcu3/YslnrZzwo24UQQvwFCrp/iM1NnHwAAAAASUVORK5CYII='
_tray_icon_notallowed = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAAPcICPcLC/cMDPcQEPcSEvcXF/cYGPcaGvcbG/ccHPgxMfgyMvg0NPg5Ofg6Ovg7O/hBQfhCQvlFRflGRvljY/pkZPplZfpnZ/p2dgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMgEwNYAAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABE0lEQVQ4T4WT65bDIAiExWbbtN0m3Uua+P4P6g4jGtN4NvNL4DuCCC5WWobe++uwmEmtwNxJUTebcwWCt5jJBwsYcKf3NE4hTOOJxj1FEnBTz4NH6qH2jUcCGr/QLLpkQgHe/6VWJXVqFgBB4yI/KVCkBCoFgPrPHw0CWbwCL8RibBFwzQDQH62/QeAtHQBeADUIDbkF/UnmnkB1ixtERrN3xCgyuF5kMntHTCJXh2vyv+wIdMhvgTeCQJ0C2hBMgSKfZlM1wSLXZ5oqgs8sjSpaCQ2VVlfKhLU6fdZGSvyWz9JMb+NE4jt/Nwfm0yJZSkBpYDg7TcJGrjm0Z7jK0B6P/fHiHK8e9Pp/eSmuf1+vf4x/ralnCN9IrncAAAAASUVORK5CYII='
_tray_icon_stop = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAANsAANsBAdsCAtwEBNwFBdwHB9wICNwLC90MDN0NDd0PD90REd0SEt4TE94UFN4WFt4XF94ZGeAjI+AlJeEnJ+EpKeEqKuErK+EsLOEuLuIvL+IyMuIzM+M1NeM2NuM3N+M6OuM8POQ9PeQ+PuQ/P+RAQOVISOVJSeVKSuZLS+ZOTuZQUOZRUedSUudVVehbW+lhYeljY+poaOtvb+twcOtxcetzc+t0dOx3d+x4eOx6eu19fe1+fu2AgO2Cgu6EhO6Ghu6Hh+6IiO6Jie+Kiu+Li++MjO+Nje+Oju+QkPCUlPCVlfKgoPKkpPKlpfKmpvOrq/SurvSxsfSysvW4uPW6uvW7u/W8vPa9vfa+vvbAwPbCwvfExPfFxffGxvfHx/fIyPfJyffKyvjLy/jNzfjQ0PjR0fnS0vnU1PnY2Pvg4Pvi4vvj4/vl5fvm5vzo6Pzr6/3u7v3v7/3x8f3z8/309P719f729v739/74+P75+f76+v77+//8/P/9/f/+/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPHCyoUAAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABnUlEQVQ4T33S50PTQBgG8D6lzLbsIUv2kD0FFWTvPWTvISDIUBGV1ecvj+8luZTR9P1wSe755XK5O4+hK4gn5bc7DcMBz/InQoMXeVjY4FXuCAtEyLUwQcTcFgq45JYQ4JqbwhMtV8IjeUJDjQ+5paqCyG9srEsGgoUlpeXpIjxA1nfyi2+Jqmo7Q9JeV+ODerpvBQTM8/ySzQ3t+xxoL7h7nJve5jd85M7wJq9McHaT8o6TwBTfIIfHQGzoAZ/YiSTSq8D5dSDQVqFADrJ5KFMLPaKLHQiQMQoscClezdgCB4CXD/jM90izR8g85UaKA3YAn4AejhV189acA5LX+DVOg00gnvfoVX/BRQsgbplNGqzLusgIffx1tDchiyRgdRbVHNdgRRZHQD9H1asm+PMzYyYMtoBU/sYgRxxgrmGtBRL/cnf5RL4zzCEHZF2QE14LoOWf6B9vMcJBG/iBxKo8dVtYnyStv6yuUq7FLfmqTzbLEOFest1GNGEemCjCPnKuwjm0LsLMbRBJWLkGr4WdO+Cl0HkYPBc6N4z//HcQqVwcOuIAAAAASUVORK5CYII='
_tray_icon_exclamation = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAAN0zM900NN01Nd02Nt03N944ON45Od46Ot47O98/P99BQd9CQt9DQ+FPT+JSUuJTU+JUVOJVVeJWVuNbW+ReXuVjY+Zra+dxceh4eOl7e+l8fOl+ful/f+qBgeqCguqDg+qFheuJieuLi+yPj+yQkO2Wlu+cnO+hofGqqvGtrfre3vrf3/ri4vvn5/75+f76+v/+/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMQ8SQkAAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABJElEQVQ4T4WS63KCMBBGsyBai62X0otY0aq90ZZa3v/dtpvsJwTijOfXt7tnILOJYY9tNonjNCtQOlqhuKKG0RrNVjgkmIHBHgMId+h7zHSiwg2a9FNVVYScupETmjkd67o+CWpYwft+R6CpCgeUlq5AOyf45+8JsRUKFI6eQLkI3n5CIREBUekLxGaLpATCymRISiAszARJCYSxiZGUQKDLQoqgnPnFhUPOTWeRoZD3FvVZlmVHkE2OEM9iV71GVoZDBGUpAg9QWN5/jx+Ilsi9hz0q4VHOWD+hEF70yc1QEr1a4Q0F0S3eJDfLuv8T4QEFXduZE1rj+et7g6hzCDxF08N+X4DAu+6lUSTnc5wE5tx73ckSTV8QVoux3N88Rykw/wP3i+vwPKk17AAAAABJRU5ErkJggg=='
_tray_icon_none = None


SYSTEM_TRAY_MESSAGE_ICON_INFORMATION = _tray_icon_success
SYSTEM_TRAY_MESSAGE_ICON_WARNING = _tray_icon_exclamation
SYSTEM_TRAY_MESSAGE_ICON_CRITICAL = _tray_icon_stop
SYSTEM_TRAY_MESSAGE_ICON_NOICON = _tray_icon_none


# ------------------------------------------------------------------------- #
#                       Tray CLASS                                      #
# ------------------------------------------------------------------------- #
class SystemTray:
    """
    A "Simulated System Tray" that duplicates the API calls available to PySimpleGUIWx and PySimpleGUIQt users.

    All of the functionality works. The icon is displayed ABOVE the system tray rather than inside of it.
    """

    def __init__(self, menu=None, filename=None, data=None, data_base64=None, tooltip=None, metadata=None):
        """
        SystemTray - create an icon in the system tray
        :param menu: Menu definition
        :type menu: ???
        :param filename: filename for icon
        :type filename: ????
        :param data: in-ram image for icon
        :type data: ???
        :param data_base64: basee-64 data for icon
        :type data_base64: ???
        :param tooltip: tooltip string
        :type tooltip: (str)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: Any
        """
        self.Menu = menu
        self.TrayIcon = None
        self.Shown = False
        self.MenuItemChosen = TIMEOUT_KEY
        self.metadata = metadata
        self.last_message_event = None

        screen_size = Window.get_screen_size()

        if filename:
            image_elem = Image(filename=filename, background_color='red', enable_events=True, tooltip=tooltip, key='-IMAGE-')
        elif data_base64:
            image_elem = Image(data=data_base64, background_color='red', enable_events=True, tooltip=tooltip, key='-IMAGE-')
        elif data:
            image_elem = Image(data=data, background_color='red', enable_events=True, tooltip=tooltip, key='-IMAGE-')
        else:
            image_elem = Image(background_color='red', enable_events=True, tooltip=tooltip, key='-IMAGE-')
        layout = [
                    [image_elem],
                 ]
        self.window = Window('Window Title', layout, element_padding=(0, 0), margins=(0, 0), grab_anywhere=True, no_titlebar=True, transparent_color='red', keep_on_top=True, right_click_menu=menu, location=(screen_size[0] - 100, screen_size[1] - 100),  finalize=True)

        self.window['-IMAGE-'].bind('<Double-Button-1>', '+DOUBLE_CLICK')


    def Read(self, timeout=None):
        """
        Reads the context menu
        :param timeout: Optional.  Any value other than None indicates a non-blocking read
        :return:
        """
        if self.last_message_event != TIMEOUT_KEY and self.last_message_event is not None:
            event = self.last_message_event
            self.last_message_event = None
            return event
        event, values = self.window.read(timeout=timeout)
        if event.endswith('DOUBLE_CLICK'):
            return EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED
        elif event == '-IMAGE-':
            return EVENT_SYSTEM_TRAY_ICON_ACTIVATED

        return event


    def Hide(self):
        """
        Hides the icon
        """
        self.window.hide()


    def UnHide(self):
        """
        Restores a previously hidden icon
        """
        self.window.un_hide()


    def ShowMessage(self, title, message, filename=None, data=None, data_base64=None, messageicon=None, time=(SYSTEM_TRAY_MESSAGE_FADE_IN_DURATION, SYSTEM_TRAY_MESSAGE_DISPLAY_DURATION_IN_MILLISECONDS)):
        """
        Shows a balloon above icon in system tray
        :param title:  Title shown in balloon
        :type title:
        :param message: Message to be displayed
        :type message:
        :param filename: Optional icon filename
        :type filename:
        :param data: Optional in-ram icon
        :type data:
        :param data_base64: Optional base64 icon
        :type data_base64:
        :param time: Amount of time to display message in milliseconds. If tuple, first item is fade in/out duration
        :type time: Union[int, Tuple[int, int]]
        :return:   The event that happened during the display such as user clicked on message
        :rtype:  (Any)
        """

        if isinstance(time, tuple):
            fade_duraction, display_duration = time
        else:
            fade_duration = SYSTEM_TRAY_MESSAGE_FADE_IN_DURATION
            display_duration = time

        user_icon = data_base64 or filename or data or messageicon

        event = self.notify(title, message, icon=user_icon, fade_in_duration=fade_duraction, display_duration_in_ms=display_duration)
        self.last_message_event = event
        return event

    def Close(self):
        """
        Close the system tray window
        """
        self.window.close()


    def Update(self, menu=None, tooltip=None,filename=None, data=None, data_base64=None,):
        """
        Updates the menu, tooltip or icon
        :param menu: menu defintion
        :type menu: ???
        :param tooltip: string representing tooltip
        :type tooltip: ???
        :param filename:  icon filename
        :type filename: ???
        :param data:  icon raw image
        :type data: ???
        :param data_base64: icon base 64 image
        :type data_base64: ???
        """
        # Menu
        if menu is not None:
            top_menu = tk.Menu(self.window.TKroot, tearoff=False)
            AddMenuItem(top_menu, menu[1], self.window['-IMAGE-'])
            self.window['-IMAGE-'].TKRightClickMenu = top_menu

        if filename:
            self.window['-IMAGE-'].update(filename=filename)
        elif data_base64:
            self.window['-IMAGE-'].update(data=data_base64)
        elif data:
            self.window['-IMAGE-'].update(data=data)

        if tooltip:
            self.window['-IMAGE-'].set_tooltip(tooltip)


    @classmethod
    def notify(cls, title, message, icon=_tray_icon_success, display_duration_in_ms=SYSTEM_TRAY_MESSAGE_DISPLAY_DURATION_IN_MILLISECONDS,
               fade_in_duration=SYSTEM_TRAY_MESSAGE_FADE_IN_DURATION, alpha=0.9, location=None):
        """
        Displays a "notification window", usually in the bottom right corner of your display.  Has an icon, a title, and a message
        The window will slowly fade in and out if desired.  Clicking on the window will cause it to move through the end the current "phase". For example, if the window was fading in and it was clicked, then it would immediately stop fading in and instead be fully visible.  It's a way for the user to quickly dismiss the window.
        :param title: Text to be shown at the top of the window in a larger font
        :type title: (str)
        :param message: Text message that makes up the majority of the window
        :type message: (str)
        :param icon: A base64 encoded PNG/GIF image or PNG/GIF filename that will be displayed in the window
        :type icon: Union[bytes, str]
        :param display_duration_in_ms: Number of milliseconds to show the window
        :type display_duration_in_ms: (int)
        :param fade_in_duration: Number of milliseconds to fade window in and out
        :type fade_in_duration: (int)
        :param alpha: Alpha channel. 0 - invisible 1 - fully visible
        :type alpha: (float)
        :param location: Location on the screen to display the window
        :type location: Tuple[int, int]
        :return: (int) reason for returning
        :rtype: (int)
        """

        messages = message.split('\n')
        full_msg = ''
        for m in messages:
            m_wrap = textwrap.fill(m, SYSTEM_TRAY_MESSAGE_MAX_LINE_LENGTH)
            full_msg += m_wrap + '\n'
        message = full_msg[:-1]

        win_msg_lines = message.count("\n") + 1
        max_line = max(message.split('\n'))

        screen_res_x, screen_res_y = Window.get_screen_size()
        win_margin = SYSTEM_TRAY_WIN_MARGINS  # distance from screen edges
        win_width, win_height = 364, 66 + (14.8 * win_msg_lines)

        layout = [[Graph(canvas_size=(win_width, win_height), graph_bottom_left=(0, win_height), graph_top_right=(win_width, 0), key="-GRAPH-",
                         background_color=SYSTEM_TRAY_MESSAGE_WIN_COLOR, enable_events=True)]]

        win_location = location if location is not None else (screen_res_x - win_width - win_margin[0], screen_res_y - win_height - win_margin[1])
        window = Window(title, layout, background_color=SYSTEM_TRAY_MESSAGE_WIN_COLOR, no_titlebar=True,
                        location=win_location, keep_on_top=True, alpha_channel=0, margins=(0, 0), element_padding=(0, 0), grab_anywhere=True, finalize=True)

        window["-GRAPH-"].draw_rectangle((win_width, win_height), (-win_width, -win_height), fill_color=SYSTEM_TRAY_MESSAGE_WIN_COLOR, line_color=SYSTEM_TRAY_MESSAGE_WIN_COLOR)
        if type(icon) is bytes:
            window["-GRAPH-"].draw_image(data=icon, location=(20, 20))
        elif icon is not None:
            window["-GRAPH-"].draw_image(filename=icon, location=(20, 20))
        window["-GRAPH-"].draw_text(title, location=(64, 20), color=SYSTEM_TRAY_MESSAGE_TEXT_COLOR, font=("Helvetica", 12, "bold"), text_location=TEXT_LOCATION_TOP_LEFT)
        window["-GRAPH-"].draw_text(message, location=(64, 44), color=SYSTEM_TRAY_MESSAGE_TEXT_COLOR, font=("Helvetica", 9), text_location=TEXT_LOCATION_TOP_LEFT)
        window["-GRAPH-"].set_cursor('hand2')

        if fade_in_duration:
            for i in range(1, int(alpha * 100)):  # fade in
                window.set_alpha(i / 100)
                event, values = window.read(timeout=fade_in_duration // 100)
                if event != TIMEOUT_KEY:
                    window.set_alpha(1)
                    break
            if event != TIMEOUT_KEY:
                window.close()
                return EVENT_SYSTEM_TRAY_MESSAGE_CLICKED if event == '-GRAPH-' else event
            event, values = window(timeout=display_duration_in_ms)
            if event == TIMEOUT_KEY:
                for i in range(int(alpha * 100), 1, -1):  # fade out
                    window.set_alpha(i / 100)
                    event, values = window.read(timeout=fade_in_duration // 100)
                    if event != TIMEOUT_KEY:
                        break
        else:
            window.set_alpha(alpha)
            event, values = window(timeout=display_duration_in_ms)
        window.close()

        return EVENT_SYSTEM_TRAY_MESSAGE_CLICKED if event == '-GRAPH-' else event

    close = Close
    hide = Hide
    read = Read
    show_message = ShowMessage
    un_hide = UnHide
    update = Update







# ################################################################################
# ################################################################################
#  END OF ELEMENT DEFINITIONS
# ################################################################################
# ################################################################################






# =========================================================================== #
# Button Lazy Functions so the caller doesn't have to define a bunch of stuff #
# =========================================================================== #

# ------------------------- A fake Element... the Pad Element ------------------------- #
def Sizer(h_pixels=0, v_pixels=0):
    """
    "Pushes" out the size of whatever it is placed inside of.  This includes Columns, Frames, Tabs and Windows

    :param h_pixels: (int) number of horizontal pixels
    :type h_pixels: (int)
    :param v_pixels: (int) number of vertical pixels
    :type v_pixels: (int)
    :return: (Column) A column element that has a pad setting set according to parameters
    :rtype: (Column)
    """

    return Column([[]], pad=((h_pixels, 0), (v_pixels, 0)))


# -------------------------  FOLDER BROWSE Element lazy function  ------------------------- #
def FolderBrowse(button_text='Browse', target=(ThisRow, -1), initial_folder=None, tooltip=None, size=(None, None),
                 auto_size_button=None, button_color=None, disabled=False, change_submits=False, enable_events=False,
                 font=None, pad=None, key=None, metadata=None):
    """
    :param button_text: text in the button (Default value = 'Browse')
    :type button_text: (str)
    :param target:  target for the button (Default value = (ThisRow, -1))
    :type target: key or (row,col)
    :param initial_folder:  starting path for folders and files
    :type initial_folder: (str)
    :param tooltip:  text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param size:  (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :param button_color: button color (foreground, background)
    :param disabled: set disable state for element (Default = False)
    :param change_submits: If True, pressing Enter key submits window (Default = False)
    :param enable_events: Turns on the element specific events.(Default = False)
    :param font: Union[str, Tuple[str, int]] specifies the font family, size, etc
    :param pad:  Amount of padding to put around element
    :param key:  Used with window.FindElement and with return values to uniquely identify this element
    :return: (Button)
    """

    return Button(button_text=button_text, button_type=BUTTON_TYPE_BROWSE_FOLDER, target=target,
                  initial_folder=initial_folder, tooltip=tooltip, size=size, auto_size_button=auto_size_button,
                  disabled=disabled, button_color=button_color, change_submits=change_submits,
                  enable_events=enable_events, font=font, pad=pad, key=key, metadata=metadata)


# -------------------------  FILE BROWSE Element lazy function  ------------------------- #
def FileBrowse(button_text='Browse', target=(ThisRow, -1), file_types=(("ALL Files", "*.*"),), initial_folder=None,
               tooltip=None, size=(None, None), auto_size_button=None, button_color=None, change_submits=False,
               enable_events=False, font=None, disabled=False,
               pad=None, key=None, metadata=None):
    """

    :param button_text: text in the button (Default value = 'Browse')
    :param target: key or (row,col) target for the button (Default value = (ThisRow, -1))
    :param file_types:  (Default value = (("ALL Files", "*.*")))
    :param initial_folder:  starting path for folders and files
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param size:  (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param change_submits: If True, pressing Enter key submits window (Default = False)
    :param enable_events: Turns on the element specific events.(Default = False)
    :param font: specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]
    :return: returns a button
    :rtype: (Button)
    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_BROWSE_FILE, target=target, file_types=file_types,
                  initial_folder=initial_folder, tooltip=tooltip, size=size, auto_size_button=auto_size_button,
                  change_submits=change_submits, enable_events=enable_events, disabled=disabled,
                  button_color=button_color, font=font, pad=pad, key=key, metadata=metadata)


# -------------------------  FILES BROWSE Element (Multiple file selection) lazy function  ------------------------- #
def FilesBrowse(button_text='Browse', target=(ThisRow, -1), file_types=(("ALL Files", "*.*"),), disabled=False,
                initial_folder=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
                change_submits=False, enable_events=False,
                font=None, pad=None, key=None, metadata=None):
    """
    Allows browsing of multiple files. File list is returned as a single list with the delimeter defined using the variable
    BROWSE_FILES_DELIMETER.  This defaults to ';' but is changable by the user

    :param button_text: text in the button (Default value = 'Browse')
    :param target: key or (row,col) target for the button (Default value = (ThisRow, -1))
    :param file_types:  (Default value = (("ALL Files", "*.*")))
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param initial_folder:  starting path for folders and files
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param size:  (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param change_submits: If True, pressing Enter key submits window (Default = False)
    :param enable_events: Turns on the element specific events.(Default = False)
    :param font: specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]
    :return: returns a button
    :rtype: (Button)
    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_BROWSE_FILES, target=target, file_types=file_types,
                  initial_folder=initial_folder, change_submits=change_submits, enable_events=enable_events,
                  tooltip=tooltip, size=size, auto_size_button=auto_size_button,
                  disabled=disabled, button_color=button_color, font=font, pad=pad, key=key, metadata=metadata)


# -------------------------  FILE BROWSE Element lazy function  ------------------------- #
def FileSaveAs(button_text='Save As...', target=(ThisRow, -1), file_types=(("ALL Files", "*.*"),), initial_folder=None,
               disabled=False, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
               change_submits=False, enable_events=False, font=None,
               pad=None, key=None, metadata=None):
    """

    :param button_text: text in the button (Default value = 'Save As...')
    :param target: key or (row,col) target for the button (Default value = (ThisRow, -1))
    :param file_types:  (Default value = (("ALL Files", "*.*")))
    :param initial_folder:  starting path for folders and files
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param size:  (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param change_submits: If True, pressing Enter key submits window (Default = False)
    :param enable_events: Turns on the element specific events.(Default = False)
    :param font: specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]
    :return: returns a button
    :rtype: (Button)
    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_SAVEAS_FILE, target=target, file_types=file_types,
                  initial_folder=initial_folder, tooltip=tooltip, size=size, disabled=disabled,
                  auto_size_button=auto_size_button, button_color=button_color, change_submits=change_submits,
                  enable_events=enable_events, font=font, pad=pad, key=key, metadata=metadata)


# -------------------------  SAVE AS Element lazy function  ------------------------- #
def SaveAs(button_text='Save As...', target=(ThisRow, -1), file_types=(("ALL Files", "*.*"),), initial_folder=None,
           disabled=False, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
           change_submits=False, enable_events=False, font=None,
           pad=None, key=None, metadata=None):
    """

    :param button_text: text in the button (Default value = 'Save As...')
    :param target: key or (row,col) target for the button (Default value = (ThisRow, -1))
    :param file_types:  (Default value = (("ALL Files", "*.*")))
    :param initial_folder:  starting path for folders and files
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param size:  (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param change_submits: If True, pressing Enter key submits window (Default = False)
    :param enable_events: Turns on the element specific events.(Default = False)
    :param font: specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]
    :return: returns a button
    :rtype: (Button)
    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_SAVEAS_FILE, target=target, file_types=file_types,
                  initial_folder=initial_folder, tooltip=tooltip, size=size, disabled=disabled,
                  auto_size_button=auto_size_button, button_color=button_color, change_submits=change_submits,
                  enable_events=enable_events, font=font, pad=pad, key=key, metadata=metadata)


# -------------------------  SAVE BUTTON Element lazy function  ------------------------- #
def Save(button_text='Save', size=(None, None), auto_size_button=None, button_color=None, bind_return_key=True,
         disabled=False, tooltip=None, font=None, focus=False, pad=None, key=None, metadata=None):
    """

    :param button_text: text in the button (Default value = 'Save')
    :param size:  (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param bind_return_key:  (Default = True)
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param focus: if focus should be set to this
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]
    :return: returns a button
    :rtype: (Button)
    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  SUBMIT BUTTON Element lazy function  ------------------------- #
def Submit(button_text='Submit', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
           bind_return_key=True, tooltip=None, font=None, focus=False, pad=None, key=None, metadata=None):
    """

    :param button_text: text in the button (Default value = 'Submit')
    :param size:  (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param bind_return_key:  (Default = True)
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param focus: if focus should be set to this
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]
    :return: returns a button
    :rtype: (Button)
    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  OPEN BUTTON Element lazy function  ------------------------- #
# -------------------------  OPEN BUTTON Element lazy function  ------------------------- #
def Open(button_text='Open', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
         bind_return_key=True, tooltip=None, font=None, focus=False, pad=None, key=None, metadata=None):
    """

    :param button_text: text in the button (Default value = 'Open')
    :param size:  (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param bind_return_key:  (Default = True)
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param focus: if focus should be set to this
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]

    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  OK BUTTON Element lazy function  ------------------------- #
def OK(button_text='OK', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
       bind_return_key=True, tooltip=None, font=None, focus=False, pad=None, key=None, metadata=None):
    """

    :param button_text: text in the button (Default value = 'OK')
    :param size:  (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param bind_return_key:  (Default = True)
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param focus: if focus should be set to this
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]
    :return: returns a button
    :rtype: (Button)
    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  YES BUTTON Element lazy function  ------------------------- #
def Ok(button_text='Ok', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
       bind_return_key=True, tooltip=None, font=None, focus=False, pad=None, key=None, metadata=None):
    """

    :param button_text: text in the button (Default value = 'Ok')
    :param size:  (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param bind_return_key:  (Default = True)
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param focus: if focus should be set to this
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]
    :return: returns a button
    :rtype: (Button)
    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  CANCEL BUTTON Element lazy function  ------------------------- #
def Cancel(button_text='Cancel', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
           tooltip=None, font=None, bind_return_key=False, focus=False, pad=None, key=None, metadata=None):
    """

    :param button_text: text in the button (Default value = 'Cancel')
    :param size:  (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param bind_return_key:  (Default = False)
    :param focus: if focus should be set to this
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]

    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  QUIT BUTTON Element lazy function  ------------------------- #
def Quit(button_text='Quit', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
         font=None, bind_return_key=False, focus=False, pad=None, key=None, metadata=None):
    """

    :param button_text: text in the button (Default value = 'Quit')
    :param size:  (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param bind_return_key:  (Default = False)
    :param focus: if focus should be set to this
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]
    :return: returns a button
    :rtype: (Button)
    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  Exit BUTTON Element lazy function  ------------------------- #
def Exit(button_text='Exit', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
         font=None, bind_return_key=False, focus=False, pad=None, key=None, metadata=None):
    """

    :param button_text: text in the button (Default value = 'Exit')
    :param size:  (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param bind_return_key:  (Default = False)
    :param focus: if focus should be set to this
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]

    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  YES BUTTON Element lazy function  ------------------------- #
def Yes(button_text='Yes', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
        font=None, bind_return_key=True, focus=False, pad=None, key=None, metadata=None):
    """

    :param button_text: text in the button (Default value = 'Yes')
    :param size:  (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param bind_return_key:  (Default = True)
    :param focus: if focus should be set to this
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]
    :return: returns a button
    :rtype: (Button)
    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  NO BUTTON Element lazy function  ------------------------- #
def No(button_text='No', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
       font=None, bind_return_key=False, focus=False, pad=None, key=None, metadata=None):
    """

    :param button_text: text in the button (Default value = 'No')
    :param size:  (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param bind_return_key:  (Default = False)
    :param focus: if focus should be set to this
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]

    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  NO BUTTON Element lazy function  ------------------------- #
def Help(button_text='Help', size=(None, None), auto_size_button=None, button_color=None, disabled=False, font=None,
         tooltip=None, bind_return_key=False, focus=False, pad=None, key=None, metadata=None):
    """

    :param button_text: text in the button (Default value = 'Help')
    :param size:  (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param bind_return_key:  (Default = False)
    :param focus: if focus should be set to this
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]
    :return: returns a button
    :rtype: (Button)
    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  NO BUTTON Element lazy function  ------------------------- #
def Debug(button_text='', size=(None, None), auto_size_button=None, button_color=None, disabled=False, font=None,
          tooltip=None, bind_return_key=False, focus=False, pad=None, key=None, metadata=None):
    """

    :param button_text: text in the button (Default value = '')
    :param size:  (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param bind_return_key:  (Default = False)
    :param focus: if focus should be set to this
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]
    :return: returns a button
    :rtype: (Button)
    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_SHOW_DEBUGGER, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=COLOR_SYSTEM_DEFAULT, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, image_data=PSG_DEBUGGER_LOGO,
                  image_subsample=4, border_width=0, metadata=metadata)


# -------------------------  GENERIC BUTTON Element lazy function  ------------------------- #
def SimpleButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
                 border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
                 font=None, bind_return_key=False, disabled=False, focus=False, pad=None, key=None, metadata=None):
    """

    :param button_text: text in the button
    :type button_text: (str)
    :param image_filename: image filename if there is a button image
    :param image_data: in-RAM image to be displayed on button
    :param image_size:  size of button image in pixels
    :param image_subsample:amount to reduce the size of the image
    :param border_width:  width of border around element
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param size: (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param bind_return_key:  (Default = False)
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param focus: if focus should be set to this
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]
    :return: returns a button
    :rtype: (Button)
    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_CLOSES_WIN, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, disabled=disabled, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  CLOSE BUTTON Element lazy function  ------------------------- #
def CloseButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
                border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None, font=None,
                bind_return_key=False, disabled=False, focus=False, pad=None, key=None, metadata=None):
    """

    :param button_text: text in the button
    :type button_text: (str)
    :param image_filename: image filename if there is a button image
    :param image_data: in-RAM image to be displayed on button
    :param image_size:  size of button image in pixels
    :param image_subsample:amount to reduce the size of the image
    :param border_width:  width of border around element
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param size: (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param bind_return_key:  (Default = False)
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param focus: if focus should be set to this
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]
    :return: returns a button
    :rtype: (Button)
    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_CLOSES_WIN, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, disabled=disabled, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


CButton = CloseButton


# -------------------------  GENERIC BUTTON Element lazy function  ------------------------- #
def ReadButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
               border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None, font=None,
               bind_return_key=False, disabled=False, focus=False, pad=None, key=None, metadata=None):
    """

    :param button_text: text in the button
    :type button_text: (str)
    :param image_filename: image filename if there is a button image
    :param image_data: in-RAM image to be displayed on button
    :param image_size:  size of button image in pixels
    :param image_subsample:amount to reduce the size of the image
    :param border_width:  width of border around element
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param size: (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param bind_return_key:  (Default = False)
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param focus: if focus should be set to this
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]

    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, size=size, disabled=disabled,
                  auto_size_button=auto_size_button, button_color=button_color, font=font,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


ReadFormButton = ReadButton
RButton = ReadFormButton


# -------------------------  Realtime BUTTON Element lazy function  ------------------------- #
def RealtimeButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
                   border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
                   font=None, disabled=False, bind_return_key=False, focus=False, pad=None, key=None, metadata=None):
    """

    :param button_text: text in the button
    :type button_text: (str)
    :param image_filename: image filename if there is a button image
    :param image_data: in-RAM image to be displayed on button
    :param image_size:  size of button image in pixels
    :param image_subsample:amount to reduce the size of the image
    :param border_width:  width of border around element
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param size: (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param bind_return_key:  (Default = False)
    :param focus: if focus should be set to this
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]

    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_REALTIME, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, disabled=disabled, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  Dummy BUTTON Element lazy function  ------------------------- #
def DummyButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
                border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None, font=None,
                disabled=False, bind_return_key=False, focus=False, pad=None, key=None, metadata=None):
    """

    :param button_text: text in the button
    :type button_text: (str)
    :param image_filename: image filename if there is a button image
    :param image_data: in-RAM image to be displayed on button
    :param image_size:  size of button image in pixels
    :param image_subsample:amount to reduce the size of the image
    :param border_width:  width of border around element
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param size: (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param bind_return_key:  (Default = False)
    :param focus: if focus should be set to this
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]
    :return: returns a button
    :rtype: (Button)
    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_CLOSES_WIN_ONLY, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, size=size, auto_size_button=auto_size_button,
                  button_color=button_color, font=font, disabled=disabled, bind_return_key=bind_return_key, focus=focus,
                  pad=pad, key=key, metadata=metadata)


# -------------------------  Calendar Chooser Button lazy function  ------------------------- #
def CalendarButton(button_text, target=(None, None), close_when_date_chosen=True, default_date_m_d_y=(None, None, None),
                   image_filename=None, image_data=None, image_size=(None, None),
                   image_subsample=None, tooltip=None, border_width=None, size=(None, None), auto_size_button=None,
                   button_color=None, disabled=False, font=None, bind_return_key=False, focus=False, pad=None,
                   key=None, locale=None, format=None, metadata=None):
    """

    :param button_text: text in the button
    :type button_text: (str)
    :param target:
    :param close_when_date_chosen:  (Default = True)
    :param default_date_m_d_y:  (Default = (None))
    :param image_filename: image filename if there is a button image
    :param image_data: in-RAM image to be displayed on button
    :param image_size:  (Default = (None))
    :param image_subsample:amount to reduce the size of the image
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param border_width:  width of border around element
    :param size: (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param bind_return_key:  (Default = False)
    :param focus: if focus should be set to this
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]
    :param locale:
    :param format:
    :return: returns a button
    :rtype: (Button)
    """
    button = Button(button_text=button_text, button_type=BUTTON_TYPE_CALENDAR_CHOOSER, target=target,
                    image_filename=image_filename, image_data=image_data, image_size=image_size,
                    image_subsample=image_subsample, border_width=border_width, tooltip=tooltip, size=size,
                    auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                    bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)
    button.CalendarCloseWhenChosen = close_when_date_chosen
    button.DefaultDate_M_D_Y = default_date_m_d_y
    button.CalendarLocale = locale
    button.CalendarFormat = format
    return button


# -------------------------  Calendar Chooser Button lazy function  ------------------------- #
def ColorChooserButton(button_text, target=(None, None), image_filename=None, image_data=None, image_size=(None, None),
                       image_subsample=None, tooltip=None, border_width=None, size=(None, None), auto_size_button=None,
                       button_color=None, disabled=False, font=None, bind_return_key=False, focus=False, pad=None,
                       key=None, metadata=None):
    """

    :param button_text: text in the button
    :type button_text: (str)
    :param target:
    :param image_filename: image filename if there is a button image
    :param image_data: in-RAM image to be displayed on button
    :param image_size:  (Default = (None))
    :param image_subsample:amount to reduce the size of the image
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param border_width:  width of border around element
    :param size: (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button:  True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param bind_return_key:  (Default = False)
    :param focus: if focus should be set to this
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple]
    :return: returns a button
    :rtype: (Button)
    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_COLOR_CHOOSER, target=target,
                  image_filename=image_filename, image_data=image_data, image_size=image_size,
                  image_subsample=image_subsample, border_width=border_width, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


#####################################  -----  RESULTS   ------ ##################################################

def AddToReturnDictionary(form, element, value):
    form.ReturnValuesDictionary[element.Key] = value
    # if element.Key is None:
    #     form.ReturnValuesDictionary[form.DictionaryKeyCounter] = value
    #     element.Key = form.DictionaryKeyCounter
    #     form.DictionaryKeyCounter += 1
    # else:
    #     form.ReturnValuesDictionary[element.Key] = value


def AddToReturnList(form, value):
    form.ReturnValuesList.append(value)


# ----------------------------------------------------------------------------#
# -------  FUNCTION InitializeResults.  Sets up form results matrix  --------#
def InitializeResults(form):
    _BuildResults(form, True, form)
    return


# =====  Radio Button RadVar encoding and decoding =====#
# =====  The value is simply the row * 1000 + col  =====#
def DecodeRadioRowCol(RadValue):
    container = RadValue // 100000
    row = RadValue // 1000
    col = RadValue % 1000
    return container, row, col


def EncodeRadioRowCol(container, row, col):
    RadValue = container * 100000 + row * 1000 + col
    return RadValue


# -------  FUNCTION BuildResults.  Form exiting so build the results to pass back  ------- #
# format of return values is
# (Button Pressed, input_values)
def _BuildResults(form, initialize_only, top_level_form):
    # Results for elements are:
    #   TEXT - Nothing
    #   INPUT - Read value from TK
    #   Button - Button Text and position as a Tuple

    # Get the initialized results so we don't have to rebuild
    form.DictionaryKeyCounter = 0
    form.ReturnValuesDictionary = {}
    form.ReturnValuesList = []
    _BuildResultsForSubform(form, initialize_only, top_level_form)
    if not top_level_form.LastButtonClickedWasRealtime:
        top_level_form.LastButtonClicked = None
    return form.ReturnValues


def _BuildResultsForSubform(form, initialize_only, top_level_form):
    button_pressed_text = top_level_form.LastButtonClicked
    for row_num, row in enumerate(form.Rows):
        for col_num, element in enumerate(row):
            if element.Key is not None and WRITE_ONLY_KEY in str(element.Key):
                continue
            value = None
            if element.Type == ELEM_TYPE_COLUMN:
                element.DictionaryKeyCounter = top_level_form.DictionaryKeyCounter
                element.ReturnValuesList = []
                element.ReturnValuesDictionary = {}
                _BuildResultsForSubform(element, initialize_only, top_level_form)
                for item in element.ReturnValuesList:
                    AddToReturnList(top_level_form, item)
                if element.UseDictionary:
                    top_level_form.UseDictionary = True
                if element.ReturnValues[0] is not None:  # if a button was clicked
                    button_pressed_text = element.ReturnValues[0]

            if element.Type == ELEM_TYPE_FRAME:
                element.DictionaryKeyCounter = top_level_form.DictionaryKeyCounter
                element.ReturnValuesList = []
                element.ReturnValuesDictionary = {}
                _BuildResultsForSubform(element, initialize_only, top_level_form)
                for item in element.ReturnValuesList:
                    AddToReturnList(top_level_form, item)
                if element.UseDictionary:
                    top_level_form.UseDictionary = True
                if element.ReturnValues[0] is not None:  # if a button was clicked
                    button_pressed_text = element.ReturnValues[0]

            if element.Type == ELEM_TYPE_PANE:
                element.DictionaryKeyCounter = top_level_form.DictionaryKeyCounter
                element.ReturnValuesList = []
                element.ReturnValuesDictionary = {}
                _BuildResultsForSubform(element, initialize_only, top_level_form)
                for item in element.ReturnValuesList:
                    AddToReturnList(top_level_form, item)
                if element.UseDictionary:
                    top_level_form.UseDictionary = True
                if element.ReturnValues[0] is not None:  # if a button was clicked
                    button_pressed_text = element.ReturnValues[0]

            if element.Type == ELEM_TYPE_TAB_GROUP:
                element.DictionaryKeyCounter = top_level_form.DictionaryKeyCounter
                element.ReturnValuesList = []
                element.ReturnValuesDictionary = {}
                _BuildResultsForSubform(element, initialize_only, top_level_form)
                for item in element.ReturnValuesList:
                    AddToReturnList(top_level_form, item)
                if element.UseDictionary:
                    top_level_form.UseDictionary = True
                if element.ReturnValues[0] is not None:  # if a button was clicked
                    button_pressed_text = element.ReturnValues[0]

            if element.Type == ELEM_TYPE_TAB:
                element.DictionaryKeyCounter = top_level_form.DictionaryKeyCounter
                element.ReturnValuesList = []
                element.ReturnValuesDictionary = {}
                _BuildResultsForSubform(element, initialize_only, top_level_form)
                for item in element.ReturnValuesList:
                    AddToReturnList(top_level_form, item)
                if element.UseDictionary:
                    top_level_form.UseDictionary = True
                if element.ReturnValues[0] is not None:  # if a button was clicked
                    button_pressed_text = element.ReturnValues[0]

            if not initialize_only:
                if element.Type == ELEM_TYPE_INPUT_TEXT:
                    try:
                        value = element.TKStringVar.get()
                    except:
                        value = ''
                    if not top_level_form.NonBlocking and not element.do_not_clear and not top_level_form.ReturnKeyboardEvents:
                        element.TKStringVar.set('')
                elif element.Type == ELEM_TYPE_INPUT_CHECKBOX:
                    value = element.TKIntVar.get()
                    value = (value != 0)
                elif element.Type == ELEM_TYPE_INPUT_RADIO:
                    RadVar = element.TKIntVar.get()
                    this_rowcol = EncodeRadioRowCol(form.ContainerElemementNumber, row_num, col_num)
                    # this_rowcol = element.EncodedRadioValue       # could use the saved one
                    value = RadVar == this_rowcol
                elif element.Type == ELEM_TYPE_BUTTON:
                    if top_level_form.LastButtonClicked == element.ButtonText:
                        button_pressed_text = top_level_form.LastButtonClicked
                        if element.BType != BUTTON_TYPE_REALTIME:  # Do not clear realtime buttons
                            top_level_form.LastButtonClicked = None
                    if element.BType == BUTTON_TYPE_CALENDAR_CHOOSER:
                        try:
                            value = element.TKCal.selection
                        except:
                            value = None
                    else:
                        try:
                            value = element.TKStringVar.get()
                        except:
                            value = None
                elif element.Type == ELEM_TYPE_INPUT_COMBO:
                    element = element  # type: Combo
                    # value = element.TKStringVar.get()
                    try:
                        if element.TKCombo.current() == -1:  # if the current value was not in the original list
                            value = element.TKCombo.get()
                        else:
                            value = element.Values[element.TKCombo.current()]  # get value from original list given index
                    except:
                        value = '*Exception occurred*'
                elif element.Type == ELEM_TYPE_INPUT_OPTION_MENU:
                    value = element.TKStringVar.get()
                elif element.Type == ELEM_TYPE_INPUT_LISTBOX:
                    try:
                        items = element.TKListbox.curselection()
                        value = [element.Values[int(item)] for item in items]
                    except:
                        value = ''
                elif element.Type == ELEM_TYPE_INPUT_SPIN:
                    try:
                        value = element.TKStringVar.get()
                        for v in element.Values:
                            if str(v) == value:
                                value = v
                                break
                    except:
                        value = 0
                elif element.Type == ELEM_TYPE_INPUT_SLIDER:
                    try:
                        value = float(element.TKScale.get())
                    except:
                        value = 0
                elif element.Type == ELEM_TYPE_INPUT_MULTILINE:
                    try:
                        value = element.TKText.get(1.0, tk.END)
                        if not top_level_form.NonBlocking and not element.do_not_clear and not top_level_form.ReturnKeyboardEvents:
                            element.TKText.delete('1.0', tk.END)
                    except:
                        value = None
                elif element.Type == ELEM_TYPE_TAB_GROUP:
                    try:
                        value = element.TKNotebook.tab(element.TKNotebook.index('current'))['text']
                        tab_key = element.FindKeyFromTabName(value)
                        if tab_key is not None:
                            value = tab_key
                    except:
                        value = None
                elif element.Type == ELEM_TYPE_TABLE:
                    value = element.SelectedRows
                elif element.Type == ELEM_TYPE_TREE:
                    value = element.SelectedRows
                elif element.Type == ELEM_TYPE_GRAPH:
                    value = element.ClickPosition
                elif element.Type == ELEM_TYPE_MENUBAR:
                    if element.MenuItemChosen is not None:
                        button_pressed_text = top_level_form.LastButtonClicked = element.MenuItemChosen
                    value = element.MenuItemChosen
                    element.MenuItemChosen = None
                elif element.Type == ELEM_TYPE_BUTTONMENU:
                    value = element.MenuItemChosen
                    element.MenuItemChosen = None

                    # if element.MenuItemChosen is not None:
                    #     button_pressed_text = top_level_form.LastButtonClicked = element.MenuItemChosen
                    # value = element.MenuItemChosen
                    # element.MenuItemChosen = None
            else:
                value = None

            # if an input type element, update the results
            if element.Type != ELEM_TYPE_BUTTON and \
                    element.Type != ELEM_TYPE_TEXT and \
                    element.Type != ELEM_TYPE_IMAGE and \
                    element.Type != ELEM_TYPE_OUTPUT and \
                    element.Type != ELEM_TYPE_PROGRESS_BAR and \
                    element.Type != ELEM_TYPE_COLUMN and \
                    element.Type != ELEM_TYPE_FRAME \
                    and element.Type != ELEM_TYPE_TAB:
                AddToReturnList(form, value)
                AddToReturnDictionary(top_level_form, element, value)
            elif (element.Type == ELEM_TYPE_BUTTON and
                  element.BType == BUTTON_TYPE_CALENDAR_CHOOSER and
                  element.Target == (None, None)) or \
                    (element.Type == ELEM_TYPE_BUTTON and
                     element.BType == BUTTON_TYPE_COLOR_CHOOSER and
                     element.Target == (None, None)) or \
                    (element.Type == ELEM_TYPE_BUTTON
                     and element.Key is not None and
                     (element.BType in (BUTTON_TYPE_SAVEAS_FILE, BUTTON_TYPE_BROWSE_FILE, BUTTON_TYPE_BROWSE_FILES,
                                        BUTTON_TYPE_BROWSE_FOLDER))):
                AddToReturnList(form, value)
                AddToReturnDictionary(top_level_form, element, value)

    # if this is a column, then will fail so need to wrap with tr
    try:
        if form.ReturnKeyboardEvents and form.LastKeyboardEvent is not None:
            button_pressed_text = form.LastKeyboardEvent
            form.LastKeyboardEvent = None
    except:
        pass

    try:
        form.ReturnValuesDictionary.pop(None, None)  # clean up dictionary include None was included
    except:
        pass

    if not form.UseDictionary:
        form.ReturnValues = button_pressed_text, form.ReturnValuesList
    else:
        form.ReturnValues = button_pressed_text, form.ReturnValuesDictionary

    return form.ReturnValues


def FillFormWithValues(window, values_dict):
    """
    Fills a window with values provided in a values dictionary { element_key : new_value }

    :param window:  The window object to fill
    :type window: (Window)
    :param values_dict:  A dictionary with element keys as key and value is values parm for Update call
    :type values_dict: (Dict[Any:Any])
    """

    for element_key in values_dict:
        try:
            window.AllKeysDict[element_key].Update(values_dict[element_key])
        except Exception as e:
            print('Problem filling form. Perhaps bad key?  This is a suspected bad key: {}'.format(element_key))


def _FindElementWithFocusInSubForm(form):
    """
    Searches through a "sub-form" (can be a window or container) for the current element with focus

    :param form: a Window, Column, Frame, or TabGroup (container elements)
    :type form: container elements
    :return: Element
    :rtyp0e: Union[Element, None]
    """
    for row_num, row in enumerate(form.Rows):
        for col_num, element in enumerate(row):
            if element.Type == ELEM_TYPE_COLUMN:
                matching_elem = _FindElementWithFocusInSubForm(element)
                if matching_elem is not None:
                    return matching_elem
            elif element.Type == ELEM_TYPE_FRAME:
                matching_elem = _FindElementWithFocusInSubForm(element)
                if matching_elem is not None:
                    return matching_elem
            elif element.Type == ELEM_TYPE_TAB_GROUP:
                matching_elem = _FindElementWithFocusInSubForm(element)
                if matching_elem is not None:
                    return matching_elem
            elif element.Type == ELEM_TYPE_TAB:
                matching_elem = _FindElementWithFocusInSubForm(element)
                if matching_elem is not None:
                    return matching_elem
            elif element.Type == ELEM_TYPE_INPUT_TEXT:
                if element.TKEntry is not None:
                    if element.TKEntry is element.TKEntry.focus_get():
                        return element
            elif element.Type == ELEM_TYPE_INPUT_MULTILINE:
                if element.TKText is not None:
                    if element.TKText is element.TKText.focus_get():
                        return element
            elif element.Type == ELEM_TYPE_BUTTON:
                if element.TKButton is not None:
                    if element.TKButton is element.TKButton.focus_get():
                        return element
            else:  # The "Catch All" - if type isn't one of the above, try generic element.Widget
                try:
                    if element.Widget is not None:
                        if element.Widget is element.Widget.focus_get():
                            return element
                except:
                    return None

    return None


if sys.version_info[0] >= 3:
    def AddMenuItem(top_menu, sub_menu_info, element, is_sub_menu=False, skip=False):
        """
        Only to be used internally. Not user callable
        :param top_menu: ???
        :param sub_menu_info: ???
        :param element: ???
        :param is_sub_menu:  (Default = False)
        :param skip:  (Default = False)

        """
        return_val = None
        if type(sub_menu_info) is str:
            if not is_sub_menu and not skip:
                # print(f'Adding command {sub_menu_info}')
                pos = sub_menu_info.find('&')
                if pos != -1:
                    if pos == 0 or sub_menu_info[pos - 1] != "\\":
                        sub_menu_info = sub_menu_info[:pos] + sub_menu_info[pos + 1:]
                if sub_menu_info == '---':
                    top_menu.add('separator')
                else:
                    try:
                        item_without_key = sub_menu_info[:sub_menu_info.index(MENU_KEY_SEPARATOR)]
                    except:
                        item_without_key = sub_menu_info

                    if item_without_key[0] == MENU_DISABLED_CHARACTER:
                        top_menu.add_command(label=item_without_key[len(MENU_DISABLED_CHARACTER):], underline=pos,
                                             command=lambda: element._MenuItemChosenCallback(sub_menu_info))
                        top_menu.entryconfig(item_without_key[len(MENU_DISABLED_CHARACTER):], state='disabled')
                    else:
                        top_menu.add_command(label=item_without_key, underline=pos,
                                             command=lambda: element._MenuItemChosenCallback(sub_menu_info))
        else:
            i = 0
            while i < (len(sub_menu_info)):
                item = sub_menu_info[i]
                if i != len(sub_menu_info) - 1:
                    if type(sub_menu_info[i + 1]) == list:
                        new_menu = tk.Menu(top_menu, tearoff=element.Tearoff)
                        if element.Font is not None:
                            new_menu.config(font=element.Font)
                        return_val = new_menu
                        pos = sub_menu_info[i].find('&')
                        if pos != -1:
                            if pos == 0 or sub_menu_info[i][pos - 1] != "\\":
                                sub_menu_info[i] = sub_menu_info[i][:pos] + sub_menu_info[i][pos + 1:]
                        if sub_menu_info[i][0] == MENU_DISABLED_CHARACTER:
                            top_menu.add_cascade(label=sub_menu_info[i][len(MENU_DISABLED_CHARACTER):], menu=new_menu,
                                                 underline=pos, state='disabled')
                        else:
                            top_menu.add_cascade(label=sub_menu_info[i], menu=new_menu, underline=pos)
                        AddMenuItem(new_menu, sub_menu_info[i + 1], element, is_sub_menu=True)
                        i += 1  # skip the next one
                    else:
                        AddMenuItem(top_menu, item, element)
                else:
                    AddMenuItem(top_menu, item, element)
                i += 1
        return return_val
else:
    def AddMenuItem(top_menu, sub_menu_info, element, is_sub_menu=False, skip=False):
        """

        :param top_menu: ???
        :param sub_menu_info: ???
        :param element: ???
        :param is_sub_menu:  (Default = False)
        :param skip:  (Default = False)

        """
        if not isinstance(sub_menu_info, list):
            if not is_sub_menu and not skip:
                # print(f'Adding command {sub_menu_info}')
                pos = sub_menu_info.find('&')
                if pos != -1:
                    if pos == 0 or sub_menu_info[pos - 1] != "\\":
                        sub_menu_info = sub_menu_info[:pos] + sub_menu_info[pos + 1:]
                if sub_menu_info == '---':
                    top_menu.add('separator')
                else:
                    try:
                        item_without_key = sub_menu_info[:sub_menu_info.index(MENU_KEY_SEPARATOR)]
                    except:
                        item_without_key = sub_menu_info

                    if item_without_key[0] == MENU_DISABLED_CHARACTER:
                        top_menu.add_command(label=item_without_key[len(MENU_DISABLED_CHARACTER):], underline=pos,
                                             command=lambda: element._MenuItemChosenCallback(sub_menu_info))
                        top_menu.entryconfig(item_without_key[len(MENU_DISABLED_CHARACTER):], state='disabled')
                    else:
                        top_menu.add_command(label=item_without_key, underline=pos,
                                             command=lambda: element._MenuItemChosenCallback(sub_menu_info))
        else:
            i = 0
            while i < (len(sub_menu_info)):
                item = sub_menu_info[i]
                if i != len(sub_menu_info) - 1:
                    if isinstance(sub_menu_info[i + 1], list):
                        new_menu = tk.Menu(top_menu, tearoff=element.Tearoff)
                        pos = sub_menu_info[i].find('&')
                        if pos != -1:
                            if pos == 0 or sub_menu_info[i][pos - 1] != "\\":
                                sub_menu_info[i] = sub_menu_info[i][:pos] + sub_menu_info[i][pos + 1:]
                        if sub_menu_info[i][0] == MENU_DISABLED_CHARACTER:
                            top_menu.add_cascade(label=sub_menu_info[i][len(MENU_DISABLED_CHARACTER):], menu=new_menu,
                                                 underline=pos, state='disabled')
                        else:
                            top_menu.add_cascade(label=sub_menu_info[i], menu=new_menu, underline=pos)
                        AddMenuItem(new_menu, sub_menu_info[i + 1], element, is_sub_menu=True)
                        i += 1  # skip the next one
                    else:
                        AddMenuItem(top_menu, item, element)
                else:
                    AddMenuItem(top_menu, item, element)
                i += 1

# 888    888      d8b          888
# 888    888      Y8P          888
# 888    888                   888
# 888888 888  888 888 88888b.  888888  .d88b.  888d888
# 888    888 .88P 888 888 "88b 888    d8P  Y8b 888P"
# 888    888888K  888 888  888 888    88888888 888
# Y88b.  888 "88b 888 888  888 Y88b.  Y8b.     888
#  "Y888 888  888 888 888  888  "Y888  "Y8888  888

# My crappy tkinter code starts here.  (search for "crappy" to get here quickly... that's the purpose if you hadn't caught on

"""
         )
        (
          ,
       ___)\
      (_____)
      (_______)

"""


# Also, to get to the point in the code where each element's widget is created, look for element + "p lacement" (without the space)


# ========================   TK CODE STARTS HERE ========================================= #
# @_timeit
def PackFormIntoFrame(form, containing_frame, toplevel_form):
    """

    :param form: a window class
    :type form: (Window)
    :param containing_frame: ???
    :type containing_frame: ???
    :param toplevel_form: ???
    :type toplevel_form: (Window)

    """

    def _char_width_in_pixels(font):
        return tkinter.font.Font(font=font).measure('A')  # single character width

    def _char_height_in_pixels(font):
        return tkinter.font.Font(font=font).metrics('linespace')

    def _string_width_in_pixels(font, string):
        return tkinter.font.Font(font=font).measure(string)  # single character width

    border_depth = toplevel_form.BorderDepth if toplevel_form.BorderDepth is not None else DEFAULT_BORDER_WIDTH
    # --------------------------------------------------------------------------- #
    # ****************  Use FlexForm to build the tkinter window ********** ----- #
    # Building is done row by row.                                                #
    # --------------------------------------------------------------------------- #
    ######################### LOOP THROUGH ROWS #########################
    # *********** -------  Loop through ROWS  ------- ***********#
    for row_num, flex_row in enumerate(form.Rows):
        ######################### LOOP THROUGH ELEMENTS ON ROW #########################
        # *********** -------  Loop through ELEMENTS  ------- ***********#
        # *********** Make TK Row                             ***********#
        tk_row_frame = tk.Frame(containing_frame)
        row_should_expand = False
        row_justify = form.ElementJustification
        for col_num, element in enumerate(flex_row):
            element.ParentRowFrame = tk_row_frame
            element.ParentForm = toplevel_form  # save the button's parent form object
            if toplevel_form.Font and (element.Font == DEFAULT_FONT or not element.Font):
                font = toplevel_form.Font
            elif element.Font is not None:
                font = element.Font
            else:
                font = DEFAULT_FONT
            # -------  Determine Auto-Size setting on a cascading basis ------- #
            if element.AutoSizeText is not None:  # if element overide
                auto_size_text = element.AutoSizeText
            elif toplevel_form.AutoSizeText is not None:  # if form override
                auto_size_text = toplevel_form.AutoSizeText
            else:
                auto_size_text = DEFAULT_AUTOSIZE_TEXT
            element_type = element.Type
            # Set foreground color
            text_color = element.TextColor
            elementpad = element.Pad if element.Pad is not None else toplevel_form.ElementPadding
            element.pad_used = elementpad    # store the value used back into the element
            # Determine Element size
            element_size = element.Size
            if (element_size == (None, None) and element_type not in (
                    ELEM_TYPE_BUTTON, ELEM_TYPE_BUTTONMENU)):  # user did not specify a size
                element_size = toplevel_form.DefaultElementSize
            elif (element_size == (None, None) and element_type in (ELEM_TYPE_BUTTON, ELEM_TYPE_BUTTONMENU)):
                element_size = toplevel_form.DefaultButtonElementSize
            else:
                auto_size_text = False  # if user has specified a size then it shouldn't autosize
            # -------------------------  COLUMN placement element  ------------------------- #
            if element_type == ELEM_TYPE_COLUMN:
                element = element  # type: Column
                if element.Scrollable:
                    element.TKColFrame = TkScrollableFrame(tk_row_frame, element.VerticalScrollOnly)  # do not use yet!  not working
                    PackFormIntoFrame(element, element.TKColFrame.TKFrame, toplevel_form)
                    element.TKColFrame.TKFrame.update()
                    if element.Size == (None, None):  # if no size specified, use column width x column height/2
                        element.TKColFrame.canvas.config(width=element.TKColFrame.TKFrame.winfo_reqwidth(),
                                                         height=element.TKColFrame.TKFrame.winfo_reqheight() / 2)
                    else:
                        if None not in (element.Size[0], element.Size[1]):
                            element.TKColFrame.canvas.config(width=element.Size[0], height=element.Size[1])
                        elif element.Size[1] is not None:
                            element.TKColFrame.canvas.config(height=element.Size[1])
                        elif element.Size[0] is not None:
                            element.TKColFrame.canvas.config(width=element.Size[0])

                    if not element.BackgroundColor in (None, COLOR_SYSTEM_DEFAULT):
                        element.TKColFrame.canvas.config(background=element.BackgroundColor)
                        element.TKColFrame.TKFrame.config(background=element.BackgroundColor, borderwidth=0,
                                                          highlightthickness=0)
                        element.TKColFrame.config(background=element.BackgroundColor, borderwidth=0,
                                                  highlightthickness=0)
                else:
                    if element.Size != (None, None):
                        element.TKColFrame = TkFixedFrame(tk_row_frame)
                        PackFormIntoFrame(element, element.TKColFrame.TKFrame, toplevel_form)
                        element.TKColFrame.TKFrame.update()
                        if None not in (element.Size[0], element.Size[1]):
                            element.TKColFrame.canvas.config(width=element.Size[0], height=element.Size[1])
                        elif element.Size[1] is not None:
                            element.TKColFrame.canvas.config(height=element.Size[1])
                        elif element.Size[0] is not None:
                            element.TKColFrame.canvas.config(width=element.Size[0])
                        if not element.BackgroundColor in (None, COLOR_SYSTEM_DEFAULT):
                            element.TKColFrame.canvas.config(background=element.BackgroundColor)
                            element.TKColFrame.TKFrame.config(background=element.BackgroundColor, borderwidth=0,
                                                              highlightthickness=0)
                    else:
                        element.TKColFrame = tk.Frame(tk_row_frame)
                        PackFormIntoFrame(element, element.TKColFrame, toplevel_form)
                        if not element.BackgroundColor in (None, COLOR_SYSTEM_DEFAULT):
                            element.TKColFrame.config(background=element.BackgroundColor, borderwidth=0,
                                                      highlightthickness=0)
                if element.Justification.lower().startswith('c'):
                    anchor = tk.N
                    side = tk.TOP
                elif element.Justification.lower().startswith('r'):
                    anchor = tk.NE
                    side = tk.RIGHT
                else:
                    anchor = tk.NW
                    side = tk.LEFT
                # anchor=tk.NW
                # side = tk.LEFT
                row_justify = element.Justification
                element.Widget = element.TKColFrame
                element.TKColFrame.pack(side=side, anchor=anchor, padx=elementpad[0], pady=elementpad[1], expand=False, fill=tk.NONE)
                # element.TKColFrame.pack(side=side, padx=elementpad[0], pady=elementpad[1], expand=True, fill='both')
                if element.Visible is False:
                    element.TKColFrame.pack_forget()
                # element.TKColFrame = element.TKColFrame
                # if element.BackgroundColor != COLOR_SYSTEM_DEFAULT and element.BackgroundColor is not None:
                #     element.TKColFrame.configure(background=element.BackgroundColor,
                #                                  highlightbackground=element.BackgroundColor,
                #                                  highlightcolor=element.BackgroundColor)
                if element.RightClickMenu or toplevel_form.RightClickMenu:
                    menu = element.RightClickMenu or toplevel_form.RightClickMenu
                    top_menu = tk.Menu(toplevel_form.TKroot, tearoff=False)
                    AddMenuItem(top_menu, menu[1], element)
                    element.TKRightClickMenu = top_menu
                    element.TKColFrame.bind('<Button-3>', element._RightClickMenuCallback)
                # row_should_expand = True
            # -------------------------  Pane placement element  ------------------------- #
            if element_type == ELEM_TYPE_PANE:
                bd = element.BorderDepth if element.BorderDepth is not None else border_depth
                element.PanedWindow = element.Widget = tk.PanedWindow(tk_row_frame,
                                                                      orient=tk.VERTICAL if element.Orientation.startswith(
                                                                          'v') else tk.HORIZONTAL,
                                                                      borderwidth=bd,
                                                                      bd=bd,
                                                                      )
                if element.Relief is not None:
                    element.PanedWindow.configure(relief=element.Relief)
                element.PanedWindow.configure(handlesize=element.HandleSize)
                if element.ShowHandle:
                    element.PanedWindow.config(showhandle=True)
                if element.Size != (None, None):
                    element.PanedWindow.config(width=element.Size[0], height=element.Size[1])
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    element.PanedWindow.configure(background=element.BackgroundColor)
                for pane in element.PaneList:
                    pane.Widget = pane.TKColFrame = tk.Frame(element.PanedWindow)
                    pane.ParentPanedWindow = element.PanedWindow
                    PackFormIntoFrame(pane, pane.TKColFrame, toplevel_form)
                    if pane.Visible:
                        element.PanedWindow.add(pane.TKColFrame)
                    if pane.BackgroundColor != COLOR_SYSTEM_DEFAULT and pane.BackgroundColor is not None:
                        pane.TKColFrame.configure(background=pane.BackgroundColor,
                                                  highlightbackground=pane.BackgroundColor,
                                                  highlightcolor=pane.BackgroundColor)

                element.PanedWindow.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1], expand=True, fill='both')
                if element.Visible is False:
                    element.PanedWindow.pack_forget()
            # -------------------------  TEXT placement element  ------------------------- #
            elif element_type == ELEM_TYPE_TEXT:
                # auto_size_text = element.AutoSizeText
                element = element  # type: Text
                display_text = element.DisplayText  # text to display
                if auto_size_text is False:
                    width, height = element_size
                else:
                    lines = display_text.split('\n')
                    max_line_len = max([len(l) for l in lines])
                    num_lines = len(lines)
                    if max_line_len > element_size[0]:  # if text exceeds element size, the will have to wrap
                        width = element_size[0]
                    else:
                        width = max_line_len
                    height = num_lines
                # ---===--- LABEL widget create and place --- #
                element = element  # type: Text
                bd = element.BorderWidth if element.BorderWidth is not None else border_depth
                stringvar = tk.StringVar()
                element.TKStringVar = stringvar
                stringvar.set(str(display_text))
                if auto_size_text:
                    width = 0
                if element.Justification is not None:
                    justification = element.Justification
                elif toplevel_form.TextJustification is not None:
                    justification = toplevel_form.TextJustification
                else:
                    justification = DEFAULT_TEXT_JUSTIFICATION
                justify = tk.LEFT if justification.startswith('l') else tk.CENTER if justification.startswith('c') else tk.RIGHT
                anchor = tk.NW if justification.startswith('l') else tk.N if justification.startswith('c') else tk.NE
                tktext_label = element.Widget = tk.Label(tk_row_frame, textvariable=stringvar, width=width,
                                                         height=height, justify=justify, bd=bd, font=font)
                # Set wrap-length for text (in PIXELS) == PAIN IN THE ASS
                wraplen = tktext_label.winfo_reqwidth()  # width of widget in Pixels
                if not auto_size_text and height == 1:  # if just 1 line high, ensure no wrap happens
                    wraplen = 0
                # print(f'Text wraplen = {wraplen} wxh = {width} x {height}')
                # print(f'Len = {len(display_text)} Text = {str(display_text)}')
                tktext_label.configure(anchor=anchor, wraplen=wraplen)  # set wrap to width of widget
                if element.Relief is not None:
                    tktext_label.configure(relief=element.Relief)
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    tktext_label.configure(background=element.BackgroundColor)
                if element.TextColor != COLOR_SYSTEM_DEFAULT and element.TextColor is not None:
                    tktext_label.configure(fg=element.TextColor)
                tktext_label.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1])
                if element.Visible is False:
                    tktext_label.pack_forget()
                element.TKText = tktext_label
                if element.ClickSubmits:
                    tktext_label.bind('<Button-1>', element._TextClickedHandler)
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element.TKText, text=element.Tooltip, timeout=DEFAULT_TOOLTIP_TIME)
                if element.RightClickMenu or toplevel_form.RightClickMenu:
                    menu = element.RightClickMenu or toplevel_form.RightClickMenu
                    top_menu = tk.Menu(toplevel_form.TKroot, tearoff=False)
                    AddMenuItem(top_menu, menu[1], element)
                    element.TKRightClickMenu = top_menu
                    tktext_label.bind('<Button-3>', element._RightClickMenuCallback)
            # -------------------------  BUTTON placement element non-ttk version  ------------------------- #
            elif (element_type == ELEM_TYPE_BUTTON and element.UseTtkButtons is False) or \
                    (element_type == ELEM_TYPE_BUTTON and element.UseTtkButtons is not True and toplevel_form.UseTtkButtons is not True):
                element = element  # type: Button
                element.UseTtkButtons = False  # indicate that ttk button was not used
                stringvar = tk.StringVar()
                element.TKStringVar = stringvar
                element.Location = (row_num, col_num)
                btext = element.ButtonText
                btype = element.BType
                if element.AutoSizeButton is not None:
                    auto_size = element.AutoSizeButton
                else:
                    auto_size = toplevel_form.AutoSizeButtons
                if auto_size is False or element.Size[0] is not None:
                    width, height = element_size
                else:
                    width = 0
                    height = toplevel_form.DefaultButtonElementSize[1]
                if element.ButtonColor != (None, None) and element.ButtonColor != DEFAULT_BUTTON_COLOR:
                    bc = element.ButtonColor
                elif toplevel_form.ButtonColor != (None, None) and toplevel_form.ButtonColor != DEFAULT_BUTTON_COLOR:
                    bc = toplevel_form.ButtonColor
                else:
                    bc = DEFAULT_BUTTON_COLOR
                bd = element.BorderWidth
                if btype != BUTTON_TYPE_REALTIME:
                    tkbutton = element.Widget = tk.Button(tk_row_frame, text=btext, width=width, height=height,
                                                          command=element.ButtonCallBack, justify=tk.CENTER, bd=bd, font=font)
                else:
                    tkbutton = element.Widget = tk.Button(tk_row_frame, text=btext, width=width, height=height,
                                                          justify=tk.CENTER, bd=bd, font=font)
                    tkbutton.bind('<ButtonRelease-1>', element.ButtonReleaseCallBack)
                    tkbutton.bind('<ButtonPress-1>', element.ButtonPressCallBack)
                if bc != (None, None) and bc != COLOR_SYSTEM_DEFAULT and bc[1] != COLOR_SYSTEM_DEFAULT:
                    tkbutton.config(foreground=bc[0], background=bc[1], activebackground=bc[1])
                elif bc[1] == COLOR_SYSTEM_DEFAULT:
                    tkbutton.config(foreground=bc[0])
                if bd == 0 and not sys.platform.startswith('darwin'):
                    tkbutton.config(relief=tk.FLAT)
                tkbutton.config(highlightthickness=0)
                element.TKButton = tkbutton  # not used yet but save the TK button in case
                wraplen = tkbutton.winfo_reqwidth()  # width of widget in Pixels
                if element.ImageFilename:  # if button has an image on it
                    tkbutton.config(highlightthickness=0)
                    photo = tk.PhotoImage(file=element.ImageFilename)
                    if element.ImageSubsample:
                        photo = photo.subsample(element.ImageSubsample)
                    if element.ImageSize != (None, None):
                        width, height = element.ImageSize
                    else:
                        width, height = photo.width(), photo.height()
                    tkbutton.config(image=photo, compound=tk.CENTER, width=width, height=height)
                    tkbutton.image = photo
                if element.ImageData:  # if button has an image on it
                    tkbutton.config(highlightthickness=0)
                    photo = tk.PhotoImage(data=element.ImageData)
                    if element.ImageSubsample:
                        photo = photo.subsample(element.ImageSubsample)
                    if element.ImageSize != (None, None):
                        width, height = element.ImageSize
                    else:
                        width, height = photo.width(), photo.height()
                    tkbutton.config(image=photo, compound=tk.CENTER, width=width, height=height)
                    tkbutton.image = photo
                if width != 0:
                    tkbutton.configure(wraplength=wraplen + 10)  # set wrap to width of widget
                tkbutton.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1])
                if element.Visible is False:
                    tkbutton.pack_forget()
                if element.BindReturnKey:
                    element.TKButton.bind('<Return>', element._ReturnKeyHandler)
                if element.Focus is True or (toplevel_form.UseDefaultFocus and not toplevel_form.FocusSet):
                    toplevel_form.FocusSet = True
                    element.TKButton.bind('<Return>', element._ReturnKeyHandler)
                    element.TKButton.focus_set()
                    toplevel_form.TKroot.focus_force()
                if element.Disabled == True:
                    element.TKButton['state'] = 'disabled'
                if element.DisabledButtonColor != (None, None):
                    if element.DisabledButtonColor[0] is not None:
                        element.TKButton['disabledforeground'] = element.DisabledButtonColor[0]
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element.TKButton, text=element.Tooltip,
                                                    timeout=DEFAULT_TOOLTIP_TIME)
            # -------------------------  BUTTON placement element ttk version ------------------------- #
            elif element_type == ELEM_TYPE_BUTTON:
                element = element  # type: Button
                element.UseTtkButtons = True  # indicate that ttk button was used
                stringvar = tk.StringVar()
                element.TKStringVar = stringvar
                element.Location = (row_num, col_num)
                btext = element.ButtonText
                btype = element.BType
                if element.AutoSizeButton is not None:
                    auto_size = element.AutoSizeButton
                else:
                    auto_size = toplevel_form.AutoSizeButtons
                if auto_size is False or element.Size[0] is not None:
                    width, height = element_size
                else:
                    width = 0
                    height = toplevel_form.DefaultButtonElementSize[1]
                if element.ButtonColor != (None, None) and element.ButtonColor != COLOR_SYSTEM_DEFAULT:
                    bc = element.ButtonColor
                elif toplevel_form.ButtonColor != (None, None) and toplevel_form.ButtonColor != COLOR_SYSTEM_DEFAULT:
                    bc = toplevel_form.ButtonColor
                else:
                    bc = DEFAULT_BUTTON_COLOR
                bd = element.BorderWidth
                if btype != BUTTON_TYPE_REALTIME:
                    tkbutton = element.Widget = ttk.Button(tk_row_frame, text=btext, width=width, command=element.ButtonCallBack)
                else:
                    tkbutton = element.Widget = ttk.Button(tk_row_frame, text=btext, width=width)
                    tkbutton.bind('<ButtonRelease-1>', element.ButtonReleaseCallBack)
                    tkbutton.bind('<ButtonPress-1>', element.ButtonPressCallBack)

                style_name = str(element.Key) + 'custombutton.TButton'
                button_style = ttk.Style()
                button_style.theme_use(toplevel_form.TtkTheme)
                button_style.configure(style_name, font=font)

                if bc != (None, None) and bc != COLOR_SYSTEM_DEFAULT and bc[1] != COLOR_SYSTEM_DEFAULT:
                    button_style.configure(style_name, foreground=bc[0], background=bc[1])
                elif bc[1] == COLOR_SYSTEM_DEFAULT:
                    button_style.configure(style_name, foreground=bc[0])
                if bd == 0 and not sys.platform.startswith('darwin'):
                    button_style.configure(style_name, relief=tk.FLAT)
                    button_style.configure(style_name, borderwidth=0)
                else:
                    button_style.configure(style_name, borderwidth=bd)
                button_style.configure(style_name, justify=tk.CENTER)
                if element.DisabledButtonColor != (None, None):
                    if element.DisabledButtonColor[0] is not None:
                        button_style.map(style_name, foreground=[('disabled', element.DisabledButtonColor[0])])
                    if element.DisabledButtonColor[1] is not None:
                        button_style.map(style_name, background=[('disabled', element.DisabledButtonColor[1])])
                if height > 1:
                    button_style.configure(style_name, padding=height * _char_width_in_pixels(font))    # should this be height instead?
                wraplen = tkbutton.winfo_reqwidth()  # width of widget in Pixels
                if width != 0:
                    button_style.configure(style_name, wraplength=wraplen)  # set wrap to width of widget

                if element.ImageFilename:  # if button has an image on it
                    button_style.configure(style_name, borderwidth=0)
                    # tkbutton.configure(highlightthickness=0)
                    photo = tk.PhotoImage(file=element.ImageFilename)
                    if element.ImageSubsample:
                        photo = photo.subsample(element.ImageSubsample)
                    if element.ImageSize != (None, None):
                        width, height = element.ImageSize
                    else:
                        width, height = photo.width(), photo.height()
                    button_style.configure(style_name, image=photo, compound=tk.CENTER, width=width, height=height)
                    tkbutton.image = photo
                if element.ImageData:  # if button has an image on it
                    # tkbutton.configure(highlightthickness=0)
                    button_style.configure(style_name, borderwidth=0)

                    photo = tk.PhotoImage(data=element.ImageData)
                    if element.ImageSubsample:
                        photo = photo.subsample(element.ImageSubsample)
                    if element.ImageSize != (None, None):
                        width, height = element.ImageSize
                    else:
                        width, height = photo.width(), photo.height()
                    button_style.configure(style_name, image=photo, compound=tk.CENTER, width=width, height=height)
                    # tkbutton.configure(image=photo, compound=tk.CENTER, width=width, height=height)
                    tkbutton.image = photo

                element.TKButton = tkbutton  # not used yet but save the TK button in case
                tkbutton.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1])
                if element.Visible is False:
                    tkbutton.pack_forget()
                if element.BindReturnKey:
                    element.TKButton.bind('<Return>', element._ReturnKeyHandler)
                if element.Focus is True or (toplevel_form.UseDefaultFocus and not toplevel_form.FocusSet):
                    toplevel_form.FocusSet = True
                    element.TKButton.bind('<Return>', element._ReturnKeyHandler)
                    element.TKButton.focus_set()
                    toplevel_form.TKroot.focus_force()
                if element.Disabled == True:
                    element.TKButton['state'] = 'disabled'

                tkbutton.configure(style=style_name)  # IMPORTANT!  Apply the style to the button!

                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element.TKButton, text=element.Tooltip,
                                                    timeout=DEFAULT_TOOLTIP_TIME)
            # -------------------------  BUTTONMENU placement element  ------------------------- #
            elif element_type == ELEM_TYPE_BUTTONMENU:
                element = element  # type: ButtonMenu
                element.Location = (row_num, col_num)
                btext = element.ButtonText
                if element.AutoSizeButton is not None:
                    auto_size = element.AutoSizeButton
                else:
                    auto_size = toplevel_form.AutoSizeButtons
                if auto_size is False or element.Size[0] is not None:
                    width, height = element_size
                else:
                    width = 0
                    height = toplevel_form.DefaultButtonElementSize[1]
                if element.ButtonColor != (None, None) and element.ButtonColor != DEFAULT_BUTTON_COLOR:
                    bc = element.ButtonColor
                elif toplevel_form.ButtonColor != (None, None) and toplevel_form.ButtonColor != DEFAULT_BUTTON_COLOR:
                    bc = toplevel_form.ButtonColor
                else:
                    bc = DEFAULT_BUTTON_COLOR
                bd = element.BorderWidth
                tkbutton = element.Widget = tk.Menubutton(tk_row_frame, text=btext, width=width, height=height,
                                                          justify=tk.LEFT, bd=bd, font=font)
                element.TKButtonMenu = tkbutton
                if bc != (None, None) and bc != COLOR_SYSTEM_DEFAULT and bc[1] != COLOR_SYSTEM_DEFAULT:
                    tkbutton.config(foreground=bc[0], background=bc[1], activebackground=bc[1])
                elif bc[1] == COLOR_SYSTEM_DEFAULT:
                    tkbutton.config(foreground=bc[0])
                if bd == 0:
                    tkbutton.config(relief=tk.FLAT)
                tkbutton.config(highlightthickness=0)
                element.TKButton = tkbutton  # not used yet but save the TK button in case
                wraplen = tkbutton.winfo_reqwidth()  # width of widget in Pixels
                if element.ImageFilename:  # if button has an image on it
                    photo = tk.PhotoImage(file=element.ImageFilename)
                    if element.ImageSize != (None, None):
                        width, height = element.ImageSize
                        if element.ImageSubsample:
                            photo = photo.subsample(element.ImageSubsample)
                    else:
                        width, height = photo.width(), photo.height()
                    tkbutton.config(image=photo, compound=tk.CENTER, width=width, height=height)
                    tkbutton.image = photo
                if element.ImageData:  # if button has an image on it
                    photo = tk.PhotoImage(data=element.ImageData)
                    if element.ImageSize != (None, None):
                        width, height = element.ImageSize
                        if element.ImageSubsample:
                            photo = photo.subsample(element.ImageSubsample)
                    else:
                        width, height = photo.width(), photo.height()
                    tkbutton.config(image=photo, compound=tk.CENTER, width=width, height=height)
                    tkbutton.image = photo
                if width != 0:
                    tkbutton.configure(wraplength=wraplen + 10)  # set wrap to width of widget
                tkbutton.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1])

                menu_def = element.MenuDefinition

                top_menu = tk.Menu(tkbutton, tearoff=False)
                AddMenuItem(top_menu, menu_def[1], element)

                tkbutton.configure(menu=top_menu)
                element.TKMenu = top_menu
                if element.Visible is False:
                    tkbutton.pack_forget()
                if element.Disabled == True:
                    element.TKButton['state'] = 'disabled'
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element.TKButton, text=element.Tooltip,
                                                    timeout=DEFAULT_TOOLTIP_TIME)


            # -------------------------  INPUT placement element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_TEXT:
                element = element  # type: InputText
                default_text = element.DefaultText
                element.TKStringVar = tk.StringVar()
                element.TKStringVar.set(default_text)
                show = element.PasswordCharacter if element.PasswordCharacter else ""
                # bd = element.BorderDepth if element.BorderDepth is not None else border_depth
                bd = border_depth
                if element.Justification is not None:
                    justification = element.Justification
                else:
                    justification = DEFAULT_TEXT_JUSTIFICATION
                justify = tk.LEFT if justification.startswith('l') else tk.CENTER if justification.startswith('c') else tk.RIGHT
                # anchor = tk.NW if justification == 'left' else tk.N if justification == 'center' else tk.NE
                element.TKEntry = element.Widget = tk.Entry(tk_row_frame, width=element_size[0],
                                                            textvariable=element.TKStringVar, bd=bd,
                                                            font=font, show=show, justify=justify)
                if element.ChangeSubmits:
                    element.TKEntry.bind('<Key>', element._KeyboardHandler)
                element.TKEntry.bind('<Return>', element._ReturnKeyHandler)
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    element.TKEntry.configure(background=element.BackgroundColor)
                if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
                    element.TKEntry.configure(fg=text_color)
                element.Widget.config(highlightthickness=0)

                element.TKEntry.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1], expand=False, fill=tk.NONE)
                if element.Visible is False:
                    element.TKEntry.pack_forget()
                if element.Focus is True or (toplevel_form.UseDefaultFocus and not toplevel_form.FocusSet):
                    toplevel_form.FocusSet = True
                    element.TKEntry.focus_set()
                if element.Disabled:
                    element.TKEntry['state'] = 'readonly' if element.UseReadonlyForDisable else 'disabled'
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element.TKEntry, text=element.Tooltip, timeout=DEFAULT_TOOLTIP_TIME)
                if element.RightClickMenu or toplevel_form.RightClickMenu:
                    menu = element.RightClickMenu or toplevel_form.RightClickMenu
                    top_menu = tk.Menu(toplevel_form.TKroot, tearoff=False)
                    AddMenuItem(top_menu, menu[1], element)
                    element.TKRightClickMenu = top_menu
                    element.TKEntry.bind('<Button-3>', element._RightClickMenuCallback)
                # row_should_expand = True

            # -------------------------  COMBO placement element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_COMBO:
                element = element  # type: InputCombo
                max_line_len = max([len(str(l)) for l in element.Values]) if len(element.Values) else 0
                if auto_size_text is False:
                    width = element_size[0]
                else:
                    width = max_line_len
                element.TKStringVar = tk.StringVar()
                style_name = 'TCombobox'
                s = ttk.Style()
                s.theme_use(toplevel_form.TtkTheme)
                # s.theme_use('default')
                if element.TextColor is not None and element.TextColor != COLOR_SYSTEM_DEFAULT:
                    # Creates 1 style per Text Color/ Background Color combination
                    style_name = str(element.Key) + '.TCombobox'
                    combostyle = ttk.Style()
                    combostyle.theme_use(toplevel_form.TtkTheme)

                    # Creates a unique name for each field element(Sure there is a better way to do this)

                    unique_field = str(element.Key) + '.TCombobox.field'

                    # Clones over the TCombobox.field element from the "alt" theme.
                    # This is what will allow us to change the background color without altering the whole programs theme

                    # try:        # if this element is in a window that's shown TWICE, will get an error here, so skip error
                    #     combostyle.element_create(unique_field, "from", "alt")
                    # except:
                    #     pass

                    # Create widget layout using cloned "alt" field
                    # combostyle.layout(style_name, [
                    #     (unique_field, {'children': [('Combobox.downarrow', {'side': 'right', 'sticky': 'ns'}),
                    #                                  ('Combobox.padding',
                    #                                   {'children': [('Combobox.focus',
                    #                                                  {'children': [('Combobox.textarea',
                    #                                                                 {'sticky': 'nswe'})],
                    #                                                   'expand': '1',
                    #                                                   'sticky': 'nswe'})],
                    #                                    'expand': '1',
                    #                                    'sticky': 'nswe'})],
                    #                     'sticky': 'nswe'})])

                    # Copy default TCombobox settings
                    # Getting an error on this line of code
                    # combostyle.configure(style_name, *combostyle.configure("TCombobox"))

                    # Set individual widget options
                    combostyle.configure(style_name, foreground=element.TextColor)
                    combostyle.configure(style_name, selectbackground=element.BackgroundColor)
                    combostyle.configure(style_name, fieldbackground=element.BackgroundColor)
                    combostyle.configure(style_name, selectforeground=element.TextColor)

                element.TKCombo = element.Widget = ttk.Combobox(tk_row_frame, width=width,
                                                                textvariable=element.TKStringVar, font=font,
                                                                style=style_name)
                if element.Size[1] != 1 and element.Size[1] is not None:
                    element.TKCombo.configure(height=element.Size[1])
                element.TKCombo['values'] = element.Values

                element.TKCombo.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1])
                if element.Visible is False:
                    element.TKCombo.pack_forget()
                if element.DefaultValue is not None:
                    element.TKCombo.set(element.DefaultValue)
                    # for i, v in enumerate(element.Values):
                    #     if v == element.DefaultValue:
                    #         element.TKCombo.current(i)
                    #         break
                # elif element.Values:
                #     element.TKCombo.current(0)
                if element.ChangeSubmits:
                    element.TKCombo.bind('<<ComboboxSelected>>', element._ComboboxSelectHandler)
                if element.Readonly:
                    element.TKCombo['state'] = 'readonly'
                if element.Disabled is True:  # note overrides readonly if disabled
                    element.TKCombo['state'] = 'disabled'
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element.TKCombo, text=element.Tooltip, timeout=DEFAULT_TOOLTIP_TIME)
            # -------------------------  OPTION MENU placement Element (Like ComboBox but different) element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_OPTION_MENU:
                max_line_len = max([len(str(l)) for l in element.Values])
                if auto_size_text is False:
                    width = element_size[0]
                else:
                    width = max_line_len
                element.TKStringVar = tk.StringVar()
                default = element.DefaultValue if element.DefaultValue else element.Values[0]
                element.TKStringVar.set(default)
                element.TKOptionMenu = element.Widget = tk.OptionMenu(tk_row_frame, element.TKStringVar,
                                                                      *element.Values)
                element.TKOptionMenu.config(highlightthickness=0, font=font, width=width)
                element.TKOptionMenu.config(borderwidth=border_depth)
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    element.TKOptionMenu.configure(background=element.BackgroundColor)
                if element.TextColor != COLOR_SYSTEM_DEFAULT and element.TextColor is not None:
                    element.TKOptionMenu.configure(fg=element.TextColor)
                element.TKOptionMenu.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1])
                if element.Visible is False:
                    element.TKOptionMenu.pack_forget()
                if element.Disabled == True:
                    element.TKOptionMenu['state'] = 'disabled'
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element.TKOptionMenu, text=element.Tooltip,
                                                    timeout=DEFAULT_TOOLTIP_TIME)
            # -------------------------  LISTBOX placement element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_LISTBOX:
                element = element  # type: Listbox
                max_line_len = max([len(str(l)) for l in element.Values]) if len(element.Values) else 0
                if auto_size_text is False:
                    width = element_size[0]
                else:
                    width = max_line_len
                listbox_frame = tk.Frame(tk_row_frame)
                element.TKStringVar = tk.StringVar()
                element.TKListbox = element.Widget = tk.Listbox(listbox_frame, height=element_size[1], width=width,
                                                                selectmode=element.SelectMode, font=font,
                                                                exportselection=False)
                element.Widget.config(highlightthickness=0)
                for index, item in enumerate(element.Values):
                    element.TKListbox.insert(tk.END, item)
                    if element.DefaultValues is not None and item in element.DefaultValues:
                        element.TKListbox.selection_set(index)
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    element.TKListbox.configure(background=element.BackgroundColor)
                if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
                    element.TKListbox.configure(fg=text_color)
                if element.ChangeSubmits:
                    element.TKListbox.bind('<<ListboxSelect>>', element._ListboxSelectHandler)
                if not element.NoScrollbar:
                    element.vsb = tk.Scrollbar(listbox_frame, orient="vertical", command=element.TKListbox.yview)
                    element.TKListbox.configure(yscrollcommand=element.vsb.set)
                    element.vsb.pack(side=tk.RIGHT, fill='y')
                listbox_frame.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1])
                element.TKListbox.pack(side=tk.LEFT)
                if element.Visible is False:
                    listbox_frame.pack_forget()
                    element.vsb.pack_forget()
                if element.BindReturnKey:
                    element.TKListbox.bind('<Return>', element._ListboxSelectHandler)
                    element.TKListbox.bind('<Double-Button-1>', element._ListboxSelectHandler)
                if element.Disabled == True:
                    element.TKListbox['state'] = 'disabled'
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element.TKListbox, text=element.Tooltip,
                                                    timeout=DEFAULT_TOOLTIP_TIME)
                if element.RightClickMenu or toplevel_form.RightClickMenu:
                    menu = element.RightClickMenu or toplevel_form.RightClickMenu
                    top_menu = tk.Menu(toplevel_form.TKroot, tearoff=False)
                    AddMenuItem(top_menu, menu[1], element)
                    element.TKRightClickMenu = top_menu
                    element.TKListbox.bind('<Button-3>', element._RightClickMenuCallback)
            # -------------------------  MULTILINE placement element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_MULTILINE:
                element = element  # type: Multiline
                width, height = element_size
                bd = element.BorderWidth
                element.TKText = element.Widget = tk.scrolledtext.ScrolledText(tk_row_frame, width=width, height=height,
                                                                               wrap='word', bd=bd, font=font,
                                                                               relief=RELIEF_SUNKEN)
                if element.DefaultText:
                    element.TKText.insert(1.0, element.DefaultText)  # set the default text
                element.TKText.config(highlightthickness=0)
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    element.TKText.configure(background=element.BackgroundColor)
                # if DEFAULT_SCROLLBAR_COLOR not in (None, COLOR_SYSTEM_DEFAULT):               # only works on Linux so not including it
                #     element.TKText.vbar.config(troughcolor=DEFAULT_SCROLLBAR_COLOR)
                element.TKText.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1])
                if element.Visible is False:
                    element.TKText.pack_forget()
                if element.ChangeSubmits:
                    element.TKText.bind('<Key>', element._KeyboardHandler)
                if element.EnterSubmits:
                    element.TKText.bind('<Return>', element._ReturnKeyHandler)
                if element.Focus is True or (toplevel_form.UseDefaultFocus and not toplevel_form.FocusSet):
                    toplevel_form.FocusSet = True
                    element.TKText.focus_set()
                if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
                    element.TKText.configure(fg=text_color)
                if element.Disabled == True:
                    element.TKText['state'] = 'disabled'
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element.TKText, text=element.Tooltip, timeout=DEFAULT_TOOLTIP_TIME)
                if element.RightClickMenu or toplevel_form.RightClickMenu:
                    menu = element.RightClickMenu or toplevel_form.RightClickMenu
                    top_menu = tk.Menu(toplevel_form.TKroot, tearoff=False)
                    AddMenuItem(top_menu, menu[1], element)
                    element.TKRightClickMenu = top_menu
                    element.TKText.bind('<Button-3>', element._RightClickMenuCallback)
                # row_should_expand = True
            # -------------------------  CHECKBOX pleacement element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_CHECKBOX:
                element = element           # type: Checkbox
                width = 0 if auto_size_text else element_size[0]
                default_value = element.InitialState
                element.TKIntVar = tk.IntVar()
                element.TKIntVar.set(default_value if default_value is not None else 0)
                if element.ChangeSubmits:
                    element.TKCheckbutton = element.Widget = tk.Checkbutton(tk_row_frame, anchor=tk.NW,
                                                                            text=element.Text, width=width,
                                                                            variable=element.TKIntVar, bd=border_depth,
                                                                            font=font,
                                                                            command=element._CheckboxHandler)
                else:
                    element.TKCheckbutton = element.Widget = tk.Checkbutton(tk_row_frame, anchor=tk.NW,
                                                                            text=element.Text, width=width,
                                                                            variable=element.TKIntVar, bd=border_depth,
                                                                            font=font)
                if element.Disabled:
                    element.TKCheckbutton.configure(state='disable')
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    element.TKCheckbutton.configure(background=element.BackgroundColor)
                    element.TKCheckbutton.configure(selectcolor=element.CheckboxBackgroundColor)    # The background of the checkbox
                    element.TKCheckbutton.configure(activebackground=element.BackgroundColor)
                if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
                    element.TKCheckbutton.configure(fg=text_color)
                element.Widget.configure(highlightthickness=0)
                element.TKCheckbutton.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1])
                if element.Visible is False:
                    element.TKCheckbutton.pack_forget()
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element.TKCheckbutton, text=element.Tooltip,
                                                    timeout=DEFAULT_TOOLTIP_TIME)
            # -------------------------  PROGRESS placement element  ------------------------- #
            elif element_type == ELEM_TYPE_PROGRESS_BAR:
                element = element  # type: ProgressBar
                # save this form because it must be 'updated' (refreshed) solely for the purpose of updating bar
                width = element_size[0]
                fnt = tkinter.font.Font()
                char_width = fnt.measure('A')  # single character width
                progress_length = width * char_width
                progress_width = element_size[1]
                direction = element.Orientation
                if element.BarColor != (None, None):  # if element has a bar color, use it
                    bar_color = element.BarColor
                else:
                    bar_color = DEFAULT_PROGRESS_BAR_COLOR
                element.TKProgressBar = TKProgressBar(tk_row_frame, element.MaxValue, progress_length, progress_width,
                                                      orientation=direction, BarColor=bar_color,
                                                      border_width=element.BorderWidth, relief=element.Relief,
                                                      style=toplevel_form.TtkTheme, key=element.Key)
                element.TKProgressBar.TKProgressBarForReal.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1])
                if element.Visible is False:
                    element.TKProgressBar.TKProgressBarForReal.pack_forget()
                element.Widget = element.TKProgressBar.TKProgressBarForReal
                # -------------------------  RADIO placement element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_RADIO:
                element = element  # type: Radio
                width = 0 if auto_size_text else element_size[0]
                default_value = element.InitialState
                ID = element.GroupID
                # see if ID has already been placed
                value = EncodeRadioRowCol(form.ContainerElemementNumber, row_num,
                                          col_num)  # value to set intvar to if this radio is selected
                element.EncodedRadioValue = value
                if ID in toplevel_form.RadioDict:
                    RadVar = toplevel_form.RadioDict[ID]
                else:
                    RadVar = tk.IntVar()
                    toplevel_form.RadioDict[ID] = RadVar
                element.TKIntVar = RadVar  # store the RadVar in Radio object
                if default_value:  # if this radio is the one selected, set RadVar to match
                    element.TKIntVar.set(value)
                if element.ChangeSubmits:
                    element.TKRadio = element.Widget = tk.Radiobutton(tk_row_frame, anchor=tk.NW, text=element.Text,
                                                                      width=width,
                                                                      variable=element.TKIntVar, value=value,
                                                                      bd=border_depth, font=font,
                                                                      command=element._RadioHandler)
                else:
                    element.TKRadio = element.Widget = tk.Radiobutton(tk_row_frame, anchor=tk.NW, text=element.Text,
                                                                      width=width,
                                                                      variable=element.TKIntVar, value=value,
                                                                      bd=border_depth, font=font)
                if not element.BackgroundColor in (None, COLOR_SYSTEM_DEFAULT):
                    element.TKRadio.configure(background=element.BackgroundColor)
                    element.TKRadio.configure(selectcolor=element.CircleBackgroundColor)
                    element.TKRadio.configure(activebackground=element.BackgroundColor)
                if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
                    element.TKRadio.configure(fg=text_color)
                element.Widget.config(highlightthickness=0)
                if element.Disabled:
                    element.TKRadio['state'] = 'disabled'
                element.TKRadio.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1])
                if element.Visible is False:
                    element.TKRadio.pack_forget()
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element.TKRadio, text=element.Tooltip, timeout=DEFAULT_TOOLTIP_TIME)
                # -------------------------  SPIN placement element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_SPIN:
                element = element  # type: Spin
                width, height = element_size
                width = 0 if auto_size_text else element_size[0]
                element.TKStringVar = tk.StringVar()
                element.TKSpinBox = element.Widget = tk.Spinbox(tk_row_frame, values=element.Values,
                                                                textvariable=element.TKStringVar,
                                                                width=width, bd=border_depth)
                if element.DefaultValue is not None:
                    element.TKStringVar.set(element.DefaultValue)
                element.TKSpinBox.configure(font=font)  # set wrap to width of widget
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    element.TKSpinBox.configure(background=element.BackgroundColor)
                element.Widget.config(highlightthickness=0)
                element.TKSpinBox.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1])
                if element.Visible is False:
                    element.TKSpinBox.pack_forget()
                if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
                    element.TKSpinBox.configure(fg=text_color)
                if element.ChangeSubmits:
                    element.TKSpinBox.bind('<ButtonRelease-1>', element._SpinChangedHandler)
                if element.Disabled == True:
                    element.TKSpinBox['state'] = 'disabled'
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element.TKSpinBox, text=element.Tooltip,
                                                    timeout=DEFAULT_TOOLTIP_TIME)
                # -------------------------  OUTPUT placement element  ------------------------- #
            elif element_type == ELEM_TYPE_OUTPUT:
                width, height = element_size
                element._TKOut = element.Widget = TKOutput(tk_row_frame, width=width, height=height, bd=border_depth,
                                                           background_color=element.BackgroundColor,
                                                           text_color=text_color, font=font,
                                                           pad=elementpad)
                element._TKOut.output.configure(takefocus=0)  # make it so that Output does not get focus
                element._TKOut.pack(side=tk.LEFT, expand=False, fill=tk.NONE)
                if element.Visible is False:
                    element._TKOut.frame.pack_forget()
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element._TKOut, text=element.Tooltip, timeout=DEFAULT_TOOLTIP_TIME)
                if element.RightClickMenu or toplevel_form.RightClickMenu:
                    menu = element.RightClickMenu or toplevel_form.RightClickMenu
                    top_menu = tk.Menu(toplevel_form.TKroot, tearoff=False)
                    AddMenuItem(top_menu, menu[1], element)
                    element.TKRightClickMenu = top_menu
                    element._TKOut.bind('<Button-3>', element._RightClickMenuCallback)
                # row_should_expand = True
                # -------------------------  IMAGE placement element  ------------------------- #
            elif element_type == ELEM_TYPE_IMAGE:
                element = element  # type: Image
                if element.Filename is not None:
                    photo = tk.PhotoImage(file=element.Filename)
                elif element.Data is not None:
                    photo = tk.PhotoImage(data=element.Data)
                else:
                    photo = None
                    # print('*ERROR laying out form.... Image Element has no image specified*')

                if photo is not None:
                    if element_size == (
                            None, None) or element_size == None or element_size == toplevel_form.DefaultElementSize:
                        width, height = photo.width(), photo.height()
                    else:
                        width, height = element_size
                    if photo is not None:
                        element.tktext_label = element.Widget = tk.Label(tk_row_frame, image=photo, width=width,
                                                                         height=height,
                                                                         bd=border_depth)
                    else:
                        element.tktext_label = element.Widget = tk.Label(tk_row_frame, width=width, height=height,
                                                                         bd=border_depth)

                    if not element.BackgroundColor in (None, COLOR_SYSTEM_DEFAULT):
                        element.tktext_label.config(background=element.BackgroundColor)

                    element.tktext_label.image = photo
                    # tktext_label.configure(anchor=tk.NW, image=photo)
                    element.tktext_label.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1])

                if element.Visible is False:
                    element.tktext_label.pack_forget()
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element.tktext_label, text=element.Tooltip,
                                                    timeout=DEFAULT_TOOLTIP_TIME)
                if element.EnableEvents:
                    element.tktext_label.bind('<ButtonPress-1>', element._ClickHandler)
                if element.RightClickMenu or toplevel_form.RightClickMenu:
                    menu = element.RightClickMenu or toplevel_form.RightClickMenu
                    top_menu = tk.Menu(toplevel_form.TKroot, tearoff=False)
                    AddMenuItem(top_menu, menu[1], element)
                    element.TKRightClickMenu = top_menu
                    element.tktext_label.bind('<Button-3>', element._RightClickMenuCallback)
                # -------------------------  Canvas placement element  ------------------------- #
            elif element_type == ELEM_TYPE_CANVAS:
                width, height = element_size
                if element._TKCanvas is None:
                    element._TKCanvas = element.Widget = tk.Canvas(tk_row_frame, width=width, height=height,
                                                                   bd=border_depth)
                else:
                    element._TKCanvas.master = tk_row_frame
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    element._TKCanvas.configure(background=element.BackgroundColor, highlightthickness=0)
                element._TKCanvas.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1])
                if element.Visible is False:
                    element._TKCanvas.pack_forget()
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element._TKCanvas, text=element.Tooltip,
                                                    timeout=DEFAULT_TOOLTIP_TIME)
                if element.RightClickMenu or toplevel_form.RightClickMenu:
                    menu = element.RightClickMenu or toplevel_form.RightClickMenu
                    top_menu = tk.Menu(toplevel_form.TKroot, tearoff=False)
                    AddMenuItem(top_menu, menu[1], element)
                    element.TKRightClickMenu = top_menu
                    element._TKCanvas.bind('<Button-3>', element._RightClickMenuCallback)
                # -------------------------  Graph placement element  ------------------------- #
            elif element_type == ELEM_TYPE_GRAPH:
                element = element  # type: Graph
                width, height = element_size
                # I don't know why TWO canvases were being defined, on inside the other.  Was it so entire canvas can move?
                # if element._TKCanvas is None:
                #     element._TKCanvas = tk.Canvas(tk_row_frame, width=width, height=height, bd=border_depth)
                # else:
                #     element._TKCanvas.master = tk_row_frame
                element._TKCanvas2 = element.Widget = tk.Canvas(tk_row_frame, width=width, height=height,
                                                                bd=border_depth)
                element._TKCanvas2.pack(side=tk.LEFT)
                element._TKCanvas2.addtag_all('mytag')
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    element._TKCanvas2.configure(background=element.BackgroundColor, highlightthickness=0)
                    # element._TKCanvas.configure(background=element.BackgroundColor, highlightthickness=0)
                element._TKCanvas2.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1])
                if element.Visible is False:
                    # element._TKCanvas.pack_forget()
                    element._TKCanvas2.pack_forget()
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element._TKCanvas2, text=element.Tooltip,
                                                    timeout=DEFAULT_TOOLTIP_TIME)
                if element.ChangeSubmits:
                    element._TKCanvas2.bind('<ButtonRelease-1>', element.ButtonReleaseCallBack)
                    element._TKCanvas2.bind('<ButtonPress-1>', element.ButtonPressCallBack)
                if element.DragSubmits:
                    element._TKCanvas2.bind('<Motion>', element.MotionCallBack)
                if element.RightClickMenu or toplevel_form.RightClickMenu:
                    menu = element.RightClickMenu or toplevel_form.RightClickMenu
                    top_menu = tk.Menu(toplevel_form.TKroot, tearoff=False)
                    AddMenuItem(top_menu, menu[1], element)
                    element.TKRightClickMenu = top_menu
                    element._TKCanvas2.bind('<Button-3>', element._RightClickMenuCallback)
            # -------------------------  MENU placement element  ------------------------- #
            elif element_type == ELEM_TYPE_MENUBAR:
                element = element  # type: MenuBar
                menu_def = element.MenuDefinition
                element.TKMenu = element.Widget = tk.Menu(toplevel_form.TKroot,
                                                          tearoff=element.Tearoff)  # create the menubar
                menubar = element.TKMenu
                for menu_entry in menu_def:
                    # print(f'Adding a Menubar ENTRY {menu_entry}')
                    baritem = tk.Menu(menubar, tearoff=element.Tearoff)
                    if element.Font is not None:
                        baritem.config(font=element.Font)
                    pos = menu_entry[0].find('&')
                    # print(pos)
                    if pos != -1:
                        if pos == 0 or menu_entry[0][pos - 1] != "\\":
                            menu_entry[0] = menu_entry[0][:pos] + menu_entry[0][pos + 1:]
                    if menu_entry[0][0] == MENU_DISABLED_CHARACTER:
                        menubar.add_cascade(label=menu_entry[0][len(MENU_DISABLED_CHARACTER):], menu=baritem,
                                            underline=pos)
                        menubar.entryconfig(menu_entry[0][len(MENU_DISABLED_CHARACTER):], state='disabled')
                    else:
                        menubar.add_cascade(label=menu_entry[0], menu=baritem, underline=pos)

                    if len(menu_entry) > 1:
                        AddMenuItem(baritem, menu_entry[1], element)
                toplevel_form.TKroot.configure(menu=element.TKMenu)
            # -------------------------  Frame placement element  ------------------------- #
            elif element_type == ELEM_TYPE_FRAME:
                element = element  # type: Frame
                labeled_frame = element.Widget = tk.LabelFrame(tk_row_frame, text=element.Title, relief=element.Relief)
                element.TKFrame = labeled_frame
                PackFormIntoFrame(element, labeled_frame, toplevel_form)
                labeled_frame.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1], fill=tk.NONE, expand=False)
                if element.Size != (None, None):
                    labeled_frame.config(width=element.Size[0], height=element.Size[1])
                if not element.Visible:
                    labeled_frame.pack_forget()
                if element.BackgroundColor != COLOR_SYSTEM_DEFAULT and element.BackgroundColor is not None:
                    labeled_frame.configure(background=element.BackgroundColor,
                                            highlightbackground=element.BackgroundColor,
                                            highlightcolor=element.BackgroundColor)
                if element.TextColor != COLOR_SYSTEM_DEFAULT and element.TextColor is not None:
                    labeled_frame.configure(foreground=element.TextColor)
                if font is not None:
                    labeled_frame.configure(font=font)
                if element.TitleLocation is not None:
                    labeled_frame.configure(labelanchor=element.TitleLocation)
                if element.BorderWidth is not None:
                    labeled_frame.configure(borderwidth=element.BorderWidth)
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(labeled_frame, text=element.Tooltip, timeout=DEFAULT_TOOLTIP_TIME)
                if element.RightClickMenu or toplevel_form.RightClickMenu:
                    menu = element.RightClickMenu or toplevel_form.RightClickMenu
                    top_menu = tk.Menu(toplevel_form.TKroot, tearoff=False)
                    AddMenuItem(top_menu, menu[1], element)
                    element.TKRightClickMenu = top_menu
                    labeled_frame.bind('<Button-3>', element._RightClickMenuCallback)
                # row_should_expand=True
            # -------------------------  Tab placement element  ------------------------- #
            elif element_type == ELEM_TYPE_TAB:
                element = element  # type: Tab
                element.TKFrame = element.Widget = tk.Frame(form.TKNotebook)
                PackFormIntoFrame(element, element.TKFrame, toplevel_form)
                state = 'normal'
                if element.Disabled:
                    state = 'disabled'
                if element.Visible is False:
                    state = 'hidden'
                form.TKNotebook.add(element.TKFrame, text=element.Title, state=state)
                form.TKNotebook.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1], fill=tk.NONE, expand=False)
                element.ParentNotebook = form.TKNotebook
                element.TabID = form.TabCount
                form.TabCount += 1
                if element.BackgroundColor != COLOR_SYSTEM_DEFAULT and element.BackgroundColor is not None:
                    element.TKFrame.configure(background=element.BackgroundColor,
                                              highlightbackground=element.BackgroundColor,
                                              highlightcolor=element.BackgroundColor)

                if element.BorderWidth is not None:
                    element.TKFrame.configure(borderwidth=element.BorderWidth)
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element.TKFrame, text=element.Tooltip,
                                                    timeout=DEFAULT_TOOLTIP_TIME)
                if element.RightClickMenu or toplevel_form.RightClickMenu:
                    menu = element.RightClickMenu or toplevel_form.RightClickMenu
                    top_menu = tk.Menu(toplevel_form.TKroot, tearoff=False)
                    AddMenuItem(top_menu, menu[1], element)
                    element.TKRightClickMenu = top_menu
                    element.TKFrame.bind('<Button-3>', element._RightClickMenuCallback)
                # row_should_expand = True
            # -------------------------  TabGroup placement element  ------------------------- #
            elif element_type == ELEM_TYPE_TAB_GROUP:
                element = element  # type: TabGroup
                custom_style = str(element.Key) + 'customtab.TNotebook'
                style = ttk.Style()
                style.theme_use(toplevel_form.TtkTheme)
                if element.TabLocation is not None:
                    position_dict = {'left': 'w', 'right': 'e', 'top': 'n', 'bottom': 's', 'lefttop': 'wn',
                                     'leftbottom': 'ws', 'righttop': 'en', 'rightbottom': 'es', 'bottomleft': 'sw',
                                     'bottomright': 'se', 'topleft': 'nw', 'topright': 'ne'}
                    try:
                        tab_position = position_dict[element.TabLocation]
                    except:
                        tab_position = position_dict['top']
                    style.configure(custom_style, tabposition=tab_position)

                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    style.configure(custom_style, background=element.BackgroundColor, foreground='purple')

                # FINALLY the proper styling to get tab colors!
                if element.SelectedTitleColor is not None and element.SelectedTitleColor != COLOR_SYSTEM_DEFAULT:
                    style.map(custom_style + '.Tab', foreground=[("selected", element.SelectedTitleColor)])
                if element.SelectedBackgroundColor is not None and element.SelectedBackgroundColor != COLOR_SYSTEM_DEFAULT:
                    style.map(custom_style + '.Tab', background=[("selected", element.SelectedBackgroundColor)])
                if element.TabBackgroundColor is not None and element.TabBackgroundColor != COLOR_SYSTEM_DEFAULT:
                    style.configure(custom_style + '.Tab', background=element.TabBackgroundColor)
                if element.TextColor is not None and element.TextColor != COLOR_SYSTEM_DEFAULT:
                    style.configure(custom_style + '.Tab', foreground=element.TextColor)
                style.configure(custom_style + '.Tab', font=font)

                element.TKNotebook = element.Widget = ttk.Notebook(tk_row_frame, style=custom_style)

                PackFormIntoFrame(element, toplevel_form.TKroot, toplevel_form)

                if element.ChangeSubmits:
                    element.TKNotebook.bind('<<NotebookTabChanged>>', element._TabGroupSelectHandler)
                if element.BorderWidth is not None:
                    element.TKNotebook.configure(borderwidth=element.BorderWidth)
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element.TKNotebook, text=element.Tooltip,
                                                    timeout=DEFAULT_TOOLTIP_TIME)
                # row_should_expand = True
                # -------------------------  SLIDER placement element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_SLIDER:
                element = element  # type: Slider
                slider_length = element_size[0] * _char_width_in_pixels(font)
                slider_width = element_size[1]
                element.TKIntVar = tk.IntVar()
                element.TKIntVar.set(element.DefaultValue)
                if element.Orientation.startswith('v'):
                    range_from = element.Range[1]
                    range_to = element.Range[0]
                    slider_length += DEFAULT_MARGINS[1] * (element_size[0] * 2)  # add in the padding
                else:
                    range_from = element.Range[0]
                    range_to = element.Range[1]
                if element.ChangeSubmits:
                    tkscale = element.Widget = tk.Scale(tk_row_frame, orient=element.Orientation,
                                                        variable=element.TKIntVar,
                                                        from_=range_from, to_=range_to, resolution=element.Resolution,
                                                        length=slider_length, width=slider_width,
                                                        bd=element.BorderWidth,
                                                        relief=element.Relief, font=font,
                                                        tickinterval=element.TickInterval,
                                                        command=element._SliderChangedHandler)
                else:
                    tkscale = element.Widget = tk.Scale(tk_row_frame, orient=element.Orientation,
                                                        variable=element.TKIntVar,
                                                        from_=range_from, to_=range_to, resolution=element.Resolution,
                                                        length=slider_length, width=slider_width,
                                                        bd=element.BorderWidth,
                                                        relief=element.Relief, font=font,
                                                        tickinterval=element.TickInterval)
                tkscale.config(highlightthickness=0)
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    tkscale.configure(background=element.BackgroundColor)
                if element.TroughColor != COLOR_SYSTEM_DEFAULT:
                    tkscale.config(troughcolor=element.TroughColor)
                if element.DisableNumericDisplay:
                    tkscale.config(showvalue=0)
                if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
                    tkscale.configure(fg=text_color)
                tkscale.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1])
                if element.Visible is False:
                    tkscale.pack_forget()
                element.TKScale = tkscale
                if element.Disabled == True:
                    element.TKScale['state'] = 'disabled'
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element.TKScale, text=element.Tooltip, timeout=DEFAULT_TOOLTIP_TIME)
            # -------------------------  TABLE placement element  ------------------------- #
            elif element_type == ELEM_TYPE_TABLE:
                element = element  # type: Table
                frame = tk.Frame(tk_row_frame)
                element.table_frame = frame
                height = element.NumRows
                if element.Justification.startswith('l'):
                    anchor = tk.W
                elif element.Justification.startswith('r'):
                    anchor = tk.E
                else:
                    anchor = tk.CENTER
                column_widths = {}
                # create column width list
                for row in element.Values:
                    for i, col in enumerate(row):
                        col_width = min(len(str(col)), element.MaxColumnWidth)
                        try:
                            if col_width > column_widths[i]:
                                column_widths[i] = col_width
                        except:
                            column_widths[i] = col_width

                if element.ColumnsToDisplay is None:
                    displaycolumns = element.ColumnHeadings if element.ColumnHeadings is not None else element.Values[0]
                else:
                    displaycolumns = []
                    for i, should_display in enumerate(element.ColumnsToDisplay):
                        if should_display:
                            if element.ColumnHeadings is not None:
                                displaycolumns.append(element.ColumnHeadings[i])
                            else:
                                displaycolumns.append(str(i))

                column_headings = element.ColumnHeadings if element.ColumnHeadings is not None else displaycolumns
                if element.DisplayRowNumbers:  # if display row number, tack on the numbers to front of columns
                    displaycolumns = [element.RowHeaderText, ] + displaycolumns
                    if column_headings is not None:
                        column_headings = [element.RowHeaderText, ] + element.ColumnHeadings
                    else:
                        column_headings = [element.RowHeaderText, ] + displaycolumns
                element.TKTreeview = element.Widget = ttk.Treeview(frame, columns=column_headings,
                                                                   displaycolumns=displaycolumns, show='headings',
                                                                   height=height,
                                                                   selectmode=element.SelectMode, )
                treeview = element.TKTreeview
                if element.DisplayRowNumbers:
                    treeview.heading(element.RowHeaderText, text=element.RowHeaderText)  # make a dummy heading
                    treeview.column(element.RowHeaderText, width=_string_width_in_pixels(font, element.RowHeaderText)+10, minwidth=10, anchor=anchor, stretch=0)

                headings = element.ColumnHeadings if element.ColumnHeadings is not None else element.Values[0]
                for i, heading in enumerate(headings):
                    treeview.heading(heading, text=heading)
                    if element.AutoSizeColumns:
                        width = max(column_widths[i], len(heading))  * _char_width_in_pixels(font)
                    else:
                        try:
                            width = element.ColumnWidths[i] * _char_width_in_pixels(font)
                        except:
                            width = element.DefaultColumnWidth * _char_width_in_pixels(font)
                    treeview.column(heading, width=width, minwidth=10, anchor=anchor, stretch=0)
                # Insert values into the tree
                for i, value in enumerate(element.Values):
                    if element.DisplayRowNumbers:
                        value = [i + element.StartingRowNumber] + value
                    id = treeview.insert('', 'end', text=value, iid=i + 1, values=value, tag=i)
                    element.tree_ids.append(id)
                if element.AlternatingRowColor is not None:  # alternating colors
                    for row in range(0, len(element.Values), 2):
                        treeview.tag_configure(row, background=element.AlternatingRowColor)
                if element.RowColors is not None:  # individual row colors
                    for row_def in element.RowColors:
                        if len(row_def) == 2:  # only background is specified
                            treeview.tag_configure(row_def[0], background=row_def[1])
                        else:
                            treeview.tag_configure(row_def[0], background=row_def[2], foreground=row_def[1])
                # ------ Do Styling of Colors -----
                style_name = str(element.Key) + 'customtable.Treeview'
                table_style = ttk.Style()
                table_style.theme_use(toplevel_form.TtkTheme)
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    table_style.configure(style_name, background=element.BackgroundColor, fieldbackground=element.BackgroundColor)
                if element.TextColor is not None and element.TextColor != COLOR_SYSTEM_DEFAULT:
                    table_style.configure(style_name, foreground=element.TextColor)
                if element.RowHeight is not None:
                    table_style.configure(style_name, rowheight=element.RowHeight)
                else:
                    table_style.configure(style_name, rowheight=_char_height_in_pixels(font))
                if element.HeaderTextColor is not None and element.HeaderTextColor != COLOR_SYSTEM_DEFAULT:
                    table_style.configure(style_name+'.Heading', foreground=element.HeaderTextColor)
                if element.HeaderBackgroundColor is not None and element.HeaderBackgroundColor != COLOR_SYSTEM_DEFAULT:
                    table_style.configure(style_name+'.Heading', background=element.HeaderBackgroundColor)
                if element.HeaderFont is not None:
                    table_style.configure(style_name+'.Heading', font=element.HeaderFont)
                else:
                    table_style.configure(style_name+'.Heading', font=font)
                table_style.configure(style_name, font=font)
                treeview.configure(style=style_name)

                # scrollable_frame.pack(side=tk.LEFT,  padx=elementpad[0], pady=elementpad[1], expand=True, fill='both')
                treeview.bind("<<TreeviewSelect>>", element._treeview_selected)
                if element.BindReturnKey:
                    treeview.bind('<Return>', element._treeview_double_click)
                    treeview.bind('<Double-Button-1>', element._treeview_double_click)

                if not element.HideVerticalScroll:
                    scrollbar = tk.Scrollbar(frame)
                    scrollbar.pack(side=tk.RIGHT, fill='y')
                    scrollbar.config(command=treeview.yview)
                    treeview.configure(yscrollcommand=scrollbar.set)

                if not element.VerticalScrollOnly:
                    hscrollbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
                    hscrollbar.pack(side=tk.BOTTOM, fill='x')
                    hscrollbar.config(command=treeview.xview)
                    treeview.configure(xscrollcommand=hscrollbar.set)

                element.TKTreeview.pack(side=tk.LEFT, expand=True, padx=0, pady=0, fill='both')
                if element.Visible is False:
                    element.TKTreeview.pack_forget()
                frame.pack(side=tk.LEFT, expand=True, padx=0, pady=0)
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element.TKTreeview, text=element.Tooltip,
                                                    timeout=DEFAULT_TOOLTIP_TIME)
                if element.RightClickMenu or toplevel_form.RightClickMenu:
                    menu = element.RightClickMenu or toplevel_form.RightClickMenu
                    top_menu = tk.Menu(toplevel_form.TKroot, tearoff=False)
                    AddMenuItem(top_menu, menu[1], element)
                    element.TKRightClickMenu = top_menu
                    element.TKTreeview.bind('<Button-3>', element._RightClickMenuCallback)
            # -------------------------  Tree placement element  ------------------------- #
            elif element_type == ELEM_TYPE_TREE:
                element = element  # type: Tree
                frame = tk.Frame(tk_row_frame)

                height = element.NumRows
                if element.Justification.startswith('l'):  # justification
                    anchor = tk.W
                elif element.Justification.startswith('r'):
                    anchor = tk.E
                else:
                    anchor = tk.CENTER

                if element.ColumnsToDisplay is None:  # Which cols to display
                    displaycolumns = element.ColumnHeadings
                else:
                    displaycolumns = []
                    for i, should_display in enumerate(element.ColumnsToDisplay):
                        if should_display:
                            displaycolumns.append(element.ColumnHeadings[i])
                column_headings = element.ColumnHeadings
                # ------------- GET THE TREEVIEW WIDGET -------------
                element.TKTreeview = element.Widget = ttk.Treeview(frame, columns=column_headings,
                                                                   displaycolumns=displaycolumns, show='tree headings',
                                                                   height=height,
                                                                   selectmode=element.SelectMode)
                treeview = element.TKTreeview
                for i, heading in enumerate(element.ColumnHeadings):  # Configure cols + headings
                    treeview.heading(heading, text=heading)
                    if element.AutoSizeColumns:
                        width = min(element.MaxColumnWidth, len(heading) + 1)
                    else:
                        try:
                            width = element.ColumnWidths[i]
                        except:
                            width = element.DefaultColumnWidth
                    treeview.column(heading, width=width * _char_width_in_pixels(font)+ 10, anchor=anchor)
                def add_treeview_data(node):
                    """

                    :param node:

                    """
                    # print(f'Inserting {node.key} under parent {node.parent}')
                    if node.key != '':
                        if node.icon:
                            if type(node.icon) is bytes:
                                photo = tk.PhotoImage(data=node.icon)
                            else:
                                photo = tk.PhotoImage(file=node.icon)
                            node.photo = photo
                            id = treeview.insert(element.KeyToID[node.parent], 'end', iid=None, text=node.text, values=node.values,
                                                 open=element.ShowExpanded, image=node.photo)
                            element.IdToKey[id] = node.key
                            element.KeyToID[node.key] = id
                        else:
                            id = treeview.insert(element.KeyToID[node.parent], 'end', iid=None, text=node.text, values=node.values,
                                                 open=element.ShowExpanded)
                            element.IdToKey[id] = node.key
                            element.KeyToID[node.key] = id

                    for node in node.children:
                        add_treeview_data(node)

                add_treeview_data(element.TreeData.root_node)
                treeview.column('#0', width=element.Col0Width * _char_width_in_pixels(font), anchor=anchor)
                # ----- configure colors -----
                style_name = str(element.Key) + '.Treeview'
                tree_style = ttk.Style()
                tree_style.theme_use(toplevel_form.TtkTheme)
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    tree_style.configure(style_name, background=element.BackgroundColor,
                                         fieldbackground=element.BackgroundColor)
                if element.TextColor is not None and element.TextColor != COLOR_SYSTEM_DEFAULT:
                    tree_style.configure(style_name, foreground=element.TextColor)
                if element.HeaderTextColor is not None and element.HeaderTextColor != COLOR_SYSTEM_DEFAULT:
                    tree_style.configure(style_name+'.Heading', foreground=element.HeaderTextColor)
                if element.HeaderBackgroundColor is not None and element.HeaderBackgroundColor != COLOR_SYSTEM_DEFAULT:
                    tree_style.configure(style_name+'.Heading', background=element.HeaderBackgroundColor)
                if element.HeaderFont is not None:
                    tree_style.configure(style_name+'.Heading', font=element.HeaderFont)
                else:
                    tree_style.configure(style_name+'.Heading', font=font)
                tree_style.configure(style_name, font=font)
                if element.RowHeight:
                    tree_style.configure(style_name, rowheight=element.RowHeight)
                treeview.configure(style=style_name)  # IMPORTANT! Be sure and set the style name for this widget
                scrollbar = tk.Scrollbar(frame)
                scrollbar.pack(side=tk.RIGHT, fill='y')
                scrollbar.config(command=treeview.yview)
                treeview.configure(yscrollcommand=scrollbar.set)
                element.TKTreeview.pack(side=tk.LEFT, expand=True, padx=0, pady=0, fill='both')
                if element.Visible is False:
                    element.TKTreeview.pack_forget()
                frame.pack(side=tk.LEFT, expand=True, padx=0, pady=0)
                treeview.bind("<<TreeviewSelect>>", element._treeview_selected)
                if element.Tooltip is not None:  # tooltip
                    element.TooltipObject = ToolTip(element.TKTreeview, text=element.Tooltip,
                                                    timeout=DEFAULT_TOOLTIP_TIME)
                if element.RightClickMenu or toplevel_form.RightClickMenu:
                    menu = element.RightClickMenu or toplevel_form.RightClickMenu
                    top_menu = tk.Menu(toplevel_form.TKroot, tearoff=False)
                    AddMenuItem(top_menu, menu[1], element)
                    element.TKRightClickMenu = top_menu
                    element.TKTreeview.bind('<Button-3>', element._RightClickMenuCallback)
            # -------------------------  Separator placement element  ------------------------- #
            elif element_type == ELEM_TYPE_SEPARATOR:
                element = element  # type: VerticalSeparator
                separator = element.Widget = ttk.Separator(tk_row_frame, orient=element.Orientation, )
                separator.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1], fill='both', expand=True)
            # -------------------------  StatusBar placement element  ------------------------- #
            elif element_type == ELEM_TYPE_STATUSBAR:
                # auto_size_text = element.AutoSizeText
                display_text = element.DisplayText  # text to display
                if auto_size_text is False:
                    width, height = element_size
                else:
                    lines = display_text.split('\n')
                    max_line_len = max([len(l) for l in lines])
                    num_lines = len(lines)
                    if max_line_len > element_size[0]:  # if text exceeds element size, the will have to wrap
                        width = element_size[0]
                    else:
                        width = max_line_len
                    height = num_lines
                # ---===--- LABEL widget create and place --- #
                stringvar = tk.StringVar()
                element.TKStringVar = stringvar
                stringvar.set(display_text)
                if auto_size_text:
                    width = 0
                if element.Justification is not None:
                    justification = element.Justification
                elif toplevel_form.TextJustification is not None:
                    justification = toplevel_form.TextJustification
                else:
                    justification = DEFAULT_TEXT_JUSTIFICATION
                justify = tk.LEFT if justification.startswith('l') else tk.CENTER if justification.startswith('c') else tk.RIGHT
                anchor = tk.NW if justification.startswith('l') else tk.N if justification.startswith('c') else tk.NE
                # tktext_label = tk.Label(tk_row_frame, textvariable=stringvar, width=width, height=height,
                #                         justify=justify, bd=border_depth, font=font)
                tktext_label = element.Widget = tk.Label(tk_row_frame, textvariable=stringvar, width=width,
                                                         height=height,
                                                         justify=justify, bd=border_depth, font=font)
                # Set wrap-length for text (in PIXELS) == PAIN IN THE ASS
                wraplen = tktext_label.winfo_reqwidth() + 40  # width of widget in Pixels
                if not auto_size_text and height == 1:
                    wraplen = 0
                # print("wraplen, width, height", wraplen, width, height)
                tktext_label.configure(anchor=anchor, wraplen=wraplen)  # set wrap to width of widget
                if element.Relief is not None:
                    tktext_label.configure(relief=element.Relief)
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    tktext_label.configure(background=element.BackgroundColor)
                if element.TextColor != COLOR_SYSTEM_DEFAULT and element.TextColor is not None:
                    tktext_label.configure(fg=element.TextColor)
                tktext_label.pack(side=tk.LEFT, padx=elementpad[0], pady=elementpad[1], fill=tk.BOTH, expand=True)
                if element.Visible is False:
                    tktext_label.pack_forget()
                element.TKText = tktext_label
                if element.ClickSubmits:
                    tktext_label.bind('<Button-1>', element._TextClickedHandler)
                if element.Tooltip is not None:
                    element.TooltipObject = ToolTip(element.TKText, text=element.Tooltip, timeout=DEFAULT_TOOLTIP_TIME)

        # ............................DONE WITH ROW pack the row of widgets ..........................#
        # done with row, pack the row of widgets
        # tk_row_frame.grid(row=row_num+2, sticky=tk.NW, padx=DEFAULT_MARGINS[0])

        if row_justify.lower().startswith('c'):
            anchor = 'n'
            side = tk.CENTER
        elif row_justify.lower().startswith('r'):
            anchor = 'ne'
            side = tk.RIGHT
        elif row_justify.lower().startswith('l'):
            anchor = 'nw'
            side = tk.LEFT
        elif toplevel_form.ElementJustification.lower().startswith('c'):
            anchor = 'n'
            side = tk.TOP
        elif toplevel_form.ElementJustification.lower().startswith('r'):
            anchor = 'ne'
            side = tk.TOP
        else:
            anchor = 'nw'
            side = tk.TOP

        # row_should_expand = False

        tk_row_frame.pack(side=tk.TOP, anchor=anchor, padx=0, pady=0,
                          expand=row_should_expand, fill=tk.BOTH if row_should_expand else tk.NONE)
        if form.BackgroundColor is not None and form.BackgroundColor != COLOR_SYSTEM_DEFAULT:
            tk_row_frame.configure(background=form.BackgroundColor)
    return


def ConvertFlexToTK(MyFlexForm):
    """

    :param MyFlexForm: (Window)

    """
    master = MyFlexForm.TKroot
    master.title(MyFlexForm.Title)
    InitializeResults(MyFlexForm)
    try:
        if MyFlexForm.NoTitleBar:
            if sys.platform == 'linux':
                MyFlexForm.TKroot.wm_attributes("-type", "splash")
            else:
                MyFlexForm.TKroot.wm_overrideredirect(True)
    except:
        pass

    PackFormIntoFrame(MyFlexForm, master, MyFlexForm)

    MyFlexForm.TKroot.configure(padx=MyFlexForm.Margins[0], pady=MyFlexForm.Margins[1])

    # ....................................... DONE creating and laying out window ..........................#
    if MyFlexForm._Size != (None, None):
        master.geometry("%sx%s" % (MyFlexForm._Size[0], MyFlexForm._Size[1]))
    screen_width = master.winfo_screenwidth()  # get window info to move to middle of screen
    screen_height = master.winfo_screenheight()
    if MyFlexForm.Location != (None, None):
        x, y = MyFlexForm.Location
    elif DEFAULT_WINDOW_LOCATION != (None, None):
        x, y = DEFAULT_WINDOW_LOCATION
    else:
        master.update_idletasks()  # don't forget to do updates or values are bad
        win_width = master.winfo_width()
        win_height = master.winfo_height()
        x = screen_width / 2 - win_width / 2
        y = screen_height / 2 - win_height / 2
        if y + win_height > screen_height:
            y = screen_height - win_height
        if x + win_width > screen_width:
            x = screen_width - win_width

    move_string = '+%i+%i' % (int(x), int(y))
    master.geometry(move_string)

    master.update_idletasks()  # don't forget

    return


# ----====----====----====----====----==== STARTUP TK ====----====----====----====----====----#
def StartupTK(my_flex_form):
    """
    NOT user callable
    Creates the window (for real) lays out all the elements, etc.  It's a HUGE set of things it does.  It's the basic
    "porting layer" that will change depending on the GUI framework PySimpleGUI is running on top of.

    :param my_flex_form: (Window):

    """
    my_flex_form = my_flex_form  # type: Window
    # global _my_windows
    # ow = _my_windows.NumOpenWindows
    ow = Window.NumOpenWindows
    # print('Starting TK open Windows = {}'.format(ow))
    if ENABLE_TK_WINDOWS:
        root = tk.Tk()
    elif not ow and not my_flex_form.ForceTopLevel:
        # if first window being created, make a throwaway, hidden master root.  This stops one user
        # window from becoming the child of another user window. All windows are children of this
        # hidden window
        Window._IncrementOpenCount()
        Window.hidden_master_root = tk.Tk()
        Window.hidden_master_root.attributes('-alpha', 0)  # HIDE this window really really really
        Window.hidden_master_root.wm_overrideredirect(True)
        Window.hidden_master_root.withdraw()
        root = tk.Toplevel()
    else:
        root = tk.Toplevel()

    if my_flex_form.DebuggerEnabled:
        root.bind('<Cancel>', my_flex_form._callback_main_debugger_window_create_keystroke)
        root.bind('<Pause>', my_flex_form._callback_popout_window_create_keystroke)

        # root.bind('<Cancel>', Debugger._build_main_debugger_window)
        # root.bind('<Pause>', Debugger._build_floating_window)
    try:
        root.attributes('-alpha', 0)  # hide window while building it. makes for smoother 'paint'
    except:
        pass
    if my_flex_form.BackgroundColor is not None and my_flex_form.BackgroundColor != COLOR_SYSTEM_DEFAULT:
        root.configure(background=my_flex_form.BackgroundColor)
    Window._IncrementOpenCount()

    my_flex_form.TKroot = root
    # Make moveable window
    if (my_flex_form.GrabAnywhere is not False and not (
            my_flex_form.NonBlocking and my_flex_form.GrabAnywhere is not True)):
        root.bind("<ButtonPress-1>", my_flex_form._StartMove)
        root.bind("<ButtonRelease-1>", my_flex_form._StopMove)
        root.bind("<B1-Motion>", my_flex_form._OnMotion)

    if not my_flex_form.Resizable:
        root.resizable(False, False)

    if my_flex_form.DisableMinimize:
        root.attributes("-toolwindow", 1)

    if my_flex_form.KeepOnTop:
        root.wm_attributes("-topmost", 1)

    if my_flex_form.TransparentColor is not None:
        my_flex_form.SetTransparentColor(my_flex_form.TransparentColor)

    # root.protocol("WM_DELETE_WINDOW", MyFlexForm.DestroyedCallback())
    # root.bind('<Destroy>', MyFlexForm.DestroyedCallback())
    ConvertFlexToTK(my_flex_form)

    my_flex_form.SetIcon(my_flex_form.WindowIcon)

    try:
        root.attributes('-alpha',
                        1 if my_flex_form.AlphaChannel is None else my_flex_form.AlphaChannel)  # Make window visible again
    except:
        pass

    if my_flex_form.ReturnKeyboardEvents and not my_flex_form.NonBlocking:
        root.bind("<KeyRelease>", my_flex_form._KeyboardCallback)
        root.bind("<MouseWheel>", my_flex_form._MouseWheelCallback)
    elif my_flex_form.ReturnKeyboardEvents:
        root.bind("<Key>", my_flex_form._KeyboardCallback)
        root.bind("<MouseWheel>", my_flex_form._MouseWheelCallback)

    if my_flex_form.AutoClose:
        duration = DEFAULT_AUTOCLOSE_TIME if my_flex_form.AutoCloseDuration is None else my_flex_form.AutoCloseDuration
        my_flex_form.TKAfterID = root.after(int(duration * 1000), my_flex_form._AutoCloseAlarmCallback)

    if my_flex_form.Timeout != None:
        my_flex_form.TKAfterID = root.after(int(my_flex_form.Timeout), my_flex_form._TimeoutAlarmCallback)
    if my_flex_form.NonBlocking:
        my_flex_form.TKroot.protocol("WM_DESTROY_WINDOW", my_flex_form._OnClosingCallback)
        my_flex_form.TKroot.protocol("WM_DELETE_WINDOW", my_flex_form._OnClosingCallback)
    else:  # it's a blocking form
        # print('..... CALLING MainLoop')
        my_flex_form.CurrentlyRunningMainloop = True
        my_flex_form.TKroot.protocol("WM_DESTROY_WINDOW", my_flex_form._OnClosingCallback)
        my_flex_form.TKroot.protocol("WM_DELETE_WINDOW", my_flex_form._OnClosingCallback)
        my_flex_form.TKroot.mainloop()
        my_flex_form.CurrentlyRunningMainloop = False
        my_flex_form.TimerCancelled = True
        # print('..... BACK from MainLoop')
        if not my_flex_form.FormRemainedOpen:
            Window._DecrementOpenCount()
            # _my_windows.Decrement()
        if my_flex_form.RootNeedsDestroying:
            try:
                my_flex_form.TKroot.destroy()
            except:
                pass
            my_flex_form.RootNeedsDestroying = False
    return


# ==============================_GetNumLinesNeeded ==#
# Helper function for determining how to wrap text   #
# ===================================================#
def _GetNumLinesNeeded(text, max_line_width):
    if max_line_width == 0:
        return 1
    lines = text.split('\n')
    num_lines = len(lines)  # number of original lines of text
    max_line_len = max([len(l) for l in lines])  # longest line
    lines_used = []
    for L in lines:
        lines_used.append(len(L) // max_line_width + (len(L) % max_line_width > 0))  # fancy math to round up
    total_lines_needed = sum(lines_used)
    return total_lines_needed


# ==============================  PROGRESS METER ========================================== #

def ConvertArgsToSingleString(*args):
    """

    :param *args:

    """
    max_line_total, width_used, total_lines, = 0, 0, 0
    single_line_message = ''
    # loop through args and built a SINGLE string from them
    for message in args:
        # fancy code to check if string and convert if not is not need. Just always convert to string :-)
        # if not isinstance(message, str): message = str(message)
        message = str(message)
        longest_line_len = max([len(l) for l in message.split('\n')])
        width_used = max(longest_line_len, width_used)
        max_line_total = max(max_line_total, width_used)
        lines_needed = _GetNumLinesNeeded(message, width_used)
        total_lines += lines_needed
        single_line_message += message + '\n'
    return single_line_message, width_used, total_lines


METER_REASON_CANCELLED = 'cancelled'
METER_REASON_CLOSED = 'closed'
METER_REASON_REACHED_MAX = 'finished'
METER_OK = True
METER_STOPPED = False


class QuickMeter(object):
    active_meters = {}
    exit_reasons = {}

    def __init__(self, title, current_value, max_value, key, *args, orientation='v', bar_color=(None, None), button_color=(None, None), size=DEFAULT_PROGRESS_BAR_SIZE, border_width=None, grab_anywhere=False, no_titlebar=False):
        """

        :param title: text to display in eleemnt
        :type title: (str)
        :param current_value: current value
        :type current_value: (int)
        :param max_value: max value of QuickMeter
        :type max_value: (int)
        :param key:  Used with window.FindElement and with return values to uniquely identify this element
        :type key: Union[str, int, tuple]
        :param *args: stuff to output
        :type *args: (Any)
        :param orientation:  'horizontal' or 'vertical' ('h' or 'v' work) (Default value = 'vertical' / 'v')
        :type orientation: (str)
        :param bar_color:  color of a bar line
        :type bar_color: str
        :param button_color: button color (foreground, background)
        :type button_color: Tuple[str, str]
        :param size:  (w,h) w=characters-wide, h=rows-high (Default value = DEFAULT_PROGRESS_BAR_SIZE)
        :type size: Tuple[int, int]
        :param border_width:  width of border around element
        :type border_width: (int)
        :param grab_anywhere: If True: can grab anywhere to move the window (Default = False)
        :type grab_anywhere: (bool)
        :param no_titlebar: If True: window will be created without a titlebar
        :type no_titlebar: (bool)
        """
        self.start_time = datetime.datetime.utcnow()
        self.key = key
        self.orientation = orientation
        self.bar_color = bar_color
        self.size = size
        self.grab_anywhere = grab_anywhere
        self.button_color = button_color
        self.border_width = border_width
        self.no_titlebar = no_titlebar
        self.title = title
        self.current_value = current_value
        self.max_value = max_value
        self.close_reason = None
        self.window = self.BuildWindow(*args)

    def BuildWindow(self, *args):
        layout = []
        if self.orientation.lower().startswith('h'):
            col = []
            col += [[T(''.join(map(lambda x: str(x) + '\n', args)),
                       key='_OPTMSG_')]]  ### convert all *args into one string that can be updated
            col += [[T('', size=(30, 10), key='_STATS_')],
                    [ProgressBar(max_value=self.max_value, orientation='h', key='_PROG_', size=self.size,
                                 bar_color=self.bar_color)],
                    [Cancel(button_color=self.button_color), Stretch()]]
            layout = [Column(col)]
        else:
            col = [[ProgressBar(max_value=self.max_value, orientation='v', key='_PROG_', size=self.size,
                                bar_color=self.bar_color)]]
            col2 = []
            col2 += [[T(''.join(map(lambda x: str(x) + '\n', args)),
                        key='_OPTMSG_')]]  ### convert all *args into one string that can be updated
            col2 += [[T('', size=(30, 10), key='_STATS_')],
                     [Cancel(button_color=self.button_color), Stretch()]]
            layout = [Column(col), Column(col2)]
        self.window = Window(self.title, grab_anywhere=self.grab_anywhere, border_depth=self.border_width, no_titlebar=self.no_titlebar)
        self.window.Layout([layout]).Finalize()

        return self.window

    def UpdateMeter(self, current_value, max_value, *args):  ### support for *args when updating

        self.current_value = current_value
        self.max_value = max_value
        self.window.Element('_PROG_').UpdateBar(self.current_value, self.max_value)
        self.window.Element('_STATS_').Update('\n'.join(self.ComputeProgressStats()))
        self.window.Element('_OPTMSG_').Update(
            value=''.join(map(lambda x: str(x) + '\n', args)))  ###  update the string with the args
        event, values = self.window.Read(timeout=0)
        if event in ('Cancel', None) or current_value >= max_value:
            self.window.Close()
            del (QuickMeter.active_meters[self.key])
            QuickMeter.exit_reasons[
                self.key] = METER_REASON_CANCELLED if event == 'Cancel' else METER_REASON_CLOSED if event is None else METER_REASON_REACHED_MAX
            return QuickMeter.exit_reasons[self.key]
        return METER_OK

    def ComputeProgressStats(self):
        utc = datetime.datetime.utcnow()
        time_delta = utc - self.start_time
        total_seconds = time_delta.total_seconds()
        if not total_seconds:
            total_seconds = 1
        try:
            time_per_item = total_seconds / self.current_value
        except:
            time_per_item = 1
        seconds_remaining = (self.max_value - self.current_value) * time_per_item
        time_remaining = str(datetime.timedelta(seconds=seconds_remaining))
        time_remaining_short = (time_remaining).split(".")[0]
        time_delta_short = str(time_delta).split(".")[0]
        total_time = time_delta + datetime.timedelta(seconds=seconds_remaining)
        total_time_short = str(total_time).split(".")[0]
        self.stat_messages = [
            '{} of {}'.format(self.current_value, self.max_value),
            '{} %'.format(100 * self.current_value // self.max_value),
            '',
            ' {:6.2f} Iterations per Second'.format(self.current_value / total_seconds),
            ' {:6.2f} Seconds per Iteration'.format(total_seconds / (self.current_value if self.current_value else 1)),
            '',
            '{} Elapsed Time'.format(time_delta_short),
            '{} Time Remaining'.format(time_remaining_short),
            '{} Estimated Total Time'.format(total_time_short)]
        return self.stat_messages


def OneLineProgressMeter(title, current_value, max_value, key, *args, orientation='v', bar_color=(None, None), button_color=None, size=DEFAULT_PROGRESS_BAR_SIZE, border_width=None, grab_anywhere=False, no_titlebar=False):
    """
    :param title: text to display in eleemnt
    :type title: (str)
    :param current_value: current value
    :type current_value: (int)
    :param max_value: max value of QuickMeter
    :type max_value: (int)
    :param key:  Used with window.FindElement and with return values to uniquely identify this element
    :type key: Union[str, int, tuple]
    :param *args: stuff to output
    :type *args: (Any)
    :param orientation:  'horizontal' or 'vertical' ('h' or 'v' work) (Default value = 'vertical' / 'v')
    :type orientation: (str)
    :param bar_color:  color of a bar line
    :type bar_color: Tuple(str, str)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param size:  (w,h) w=characters-wide, h=rows-high (Default value = DEFAULT_PROGRESS_BAR_SIZE)
    :type size: Tuple[int, int]
    :param border_width:  width of border around element
    :type border_width: (int)
    :param grab_anywhere: If True: can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param no_titlebar: If True: no titlebar will be shown on the window
    :type no_titlebar: (bool)
    :return: True if updated successfully. False if user closed the meter with the X or Cancel button
    :rtype: (bool)
    """
    if key not in QuickMeter.active_meters:
        meter = QuickMeter(title, current_value, max_value, key, *args, orientation=orientation, bar_color=bar_color, button_color=button_color, size=size, border_width=border_width, grab_anywhere=grab_anywhere, no_titlebar=no_titlebar)
        QuickMeter.active_meters[key] = meter
    else:
        meter = QuickMeter.active_meters[key]

    rc = meter.UpdateMeter(current_value, max_value, *args)  ### pass the *args to to UpdateMeter function
    OneLineProgressMeter.exit_reasons = getattr(OneLineProgressMeter, 'exit_reasons', QuickMeter.exit_reasons)
    return rc == METER_OK


def OneLineProgressMeterCancel(key):
    """
    Cancels and closes a previously created One Line Progress Meter window

    :param key:  Key used when meter was created
    :type key: (Any)
    """
    try:
        meter = QuickMeter.active_meters[key]
        meter.window.Close()
        del (QuickMeter.active_meters[key])
        QuickMeter.exit_reasons[key] = METER_REASON_CANCELLED
    except:  # meter is already deleted
        return


# input is #RRGGBB
# output is #RRGGBB
def GetComplimentaryHex(color):
    # strip the # from the beginning
    color = color[1:]
    # convert the string into hex
    color = int(color, 16)
    # invert the three bytes
    # as good as substracting each of RGB component by 255(FF)
    comp_color = 0xFFFFFF ^ color
    # convert the color back to hex by prefixing a #
    comp_color = "#%06X" % comp_color
    return comp_color


# ========================  EasyPrint           =====#
# ===================================================#
class _DebugWin():
    debug_window = None

    def __init__(self, size=(None, None), location=(None, None), font=None, no_titlebar=False, no_button=False,
                 grab_anywhere=False, keep_on_top=False, do_not_reroute_stdout=True):
        """

        :param size:  (w,h) w=characters-wide, h=rows-high
        :type size: Tuple[int, int]
        :param location:  Location of upper left corner of the window
        :type location: Tuple[int, int]
        :param font:  specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param no_titlebar: If True no titlebar will be shown
        :type no_titlebar: (bool)

        :param no_button: show button
        :type no_button: (bool)

        :param grab_anywhere: If True: can grab anywhere to move the window (Default = False)
        :type grab_anywhere: (bool)

        :param location:  Location of upper left corner of the window
        :type location: Tuple[int, int]
        :param do_not_reroute_stdout: ??? (Default = True)
        :type do_not_reroute_stdout: (bool)

        """
        # Show a form that's a running counter
        self.size = size
        self.location = location
        self.font = font
        self.no_titlebar = no_titlebar
        self.no_button = no_button
        self.grab_anywhere = grab_anywhere
        self.keep_on_top = keep_on_top
        self.do_not_reroute_stdout = do_not_reroute_stdout

        win_size = size if size != (None, None) else DEFAULT_DEBUG_WINDOW_SIZE
        self.output_element = Multiline(size=win_size, autoscroll=True,
                                        key='_MULTILINE_') if do_not_reroute_stdout else Output(size=win_size)
        if no_button:
            self.layout = [[self.output_element]]
        else:
            self.layout = [ [self.output_element],
                            [DummyButton('Quit'), Stretch()]]

        self.window = Window('Debug Window', self.layout, no_titlebar=no_titlebar, auto_size_text=True, location=location,
                             font=font or ('Courier New', 10), grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, finalize=False)
        # self.window.NonBlocking = True        # if finalizing this window, then need to uncommment this line
        return

    def Print(self, *args, end=None, sep=None, text_color=None, background_color=None):
        sepchar = sep if sep is not None else ' '
        endchar = end if end is not None else '\n'

        if self.window is None:  # if window was destroyed alread re-open it
            self.__init__(size=self.size, location=self.location, font=self.font, no_titlebar=self.no_titlebar,
                          no_button=self.no_button, grab_anywhere=self.grab_anywhere, keep_on_top=self.keep_on_top,
                          do_not_reroute_stdout=self.do_not_reroute_stdout)
        event, values = self.window.Read(timeout=0)
        if event == 'Quit' or event is None:
            self.Close()
            self.__init__(size=self.size, location=self.location, font=self.font, no_titlebar=self.no_titlebar,
                          no_button=self.no_button, grab_anywhere=self.grab_anywhere, keep_on_top=self.keep_on_top,
                          do_not_reroute_stdout=self.do_not_reroute_stdout)
            event, values = self.window.Read(timeout=0)
        # print(f'Printing {ObjToStringSingleObj(self.output_element)}')
        if self.do_not_reroute_stdout:
            end_str = str(end) if end is not None else '\n'
            sep_str = str(sep) if sep is not None else ' '

            outstring = ''
            num_args = len(args)
            for i, arg in enumerate(args):
                outstring += str(arg)
                if i != num_args - 1:
                    outstring += sep_str
            outstring += end_str

            self.output_element.Update(outstring, append=True, text_color_for_value=text_color, background_color_for_value=background_color)
        else:
            print(*args, sep=sepchar, end=endchar)

    def Close(self):
        if self.window.XFound:             # increment the number of open windows to get around a bug with debug windows
            Window._IncrementOpenCount()
        self.window.Close()
        self.window = None


def PrintClose():
    """
    Close a previously opened EasyPrint window
    """
    EasyPrintClose()


def EasyPrint(*args, size=(None, None), end=None, sep=None, location=(None, None), font=None, no_titlebar=False,
              no_button=False, grab_anywhere=False, keep_on_top=False, do_not_reroute_stdout=True, text_color=None, background_color=None):
    """
    Works like a "print" statement but with windowing options.  Routes output to the "Debug Window"

    :param *args: stuff to output
    :type *args: (Any)
    :param size: (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param sep: end character
    :type end: (str)
    :param sep: separator character
    :type sep: (str)
    :param location:  Location of upper left corner of the window
    :type location: Tuple[int, int]
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param no_button: don't show button
    :type no_button: (bool)
    :param grab_anywhere: If True: can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location:  Location of upper left corner of the window
    :type location: Tuple[int, int]
    :param do_not_reroute_stdout: do not reroute stdout
    :type do_not_reroute_stdout: (bool)
    """
    if _DebugWin.debug_window is None:
        _DebugWin.debug_window = _DebugWin(size=size, location=location, font=font, no_titlebar=no_titlebar,
                                           no_button=no_button, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top,
                                           do_not_reroute_stdout=do_not_reroute_stdout)
    _DebugWin.debug_window.Print(*args, end=end, sep=sep, text_color=text_color, background_color=background_color)


Print = EasyPrint
eprint = EasyPrint


def EasyPrintClose():
    """
    Close a previously opened EasyPrint window
    """
    if _DebugWin.debug_window is not None:
        _DebugWin.debug_window.Close()
        _DebugWin.debug_window = None

# ------------------------------------------------------------------------------------------------ #
# A print-like call that can be used to output to a multiline element as if it's an Output element #
# ------------------------------------------------------------------------------------------------ #

def _print_to_element(multiline_element, *args, end=None, sep=None, text_color=None, background_color=None):
    """
    Print like Python normally prints except route the output to a multline element and also add colors if desired

    :param multiline_element:  The multiline element to be output to
    :type multiline_element: (Multiline)
    :param args:  The arguments to print
    :type args: List[Any]
    :param end:  The end char to use just like print uses
    :type end: (str)
    :param sep:  The separation character like print uses
    :type sep: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param background_color: The background color of the line
    :type background_color: (str)
    """
    end_str = str(end) if end is not None else '\n'
    sep_str = str(sep) if sep is not None else ' '

    outstring = ''
    num_args = len(args)
    for i, arg in enumerate(args):
        outstring += str(arg)
        if i != num_args-1:
            outstring += sep_str
    outstring += end_str

    multiline_element.update(outstring, append=True, text_color_for_value=text_color, background_color_for_value=background_color)


# ============================== SetGlobalIcon ======#
# Sets the icon to be used by default                #
# ===================================================#
def SetGlobalIcon(icon):
    """
    Sets the icon which will be used any time a window is created if an icon is not provided when the
    window is created.

    :param icon: Union[bytes, str] Either a Base64 byte string or a filename
    """

    Window._user_defined_icon = icon


# ============================== SetOptions =========#
# Sets the icon to be used by default                #
# ===================================================#
def SetOptions(icon=None, button_color=None, element_size=(None, None), button_element_size=(None, None),
               margins=(None, None),
               element_padding=(None, None), auto_size_text=None, auto_size_buttons=None, font=None, border_width=None,
               slider_border_width=None, slider_relief=None, slider_orientation=None,
               autoclose_time=None, message_box_line_width=None,
               progress_meter_border_depth=None, progress_meter_style=None,
               progress_meter_relief=None, progress_meter_color=None, progress_meter_size=None,
               text_justification=None, background_color=None, element_background_color=None,
               text_element_background_color=None, input_elements_background_color=None, input_text_color=None,
               scrollbar_color=None, text_color=None, element_text_color=None, debug_win_size=(None, None),
               window_location=(None, None), error_button_color=(None, None), tooltip_time=None, use_ttk_buttons=None, ttk_theme=None):
    """
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param button_color: Color of the button (text, background)
    :type button_color: Tuple[str, str]
    :param element_size: element size (width, height) in characters
    :type element_size: Tuple[int, int]
    :param button_element_size: Size of button
    :type button_element_size: Tuple[int, int]
    :param margins: (left/right, top/bottom) tkinter margins around outsize. Amount of pixels to leave inside the window's frame around the edges before your elements are shown.
    :type margins: Tuple[int, int]
    :param element_padding: Default amount of padding to put around elements in window (left/right, top/bottom) or ((left, right), (top, bottom))
    :type element_padding: Tuple[int, int] or ((int, int),(int,int))
    :param auto_size_text: True if the Widget should be shrunk to exactly fit the number of chars to show
    :type auto_size_text: bool
    :param auto_size_buttons: True if Buttons in this Window should be sized to exactly fit the text on this.
    :type auto_size_buttons: (bool)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param border_width:  width of border around element
    :type border_width: (int)
    :param slider_border_width: ???
    :type slider_border_width: ???
    :param slider_relief: ???
    :type slider_relief: ???
    :param slider_orientation: ???
    :type slider_orientation: ???
    :param autoclose_time: ???
    :type autoclose_time: ???
    :param message_box_line_width: ???
    :type message_box_line_width: ???
    :param progress_meter_border_depth: ???
    :type progress_meter_border_depth: ???

    :param progress_meter_style:  You can no longer set a progress bar style. All ttk styles must be the same for the window
    :type progress_meter_style: ---

    :param progress_meter_relief:
    :param progress_meter_color:
    :param progress_meter_size:
    :param text_justification: Union ['left', 'right', 'center'] Default text justification for all Text Elements in window
    :type text_justification: (str)
    :param background_color: color of background
    :type background_color: (str)
    :param element_background_color: element background color
    :type element_background_color: (str)
    :param text_element_background_color: text element background color
    :type text_element_background_color: (str)
    :param input_elements_background_color:
    :param input_text_color:
    :param scrollbar_color:
    :param text_color: color of the text
    :type text_color: (str)
    :param element_text_color: ???
    :type element_text_color: ???
    :param debug_win_size:  (Default = (None))
    :type debug_win_size:  Tuple[int, int]
    :param window_location:  (Default = (None))
    :type window_location: ???
    :param error_button_color:  (Default = (None))
    :type error_button_color: ???
    :param tooltip_time:  time in milliseconds to wait before showing a tooltip. Default is 400ms
    :type tooltip_time: (int)
    :param use_ttk_buttons: if True will cause all buttons to be ttk buttons
    :type use_ttk_buttons: (bool)
    :param ttk_theme:  (str) Theme to use with ttk widgets.  Choices (on Windows) include - 'default', 'winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative'
    :type ttk_theme:  (str)
    ==============
    """
    global DEFAULT_ELEMENT_SIZE
    global DEFAULT_BUTTON_ELEMENT_SIZE
    global DEFAULT_MARGINS  # Margins for each LEFT/RIGHT margin is first term
    global DEFAULT_ELEMENT_PADDING  # Padding between elements (row, col) in pixels
    global DEFAULT_AUTOSIZE_TEXT
    global DEFAULT_AUTOSIZE_BUTTONS
    global DEFAULT_FONT
    global DEFAULT_BORDER_WIDTH
    global DEFAULT_AUTOCLOSE_TIME
    global DEFAULT_BUTTON_COLOR
    global MESSAGE_BOX_LINE_WIDTH
    global DEFAULT_PROGRESS_BAR_BORDER_WIDTH
    global DEFAULT_PROGRESS_BAR_STYLE
    global DEFAULT_PROGRESS_BAR_RELIEF
    global DEFAULT_PROGRESS_BAR_COLOR
    global DEFAULT_PROGRESS_BAR_SIZE
    global DEFAULT_TEXT_JUSTIFICATION
    global DEFAULT_DEBUG_WINDOW_SIZE
    global DEFAULT_SLIDER_BORDER_WIDTH
    global DEFAULT_SLIDER_RELIEF
    global DEFAULT_SLIDER_ORIENTATION
    global DEFAULT_BACKGROUND_COLOR
    global DEFAULT_INPUT_ELEMENTS_COLOR
    global DEFAULT_ELEMENT_BACKGROUND_COLOR
    global DEFAULT_TEXT_ELEMENT_BACKGROUND_COLOR
    global DEFAULT_SCROLLBAR_COLOR
    global DEFAULT_TEXT_COLOR
    global DEFAULT_WINDOW_LOCATION
    global DEFAULT_ELEMENT_TEXT_COLOR
    global DEFAULT_INPUT_TEXT_COLOR
    global DEFAULT_TOOLTIP_TIME
    global DEFAULT_ERROR_BUTTON_COLOR
    global DEFAULT_TTK_THEME
    global USE_TTK_BUTTONS
    # global _my_windows

    if icon:
        Window._user_defined_icon = icon
        # _my_windows._user_defined_icon = icon

    if button_color != None:
        DEFAULT_BUTTON_COLOR = button_color

    if element_size != (None, None):
        DEFAULT_ELEMENT_SIZE = element_size

    if button_element_size != (None, None):
        DEFAULT_BUTTON_ELEMENT_SIZE = button_element_size

    if margins != (None, None):
        DEFAULT_MARGINS = margins

    if element_padding != (None, None):
        DEFAULT_ELEMENT_PADDING = element_padding

    if auto_size_text != None:
        DEFAULT_AUTOSIZE_TEXT = auto_size_text

    if auto_size_buttons != None:
        DEFAULT_AUTOSIZE_BUTTONS = auto_size_buttons

    if font != None:
        DEFAULT_FONT = font

    if border_width != None:
        DEFAULT_BORDER_WIDTH = border_width

    if autoclose_time != None:
        DEFAULT_AUTOCLOSE_TIME = autoclose_time

    if message_box_line_width != None:
        MESSAGE_BOX_LINE_WIDTH = message_box_line_width

    if progress_meter_border_depth != None:
        DEFAULT_PROGRESS_BAR_BORDER_WIDTH = progress_meter_border_depth

    if progress_meter_style != None:
        warnings.warn('You can no longer set a progress bar style. All ttk styles must be the same for the window', UserWarning)
        # DEFAULT_PROGRESS_BAR_STYLE = progress_meter_style

    if progress_meter_relief != None:
        DEFAULT_PROGRESS_BAR_RELIEF = progress_meter_relief

    if progress_meter_color != None:
        DEFAULT_PROGRESS_BAR_COLOR = progress_meter_color

    if progress_meter_size != None:
        DEFAULT_PROGRESS_BAR_SIZE = progress_meter_size

    if slider_border_width != None:
        DEFAULT_SLIDER_BORDER_WIDTH = slider_border_width

    if slider_orientation != None:
        DEFAULT_SLIDER_ORIENTATION = slider_orientation

    if slider_relief != None:
        DEFAULT_SLIDER_RELIEF = slider_relief

    if text_justification != None:
        DEFAULT_TEXT_JUSTIFICATION = text_justification

    if background_color != None:
        DEFAULT_BACKGROUND_COLOR = background_color

    if text_element_background_color != None:
        DEFAULT_TEXT_ELEMENT_BACKGROUND_COLOR = text_element_background_color

    if input_elements_background_color != None:
        DEFAULT_INPUT_ELEMENTS_COLOR = input_elements_background_color

    if element_background_color != None:
        DEFAULT_ELEMENT_BACKGROUND_COLOR = element_background_color

    if window_location != (None, None):
        DEFAULT_WINDOW_LOCATION = window_location

    if debug_win_size != (None, None):
        DEFAULT_DEBUG_WINDOW_SIZE = debug_win_size

    if text_color != None:
        DEFAULT_TEXT_COLOR = text_color

    if scrollbar_color != None:
        DEFAULT_SCROLLBAR_COLOR = scrollbar_color

    if element_text_color != None:
        DEFAULT_ELEMENT_TEXT_COLOR = element_text_color

    if input_text_color is not None:
        DEFAULT_INPUT_TEXT_COLOR = input_text_color

    if tooltip_time is not None:
        DEFAULT_TOOLTIP_TIME = tooltip_time

    if error_button_color != (None, None):
        DEFAULT_ERROR_BUTTON_COLOR = error_button_color

    if ttk_theme is not None:
        DEFAULT_TTK_THEME = ttk_theme

    if use_ttk_buttons is not None:
        USE_TTK_BUTTONS = use_ttk_buttons

    return True

# ----------------------------------------------------------------- #

# .########.##.....##.########.##.....##.########..######.
# ....##....##.....##.##.......###...###.##.......##....##
# ....##....##.....##.##.......####.####.##.......##......
# ....##....#########.######...##.###.##.######....######.
# ....##....##.....##.##.......##.....##.##.............##
# ....##....##.....##.##.......##.....##.##.......##....##
# ....##....##.....##.########.##.....##.########..######.

# ----------------------------------------------------------------- #

# The official Theme code

#################### ChangeLookAndFeel #######################
# Predefined settings that will change the colors and styles #
# of the elements.                                           #
##############################################################
LOOK_AND_FEEL_TABLE = {'SystemDefault':
                           {'BACKGROUND': COLOR_SYSTEM_DEFAULT,
                            'TEXT': COLOR_SYSTEM_DEFAULT,
                            'INPUT': COLOR_SYSTEM_DEFAULT,
                            'TEXT_INPUT': COLOR_SYSTEM_DEFAULT,
                            'SCROLL': COLOR_SYSTEM_DEFAULT,
                            'BUTTON': OFFICIAL_PYSIMPLEGUI_BUTTON_COLOR,
                            'PROGRESS': COLOR_SYSTEM_DEFAULT,
                            'BORDER': 1, 'SLIDER_DEPTH': 1,
                            'PROGRESS_DEPTH': 0},

                       'SystemDefaultForReal':
                           {'BACKGROUND': COLOR_SYSTEM_DEFAULT,
                            'TEXT': COLOR_SYSTEM_DEFAULT,
                            'INPUT': COLOR_SYSTEM_DEFAULT,
                            'TEXT_INPUT': COLOR_SYSTEM_DEFAULT,
                            'SCROLL': COLOR_SYSTEM_DEFAULT,
                            'BUTTON': COLOR_SYSTEM_DEFAULT,
                            'PROGRESS': COLOR_SYSTEM_DEFAULT,
                            'BORDER': 1, 'SLIDER_DEPTH': 1,
                            'PROGRESS_DEPTH': 0},

                       'SystemDefault1':
                           {'BACKGROUND': COLOR_SYSTEM_DEFAULT,
                            'TEXT': COLOR_SYSTEM_DEFAULT,
                            'INPUT': COLOR_SYSTEM_DEFAULT,
                            'TEXT_INPUT': COLOR_SYSTEM_DEFAULT,
                            'SCROLL': COLOR_SYSTEM_DEFAULT,
                            'BUTTON': COLOR_SYSTEM_DEFAULT,
                            'PROGRESS': COLOR_SYSTEM_DEFAULT,
                            'BORDER': 1, 'SLIDER_DEPTH': 1,
                            'PROGRESS_DEPTH': 0},

                       'Material1': {'BACKGROUND': '#E3F2FD',
                                     'TEXT': '#000000',
                                     'INPUT': '#86A8FF',
                                     'TEXT_INPUT': '#000000',
                                     'SCROLL': '#86A8FF',
                                     'BUTTON': ('#FFFFFF', '#5079D3'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                     'BORDER': 0, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0,
                                     'ACCENT1': '#FF0266',
                                     'ACCENT2': '#FF5C93',
                                     'ACCENT3': '#C5003C'},

                       'Material2': {'BACKGROUND': '#FAFAFA',
                                     'TEXT': '#000000',
                                     'INPUT': '#004EA1',
                                     'TEXT_INPUT': '#FFFFFF',
                                     'SCROLL': '#5EA7FF',
                                     'BUTTON': ('#FFFFFF', '#0079D3'),  # based on Reddit color
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                     'BORDER': 0, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0,
                                     'ACCENT1': '#FF0266',
                                     'ACCENT2': '#FF5C93',
                                     'ACCENT3': '#C5003C'},

                       'Reddit': {'BACKGROUND': '#ffffff',
                                  'TEXT': '#1a1a1b',
                                  'INPUT': '#dae0e6',
                                  'TEXT_INPUT': '#222222',
                                  'SCROLL': '#a5a4a4',
                                  'BUTTON': ('#FFFFFF', '#0079d3'),
                                  'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                  'BORDER': 1,
                                  'SLIDER_DEPTH': 0,
                                  'PROGRESS_DEPTH': 0,
                                  'ACCENT1': '#ff5414',
                                  'ACCENT2': '#33a8ff',
                                  'ACCENT3': '#dbf0ff'},

                       'Topanga': {'BACKGROUND': '#282923',
                                   'TEXT': '#E7DB74',
                                   'INPUT': '#393a32',
                                   'TEXT_INPUT': '#E7C855',
                                   'SCROLL': '#E7C855',
                                   'BUTTON': ('#E7C855', '#284B5A'),
                                   'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                   'BORDER': 1,
                                   'SLIDER_DEPTH': 0,
                                   'PROGRESS_DEPTH': 0,
                                   'ACCENT1': '#c15226',
                                   'ACCENT2': '#7a4d5f',
                                   'ACCENT3': '#889743'},

                       'GreenTan': {'BACKGROUND': '#9FB8AD',
                                    'TEXT': COLOR_SYSTEM_DEFAULT,
                                    'INPUT': '#F7F3EC', 'TEXT_INPUT': '#000000',
                                    'SCROLL': '#F7F3EC',
                                    'BUTTON': ('#FFFFFF', '#475841'),
                                    'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                    'BORDER': 1, 'SLIDER_DEPTH': 0,
                                    'PROGRESS_DEPTH': 0},

                       'Dark': {'BACKGROUND': '#404040',
                                'TEXT': '#FFFFFF',
                                'INPUT': '#4D4D4D',
                                'TEXT_INPUT': '#FFFFFF',
                                'SCROLL': '#707070',
                                'BUTTON': ('#FFFFFF', '#004F00'),
                                'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                'BORDER': 1,
                                'SLIDER_DEPTH': 0,
                                'PROGRESS_DEPTH': 0},

                       'LightGreen': {'BACKGROUND': '#B7CECE',
                                      'TEXT': '#000000',
                                      'INPUT': '#FDFFF7',
                                      'TEXT_INPUT': '#000000',
                                      'SCROLL': '#FDFFF7',
                                      'BUTTON': ('#FFFFFF', '#658268'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                      'BORDER': 1,
                                      'SLIDER_DEPTH': 0,
                                      'ACCENT1': '#76506d',
                                      'ACCENT2': '#5148f1',
                                      'ACCENT3': '#0a1c84',
                                      'PROGRESS_DEPTH': 0},

                       'Dark2': {'BACKGROUND': '#404040',
                                 'TEXT': '#FFFFFF',
                                 'INPUT': '#FFFFFF',
                                 'TEXT_INPUT': '#000000',
                                 'SCROLL': '#707070',
                                 'BUTTON': ('#FFFFFF', '#004F00'),
                                 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                 'BORDER': 1,
                                 'SLIDER_DEPTH': 0,
                                 'PROGRESS_DEPTH': 0},

                       'Black': {'BACKGROUND': '#000000',
                                 'TEXT': '#FFFFFF',
                                 'INPUT': '#4D4D4D',
                                 'TEXT_INPUT': '#FFFFFF',
                                 'SCROLL': '#707070',
                                 'BUTTON': ('#000000', '#FFFFFF'),
                                 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                 'BORDER': 1,
                                 'SLIDER_DEPTH': 0,
                                 'PROGRESS_DEPTH': 0},

                       'Tan': {'BACKGROUND': '#fdf6e3',
                               'TEXT': '#268bd1',
                               'INPUT': '#eee8d5',
                               'TEXT_INPUT': '#6c71c3',
                               'SCROLL': '#eee8d5',
                               'BUTTON': ('#FFFFFF', '#063542'),
                               'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                               'BORDER': 1,
                               'SLIDER_DEPTH': 0,
                               'PROGRESS_DEPTH': 0},

                       'TanBlue': {'BACKGROUND': '#e5dece',
                                   'TEXT': '#063289',
                                   'INPUT': '#f9f8f4',
                                   'TEXT_INPUT': '#242834',
                                   'SCROLL': '#eee8d5',
                                   'BUTTON': ('#FFFFFF', '#063289'),
                                   'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                   'BORDER': 1,
                                   'SLIDER_DEPTH': 0,
                                   'PROGRESS_DEPTH': 0},

                       'DarkTanBlue': {'BACKGROUND': '#242834',
                                       'TEXT': '#dfe6f8',
                                       'INPUT': '#97755c',
                                       'TEXT_INPUT': '#FFFFFF',
                                       'SCROLL': '#a9afbb',
                                       'BUTTON': ('#FFFFFF', '#063289'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                       'BORDER': 1,
                                       'SLIDER_DEPTH': 0,
                                       'PROGRESS_DEPTH': 0},

                       'DarkAmber': {'BACKGROUND': '#2c2825',
                                     'TEXT': '#fdcb52',
                                     'INPUT': '#705e52',
                                     'TEXT_INPUT': '#fdcb52',
                                     'SCROLL': '#705e52',
                                     'BUTTON': ('#000000', '#fdcb52'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                     'BORDER': 1,
                                     'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0},

                       'DarkBlue': {'BACKGROUND': '#1a2835',
                                    'TEXT': '#d1ecff',
                                    'INPUT': '#335267',
                                    'TEXT_INPUT': '#acc2d0',
                                    'SCROLL': '#1b6497',
                                    'BUTTON': ('#000000', '#fafaf8'),
                                    'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                    'BORDER': 1, 'SLIDER_DEPTH': 0,
                                    'PROGRESS_DEPTH': 0},

                       'Reds': {'BACKGROUND': '#280001',
                                'TEXT': '#FFFFFF',
                                'INPUT': '#d8d584',
                                'TEXT_INPUT': '#000000',
                                'SCROLL': '#763e00',
                                'BUTTON': ('#000000', '#daad28'),
                                'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                'BORDER': 1,
                                'SLIDER_DEPTH': 0,
                                'PROGRESS_DEPTH': 0},

                       'Green': {'BACKGROUND': '#82a459',
                                 'TEXT': '#000000',
                                 'INPUT': '#d8d584',
                                 'TEXT_INPUT': '#000000',
                                 'SCROLL': '#e3ecf3',
                                 'BUTTON': ('#FFFFFF', '#517239'),
                                 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                 'BORDER': 1,
                                 'SLIDER_DEPTH': 0,
                                 'PROGRESS_DEPTH': 0},

                       'BluePurple': {'BACKGROUND': '#A5CADD',
                                      'TEXT': '#6E266E',
                                      'INPUT': '#E0F5FF',
                                      'TEXT_INPUT': '#000000',
                                      'SCROLL': '#E0F5FF',
                                      'BUTTON': ('#FFFFFF', '#303952'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                      'BORDER': 1,
                                      'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0},

                       'Purple': {'BACKGROUND': '#B0AAC2',
                                  'TEXT': '#000000',
                                  'INPUT': '#F2EFE8',
                                  'SCROLL': '#F2EFE8',
                                  'TEXT_INPUT': '#000000',
                                  'BUTTON': ('#000000', '#C2D4D8'),
                                  'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                  'BORDER': 1,
                                  'SLIDER_DEPTH': 0,
                                  'PROGRESS_DEPTH': 0},

                       'BlueMono': {'BACKGROUND': '#AAB6D3',
                                    'TEXT': '#000000',
                                    'INPUT': '#F1F4FC',
                                    'SCROLL': '#F1F4FC',
                                    'TEXT_INPUT': '#000000',
                                    'BUTTON': ('#FFFFFF', '#7186C7'),
                                    'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                    'BORDER': 1,
                                    'SLIDER_DEPTH': 0,
                                    'PROGRESS_DEPTH': 0},

                       'GreenMono': {'BACKGROUND': '#A8C1B4',
                                     'TEXT': '#000000',
                                     'INPUT': '#DDE0DE',
                                     'SCROLL': '#E3E3E3',
                                     'TEXT_INPUT': '#000000',
                                     'BUTTON': ('#FFFFFF', '#6D9F85'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                     'BORDER': 1,
                                     'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0},

                       'BrownBlue': {'BACKGROUND': '#64778d',
                                     'TEXT': '#FFFFFF',
                                     'INPUT': '#f0f3f7',
                                     'SCROLL': '#A6B2BE',
                                     'TEXT_INPUT': '#000000',
                                     'BUTTON': ('#FFFFFF', '#283b5b'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                     'BORDER': 1,
                                     'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0},

                       'BrightColors': {'BACKGROUND': '#b4ffb4',
                                        'TEXT': '#000000',
                                        'INPUT': '#ffff64',
                                        'SCROLL': '#ffb482',
                                        'TEXT_INPUT': '#000000',
                                        'BUTTON': ('#000000', '#ffa0dc'),
                                        'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                        'BORDER': 1,
                                        'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0},

                       'NeutralBlue': {'BACKGROUND': '#92aa9d',
                                       'TEXT': '#000000',
                                       'INPUT': '#fcfff6',
                                       'SCROLL': '#fcfff6',
                                       'TEXT_INPUT': '#000000',
                                       'BUTTON': ('#000000', '#d0dbbd'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                       'BORDER': 1,
                                       'SLIDER_DEPTH': 0,
                                       'PROGRESS_DEPTH': 0},

                       'Kayak': {'BACKGROUND': '#a7ad7f',
                                 'TEXT': '#000000',
                                 'INPUT': '#e6d3a8',
                                 'SCROLL': '#e6d3a8',
                                 'TEXT_INPUT': '#000000',
                                 'BUTTON': ('#FFFFFF', '#5d907d'),
                                 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                 'BORDER': 1,
                                 'SLIDER_DEPTH': 0,
                                 'PROGRESS_DEPTH': 0},

                       'SandyBeach': {'BACKGROUND': '#efeccb',
                                      'TEXT': '#012f2f',
                                      'INPUT': '#e6d3a8',
                                      'SCROLL': '#e6d3a8',
                                      'TEXT_INPUT': '#012f2f',
                                      'BUTTON': ('#FFFFFF', '#046380'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                      'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0},

                       'TealMono': {'BACKGROUND': '#a8cfdd',
                                    'TEXT': '#000000',
                                    'INPUT': '#dfedf2',
                                    'SCROLL': '#dfedf2',
                                    'TEXT_INPUT': '#000000',
                                    'BUTTON': ('#FFFFFF', '#183440'),
                                    'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                    'BORDER': 1,
                                    'SLIDER_DEPTH': 0,
                                    'PROGRESS_DEPTH': 0},
                       ################################## Renamed Original Themes ##################################
                       'Default':  # plain gray but blue buttons
                           {'BACKGROUND': COLOR_SYSTEM_DEFAULT,
                            'TEXT': COLOR_SYSTEM_DEFAULT,
                            'INPUT': COLOR_SYSTEM_DEFAULT,
                            'TEXT_INPUT': COLOR_SYSTEM_DEFAULT,
                            'SCROLL': COLOR_SYSTEM_DEFAULT,
                            'BUTTON': OFFICIAL_PYSIMPLEGUI_BUTTON_COLOR,
                            'PROGRESS': COLOR_SYSTEM_DEFAULT,
                            'BORDER': 1, 'SLIDER_DEPTH': 1,
                            'PROGRESS_DEPTH': 0},

                       'Default1':  # everything is gray
                           {'BACKGROUND': COLOR_SYSTEM_DEFAULT,
                            'TEXT': COLOR_SYSTEM_DEFAULT,
                            'INPUT': COLOR_SYSTEM_DEFAULT,
                            'TEXT_INPUT': COLOR_SYSTEM_DEFAULT,
                            'SCROLL': COLOR_SYSTEM_DEFAULT,
                            'BUTTON': COLOR_SYSTEM_DEFAULT,
                            'PROGRESS': COLOR_SYSTEM_DEFAULT,
                            'BORDER': 1, 'SLIDER_DEPTH': 1,
                            'PROGRESS_DEPTH': 0},

                       'DefaultNoMoreNagging':  # a duplicate of "Default" for users that are tired of the nag screen
                           {'BACKGROUND': COLOR_SYSTEM_DEFAULT,
                            'TEXT': COLOR_SYSTEM_DEFAULT,
                            'INPUT': COLOR_SYSTEM_DEFAULT,
                            'TEXT_INPUT': COLOR_SYSTEM_DEFAULT,
                            'SCROLL': COLOR_SYSTEM_DEFAULT,
                            'BUTTON': OFFICIAL_PYSIMPLEGUI_BUTTON_COLOR,
                            'PROGRESS': COLOR_SYSTEM_DEFAULT,
                            'BORDER': 1, 'SLIDER_DEPTH': 1,
                            'PROGRESS_DEPTH': 0},

                       'LightBlue': {'BACKGROUND': '#E3F2FD',
                                     'TEXT': '#000000',
                                     'INPUT': '#86A8FF',
                                     'TEXT_INPUT': '#000000',
                                     'SCROLL': '#86A8FF',
                                     'BUTTON': ('#FFFFFF', '#5079D3'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                     'BORDER': 0, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0,
                                     'ACCENT1': '#FF0266',
                                     'ACCENT2': '#FF5C93',
                                     'ACCENT3': '#C5003C'},

                       'LightGrey': {'BACKGROUND': '#FAFAFA',
                                     'TEXT': '#000000',
                                     'INPUT': '#004EA1',
                                     'TEXT_INPUT': '#FFFFFF',
                                     'SCROLL': '#5EA7FF',
                                     'BUTTON': ('#FFFFFF', '#0079D3'),  # based on Reddit color
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                     'BORDER': 0, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0,
                                     'ACCENT1': '#FF0266',
                                     'ACCENT2': '#FF5C93',
                                     'ACCENT3': '#C5003C'},

                       'LightGrey1': {'BACKGROUND': '#ffffff',
                                      'TEXT': '#1a1a1b',
                                      'INPUT': '#dae0e6',
                                      'TEXT_INPUT': '#222222',
                                      'SCROLL': '#a5a4a4',
                                      'BUTTON': ('#FFFFFF', '#0079d3'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                      'BORDER': 1,
                                      'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0,
                                      'ACCENT1': '#ff5414',
                                      'ACCENT2': '#33a8ff',
                                      'ACCENT3': '#dbf0ff'},

                       'DarkBrown': {'BACKGROUND': '#282923',
                                     'TEXT': '#E7DB74',
                                     'INPUT': '#393a32',
                                     'TEXT_INPUT': '#E7C855',
                                     'SCROLL': '#E7C855',
                                     'BUTTON': ('#E7C855', '#284B5A'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                     'BORDER': 1,
                                     'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0,
                                     'ACCENT1': '#c15226',
                                     'ACCENT2': '#7a4d5f',
                                     'ACCENT3': '#889743'},

                       'LightGreen1': {'BACKGROUND': '#9FB8AD',
                                       'TEXT': COLOR_SYSTEM_DEFAULT,
                                       'INPUT': '#F7F3EC', 'TEXT_INPUT': '#000000',
                                       'SCROLL': '#F7F3EC',
                                       'BUTTON': ('#FFFFFF', '#475841'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                       'BORDER': 1, 'SLIDER_DEPTH': 0,
                                       'PROGRESS_DEPTH': 0},

                       'DarkGrey': {'BACKGROUND': '#404040',
                                    'TEXT': '#FFFFFF',
                                    'INPUT': '#4D4D4D',
                                    'TEXT_INPUT': '#FFFFFF',
                                    'SCROLL': '#707070',
                                    'BUTTON': ('#FFFFFF', '#004F00'),
                                    'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                    'BORDER': 1,
                                    'SLIDER_DEPTH': 0,
                                    'PROGRESS_DEPTH': 0},

                       'LightGreen2': {'BACKGROUND': '#B7CECE',
                                       'TEXT': '#000000',
                                       'INPUT': '#FDFFF7',
                                       'TEXT_INPUT': '#000000',
                                       'SCROLL': '#FDFFF7',
                                       'BUTTON': ('#FFFFFF', '#658268'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                       'BORDER': 1,
                                       'SLIDER_DEPTH': 0,
                                       'ACCENT1': '#76506d',
                                       'ACCENT2': '#5148f1',
                                       'ACCENT3': '#0a1c84',
                                       'PROGRESS_DEPTH': 0},

                       'DarkGrey1': {'BACKGROUND': '#404040',
                                     'TEXT': '#FFFFFF',
                                     'INPUT': '#FFFFFF',
                                     'TEXT_INPUT': '#000000',
                                     'SCROLL': '#707070',
                                     'BUTTON': ('#FFFFFF', '#004F00'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                     'BORDER': 1,
                                     'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0},

                       'DarkBlack': {'BACKGROUND': '#000000',
                                     'TEXT': '#FFFFFF',
                                     'INPUT': '#4D4D4D',
                                     'TEXT_INPUT': '#FFFFFF',
                                     'SCROLL': '#707070',
                                     'BUTTON': ('#000000', '#FFFFFF'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                     'BORDER': 1,
                                     'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0},

                       'LightBrown': {'BACKGROUND': '#fdf6e3',
                                      'TEXT': '#268bd1',
                                      'INPUT': '#eee8d5',
                                      'TEXT_INPUT': '#6c71c3',
                                      'SCROLL': '#eee8d5',
                                      'BUTTON': ('#FFFFFF', '#063542'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                      'BORDER': 1,
                                      'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0},

                       'LightBrown1': {'BACKGROUND': '#e5dece',
                                       'TEXT': '#063289',
                                       'INPUT': '#f9f8f4',
                                       'TEXT_INPUT': '#242834',
                                       'SCROLL': '#eee8d5',
                                       'BUTTON': ('#FFFFFF', '#063289'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                       'BORDER': 1,
                                       'SLIDER_DEPTH': 0,
                                       'PROGRESS_DEPTH': 0},

                       'DarkBlue1': {'BACKGROUND': '#242834',
                                     'TEXT': '#dfe6f8',
                                     'INPUT': '#97755c',
                                     'TEXT_INPUT': '#FFFFFF',
                                     'SCROLL': '#a9afbb',
                                     'BUTTON': ('#FFFFFF', '#063289'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                     'BORDER': 1,
                                     'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0},

                       'DarkBrown1': {'BACKGROUND': '#2c2825',
                                      'TEXT': '#fdcb52',
                                      'INPUT': '#705e52',
                                      'TEXT_INPUT': '#fdcb52',
                                      'SCROLL': '#705e52',
                                      'BUTTON': ('#000000', '#fdcb52'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                      'BORDER': 1,
                                      'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0},

                       'DarkBlue2': {'BACKGROUND': '#1a2835',
                                     'TEXT': '#d1ecff',
                                     'INPUT': '#335267',
                                     'TEXT_INPUT': '#acc2d0',
                                     'SCROLL': '#1b6497',
                                     'BUTTON': ('#000000', '#fafaf8'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                     'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0},

                       'DarkBrown2': {'BACKGROUND': '#280001',
                                      'TEXT': '#FFFFFF',
                                      'INPUT': '#d8d584',
                                      'TEXT_INPUT': '#000000',
                                      'SCROLL': '#763e00',
                                      'BUTTON': ('#000000', '#daad28'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                      'BORDER': 1,
                                      'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0},

                       'DarkGreen': {'BACKGROUND': '#82a459',
                                     'TEXT': '#000000',
                                     'INPUT': '#d8d584',
                                     'TEXT_INPUT': '#000000',
                                     'SCROLL': '#e3ecf3',
                                     'BUTTON': ('#FFFFFF', '#517239'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                     'BORDER': 1,
                                     'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0},

                       'LightBlue1': {'BACKGROUND': '#A5CADD',
                                      'TEXT': '#6E266E',
                                      'INPUT': '#E0F5FF',
                                      'TEXT_INPUT': '#000000',
                                      'SCROLL': '#E0F5FF',
                                      'BUTTON': ('#FFFFFF', '#303952'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                      'BORDER': 1,
                                      'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0},

                       'LightPurple': {'BACKGROUND': '#B0AAC2',
                                       'TEXT': '#000000',
                                       'INPUT': '#F2EFE8',
                                       'SCROLL': '#F2EFE8',
                                       'TEXT_INPUT': '#000000',
                                       'BUTTON': ('#000000', '#C2D4D8'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                       'BORDER': 1,
                                       'SLIDER_DEPTH': 0,
                                       'PROGRESS_DEPTH': 0},

                       'LightBlue2': {'BACKGROUND': '#AAB6D3',
                                      'TEXT': '#000000',
                                      'INPUT': '#F1F4FC',
                                      'SCROLL': '#F1F4FC',
                                      'TEXT_INPUT': '#000000',
                                      'BUTTON': ('#FFFFFF', '#7186C7'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                      'BORDER': 1,
                                      'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0},

                       'LightGreen3': {'BACKGROUND': '#A8C1B4',
                                       'TEXT': '#000000',
                                       'INPUT': '#DDE0DE',
                                       'SCROLL': '#E3E3E3',
                                       'TEXT_INPUT': '#000000',
                                       'BUTTON': ('#FFFFFF', '#6D9F85'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                       'BORDER': 1,
                                       'SLIDER_DEPTH': 0,
                                       'PROGRESS_DEPTH': 0},

                       'DarkBlue3': {'BACKGROUND': '#64778d',
                                     'TEXT': '#FFFFFF',
                                     'INPUT': '#f0f3f7',
                                     'SCROLL': '#A6B2BE',
                                     'TEXT_INPUT': '#000000',
                                     'BUTTON': ('#FFFFFF', '#283b5b'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                     'BORDER': 1,
                                     'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0},

                       'LightGreen4': {'BACKGROUND': '#b4ffb4',
                                       'TEXT': '#000000',
                                       'INPUT': '#ffff64',
                                       'SCROLL': '#ffb482',
                                       'TEXT_INPUT': '#000000',
                                       'BUTTON': ('#000000', '#ffa0dc'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                       'BORDER': 1,
                                       'SLIDER_DEPTH': 0,
                                       'PROGRESS_DEPTH': 0},

                       'LightGreen5': {'BACKGROUND': '#92aa9d',
                                       'TEXT': '#000000',
                                       'INPUT': '#fcfff6',
                                       'SCROLL': '#fcfff6',
                                       'TEXT_INPUT': '#000000',
                                       'BUTTON': ('#000000', '#d0dbbd'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                       'BORDER': 1,
                                       'SLIDER_DEPTH': 0,
                                       'PROGRESS_DEPTH': 0},

                       'LightBrown2': {'BACKGROUND': '#a7ad7f',
                                       'TEXT': '#000000',
                                       'INPUT': '#e6d3a8',
                                       'SCROLL': '#e6d3a8',
                                       'TEXT_INPUT': '#000000',
                                       'BUTTON': ('#FFFFFF', '#5d907d'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                       'BORDER': 1,
                                       'SLIDER_DEPTH': 0,
                                       'PROGRESS_DEPTH': 0},

                       'LightBrown3': {'BACKGROUND': '#efeccb',
                                       'TEXT': '#012f2f',
                                       'INPUT': '#e6d3a8',
                                       'SCROLL': '#e6d3a8',
                                       'TEXT_INPUT': '#012f2f',
                                       'BUTTON': ('#FFFFFF', '#046380'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                       'BORDER': 1, 'SLIDER_DEPTH': 0,
                                       'PROGRESS_DEPTH': 0},

                       'LightBlue3': {'BACKGROUND': '#a8cfdd',
                                      'TEXT': '#000000',
                                      'INPUT': '#dfedf2',
                                      'SCROLL': '#dfedf2',
                                      'TEXT_INPUT': '#000000',
                                      'BUTTON': ('#FFFFFF', '#183440'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                      'BORDER': 1,
                                      'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0},

                       ################################## End Renamed Original Themes ##################################

                       #
                       'LightBrown4': {'BACKGROUND': '#d7c79e', 'TEXT': '#a35638', 'INPUT': '#9dab86', 'TEXT_INPUT': '#000000', 'SCROLL': '#a35638',
                                       'BUTTON': ('#FFFFFF', '#a35638'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#a35638', '#9dab86', '#e08f62', '#d7c79e'], },
                       'DarkTeal': {'BACKGROUND': '#003f5c', 'TEXT': '#fb5b5a', 'INPUT': '#bc4873', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#bc4873',
                                    'BUTTON': ('#FFFFFF', '#fb5b5a'),
                                    'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                    'COLOR_LIST': ['#003f5c', '#472b62', '#bc4873', '#fb5b5a'], },
                       'DarkPurple': {'BACKGROUND': '#472b62', 'TEXT': '#fb5b5a', 'INPUT': '#bc4873', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#bc4873',
                                      'BUTTON': ('#FFFFFF', '#472b62'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#003f5c', '#472b62', '#bc4873', '#fb5b5a'], },
                       'LightGreen6': {'BACKGROUND': '#eafbea', 'TEXT': '#1f6650', 'INPUT': '#6f9a8d', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#1f6650',
                                       'BUTTON': ('#FFFFFF', '#1f6650'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#1f6650', '#6f9a8d', '#ea5e5e', '#eafbea'], },
                       'DarkGrey2': {'BACKGROUND': '#2b2b28', 'TEXT': '#f8f8f8', 'INPUT': '#f1d6ab', 'TEXT_INPUT': '#000000', 'SCROLL': '#f1d6ab',
                                     'BUTTON': ('#2b2b28', '#e3b04b'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#2b2b28', '#e3b04b', '#f1d6ab', '#f8f8f8'], },
                       'LightBrown6': {'BACKGROUND': '#f9b282', 'TEXT': '#8f4426', 'INPUT': '#de6b35', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#8f4426',
                                       'BUTTON': ('#FFFFFF', '#8f4426'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#8f4426', '#de6b35', '#64ccda', '#f9b282'], },
                       'DarkTeal1': {'BACKGROUND': '#396362', 'TEXT': '#ffe7d1', 'INPUT': '#f6c89f', 'TEXT_INPUT': '#000000', 'SCROLL': '#f6c89f',
                                     'BUTTON': ('#ffe7d1', '#4b8e8d'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#396362', '#4b8e8d', '#f6c89f', '#ffe7d1'], },
                       'LightBrown7': {'BACKGROUND': '#f6c89f', 'TEXT': '#396362', 'INPUT': '#4b8e8d', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#396362',
                                       'BUTTON': ('#FFFFFF', '#396362'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                       'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#396362', '#4b8e8d', '#f6c89f', '#ffe7d1'], },
                       'DarkPurple1': {'BACKGROUND': '#0c093c', 'TEXT': '#fad6d6', 'INPUT': '#eea5f6', 'TEXT_INPUT': '#000000', 'SCROLL': '#eea5f6',
                                       'BUTTON': ('#FFFFFF', '#df42d1'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#0c093c', '#df42d1', '#eea5f6', '#fad6d6'], },
                       'DarkGrey3': {'BACKGROUND': '#211717', 'TEXT': '#dfddc7', 'INPUT': '#f58b54', 'TEXT_INPUT': '#000000', 'SCROLL': '#f58b54',
                                     'BUTTON': ('#dfddc7', '#a34a28'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#211717', '#a34a28', '#f58b54', '#dfddc7'], },
                       'LightBrown8': {'BACKGROUND': '#dfddc7', 'TEXT': '#211717', 'INPUT': '#a34a28', 'TEXT_INPUT': '#dfddc7', 'SCROLL': '#211717',
                                       'BUTTON': ('#dfddc7', '#a34a28'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#211717', '#a34a28', '#f58b54', '#dfddc7'], },
                       'DarkBlue4': {'BACKGROUND': '#494ca2', 'TEXT': '#e3e7f1', 'INPUT': '#c6cbef', 'TEXT_INPUT': '#000000', 'SCROLL': '#c6cbef',
                                     'BUTTON': ('#FFFFFF', '#8186d5'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#494ca2', '#8186d5', '#c6cbef', '#e3e7f1'], },
                       'LightBlue4': {'BACKGROUND': '#5c94bd', 'TEXT': '#470938', 'INPUT': '#1a3e59', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#470938',
                                      'BUTTON': ('#FFFFFF', '#470938'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#470938', '#1a3e59', '#5c94bd', '#f2d6eb'], },
                       'DarkTeal2': {'BACKGROUND': '#394a6d', 'TEXT': '#c0ffb3', 'INPUT': '#52de97', 'TEXT_INPUT': '#000000', 'SCROLL': '#52de97',
                                     'BUTTON': ('#c0ffb3', '#394a6d'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#394a6d', '#3c9d9b', '#52de97', '#c0ffb3'], },
                       'DarkTeal3': {'BACKGROUND': '#3c9d9b', 'TEXT': '#c0ffb3', 'INPUT': '#52de97', 'TEXT_INPUT': '#000000', 'SCROLL': '#52de97',
                                     'BUTTON': ('#c0ffb3', '#394a6d'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#394a6d', '#3c9d9b', '#52de97', '#c0ffb3'], },
                       'DarkPurple5': {'BACKGROUND': '#730068', 'TEXT': '#f6f078', 'INPUT': '#01d28e', 'TEXT_INPUT': '#000000', 'SCROLL': '#01d28e',
                                       'BUTTON': ('#f6f078', '#730068'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#730068', '#434982', '#01d28e', '#f6f078'], },
                       'DarkPurple2': {'BACKGROUND': '#202060', 'TEXT': '#b030b0', 'INPUT': '#602080', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#602080',
                                       'BUTTON': ('#FFFFFF', '#202040'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#202040', '#202060', '#602080', '#b030b0'], },
                       'DarkBlue5': {'BACKGROUND': '#000272', 'TEXT': '#ff6363', 'INPUT': '#a32f80', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#a32f80',
                                     'BUTTON': ('#FFFFFF', '#341677'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#000272', '#341677', '#a32f80', '#ff6363'], },
                       'LightGrey2': {'BACKGROUND': '#f6f6f6', 'TEXT': '#420000', 'INPUT': '#d4d7dd', 'TEXT_INPUT': '#420000', 'SCROLL': '#420000',
                                      'BUTTON': ('#420000', '#d4d7dd'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#420000', '#d4d7dd', '#eae9e9', '#f6f6f6'], },
                       'LightGrey3': {'BACKGROUND': '#eae9e9', 'TEXT': '#420000', 'INPUT': '#d4d7dd', 'TEXT_INPUT': '#420000', 'SCROLL': '#420000',
                                      'BUTTON': ('#420000', '#d4d7dd'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#420000', '#d4d7dd', '#eae9e9', '#f6f6f6'], },
                       'DarkBlue6': {'BACKGROUND': '#01024e', 'TEXT': '#ff6464', 'INPUT': '#8b4367', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#8b4367',
                                     'BUTTON': ('#FFFFFF', '#543864'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#01024e', '#543864', '#8b4367', '#ff6464'], },
                       'DarkBlue7': {'BACKGROUND': '#241663', 'TEXT': '#eae7af', 'INPUT': '#a72693', 'TEXT_INPUT': '#eae7af', 'SCROLL': '#a72693',
                                     'BUTTON': ('#eae7af', '#160f30'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#160f30', '#241663', '#a72693', '#eae7af'], },
                       'LightBrown9': {'BACKGROUND': '#f6d365', 'TEXT': '#3a1f5d', 'INPUT': '#c83660', 'TEXT_INPUT': '#f6d365', 'SCROLL': '#3a1f5d',
                                       'BUTTON': ('#f6d365', '#c83660'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#3a1f5d', '#c83660', '#e15249', '#f6d365'], },
                       'DarkPurple3': {'BACKGROUND': '#6e2142', 'TEXT': '#ffd692', 'INPUT': '#e16363', 'TEXT_INPUT': '#ffd692', 'SCROLL': '#e16363',
                                       'BUTTON': ('#ffd692', '#943855'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#6e2142', '#943855', '#e16363', '#ffd692'], },
                       'LightBrown10': {'BACKGROUND': '#ffd692', 'TEXT': '#6e2142', 'INPUT': '#943855', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#6e2142',
                                        'BUTTON': ('#FFFFFF', '#6e2142'),
                                        'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        'COLOR_LIST': ['#6e2142', '#943855', '#e16363', '#ffd692'], },
                       'DarkPurple4': {'BACKGROUND': '#200f21', 'TEXT': '#f638dc', 'INPUT': '#5a3d5c', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#5a3d5c',
                                       'BUTTON': ('#FFFFFF', '#382039'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#200f21', '#382039', '#5a3d5c', '#f638dc'], },
                       'LightBlue5': {'BACKGROUND': '#b2fcff', 'TEXT': '#3e64ff', 'INPUT': '#5edfff', 'TEXT_INPUT': '#000000', 'SCROLL': '#3e64ff',
                                      'BUTTON': ('#FFFFFF', '#3e64ff'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#3e64ff', '#5edfff', '#b2fcff', '#ecfcff'], },
                       'DarkTeal4': {'BACKGROUND': '#464159', 'TEXT': '#c7f0db', 'INPUT': '#8bbabb', 'TEXT_INPUT': '#000000', 'SCROLL': '#8bbabb',
                                     'BUTTON': ('#FFFFFF', '#6c7b95'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#464159', '#6c7b95', '#8bbabb', '#c7f0db'], },
                       'LightTeal': {'BACKGROUND': '#c7f0db', 'TEXT': '#464159', 'INPUT': '#6c7b95', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#464159',
                                     'BUTTON': ('#FFFFFF', '#464159'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#464159', '#6c7b95', '#8bbabb', '#c7f0db'], },
                       'DarkTeal5': {'BACKGROUND': '#8bbabb', 'TEXT': '#464159', 'INPUT': '#6c7b95', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#464159',
                                     'BUTTON': ('#c7f0db', '#6c7b95'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#464159', '#6c7b95', '#8bbabb', '#c7f0db'], },
                       'LightGrey4': {'BACKGROUND': '#faf5ef', 'TEXT': '#672f2f', 'INPUT': '#99b19c', 'TEXT_INPUT': '#672f2f', 'SCROLL': '#672f2f',
                                      'BUTTON': ('#672f2f', '#99b19c'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#672f2f', '#99b19c', '#d7d1c9', '#faf5ef'], },
                       'LightGreen7': {'BACKGROUND': '#99b19c', 'TEXT': '#faf5ef', 'INPUT': '#d7d1c9', 'TEXT_INPUT': '#000000', 'SCROLL': '#d7d1c9',
                                       'BUTTON': ('#FFFFFF', '#99b19c'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#672f2f', '#99b19c', '#d7d1c9', '#faf5ef'], },
                       'LightGrey5': {'BACKGROUND': '#d7d1c9', 'TEXT': '#672f2f', 'INPUT': '#99b19c', 'TEXT_INPUT': '#672f2f', 'SCROLL': '#672f2f',
                                      'BUTTON': ('#FFFFFF', '#672f2f'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#672f2f', '#99b19c', '#d7d1c9', '#faf5ef'], },
                       'DarkBrown3': {'BACKGROUND': '#a0855b', 'TEXT': '#f9f6f2', 'INPUT': '#f1d6ab', 'TEXT_INPUT': '#000000', 'SCROLL': '#f1d6ab',
                                      'BUTTON': ('#FFFFFF', '#38470b'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#38470b', '#a0855b', '#f1d6ab', '#f9f6f2'], },
                       'LightBrown11': {'BACKGROUND': '#f1d6ab', 'TEXT': '#38470b', 'INPUT': '#a0855b', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#38470b',
                                        'BUTTON': ('#f9f6f2', '#a0855b'),
                                        'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        'COLOR_LIST': ['#38470b', '#a0855b', '#f1d6ab', '#f9f6f2'], },
                       'DarkRed': {'BACKGROUND': '#83142c', 'TEXT': '#f9d276', 'INPUT': '#ad1d45', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#ad1d45',
                                   'BUTTON': ('#f9d276', '#ad1d45'),
                                   'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                   'COLOR_LIST': ['#44000d', '#83142c', '#ad1d45', '#f9d276'], },
                       'DarkTeal6': {'BACKGROUND': '#204969', 'TEXT': '#fff7f7', 'INPUT': '#dadada', 'TEXT_INPUT': '#000000', 'SCROLL': '#dadada',
                                     'BUTTON': ('#000000', '#fff7f7'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#204969', '#08ffc8', '#dadada', '#fff7f7'], },
                       'DarkBrown4': {'BACKGROUND': '#252525', 'TEXT': '#ff0000', 'INPUT': '#af0404', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#af0404',
                                      'BUTTON': ('#FFFFFF', '#252525'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#252525', '#414141', '#af0404', '#ff0000'], },
                       'LightYellow': {'BACKGROUND': '#f4ff61', 'TEXT': '#27aa80', 'INPUT': '#32ff6a', 'TEXT_INPUT': '#000000', 'SCROLL': '#27aa80',
                                       'BUTTON': ('#f4ff61', '#27aa80'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#27aa80', '#32ff6a', '#a8ff3e', '#f4ff61'], },
                       'DarkGreen1': {'BACKGROUND': '#2b580c', 'TEXT': '#fdef96', 'INPUT': '#f7b71d', 'TEXT_INPUT': '#000000', 'SCROLL': '#f7b71d',
                                      'BUTTON': ('#fdef96', '#2b580c'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#2b580c', '#afa939', '#f7b71d', '#fdef96'], },

                       'LightGreen8': {'BACKGROUND': '#c8dad3', 'TEXT': '#63707e', 'INPUT': '#93b5b3', 'TEXT_INPUT': '#000000', 'SCROLL': '#63707e',
                                       'BUTTON': ('#FFFFFF', '#63707e'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#63707e', '#93b5b3', '#c8dad3', '#f2f6f5'], },

                       'DarkTeal7': {'BACKGROUND': '#248ea9', 'TEXT': '#fafdcb', 'INPUT': '#aee7e8', 'TEXT_INPUT': '#000000', 'SCROLL': '#aee7e8',
                                     'BUTTON': ('#000000', '#fafdcb'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#248ea9', '#28c3d4', '#aee7e8', '#fafdcb'], },
                       'DarkBlue8': {'BACKGROUND': '#454d66', 'TEXT': '#d9d872', 'INPUT': '#58b368', 'TEXT_INPUT': '#000000', 'SCROLL': '#58b368',
                                     'BUTTON': ('#000000', '#009975'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#009975', '#454d66', '#58b368', '#d9d872'], },
                       'DarkBlue9': {'BACKGROUND': '#263859', 'TEXT': '#ff6768', 'INPUT': '#6b778d', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#6b778d',
                                     'BUTTON': ('#ff6768', '#263859'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#17223b', '#263859', '#6b778d', '#ff6768'], },
                       'DarkBlue10': {'BACKGROUND': '#0028ff', 'TEXT': '#f1f4df', 'INPUT': '#10eaf0', 'TEXT_INPUT': '#000000', 'SCROLL': '#10eaf0',
                                      'BUTTON': ('#f1f4df', '#24009c'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#24009c', '#0028ff', '#10eaf0', '#f1f4df'], },
                       'DarkBlue11': {'BACKGROUND': '#6384b3', 'TEXT': '#e6f0b6', 'INPUT': '#b8e9c0', 'TEXT_INPUT': '#000000', 'SCROLL': '#b8e9c0',
                                      'BUTTON': ('#e6f0b6', '#684949'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#684949', '#6384b3', '#b8e9c0', '#e6f0b6'], },

                       'DarkTeal8': {'BACKGROUND': '#71a0a5', 'TEXT': '#212121', 'INPUT': '#665c84', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#212121',
                                     'BUTTON': ('#fab95b', '#665c84'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#212121', '#665c84', '#71a0a5', '#fab95b']},
                       'DarkRed1': {'BACKGROUND': '#c10000', 'TEXT': '#eeeeee', 'INPUT': '#dedede', 'TEXT_INPUT': '#000000', 'SCROLL': '#dedede',
                                    'BUTTON': ('#c10000', '#eeeeee'),
                                    'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                    'COLOR_LIST': ['#c10000', '#ff4949', '#dedede', '#eeeeee'], },
                       'LightBrown5': {'BACKGROUND': '#fff591', 'TEXT': '#e41749', 'INPUT': '#f5587b', 'TEXT_INPUT': '#000000', 'SCROLL': '#e41749',
                                       'BUTTON': ('#fff591', '#e41749'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#e41749', '#f5587b', '#ff8a5c', '#fff591']},
                       'LightGreen9': {'BACKGROUND': '#f1edb3', 'TEXT': '#3b503d', 'INPUT': '#4a746e', 'TEXT_INPUT': '#f1edb3', 'SCROLL': '#3b503d',
                                       'BUTTON': ('#f1edb3', '#3b503d'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                       'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#3b503d', '#4a746e', '#c8cf94', '#f1edb3'], 'DESCRIPTION': ['Green', 'Turquoise', 'Yellow']},
                       'DarkGreen2': {'BACKGROUND': '#3b503d', 'TEXT': '#f1edb3', 'INPUT': '#c8cf94', 'TEXT_INPUT': '#000000', 'SCROLL': '#c8cf94',
                                      'BUTTON': ('#f1edb3', '#3b503d'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#3b503d', '#4a746e', '#c8cf94', '#f1edb3'], 'DESCRIPTION': ['Green', 'Turquoise', 'Yellow']},
                       'LightGray1': {'BACKGROUND': '#f2f2f2', 'TEXT': '#222831', 'INPUT': '#393e46', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#222831',
                                      'BUTTON': ('#f2f2f2', '#222831'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#222831', '#393e46', '#f96d00', '#f2f2f2'],
                                      'DESCRIPTION': ['#000000', 'Grey', 'Orange', 'Grey', 'Autumn']},
                       'DarkGrey4': {'BACKGROUND': '#52524e', 'TEXT': '#e9e9e5', 'INPUT': '#d4d6c8', 'TEXT_INPUT': '#000000', 'SCROLL': '#d4d6c8',
                                     'BUTTON': ('#FFFFFF', '#9a9b94'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#52524e', '#9a9b94', '#d4d6c8', '#e9e9e5'],
                                     'DESCRIPTION': ['Grey', 'Pastel', 'Winter']},
                       'DarkBlue12': {'BACKGROUND': '#324e7b', 'TEXT': '#f8f8f8', 'INPUT': '#86a6df', 'TEXT_INPUT': '#000000', 'SCROLL': '#86a6df',
                                      'BUTTON': ('#FFFFFF', '#5068a9'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#324e7b', '#5068a9', '#86a6df', '#f8f8f8'],
                                      'DESCRIPTION': ['Blue', 'Grey', 'Cold', 'Winter']},
                       'DarkPurple6': {'BACKGROUND': '#070739', 'TEXT': '#e1e099', 'INPUT': '#c327ab', 'TEXT_INPUT': '#e1e099', 'SCROLL': '#c327ab',
                                       'BUTTON': ('#e1e099', '#521477'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                       'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#070739', '#521477', '#c327ab', '#e1e099'],
                                       'DESCRIPTION': ['#000000', 'Purple', 'Yellow', 'Dark']},
                       'DarkBlue13': {'BACKGROUND': '#203562', 'TEXT': '#e3e8f8', 'INPUT': '#c0c5cd', 'TEXT_INPUT': '#000000', 'SCROLL': '#c0c5cd',
                                      'BUTTON': ('#FFFFFF', '#3e588f'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#203562', '#3e588f', '#c0c5cd', '#e3e8f8'],
                                      'DESCRIPTION': ['Blue', 'Grey', 'Wedding', 'Cold']},
                       'DarkBrown5': {'BACKGROUND': '#3c1b1f', 'TEXT': '#f6e1b5', 'INPUT': '#e2bf81', 'TEXT_INPUT': '#000000', 'SCROLL': '#e2bf81',
                                      'BUTTON': ('#3c1b1f', '#f6e1b5'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#3c1b1f', '#b21e4b', '#e2bf81', '#f6e1b5'],
                                      'DESCRIPTION': ['Brown', 'Red', 'Yellow', 'Warm']},
                       'DarkGreen3': {'BACKGROUND': '#062121', 'TEXT': '#eeeeee', 'INPUT': '#e4dcad', 'TEXT_INPUT': '#000000', 'SCROLL': '#e4dcad',
                                      'BUTTON': ('#eeeeee', '#181810'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#062121', '#181810', '#e4dcad', '#eeeeee'],
                                      'DESCRIPTION': ['#000000', '#000000', 'Brown', 'Grey']},
                       'DarkBlack1': {'BACKGROUND': '#181810', 'TEXT': '#eeeeee', 'INPUT': '#e4dcad', 'TEXT_INPUT': '#000000', 'SCROLL': '#e4dcad',
                                      'BUTTON': ('#FFFFFF', '#062121'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#062121', '#181810', '#e4dcad', '#eeeeee'],
                                      'DESCRIPTION': ['#000000', '#000000', 'Brown', 'Grey']},
                       'DarkGrey5': {'BACKGROUND': '#343434', 'TEXT': '#f3f3f3', 'INPUT': '#e9dcbe', 'TEXT_INPUT': '#000000', 'SCROLL': '#e9dcbe',
                                     'BUTTON': ('#FFFFFF', '#8e8b82'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#343434', '#8e8b82', '#e9dcbe', '#f3f3f3'], 'DESCRIPTION': ['Grey', 'Brown']},
                       'LightBrown12': {'BACKGROUND': '#8e8b82', 'TEXT': '#f3f3f3', 'INPUT': '#e9dcbe', 'TEXT_INPUT': '#000000', 'SCROLL': '#e9dcbe',
                                        'BUTTON': ('#f3f3f3', '#8e8b82'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#343434', '#8e8b82', '#e9dcbe', '#f3f3f3'], 'DESCRIPTION': ['Grey', 'Brown']},
                       'DarkTeal9': {'BACKGROUND': '#13445a', 'TEXT': '#fef4e8', 'INPUT': '#446878', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#446878',
                                     'BUTTON': ('#fef4e8', '#446878'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#13445a', '#970747', '#446878', '#fef4e8'],
                                     'DESCRIPTION': ['Red', 'Grey', 'Blue', 'Wedding', 'Retro']},
                       'DarkBlue14': {'BACKGROUND': '#21273d', 'TEXT': '#f1f6f8', 'INPUT': '#b9d4f1', 'TEXT_INPUT': '#000000', 'SCROLL': '#b9d4f1',
                                      'BUTTON': ('#FFFFFF', '#6a759b'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#21273d', '#6a759b', '#b9d4f1', '#f1f6f8'],
                                      'DESCRIPTION': ['Blue', '#000000', 'Grey', 'Cold', 'Winter']},
                       'LightBlue6': {'BACKGROUND': '#f1f6f8', 'TEXT': '#21273d', 'INPUT': '#6a759b', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#21273d',
                                      'BUTTON': ('#f1f6f8', '#6a759b'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#21273d', '#6a759b', '#b9d4f1', '#f1f6f8'],
                                      'DESCRIPTION': ['Blue', '#000000', 'Grey', 'Cold', 'Winter']},
                       'DarkGreen4': {'BACKGROUND': '#044343', 'TEXT': '#e4e4e4', 'INPUT': '#045757', 'TEXT_INPUT': '#e4e4e4', 'SCROLL': '#045757',
                                      'BUTTON': ('#e4e4e4', '#045757'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#222222', '#044343', '#045757', '#e4e4e4'],
                                      'DESCRIPTION': ['#000000', 'Turquoise', 'Grey', 'Dark']},
                       'DarkGreen5': {'BACKGROUND': '#1b4b36', 'TEXT': '#e0e7f1', 'INPUT': '#aebd77', 'TEXT_INPUT': '#000000', 'SCROLL': '#aebd77',
                                      'BUTTON': ('#FFFFFF', '#538f6a'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#1b4b36', '#538f6a', '#aebd77', '#e0e7f1'], 'DESCRIPTION': ['Green', 'Grey']},
                       'DarkTeal10': {'BACKGROUND': '#0d3446', 'TEXT': '#d8dfe2', 'INPUT': '#71adb5', 'TEXT_INPUT': '#000000', 'SCROLL': '#71adb5',
                                      'BUTTON': ('#FFFFFF', '#176d81'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#0d3446', '#176d81', '#71adb5', '#d8dfe2'],
                                      'DESCRIPTION': ['Grey', 'Turquoise', 'Winter', 'Cold']},
                       'DarkGrey6': {'BACKGROUND': '#3e3e3e', 'TEXT': '#ededed', 'INPUT': '#68868c', 'TEXT_INPUT': '#ededed', 'SCROLL': '#68868c',
                                     'BUTTON': ('#FFFFFF', '#405559'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#3e3e3e', '#405559', '#68868c', '#ededed'],
                                     'DESCRIPTION': ['Grey', 'Turquoise', 'Winter']},
                       'DarkTeal11': {'BACKGROUND': '#405559', 'TEXT': '#ededed', 'INPUT': '#68868c', 'TEXT_INPUT': '#ededed', 'SCROLL': '#68868c',
                                      'BUTTON': ('#ededed', '#68868c'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#3e3e3e', '#405559', '#68868c', '#ededed'],
                                      'DESCRIPTION': ['Grey', 'Turquoise', 'Winter']},
                       'LightBlue7': {'BACKGROUND': '#9ed0e0', 'TEXT': '#19483f', 'INPUT': '#5c868e', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#19483f',
                                      'BUTTON': ('#FFFFFF', '#19483f'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#19483f', '#5c868e', '#ff6a38', '#9ed0e0'],
                                      'DESCRIPTION': ['Orange', 'Blue', 'Turquoise']},
                       'LightGreen10': {'BACKGROUND': '#d8ebb5', 'TEXT': '#205d67', 'INPUT': '#639a67', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#205d67',
                                        'BUTTON': ('#d8ebb5', '#205d67'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#205d67', '#639a67', '#d9bf77', '#d8ebb5'],
                                        'DESCRIPTION': ['Blue', 'Green', 'Brown', 'Vintage']},
                       'DarkBlue15': {'BACKGROUND': '#151680', 'TEXT': '#f1fea4', 'INPUT': '#375fc0', 'TEXT_INPUT': '#f1fea4', 'SCROLL': '#375fc0',
                                      'BUTTON': ('#f1fea4', '#1c44ac'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#151680', '#1c44ac', '#375fc0', '#f1fea4'],
                                      'DESCRIPTION': ['Blue', 'Yellow', 'Cold']},
                       'DarkBlue16': {'BACKGROUND': '#1c44ac', 'TEXT': '#f1fea4', 'INPUT': '#375fc0', 'TEXT_INPUT': '#f1fea4', 'SCROLL': '#375fc0',
                                      'BUTTON': ('#f1fea4', '#151680'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#151680', '#1c44ac', '#375fc0', '#f1fea4'],
                                      'DESCRIPTION': ['Blue', 'Yellow', 'Cold']},
                       'DarkTeal12': {'BACKGROUND': '#004a7c', 'TEXT': '#fafafa', 'INPUT': '#e8f1f5', 'TEXT_INPUT': '#000000', 'SCROLL': '#e8f1f5',
                                      'BUTTON': ('#fafafa', '#005691'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#004a7c', '#005691', '#e8f1f5', '#fafafa'],
                                      'DESCRIPTION': ['Grey', 'Blue', 'Cold', 'Winter']},
                       'LightBrown13': {'BACKGROUND': '#ebf5ee', 'TEXT': '#921224', 'INPUT': '#bdc6b8', 'TEXT_INPUT': '#921224', 'SCROLL': '#921224',
                                        'BUTTON': ('#FFFFFF', '#921224'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#921224', '#bdc6b8', '#bce0da', '#ebf5ee'],
                                        'DESCRIPTION': ['Red', 'Blue', 'Grey', 'Vintage', 'Wedding']},
                       'DarkBlue17': {'BACKGROUND': '#21294c', 'TEXT': '#f9f2d7', 'INPUT': '#f2dea8', 'TEXT_INPUT': '#000000', 'SCROLL': '#f2dea8',
                                      'BUTTON': ('#f9f2d7', '#141829'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#141829', '#21294c', '#f2dea8', '#f9f2d7'],
                                      'DESCRIPTION': ['#000000', 'Blue', 'Yellow']},
                       'DarkBrown6': {'BACKGROUND': '#785e4d', 'TEXT': '#f2eee3', 'INPUT': '#baaf92', 'TEXT_INPUT': '#000000', 'SCROLL': '#baaf92',
                                      'BUTTON': ('#FFFFFF', '#785e4d'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#785e4d', '#ff8426', '#baaf92', '#f2eee3'],
                                      'DESCRIPTION': ['Grey', 'Brown', 'Orange', 'Autumn']},
                       'DarkGreen6': {'BACKGROUND': '#5c715e', 'TEXT': '#f2f9f1', 'INPUT': '#ddeedf', 'TEXT_INPUT': '#000000', 'SCROLL': '#ddeedf',
                                      'BUTTON': ('#f2f9f1', '#5c715e'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#5c715e', '#b6cdbd', '#ddeedf', '#f2f9f1'],
                                      'DESCRIPTION': ['Grey', 'Green', 'Vintage']},
                       'DarkGrey7': {'BACKGROUND': '#4b586e', 'TEXT': '#dddddd', 'INPUT': '#574e6d', 'TEXT_INPUT': '#dddddd', 'SCROLL': '#574e6d',
                                     'BUTTON': ('#dddddd', '#43405d'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#43405d', '#4b586e', '#574e6d', '#dddddd'],
                                     'DESCRIPTION': ['Grey', 'Winter', 'Cold']},
                       'DarkRed2': {'BACKGROUND': '#ab1212', 'TEXT': '#f6e4b5', 'INPUT': '#cd3131', 'TEXT_INPUT': '#f6e4b5', 'SCROLL': '#cd3131',
                                    'BUTTON': ('#f6e4b5', '#ab1212'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                    'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#ab1212', '#1fad9f', '#cd3131', '#f6e4b5'],
                                    'DESCRIPTION': ['Turquoise', 'Red', 'Yellow']},
                       'LightGrey6': {'BACKGROUND': '#e3e3e3', 'TEXT': '#233142', 'INPUT': '#455d7a', 'TEXT_INPUT': '#e3e3e3', 'SCROLL': '#233142',
                                      'BUTTON': ('#e3e3e3', '#455d7a'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#233142', '#455d7a', '#f95959', '#e3e3e3'],
                                      'DESCRIPTION': ['#000000', 'Blue', 'Red', 'Grey']},
                       'HotDogStand': {'BACKGROUND': 'red', 'TEXT': 'yellow', 'INPUT': 'yellow', 'TEXT_INPUT': '#000000', 'SCROLL': 'yellow',
                                      'BUTTON': ('red', 'yellow'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0,
                                     },
                       }


def ListOfLookAndFeelValues():
    """
    Get a list of the valid values to pass into your call to change_look_and_feel
    :return: List[str] - list of valid string values
    """
    return sorted(list(LOOK_AND_FEEL_TABLE.keys()))


def theme(new_theme=None):
    """
    Sets / Gets the current Theme.  If none is specified then returns the current theme.
    This call replaces the ChangeLookAndFeel / change_look_and_feel call which only sets the theme.

    :param new_theme: (str) the new theme name to use
    :return: (str) the currently selected theme
    """
    if new_theme is not None:
        change_look_and_feel(new_theme)
    return CURRENT_LOOK_AND_FEEL


def theme_background_color(color=None):
    """
    Sets/Returns the background color currently in use
    Used for Windows and containers (Column, Frame, Tab) and tables

    :return: (str) - color string of the background color currently in use
    :rtype: (str)
    """
    if color is not None:
        set_options(background_color=color)
    return DEFAULT_BACKGROUND_COLOR


def theme_element_background_color(color=None):
    """
    Sets/Returns the background color currently in use for all elements except containers

    :return: (str) - color string of the element background color currently in use
    :rtype: (str)
    """
    if color is not None:
        set_options(element_background_color=color)
    return DEFAULT_ELEMENT_BACKGROUND_COLOR


def theme_text_color(color=None):
    """
    Sets/Returns the text color currently in use

    :return: (str) - color string of the text color currently in use
    :rtype: (str)
    """
    if color is not None:
        set_options(text_color=color)
    return DEFAULT_TEXT_COLOR


def theme_text_element_background_color(color=None):
    """
    Sets/Returns the background color for text elements

    :return: (str) - color string of the text background color currently in use
    :rtype: (str)
    """
    if color is not None:
        set_options(text_element_background_color=color)
    return DEFAULT_TEXT_ELEMENT_BACKGROUND_COLOR

def theme_input_background_color(color=None):
    """
    Sets/Returns the input element background color currently in use

    :return: (str) - color string of the input element background color currently in use
    :rtype: (str)
    """
    if color is not None:
        set_options(input_elements_background_color=color)
    return DEFAULT_INPUT_ELEMENTS_COLOR


def theme_input_text_color(color=None):
    """
    Sets/Returns the input element entry color (not the text but the thing that's displaying the text)

    :return: (str) - color string of the input element color currently in use
    :rtype: (str)
    """
    if color is not None:
        set_options(input_text_color=color)
    return DEFAULT_INPUT_TEXT_COLOR



def theme_button_color(color=None):
    """
    Sets/Returns the button color currently in use

    :return: Tuple[str, str] - TUPLE with color strings of the button color currently in use (button text color, button background color)
    :rtype: (str)
    """
    if color is not None:
        set_options(button_color=color)
    return DEFAULT_BUTTON_COLOR


def theme_progress_bar_color(color=None):
    """
    Sets/Returns the progress bar colors by the current color theme

    :return: Tuple[str, str] - TUPLE with color strings of the ProgressBar color currently in use(button text color, button background color)
    :rtype: (str)
    """
    if color is not None:
        set_options(progress_meter_color=color)
    return DEFAULT_PROGRESS_BAR_COLOR


def theme_slider_color(color=None):
    """
    Sets/Returns the slider color (used for sliders)

    :return: (str) - color string of the slider color currently in use
    :rtype: (str)
    """
    if color is not None:
        set_options(scrollbar_color=color)
    return DEFAULT_SCROLLBAR_COLOR


def theme_border_width(border_width=None):
    """
    Sets/Returns the border width currently in use
    Used by non ttk elements at the moment

    :return: (int) - border width currently in use
    :rtype: (str)
    """
    if border_width is not None:
        set_options(border_width=border_width)
    return DEFAULT_BORDER_WIDTH


def theme_slider_border_width(border_width=None):
    """
    Sets/Returns the slider border width currently in use

    :return: (int) - border width currently in use
    :rtype: (str)
    """
    if border_width is not None:
        set_options(slider_border_width=border_width)
    return DEFAULT_SLIDER_BORDER_WIDTH


def theme_progress_bar_border_width(border_width=None):
    """
    Sets/Returns the progress meter border width currently in use

    :return: (int) - border width currently in use
    :rtype: (str)
    """
    if border_width is not None:
        set_options(progress_meter_border_depth=border_width)
    return DEFAULT_PROGRESS_BAR_BORDER_WIDTH



def theme_element_text_color(color=None):
    """
    Sets/Returns the text color used by elements that have text as part of their display (Tables, Trees and Sliders)

    :return: (str) - color string currently in use
    :rtype: (str)
    """
    if color is not None:
        set_options(element_text_color=color)
    return DEFAULT_ELEMENT_TEXT_COLOR


def theme_list():
    """
    Returns a sorted list of the currently available color themes

    :return: List[str] - A sorted list of the currently available color themes
    :rtype: (str)
    """
    return list_of_look_and_feel_values()


def theme_previewer(columns=12):
    """
    Show a window with all of the color themes - takes a while so be patient

    :param columns: (int) number of themes in a single row
    """
    preview_all_look_and_feel_themes(columns)

def ChangeLookAndFeel(index, force=False):
    """
    Change the "color scheme" of all future PySimpleGUI Windows.
    The scheme are string names that specify a group of colors. Background colors, text colors, button colors.
    There are 13 different color settings that are changed at one time using a single call to ChangeLookAndFeel
    The look and feel table itself has these indexes into the dictionary LOOK_AND_FEEL_TABLE.
    The original list was (prior to a major rework and renaming)... these names still work...
    In Nov 2019 a new Theme Formula was devised to make choosing a theme easier:
    The "Formula" is:
    ["Dark" or "Light"] Color Number
    Colors can be Blue Brown Grey Green Purple Red Teal Yellow Black
    The number will vary for each pair. There are more DarkGrey entries than there are LightYellow for example.
    Default = The default settings (only button color is different than system default)
    Default1 = The full system default including the button (everything's gray... how sad... don't be all gray... please....)
    :param index:  the name of the index into the Look and Feel table (does not have to be exact, can be "fuzzy")
    :type index: (str)
    :param force:  no longer used
    :type force: (bool)
    """

    global CURRENT_LOOK_AND_FEEL

    # if sys.platform.startswith('darwin') and not force:
    #     print('*** Changing look and feel is not supported on Mac platform ***')
    #     return

    theme = index
    # normalize available l&f values
    lf_values = [item.lower() for item in list_of_look_and_feel_values()]

    # option 1
    opt1 = theme.replace(' ', '').lower()

    # option 2 (reverse lookup)
    optx = theme.lower().split(' ')
    optx.reverse()
    opt2 = ''.join(optx)

    # search for valid l&f name
    if opt1 in lf_values:
        ix = lf_values.index(opt1)
    elif opt2 in lf_values:
        ix = lf_values.index(opt2)
    else:
        ix = randint(0, len(lf_values) - 1)
        print('** Warning - {} Theme is not a valid theme. Change your theme call. **'.format(index))
        print('valid values are', list_of_look_and_feel_values())
        print('Instead, please enjoy a random Theme named {}'.format(list_of_look_and_feel_values()[ix]))

    selection = list_of_look_and_feel_values()[ix]
    CURRENT_LOOK_AND_FEEL = selection
    try:
        colors = LOOK_AND_FEEL_TABLE[selection]

        # Color the progress bar using button background and input colors...unless they're the same
        if colors['PROGRESS'] != COLOR_SYSTEM_DEFAULT:
            if colors['BUTTON'][1] != colors['INPUT'] and colors['BUTTON'][1] != colors['BACKGROUND']:
                colors['PROGRESS'] = colors['BUTTON'][1], colors['INPUT']
            else:  # if the same, then use text input on top of input color
                colors['PROGRESS'] = (colors['TEXT_INPUT'], colors['INPUT'])
        else:
            colors['PROGRESS'] = DEFAULT_PROGRESS_BAR_COLOR_OFFICIAL
        # call to change all the colors
        SetOptions(background_color=colors['BACKGROUND'],
                   text_element_background_color=colors['BACKGROUND'],
                   element_background_color=colors['BACKGROUND'],
                   text_color=colors['TEXT'],
                   input_elements_background_color=colors['INPUT'],
                   # button_color=colors['BUTTON'] if not sys.platform.startswith('darwin') else None,
                   button_color=colors['BUTTON'],
                   progress_meter_color=colors['PROGRESS'],
                   border_width=colors['BORDER'],
                   slider_border_width=colors['SLIDER_DEPTH'],
                   progress_meter_border_depth=colors['PROGRESS_DEPTH'],
                   scrollbar_color=(colors['SCROLL']),
                   element_text_color=colors['TEXT'],
                   input_text_color=colors['TEXT_INPUT'])
    except:  # most likely an index out of range
        print('** Warning - Theme value not valid. Change your theme call. **')
        print('valid values are', list_of_look_and_feel_values())


def preview_all_look_and_feel_themes(columns=12):
    """
    Displays a "Quick Reference Window" showing all of the different Look and Feel settings that are available.
    They are sorted alphabetically.  The legacy color names are mixed in, but otherwise they are sorted into Dark and Light halves
    :param columns: (int) The number of themes to display per row
    """

    # Show a "splash" type message so the user doesn't give up waiting
    popup_quick_message('Hang on for a moment, this will take a bit to create....', background_color='red', text_color='#FFFFFF', auto_close=True, non_blocking=True)

    web = False

    win_bg = 'black'

    def sample_layout():
        return [[Text('Text element'), InputText('Input data here', size=(10, 1))],
                [Button('Ok'), Button('Cancel'), Slider((1, 10), orientation='h', size=(5, 15))]]

    layout = [[Text('Here is a complete list of themes', font='Default 18', background_color=win_bg)]]

    names = list_of_look_and_feel_values()
    names.sort()
    row = []
    for count, theme in enumerate(names):
        change_look_and_feel(theme)
        if not count % columns:
            layout += [row]
            row = []
        row += [Frame(theme, sample_layout() if not web else [[T(theme)]] + sample_layout())]
    if row:
        layout += [row]

    window = Window('Preview of all Look and Feel choices', layout, background_color=win_bg)
    window.read()
    window.close()


# ------------------------ Color processing functions ------------------------

def _hex_to_hsl(hex):
    r,g,b = _hex_to_rgb(hex)
    return _rgb_to_hsl(r,g,b)

def _hex_to_rgb(hex):
    hex = hex.lstrip('#')
    hlen = len(hex)
    return tuple(int(hex[i:i + hlen // 3], 16) for i in range(0, hlen, hlen // 3))


def _rgb_to_hsl(r, g, b):
    r = float(r)
    g = float(g)
    b = float(b)
    high = max(r, g, b)
    low = min(r, g, b)
    h, s, v = ((high + low) / 2,)*3
    if high == low:
        h = s = 0.0
    else:
        d = high - low
        l = (high + low) / 2
        s = d / (2 - high - low) if l > 0.5 else d / (high + low)
        h = {
            r: (g - b) / d + (6 if g < b else 0),
            g: (b - r) / d + 2,
            b: (r - g) / d + 4,
        }[high]
        h /= 6
    return h, s, v


def _hsl_to_rgb(h, s, l):
    def hue_to_rgb(p, q, t):
        t += 1 if t < 0 else 0
        t -= 1 if t > 1 else 0
        if t < 1/6: return p + (q - p) * 6 * t
        if t < 1/2: return q
        if t < 2/3: p + (q - p) * (2/3 - t) * 6
        return p

    if s == 0:
        r, g, b = l, l, l
    else:
        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r = hue_to_rgb(p, q, h + 1/3)
        g = hue_to_rgb(p, q, h)
        b = hue_to_rgb(p, q, h - 1/3)

    return r, g, b

def _hsv_to_hsl(h, s, v):
    l = 0.5 * v  * (2 - s)
    s = v * s / (1 - fabs(2*l-1))
    return h, s, l

def _hsl_to_hsv(h, s, l):
    v = (2*l + s*(1- fabs(2*l-1)))/2
    s = 2*(v-l)/v
    return h, s, v

# Converts an object's contents into a nice printable string.  Great for dumping debug data
def ObjToStringSingleObj(obj):
    """
    Dumps an Object's values as a formatted string.  Very nicely done. Great way to display an object's member variables in human form
    Returns only the top-most object's variables instead of drilling down to dispolay more
    :param obj: (Any) The object to display
    returns (str) Formatted output of the object's values
    """
    if obj is None:
        return 'None'
    return str(obj.__class__) + '\n' + '\n'.join(
        (repr(item) + ' = ' + repr(obj.__dict__[item]) for item in sorted(obj.__dict__)))


def ObjToString(obj, extra='    '):
    """
    Dumps an Object's values as a formatted string.  Very nicely done. Great way to display an object's member variables in human form
    :param obj: The object to display
    :type obj: (Any)
    :param extra:  (Default value = '    ')
    :type extra: (str)
    :return:  Formatted output of the object's values
    :rtype: (str)
    """
    if obj is None:
        return 'None'
    return str(obj.__class__) + '\n' + '\n'.join(
        (extra + (str(item) + ' = ' +
                  (ObjToString(obj.__dict__[item], extra + '    ') if hasattr(obj.__dict__[item], '__dict__') else str(
                      obj.__dict__[item])))
         for item in sorted(obj.__dict__)))


######
#     #   ####   #####   #    #  #####    ####
#     #  #    #  #    #  #    #  #    #  #
######   #    #  #    #  #    #  #    #   ####
#        #    #  #####   #    #  #####        #
#        #    #  #       #    #  #       #    #
#         ####   #        ####   #        ####


# ------------------------------------------------------------------------------------------------------------------ #
# =====================================   Upper PySimpleGUI ======================================================== #
# ------------------------------------------------------------------------------------------------------------------ #
# ----------------------------------- The mighty Popup! ------------------------------------------------------------ #

def Popup(*args, title=None, button_color=None, background_color=None, text_color=None, button_type=POPUP_BUTTONS_OK, auto_close=False,
          auto_close_duration=None, custom_text=(None, None), non_blocking=False, icon=None, line_width=None, font=None, no_titlebar=False, grab_anywhere=False,
          keep_on_top=False, location=(None, None)):
    """
    Popup - Display a popup Window with as many parms as you wish to include.  This is the GUI equivalent of the
    "print" statement.  It's also great for "pausing" your program's flow until the user can read some error messages.

    :param *args:  Variable number of your arguments.  Load up the call with stuff to see!
    :type *args: (Any)
    :param title:   Optional title for the window. If none provided, the first arg will be used instead.
    :type title: (str)
    :param button_color: Color of the buttons shown (text color, button color)
    :type button_color: Tuple[str, str]
    :param background_color:  Window's background color
    :type background_color: (str)
    :param text_color:  text color
    :type text_color: (str)
    :param button_type:  NOT USER SET!  Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). There are many Popup functions and they call Popup, changing this parameter to get the desired effect.
    :type button_type: (int)
    :param auto_close:  If True the window will automatically close
    :type auto_close: (bool)
    :param auto_close_duration:  time in seconds to keep window open before closing it automatically
    :type auto_close_duration: (int)
    :param custom_text:  A string or pair of strings that contain the text to display on the buttons
    :type custom_text: Union[Tuple[str, str], str]
    :param non_blocking:  If True then will immediately return from the function without waiting for the user's input.
    :type non_blocking: (bool)
    :param icon:  icon to display on the window. Same format as a Window call
    :type icon: Union[str, bytes]
    :param line_width:  Width of lines in characters.  Defaults to MESSAGE_BOX_LINE_WIDTH
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, tuple(font name, size, modifiers]
    :param no_titlebar:  If True will not show the frame around the window and the titlebar across the top
    :type no_titlebar: (bool)
    :param grab_anywhere:  If True can grab anywhere to move the window. If no_titlebar is True, grab_anywhere should likely be enabled too
    :type grab_anywhere: (bool)
    :param location:   Location on screen to display the top left corner of window. Defaults to window centered on screen
    :type location: Tuple[int, int]
    :return: Returns text of the button that was pressed.  None will be returned if user closed window with X
    :rtype: Union[str, None]
    """

    if not args:
        args_to_print = ['']
    else:
        args_to_print = args
    if line_width != None:
        local_line_width = line_width
    else:
        local_line_width = MESSAGE_BOX_LINE_WIDTH
    _title = title if title is not None else args_to_print[0]
    window = Window(_title, auto_size_text=True, background_color=background_color, button_color=button_color,
                    auto_close=auto_close, auto_close_duration=auto_close_duration, icon=icon, font=font,
                    no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)
    max_line_total, total_lines = 0, 0
    for message in args_to_print:
        # fancy code to check if string and convert if not is not need. Just always convert to string :-)
        # if not isinstance(message, str): message = str(message)
        message = str(message)
        if message.count('\n'):
            message_wrapped = message
        else:
            message_wrapped = textwrap.fill(message, local_line_width)
        message_wrapped_lines = message_wrapped.count('\n') + 1
        longest_line_len = max([len(l) for l in message.split('\n')])
        width_used = min(longest_line_len, local_line_width)
        max_line_total = max(max_line_total, width_used)
        # height = _GetNumLinesNeeded(message, width_used)
        height = message_wrapped_lines
        window.AddRow(
            Text(message_wrapped, auto_size_text=True, text_color=text_color, background_color=background_color))
        total_lines += height

    if non_blocking:
        PopupButton = DummyButton  # important to use or else button will close other windows too!
    else:
        PopupButton = Button
    # show either an OK or Yes/No depending on paramater
    if custom_text != (None, None):
        if type(custom_text) is not tuple:
            window.AddRow(PopupButton(custom_text, size=(len(custom_text), 1), button_color=button_color, focus=True,
                                      bind_return_key=True))
        elif custom_text[1] is None:
            window.AddRow(
                PopupButton(custom_text[0], size=(len(custom_text[0]), 1), button_color=button_color, focus=True,
                            bind_return_key=True))
        else:
            window.AddRow(PopupButton(custom_text[0], button_color=button_color, focus=True, bind_return_key=True,
                                      size=(len(custom_text[0]), 1)),
                          PopupButton(custom_text[1], button_color=button_color, size=(len(custom_text[0]), 1)))
    elif button_type is POPUP_BUTTONS_YES_NO:
        window.AddRow(PopupButton('Yes', button_color=button_color, focus=True, bind_return_key=True, pad=((20, 5), 3),
                                  size=(5, 1)), PopupButton('No', button_color=button_color, size=(5, 1)))
    elif button_type is POPUP_BUTTONS_CANCELLED:
        window.AddRow(
            PopupButton('Cancelled', button_color=button_color, focus=True, bind_return_key=True, pad=((20, 0), 3)))
    elif button_type is POPUP_BUTTONS_ERROR:
        window.AddRow(PopupButton('Error', size=(6, 1), button_color=button_color, focus=True, bind_return_key=True,
                                  pad=((20, 0), 3)))
    elif button_type is POPUP_BUTTONS_OK_CANCEL:
        window.AddRow(PopupButton('OK', size=(6, 1), button_color=button_color, focus=True, bind_return_key=True),
                      PopupButton('Cancel', size=(6, 1), button_color=button_color))
    elif button_type is POPUP_BUTTONS_NO_BUTTONS:
        pass
    else:
        window.AddRow(PopupButton('OK', size=(5, 1), button_color=button_color, focus=True, bind_return_key=True,
                                  pad=((20, 0), 3)))

    if non_blocking:
        button, values = window.Read(timeout=0)
    else:
        button, values = window.Read()
        window.close(); del window

    return button


# ==============================  MsgBox============#
# Lazy function. Same as calling Popup with parms   #
# This function WILL Disappear perhaps today        #
# ==================================================#
# MsgBox is the legacy call and should not be used any longer
def MsgBox(*args):
    """
    Do not call this anymore it will raise exception.  Use Popups instead
    :param *args:

    """
    raise DeprecationWarning('MsgBox is no longer supported... change your call to Popup')


# ========================  Scrolled Text Box   =====#
# ===================================================#
def PopupScrolled(*args, title=None, button_color=None, background_color=None, text_color=None, yes_no=False, auto_close=False, auto_close_duration=None,
                  size=(None, None), location=(None, None), non_blocking=False, no_titlebar=False, grab_anywhere=False, keep_on_top=False, font=None):
    """
    Show a scrolled Popup window containing the user's text that was supplied.  Use with as many items to print as you
    want, just like a print statement.

    :param *args: Variable number of items to display
    :type *args: (Any)
    :param title: Title to display in the window.
    :type title: (str)
    :param button_color:  button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param yes_no:  If True, displays Yes and No buttons instead of Ok
    :type yes_no: (bool)
    :param auto_close:   if True window will close itself
    :type auto_close:  (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param size:  (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param location:  Location on the screen to place the upper left corner of the window
    :type location: Tuple[int, int]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :return: Returns text of the button that was pressed.  None will be returned if user closed window with X
    :rtype: Union[str, None, TIMEOUT_KEY]
    """
    if not args: return
    width, height = size
    width = width if width else MESSAGE_BOX_LINE_WIDTH
    window = Window(title=title or args[0], auto_size_text=True, button_color=button_color, auto_close=auto_close,
                    auto_close_duration=auto_close_duration, location=location, resizable=True, font=font, background_color=background_color,
                    no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top)
    max_line_total, max_line_width, total_lines, height_computed = 0, 0, 0, 0
    complete_output = ''
    for message in args:
        # fancy code to check if string and convert if not is not need. Just always convert to string :-)
        # if not isinstance(message, str): message = str(message)
        message = str(message)
        longest_line_len = max([len(l) for l in message.split('\n')])
        width_used = min(longest_line_len, width)
        max_line_total = max(max_line_total, width_used)
        max_line_width = width
        lines_needed = _GetNumLinesNeeded(message, width_used)
        height_computed += lines_needed
        complete_output += message + '\n'
        total_lines += lines_needed
    height_computed = MAX_SCROLLED_TEXT_BOX_HEIGHT if height_computed > MAX_SCROLLED_TEXT_BOX_HEIGHT else height_computed
    if height:
        height_computed = height
    window.AddRow(Multiline(complete_output, size=(max_line_width, height_computed), background_color=background_color, text_color=text_color))
    pad = max_line_total - 15 if max_line_total > 15 else 1
    # show either an OK or Yes/No depending on paramater
    button = DummyButton if non_blocking else Button
    if yes_no:
        window.AddRow(Text('', size=(pad, 1), auto_size_text=False, background_color=background_color), button('Yes'), button('No'))
    else:
        window.AddRow(Text('', size=(pad, 1), auto_size_text=False, background_color=background_color),
                      button('OK', size=(5, 1), button_color=button_color))

    if non_blocking:
        button, values = window.Read(timeout=0)
    else:
        button, values = window.Read()
        window.close(); del window
    return button


ScrolledTextBox = PopupScrolled

# ============================== sprint ======#
# Is identical to the Scrolled Text Box       #
# Provides a crude 'print' mechanism but in a #
# GUI environment                             #
# This is in addition to the Print function   #
# which routes output to a "Debug Window"     #
# ============================================#
sprint = ScrolledTextBox


# --------------------------- PopupNoButtons ---------------------------
def PopupNoButtons(*args, title=None, background_color=None, text_color=None, auto_close=False,
                   auto_close_duration=None, non_blocking=False, icon=None, line_width=None, font=None,
                   no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """Show a Popup but without any buttons

    :param *args: Variable number of items to display
    :type *args: (Any)
    :param title: Title to display in the window.
    :type title: (str)
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close:  if True window will close itself
    :type auto_close:  (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking:  If True then will immediately return from the function without waiting for the user's input. (Default = False)
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True, than can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param location:  Location of upper left corner of the window
    :type location: Tuple[int, int]
    """
    Popup(*args, title=title, button_color=None, background_color=background_color, text_color=text_color,
          button_type=POPUP_BUTTONS_NO_BUTTONS,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


# --------------------------- PopupNonBlocking ---------------------------
def PopupNonBlocking(*args, title=None, button_type=POPUP_BUTTONS_OK, button_color=None, background_color=None,
                     text_color=None,
                     auto_close=False, auto_close_duration=None, non_blocking=True, icon=None,
                     line_width=None, font=None, no_titlebar=False, grab_anywhere=False, keep_on_top=False,
                     location=(None, None)):
    """
    Show Popup window and immediately return (does not block)

    :param *args: Variable number of items to display
    :type *args: (Any)
    :param title: Title to display in the window.
    :type title: (str)
    :param button_type: Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK).
    :type button_type: (int)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close:  if True window will close itself
    :type auto_close:  (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True: can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param location:  Location of upper left corner of the window
    :type location: Tuple[int, int]
    """
    Popup(*args, title=title, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=button_type,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


PopupNoWait = PopupNonBlocking


# --------------------------- PopupQuick - a NonBlocking, Self-closing Popup  ---------------------------
def PopupQuick(*args, title=None, button_type=POPUP_BUTTONS_OK, button_color=None, background_color=None,
               text_color=None,
               auto_close=True, auto_close_duration=2, non_blocking=True, icon=None, line_width=None,
               font=None, no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
    Show Popup box that doesn't block and closes itself

    :param *args: Variable number of items to display
    :type *args: (Any)
    :param title: Title to display in the window.
    :type title: (str)
    :param button_type: Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK).
    :type button_type: (int)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close:  if True window will close itself
    :type auto_close:  (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True: can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param location:  Location of upper left corner of the window
    :type location: Tuple[int, int]

    """
    Popup(*args, title=title, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=button_type,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


# --------------------------- PopupQuick - a NonBlocking, Self-closing Popup with no titlebar and no buttons ---------------------------
def PopupQuickMessage(*args, title=None, button_type=POPUP_BUTTONS_NO_BUTTONS, button_color=None, background_color=None,
                      text_color=None,
                      auto_close=True, auto_close_duration=2, non_blocking=True, icon=None,
                      line_width=None,
                      font=None, no_titlebar=True, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
    Show Popup window with no titlebar, doesn't block, and auto closes itself.

    :param *args: Variable number of items to display
    :type *args: (Any)
    :param title: Title to display in the window.
    :type title: (str)
    :param button_type: Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK).
    :type button_type: (int)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close:  if True window will close itself
    :type auto_close:  (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True: can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param location:  Location of upper left corner of the window
    :type location: Tuple[int, int]
    """
    Popup(*args, title=title, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=button_type,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


# --------------------------- PopupNoTitlebar ---------------------------
def PopupNoTitlebar(*args, title=None, button_type=POPUP_BUTTONS_OK, button_color=None, background_color=None,
                    text_color=None,
                    auto_close=False, auto_close_duration=None, non_blocking=False, icon=None,
                    line_width=None, font=None, grab_anywhere=True, keep_on_top=False, location=(None, None)):
    """
    Display a Popup without a titlebar.   Enables grab anywhere so you can move it

    :param *args: Variable number of items to display
    :type *args: (Any)
    :param title: Title to display in the window.
    :type title: (str)
    :param button_type: Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK).
    :type button_type: (int)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close:  if True window will close itself
    :type auto_close:  (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param grab_anywhere: If True: can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location:  Location of upper left corner of the window
    :type location: Tuple[int, int]
    """
    Popup(*args, title=title, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=button_type,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=True, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


PopupNoFrame = PopupNoTitlebar
PopupNoBorder = PopupNoTitlebar
PopupAnnoying = PopupNoTitlebar


# --------------------------- PopupAutoClose ---------------------------
def PopupAutoClose(*args, title=None, button_type=POPUP_BUTTONS_OK, button_color=None, background_color=None,
                   text_color=None,
                   auto_close=True, auto_close_duration=None, non_blocking=False, icon=None,
                   line_width=None, font=None, no_titlebar=False, grab_anywhere=False, keep_on_top=False,
                   location=(None, None)):
    """Popup that closes itself after some time period

    :param *args: Variable number of items to display
    :type *args: (Any)
    :param title: Title to display in the window.
    :type title: (str)
    :param button_type: Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK).
    :type button_type: (int)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close:  if True window will close itself
    :type auto_close:  (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True: can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location:  Location of upper left corner of the window
    :type location: Tuple[int, int]

    """
    Popup(*args, title=title, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=button_type,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


PopupTimed = PopupAutoClose


# --------------------------- PopupError ---------------------------
def PopupError(*args, title=None, button_color=(None, None), background_color=None, text_color=None, auto_close=False,
               auto_close_duration=None, non_blocking=False, icon=None, line_width=None, font=None,
               no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
    Popup with colored button and 'Error' as button text

    :param *args: Variable number of items to display
    :type *args: (Any)
    :param title: Title to display in the window.
    :type title: (str)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close:  if True window will close itself
    :type auto_close:  (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True: can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location:  Location of upper left corner of the window
    :type location: Tuple[int, int]
    """
    tbutton_color = DEFAULT_ERROR_BUTTON_COLOR if button_color == (None, None) else button_color
    return Popup(*args, title=title, button_type=POPUP_BUTTONS_ERROR, background_color=background_color, text_color=text_color,
                 non_blocking=non_blocking, icon=icon, line_width=line_width, button_color=tbutton_color,
                 auto_close=auto_close,
                 auto_close_duration=auto_close_duration, font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere,
                 keep_on_top=keep_on_top, location=location)


# --------------------------- PopupCancel ---------------------------
def PopupCancel(*args, title=None, button_color=None, background_color=None, text_color=None, auto_close=False,
                auto_close_duration=None, non_blocking=False, icon=None, line_width=None, font=None,
                no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
    Display Popup with "cancelled" button text

    :param *args: Variable number of items to display
    :type *args: (Any)
    :param title: Title to display in the window.
    :type title: (str)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close:  if True window will close itself
    :type auto_close:  (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True: can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location:  Location of upper left corner of the window
    :type location: Tuple[int, int]
    """
    return Popup(*args, title=title, button_type=POPUP_BUTTONS_CANCELLED, background_color=background_color,
                 text_color=text_color,
                 non_blocking=non_blocking, icon=icon, line_width=line_width, button_color=button_color, auto_close=auto_close,
                 auto_close_duration=auto_close_duration, font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere,
                 keep_on_top=keep_on_top, location=location)


# --------------------------- PopupOK ---------------------------
def PopupOK(*args, title=None, button_color=None, background_color=None, text_color=None, auto_close=False,
            auto_close_duration=None, non_blocking=False, icon=None, line_width=None, font=None,
            no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
    Display Popup with OK button only

    :param *args: Variable number of items to display
    :type *args: (Any)
    :param title: Title to display in the window.
    :type title: (str)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close:  if True window will close itself
    :type auto_close:  (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True: can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location:  Location of upper left corner of the window
    :type location: Tuple[int, int]
    """
    return Popup(*args, title=title, button_type=POPUP_BUTTONS_OK, background_color=background_color, text_color=text_color,
                 non_blocking=non_blocking, icon=icon, line_width=line_width, button_color=button_color, auto_close=auto_close,
                 auto_close_duration=auto_close_duration, font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere,
                 keep_on_top=keep_on_top, location=location)


# --------------------------- PopupOKCancel ---------------------------
def PopupOKCancel(*args, title=None, button_color=None, background_color=None, text_color=None, auto_close=False,
                  auto_close_duration=None, non_blocking=False, icon=DEFAULT_WINDOW_ICON, line_width=None, font=None,
                  no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
    Display popup with OK and Cancel buttons

    :param *args: Variable number of items to display
    :type *args: (Any)
    :param title: Title to display in the window.
    :type title: (str)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close:  if True window will close itself
    :type auto_close:  (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True: can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location:  Location of upper left corner of the window
    :type location: Tuple[int, int]
    :return: clicked button
    :rtype: Union["OK", "Cancel", None]
    """
    return Popup(*args, title=title, button_type=POPUP_BUTTONS_OK_CANCEL, background_color=background_color,
                 text_color=text_color,
                 non_blocking=non_blocking, icon=icon, line_width=line_width, button_color=button_color,
                 auto_close=auto_close, auto_close_duration=auto_close_duration, font=font, no_titlebar=no_titlebar,
                 grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


# --------------------------- PopupYesNo ---------------------------
def PopupYesNo(*args, title=None, button_color=None, background_color=None, text_color=None, auto_close=False,
               auto_close_duration=None, non_blocking=False, icon=None, line_width=None, font=None,
               no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
    Display Popup with Yes and No buttons

    :param *args: Variable number of items to display
    :type *args: (Any)
    :param title: Title to display in the window.
    :type title: (str)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close:  if True window will close itself
    :type auto_close:  (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True: can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location:  Location of upper left corner of the window
    :type location: Tuple[int, int]
    :return: clicked button
    :rtype: Union["Yes", "No", None]
    """
    return Popup(*args, title=title, button_type=POPUP_BUTTONS_YES_NO, background_color=background_color,
                 text_color=text_color,
                 non_blocking=non_blocking, icon=icon, line_width=line_width, button_color=button_color,
                 auto_close=auto_close, auto_close_duration=auto_close_duration, font=font, no_titlebar=no_titlebar,
                 grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


##############################################################################
#   The PopupGet_____ functions - Will return user input                     #
##############################################################################

# --------------------------- PopupGetFolder ---------------------------


def PopupGetFolder(message, title=None, default_path='', no_window=False, size=(None, None), button_color=None,
                   background_color=None, text_color=None, icon=None, font=None, no_titlebar=False,
                   grab_anywhere=False, keep_on_top=False, location=(None, None), initial_folder=None):
    """
    Display popup with text entry field and browse button so that a folder can be chosen.

    :param message:  message displayed to user
    :type message: (str)
    :param title:  Window title
    :type title: (str)
    :param default_path: path to display to user as starting point (filled into the input field)
    :type default_path: (str)
    :param no_window:  if True, no PySimpleGUI window will be shown. Instead just the tkinter dialog is shown
    :type no_window: (bool)
    :param size: (width, height) of the InputText Element
    :type size: Tuple[int, int]
    :param button_color:  button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param font: specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True: can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location:  Location of upper left corner of the window
    :type location: Tuple[int, int]
    :param initial_folder:  location in filesystem to begin browsing
    :type initial_folder: (str)
    :return: string representing the path chosen, None if cancelled or window closed with X
    :rtype: Union[str, None]
    """

    # global _my_windows
    if no_window:
        if not Window.hidden_master_root:
            # if first window being created, make a throwaway, hidden master root.  This stops one user
            # window from becoming the child of another user window. All windows are children of this
            # hidden window
            Window._IncrementOpenCount()
            Window.hidden_master_root = tk.Tk()
            Window.hidden_master_root.attributes('-alpha', 0)  # HIDE this window really really really
            Window.hidden_master_root.wm_overrideredirect(True)
            Window.hidden_master_root.withdraw()
        root = tk.Toplevel()

        try:
            root.attributes('-alpha', 0)  # hide window while building it. makes for smoother 'paint'
            root.wm_overrideredirect(True)
            root.withdraw()
        except:
            pass
        folder_name = tk.filedialog.askdirectory()  # show the 'get folder' dialog box

        root.destroy()
        if Window.NumOpenWindows == 1:
            Window.NumOpenWindows = 0
            Window.hidden_master_root.destroy()
            Window.hidden_master_root = None

        return folder_name

    layout = [[Text(message, auto_size_text=True, text_color=text_color, background_color=background_color)],
              [InputText(default_text=default_path, size=size, key='_INPUT_'),
               FolderBrowse(initial_folder=initial_folder)],
              [Button('Ok', size=(5, 1), bind_return_key=True), Button('Cancel', size=(5, 1))]]

    window = Window(title=title or message, layout=layout, icon=icon, auto_size_text=True, button_color=button_color,
                    background_color=background_color,
                    font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top,
                    location=location)

    button, values = window.Read()
    window.close(); del window
    if button != 'Ok':
        return None
    else:
        return values['_INPUT_']


# --------------------------- PopupGetFile ---------------------------

def PopupGetFile(message, title=None, default_path='', default_extension='', save_as=False, multiple_files=False,
                 file_types=(("ALL Files", "*.*"),),
                 no_window=False, size=(None, None), button_color=None, background_color=None, text_color=None,
                 icon=None, font=None, no_titlebar=False, grab_anywhere=False, keep_on_top=False,
                 location=(None, None), initial_folder=None):
    """
    Display popup window with text entry field and browse button so that a file can be chosen by user.

    :param message:  message displayed to user
    :type message: (str)
    :param title:  Window title
    :type title: (str)
    :param default_path: path to display to user as starting point (filled into the input field)
    :type default_path: (str)
    :param default_extension:  If no extension entered by user, add this to filename (only used in saveas dialogs)
    :type default_extension: (str)
    :param save_as: if True, the "save as" dialog is shown which will verify before overwriting
    :type save_as: (bool)
    :param multiple_files:  if True, then allows multiple files to be selected that are returned with ';' between each filename
    :type multiple_files: (bool)
    :param file_types: List of extensions to show using wildcards. All files (the default) = (("ALL Files", "*.*"),)
    :type file_types:  Tuple[Tuple[str,str]]
    :param no_window:  if True, no PySimpleGUI window will be shown. Instead just the tkinter dialog is shown
    :type no_window:  (bool)
    :param size: (width, height) of the InputText Element
    :type size: Tuple[int, int]
    :param button_color: Color of the button (text, background)
    :type button_color: Tuple[str, str]
    :param background_color: background color of the entire window
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param font: specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True: can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location:  Location of upper left corner of the window
    :type location: Tuple[int, int]
    :param initial_folder:  location in filesystem to begin browsing
    :type initial_folder: (str)
    :return: string representing the file(s) chosen, None if cancelled or window closed with X
    :rtype: Union[str, None]
    """

    if no_window:
        if not Window.hidden_master_root:
            # if first window being created, make a throwaway, hidden master root.  This stops one user
            # window from becoming the child of another user window. All windows are children of this
            # hidden window
            Window._IncrementOpenCount()
            Window.hidden_master_root = tk.Tk()
            Window.hidden_master_root.attributes('-alpha', 0)  # HIDE this window really really really
            Window.hidden_master_root.wm_overrideredirect(True)
            Window.hidden_master_root.withdraw()
        root = tk.Toplevel()

        try:
            root.attributes('-alpha', 0)  # hide window while building it. makes for smoother 'paint'
            root.wm_overrideredirect(True)
            root.withdraw()
        except:
            pass
        # TODO - Macs will not like this code because of the filetypes being used.  Need another Darwin check.
        if save_as:
            filename = tk.filedialog.asksaveasfilename(filetypes=file_types,
                                                       initialdir=initial_folder,
                                                       defaultextension=default_extension)  # show the 'get file' dialog box
        elif multiple_files:
            filename = tk.filedialog.askopenfilenames(filetypes=file_types,
                                                      initialdir=initial_folder,
                                                      defaultextension=default_extension)  # show the 'get file' dialog box
        else:
            filename = tk.filedialog.askopenfilename(filetypes=file_types,
                                                     initialdir=initial_folder,
                                                     defaultextension=default_extension)  # show the 'get files' dialog box

        root.destroy()
        if Window.NumOpenWindows == 1:
            Window.NumOpenWindows = 0
            Window.hidden_master_root.destroy()
            Window.hidden_master_root = None
        if not multiple_files and type(filename) in (tuple, list):
            if len(filename):  # only if not 0 length, otherwise will get an error
                filename = filename[0]
        return filename

    if save_as:
        browse_button = SaveAs(file_types=file_types, initial_folder=initial_folder)
    elif multiple_files:
        browse_button = FilesBrowse(file_types=file_types, initial_folder=initial_folder)
    else:
        browse_button = FileBrowse(file_types=file_types, initial_folder=initial_folder)

    layout = [[Text(message, auto_size_text=True, text_color=text_color, background_color=background_color)],
              [InputText(default_text=default_path, size=size, key='_INPUT_'), browse_button],
              [Button('Ok', size=(6, 1), bind_return_key=True), Button('Cancel', size=(6, 1))]]

    window = Window(title=title or message, layout=layout, icon=icon, auto_size_text=True, button_color=button_color,
                    font=font,
                    background_color=background_color,
                    no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)

    button, values = window.Read()
    window.close(); del window
    if button != 'Ok':
        return None
    else:
        path = values['_INPUT_']
        return path


# --------------------------- PopupGetText ---------------------------

def PopupGetText(message, title=None, default_text='', password_char='', size=(None, None), button_color=None,
                 background_color=None, text_color=None, icon=None, font=None, no_titlebar=False,
                 grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
    Display Popup with text entry field. Returns the text entered or None if closed / cancelled

    :param message: (str) message displayed to user
    :type message: (str)
    :param title: (str) Window title
    :type title: (str)
    :param default_text:  (str) default value to put into input area
    :type default_text: (str)
    :param password_char: (str) character to be shown instead of actually typed characters
    :type password_char: (str)
    :param size: (width, height) of the InputText Element
    :type size: Tuple[int, int]
    :param button_color:  Color of the button (text, background)
    :type button_color: Tuple[str, str]
    :param background_color: (str) background color of the entire window
    :type background_color: (str)
    :param text_color: (str) color of the message text
    :type text_color: (str)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param font: specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: (bool) If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: (bool) If True can click and drag anywhere in the window to move the window
    :type grab_anywhere: (bool)
    :param keep_on_top: (bool) If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location: (x,y) Location on screen to display the upper left corner of window
    :type location: Tuple[int, int]
    :return: Text entered or None if window was closed or cancel button clicked
    :rtype: Union[str, None]
    """

    layout = [[Text(message, auto_size_text=True, text_color=text_color, background_color=background_color, font=font)],
              [InputText(default_text=default_text, size=size, key='_INPUT_', password_char=password_char)],
              [Button('Ok', size=(5, 1), bind_return_key=True), Button('Cancel', size=(5, 1))]]

    window = Window(title=title or message, layout=layout, icon=icon, auto_size_text=True, button_color=button_color,
                    no_titlebar=no_titlebar,
                    background_color=background_color, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top,
                    location=location)

    button, values = window.Read()
    window.close(); del window
    if button != 'Ok':
        return None
    else:
        path = values['_INPUT_']
        return path



def popup_get_date(start_mon, start_day,  start_year, begin_at_sunday_plus=0, location=(None, None)):
    """
    Display a calendar window, get the user's choice, return as a tuple (mon, day, year)

    :param start_mon: The starting month
    :type start_mon: int
    :param start_day: The starting day - optional. Set to 0 if no date to be chosen at start
    :type start_day: int
    :param start_year: The starting year
    :type start_year: int
    :param begin_at_sunday_plus: Determines the left-most day in the display. 0=sunday, 1=monday, etc
    :type begin_at_sunday_plus: int
    :return: Tuple containing (month, day, year) of chosen date or None if was cancelled
    :rtype: None or (int, int, int)
    """

    day_font = 'TkFixedFont 8'
    mon_year_font = 'TkFixedFont 10'
    arrow_font = 'TkFixedFont 8'

    def update_days(window, month, year, begin_at_sunday_plus):
        [window[(week, day)].update('') for day in range(7) for week in range(6)]
        weeks = cal.monthcalendar(year, month)
        month_days = list(itertools.chain.from_iterable([[0 for _ in range(8 - begin_at_sunday_plus)]] + weeks))
        if month_days[6] == 0:
            month_days = month_days[7:]
            if month_days[6] == 0:
                month_days = month_days[7:]
        for i, day in enumerate(month_days):
            offset = i
            if offset >= 6 * 7:
                break
            window[(offset // 7, offset % 7)].update(str(day) if day else '')

    def make_days_layout():
        days_layout = []
        for week in range(6):
            row = []
            for day in range(7):
                row.append(T('', size=(4, 1), justification='c', font=day_font, key=(week, day), enable_events=True, pad=(0, 0)))
            days_layout.append(row)
        return days_layout

    cur_month = start_mon
    cur_year = start_year
    cur_day = start_day

    days_layout = make_days_layout()

    layout = [[B('◄', font=arrow_font, border_width=0, key='-MON-DOWN-'),
               Text('{} {}'.format(cal.month_name[cur_month], cur_year), size=(16,1), justification='c', font=mon_year_font, key='-MON-YEAR-'),
               B('►', font=arrow_font,border_width=0, key='-MON-UP-')]]
    layout += [[Col([[T(cal.day_abbr[i - (8 - begin_at_sunday_plus) % 7], size=(4,1), font=day_font, background_color=theme_text_color(), text_color=theme_background_color(), pad=(0,0)) for i in range(7)]], background_color=theme_text_color(), pad=(0,0))]]
    layout += days_layout
    layout += [[Button('Ok', border_width=0,font='TkFixedFont 8'), Button('Cancel',border_width=0, font='TkFixedFont 8')]]

    window = Window('Window Title', layout, no_titlebar=True, grab_anywhere=True, keep_on_top=True, font='TkFixedFont 12', use_default_focus=False, location=location, finalize=True)

    update_days(window, cur_month, cur_year, begin_at_sunday_plus)

    prev_choice = chosen_mon_day_year = None

    if cur_day:
        chosen_mon_day_year = cur_month, cur_day, cur_year
        for week in range(6):
            for day in range(7):
                if window[(week,day)].DisplayText == str(cur_day):
                    window[(week,day)].update(background_color=theme_text_color(), text_color=theme_background_color())
                    prev_choice = (week,day)
                    break

    while True:             # Event Loop
        event, values = window.read()
        if event in (None, 'Cancel'):
            chosen_mon_day_year = None
            break
        if event == 'Ok':
            break
        if event in ('-MON-UP-', '-MON-DOWN-'):
            cur_month += 1 if event == '-MON-UP-' else -1
            if cur_month > 12:
                cur_month = 1
                cur_year += 1
            elif cur_month < 1:
                cur_month = 12
                cur_year -= 1
            window['-MON-YEAR-'].update('{} {}'.format(cal.month_name[cur_month], cur_year))
            update_days(window, cur_month, cur_year, begin_at_sunday_plus)
            if prev_choice:
                window[prev_choice].update(background_color=theme_background_color(), text_color=theme_text_color())
        elif type(event) is tuple:
            if window[event].DisplayText != "":
                chosen_mon_day_year = cur_month, int(window[event].DisplayText), cur_year
                if prev_choice:
                    window[prev_choice].update(background_color=theme_background_color(), text_color=theme_text_color())
                window[event].update(background_color=theme_text_color(), text_color=theme_background_color())
                prev_choice = event
    window.close()
    return chosen_mon_day_year




# --------------------------- PopupAnimated ---------------------------

def PopupAnimated(image_source, message=None, background_color=None, text_color=None, font=None, no_titlebar=True, grab_anywhere=True, keep_on_top=True, location=(None, None), alpha_channel=None, time_between_frames=0, transparent_color=None, title=''):
    """
     Show animation one frame at a time.  This function has its own internal clocking meaning you can call it at any frequency
     and the rate the frames of video is shown remains constant.  Maybe your frames update every 30 ms but your
     event loop is running every 10 ms.  You don't have to worry about delaying, just call it every time through the
     loop.

    :param image_source:  Either a filename or a base64 string.
    :type image_source: Union[str, bytes]
    :param message:  An optional message to be shown with the animation
    :type message: (str)
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, tuple]
    :param no_titlebar:   If True then the titlebar and window frame will not be shown
    :type no_titlebar: (bool)
    :param grab_anywhere:  If True then you can move the window just clicking anywhere on window, hold and drag
    :type grab_anywhere: (bool)
    :param keep_on_top:   If True then Window will remain on top of all other windows currently shownn
    :type keep_on_top:  (bool)
    :param location:   (x,y) location on the screen to place the top left corner of your window. Default is to center on screen
    :type location:  (int, int)
    :param alpha_channel:  Window transparency 0 = invisible 1 = completely visible. Values between are see through
    :type alpha_channel: (float)
    :param time_between_frames:  Amount of time in milliseconds between each frame
    :type time_between_frames: (int)
    :param transparent_color:  This color will be completely see-through in your window. Can even click through
    :type transparent_color: (str)
    :param title:  Title that will be shown on the window
    :type title: (str)
    """
    if image_source is None:
        for image in Window._animated_popup_dict:
            window = Window._animated_popup_dict[image]
            window.Close()
        Window._animated_popup_dict = {}
        return

    if image_source not in Window._animated_popup_dict:
        if type(image_source) is bytes or len(image_source) > 300:
            layout = [[Image(data=image_source, background_color=background_color, key='_IMAGE_', )], ]
        else:
            layout = [[Image(filename=image_source, background_color=background_color, key='_IMAGE_', )], ]
        if message:
            layout.append([Text(message, background_color=background_color, text_color=text_color, font=font)])

        window = Window(title, layout, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere,
                        keep_on_top=keep_on_top, background_color=background_color, location=location,
                        alpha_channel=alpha_channel, element_padding=(0, 0), margins=(0, 0),
                        transparent_color=transparent_color, finalize=True, element_justification='c')
        Window._animated_popup_dict[image_source] = window
    else:
        window = Window._animated_popup_dict[image_source]
        window.Element('_IMAGE_').UpdateAnimation(image_source, time_between_frames=time_between_frames)

    window.refresh() # call refresh instead of Read to save significant CPU time


# Popup Notify
def popup_notify(*args, title='', icon=SYSTEM_TRAY_MESSAGE_ICON_INFORMATION, display_duration_in_ms=SYSTEM_TRAY_MESSAGE_DISPLAY_DURATION_IN_MILLISECONDS,
               fade_in_duration=SYSTEM_TRAY_MESSAGE_FADE_IN_DURATION, alpha=0.9, location=None):
    """
    Displays a "notification window", usually in the bottom right corner of your display.  Has an icon, a title, and a message.  It is more like a "toaster" window than the normal popups.

    The window will slowly fade in and out if desired.  Clicking on the window will cause it to move through the end the current "phase". For example, if the window was fading in and it was clicked, then it would immediately stop fading in and instead be fully visible.  It's a way for the user to quickly dismiss the window.

    The return code specifies why the call is returning (e.g. did the user click the message to dismiss it)

    :param title: (str) Text to be shown at the top of the window in a larger font
    :type title: (str)
    :param message: (str) Text message that makes up the majority of the window
    :type message: (str)
    :param icon: A base64 encoded PNG/GIF image or PNG/GIF filename that will be displayed in the window
    :type icon: Union[bytes, str]
    :param display_duration_in_ms: (int) Number of milliseconds to show the window
    :type display_duration_in_ms: (int)
    :param fade_in_duration: (int) Number of milliseconds to fade window in and out
    :type fade_in_duration: (int)
    :param alpha: (float) Alpha channel. 0 - invisible 1 - fully visible
    :type alpha: (float)
    :param location: Location on the screen to display the window
    :type location: Tuple[int, int]
    :return: reason for returning
    :rtype: (int)
    """

    if not args:
        args_to_print = ['']
    else:
        args_to_print = args
    output = ''
    max_line_total, total_lines, local_line_width = 0, 0, SYSTEM_TRAY_MESSAGE_MAX_LINE_LENGTH
    for message in args_to_print:
        # fancy code to check if string and convert if not is not need. Just always convert to string :-)
        # if not isinstance(message, str): message = str(message)
        message = str(message)
        if message.count('\n'):
            message_wrapped = message
        else:
            message_wrapped = textwrap.fill(message, local_line_width)
        message_wrapped_lines = message_wrapped.count('\n') + 1
        longest_line_len = max([len(l) for l in message.split('\n')])
        width_used = min(longest_line_len, local_line_width)
        max_line_total = max(max_line_total, width_used)
        # height = _GetNumLinesNeeded(message, width_used)
        height = message_wrapped_lines
        output += message_wrapped+'\n'
        total_lines += height

    message = output

    # def __init__(self, menu=None, filename=None, data=None, data_base64=None, tooltip=None, metadata=None):
    return SystemTray.notify(title=title, message=message, icon=icon, display_duration_in_ms=display_duration_in_ms, fade_in_duration=fade_in_duration, alpha=alpha, location=location)



#####################################################################
# Animated window while shell command is executed
#####################################################################

def _process_thread(*args):
    global __shell_process__

    # start running the command with arugments
    # print(f'running args = {args}')
    try:
        __shell_process__ = run(args, shell=True, stdout=PIPE)
    except Exception as e:
        print(f'Exception running process args = {args}')
        __shell_process__ = None


def shell_with_animation(command, args=None, image_source=DEFAULT_BASE64_LOADING_GIF, message=None, background_color=None, text_color=None, font=None, no_titlebar=True, grab_anywhere=True, keep_on_top=True, location=(None, None), alpha_channel=None, time_between_frames=100, transparent_color=None):
    """
    Execute a "shell command" (anything capable of being launched using subprocess.run) and
    while the command is running, show an animated popup so that the user knows that a long-running
    command is being executed.  Without this mechanism, the GUI appears locked up.

    :param command: (str) The command to run
    :type command: (str)
    :param args: List[str] List of arguments
    :type args: List[str]
    :param image_source: Either a filename or a base64 string.
    :type image_source: Union[str, bytes]
    :param message:  An optional message to be shown with the animation
    :type message: (str)
    :param background_color: (str) color of background
    :type background_color: (str)
    :param text_color:  color of the text
    :type text_color: (str)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, tuple]
    :param no_titlebar: If True then the titlebar and window frame will not be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True then you can move the window just clicking anywhere on window, hold and drag
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True then Window will remain on top of all other windows currently shownn
    :type keep_on_top: (bool)
    :param location:  (x,y) location on the screen to place the top left corner of your window. Default is to center on screen
    :type location: (int, int)
    :param alpha_channel:  Window transparency 0 = invisible 1 = completely visible. Values between are see through
    :type alpha_channel: (float)
    :param time_between_frames: Amount of time in milliseconds between each frame
    :type time_between_frames: (int)
    :param transparent_color: This color will be completely see-through in your window. Can even click through
    :type transparent_color: (str)
    :return: The resulting string output from stdout
    :rtype: (str)
    """

    global __shell_process__

    real_args = [command]
    if args is not None:
        for arg in args:
            real_args.append(arg)
        # real_args.append(args)
    thread = Thread(target=_process_thread, args=real_args, daemon=True)
    thread.start()

    # Poll to see if the thread is still running.  If so, then continue showing the animation
    while True:
        popup_animated(image_source=image_source, message=message, time_between_frames=time_between_frames, transparent_color=transparent_color, text_color=text_color, background_color=background_color, font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location, alpha_channel=alpha_channel)
        thread.join(timeout=time_between_frames/1000)
        if not thread.is_alive():
            break
    popup_animated(None)    # stop running the animation

    output = __shell_process__.__str__().replace('\\r\\n', '\n')    # fix up the output string
    output = output[output.index("stdout=b'")+9:-2]
    return output



#####################################################################################################
# Debugger
#####################################################################################################


PSGDebugLogo = b'R0lGODlhMgAtAPcAAAAAADD/2akK/4yz0pSxyZWyy5u3zZ24zpW30pG52J250J+60aC60KS90aDC3a3E163F2K3F2bPI2bvO3rzP3qvJ4LHN4rnR5P/zuf/zuv/0vP/0vsDS38XZ6cnb6f/xw//zwv/yxf/1w//zyP/1yf/2zP/3z//30wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAyAC0AAAj/AP8JHEiwoMGDCBMqXMiwoUOFAiJGXBigYoAPDxlK3CigwUGLIAOEyIiQI8cCBUOqJFnQpEkGA1XKZPlPgkuXBATK3JmRws2bB3TuXNmQw8+jQoeCbHj0qIGkSgNobNoUqlKIVJs++BfV4oiEWalaHVpyosCwJidw7Sr1YMQFBDn+y4qSbUW3AiDElXiWqoK1bPEKGLixr1jAXQ9GuGn4sN22Bl02roo4Kla+c8OOJbsQM9rNPJlORlr5asbPpTk/RP2YJGu7rjWnDm2RIQLZrSt3zgp6ZmqwmkHAng3ccWDEMe8Kpnw8JEHlkXnPdh6SxHPILaU/dp60LFUP07dfRq5aYntohAO0m+c+nvT6pVMPZ3jv8AJu8xktyNbw+ATJDtKFBx9NlA20gWU0DVQBYwZhsJMICRrkwEYJJGRCSBtEqGGCAQEAOw=='

red_x = b"R0lGODlhEAAQAPeQAIsAAI0AAI4AAI8AAJIAAJUAAJQCApkAAJoAAJ4AAJkJCaAAAKYAAKcAAKcCAKcDA6cGAKgAAKsAAKsCAKwAAK0AAK8AAK4CAK8DAqUJAKULAKwLALAAALEAALIAALMAALMDALQAALUAALYAALcEALoAALsAALsCALwAAL8AALkJAL4NAL8NAKoTAKwbAbEQALMVAL0QAL0RAKsREaodHbkQELMsALg2ALk3ALs+ALE2FbgpKbA1Nbc1Nb44N8AAAMIWAMsvAMUgDMcxAKVABb9NBbVJErFYEq1iMrtoMr5kP8BKAMFLAMxKANBBANFCANJFANFEB9JKAMFcANFZANZcANpfAMJUEMZVEc5hAM5pAMluBdRsANR8AM9YOrdERMpIQs1UVMR5WNt8X8VgYMdlZcxtYtx4YNF/btp9eraNf9qXXNCCZsyLeNSLd8SSecySf82kd9qqc9uBgdyBgd+EhN6JgtSIiNuJieGHhOGLg+GKhOKamty1ste4sNO+ueenp+inp+HHrebGrefKuOPTzejWzera1O7b1vLb2/bl4vTu7fbw7ffx7vnz8f///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAJAALAAAAAAQABAAAAjUACEJHEiwYEEABniQKfNFgQCDkATQwAMokEU+PQgUFDAjjR09e/LUmUNnh8aBCcCgUeRmzBkzie6EeQBAoAAMXuA8ciRGCaJHfXzUMCAQgYooWN48anTokR8dQk4sELggBhQrU9Q8evSHiJQgLCIIfMDCSZUjhbYuQkLFCRAMAiOQGGLE0CNBcZYmaRIDLqQFGF60eTRoSxc5jwjhACFWIAgMLtgUocJFy5orL0IQRHAiQgsbRZYswbEhBIiCCH6EiJAhAwQMKU5DjHCi9gnZEHMTDAgAOw=="

COLOR_SCHEME = 'LightGreen'

WIDTH_VARIABLES = 23
WIDTH_RESULTS = 46

WIDTH_WATCHER_VARIABLES = 20
WIDTH_WATCHER_RESULTS = 60

WIDTH_LOCALS = 80
NUM_AUTO_WATCH = 9

MAX_LINES_PER_RESULT_FLOATING = 4
MAX_LINES_PER_RESULT_MAIN = 3

POPOUT_WINDOW_FONT = 'Sans 8'


class _Debugger():
    debugger = None

    #     #                    ######
    ##   ##   ##   # #    #    #     # ###### #####  #    #  ####   ####  ###### #####
    # # # #  #  #  # ##   #    #     # #      #    # #    # #    # #    # #      #    #
    #  #  # #    # # # #  #    #     # #####  #####  #    # #      #      #####  #    #
    #     # ###### # #  # #    #     # #      #    # #    # #  ### #  ### #      #####
    #     # #    # # #   ##    #     # #      #    # #    # #    # #    # #      #   #
    #     # #    # # #    #    ######  ###### #####   ####   ####   ####  ###### #    #

    def __init__(self):
        self.watcher_window = None  # type: Window
        self.popout_window = None  # type: Window
        self.local_choices = {}
        self.myrc = ''
        self.custom_watch = ''
        self.locals = {}
        self.globals = {}
        self.popout_choices = {}

    # Includes the DUAL PANE (now 2 tabs)!  Don't forget REPL is there too!
    def _build_main_debugger_window(self, location=(None, None)):
        ChangeLookAndFeel(COLOR_SCHEME)

        def InVar(key1):
            row1 = [T('    '),
                    I(key=key1, size=(WIDTH_VARIABLES, 1)),
                    T('', key=key1 + 'CHANGED_', size=(WIDTH_RESULTS, 1)), B('Detail', key=key1 + 'DETAIL_'),
                    B('Obj', key=key1 + 'OBJ_'), ]
            return row1

        variables_frame = [InVar('_VAR0_'),
                           InVar('_VAR1_'),
                           InVar('_VAR2_'), ]

        interactive_frame = [[T('>>> '), In(size=(83, 1), key='_REPL_',
                                            tooltip='Type in any "expression" or "statement"\n and it will be disaplayed below.\nPress RETURN KEY instead of "Go"\nbutton for faster use'),
                              B('Go', bind_return_key=True, visible=True)],
                             [Multiline(size=(93, 26), key='_OUTPUT_', autoscroll=True, do_not_clear=True)], ]

        autowatch_frame = [[Button('Choose Variables To Auto Watch', key='_LOCALS_'),
                            Button('Clear All Auto Watches'),
                            Button('Show All Variables', key='_SHOW_ALL_'),
                            Button('Locals', key='_ALL_LOCALS_'),
                            Button('Globals', key='_GLOBALS_'),
                            Button('Popout', key='_POPOUT_')]]

        var_layout = []
        for i in range(NUM_AUTO_WATCH):
            var_layout.append([T('', size=(WIDTH_WATCHER_VARIABLES, 1), key='_WATCH%s_' % i),
                               T('', size=(WIDTH_WATCHER_RESULTS, MAX_LINES_PER_RESULT_MAIN), key='_WATCH%s_RESULT_' % i,
                                 )])

        col1 = [
            # [Frame('Auto Watches', autowatch_frame+variable_values, title_color='blue')]
            [Frame('Auto Watches', autowatch_frame + var_layout, title_color='blue')]
        ]

        col2 = [
            [Frame('Variables or Expressions to Watch', variables_frame, title_color='blue'), ],
            [Frame('REPL-Light - Press Enter To Execute Commands', interactive_frame, title_color='blue'), ]
        ]

        # Tab based layout
        layout = [[TabGroup([[Tab('Variables', col1), Tab('REPL & Watches', col2)]])],
                  [Button('', image_data=red_x, key='_EXIT_', button_color=None), ]]

        # ------------------------------- Create main window -------------------------------
        window = Window("PySimpleGUI Debugger", layout, icon=PSGDebugLogo, margins=(0, 0), location=location)

        Window._read_call_from_debugger = True
        window.finalize()
        Window._read_call_from_debugger = False

        window.Element('_VAR1_').SetFocus()
        self.watcher_window = window
        ChangeLookAndFeel('SystemDefault')  # set look and feel to default before exiting
        return window

    #     #                    #######                               #
    ##   ##   ##   # #    #    #       #    # ###### #    # #####    #        ####   ####  #####
    # # # #  #  #  # ##   #    #       #    # #      ##   #   #      #       #    # #    # #    #
    #  #  # #    # # # #  #    #####   #    # #####  # #  #   #      #       #    # #    # #    #
    #     # ###### # #  # #    #       #    # #      #  # #   #      #       #    # #    # #####
    #     # #    # # #   ##    #        #  #  #      #   ##   #      #       #    # #    # #
    #     # #    # # #    #    #######   ##   ###### #    #   #      #######  ####   ####  #

    def _refresh_main_debugger_window(self, mylocals, myglobals):
        if not self.watcher_window:  # if there is no window setup, nothing to do
            return False
        event, values = self.watcher_window.Read(timeout=1)
        if event in (None, 'Exit', '_EXIT_'):  # EXIT BUTTON / X BUTTON
            try:
                self.watcher_window.Close()
            except:
                pass
            self.watcher_window = None
            return False
        # ------------------------------- Process events from REPL Tab -------------------------------
        cmd = values['_REPL_']  # get the REPL entered
        # BUTTON - GO (NOTE - This button is invisible!!)
        if event == 'Go':  # GO BUTTON
            self.watcher_window.Element('_REPL_').Update('')
            self.watcher_window.Element('_OUTPUT_').Update(">>> {}\n".format(cmd), append=True, autoscroll=True)

            try:
                result = eval('{}'.format(cmd), myglobals, mylocals)
            except Exception as e:
                if sys.version_info[0] < 3:
                    result = 'Not available in Python 2'
                else:
                    try:
                        result = exec('{}'.format(cmd), myglobals, mylocals)
                    except Exception as e:
                        result = 'Exception {}\n'.format(e)

            self.watcher_window.Element('_OUTPUT_').Update('{}\n'.format(result), append=True, autoscroll=True)
        # BUTTON - DETAIL
        elif event.endswith('_DETAIL_'):  # DETAIL BUTTON
            var = values['_VAR{}_'.format(event[4])]
            try:
                result = str(eval(str(var), myglobals, mylocals))
            except:
                result = ''
            PopupScrolled(str(values['_VAR{}_'.format(event[4])]) + '\n' + result, title=var, non_blocking=True)
        # BUTTON - OBJ
        elif event.endswith('_OBJ_'):  # OBJECT BUTTON
            var = values['_VAR{}_'.format(event[4])]
            try:
                result = ObjToStringSingleObj(mylocals[var])
            except Exception as e:
                try:
                    result = eval('{}'.format(var), myglobals, mylocals)
                    result = ObjToStringSingleObj(result)
                except Exception as e:
                    result = '{}\nError showing object {}'.format(e, var)
            PopupScrolled(str(var) + '\n' + str(result), title=var, non_blocking=True)
        # ------------------------------- Process Watch Tab -------------------------------
        # BUTTON - Choose Locals to see
        elif event == '_LOCALS_':  # Show all locals BUTTON
            self._choose_auto_watches(mylocals)
        # BUTTON - Locals (quick popup)
        elif event == '_ALL_LOCALS_':
            self._display_all_vars(mylocals)
        # BUTTON - Globals (quick popup)
        elif event == '_GLOBALS_':
            self._display_all_vars(myglobals)
        # BUTTON - clear all
        elif event == 'Clear All Auto Watches':
            if PopupYesNo('Do you really want to clear all Auto-Watches?', 'Really Clear??') == 'Yes':
                self.local_choices = {}
                self.custom_watch = ''
        # BUTTON - Popout
        elif event == '_POPOUT_':
            if not self.popout_window:
                self._build_floating_window()
        # BUTTON - Show All
        elif event == '_SHOW_ALL_':
            for key in self.locals:
                self.local_choices[key] = not key.startswith('_')

        # -------------------- Process the manual "watch list" ------------------
        for i in range(3):
            key = '_VAR{}_'.format(i)
            out_key = '_VAR{}_CHANGED_'.format(i)
            self.myrc = ''
            if self.watcher_window.Element(key):
                var = values[key]
                try:
                    result = eval(str(var), myglobals, mylocals)
                except:
                    result = ''
                self.watcher_window.Element(out_key).Update(str(result))
            else:
                self.watcher_window.Element(out_key).Update('')

        # -------------------- Process the automatic "watch list" ------------------
        slot = 0
        for key in self.local_choices:
            if key == '_CUSTOM_WATCH_':
                continue
            if self.local_choices[key]:
                self.watcher_window.Element('_WATCH{}_'.format(slot)).Update(key)
                try:
                    self.watcher_window.Element('_WATCH{}_RESULT_'.format(slot), silent_on_error=True).Update(mylocals[key])
                except:
                    self.watcher_window.Element('_WATCH{}_RESULT_'.format(slot)).Update('')
                slot += 1

            if slot + int(not self.custom_watch in (None, '')) >= NUM_AUTO_WATCH:
                break
        # If a custom watch was set, display that value in the window
        if self.custom_watch:
            self.watcher_window.Element('_WATCH{}_'.format(slot)).Update(self.custom_watch)
            try:
                self.myrc = eval(self.custom_watch, myglobals, mylocals)
            except:
                self.myrc = ''
            self.watcher_window.Element('_WATCH{}_RESULT_'.format(slot)).Update(self.myrc)
            slot += 1
        # blank out all of the slots not used (blank)
        for i in range(slot, NUM_AUTO_WATCH):
            self.watcher_window.Element('_WATCH{}_'.format(i)).Update('')
            self.watcher_window.Element('_WATCH{}_RESULT_'.format(i)).Update('')

        return True  # return indicating the window stayed open

    ######                                 #     #
    #     #  ####  #####  #    # #####     #  #  # # #    # #####   ####  #    #
    #     # #    # #    # #    # #    #    #  #  # # ##   # #    # #    # #    #
    ######  #    # #    # #    # #    #    #  #  # # # #  # #    # #    # #    #
    #       #    # #####  #    # #####     #  #  # # #  # # #    # #    # # ## #
    #       #    # #      #    # #         #  #  # # #   ## #    # #    # ##  ##
    #        ####  #       ####  #          ## ##  # #    # #####   ####  #    #

    ######                                    #                     #     #
    #     # #    # #    # #####   ####       # #   #      #         #     #   ##   #####   ####
    #     # #    # ##  ## #    # #          #   #  #      #         #     #  #  #  #    # #
    #     # #    # # ## # #    #  ####     #     # #      #         #     # #    # #    #  ####
    #     # #    # #    # #####       #    ####### #      #          #   #  ###### #####       #
    #     # #    # #    # #      #    #    #     # #      #           # #   #    # #   #  #    #
    ######   ####  #    # #       ####     #     # ###### ######       #    #    # #    #  ####
    # displays them into a single text box

    def _display_all_vars(self, dict):
        num_cols = 3
        output_text = ''
        num_lines = 2
        cur_col = 0
        out_text = 'All of your Vars'
        longest_line = max([len(key) for key in dict])
        line = []
        sorted_dict = {}
        for key in sorted(dict.keys()):
            sorted_dict[key] = dict[key]
        for key in sorted_dict:
            value = dict[key]
            wrapped_list = textwrap.wrap(str(value), 60)
            wrapped_text = '\n'.join(wrapped_list)
            out_text += '{} - {}\n'.format(key, wrapped_text)
            if cur_col + 1 == num_cols:
                cur_col = 0
                num_lines += len(wrapped_list)
            else:
                cur_col += 1
        ScrolledTextBox(out_text, non_blocking=True)

     #####                                        #     #
    #     # #    #  ####   ####   ####  ######    #  #  #   ##   #####  ####  #    #
    #       #    # #    # #    # #      #         #  #  #  #  #    #   #    # #    #
    #       ###### #    # #    #  ####  #####     #  #  # #    #   #   #      ######
    #       #    # #    # #    #      # #         #  #  # ######   #   #      #    #
    #     # #    # #    # #    # #    # #         #  #  # #    #   #   #    # #    #
     #####  #    #  ####   ####   ####  ######     ## ##  #    #   #    ####  #    #

    #     #                                                       #     #
    #     #   ##   #####  #   ##   #####  #      ######  ####     #  #  # # #    #
    #     #  #  #  #    # #  #  #  #    # #      #      #         #  #  # # ##   #
    #     # #    # #    # # #    # #####  #      #####   ####     #  #  # # # #  #
     #   #  ###### #####  # ###### #    # #      #           #    #  #  # # #  # #
      # #   #    # #   #  # #    # #    # #      #      #    #    #  #  # # #   ##
       #    #    # #    # # #    # #####  ###### ######  ####      ## ##  # #    #

    def _choose_auto_watches(self, my_locals):
        ChangeLookAndFeel(COLOR_SCHEME)
        num_cols = 3
        output_text = ''
        num_lines = 2
        cur_col = 0
        layout = [[Text('Choose your "Auto Watch" variables', font='ANY 14', text_color='red')]]
        longest_line = max([len(key) for key in my_locals])
        line = []
        sorted_dict = {}
        for key in sorted(my_locals.keys()):
            sorted_dict[key] = my_locals[key]
        for key in sorted_dict:
            line.append(CB(key, key=key, size=(longest_line, 1),
                           default=self.local_choices[key] if key in self.local_choices else False))
            if cur_col + 1 == num_cols:
                cur_col = 0
                layout.append(line)
                line = []
            else:
                cur_col += 1
        if cur_col:
            layout.append(line)

        layout += [
            [Text('Custom Watch (any expression)'), Input(default_text=self.custom_watch, size=(40, 1), key='_CUSTOM_WATCH_')]]
        layout += [
            [Ok(), Cancel(), Button('Clear All'), Button('Select [almost] All', key='_AUTO_SELECT_')]]

        window = Window('All Locals', layout, icon=PSGDebugLogo).Finalize()

        while True:  # event loop
            event, values = window.Read()
            if event in (None, 'Cancel'):
                break
            elif event == 'Ok':
                self.local_choices = values
                self.custom_watch = values['_CUSTOM_WATCH_']
                break
            elif event == 'Clear All':
                PopupQuickMessage('Cleared Auto Watches', auto_close=True, auto_close_duration=3, non_blocking=True,
                                  text_color='red', font='ANY 18')
                for key in sorted_dict:
                    window.Element(key).Update(False)
                window.Element('_CUSTOM_WATCH_').Update('')
            elif event == 'Select All':
                for key in sorted_dict:
                    window.Element(key).Update(False)
            elif event == '_AUTO_SELECT_':
                for key in sorted_dict:
                    window.Element(key).Update(not key.startswith('_'))

        # exited event loop
        window.Close()
        ChangeLookAndFeel('SystemDefault')

    ######                            #######
    #     # #    # # #      #####     #       #       ####    ##   ##### # #    #  ####
    #     # #    # # #      #    #    #       #      #    #  #  #    #   # ##   # #    #
    ######  #    # # #      #    #    #####   #      #    # #    #   #   # # #  # #
    #     # #    # # #      #    #    #       #      #    # ######   #   # #  # # #  ###
    #     # #    # # #      #    #    #       #      #    # #    #   #   # #   ## #    #
    ######   ####  # ###### #####     #       ######  ####  #    #   #   # #    #  ####

    #     #
    #  #  # # #    # #####   ####  #    #
    #  #  # # ##   # #    # #    # #    #
    #  #  # # # #  # #    # #    # #    #
    #  #  # # #  # # #    # #    # # ## #
    #  #  # # #   ## #    # #    # ##  ##
     ## ##  # #    # #####   ####  #    #

    def _build_floating_window(self, location=(None, None)):
        """

        :param location:

        """
        if self.popout_window:  # if floating window already exists, close it first
            self.popout_window.Close()
        ChangeLookAndFeel('Topanga')
        num_cols = 2
        width_var = 15
        width_value = 30
        layout = []
        line = []
        col = 0
        # self.popout_choices = self.local_choices
        self.popout_choices = {}
        if self.popout_choices == {}:  # if nothing chosen, then choose all non-_ variables
            for key in sorted(self.locals.keys()):
                self.popout_choices[key] = not key.startswith('_')

        width_var = max([len(key) for key in self.popout_choices])
        for key in self.popout_choices:
            if self.popout_choices[key] is True:
                value = str(self.locals.get(key))
                h = min(len(value) // width_value + 1, MAX_LINES_PER_RESULT_FLOATING)
                line += [Text('{}'.format(key), size=(width_var, 1), font=POPOUT_WINDOW_FONT),
                         Text(' = ', font=POPOUT_WINDOW_FONT),
                         Text(value, key=key, size=(width_value, h), font=POPOUT_WINDOW_FONT)]
                if col + 1 < num_cols:
                    line += [VerticalSeparator(), T(' ')]
                col += 1
            if col >= num_cols:
                layout.append(line)
                line = []
                col = 0
        if col != 0:
            layout.append(line)
        layout = [[Column(layout), Column(
            [[Button('', key='_EXIT_', image_data=red_x, button_color=('#282923', '#282923'), border_width=0)]])]]

        self.popout_window = Window('Floating', layout, alpha_channel=0, no_titlebar=True, grab_anywhere=True,
                                    element_padding=(0, 0), margins=(0, 0), keep_on_top=True,
                                    right_click_menu=['&Right', ['Debugger::RightClick', 'Exit::RightClick']], location=location, finalize=False)

        Window._read_call_from_debugger = True
        self.popout_window.Finalize()
        Window._read_call_from_debugger = False

        if location == (None, None):
            screen_size = self.popout_window.GetScreenDimensions()
            self.popout_window.Move(screen_size[0] - self.popout_window.Size[0], 0)
        self.popout_window.SetAlpha(1)

        ChangeLookAndFeel('SystemDefault')
        return True

    ######
    #     # ###### ###### #####  ######  ####  #    #
    #     # #      #      #    # #      #      #    #
    ######  #####  #####  #    # #####   ####  ######
    #   #   #      #      #####  #           # #    #
    #    #  #      #      #   #  #      #    # #    #
    #     # ###### #      #    # ######  ####  #    #

    #######
    #       #       ####    ##   ##### # #    #  ####
    #       #      #    #  #  #    #   # ##   # #    #
    #####   #      #    # #    #   #   # # #  # #
    #       #      #    # ######   #   # #  # # #  ###
    #       #      #    # #    #   #   # #   ## #    #
    #       ######  ####  #    #   #   # #    #  ####

    #     #
    #  #  # # #    # #####   ####  #    #
    #  #  # # ##   # #    # #    # #    #
    #  #  # # # #  # #    # #    # #    #
    #  #  # # #  # # #    # #    # # ## #
    #  #  # # #   ## #    # #    # ##  ##
     ## ##  # #    # #####   ####  #    #

    def _refresh_floating_window(self):
        if not self.popout_window:
            return
        for key in self.popout_choices:
            if self.popout_choices[key] is True and key in self.locals:
                if key is not None and self.popout_window is not None:
                    self.popout_window.Element(key, silent_on_error=True).Update(self.locals.get(key))
        event, values = self.popout_window.Read(timeout=1)
        if event in (None, '_EXIT_', 'Exit::RightClick'):
            self.popout_window.Close()
            self.popout_window = None
        elif event == 'Debugger::RightClick':
            show_debugger_window()


# 888     888                                .d8888b.         d8888 888 888          888      888
# 888     888                               d88P  Y88b       d88888 888 888          888      888
# 888     888                               888    888      d88P888 888 888          888      888
# 888     888 .d8888b   .d88b.  888d888     888            d88P 888 888 888  8888b.  88888b.  888  .d88b.
# 888     888 88K      d8P  Y8b 888P"       888           d88P  888 888 888     "88b 888 "88b 888 d8P  Y8b
# 888     888 "Y8888b. 88888888 888         888    888   d88P   888 888 888 .d888888 888  888 888 88888888
# Y88b. .d88P      X88 Y8b.     888         Y88b  d88P  d8888888888 888 888 888  888 888 d88P 888 Y8b.
#  "Y88888P"   88888P'  "Y8888  888          "Y8888P"  d88P     888 888 888 "Y888888 88888P"  888  "Y8888

# 8888888888                            888    d8b
# 888                                   888    Y8P
# 888                                   888
# 8888888    888  888 88888b.   .d8888b 888888 888  .d88b.  88888b.  .d8888b
# 888        888  888 888 "88b d88P"    888    888 d88""88b 888 "88b 88K
# 888        888  888 888  888 888      888    888 888  888 888  888 "Y8888b.
# 888        Y88b 888 888  888 Y88b.    Y88b.  888 Y88..88P 888  888      X88
# 888         "Y88888 888  888  "Y8888P  "Y888 888  "Y88P"  888  888  88888P'


def show_debugger_window(location=(None, None), *args):
    """
    Shows the large main debugger window
    :param location:  Locations (x,y) on the screen to place upper left corner of the window
    :ttype location: Tuple[int, int]
    """
    if _Debugger.debugger is None:
        _Debugger.debugger = _Debugger()
    debugger = _Debugger.debugger
    frame = inspect.currentframe()
    prev_frame = inspect.currentframe().f_back
    # frame, *others = inspect.stack()[1]
    try:
        debugger.locals = frame.f_back.f_locals
        debugger.globals = frame.f_back.f_globals
    finally:
        del frame

    if not debugger.watcher_window:
        debugger.watcher_window = debugger._build_main_debugger_window(location=location)
    return True


def show_debugger_popout_window(location=(None, None), *args):
    """
    Shows the smaller "popout" window.  Default location is the upper right corner of your screen

    :param location:  Locations (x,y) on the screen to place upper left corner of the window
    :type location: Tuple[int, int]
    """
    if _Debugger.debugger is None:
        _Debugger.debugger = _Debugger()
    debugger = _Debugger.debugger
    frame = inspect.currentframe()
    prev_frame = inspect.currentframe().f_back
    # frame = inspect.getframeinfo(prev_frame)
    # frame, *others = inspect.stack()[1]
    try:
        debugger.locals = frame.f_back.f_locals
        debugger.globals = frame.f_back.f_globals
    finally:
        del frame
    if debugger.popout_window:
        debugger.popout_window.Close()
        debugger.popout_window = None
    debugger._build_floating_window(location=location)


def _refresh_debugger():
    """
    Refreshes the debugger windows. USERS should NOT be calling this function. Within PySimpleGUI it is called for the USER every time the Window.Read function is called.

    :return: rc (bool) False if user closed the main debugger window.
    """
    if _Debugger.debugger is None:
        _Debugger.debugger = _Debugger()
    debugger = _Debugger.debugger
    Window._read_call_from_debugger = True
    # frame = inspect.currentframe()
    # frame = inspect.currentframe().f_back
    frame, *others = inspect.stack()[1]
    try:
        debugger.locals = frame.f_back.f_locals
        debugger.globals = frame.f_back.f_globals
    finally:
        del frame
    debugger._refresh_floating_window() if debugger.popout_window else None
    rc = debugger._refresh_main_debugger_window(debugger.locals, debugger.globals) if debugger.watcher_window else False
    Window._read_call_from_debugger = False
    return rc


#                        d8b
#                        Y8P
#
# 88888b.d88b.   8888b.  888 88888b.
# 888 "888 "88b     "88b 888 888 "88b
# 888  888  888 .d888888 888 888  888
# 888  888  888 888  888 888 888  888
# 888  888  888 "Y888888 888 888  888

import sys
import site
import shutil
import hashlib
import base64
from pathlib import Path
import configparser
import urllib.request
import urllib.error


def _install(files, url=None):
    """
    install one file package from GitHub

    Parameters
    ----------
    files : list
        files to be installed
        the first item (files[0]) will be used as the name of the package
        optional files should be preceded wit an exclamation mark (!)

    url : str
        url of the location of the GitHub repository
        this will start usually with https://raw.githubusercontent.com/ and end with /master/
        if omitted, the files will be copied from the current directory (no GitHub)

    Returns
    -------
    info : Info instance
        with structure contains
        info.package : name of the package installed
        info.path : name where the package is installed in the site-packages
        info.version : version of the package (obtained from <package>.py)
        info.files_copied : list of copied files

    Notes
    -----
    The program automatically makes the required __init__.py file (unless given in files) and
    <package><version>.dist-info folder with the usual files METADATA, INSTALLER and RECORDS.
    As the setup.py is not run, the METADATA is very limited, i.e. is contains just name and version.

    If an __init__.py is in files that file will be used.
    Otherwise, an __init__/py file will be generated. In thet case, if a __version__ = statement
    is found in the source file, the __version__ will be included in that __init__.py file.

    Version history
    ---------------
    version 1.0.1  2020-03-04
        now uses urllib instead of requests to avoid non standard libraries
        installation for Pythonista improved

    version 1.0.0  2020-03-04
        initial version

    (c)2020 Ruud van der Ham - www.salabim.org
    """

    class Info:
        version = "?"
        package = "?"
        path = "?"
        files_copied = []

    info = Info()
    Pythonista = sys.platform == "ios"
    if not files:
        raise ValueError('no files specified')
    if files[0][0] == '!':
        raise ValueError('first item in files (sourcefile) may not be optional')
    package = Path(files[0]).stem
    sourcefile = files[0]

    file_contents = {}
    for file in files:
        optional = file[0] == "!"
        if optional:
            file = file[1:]

        if url:
            try:
                with urllib.request.urlopen(url + file) as response:
                    page = response.read()
                #                page = requests.get(url + file)
                file_contents[file] = page
                exists = True
            except urllib.error.URLError:
                exists = False

        else:
            exists = Path(file).is_file()
            if exists:
                with open(file, "rb") as f:
                    file_contents[file] = f.read()

        if (not exists) and (not optional):
            raise FileNotFoundError(file + " not found. Nothing installed.")

    version = "unknown"
    for line in file_contents[sourcefile].decode("utf-8").split("\n"):
        line_split = line.split("__version__ =")
        if len(line_split) > 1:
            raw_version = line_split[-1].strip(" '\"")
            version = ""
            for c in raw_version:
                if c in "0123456789-.":
                    version += c
                else:
                    break
            break

    info.files_copied = list(file_contents.keys())
    info.package = package
    info.version = version
    paths = []

    file = '__init__.py'
    if file not in file_contents:
        file_contents[file] = ("from ." + package + " import *\n").encode()
        if version != 'unknown':
            file_contents[file] += ("from ." + package + " import __version__\n").encode()

    if Pythonista:
        cwd = Path.cwd()
        parts1 = []
        for part in cwd.parts:
            parts1.append(part)
            if part == "Documents":
                break
        else:
            raise EnvironmentError("unable to install")

        sitepackages_paths = [Path(*parts1) / ("site-packages" + ver) for ver in ("", "-2", "-3")]
    else:
        sitepackages_paths = [Path(site.getsitepackages()[-1])]

    for sitepackages_path in sitepackages_paths:

        path = sitepackages_path / package
        paths.append(str(path))

        if not path.is_dir():
            path.mkdir()

        for file, contents in file_contents.items():
            with open(path / file, "wb") as f:
                f.write(contents)

        if Pythonista:
            pypi_packages = sitepackages_path / '.pypi_packages'
            config = configparser.ConfigParser()
            config.read(pypi_packages)
            config[package] = {}
            config[package]['url'] = 'github'
            config[package]['version'] = version
            config[package]['summary'] = ''
            config[package]['files'] = path.as_posix()
            config[package]['dependency'] = ''
            with pypi_packages.open('w') as f:
                config.write(f)
        else:
            for entry in sitepackages_path.glob("*"):
                if entry.is_dir():
                    if entry.stem.startswith(package) and entry.suffix == ".dist-info":
                        shutil.rmtree(entry)
            path_distinfo = Path(str(path) + "-" + version + ".dist-info")
            if not path_distinfo.is_dir():
                path_distinfo.mkdir()
            with open(path_distinfo / "METADATA", "w") as f:  # make a dummy METADATA file
                f.write("Name: " + package + "\n")
                f.write("Version: " + version + "\n")

            with open(path_distinfo / "INSTALLER", "w") as f:  # make a dummy METADATA file
                f.write("github\n")
            with open(path_distinfo / "RECORD", "w") as f:
                pass  # just to create the file to be recorded

            with open(path_distinfo / "RECORD", "w") as record_file:

                for p in (path, path_distinfo):
                    for file in p.glob("**/*"):

                        if file.is_file():
                            name = file.relative_to(sitepackages_path).as_posix()  # make sure we have slashes
                            record_file.write(name + ",")

                            if (file.stem == "RECORD" and p == path_distinfo) or ("__pycache__" in name.lower()):
                                record_file.write(",")
                            else:
                                with open(file, "rb") as f:
                                    file_contents = f.read()
                                    hash = "sha256=" + base64.urlsafe_b64encode(
                                        hashlib.sha256(file_contents).digest()
                                    ).decode("latin1").rstrip("=")
                                    # hash calculation derived from wheel.py in pip

                                    length = str(len(file_contents))
                                    record_file.write(hash + "," + length)

                            record_file.write("\n")

    info.path = ','.join(paths)
    return info

def _upgrade_from_github():
    info = _install(
        files="PySimpleGUI.py !init.py".split(), url="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/"
    )
    """
    info = install(
        files="salabim.py !calibri.ttf !mplus-1m-regular.ttf !license.txt !DejaVuSansMono.ttf !changelog.txt".split(),
        url="https://raw.githubusercontent.com/salabim/salabim/master/",
    )
    """

    # print(info.package + " " + info.version + " successfully installed in " + info.path)
    # print("files copied: ", info.files_copied)

    popup("*** SUCCESS ***", info.package, info.version, "successfully installed in ", info.path, "files copied: ", info.files_copied,
          keep_on_top=True, background_color='red', text_color='white')


def _upgrade_gui():
    try:
        cur_ver = version[:version.index('\n')]
    except:
        cur_ver = version

    if popup_yes_no('* WARNING *',
                    'You are about to upgrade your PySimpleGUI package previously installed via pip to the latest version location on the GitHub server.',
                    'You are running verrsion {}'.format(cur_ver),
                    'Are you sure you want to overwrite this release?', title='Are you sure you want to overwrite?',
                    keep_on_top=True) == 'Yes':
        _upgrade_from_github()
    else:
        popup_quick_message('Cancelled upgrade\nNothing overwritten', background_color='red', text_color='white', keep_on_top=True, non_blocking=False)


def main():
    """
    The PySimpleGUI "Test Harness".  This is meant to be a super-quick test of the Elements.
    """
    from random import randint

    # theme('dark blue 3')
    # theme('dark brown 2')
    # theme('dark red')
    # theme('Light Green 6')
    try:
        ver = version[:version.index('\n')]
    except:
        ver = version

    print('Starting up PySimpleGUI Test Harness\n', 'PySimpleGUI Version ', ver, '\ntcl ver = {}'.format(tkinter.TclVersion),
          'tkinter version = {}'.format(tkinter.TkVersion), '\nPython Version {}'.format(sys.version))

    # ------ Menu Definition ------ #
    menu_def = [['&File', ['!&Open', '&Save::savekey', '---', '&Properties', 'E&xit']],
                ['!&Edit', ['!&Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['&Debugger', ['Popout', 'Launch Debugger']],
                ['&Toolbar', ['Command &1', 'Command &2', 'Command &3', 'Command &4']],
                ['&Help', '&About...'], ]

    treedata = TreeData()

    treedata.Insert("", '_A_', 'Tree Item 1', [1, 2, 3], )
    treedata.Insert("", '_B_', 'B', [4, 5, 6], )
    treedata.Insert("_A_", '_A1_', 'Sub Item 1', ['can', 'be', 'anything'], )
    treedata.Insert("", '_C_', 'C', [], )
    treedata.Insert("_C_", '_C1_', 'C1', ['or'], )
    treedata.Insert("_A_", '_A2_', 'Sub Item 2', [None, None])
    treedata.Insert("_A1_", '_A3_', 'A30', ['getting deep'])
    treedata.Insert("_C_", '_C2_', 'C2', ['nothing', 'at', 'all'])

    for i in range(100):
        treedata.Insert('_C_', i, i, [])

    frame1 = [
        [Input('Input Text', size=(25, 1)), ],
        [Multiline(size=(30, 5), default_text='Multiline Input')],
    ]

    frame2 = [
        # [ProgressBar(100, bar_color=('red', 'green'), orientation='h')],

        [Listbox(['Listbox 1', 'Listbox 2', 'Listbox 3'], select_mode=SELECT_MODE_EXTENDED, size=(20, 5), no_scrollbar=True)],
        [Combo(['Combo item %s' % i for i in range(5)], size=(20, 3), default_value='Combo item 2', key='_COMBO1_', )],
        # [Combo(['Combo item 1', 2,3,4], size=(20, 3), readonly=False, text_color='blue', background_color='red', key='_COMBO2_')],
        [Spin([1, 2, 3, 'a', 'b', 'c'], initial_value='a', size=(4, 3))],
    ]

    frame3 = [
        [Checkbox('Checkbox1', True), Checkbox('Checkbox1')],
        [Radio('Radio Button1', 1), Radio('Radio Button2', 1, default=True, tooltip='Radio 2')],
        [T('', size=(1, 4))],
    ]

    frame4 = [
        [Slider(range=(0, 100), orientation='v', size=(7, 15), default_value=40, key='-SLIDER1-'),
         Slider(range=(0, 100), orientation='h', size=(11, 15), default_value=40, key='-SLIDER2-'), ],
    ]
    matrix = [[str(x * y) for x in range(1, 5)] for y in range(1, 8)]

    frame5 = [[
        Table(values=matrix, headings=matrix[0],
              auto_size_columns=False, display_row_numbers=True, change_submits=False, justification='right',
              num_rows=10, alternating_row_color='lightblue', key='_table_',
              col_widths=[5, 5, 5, 5], size=(400, 200), ),
        T('  '),
        Tree(data=treedata, headings=['col1', 'col2', 'col3'], change_submits=True, auto_size_columns=True,
             num_rows=10, col0_width=10, key='_TREE_', show_expanded=True,),
    ],
    ]

    graph_elem = Graph((600, 150), (0, 0), (800, 300), key='+GRAPH+')

    frame6 = [
        [graph_elem],
    ]

    tab1 = Tab('Graph', frame6, tooltip='Graph is in here', title_color='red')
    tab2 = Tab('Multiple/Binary Choice Groups', [[Frame('Multiple Choice Group', frame2, title_color='green', tooltip='Checkboxes, radio buttons, etc'),
                                                  Frame('Binary Choice Group', frame3, title_color='#FFFFFF', tooltip='Binary Choice'), ]])
    tab3 = Tab('Table and Tree', [[Frame('Structured Data Group', frame5, title_color='red', element_justification='l')]], tooltip='tab 3', title_color='red')
    tab4 = Tab('Variable Choice', [[Frame('Variable Choice Group', frame4, title_color='blue')]], tooltip='tab 4', title_color='red')

    layout1 = [
        [Image(data=DEFAULT_BASE64_ICON, enable_events=True, key='-LOGO-'), Image(data=DEFAULT_BASE64_LOADING_GIF, enable_events=True, key='_IMAGE_'),
         Text('You are running the PySimpleGUI.py file instead of importing it.\nAnd are thus seeing a test harness instead of your code', font='ANY 15',
              tooltip='My tooltip', key='_TEXT1_')],
        [Frame('Input Text Group', frame1, title_color='red')],
         [Text('PySimpleGUI Version {}'.format(ver), size=(50, None), font='ANY 12')],
         [Text('PySimpleGUI Location {}'.format(os.path.dirname(os.path.abspath(__file__))), size=(50, None), font='ANY 12')],
         [Text('Python Version {}'.format(sys.version), size=(50, None), font='ANY 12')],
         [Text('TK / TCL Versions {} / {}'.format(tk.TkVersion, tk.TclVersion), size=(50, None), font='ANY 12')],
        [TabGroup([[tab1, tab2, tab3, tab4]], key='_TAB_GROUP_', )],
        [Button('Button'), B('Hide Stuff', metadata='my metadata'),
         Button('ttk Button', use_ttk_buttons=True, tooltip='This is a TTK Button'),
         Button('See-through Mode', tooltip='Make the background transparent'),
         Button('Install PySimpleGUI from GitHub', button_color=('white', 'red') ,key='-INSTALL-'),
         Button('Exit', tooltip='Exit button')],
    ]

    layout = [[Column([[Menu(menu_def, key='_MENU_', font='Courier 15')]] + layout1), Column([[ProgressBar(max_value=800, size=(45, 25), orientation='v', key='+PROGRESS+')]])]]
    window = Window('Window Title', layout,
                    # font=('Helvetica', 18),
                    # background_color='black',
                    right_click_menu=['&Right', ['Right', '!&Click', '&Menu', 'E&xit', 'Properties']],
                    # transparent_color= '#9FB8AD',
                    resizable=True,
                    keep_on_top=True,
                    element_justification='left',
                    metadata='My window metadata',
                    # ttk_theme=THEME_VISTA,
                    # icon=PSG_DEBUGGER_LOGO
                    )
    # graph_elem.DrawCircle((200, 200), 50, 'blue')
    i = 0
    Print('', location=(0, 0), font='Courier 10', size=(100, 20), grab_anywhere=True)
    # print(window.element_list())
    while True:  # Event Loop
        event, values = window.Read(timeout=5)
        if event != TIMEOUT_KEY:
            print(event, values)
            Print(event, text_color='white', background_color='red', end='')
            Print(values)
        if event is None or event == 'Exit':
            break
        if i < 800:
            graph_elem.DrawLine((i, 0), (i, randint(0, 300)), width=1, color='#{:06x}'.format(randint(0, 0xffffff)))
        else:
            graph_elem.Move(-1, 0)
            graph_elem.DrawLine((i, 0), (i, randint(0, 300)), width=1, color='#{:06x}'.format(randint(0, 0xffffff)))
        window['+PROGRESS+'].UpdateBar(i % 800)
        window.Element('_IMAGE_').UpdateAnimation(DEFAULT_BASE64_LOADING_GIF, time_between_frames=50)
        i += 1
        if event == 'Button':
            window.Element('_TEXT1_').SetTooltip('NEW TEXT')
            window.Element('_MENU_').Update(visible=True)
        elif event.startswith('Hide'):
            # window.Normal()
            window.Element('_MENU_').Update(visible=False)
        elif event == 'Popout':
            show_debugger_popout_window()
        elif event == 'Launch Debugger':
            show_debugger_window()
        elif event == 'About...':
            popup_no_wait('About this program...', 'You are looking at the test harness for the PySimpleGUI program')
        elif event.startswith('See'):
            window.set_transparent_color(theme_background_color())
        elif event == '-INSTALL-':
            _upgrade_gui()

        i += 1
        # _refresh_debugger()
    window.close()


# ------------------------ PEP8-ify The SDK ------------------------#

change_look_and_feel = ChangeLookAndFeel
convert_args_to_single_string = ConvertArgsToSingleString
convert_flex_to_tk = ConvertFlexToTK
easy_print = EasyPrint
easy_print_close = EasyPrintClose
fill_form_with_values = FillFormWithValues
get_complimentary_hex = GetComplimentaryHex
list_of_look_and_feel_values = ListOfLookAndFeelValues
obj_to_string = ObjToString
obj_to_string_single_obj = ObjToStringSingleObj
one_line_progress_meter = OneLineProgressMeter
one_line_progress_meter_cancel = OneLineProgressMeterCancel
popup = Popup
popup_animated = PopupAnimated
popup_annoying = PopupAnnoying
popup_auto_close = PopupAutoClose
popup_cancel = PopupCancel
popup_error = PopupError
popup_get_file = PopupGetFile
popup_get_folder = PopupGetFolder
popup_get_text = PopupGetText
popup_no_border = PopupNoBorder
popup_no_buttons = PopupNoButtons
popup_no_frame = PopupNoFrame
popup_no_titlebar = PopupNoTitlebar
popup_no_wait = PopupNoWait
popup_non_blocking = PopupNonBlocking
popup_ok = PopupOK
popup_ok_cancel = PopupOKCancel
popup_quick = PopupQuick
popup_quick_message = PopupQuickMessage
popup_scrolled = PopupScrolled
popup_timed = PopupTimed
popup_yes_no = PopupYesNo
sgprint = Print
sgprint_close = PrintClose
rgb = RGB
set_global_icon = SetGlobalIcon
set_options = SetOptions

test = main

#------------------------ Set the "Official PySimpleGUI Theme Colors" ------------------------
theme(CURRENT_LOOK_AND_FEEL)


# -------------------------------- ENTRY POINT IF RUN STANDALONE -------------------------------- #
if __name__ == '__main__':
    # To execute the upgrade from command line, type:
    # python -m PySimpleGUI.PySimpleGUI upgrade
    if len(sys.argv) > 1 and sys.argv[1] == 'upgrade':
        _upgrade_gui()
        exit(0)

    main()
    exit(0)

