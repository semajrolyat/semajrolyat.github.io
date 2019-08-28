---
layout: post
title:  "Introduction"
date:   2019-08-26 00:00:00 -0400
schedule:   2019-08-26 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
reading: "HtTLaCS 2.4-2.7"
exercises: "/gwu/sp19/cs1012/2019/08/28/exercises.html"
term: "fa19"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Why learn Python
According to the job listing site Indeed, the two sectors with the best job offerings in [2017](http://blog.indeed.com/2017/03/21/best-jobs-united-states-2017/) and [2018](http://blog.indeed.com/2018/03/15/best-jobs-united-states/) are computer related fields.


Computer programming is becoming a necessary skill that services a large number of sectors.  The website Stack Overflow is dedicated to answering programming questions, and according to their metrics, the demand for Python programming skills is [growing rapidly](https://stackoverflow.blog/2017/09/06/incredible-growth-python/) across a [variety of economic sectors](https://stackoverflow.blog/2017/09/14/python-growing-quickly/).


It can be argued that those that develop domain expertise in fields outside of computer science are often best suited to translating that knowledge into software.  It is not necessary to earn a Computer Science degree to [be in demand](https://www.forbes.com/sites/georgeanders/2015/07/29/liberal-arts-degree-tech/#19e268c1745d) in the technology sector and there is a wide demand among all industries for [T-shaped people](https://collegeinfogeek.com/become-t-shaped-person/).

## Preliminaries
We will be using Anaconda to ease the problems surrounding installation and maintenance of Python and any additional packages.  We will be working in Python version 3 for this class.  Anaconda is installed on the lab computers; however, you are heavily encouraged to install Anaconda 3 (Python version 3.x) on a laptop and bring it to all future classes.  Anaconda can be downloaded from the [Anaconda Download Page](https://www.anaconda.com/download/).

We will use the online, interactive book [How to Think Like a Computer Scientist](http://interactivepython.org/courselib/static/thinkcspy/index.html) for the course.  You will be assigned readings from the book that must be read before the next class.

At some point, you may need the unadulterated [Python 3 Documentation](https://docs.python.org/3/index.html) as a reference.

You may find exercises beyond the course on [Coding Bat](https://codingbat.com/python) and [LeetCode](https://leetcode.com/).

# The Python Interactive Environment
The Python Interactive Environment is a command line environment where you may execute Python commands.

To open Interactive Python at a shell prompt, type the following at the command line:
```
$ python
```
In this and future course documents, the `$` will be used to indicate that the instruction is typed at a command prompt.  For Windows users, the command prompt is accessible through the Anaconda Prompt under the Start menu.  For MacOS users, the command prompt is accessible through the Terminal window.

The command line environment will give a visual indicator that the shell is not inside the python interpreter.  The Python interactive environment is indicated by three right angle braces, `>>>`:
```Python
>>>
```

To exit the Python interactive environment, call quit with the following statement:
```Python
>>> quit()
```

## Hello World
The first program that is taught in most language is called "Hello World".  This program prints "Hello World" to the screen.  In Python, this program is very simple and consists of one line of code.

In the Python Interactive Environment enter the following command:
```Python
>>> print("Hello World!")
```

Python will respond:
```
Hello World!
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
