#! /usr/bin/env python3

"""
Demo_Logging_to_GUI.py

How to ...

* Show logging messages in both CLI and GUI
* Show "pre GUI" logging messages in the GUI.
  "pre GUI" messages are created before the GUI window is created
* Patch the logger methods to behave like print()
* Use short names for loglevels
"""

import PySimpleGUI as sg

import logging
import io
import sys

__version__ = "1.2.3"
__name__ = "demo-app"

# short loglevel names
logging._levelToName = { 0: '?', 10: 'd', 20: 'i', 30: 'w', 40: 'e', 50: 'c' }

def init_log(
    level=logging.DEBUG, # debug by default. make it easier for users to report bugs
    ):

	log = logging.getLogger(__name__)
	log.setLevel(level)

	log._stderr_handler = logging.StreamHandler() # default stream: sys.stderr
	log.addHandler(log._stderr_handler)

	log._string_stream = io.StringIO()
	log._string_handler = logging.StreamHandler(stream=log._string_stream)
	log.addHandler(log._string_handler)

	log_formatter = logging.Formatter(
		# message format:
		'%(asctime)s %(levelname)s  %(message)s',
		# time format:
		#"%Y-%m-%d %H:%M:%S",
	)
	[h.setFormatter(log_formatter) for h in log.handlers]

	# make the logger methods behave like print()
    # so we can use, for example, log.info("some.var:", some.var)
	def wrap_log_method(log_method):
		def new_log(*args, **kwargs):
			# https://stackoverflow.com/a/39823534/10440128
			f = io.StringIO()
			print(*args, file=f, end="", **kwargs)
			string = f.getvalue()
			f.close()
			log_method(string)
		return new_log
	log.debug = wrap_log_method(log.debug)
	log.info = wrap_log_method(log.info)
	log.warning = wrap_log_method(log.warning)
	log.error = wrap_log_method(log.error)

	return log

log = init_log()

log.info(f"{__name__} version {__version__}")

# test
log.debug('debug message')
log.info('info message')
log.warning('warning message')
log.error('error message')
log.critical('critical message')

layout = [
    [sg.Multiline(
        font="monospace",
        size=(60, 18),
        autoscroll=True, # auto scroll to end
        horizontal_scroll=False,
        reroute_stdout=True, # send stdout to this element. this will replace sys.stdout
        reroute_stderr=True, # send stderr to this element. this will replace sys.stderr
        echo_stdout_stderr=True, # show stdout/stderr in both CLI and GUI
        key="-log-",
    )],
    [sg.Button("Log something", key="Button"), sg.Button("Exit")],
]

window = sg.Window(__name__, layout, finalize=True)

log.removeHandler(log._string_handler)
window['-log-'].update(log._string_stream.getvalue())
log._string_stream.close()
log._stderr_handler.setStream(sys.stderr) # use the new sys.stderr

log_counter = 0

def log_something():
    global log, log_counter
    #print(f"print: {log_counter}")
    log.info(f"logging.info: {log_counter}")
    log_counter += 1

while log_counter < 5:
    log_something()

while True:
    event, values = window.read()
    #print("event", event)
    if event in (None, "Exit"):
        break
    if event == "Button":
        log_something()
