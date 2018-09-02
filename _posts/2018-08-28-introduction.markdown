---
layout: post
title:  "Introduction"
date:   2018-08-28 00:00:00 -0400
schedule:   2018-08-28 00:00:00 -0400
categories: Coursework
reading: "2.4-2.7"
organization: "GWU"
course: cs1012
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Why learn Python
According to the job listing site Indeed, the two sectors with the best job offerings in [2017](http://blog.indeed.com/2017/03/21/best-jobs-united-states-2017/) and [2018](http://blog.indeed.com/2018/03/15/best-jobs-united-states/) are computer related fields.  


Computer programming is becoming a necessary skill that services a large number of sectors.  The website Stack Overflow is dedicated to answering programming questions, and according to their metrics, the demand for Python programming skills is [growing rapidly](https://stackoverflow.blog/2017/09/06/incredible-growth-python/) across a [variety of economic sectors](https://stackoverflow.blog/2017/09/14/python-growing-quickly/).


It can be argued that those that develop domain expertise in fields outside of computer science are often best suited to translating that knowledge into software and it is not necessary to earn a Computer Science degree to [be in demand](https://www.forbes.com/sites/georgeanders/2015/07/29/liberal-arts-degree-tech/#19e268c1745d) in the technology sector.

## Preliminaries
We will be using Anaconda to ease the problems surrounding installion and maintenance of Python and any additional packages.  We will be working in Python version 3 for this class.  You must install Anaconda - Python version 3.x on a laptop and bring it to all future classes.  Anaconda can be downloaded from the [Anaconda Download Page](https://www.anaconda.com/download/).

We will use the online, interactive book [How to Think Like a Computer Scientist](http://interactivepython.org/courselib/static/thinkcspy/index.html) for the course.  You will be assigned readings from the book that must be read before the next class.

At some point, you may need a the unadulterated [Python 3 Documentation](https://docs.python.org/3/index.html) as a reference.

You may find exercises beyond the course on [Coding Bat](https://codingbat.com/python) and [LeetCode](https://leetcode.com/).

# Interactive Python
To open an interactive python at a shell prompt, type the following at the command line:
```
$ python
```
In this and future course documents, the `$` will be used to indicate that the instruction is typed at a command prompt.  For Windows users, the command prompt is accessible through the Anaconda Prompt under the Start menu.  For MacOS users, the command prompt is accessable through the Terminal window.

The command line environment will give a visual indicator that the shell is not inside the python interpreter.  The Python interactive environment is indicated by three right angle braces, `>>>`:
```Python
>>>
```

To exit the Python interactive environment, call quit with the following statement:
```Python
>>> quit()
```

## Python Turtle
Python Turtle Graphics is based on the Logo educational programming language that was developed in 1967.  This language allows a novice programmer to jump right in and draw complex pictures using simple statements.

To run Python Turtle Graphics, type:
{% highlight python %}
>>> from turtle import *
{% endhighlight %}

To begin drawing with the turtle, type:
{% highlight python %}
>>> from turtle import *
>>> forward(100)
{% endhighlight %}

The turtle begins in the center and oriented toward the right hand side of the screen or canvas with the pen down.  The `forward(100)` statement instructs the turtle to move forward 100 units and then stop.  The turtle is now positioned 100 units to the right of the center of the screen.  Because the pen was down during the turtle's movement, the movement results in a line being drawn on the canvas.

### Basic Turtle Control
#### Movement
To move the turtle forward 100 units type:
{% highlight python %}
>>> forward(100)
{% endhighlight %}

To move the turtle backward 100 units type:
{% highlight python %}
>>> backward(100)
{% endhighlight %}

To turn the turtle 90 degrees to the right type:
{% highlight python %}
>>> right(90)
{% endhighlight %}

To turn the turtle 90 degrees to the left type:
{% highlight python %}
>>> left(90)
{% endhighlight %}

#### Controlling the Pen
To lower the pen (the pen is lowered by default) type:
{% highlight python %}
>>> pendown()
{% endhighlight %}

To raise the pen (and not draw until the pen is lowered again) type:
{% highlight python %}
>>> penup()
{% endhighlight %}

#### Reference
For a full reference for Python Turtle Graphics refer to the [Python Documentation](https://docs.python.org/3/library/turtle.html#turtle-methods)

## Exercises
Before trying to write any code, plan out how you will to use the primitives defined here to draw the solution.  If you don't plan, you may make a mistake and have to start over.  It's a good idea to have pen and paper available.

You are allowed to collaborate with your neighbor on these exercises.  Each of you must complete the programming tasks individually; however, you are encouraged to discuss and work together to design a solution to the problems.

Take a screenshot of each of your solutions and save each screenshot.  Create a zip archive containing all of your screenshots and submit them to blackboard.

------
To take a screenshot of a window:

(Mac) hold down **Cmd+Shift+4**

(Windows) hold **Alt+PrtSc**

------

### Example 1 - Drawing a Square
Suppose we wish to draw a square.  We can do so using the following set of statements:
{% highlight python %}
>>> from turtle import *
>>> forward(100)
>>> left(90)
>>> forward(100)
>>> left(90)
>>> forward(100)
>>> left(90)
>>> forward(100)
{% endhighlight %}

The turtle will draw a square similar to the following image:

![Example 1 Square]({{ "/assets/gwu/cs1012/1/example1.png" | absolute_url }})

### Exercise 1 - Center the Square
The square in Example 1 is not centered in the middle of the canvas.  Using the statements described above, how can you draw the same square centered in the canvas?  The turtle should end up in the same corner of the square as in Example 1.

Draw the square.  The result should look like the following image:

![Exercise 1 Square]({{ "/assets/gwu/cs1012/1/exercise1.png" | absolute_url }})

### Example 2 - Drawing a Circle
While is is possible to draw a circle using a sequence of primitive moving and turning statements, such a program would be cumbersome to write.  Fortunately, there is a built in `circle` that we can use to control the turtle.

We can use the following python code to draw a circle from the turtle's starting position with a diameter of 100 units:
{% highlight python %}
>>> from turtle import *
>>> circle(50)
{% endhighlight %}
Note that number supplied to the circle is half the diameter which is by definition the radius of the circle.

The turtle will draw a circle similar to the following image:

![Example 2 Circle]({{ "/assets/gwu/cs1012/1/example2.png" | absolute_url }})

### Exercise 2 - Circumscribe a Centered Diamond
In this exercise, you will draw a diamond that has a circle drawn around it.  The diamond should be centered in the canvas and should have the same dimensions as the square in Exercise 1.  This diamond is simply a square rotated by 45 degrees.  The turtle should end up at the bottom-most point of the diamond and rotated toward the right hand side of the canvas.

Recall that the pythagorean theorem is a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup>

Draw the circumscribed diamond.  The result should look like the following image:

![Exercise 2 Diamond]({{ "/assets/gwu/cs1012/1/exercise2.png" | absolute_url }})

### Example 3 - Running a Python Script
While we can accomplish a lot using the interactive python prompt, writing a program entirely at the prompt poses a number of problems:
* Mistakes are costly.  If you make a mistake, it can be difficult to correct without starting over.
* To run the same program again, you have to rewrite the program which opens up the possiblity of making a new mistake each time you write the program.

Instead of writing code at the interactive python prompt, we can instead write a python program, typically called a script and run the script at a shell prompt.  A python script must have the file extension `.py`.  

Suppose you write a script for Exercise 2 named `exercise2.py`.  You can run the script at the shell using the following command:
```
$ python exercise2.py
```
There are some special rules for specifying the file for different shells.  With the number of different platforms in the class, we will discuss this as it arises.

Unfortunately, the Python Turtle Graphics window will automatically close if the end of a script is reached without the encountering the following instruction:
{% highlight python %}
done()
{% endhighlight %}

If we were to write Example 1 as a script, the contents of the file would read:
{% highlight python %}
# This script is recreates Example 1
from turtle import *

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
done()
{% endhighlight %}



### Exercise 3 - Draw a House
In this exercise, write a python script to draw a house.  You do not have to draw the house exactly as illustrated in the image below; however, it should have the same general characteristics: a pitched roof, a centered door and a window on either side of the door.  The turtle can end up anywhere you choose.

![Exercise 3 House]({{ "/assets/gwu/cs1012/1/exercise3.png" | absolute_url }})

## Reflection
Drawing with a Turtle program may appear to be overly simple; however, the simplicity of today's work masks some very important concepts.

We wrote our first programs.  Programming boils down to learning the primitive operations that are available in your language of choice and combining those operations in a variety of ways to accomplish our goal.  Conversely, designing a program involves taking a large task and breaking it down into simple steps that can be expressed by the primitive operations available to you.

We were able to accomplish these tasks without a significant amount of math.  Non-programmers often believe that programming requires deep mathematical understanding.  While sophisticated mathematics may be necessary to solve domain specific problems or to optimize programs so that they run as fast as possible, most programming does not involve more math than simple algebra or trigonometry.

We converted problems described by natural language into code.  Word problems are almost universally loathed, but much of programming (or any professional task) involves converting a description provided by a client, _i.e._ a word problem, into a technical solution.

We introduced the concept of a script or a file containing source code.  Programming principally involves the reading and writing of source code.  Ideally, we hope to write source code once, but the reality is that the same source code may be read and rewritten many times so readability is an important consideration.  Throughout this course, readability and organizational techniques will be an important topic that you will only come to appreciate once you have significant programming experience.
