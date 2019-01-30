---
layout: post
title:  "Exercises"
date:   2019-01-30 00:00:00 -0400
schedule:   2019-01-30 00:00:00 -0400
categories: [GWU]
docclass: "exercises"
gwclass: "cs1012"
term: "sp19"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Exercises 2

### Due Date
**The solutions to these exercises must be submitted by the end of the day.**

### Instructions

Before trying to write any code, plan out how you will to use the primitives defined here to draw the solution.  If you don't plan, you may make a mistake and have to start over.  It's a good idea to have pen and paper available.

You are allowed to collaborate with your neighbor on these exercises.  Each of you must complete the programming tasks individually; however, you are encouraged to discuss and work together to design a solution to the problems.

Before beginning, make sure to create a new folder named ```exercises02``` in your class folder.

Create a .zip archive containing all of your code files and submit the .zip archive to blackboard as your solutions to these exercises.

### Output to a Terminal Window
We can output information into the terminal by using the ```print``` command.  ```print``` will write to the terminal any string information that appears inside the parentheses.  Multiple strings can be printed to the terminal (separated by a space) if each string is separated by a comma.  

For example, run the following code:
```python
print("Hello World")
```
You will see the follow output in the terminal:
```
Hello World
```

Also run the following code:
```python
print("Hello", "World")
```
You will see the follow output in the terminal:
```
Hello World
```

Note that the above print statements produce equivalent output in the terminal even though we printed one string in the first example and two separate strings in the second example.

We can also output the values stored in a variable using the ```print``` command.  For example, the following code prints the value of the variable ```x```:

```python
x = 100
print(x)
```

We can also combine a string with a variable using the earlier comma separation technique to create a more meaningful output:

```python
x = 100
print('x =', x)
```

The above example prints the following output to the terminal:
```
x = 100
```

We will discuss more about strings in future classes; however, this is a simple primer for using strings and printing to the terminal that you may find very useful for checking the value of a variable at a specific point in your program.  You can insert print statements at any point in the program and print the value of a variable at that point.  You can then compare the output between two or more points in a program to see whether the variable has the value that you expect it does.  This is one way to "debug" a program.

### Computing a Square Root
In previous exercises, we needed to compute a square root in order to apply the Pythagorean theorem.  In order to do so, we precomputed the square root by hand.  This is not always feasible; because we do not necessarily know the value in advance of running a program that requires a square root computation.

Of course Python has built in operations to compute mathematical operations such as square root.  These operations or "functions" are built into the ```math``` module.  We will talk more about the available Python mathematics functions and modules later; however, you may find it useful to use the square root operation sooner than later.

In order to gain access to the square root function, we will need to "import" the mathematics module into our program.  To do so, add the following statement at the beginning of any program where you need to use square root:
```python
import math
```
You will then have a function named ```math.sqrt``` available in your program that you can use to compute a square root.  For example:
```python
import math          # import the math module to access the sqrt function

x2 = 9
x = math.sqrt(x2)    # compute the square root of x2 and store in x     
print(x)
```
The above program produces the following output:
```
3.0
```

You will need to use the square root function in today's exercises.

### Exercise 1 - Day of the Week
> This exercise will allow you to work with expressions, variables, and integer division operators.

Create a script named ```exercise1.py```.

We can associate a number with the day of the week.  For example:

* Monday is the 1st day of the week so it is day 1
* Tuesday is the 2nd day of the week so it is day 2
* Sunday is the last day of the week so it is day 7

Write a program that computes the day of the week given a numerical representation of a day of the week and a number of days in the future.  Your program will also computes the number of weeks, months, and years that will be spanned by that number of days.  For example:

* Yesterday was Tuesday so it was day 2 of the week.  1 day from yesterday is Wednesday, so it is day 3 of the week and 0 weeks have passed.
* Today is Wednesday so it is day 3 of the week.  7 days from today will be another Wednesday so it will be day 3 of the week and 1 week will have passed.
* Tomorrow is Thursday so it will be day 4 of the week.  17 days from tomorrow will be Sunday so it will be day 7 of the week and two weeks will have passed.  

Your program must have a variable ```day0``` which will be a number ranging from 1 to 7, a variable ```days``` which will be the number days to count forward, ```dayn``` the number of the day it will be in ```days``` from ```day0```, and a variable ```weeks``` which you will compute as the number of weeks that will pass over the period of ```days```.  

You program must print the number of the initial day ```day0```, the number of days to pass ```days```, the number of the subsequent day ```dayn```, and the number of weeks ```weeks``` that will lapse over that time span using the following example as a model:
```
7 day(s) from day 3 will be day 3 which will span 1 week(s)
```

Run your program using the following examples and make sure that your program produces the expected output:
```
1 day(s) from day 2 will be day 3 which will span 0 week(s)
7 day(s) from day 3 will be day 3 which will span 1 week(s)
17 day(s) from day 4 will be day 7 which will span 2 week(s)
```

You will submit ```exercise1.py```.

### Exercise 2 - Circumscribe a Centered Diamond with Variables
> This exercise will allow you to work with expressions, variables, and the mathematical function ```sqrt```.

Create a script named ```exercise2.py```.

Write a script that implements the circumscribed diamond from the introductory [Exercise 2]({{ "/gwu/sp19/cs1012/2019/01/23/exercises.html" | absolute_url }}) again; however, this time you will use the variable ```r``` for the radius of the circle.  Use the ```sqrt``` function to compute the length of a side of the diamond based on the value assigned to ```r```.  Save ```exercise2.py``` and run the script.

You will submit ```exercise2.py```.

#### Exercise 3 - Quadratic Formula
> This exercise will allow you to work with expressions, variables, the mathematical function ```sqrt```, and operator precedence.

Recall that a Quadratic Equation has the form:

![Quadratic Equation]({{ "/gwu/sp19/cs1012/assets/exercises02/quadratic-eq.png" | absolute_url }})

The Quadratic Formula allows us to compute the roots of a Quadratic Equation and is defined by the formula:

![Quadratic Formula]({{ "/gwu/sp19/cs1012/assets/exercises02/quadratic-formula.png" | absolute_url }})

Write a script that contains the variables ```a```, ```b```, and ```c``` for the Quadratic Equation.  Compute the two roots of the Quadratic Equation using the Quadratic Formula, and print the roots to the console.  Save your script as ```exercise3.py```

We cannot successfully compute roots for all Quadratic Equations because some of the roots will be imaginary.  We will only test our scripts using a narrow set of coefficients that we can compute so that we do not generate any errors.  Test your scripts with the following values of ```a```, ```b```, and ```c``` and make sure that your program prints the same output to the terminal (You must follow the same format indicated in the examples below meaning that you must print the same section headers and variables as shown):

```
Coefficients:
a = 1
b = 0
c = -1
Roots:
root = 1
root = -1
```

```
Coefficients:
a = 4
b = -3
c = -2
Roots:
root = 1.175390529679106
root = -0.42539052967910607
```

```
Coefficients:
a = 2
b = -1
c = -2
Roots:
root = 1.2807764064044151
root = -0.7807764064044151
```

You will submit ```exercise3.py```.
