---
layout: post
title:  "Modules"
date:   2018-09-25 00:00:00 -0400
schedule:   2018-09-25 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
reading: "HtTLaCS 7.1-7.8"
exercises: "/gwu/fa18/cs1012/2018/09/25/exercises.html"
term: "fa18"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

### ```turtle``` BUG --- Error every other script execution
We have seen a consistent problem this term when drawing with the ```turtle``` in Python 3.5.  This is an obscure error that is difficult to explain; however, the solution is simple.  Instead of using just the following statement at the beginning of a turtle script:
```python
from turtle import *
```

Use the following two statements together:
```python
from turtle import *
TurtleScreen._RUNNING = True
```

> Bugs can be introduced in different versions of software.  This issue appears to be resolved in Python 3.6 and later.  It is important to keep your software updated for this reason.

### Modules
A _**module**_ is a file or set of files that contain Python definitions and statements intended for use in other Python programs.

We have been regularly using modules since our first program.  When we use the ```import``` keyword, we are instructing Python to import definitions from a module.  So for our drawing, we have been using the statement:

```python
from turtle import *
```

The above statement instructs Python to import everything ```*``` from the ```turtle``` module.  It is by importing the turtle definitions that gave us the ability to call the ```forward```, ```backward```, ```left```, ```right```, ```penup```, and ```pendown``` functions in our programs.

Similarly, we have used the following statement to import the definitions provided in the ```math``` module, _i.e._ to use the ```sqrt``` function:
```python
from math import *
```

### What Modules Are Available and How to Get Help
Every language relies on a large library of built in features or additional libraries that may have been developed by third parties.

