## Fixed Size Columns - With `element_justification`

Generally speaking, PySimpleGUI likes it when you don't force sizes of things to be a specific number of pixels.  Instead, it's suggested that you make things "float", to size themselves.

The `Column` element supports setting a specific size for the Column, however, the use of the paramter `element_justification` does not work on these fixed size Columns.  Instead, another approach is needed.  
Two options are (there may be more of course):
1. Use a `Frame` element
2. Instead of `size` parameter, use a `Sizer` element

### The Frame Solution

The easiest approach is to use a `Frame` element instead of a `Column`.  If using a `Frame` element, then setting a fixed size works with the `element_justification` parameter.

In order to get the vertical alignment the easiest solution is to use the `VPush` element above and below the layout.  This will "push" from the top and the bottom with the result being that the layout is centered vertically.


<iframe src='https://trinket.io/embed/pygame/e240ba6e38?start=result' width='100%' height='600' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>


### The Column Solution

The way to get both a fixed size Column and have the interrior be able to be justified is to use a little-known "helper element" called `Sizer`.  This element simply adds space in horizontal and veritcal directions.  The implementation of it is that it's simply a Column with padding added.  

To help you use these, this demo was created.  It makes a "User Defined Element" (a function that looks like an element and can be used in layouts) that acts like a Column that enables you to have both a size and an element_justification parameter.


<iframe src='https://trinket.io/embed/pygame/f38bc15b69?start=result' width='100%' height='600' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
