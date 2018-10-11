---
layout: post
title:  "Variables and Expressions"
date:   2018-09-04 00:00:00 -0400
schedule:   2018-09-04 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
reading: "HtTLaCS 2.2-2.3 & 2.8-2.11"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Introduction
> Much of what we discuss today will be placed in the context of mathematics.  If we only use mathematics then our programs will be nothing more than glorified calculators; however, we are focuing on mathematics now because it is hopefully a context that we all share.  We will expand beyond mathematical concepts very soon.

## Literals
Any time you write a number (or a _**string**_) into a program, that value is called a _**literal**_ and is sometimes described as being a value that is _**hardcoded**_ into the program.  In the above example, we use the literal 100 for the length of a side and the literal 90 for the angle of the turn.
> We will define what the term "string" means later.  The term "hardcoded" implies that the value cannot be changed once the program is started.

We can accomplish a lot using literals and they are necessary; however, if we only use literals, it will be difficult to modify the program later to write code that can be reused in different contexts.

For example, in the previous class, we draw a square that had a hardcoded size of ```100```.  If we hardcode the size, we cannot reuse the same script to draw squares of other sizes.  We would like to write one script that can draw all squares rather than write a script for each and every square that we might draw.

> Programmers strive to reuse software as much as possible.  Generalization promotes code reuse, reduces the size of code, and is a fundamental principle of programming. Less code is usually better because there is less opportunity to make a mistake.

## Variables
A variable in programming is a way to attach a name to a value.  In Python, if we assign a variable using the assignment operator ```=```, we both define the name as a variable to Python and instruct Python assign it the value indicated.  The variable also has a "type" which we will talk about throughout the rest of the semester.

### Variable Names
Variables names must follow specific rules:

* There are keywords that have specific meaning to Python.  Variables can never have a name that matches a keyword.
* Variable names cannot include special characters, _i.e._ ```!```, ```@```, ```#```, ```$```, ```%```, etc., with one exception.  Variable names can include the underscore character ```_```.
* Variable names must begin with a letter or underscore ```_``` and may contain numbers.
* Variable names are case sensitive.  For example, ```MyVar``` is not the same name as ```myvar```.

#### Python Keywords
[Reserved Keyword Reference](https://docs.python.org/3/reference/lexical_analysis.html#keywords)

This is the list of reserved keywords in Python 3:
```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```
> We will discuss many of these keywords later.  For now, use this list as a reference for variable names that cannot be used.

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

> The assignment of ```s1``` in the above code is legal because the value being assigned is inside double quotes ```"Hello there!"```.  A value inside quotes is called a _**string**_.  We will talk more about strings later.  The assignment of ```s2``` is not legal because the expression to the right of the assignment operator is not a valid expression.

## Style
* Variables should be given meaningful names.  A meaningful name improves the readability of code.
* While many of the early examples in this course use single letter variable names  _i.e._ ```a```, ```b```, ```x```, ```y```, etc., these names are not generally meaningful unless they apply a known mathematical theorem.
* Comments and white space can improve the readability of code.  Comments provide meaningful information while whitespace can help group code.
* Comments are are ignored by the Python interpreter and begin with the ```#``` character.

## Expressions
In Python we use _**infix notation**_ to join together _**operands**_ using _**operators**_ to form an _**expression**_.  Infix notation means that binary operators appear between two operands.  Operands are values to be operated on and operators describe the operations to be performed.  An expression may be formed by combining a number of operands and operators and expressions may appear in different contexts.  These are some examples of legal expressions:
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

### Operator Precedence
[Operator Precedence Reference](https://docs.python.org/3/reference/expressions.html#operator-precedence)

Each operator has a precedence which is the same as that used in mathematics.
1. Grouping operators ```(``` and ```)```
2. Binary math operator ```**```
3. Unary math operator ```-```
4. Binary math operators ```*```, ```/```, ```//```, and ```%```
5. Binary math operators ```+``` and ```-```

> This list will grow as we introduce other types of operators.

## Application
So far, we have issued Python Turtle commands using fixed numbers.  For example, the following Python script draws a square 100 units on a side:
```python
from turtle import *

# Draw a square with sides equal to 100 units
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
done()
```
In the above example, we use the literal 100 for the length of a side and the literal 90 for the angle of the turn.

We can accomplish a lot using literals and they are necessary; however, if we only use literals, it will be difficult to modify the program later to draw a square of any size other than 100 units.

> Programmers strive to reuse software as much as possible.  Generalization promotes code reuse, reduces the size of code, and is a fundamental principle of programming. Less code is usually better because there is less opportunity to make a mistake.

Instead of hardcoding 100 as the length of a side, we can use a variable instead.  Compare the following Python script to the preceding Python script:

```python
from turtle import *
# Length of a side
x = 100

# Draw a square with sides equal to x units
forward(x)
left(90)
forward(x)
left(90)
forward(x)
left(90)
forward(x)
done()
```

**Question**: Do these two python scripts produce drawings that are equivalent?

Recall that we also created a centered square.  The following set of commands allowed us to first reposition the turtle before beginning to draw.

```python
from turtle import *
# Length of a side
x=100

# Center the square
penup()
right(90)
forward(x / 2)
left(90)
backward(x / 2)
pendown()

# Draw a square with sides equal to x units
forward(x)
left(90)
forward(x)
left(90)
forward(x)
left(90)
forward(x)
done()
```
Because the turtle begins at the center of the screen, the distance the turtle needs to move before we begin drawing is half the length of a side.  We can use an expression to compute this distance from ```x``` instead of hardcoding the literal ```50```.
