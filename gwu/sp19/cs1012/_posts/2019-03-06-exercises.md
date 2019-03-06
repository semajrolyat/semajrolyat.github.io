---
layout: post
title:  "Exercises"
date:   2018-03-06 00:00:00 -0400
schedule:   2018-03-06 00:00:00 -0400
categories: [GWU]
docclass: "exercises"
gwclass: "cs1012"
term: "sp19"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Exercises 6

### Due Date
**The solutions to these exercises must be submitted by the end of the day.**

### Instructions

Before trying to write any code, plan out how you will to use the primitives defined here to draw the solution.  If you don't plan, you may make a mistake and have to start over.  It's a good idea to have pen and paper available.

You are allowed to collaborate with your neighbor on these exercises.  Each of you must complete the programming tasks individually; however, you are encouraged to discuss and work together to design a solution to the problems.

Before beginning, make sure to create a new folder named ```exercises06``` in your class folder.

Create a .zip archive containing all of your code files and any written solutions and submit the .zip archive to blackboard as your solutions to these exercises.

You **MUST** include comments in your code.  For each function, you must also provide a block comment that precedes the function and describes every input to the function if it accepts any parameters, what the function does, and what the function returns if it returns a value.  If your code contains no comments, it is incomplete and will not receive credit.  Comments are as important to your code as the code itself.  You must include a comment in the header portion of the file that summarizes what the program does.  You must include comments inline with code to describe the steps in natural language.


#### Exercise 1 - Summation Function
Create a file named ```exercise1.py```.

Write a function with the definition ```sum_to(n)``` that returns the sum of all positive integers up to and including ```n```.

Write a main program that calls ```sum_to(n)``` several times.  Your main program should look like the following:
```python
print(sum_to(10))
print(sum_to(50))
print(sum_to(100))
```
The output from this script should be:
```
55
1275
5050
```

Submit ```exercise1.py```.

> Other than writing the function and running it for a number of test cases, how can we know what the output should be?  We have been providing specific test cases in this class; however, one of the largest challenges in programming is validating that a program is correct.  The most dangerous program is one that generates an answer.   

#### Exercise 2 - Regular Polygon Function
Create a file named ```exercise2.py```.

In [Homework 4]({{ "/gwu/sp19/cs1012/2019/02/13/homework.html" | absolute_url }}), we drew a hexagon which is a regular polygon with six sides.  Ideally, we would have used a function to draw the hexagon because it would have been easy to reuse.  Recall that one of our principles of programming is generalization to maximize reusability.  The generalization of a drawing function for a hexagon would be a drawing function for a regular polygon.  

In this exercise, you will implement a function to do draw a regular polygon.  This function should have the following declaration:

```python
def polygon(sides,length):
```

Given the above declaration, this function should draw a regular polygon where the ```sides``` parameter specifies the number of sides for the polygon and ```length``` specifies the length of a single side.

In the main body of the script, use the following code to draw three polygons on the screen:
```python
polygon(3,100)
polygon(6,50)
polygon(8,25)
```

The output of this program should look like the following image.

![Exercise 2 Output]({{ "/gwu/sp19/cs1012/assets/exercises06/exercise2.png" | absolute_url }})

Submit ```exercise2.py```.

#### Exercise 3 - Inset Squares
Create a file named ```exercise3.py```.

Write a program to draw ten squares inset into one another.

Assume that the length of a side for the innermost square is 20 units and each successive square is 20 units larger than the previous square.  This script should center the squares.  The output of this program should look like the following image.

![Exercise 3 Output]({{ "/gwu/sp19/cs1012/assets/exercises06/exercise3.png" | absolute_url }})

Submit ```exercise3.py```.

>Hint: You will probably want a function to draw a square and a function to reposition the turtle without drawing.
