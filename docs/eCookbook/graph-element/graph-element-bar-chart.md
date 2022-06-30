## Graph Element - Bar Charts

Sometimes using Matplotlib is overkill.  

Some graphing can be done trivially with PySimpleGUI.  A **Bar Chart** in particular is *quite easy*.

The reason bar charts are simple and easy to make can be found by breaking down a bar chart.  A bar chart is literally a series of rectangles.

##  A 6-line Example

Here's an example with the minmum number of lines of code I could write and still have it be readable.

Each of the steps is 1 line of code except for the for-loop being 1 more
1. Import PySimpleGUI
2. Make the Window
3. Loop through the data
4. Draw a Bar
5. Draw a label above it with the value of the data point
6. Wait for window to be closed by user



<iframe src='https://trinket.io/embed/pygame/73aab03d9a?start=result' width='100%' height='600' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>



## Drawing X and Y Axis

This example is a copy of a chart produced using Matplotlib.  

The chart data is contained in 3 lists.

1.  The X-Axis labels for each bar
2.  The color of each bar
3.  The Y-Value for each bar
  
This example is rather specific as the number of data points was known ahead of time as was the maximum Y value.  A minumum amount of code enables you to see each component of the graph.


<iframe src='https://trinket.io/embed/pygame/ada96fdf1b?start=result' width='100%' height='600' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>




## Another Example

This chart updates every time you click the button.  The bar values are labeled as well with the label being at the top of each bar.  This is just the starting point for you to jump from and modify.



<iframe src='https://trinket.io/embed/pygame/966cc03477?start=result' width='100%' height='660' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
