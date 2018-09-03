---
layout: post
title:  "Variables and Expressions"
date:   2018-09-04 00:00:00 -0400
schedule:   2018-09-04 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
reading: "HtTLaCS 2.2, 2.3, 2.8, & 2.9"
exercises: "/gwu/fa18/cs1012/2018/09/04/exercises.html"
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

## Introduction
> Much of what we discuss today will be placed in the context of mathematics.  If we only use mathematics then our programs will be nothing more than glorified calculators; however, we are focuing on mathematics now because it is hopefully a context that we all share.  We will expand beyond mathematical concepts very soon.

So far, we have issued Python Turtle commands using fixed numbers.  For example, the following python script draws a square 100 units on a side:
```python
from turtle import *
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
done()
```
Any time you write a number (or a _string_) into a program, that value is called a _literal_ and is sometimes described as being a value that is _hardcoded_ into the program.  In the above example, we use the literal 100 for the length of a side and the literal 90 for the angle of the turn.
> We will define what the term "string" means later.  The term "hardcoded" implies that the value cannot be changed once the program is started.

We can accomplish a lot using literals and they are necessary; however, if we only use literals, it will be difficult to modify the program later to draw a square of any size other than 100 units.

> Programmers strive to reuse software as much as possible.  Generalization promotes code reuse, reduces the size of code, and is a fundamental principle of programming. Less code is usually better because there is less opportunity to make a mistake.

Instead of hardcoding 100 as the length of a side, we can use a _variable_ insted.  Compare the following python script to the preceding python script:

```python
from turtle import *
length = 100
forward(length)
left(90)
forward(length)
left(90)
forward(length)
left(90)
forward(length)
done()
```

**Question**: Do these two python scripts produce drawings that are equivalent?

## Variables

### Variable Names

### Variable Assignment
The assignment operator ```=``` directs Python to assign the value on the right side of the assignment operator to the variable on the left side of the assignment operator.  For example:
```python
# Assign 5 to the variable x
x = 5
```
> You may be inclined to read ```=``` as 'equal to', but it is better to read it as 'is assigned'.  For the statement ```x = 5```, read it as 'x is assigned 5'.

The symbol on the left of the assignment operator must be a legal variable name and the expression to the right of the assignment operator must be a legal expression.  For example:
```python
# These are legal assignments
x = 5                   # legal - assign literal 5 to variable x
y = x                   # legal - assign value stored in x to y
s1 = "Hello there!"      # legal - assign literal string to variable s
# These are not legal assignments
5 = a                   # illegal - cannot assign a to 5
s2 = Hello there!        # illegal - Hello There! is not a legal expression
```

> The assignment of ```s1``` in the above code is legal because the value being assigned is inside double quotes ```"Hello there!"```.  A value inside quotes is called a _string_.  We will talk more about strings later.  The assignment of ```s2``` is not legal because the expression to the right of the assignment operator is not a valid expression.

## Expressions
In Python we use _infix notation_ to join together _operands_ using _operators_ to form an _expression_.  Infix notation means that binary operators appear between two operands.  Operands are values to be operated on and operators describe the operations to be performed.  An expression may be formed by combining a number of operands and operators and expressions may appear in different contexts.  These are some examples of legal expressions:
```python
x = 3
y = 0.5 * x + 1
```
**Question**: How many expressions are there in the above example?

### Binary Mathematical Operators
In infix notation, a binary operator appears between two operands.  In terms of mathematics, ```a + b```, ```a * b```, ```a / b``` are all examples of binary operators.

The binary mathematical operators are:
* ```a + b``` : Addition
* ```a - b``` : Subtraction
* ```a * b``` : Multiplication
* ```a / b``` : Floating point division
* ```a // b``` : Integer division
* ```a % b``` : Remainder (or modulus) of integer division
* ```a ** b``` : Raise ```a``` to the power ```b```


### Unary Mathematical Operators
In terms of mathematics, negation, _i.e._ ```-x```, is an example of a unary operator.  In infix notation, a unary operator precedes the operand.

### Comparison Operators
We can also form expressions using comparison operations.

**Question**: What type of answer does a comparison produce?  For example, what possible values could be assigned to ```r``` by the expression ```r = a > b```?

The comparison operators are the following binary operators:
* ```a == b``` : Is ```a``` equal to ```b```?
* ```a != b``` : Is ```a``` not equal to ```b```?
* ```a > b``` : Is ```a``` greater than ```b```?
* ```a >= b``` : Is ```a``` greater than or equal to ```b```?
* ```a < b``` : Is ```a``` less than ```b```?
* ```a <= b``` : Is ```a``` less than or equal to ```b```?

> The comparison operator ```==``` is different than the assignment operator ```=```.  It is very common to confuse the assignment operator for the comparison operator.  Make sure to be very careful to use the correct operator for the correct context.  The computer will do only what you tell it.

### Operator Precedence
[Python Reference](https://docs.python.org/3/reference/expressions.html#operator-precedence)

Each operator has a precedence which is the same as that used in mathematics.
1. Grouping operators ```(``` and ```)```
2. Binary math operator ```**```
3. Unary math operator ```-```
4. Binary math operators ```*```, ```/```, ```//```, and ```%```
5. Binary math operators ```+``` and ```-```
6. Binary comparison operators ```<```, ```<=```, ```>```, ```>=```, ```!=```, and ```==```

This list will grow as we introduce other types of operators.

## Exercises


## Reflection
