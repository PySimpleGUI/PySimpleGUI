**Coin Calculator **

![SNAG-0523.jpg](/api/files/5db87c8a77188f52156f0b5e/snag-0523.jpeg "SNAG-0523.jpg")

This is an example of a program originally written for tkinter.  The length is roughly 1/2 the original program.  However, it's the readability of the lines that is the more important difference.

Note - need to add formatting of the text being output so that it's closer to looking like dollars and cents.  This can be done by modifying these 4 lines of code:
```python
    window['Quarters_total'].update(quarters)
    window['Dimes_total'].update(dimes)
    window['Nickels_total'].update(nickels)
    window['Pennies_total'].update(pennies)
```
 
Use f-strings insead of the variable names directly as paramters to `update`.  It seemed better to keep the code simpler looking than add the formatting.  
    
    

<iframe src='https://trinket.io/embed/pygame/4788483a5b?start=result' width='100%' height='550' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
