---
layout: post
title:  "Types"
date:   2018-09-06 00:00:00 -0400
schedule:   2018-09-06 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
reading: "HtTLaCS 4.4-4.7"
exercises: "/gwu/fa18/cs1012/2018/09/06/exercises.html"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Types
In our previous discussions, we have established that values whether literals or variables have a _type_ (shorthand for _data type_).  In Python, every value is treated as an _object_.  We will discuss objects more in depth later.

In the previous class, we established that operations produce output that conforms to types that are determined by the operation and/or the operands used in the operation.  In many other languages, data types are a critical concern and the programmer must explicitly specify the type of each variable.  In Python, data type is still an important concern but it is generally handled behind the scenes.  As a result, a Python programmer does not have to be as concerned with types as a programmer in one of these other languages, but a Python programmer still must be aware of the issues involved with types.

The fundamental data types that we have so far discussed are integer, floating-point, and string.

#### Integer
In Python, the keyword ```int``` is used to specify an integer type.  The ```int``` type maps generally to the [Set of Integers](https://en.wikipedia.org/wiki/Integer); however, due to the natural limits imposed by computer hardware, not all integers can be represented, but we have to reach really large numbers (positive or negative) before we need to worry about whether an integer can be represented.


#### Floating-Point
In Python, the keyword ```float``` is used to specify a floating-point type.  The ```float``` type maps generally to the [Set of Real Numbers](https://en.wikipedia.org/wiki/Real_number); however, due to the natural limits of computer hardware, not all real numbers can be represented.  And due to the way computers represent these numbers, there is some inherent inaccuracy that will introduce error into floating point calculations.

> The error in floating point calculations is typically very small, but it exists.  For the most part, this error is so small that you can dismiss it; however, there are some applications that use floating point numbers where we have to design the code to accommodate the possiblity of error or to correct the error that may accrue over a large number of calculations.  For now, just be aware that when dealing with floating point, there is inherent inaccuracy.

#### String
Programmers use the term _string_ to describe data that contains a sequence of characters.  In Python, any characters enclosed between single quotes, double quotes, or a set of triple quotes (double or single) will be interpreted as string.  For example, each of the following statements is interpreted in Python as a string:
```python
"Hello World"
'Hello World'
'''Hello World'''
"""Hello World"""
```

Triple quotes are allowed to span multiple lines.  For example, the following example shows one string that spans multiple lines:
```python
"""
This
is
a
multi-line
string
"""
```

### Checking Type
We can check the type of an expression by using the ```type(x)``` function.

```python
print(type(1))
print(type(1.0))
print(type('a'))
```
The output from the above code is:
```
<class 'int'>
<class 'float'>
<class 'str'>
```

### Type Conversion
The ```int(x)```, ```float(x)```, and ```str(x)``` functions take an input value ```x``` and return that value respectively as an integer, float, or string.  For example, the following code demonstrates converting from differnt types:
```python
x = int(1.5)
y = float(5)
s = str(y)
```

We have discussed in class that we may need to control the type of the values produced from mathematical operators like ```/``` and ```%```.  We can explicitly define what type the result of an operation should produce.  We can either convert the type before the operation or convert the type after the operation is performed by using a type conversion function.  Consider the following code:

```python
x = int(1.0)/int(1.5)
y = int(1.0/1/5)
print(x)
print(y)
```
The output from this code is:
```
1.0
0
```
**Question**:  Why does the preceding code produce the above output?

## Input
The ```input(prompt)``` function allows a python programmer to request input from a user at the command line.  The ```prompt``` parameter inside the parentheses for ```input(prompt)``` represents the message that you would like to print to the terminal to prompt the user for input.  For example, the following Python code, prints "Enter a value: " to the terminal and waits for the user to enter information and then press the *RETURN* key on the keyboard:
```python
x = input("Enter a value: ")
```
In the above code, whatever information that was entered by the user before pressing the *RETURN* key is stored in the variable ```x```.

In order to use information input by the user, we must make sure that it is of the correct type.  The first question we must ask is what the inherent type of the information that was input.  The following code will make clear the inherent type of user input:
```python
x = input("Enter a value: ")
print(type(x))
```
Run the above code several times and enter the following inputs:
```
1
1.0
abc
```
**Question**: What implicit type does the ```input``` function produce?  How can we ensure that the values input by a user are handled using a type compatible with code that we have written?


## Reassignment
The expression on the right side of the assignment operator is evaluated before any assignment is made.  We can therefore use the same variable that is being assigned in the expression on the right side of the assignment operator.  The following code is legal if ```x``` has been assigned before the program reaches this code:
```python
x = x + 1
```

For example, the following is legal in Python:
```python
x = 5
x = x + 1
```

**Question**: If the following code was the entire Python program, why would this code generate an error:
```python
y = y + 1
```
**Question**: Why might we use reassignment?
