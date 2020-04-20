---
layout: post
title:  "Introduction to Plotting"
date:   2020-04-20 00:00:00 -0400
schedule:   2020-04-20 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
term: "sp20"
---

## Using ```matplotlib```
This is a very simple introduction to ```matplotlib```.  There are many features that cannot be touched on here, so we will focus on a general introduction to using the module and there are a much deeper layers to the module that we unfortunately do not have time to discuss in this course.  I hope this introduction will inspire you to explore the module more and more as you find more applications for it.

We will focus in the [PyPlot](https://matplotlib.org/api/pyplot_summary.html) module in ```matplotlib```.  This module primarily focuses on the [```plot```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html) function; however, there are a large number of other plotting functions that can generate a variety of other types of plots.

The ```pyplot.plot``` function is very flexible.  It can operate on a single vector or on a set of vectors.  If one vector is provided then the x and y dimensions will be drawn from the input vector.  For example, the following plot represents a line plot where ```x=y```

```python
import matplotlib.pyplot as plt
import numpy as np

plt.plot(np.arange(10))
```

![Line Plot]({{"/gwu/fa18/cs1012/assets/11_20_2018/line01.png" | absolute_url }})

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = x * 2
plt.plot(x, y)
```
![Line Plot 2]({{"/gwu/fa18/cs1012/assets/11_20_2018/line02.png" | absolute_url }})

### Viewing the Plot
If we wish to view the plot, we can call the ```pyplot.show``` function which will display the plot in a special viewing window.

> In spyder, the plot is displayed in the console, so it is not necessary to call ```show```; however, if you run your scripts at the console, you may wish to use ```show```.

```python
import matplotlib.pyplot as plt
import numpy as np

plt.plot(np.arange(10))

plt.show()
```

### Saving the Figure
We can automatically save the figure generated using the ```savefig``` function.  You must provide a filename when calling ```savefig``` and the image that is produced will be saved by default into the folder in which the script was run.  The following example generates a simple plot and then saves the figure as ```test.png```:
```python
import matplotlib.pyplot as plt
import numpy as np

plt.plot(np.arange(10))

plt.savefig("test.png")
```

The format of the file is determined by the extension provided in the filename.  In general, the ```png``` file format will produce high quality images that are still small.

The ```savefig``` function may take a number of arguments.  One of these arguments, ```dpi```, is useful if we need to increase the resolution and therefore the quality of the image that is produced.  ```dpi``` is short for dots-per-square-inch and it requires a numeric value.  For example, the following code generates a plot and then saves the figure with a ```200``` ```dpi```:

```python
import matplotlib.pyplot as plt
import numpy as np

plt.plot(np.arange(10))

plt.savefig("test.png", dpi=200)
```

For more information on ```savefig``` refer to the [matplotlib ```savefig``` reference page](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html)

#### Labeling the Plot
We can label a plot by calling the ```xlabel```, ```ylabel```, and ```title``` functions.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = x * 2
plt.plot(x, y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Example plot')
```

> You may need to manipulate font properties such as type and size.  These require more advanced interaction with ```pyplot``` than is described here; however, there are extensive number of operations that allow you to fully customize the image that is generated.

![Labeled Plot]({{"/gwu/fa18/cs1012/assets/11_20_2018/label.png" | absolute_url }})

#### Plotting multiple lines
A single call to ```plot``` will plot a line; however, there is no limit to the number of times that ```plot``` can be called.  For each call to ```plot```, ```pyplot``` will generate a new line.  This way we can represent muliple data sets and compare the two.  For example, the following illustrates generating two lines:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y1 = x * 2
y2 = x * 4
plt.plot(x, y1)
plt.plot(x, y2)
```
Note that the system has automatically selected a color for each plot.

![Multiline Plot]({{"/gwu/fa18/cs1012/assets/11_20_2018/multiline.png" | absolute_url }})

### Plotting columns
If our data is stored in a multidimensional ```numpy``` array, we can pass individual columns into each call to ```plot```.  For example, the following code generates a ```numpy``` array where the first column represents time, the second column represents data from a first experimental trial, and the third column represents data from a second experimental trial:

```python
import matplotlib.pyplot as plt
import numpy as np

# load data... format[time, exp1, exp2]
data = np.zeros((100,3))             # 100 rows x 3 columns
data[:,0] = np.arange(0,10,0.1)      # time
data[:,1] = np.random.random(100)    # exp1
data[:,2] = np.random.random(100)    # exp2

# plot exp1 w.r.t time
plt.plot(data[:,0],data[:,1])
# plot exp2 w.r.t time
plt.plot(data[:,0],data[:,2])
```

The primary restriction with a plot is that the length of the ```x``` vector and the accompanying ```y``` vector must have the same length.  In the above example, the array has 100 records, so the length of the ```x``` vector is the same as the lengths of the second and third columns.

![numpy Columns Plot]({{"/gwu/fa18/cs1012/assets/11_20_2018/columns.png" | absolute_url }})

### Designating color
There are a variety of ways to specify color.  The simplest way is to pass one of the legal abbreviations to the ```color``` argument.  The legal abbreviations are:
* 'r' for red
* 'g' for green
* 'b' for blue
* 'c' for cyan
* 'm' for magenta
* 'y' for yellow
* 'k' for black
* 'w' for white

For example, to specify that a line should be plotted in red, you can pass ```r``` as the color argument:
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
plt.plot(x, color='r')
```

![Colors]({{"/gwu/fa18/cs1012/assets/11_20_2018/colors.png" | absolute_url }})

The color argument accepts a wide variety of color specifications which allows you to customize the color to your needs; however, understanding many of these specifications requires a discussion that is beyond the scope of this class.  For a comprehensive list of the legal color arguments refer to the [matplotlib Color reference](https://matplotlib.org/api/colors_api.html).

### Linewidth
The width of a line can be specified using the ```linewidth``` argument.  This argument is a numeric value.  For example, the following code specifies that the line should be rendered with a width of ```8```:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
plt.plot(x, linewidth=8)
```

![Linewidth]({{"/gwu/fa18/cs1012/assets/11_20_2018/linewidth.png" | absolute_url }})

### Linestyles
There are a variety line styles available in ```matplotlib```.  The linestyle is specified through the ```linestyle``` argument with one of the following values:
* '-' specifies a solid line
* '--' specifies a dashed line
* '-.' specifies an alternating dash-dot line
* ':' specifies a dotted line

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
plt.plot(x, linestyle='--')
```

![Linestyle]({{"/gwu/fa18/cs1012/assets/11_20_2018/linestyle.png" | absolute_url }})


For a comprehensive list of the legal marker arguments refer to the [matplotlib Linestyle reference](https://matplotlib.org/gallery/lines_bars_and_markers/line_styles_reference.html)

### Markers
For some plots, you will want to show the points in the plot.  You can control the representation of these points using the ```marker``` argument.  Some common abbreviations for markers are:
* '.' renders the point as a small circle
* 'o' renders the point as a large circle
* '^' renders the point as a large triangle
* 's' renders the point as a large square
* 'D' renders the point as a large diamond

For example, the following code plots the points on the line using a large circle:
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
plt.plot(x, marker='o')
```

![Markers]({{"/gwu/fa18/cs1012/assets/11_20_2018/markers.png" | absolute_url }})

For a comprehensive list of the legal marker arguments refer to the [matplotlib Markers reference](https://matplotlib.org/api/markers_api.html).

### Scatter Plot Example
As suggested above, ```pyplot``` has a number of other plotting features.  We can generate a scatter plot using the ```scatter``` function.  For example, the following code generates a scatter plot using data generated from ```numpy.random```:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y = np.random.random(100)

plt.scatter(x,y)
```
![Scatter Plot]({{"/gwu/fa18/cs1012/assets/11_20_2018/scatter01.png" | absolute_url }})

There are some cases where scatter does not work as you might expect.  You can still use the ```plot``` function to generate a scatter plot by using the ```marker``` argument and by setting the ```linewidth``` to ```0```.
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y = np.random.random(100)

plt.plot(x,y,marker='o',linewidth=0)
```
![Scatter Plot]({{"/gwu/fa18/cs1012/assets/11_20_2018/scatter02.png" | absolute_url }})

### Histogram Example
As opposed to the more general linear or scatter plots, some plots are specialized statistical tools.  One example is the histogram, in ```pyplot``` the ```hist``` function, which represents a count of the number of samples that fall into a particular bin.  The histogram shows how tightly clustered/related data is given the right granularity.

A chart designer can choose between having a few bins where many items are counted in a single bin or having many bins where very few items are counted together.  Choosing the appropriate number of bins can significantly change the perspective on the data: too few and all samples are tightly clustered into a few bins; too many and very few samples are clustered together.

The following code uses the normal distribution function from ```numpy.random``` to produce a normal distribution and then plots a histogram of the distribution using the ```hist``` function:

```python
import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, 1000)

plt.hist(s)
```

If the number of bins is omitted as above the default number of bins of 10 is chosen.

![Histogram]({{"/gwu/fa18/cs1012/assets/11_20_2018/histogram.png" | absolute_url }})

To control the number of bins, pass the ```bin``` parameter when calling the ```hist``` function.  For example, this program increases the number of bins from the default of ```10``` to ```50```:

```python
import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, 1000)

plt.hist(s, bins=50)
```

### Pie Chart Example
Another statistical tool is the pie chart which shows apportionment of subsets of data within the larger set.  With a pie chart, we can see how much weight a particular subset has.

For example, the following pie chart illustrates preferences of primary pizza topping among the US population in the early 2010's:

```python
import matplotlib.pyplot as plt

labels = 'Pepperoni', 'Sausage', 'Beef', 'Chicken', 'Cheese', 'Vegetables', 'Other'
sizes = [36, 14, 4, 7, 8, 19, 12]

plt.pie(sizes)

plt.show()
```

The above code produces the following plot:

![Basic Pie]({{"/gwu/fa18/cs1012/assets/11_20_2018/basicpie.png" | absolute_url }})

While the above generates a plot, it is not entirely useful as it is not labeled and it's not clear how the renderer generated the slices.  We can control the pie plot by using a number of parameters.  For example, the following code generates a plot from the same data, but the plot is now labeled and the initial positioning of the first slice is specified:

```python
import matplotlib.pyplot as plt

labels = 'Pepperoni', 'Sausage', 'Beef', 'Chicken', 'Cheese', 'Vegetables', 'Other'
sizes = [36, 14, 4, 7, 8, 19, 12]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.show()
```

The above code produces the following plot:

![Labeled Pie]({{"/gwu/fa18/cs1012/assets/11_20_2018/labeledpie.png" | absolute_url }})

There are many optional parameters for the ```pie``` function.  Most of the details are beyond this introduction; however, you should look at the ```pie``` function [reference documentation](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.pie.html) for additional features and examples.

### Generating data from math functions
We may wish to compare data from an experimental set with an analytical solution.  The following example demonstrates how to plot the ```sin``` function by sampling ```sin``` using evenly spaced inputs:

```python
import matplotlib.pyplot as plt
import numpy as np
# generate some sample data
x = np.arange(0, 2*math.pi, 0.1)
y = np.sin(x)
# plot the data
plt.plot(x,y)
```
![Math Functions]({{"/gwu/fa18/cs1012/assets/11_20_2018/math01.png" | absolute_url }})

We can generate a number of plots for different analytical problems using the same technique and plotting each of the computed data sets.  For example, the following code plots the ```sin``` and ```cos``` functions over the interval ```[0,2pi]```:

```python
import matplotlib.pyplot as plt
import numpy as np
# generate some sample data
x = np.arange(0, 2*math.pi, 0.1)
s = np.sin(x)
c = np.cos(x)
# plot the data
plt.plot(x,s)
plt.plot(x,c)
```

![Math Functions]({{"/gwu/fa18/cs1012/assets/11_20_2018/math02.png" | absolute_url }})

> There are large number of statistical, probability, and signal processing functions in the ```scipy``` library.  You may need to explicitly install ```scipy``` through Anaconda to gain access to these features.

### Adding a legend
You may wish to generate a legend for your plot.  You may do this by passing a ```label``` argument when plotting a line and then calling the ```legend``` function to generate the legend.

```python
import matplotlib.pyplot as plt
import numpy as np
# generate some sample data
x = np.arange(0, 2*math.pi, 0.1)
s = np.sin(x)
c = np.cos(x)
# plot the data
plt.plot(x,s, label='sin(x)')  # assign the legend label
plt.plot(x,c, label='cos(x)')  # assign the legend label
# add a legend
plt.legend()
```
![Legend]({{"/gwu/fa18/cs1012/assets/11_20_2018/legend01.png" | absolute_url }})

By default, ```legend``` attempts to place the legend in the 'best' location, a location that does not mask anything that was drawn.  If you wish to force the location, you can pass the ```loc``` argument with a numeric value to the call to ```legend```.  Refer to the [documentation](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html) for more information on location parameters.  The following example passes ```1``` as the location argument which draws the legend in the top right corner:

```python
import matplotlib.pyplot as plt
import numpy as np
# generate some sample data
x = np.arange(0, 2*math.pi, 0.1)
s = np.sin(x)
c = np.cos(x)
# plot the data
plt.plot(x,s, label='sin(x)')
plt.plot(x,c, label='cos(x)')
# add a legend
plt.legend(loc=1)     # draw the legend in the top right corner
```

![Legend Top Right]({{"/gwu/fa18/cs1012/assets/11_20_2018/legend02.png" | absolute_url }})

For detailed information on using ```legend```, refer to the [matplotlib ```legend``` reference page](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html).

### ```matplotlib.pyplot.subplot```
The ```matplotlib.pyplot.subplot``` interface allows us to draw more than one plot onto a single figure.  

A figure represents the overall drawing while each individual plot created within that figure is an axes.  If we use the base ```matplotlib.pyplot``` interface, we draw on the default figure and the default axes.  If we use this approach, we don't realize that we interact with these objects because we can perform all of the same operations through the ```matplotlib.pyplot``` interface.

Consider the following two examples:
**Example 1**
```python
import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0, 2*math.pi, 0.1)
s = np.sin(x)

