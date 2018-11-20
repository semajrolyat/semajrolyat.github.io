---
layout: post
title:  "Introduction to Plotting"
date:   2018-11-20 00:00:00 -0400
schedule:   2018-11-20 00:00:00 -0400
categories: [preview]
docclass: "discussion"
gwclass: "cs1012"
---

## Using ```matplotlib```

[PyPlot](https://matplotlib.org/api/pyplot_summary.html)
[Plot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html)

```pyplot.plot``` is very flexible.  It can operate on a single vector or on a set of vectors.  If one vector is provided then the x and y dimensions will be drawn from the input vector.  For example, the following plot represents a line plot where ```x=y```

```Python
import matplotlib.pyplot as plt
import numpy as np

plt.plot(np.arange(10))
```

![Line Plot]({{"/gwu/fa18/cs1012/assets/11_20_2018/line01.png" | absolute_url }})


```Python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = x * 2
plt.plot(x, y)
```
![Line Plot 2]({{"/gwu/fa18/cs1012/assets/11_20_2018/line02.png" | absolute_url }})

### Viewing the Plot
```Python
import matplotlib.pyplot as plt
import numpy as np

plt.plot(np.arange(10))

plt.show()
```

### Saving the Plot
```Python
import matplotlib.pyplot as plt
import numpy as np

plt.plot(np.arange(10))

plt.savefig("test.png")
```

#### Labeling the Plot
```Python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = x * 2
plt.plot(x, y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Example plot')
```
![Labeled Plot]({{"/gwu/fa18/cs1012/assets/11_20_2018/label.png" | absolute_url }})

#### Plotting multiple lines
```Python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y1 = x * 2
y2 = x * 4
plt.plot(x, y1)
plt.plot(x, y2)
```
The system has automatically selected a color for each plot.

### Plotting columns
```Python
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
```Python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
plt.plot(x, color='r')
```
The color argument accepts a wide variety of color specifications which allows you to customize the color to your needs; however, understanding many of these specifications requires a discussion that is beyond the scope of this class.  For a comprehensive list of the legal color arguments refer to the [matplotlib Color reference](https://matplotlib.org/api/colors_api.html).

### Linewidth
The width of a line can be specified using the ```linewidth``` argument.  This argument is a numeric value.  For example, the following code specifies that the line should be rendered with a width of ```8```:

```Python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
plt.plot(x, linewidth=8)
```

### Linestyles
There are a variety line styles available in ```matplotlib```.  The linestyle is specified through the ```linestyle``` argument with one of the following values:
* '-' specifies a solid line
* '--' specifies a dashed line
* '-.' specifies an alternating dash-dot line
* ':' specifies a dotted line
```Python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
plt.plot(x, linestyle='--')
```

For a comprehensive list of the legal marker arguments refer to the [matplotlib Linestyle reference](https://matplotlib.org/gallery/lines_bars_and_markers/line_styles_reference.html)

### Markers
For some plots, you will want to show the points in the plot.  You can control the representation of these points using the ```marker``` argument.  Some common abbreviations for markers are:
* '.' renders the point as a small circle
* 'o' renders the point as a large circle
* '^' renders the point as a large triangle
* 's' renders the point as a large square
* 'D' renders the point as a large diamond

For example, the following code plots the points on the line using a large circle:
```Python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
plt.plot(x, marker='o')
```

For a comprehensive list of the legal marker arguments refer to the [matplotlib Markers reference](https://matplotlib.org/api/markers_api.html).

### Scatter Plot Example
```Python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y = np.random.random(100)

plt.scatter(x,y)
```

There are some cases where scatter does not work as you might expect.  You can still use the ```plot``` function to generate a scatter plot by using the ```marker``` argument and by setting the ```linewidth``` to ```0```.
```Python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y = np.random.random(100)

plt.plot(x,y,marker='o',linewidth=0)
```

### Histogram Example
```Python
import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, 1000)

plt.hist(s)
```

There are large number of statistical, probability, and signal processing functions in the ```scipy``` library.  You may need to explicitly install ```scipy``` through Anaconda to gain access to these features.

### Working with axes

### Adding a legend


### Generating data from math functions


```Python
import matplotlib.pyplot as plt
import numpy as np
# generate some sample data
x = np.arange(0, 2*math.pi, 0.1)
y = np.sin(x)
# plot the data
plt.plot(x,y)
```

```Python
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
