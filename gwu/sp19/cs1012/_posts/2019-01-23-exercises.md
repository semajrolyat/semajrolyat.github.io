---
layout: post
title:  "Exercises"
date:   2019-01-23 00:00:00 -0400
schedule:   2019-01-23 00:00:00 -0400
categories: [GWU]
docclass: "exercises"
gwclass: "cs1012"
term: "sp19"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Exercises 1

Before trying to write any code, plan out how you will to use the primitives defined here to draw the solution.  If you don't plan, you may make a mistake and have to start over.  It's a good idea to have pen and paper available.

You are allowed to collaborate with your neighbor on these exercises.  Each of you must complete the programming tasks individually; however, you are encouraged to discuss and work together to design a solution to the problems.

Take a screenshot of each of your solutions and save each screenshot.  Create a zip archive containing all of your screenshots and submit the zip archive to blackboard as your solutions to these exercises.

------
To take a screenshot of a window:

(Mac) hold down **Cmd+Shift+4**

(Windows) hold **Alt+PrtSc**

------

**The solutions to these exercises must be submitted by the end of the day.**

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

![Example 1 Square]({{ "/gwu/sp19/cs1012/assets/exercises01/example01.png" | absolute_url }})

### Exercise 1 - Center the Square
The square in Example 1 is not centered in the middle of the canvas.  Using the statements described above, how can you draw the same square centered in the canvas?  The turtle should end up in the same corner of the square and with the same orientation as in Example 1.

Draw the square.  The result should look like the following image:

![Exercise 1 Square]({{ "/gwu/sp19/cs1012/assets/exercises01/exercise01.png" | absolute_url }})

Save a screenshot of your solution as ```exercise1.png```.

### Exercise 2 - Drawing a Triangle

Recall that the Pythagorean theorem is a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup>.  This mathematical theorem is useful whenever we need to compute the length of an unknown side for a right triangle because it defines the relationship between the length of the hypotenuse and the lengths of the sides for a right triangle.

> Of course Python supports the ability to compute powers and square roots; however, for now you will compute these values with a calculator.  We will learn in a future lesson how to instruct Python to make these calculations.

Draw a right triangle with sides of length 100.  Use the Pythagorean theorem to calculate the length of the hypotenuse and draw a line connecting the ends of the sides.  Your turtle must end with the same position and orientation and your triangle must look like the following image:

![Exercise 2 Triangle]({{ "/gwu/sp19/cs1012/assets/exercises01/exercise02.png" | absolute_url }})

Save a screenshot of your solution as ```exercise2.png```.

### Example 2 - Drawing a Circle
While is is possible to draw a circle using a sequence of primitive moving and turning statements, such a program would be cumbersome to write.  Fortunately, there is a built in `circle` that we can use to control the turtle.

We can use the following Python code to draw a circle from the turtle's starting position with a diameter of 100 units:
{% highlight python %}
>>> from turtle import *
>>> circle(50)
{% endhighlight %}

Note that number supplied to the circle is half the diameter which is by definition the radius of the circle.

> The ```circle``` command assumes that the center of the circle is located to the left of the turtle at a distance equal to the radius.

The turtle will draw a circle similar to the following image:

![Example 2 Circle]({{ "/gwu/sp19/cs1012/assets/exercises01/example02.png" | absolute_url }})

### Exercise 3 - Circumscribe a Centered Diamond
In this exercise, you will draw a diamond that has a circle drawn around it.  The diamond should be centered in the canvas and should have the same dimensions as the square in Exercise 1.  This diamond is simply a square rotated by 45 degrees.  The turtle should end up at the bottom-most point of the diamond and rotated toward the right hand side of the canvas.

> The length of each side of the diamond is 100 units.  You will need to use the Pythagorean theorem to compute the radius of the circle.  

Draw the circumscribed diamond.  The result should look like the following image:

![Exercise 3 Diamond]({{ "/gwu/sp19/cs1012/assets/exercises01/exercise03.png" | absolute_url }})

Save a screenshot of your solution as ```exercise3.png```.

