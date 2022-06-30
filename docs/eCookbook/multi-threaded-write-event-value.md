## Example using `Window.write_event_value`

In July 2020 an important upgrade was added to the multithreaded capabilities of PySimpleGUI.  Gone are the requirements to poll for incoming messages from threads.  Now "events" from threads are received through the normal event loop.

The technique has several benefits including:

1. Efficiency - Polling is inefficient. Removing the polling added back a lot of CPI time
2. Simplicity - Communicating between a window and a thread is a single function call, `Window.write_event_value`
3. Encapsulation - The actual communication between the thread and the user's application is encapsulated within PySimpleGUI itself using a `queue.Queue` object.
 
This specific demo shows a couple of newer features in addition to the `write_event_value` call.  It also shows how the routing of `cprint` calls can be accomplished by the `Multiline` definition itself.

### Communicating Between Thread and Event Loop

The most important line of code in this entire program is this one:

```python
window.write_event_value('-THREAD-', (threading.current_thread().name, i))
```

This call will cause an event to be generated and is read in the event loop when the main program calls `window.read()`.

In this example, the event that will be generated is `'-THREAD-'`
The values dictionary will also have an entry associated with that "key". In this call we passed a tuple with the values:
```python
(threading.current_thread().name, i)
```

The first entry in the tuple is the name that Python assigned the thread.  The second part of the tuple is a counter.  You will see these values in the output window in red.


### Screenshot on Windows

On windows, the output looks something like this:

![SNAG-0865.jpg](/api/files/5f133f9986e5654c74274796/snag-0865.jpeg "SNAG-0865.jpg")


<iframe src='https://trinket.io/embed/pygame/f1e7022af2?start=result' width='100%' height='600' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
