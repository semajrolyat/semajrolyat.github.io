---
layout: post
title:  "Exercises"
date:   2018-09-06 00:00:00 -0400
schedule:   2018-09-06 00:00:00 -0400
categories: [GWU]
docclass: "exercises"
gwclass: "cs1012"
term: "fa18"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Interactive Development Environment
An Interactive Development Environment (IDE) is a program that provides a number of tools for developers.  An IDE is usually focused around a text editor that allows a programmer to easily write new scripts and to load scripts from disk for editing.  An IDE also typically provides other tools such as a way to run a script, to view output, and a terminal in which the programmer can interact with a running script.  Anaconda provides access to a number of IDEs of varying quality.

For this class, we will use *spyder* as our preferred IDE which is available through Anaconda and is already available on all lab computers.

### Launching spyder
Follow the instructions for your operating system.
#### Windows
> These instructions will launch spyder on the lab computers without any additional configuration.
Open the Anaconda Prompt from the *Start Menu*.  In the Anaconda Prompt, enter the following command:
```
$ spyder
```
This should launch spyder

> Remember, don't type the ```$```.  The ```$``` symbol is to remind you that you need to type the command in the Anaconda Prompt.

#### MacOSX
> These instructions should work on your laptop.  If they do not, use your lab computer and follow the Windows instructions above; however, notify your instructor.
Open the Terminal.  Enter the following command in the terminal:
```
$ spyder
```
This should launch spyder

> Remember, don't type the ```$```.  The ```$``` symbol is to remind you that you need to type the command in the Terminal prompt.

### Intro to spyder
The spyder IDE should look like the following image:

![spyder IDE]({{ "/gwu/fa18/cs1012/assets/09_06_2018/spyder.png" | absolute_url }})

The left hand pane contains the text editor and the bottom right hand pane contains a Python console.  You can type a Python script into the text editor and save it using the controls along the top.  You can run the script by clicking the *PLAY* button along the toolbar at the top and interact with the program in the Python console.  There are other features that we might use later, but these basic elements are all you need to write and run a Python program in spyder.

> Save your files in a consistent directory that you can easily find later.  I suggest you create a folder on your desktop named ```cs1012```.  Each class, create a new folder inside the ```cs1012``` folder using either the class date or the day's topic as the folder name.  Save all your exercises for the day in the appropriate folder.  When you submit your work, you can simply zip the folder of the day and submit the zip file.

## Printing
The prototypical first program in most languages is to print "Hello World!" to the console.  This code will accomplish the goal:
```python
print("Hello World!")
```
![IDLE Hello]({{ "/gwu/fa18/cs1012/assets/09_04_2018/idle-hello.png" | absolute_url }})

## Computing a Square Root
So far, we have been importing turtle commands using the following statement:
```python
from turtle import *
```
You were required to calculate the square root by hand in order to use the pythogorean theorum in the previous set of exercises.  Of course a computer is capable of computing a square root and we can gain access to the square root command using the same approach that allowed access to the turtle commands.  If you add the following line at the beginning of a Python script, you can use the built in square root command:
```python
from math import *
```
If you have the above line at the beginning of your script, you can compute a square root using the following command:
```python
a = 9
b = sqrt(a)
```
> We have not discussed the concept of a function in depth yet and I have used the term occasionally so far; however, the turtle "commands", the print "command", and the sqrt "command" are all functions built into Python.  We will discuss functions more in depth in a future class including how you can write functions of your own.

## Exercises
Each exercise describes exactly what you must submit.  **DO NOT** submit individual files.  Save everything described into one folder, zip that folder, and submit the zip containing all files.

In your ```cs1012``` folder create a subfolder named ```09_06_2018```.  Save all of your work from today in this folder.  When you complete your work, zip the ```09_06_2018``` folder and submit it to blackboard.  These exercises are due before the next class.

You **MUST** include comments in your code.  If your code contains no comments, it is incomplete and will not receive credit.  Comments are as important to your code as the code itself.

#### Exercise 1 - Hello World!
Write a "Hello World" script using spyder.  Save this script as ```hello.py```.  Run the script and verify the expected output is produced in spyder's Python console.

Submit ```hello.py```.

> This exercise will make sure you can run a very simple script using spyder and will be your first practice using strings and printing.

#### Exercise 2 - Turtle with Variables and User Input
Write a script that implements the circumscribed diamond from the introductory [Exercise 2]({{ "/gwu/fa18/cs1012/2018/08/28/exercises.html" | absolute_url }}); however, you will take user input to determine the radius of the circle.  In addition, you need to center this drawing, and you will also need to use the ```sqrt``` function to compute the length of the diamond's edge.

Your input prompt should read "Enter the radius of the circle: ".  Use the user input value to compute the distance necessary to center the drawing and for each command necessary to complete the drawing.  Save your script as ```diamond.py```.

Test your program by running your script twice.  Enter a value of 50 at the prompt on the first run and enter a value of 100 at the prompt on the second run.  Take a screen shot of each drawing that is produced from these runs.  Save the screenshot of the first drawing (radius 50) as ```diamond50.png``` and save the screenshot of the second drawing (radius 100) as ```diamond100.png```.

Submit both ```diamond.py```, ```diamond50.png```, and ```diamond100.png```.

> This exercise will allow you to work with expressions, variables, types, user input, and the mathematical function ```sqrt```.

#### Exercise 3 - Quadratic Formula
Recall that a Quadratic Equation has the form:

![Quadratic Equation]({{ "/gwu/fa18/cs1012/assets/09_06_2018/quadratic-eq.png" | absolute_url }})

The Quadratic Formula allows us to compute the roots of a Quadratic Equation and is defined by the formula:

![Quadratic Formula]({{ "/gwu/fa18/cs1012/assets/09_06_2018/quadratic-formula.png" | absolute_url }})

Write a script that takes the user inputs ```a```, ```b```, and ```c``` for the Quadratic Equation.  Compute the two roots of the Quadratic using the Quadratic Formula, and print the roots to the console.  Save your script as ```quadratic.py```

We cannot successfully compute roots for all Quadratics because some of the roots will be imaginary.  We will only test our scripts using a narrow set of coefficients that we can compute so that we do not generate any errors.  You must take user input using the ```input``` function, but you must test your scripts with the following inputs and outputs:

```
# input
a = 1
b = 0
c = -1
# output
root = 1
root = -1
```

```
# input
a = 4
b = -3
c = -2
# output
root = 1.175390529679106
root = -0.42539052967910607
```

```
# input
a = 2
b = -1
c = -2
# output
root = 1.2807764064044151
root = -0.7807764064044151
```

Submit ```quadratic.py```.

> This exercise will allow you to work with expressions, variables, types, user input, the mathematical function ```sqrt```, and operator precedence.