## Writing a Python Script
While we can accomplish a lot using the Interactive Python Prompt, writing a program entirely at the prompt poses a number of problems:
* Mistakes are costly.  If you make a mistake, it can be difficult to correct without starting over.
* To run the same program again, you have to rewrite the program which opens up the possibility of making a new mistake each time you write the program.

Instead of writing code at the Interactive Python Prompt, we can instead write a Python program, typically called a script and run the script at a shell prompt or we can write a script in an Interactive Development Environment (IDE) and run the script inside the environment.  

> A Python script must have the file extension `.py`.

### Interactive Development Environment
An Interactive Development Environment (IDE) is a program that provides a number of tools for developers.  An IDE is usually focused around a text editor that allows a programmer to easily write new scripts and to load scripts from disk for editing.  An IDE also typically provides other tools such as a way to run a script, to view output, and a terminal in which the programmer can interact with a running script.  Anaconda provides access to a number of IDEs of varying quality.

For this class, we will use *spyder* as our preferred IDE which is available through Anaconda and is already available on all lab computers.

#### Launching spyder
Follow the instructions for your operating system.
##### Windows
> These instructions will launch spyder on the lab computers without any additional configuration.
Open the Anaconda Prompt from the *Start Menu*.  In the Anaconda Prompt, enter the following command:
```
$ spyder
```
This should launch spyder

> Remember, don't type the ```$```.  The ```$``` symbol is to remind you that you need to type the command in the Anaconda Prompt.

##### MacOSX
> These instructions should work on your laptop.  If they do not, use your lab computer and follow the Windows instructions above; however, notify your instructor.
Open the Terminal.  Enter the following command in the terminal:
```
$ spyder
```
This should launch spyder

> Remember, don't type the ```$```.  The ```$``` symbol is to remind you that you need to type the command in the Terminal prompt.

### Intro to spyder
The spyder IDE should look like the following image:

![spyder IDE]({{ "/gwu/sp19/cs1012/assets/exercises01/spyder.png" | absolute_url }})

The left hand pane contains the text editor and the bottom right hand pane contains a Python console.  You can type a Python script into the text editor and save it using the controls along the top.  You can run the script by clicking the *PLAY* button along the toolbar at the top and interact with the program in the Python console.  There are other features that we might use later, but these basic elements are all you need to write and run a Python program in spyder.

> Save your files in a consistent directory that you can easily find later.  I suggest you create a folder on your desktop named ```cs1012```.  Each class, create a new folder inside the ```cs1012``` folder using either the class date, the day's topic, or the exercise or homework identifier as the folder name.  Save all your work in the appropriate folder.  When you submit your work, you can simply zip that work folder and submit the zip file.

### spyder and the turtle
The window in which the turtle draws can be a bit cantankerous.  There are two issues that can regularly come up when using the ```turtle``` module in spyder.
1. The window may be difficult to close
2. When running a ```turtle``` program a second time, the system may generate an error and fail.

The following guidelines will help resolve these two issues.

#### Making the ```turtle``` window more friendly
At the end of a ```turtle``` program, call the ```done()``` command.

The reason the ```turtle``` window does not wish to close is the window is waiting for more instructions.  If the ```done()``` command is the last instruction in the script, the window is notified that there will be no more instructions.  As a result, it will be easier to close.

The following script shows how to use ```done()```:
```python
from turtle import *

forward(100)
right(90)
forward(100)

done()       # this needs to be the last instruction in every turtle program
```

#### Preventing the second run error
This error is also obscure and is caused by a similar reason as the previous.  You may not have the bug on your system; however, the solution provided here should prevent the bug if your program is run on another system.

> Bugs can be introduced in different versions of software.  This issue appears to be resolved in Python 3.6 and later.  It is important to keep your software updated for this reason.

The bug is primarily due to the ```turtle``` window not being fully unloaded when it is run a first time.  When ```turtle``` is run a second time, this causes an error in the window which then fully unloads.  Practically, this means that every other time you try to run a ```turtle``` program, it errors which can mislead a programmer into believing that the error is with the program and not with the environment.

Fortunately, the solution is rather simple...  instead of using just the following statement at the beginning of a turtle script:
```python
from turtle import *
```

Use the following two statements together:
```python
from turtle import *
TurtleScreen._RUNNING = True
```