The core Python features are extensively documented on the [Python Documentation](https://docs.python.org/3/) website.  Many fundamental operations that you might need are already defined and ready to use in any Python script, but you may need to look through the documentation to find out how to use these features.

Python also has a number of core modules that are built into the distribution.  These include the ```turtle``` module and the ```math``` module.  The list of built in Python modules can be found in the [Python Module Index](https://docs.python.org/3/py-modindex.html).

We are also using the Anaconda Package management system to ease access to a large library of third party modules.  Third parties are independent developers who have created modules that extend the capabilities of Python even further to address more sophisticated problems that are beyond the realm of the core distribution.  You can think of these third party modules as a form of app and Anaconda as a form of app store; however, these are provided free of charge.  The modules available through Anaconda provide very powerful features that allow Python developers to reuse expertise from other developers.  The [Anaconda Package Index](https://docs.anaconda.com/anaconda/packages/pkg-docs/) provides a list of all of the modules that are immediately available through Anaconda.

There are also other modules that have not been integrated into the Python core or Anaconda.  These modules may be new, may still be in an unstable or experimental state, or may simply be small projects.  These modules can be integrated into your system; however, installing and using these modules may require more investment on your part to understand your computer and may require more support by the developer.  These modules are typically found in the wild through an internet search or from conference publications.

> You should be very careful when installing and using third party packages.  Modules and packages available in the Python core or through Anaconda are widely vetted, but those that you might acquire from other third parties might have malicious intent.

### The ```import``` Statement
The python documentation describes the ```import``` statement as:
>The import statement combines two operations; it searches for the named module, then it binds the results of that search to a name in the local scope.

The ```import``` statement can be used in several ways to bind the module into a the current scope of a script at which the ```import``` statement appears.  We have been using one of these approaches by combining the ```from``` and ```import``` keywords to import all definitions from turtle and math into our scripts at global scope.  This effectively makes the definitions from the ```turtle``` and ```math``` modules visible at all levels, _i.e._ global and local, in your script.

For example, if the following statement appears at the beginning of your script, all ```turtle``` definitions are bound at the global scope:

```python
from turtle import *
```

> Recall that earlier in the course, we claimed that "all values are treated as objects".  We have chosen the above approach to importing ```turtle``` definitions in order to delay deep consideration of objects.

Alternatively, we can use the following statement to bind all ```turtle``` definitions to an object named ```turtle``` within our script.

```python
import turtle
```
The bindings produced from this statement differ from our more regular usage because all turtle definitions are bound to an object named ```turtle```.  When we used the ```from``` approach, we were able to simply call ```forward``` to call the turtle's ```forward``` function; however, if we instead bind all the turtle definitions to the ```turtle``` name, we can only access those functions if we also provide the name of the object.  For example, the following two code samples produce equivalent behavior:

```python
from turtle import *   # imports the turtle module and binds its definitions without a name
forward(100)
left(90)
forward(100)
done()
```

```python
import turtle          # imports the turtle module and binds its definitions to the name turtle
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.done()
```

### Submodules
Some modules consist of a number of components called submodules.  When we used the ```from``` keyword in our import statement, we are actually importing the submodules.

If we analyze what the ```import``` statement we have regularly used:
```python
from turtle import *
```
We are actually requesting that Python import all of the submodules from the ```turtle``` module into the current scope.  Because we provide this statement at the beginning of our scripts, we are importing all of the definitions in the ```turtle``` module into the global scope of our script.  This is why we can simply use the ```forward``` function along with any other ```turtle``` functions without using the ```turtle``` prefix, _i.e._ without needing to use ```turtle.forward```.

### Aliasing using the ```as``` keyword
We can create an _**alias**_ for a module when we import it.  Aliasing allows us to choose what name we bind the module to when we import it.  For example:

```python
import turtle as toby # imports the turtle module and binds its definitions to the name toby
toby.forward(100)
toby.left(90)
toby.forward(100)
toby.done()
```
It is important to note that When we use the ```as``` keyword, we are aliasing which means that we are effectively associating the turtle definitions with a new name.  This is in contrast to creating multiple unique turtle object or _**instances**_ of turtles with different names.

### Creating Unique Instances of ```turtle``` Objects
We can create unique turtle instances by using the ```Turtle``` constructor.  We will talk more about constructors when we discuss classes; however, the constructor is like a function that returns a new instance of an object.  In the following example, the Turtle constructor is called to create a new turtle instance named ```tina```:

```python
import turtle

tina = turtle.Turtle()     # create an instance of a turtle named tina
# these statements explicitly control the instance of tina
tina.left(90)
tina.forward(100)
tina.left(90)
tina.forward(100)

turtle.done()
```

Creating unique instances of ```turtle``` objects allows us to control different turtles independent of one another.  In the following example, we create two unique ```turtle``` instances, _i.e._ ```alice``` and ```bob```, which carry out their own instructions:
```python
import turtle

alice = turtle.Turtle()    # create an instance of a turtle named alice
alice.color("green")       # alice will draw using a green pen
# these remaining statements prefixed with alice will control on the alice turtle
alice.left(90)
alice.forward(100)
alice.left(90)
alice.forward(100)

bob = turtle.Turtle()      # create an instance of a turtle named bob
bob.color("blue")          # bob will draw using a blue pen
# these remaining statements prefixed with bob will control on the bob turtle
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)

turtle.done()
```

While the ```turtle``` module is designed to allow instancing of new objects, not all modules are designed to allow instancing.  Some modules are just a collection of definitions, _i.e._ ```math```.

### Using ```math``` Functions
The ```math``` module is a collection of mathematical functions and definitions that extend the mathematical capabilities of Python.  For example, there is no mathematical operator for computing the square root of an expression, but we have established that there is the ```sqrt``` function which accomplishes this task.

The ```math``` module provides a wide range of definitions that extend the mathematical capabilities of Python.  The ```math``` modules contains definitions for mathematical constants like ```pi```, angular functions, trigonometric functions, hyperbolic functions, logarithmic functions, etc.  Documentation for the Python ```math``` module can be found on the [Math Module Documentation Page](https://docs.python.org/3/library/math.html?highlight=math#module-math).

We have so far gained access to the ```math``` module using the following import statement:
```python
from math import *
```
This import statement binds the math functions such that we can call the ```sqrt``` function using a statement like:
```python
y = sqrt(x)
```
If we do not use the ```from``` or ```as``` keywords, we must access the math functions using the ```math``` name.  For example:
```python
import math
y = math.sqrt(10)   # the import math means we must refer to sqrt through the math name
```

### The ```random``` Module
Random numbers are a very important tool for software development and testing.  We may want to use a random process to generate information such as to simulate coin flipping or dice rolling, or we may want to generate large amounts of data for testing.  The Python distribution provides the ```random``` module to generate pseudo-random data.

There are a number of functions defined in the ```random``` module; however, the two functions we will consider are ```randrange``` and ```random```.  Documentation for the Python ```random``` module can be found on the [Random Module Documentation Page](https://docs.python.org/3/library/random.html).

```randrange``` follows the same input model as ```range``` and generates an integer between the first and second argument.  The first argument represents the lower bound and the second argument represents the upper bound and the lower bound is included in and upper bound is excluded from the range of integers that may be generated.  Every value in the range has an equal chance of being generated meaning that ```randrange``` produces a uniform distribution.  For example, the following will model a dice roll:
```python
import random
droll = random.randrange(1,7)
```

```random``` returns a floating point number in the range [0.0, 1.0) where the lower bound is closed and the upper bound is open; therefore, 0.0 can be generated while 1.0 cannot.  In order to generate a random number outside of this interval, the result can be scaled through multiplication.  For example, the following will generate a random floating point number in the range [0.0, 10.0):

```python
import random
x = random.random() * 10.0
```
