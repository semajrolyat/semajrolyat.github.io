---
layout: post
title:  "Types"
date:   2019-02-04 00:00:00 -0400
schedule:   2019-02-04 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
reading: "HtTLaCS 4.4-4.7"
exercises: "/gwu/sp19/cs1012/2019/02/06/exercises.html"
homework: "/gwu/sp19/cs1012/2019/02/06/homework.html"
term: "sp19"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Types
In our previous discussions, we have established that values whether literals or variables have a _**type**_ (shorthand for _**data type**_).  In Python, every value is treated as an _**object**_.  We will discuss objects more in depth later.

In the previous class, we established that operations produce output that conforms to types that are determined by the operation and/or the operands used in the operation.  In many other languages, data types are a critical concern and the programmer must explicitly specify the type of each variable.  In Python, data type is still an important concern but it is generally handled behind the scenes.  As a result, a Python programmer does not have to be as concerned with types as a programmer in one of these other languages, but a Python programmer still must be aware of issues involving types.

The fundamental data types that we have been introduced to so far are integer, floating-point, and string.

#### Integer
In Python, the keyword ```int``` is used to specify an [integer](https://en.wikipedia.org/wiki/Integer_(computer_science%29) type.  The ```int``` type maps generally to the [Set of Integers](https://en.wikipedia.org/wiki/Integer); however, due to the natural limits imposed by computer hardware, not all integers can be represented, but we have to reach really large numbers (positive or negative) before we need to worry about whether an integer can be represented.

For example, a 32-bit integer can represent a range of more than 2 billion positive and negative numbers or a total range exceeding 4 billion numbers.  If we are working with whole numbers within these ranges, we do not need to be too concerned with numerical errors.  However, this does highlight an important consideration, memory and therefore representations are finite.

#### Floating-Point
In Python, the keyword ```float``` is used to specify a [floating-point](https://en.wikipedia.org/wiki/Floating-point_arithmetic) type.  The ```float``` type maps generally to the [Set of Real Numbers](https://en.wikipedia.org/wiki/Real_number); however, due to the natural limits of computer hardware, not all real numbers can be represented.  And due to the way computers represent these numbers, there is some inherent inaccuracy that will introduce error into floating point calculations.

The error in floating point calculations is typically very small, but it exists.  Remember that memory is finite so rational numbers like ```1/3``` and irrational numbers like ```pi``` must be approximated because they are infinite series when represented in decimal form.

For the most part, floating point error is small enough that we can dismiss it; however, there are some applications that use floating point numbers where we have to design the code to accommodate the possibility of error or to correct the error that may accrue over a large number of calculations.  One such error that we need to consider is that two floating point numbers can be approximately equal but not actually equal.

For now, just be aware that when dealing with floating point, there is inherent inaccuracy.

#### String
Programmers use the term _**string**_ to describe data that contains a sequence of characters.  In Python, any characters enclosed between single quotes, double quotes, or a set of triple quotes (double or single) will be interpreted as string.  For example, each of the following statements is interpreted in Python as a string:
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

**Question**: If triple quotes are legitimate, why not a set of double quotes?

> A string belongs to a set of types known as sequence types.  We will revisit the string when we dive deep into sequence types.

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
The ```int(x)```, ```float(x)```, and ```str(x)``` functions take an input value ```x``` and return that value respectively as an integer, float, or string.  For example, the following code demonstrates converting from different types:
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

### Type Errors
Both explicit and implicit errors can arise in a program due to type.  Due to the flexibility of the Python language, many type errors that would be explicitly caught in other languages are allowed not caught and result in implicit errors.  All programmers must become proficient in expressing their full intent in a programming language in order to minimize implicit errors as these errors can be very difficult to locate and debug.

#### Explicit Type Error
An explicit type error will throw an exception (an error), cause the program to halt, and report the location of the error and a relevant message (hopefully) regarding the error.   For example, the following program explicitly fails because the ```+``` operator in this context must have the same type (string or numeric) for both operands and can not mix and match as it does:

```python
print("x = " + 1)
```
The above program generates an exception which is reported in the terminal:
```
File "ex_explicit_type_error.py", line 1, in <module>
    print( "x = " + 1 )

TypeError: can only concatenate str (not "int") to str
```
The above exception indicates that there is a type error that was explicitly caught on line 1 of the program.  The message indicates that the ```+``` operator in this context must have strings in both operands (Actually, this is a little misleading, because it would be legal to have numerics for both operands).  If the intent is to print ```x = 1```, we can solve this by type converting the numeric.

```python
print("x = " + str(1))
```
The above program now produces the following output:
```
x = 1
```
> We will talk more about concatenation when we dive deep into strings.  For now, you should note that an operator may be interpreted different ways depending on the operands.  Context matters.

#### Implicit Type Error
An implicit type error occurs because a programmer fails to fully express their intent in the language by creating a legal statement that can successfully perform an unintended operation.  Consider the following code for a moment:

```python
print( "x" * 2 )
```

It may not be entirely clear what the programmer's intent is with the above program; however, the above program is entirely legal and produces the following output:

```
xx
```

The above result may be precisely what the programmer intended, it is legal after all; however, this also may be an _**implementation error**_ meaning that the programmer failed to implement the program correctly.  Without some accompanying documentation like comments, it will be exceedingly difficult for anyone to correct the program.  Implementation errors can have disastrous consequences on programs and users; because, even if a program produces an answer, it is unclear whether the answer is correct or not.

> Implicit and explicit errors are not limited to errors due to types, but a failure to manage type often leads to one or more bugs.  A bug may be caused by either explicit or implicit errors; however, with explicit errors there is at least an indication that an error is present.  With implicit errors, we may not know that a bug is present until significant consequences have arisen or even irreparable harm has been caused (see [Mars Polar Lander](https://en.wikipedia.org/wiki/Mars_Polar_Lander#Loss_of_communications), [Therac-25](https://en.wikipedia.org/wiki/Therac-25#Problem_description), and [Y2K](https://en.wikipedia.org/wiki/Year_2000_problem#Resulting_bugs_from_date_programming)).  We must make sure that we properly and fully express our intent when writing code and we must take steps to validate results in order to eliminate implicit errors.   Debugging implicit errors is time consuming and difficult.



## Input
The ```input(prompt)``` function allows a python programmer to request input from a user at the command line.  The ```prompt``` parameter inside the parentheses for ```input(prompt)``` represents the message as a ```string``` that you would like to print to the terminal to prompt the user for input.  For example, the following Python code prints "Enter a value: " to the terminal, waits for the user to enter information, and then assigns ```x``` when the user presses the *RETURN* or *ENTER* key on the keyboard:

```python
x = input("Enter a value: ")
```

In the above code, whatever information that was entered by the user before pressing the *ENTER* key is stored in the variable ```x```.

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
