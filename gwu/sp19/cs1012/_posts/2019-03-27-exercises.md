---
layout: post
title:  "Exercises"
date:   2019-03-27 00:00:00 -0400
schedule:   2019-03-27 00:00:00 -0400
categories: [GWU]
docclass: "exercises"
gwclass: "cs1012"
term: "sp19"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Exercises 7

### Due Date
**The solutions to these exercises must be submitted by the end of the day.**

### Instructions

You are allowed to collaborate with your neighbor on these exercises.  Each of you must complete the programming tasks individually; however, you are encouraged to discuss and work together to design a solution to the problems.

Before beginning, make sure to create a new folder named ```exercises07``` in your class folder.

Create a .zip archive containing all of your code files and any written solutions and submit the .zip archive to blackboard as your solutions to these exercises.

You **MUST** include comments in your code.  For each function, you must also provide a block comment that precedes the function and describes every input to the function if it accepts any parameters, what the function does, and what the function returns if it returns a value.  If your code contains no comments, it is incomplete and will not receive credit.  Comments are as important to your code as the code itself.  You must include a comment in the header portion of the file that summarizes what the program does.  You must include comments inline with code to describe the steps in natural language.

#### Exercise 1 - Rolling a 2 dice
Create a file named ```exercise1.py```.

Write a script to simulate rolling 2 six-sided dice.  

Write two functions named ```rolldie``` and ```roll2dice```.  ```rolldie``` takes no parameters and returns a random value in the range from 1 to 6.  ```roll2dice``` takes no parameters and returns no values; however, ```roll2dice``` prints the outcome of rolling two individual dice with the following format:

```
<valueofdie1> <valueofdie2>
```

For example, if the values produced by rolling two dice is ```5``` and ```3```, ```roll2dice``` will print:

```
5 3
```

Your main program should test ```roll2dice``` by iterating 10 times and calling ```roll2dice``` each time.  Confirm that the outcome of each throw produces a pair of values with the total of each pair in the range of 2 to 12.

Submit ```exercise1.py```.

#### Exercise 2 - Generating Random Floating Point Numbers
Create a file named ```exercise2.py```.

Write a script that generates random floating point numbers between -100.0 and 100.0.  

Write a function named ```randomfloat``` that takes a range as two parameters.  The definition for this function should be:

```python
def randomfloat(low,high):
```

```randomfloat``` generates a floating point value in the range of [low, high) and returns the generated value.  Your main program will iterate a hundred times, and each iteration, it will call ```randomfloat``` to generate a random number in the range of [-100.0,100.0).

Verify that each value produced by ```randomfloat``` is within the prescribed interval by comparing the value returned to the interval.  If the value is within the range print out the value.  If the value is not in the range, print out a message that indicates that the value generated is not in the range, print the range, and print the value that was generated.

Submit ```exercise2.py```.

#### Exercise 3 - Remove all instances of a character from a string
Create a file named ```exercise3.py```.

In this exercise, you will write a function that removes all instances of a character from a string and returns the resulting string.

Your function must have the following definition where ```s``` is the string to remove characters from and ```c``` is the character to remove from ```s```, and your function must return the string without any instances of ```c```:
```python
def trimchar(s, c):
```

Test your function using the following main program:

```python
print(trimchar('Hello World!','l'))
print(trimchar('Introduction to programming with python','o'))
print(trimchar('HtTLaCS is short for "How to Think Like a Computer Scientist"','T'))
```

Your program should produce the following output:
```
Heo Word!
Intrductin t prgramming with pythn
HtLaCS is short for "How to hink Like a Computer Scientist"
```

Submit ```exercise3.py```.