plt.plot(x,s)
```
**Example 2**
```python
import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0, 2*math.pi, 0.1)
s = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x,s)
```
Both of the above programs produce the same plot as shown below; however, the first program generates the plot using the ```matplotlib.pyplot``` interface while the second program generates the plot through the axes generated through the ```matplotlib.pyplot.subplot``` interface.

![Plot vs Subplot]({{"/gwu/fa19/cs1012/assets/discussion11/pltvssubplot.png" | absolute_url }})

It seems that we do not need the more complex ```matplotlib.pyplot.subplot``` interface if we can simply use the ```matplotlib.pyplot``` interface.  For many basic cases, this might be true; however, for many sophisticated plots, we will need to work with the figure and axes object.  For example, if we wish to plot multiple plots to a single figure so that we may directly compare one to another, we will want to use the ```matplotlib.pyplot.subplot``` interface.   

#### Creating Subplots

Lets revisit the earlier example where we plotted the sine and cosine plots on the same axes.  We might instead wish to present this information as two separate plots.  For example, the following figure plots the sine and cosine functions to independent axes in the same figure:

```python
import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0, 2*math.pi, 0.1)
s = np.sin(x)
c = np.cos(x)

fig, (ax1, ax2) = plt.subplots(2,1)
ax1.plot(x,s)
ax2.plot(x,c)
```

The above program produces the following figure:

![Trigonometric Subplots]({{"/gwu/fa19/cs1012/assets/discussion11/trigsubplot.png" | absolute_url }})

The plotting functions attached to the ```matplotlib.pyplot``` object plot to the default figure and axes; however, if we generate a set of subplots, we create an axes for each subplot, _e.g._ ```ax1``` and ```ax2```, and we can plot to the desired subplot using the methods associated with the respective axes.  

Each axes is therefore its own plot and can represent data independently from one another.  For example, the following program creates a figure that contains two subplots where one subplot is a line plot and the other is a histogram:

```python
import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0, 2*math.pi, 0.1)
s = np.sin(x)
h = np.random.normal(0, 0.5, 1000)

fig, (ax1, ax2) = plt.subplots(2,1)
ax1.plot(x,s)
ax2.hist(h,bins=25)
```

The above program produces the following plot:

![Mixed Subplot]({{"/gwu/fa19/cs1012/assets/discussion11/mixedsubplot.png" | absolute_url }})
