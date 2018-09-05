---
layout: post
title:  "Types"
date:   2018-09-06 00:00:00 -0400
schedule:   2018-09-06 00:00:00 -0400
categories: [preview]
docclass: "discussion"
gwclass: "cs1012"
reading: "HtTLaCS 2.4-2.7"
exercises: "/gwu/fa18/cs1012/2018/09/06/exercises.html"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Types
I our previous discussions, we have established that values whether literals or variables have a _type_.  In Python, every value is treated as an _object_.  We will

Every value in Python has a type or _data type_ associated with it.  Some values are represented as _primitive_ data types such as integers or floating-point
or string or ```string```.

```int``` is Python shorthand for integer.  The ```int``` data type maps generally to the [Set of Integers](https://en.wikipedia.org/wiki/Integer); however, due to the natural limits imposed by computer hardware, not all integers can be represented.

```float``` is Python shorthand for floating-point.  The ```float``` data type maps generally to the [Set of Real Numbers](https://en.wikipedia.org/wiki/Real_number); however, due to the natural limits by computer hardware, not all real numbers can be represented.  And due to the way computers represent these numbers, there is some inherent inaccuracy that will introduce some error into floating point calculations.

> The error in floating point calculations is very small, but it exists.  For the most part, this error is so small that you can dismiss it; however, there are some applications using floating point numbers where we have to design the code to accommodate the possiblity of error or to correct error that may accrue over a large number of calculations.  For now, just be aware that when dealing with floating point, there is error.

```string``` is Python shorthand for 'a string of characters'.
single quotes
double quotes
triple double quotes

## Type Conversion
```int()```
```float()```
```str()```

## Input
```<user_input> = input(<prompt>)```

## Reassignment
Expression on the right side of the assignment operator is evaluated first.  We can assign a variable that is used in the expression in the right side expression.  Consider the following code.
```python
x = 0
x = x + 1
```

What is wrong with this code if this is the entire program:
```python
y = y + 1
```
A variable has to initialized before using it.

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

> This list will grow as we introduce other types of operators.
