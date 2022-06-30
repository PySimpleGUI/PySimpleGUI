
The beginnings of a Dashboard.  Shows dummy data as a moving line graph, some Elements to gather input, a play and pause button. 

This demo uses a construct named "User Defined Elements".  These are functions that return an element and thus the function call can be made from inside of a layout.  In the layout there 3 elements on a row that look like this:

`[ColumnParm('Model', 1, model_dict), ColumnParm('Parameter', 2, parm_dict),ColumnParm('Data Set', 3, data_set_dict),   ],
`

`ColumnParm` returns a `Frame` Element that has a number of radio buttons inside.  

This link shows the program running on Trinket in "Published" mode:

https://pysimplegui.trinket.io/sites/quick-and-dirty-dashboard-for-reddit


And as usual here is the code:

<iframe src="https://trinket.io/embed/pygame/3fed5650f4" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>