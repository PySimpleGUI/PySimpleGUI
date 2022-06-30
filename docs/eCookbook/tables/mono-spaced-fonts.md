## Mono-Spaced Fonts

Let's start tables using text.

One common problem when working with text and tables is how to get columns to align properly.  Most fonts, including the default font, are variable spaced.... each character is a slightly different width than others.

Here's an example using the font used on this webpage.  Each of these rows of character are 10 chars long.  But,  they are clearly different lengths.


1234567890   
aaaaaaaaaa  
iiiiiiiiii    


What to do?  Entry our friend the mono-spaced font where each character takes up the exact same width as all the other characters.  The most common of these mono-spaced fonts is "Courier".  These same rows of characters, when formatted using a Courier font have the same length:

```
1234567890   
aaaaaaaaaa  
iiiiiiiiii    
```

Now let's try this out in a PySimpleGUI program.

This program presents a table in a Multiline element using a default font, which will have variable spaces.  As you will initially see, the table is a mess.  But, by changing the font of the Multiline to a Courier font, the table become tidy and clear.

<iframe src='https://trinket.io/embed/pygame/192aeae1a7?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
