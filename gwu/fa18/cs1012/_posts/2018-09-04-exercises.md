---
layout: post
title:  "Exercises"
date:   2018-09-04 00:00:00 -0400
schedule:   2018-09-04 00:00:00 -0400
categories: [GWU]
docclass: "exercises"
gwclass: "cs1012"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Interactive Development and Learning Environment (IDLE)
As indicated in the previous class, it is beneficial to write a Python program in a script rather than in the interactive console.  In order to write a script, we will need to use a text editor.  There are a broad array of editors available that will make programming much easier; however, due to the differences between each student's system, we will use the built in Python IDLE program as our editor of choice.  To run idle, open the interactive python shell and type the following two commands:
```
>>> import idlelib.PyShell
>>> idlelib.PyShell.main()
```
This will open a window that looks like this:

![IDLE Shell]({{ "/gwu/fa18/cs1012/assets/09_04_2018/idle-shell.png" | absolute_url }})

This window functions the same as the python interactive shell except it is inside a window that includes a menu at the top.  On the menu, the ```File | New File``` option will open a new editor window in which you can write a script.

![IDLE File]({{ "/gwu/fa18/cs1012/assets/09_04_2018/idle-file.png" | absolute_url }})

You can run the script from the editor's ```Run | Run Module``` menu option; however, you must save the script first using the editor's ```File``` menu.

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
> We have not discussed the concept of a function yet and I have avoided the term so far; however, the turtle "commands", the print "command", and the sqrt "command" are all functions.  We will discuss functions more in depth in a future class.

# Exercises
Each exercise describes exactly what you must submit.  **DO NOT** submit individual files.  Save everything described into one folder, zip that folder, and submit the zip containing all files.

## Exercise 1 - Hello World!
Write a "Hello World" script using IDLE.  Save this script as ```hello.py```.  Run the script.  Take a screenshot of the output from ```hello.py``` in IDLE shell and save the screenshot as ```hello.png```.  Submit both ```hello.py``` and ```hello.png```.

## Exercise 2 - Turtle with Variables
Write a script that implements the circumscribed diamond from the introductory [Exercise 2]({{ "/gwu/fa18/cs1012/2018/08/28/exercises.html" | absolute_url }}) again using the variable ```r``` for the radius of the circle.  Use the ```sqrt``` function to compute the length of a side of the diamond based on the value assigned to ```r```.  Save the script as ```cdiamond.py``` and run the script.  Save a screen shot of the diamond as ```cdiamond.png```.  Submit both ```cdiamond.py``` and ```cdiamond.png```.
