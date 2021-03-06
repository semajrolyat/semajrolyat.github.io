---
layout: post
title:  "Exercises"
date:   2019-02-13 00:00:00 -0400
schedule:   2019-02-13 00:00:00 -0400
categories: [GWU]
docclass: "exercises"
gwclass: "cs1012"
term: "sp19"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Exercises 4

### Due Date
**The solutions to these exercises must be submitted by the end of the day.**

### Instructions

Before trying to write any code, plan out how you will to use the primitives defined here to draw the solution.  If you don't plan, you may make a mistake and have to start over.  It's a good idea to have pen and paper available.

You are allowed to collaborate with your neighbor on these exercises.  Each of you must complete the programming tasks individually; however, you are encouraged to discuss and work together to design a solution to the problems.

Before beginning, make sure to create a new folder named ```exercises04``` in your class folder.

Create a .zip archive containing all of your code files and submit the .zip archive to blackboard as your solutions to these exercises.

### Exercise 1 - Days of the Week
> This exercise will allow you to work with input, strings, and formatted output.

Create a script named ```exercise1.py```.

Write a program that iterates using a ```for``` loop which prints the number indicating the day of the week and the corresponding name of the day.

Create a list composed of the strings ```"Monday"```, ```"Tuesday"```, ```"Wednesday"```, ```"Thursday"```, ```"Friday"```, ```"Saturday"```, and ```"Sunday",```.  Each iteration through the loop, print out a number indicating the numeric day of the week and the name of the day.  For example, your program should produce the following output:

```
Day 1 of the week is Monday
Day 2 of the week is Tuesday
Day 3 of the week is Wednesday
Day 4 of the week is Thursday
Day 5 of the week is Friday
Day 6 of the week is Saturday
Day 7 of the week is Sunday
```

You will submit ```exercise1.py```.

### Exercise 2 - Multiplication Table

Create a script named ```exercise2.py```.

In this exercise, you will use nested ```for``` loops and string concatenation to compute the multiplication table up to and including ```10```.  

> A "nested" loop is a loop inside a loop.

A multiplication table includes rows and columns.  Each cell in the table represents the product of the current row factor and the current column factor.  You may print only the products for your table and do not have to print the factors as the headings of the rows and columns.

Each pass through the "inner" loop, compute the product between the current row and column factors and concatenate the product into a string representing the current row.  Once all products for a row have been computed, print the row to the console.

Formatting a string containing a set of numbers as a consistently organized table can be a little difficult.  Each number may have a different length, so columns may not line up.  To simplify the formatting and produce consistent tables, insert a tab character between each product while building the string for a row.  

>Recall that the ```\t``` character combination is interpreted as the tab character by Python.   

Your program should produce the following output:
```
1       2       3       4       5       6       7       8       9       10      
2       4       6       8       10      12      14      16      18      20      
3       6       9       12      15      18      21      24      27      30      
4       8       12      16      20      24      28      32      36      40      
5       10      15      20      25      30      35      40      45      50      
6       12      18      24      30      36      42      48      54      60      
7       14      21      28      35      42      49      56      63      70      
8       16      24      32      40      48      56      64      72      80      
9       18      27      36      45      54      63      72      81      90      
10      20      30      40      50      60      70      80      90      100     
```

You will submit ```exercise2.py```.

#### Exercise 3 - Sum All Positive, Even Integers Less Than 100

Create a script named ```exercise3.py```.

Write a script that computes the sum of all positive even integers up to but not including 100 and prints the total sum after the computation finishes.  You must use a ```for``` loop with the ```range``` function to perform this computation.  

Your program should produce the following output:
```
2450
```

You will submit ```exercise3.py```.
