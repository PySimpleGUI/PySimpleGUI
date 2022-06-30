The ability to output text in multiple colors has been a long-requested feature for PySimpleGUI.  It's finally here.

It should be noted that it does not use ANSI codes embedded into strings in order to accomplish this.  Instead you specify the colors when you send the text to the `Multiline` element via its `update` method.


<iframe src='https://trinket.io/embed/pygame/f665612d7d?start=result' width='100%' height='650' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
