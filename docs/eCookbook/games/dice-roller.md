## Dice Roller

A classic beginner problem to solve.... simulate rolling some dice.

This little program allows you to choose the numer of sides on the dice and the number of dice to roll.  

There's nothing really tricky about this program.  The rolling and display of the results has been compressed down to a single line of code:
```python
    window['-ROLLED-'].update(' '.join([str(random.randint(0, int(values['-DICE-'])-1)+1) for i in range(int(values['-NUM DICE-']))]))

```

A list comprehension is used to generate the list of dice results, combined into a single string and then output in the window.


<iframe src='https://trinket.io/embed/pygame/cc8f84f76b?start=result' width='100%' height='600' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
