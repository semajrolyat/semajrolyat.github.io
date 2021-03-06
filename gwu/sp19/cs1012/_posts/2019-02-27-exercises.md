---
layout: post
title:  "Exercises"
date:   2019-02-27 00:00:00 -0400
schedule:   2019-02-27 00:00:00 -0400
categories: [GWU]
docclass: "exercises"
gwclass: "cs1012"
term: "sp19"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Exercises 5

### Due Date
**The solutions to these exercises must be submitted by the end of the day.**

### Instructions

Before trying to write any code, plan out how you will to use the primitives defined here to draw the solution.  If you don't plan, you may make a mistake and have to start over.  It's a good idea to have pen and paper available.

You are allowed to collaborate with your neighbor on these exercises.  Each of you must complete the programming tasks individually; however, you are encouraged to discuss and work together to design a solution to the problems.

Before beginning, make sure to create a new folder named ```exercises05``` in your class folder.

Create a .zip archive containing all of your code files and any written solutions and submit the .zip archive to blackboard as your solutions to these exercises.
You **MUST** include comments in your code.  If your code contains no comments, it is incomplete and will not receive credit.  Comments are as important to your code as the code itself.

### Warning
If you make a mistake with the design of a ```while``` loop, it is very easy to end up in an infinite loop.  If this happens, your program will run forever.  It can be difficult to determine whether your program is looping in this way.

It is a good idea to include a print statement inside a ```while``` loop when initially designing a program so that you can see that it is not making progress.  We might call these debugging statements.  I'll note in these exercises where you might want to include a debugging statements.  When you have fully debugged your program, comment out any debugging statements so that they are not processed by the actual program.

If your program enters an infinite loop, you must interrupt the program so that it does not continue to run forever.  To interrupt a program in spyder, click in the interactive terminal (bottom right) and use the key combination ```Ctrl-C``` on Windows or Linux or use the key combination ```Cmd-C``` on OSX.  These key combinations send a command to your operating system to force the current program to quit in a terminal window.

#### Exercise 1 - Boolean Logic
Create a text file named ```exercise1.txt```.

This exercise is NOT a programming exercise but is instead a chance to practice using creating boolean expressions.  In ```exercise1.txt```, write boolean expressions using Python syntax that meet the criteria described in the questions below.  You are encouraged to use truth tables to determine the correct operators.

1. Write a boolean expression that evaluates to ```True``` if *all* of the following conditions are ```True``` and otherwise evaluates to ```False```.
  * ```x``` is positive, ```y``` is between ```1``` and ```10``` inclusively.
2. Write a boolean expression that evaluates to ```True``` if *any* of the following conditions are ```True``` and otherwise evaluates to ```False```.
  * ```n``` is non-zero, ```m``` is negative.
3. Write a boolean expression that evaluates to ```False``` if *all* the following conditions are ```True``` and otherwise evaluate to ```True```:
  * ```p``` is ```True```, ```q``` is ```False```.
4. Write a boolean expression that evaluates to ```False``` if *any* the following conditions are ```True``` and otherwise evaluate to ```True```:
  * ```a``` is even, ```b``` is odd.

Submit ```exercise1.txt```

#### Exercise 2 - Computing Leap Years
Create a file named ```exercise2.py```.

3 criteria must be taken into account to identify leap years:
* The year is evenly divisible by 4;
* If the year can be evenly divided by 100, it is NOT a leap year, unless;
* The year is also evenly divisible by 400. Then it is a leap year.

Write a script based on the above algorithm.  Prompt the user to input a year, compute whether the input year is a leap year or not using the above algorithm, and print a message declaring whether the input year is a leap year or not.  Your program's behavior should reflect the same input and output for the following examples:   

**Example 1**
```
Input a year: 1900
1900 is not a leap year
```
1900 is evenly divisible by 4 and 100 but not by 400, so 1900 is not a leap year

**Example 2**
```
Input a year: 2000
2000 is a leap year
```
2000 is evenly divisible by 4, 100, and 400, so 2000 is a leap year

**Example 3**
```
Input a year: 2001
2001 is not a leap year
```
2001 is not evenly divisible by 4, so 2001 is not a leap year

**Example 4**
```
Input a year: 2016
2016 is a leap year
```
2016 is evenly divisible by 4 but is not evenly divisible by 100, so 2016 is a leap year

**Example 5**
```
Input a year: 2018
2018 is a leap year
```
2018 is not evenly divisible by 4, so 2018 is not a leap year

Submit ```exercise2.py```

#### Exercise 3 - Adding Machine
Create a file named ```exercise3.py```.

Old adding machines would take in a sequence of numbers followed by the Enter key and then keep a running total of the sum of the values entered.  In this exercise, we will model this simple concept using Python.

Prompt the user to enter an integer.  If the user enters an integer, add that value to a running total in your program.  If the user presses the Enter key without entering an integer, then the program should print the total and exit.

For example, the following output illustrates the behavior of the program:
```
Enter an integer or press Enter to see the sum? 1
Enter an integer or press Enter to see the sum? 2
Enter an integer or press Enter to see the sum? 3
Enter an integer or press Enter to see the sum?
The sum of all values is 6
```

**Hint**
This is clearly an iterative process; however, you do not know in advance how many times the user will enter a value, so this program should be structured around a ```while``` loop.  There are several ways to express this loop, but the most simple would be to use an "infinite while" loop with a conditional that breaks the loop if the desired break condition arises.   

Submit ```exercise3.py```
