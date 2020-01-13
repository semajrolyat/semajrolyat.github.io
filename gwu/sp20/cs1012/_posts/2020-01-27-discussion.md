---
layout: post
title:  "Variables, Expressions, and Types"
date:   2020-01-27 00:00:00 -0400
schedule:   2020-01-27 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
reading: "HtTLaCS 2.2-2.11"
term: "sp20"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Introduction
> Much of what we discuss today will be placed in the context of mathematics.  If we only use mathematics then our programs will be nothing more than glorified calculators; however, we are focusing on mathematics now because it is hopefully a context that we all share.  We will expand beyond mathematical concepts very soon.

## Literals
Any time you write a number (or a _**string**_) into a program, that value is called a _**literal**_ and is sometimes described as being a value that is _**hardcoded**_ into the program.  In the above example, we use the literal 100 for the length of a side and the literal ```90``` for the angle of the turn.
> We will define what the term "string" means later.  The term "hardcoded" implies that the value cannot be changed once the program is started.

We can accomplish a lot using literals and they are necessary; however, if we only use literals, it will be difficult to modify the program later to write code that can be reused in different contexts.

For example, in the previous class, we draw a square that had a hardcoded size of ```100```.  If we hardcode the size, we cannot reuse the same script to draw squares of other sizes.  We would like to write one script that can draw all squares rather than write a script for each and every square that we might draw.

> Programmers strive to reuse software as much as possible.  _**Generalization**_ promotes code reuse, reduces the size of code, and is a fundamental principle of programming. Less code is usually better because there is less opportunity to make a mistake.  Most of the features in programming languages are intended to allow for generalization.

## Variables
A _**variable**_ in programming is a way to associate a **name** with a **value**.  A variable by definition can change throughout the execution of a program as opposed to a literal that cannot change.  In Python, if we assign a variable using the **assignment operator** ```=```, we both define the name as a variable to Python and instruct Python assign it the associated value.  A variable also has a **type** which we will talk about throughout the rest of the semester.

* Every variable has a type, a name, and a value.

### Names
Names given to variables (and other structures that we will discuss later) must follow specific rules:

* There are keywords that have specific meaning to Python.  Names can never match a keyword.
* Names cannot include special characters, _i.e._ ```!```, ```@```, ```#```, ```$```, ```%```, etc., with one exception.  Names can include the underscore character ```_```.
* Names must begin with a letter or underscore ```_``` and may contain numbers or the underscore character.
* Names are case sensitive.  For example, ```MyVar``` is not the same name as ```myvar```.

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
> We will discuss many of these keywords later.  For now, use this list as a reference for names that cannot be used.

### Variable Assignment
The _**assignment operator**_ ```=``` directs Python to assign the value of the expression on the right side of the assignment operator to the variable on the left side of the assignment operator.  For example:
```python
# Assign 5 to the variable x
x = 5
```
> You may be inclined to read ```=``` as 'equal to', but it is better to read it as 'is assigned'.  For the statement ```x = 5```, read it as 'x is assigned 5'.

The symbol on the left of the assignment operator must be a legal variable name and the expression to the right of the assignment operator must be a legal expression.  For example:
```python
# These are legal assignments
x = 5                    # legal - assign literal 5 to variable x
y = x                    # legal - assign value stored in x to y
s1 = "Hello there!"      # legal - assign literal string to variable s
# These are not legal assignments
5 = a                    # illegal - cannot assign a to 5
s2 = Hello there!        # illegal - Hello There! is not a legal expression
```

> The assignment of ```s1``` in the above code is legal because the value being assigned is inside double quotes ```"Hello there!"```.  A value inside quotes is called a _**string**_.  We will talk more about strings later.  The assignment of ```s2``` is not legal because the expression to the right of the assignment operator is not a valid expression.

The expression to the right of the assignment operator is evaluated and the value of the expression is then assigned to the variable on the left of the assignment operator.  Practically, this means that the same variable can appear on both the left and the right of the assignment operator where the variable on the right holds the value before the expression is evaluated and the variable on the left holds the value after the expression is evaluated.

```python
x = 0         # assign x the value of 0
x = x + 1     # x on the right is equal to 0 while x on the left is 1
```

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


## Readability
* Variables should be given meaningful names.  A meaningful name improves the readability of code.
* While many of the early examples in this course use single letter variable names  _i.e._ ```a```, ```b```, ```x```, ```y```, etc., these names are not generally meaningful unless they apply a known mathematical theorem.
* Comments and white space can improve the readability of code.  Comments provide meaningful information while whitespace can help group code.
* Comments are ignored by the Python interpreter and begin with the ```#``` character.

Readability is a very important consideration whenever writing code.  Reading code is a nonproductive exercise that costs time.  We may rely on a form of shorthand to write code faster, but a programmer should always remember that the code may need to be rewritten or fixed at a later date.  By using clear variable names, the time required to understand the code later can be significantly reduced.

For example, consider the following Python code:

```Python
l2 = math.sqrt(x*x + y*y + z*z)
```
> Note that ```math.sqrt``` will be discussed this week in lab.

More mathematically aware programmers may recognize this formula as the computation of the _**l2 norm**_; however, the l2 norm has a more common name, _**magnitude**_.  The above code could be rewritten as:

```Python
magnitude = math.sqrt(x*x + y*y + z*z)
```

or

```Python
mag = math.sqrt(x*x + y*y + z*z)
```

While it may be faster to write the variable name as ```l2```, it may not be appropriate in your organization if readers of your code will not recognize the implications of the name.  In this case, it might be more appropriate to name the variable using some variant of the term magnitude.

### Long Names
Long names may add significant more information for a reader; however, there are a number of problems that may arise if the variable name is too verbose.  One problem is simply being able to read and discern a variable if it is too long, _**readability**_, and another is being able to remember and rewrite that variable again later, _**writability**_.  

Programmers use a number of techniques to make it easier to comprehend long names.  These two strategies are either to insert underscores between words in place of spaces in a variable name or to use "Camel Casing".  

> It's called Camel Casing because the beginning of each word is made large like the hump of a many humped camel.

To highlight long names, consider an example where we need to compute the area of a number of shapes.  Let's assume that we have a rectangle defined by the variables ```length``` and ```width``` and a circle defined by the variable ```radius```.  We need to compute the area of both shapes, but we need to keep the data around for a long period of time after doing so, so we need to store each in their own variable.  If we use a variable simply named ```area```, one calculation will overwrite the other.

```Python
area = length * width
area = math.pi * radius * radius   # reassignment of area destroys the result
                                   # from the previous square calculation
```

> Since these are well defined mathematical formulas it would be quite common for the variables ```length```, ```width``` and ```radius``` to be written as ```l```, ```w```, and ```r```, but they are spelled out here since this is a discussion on readability.

We need to create unique "area" variables to store the computed values for a longer time.  Instead, we might write a short phrase by combining "area" and the type of shape:

```Python
areaofsquare = length * width
areaofcircle = math.pi * radius * radius
```

These variables will not clash with one another; however, they are a little difficult to read because there are no clear transitions for the eye between words.

#### Long Names with Underscores
If we insert underscores between the words, it will look a little more like a phrase and be more readable:

```Python
area_of_square = length * width
area_of_circle = math.pi * radius * radius
```

> Inserting underscores is a little old fashioned.  Some programmers may find it awkward to use the key which may slow them down; however, it does make a variable name highly readable.

#### Long Names with Camel Casing
A widely adopted approach today for long names is to use Camel Casing.  Camel Casing simply means to capitalize the first character of a word in long name.  Typically, the first character of a variable remains lower cased, but all subsequent words in a variable consisting of a number of words is upper cased:

```Python
areaOfSquare = length * width
areaOfCircle = math.pi * radius * radius
```

To gain make the code a little more writable and concise, the code might be reduced to:
```Python
areaSquare = length * width
areaCircle = math.pi * radius * radius
```

> There are a few more rules that have been generally agreed upon by the programming community to tell us when to capitalize a name.  In general variables will always begin with a lower case.  We won't really get into these rules further as they tend to deal with a programming structure that we will only briefly mention in this course.

## Expressions
In Python we use _**infix notation**_ to join together _**operands**_ using _**operators**_ to form an _**expression**_.  Infix notation means that binary operators appear between two operands.  Operands are values to be operated on and operators describe the operations to be performed.  An _**expression**_ may be formed by combining a number of operands and operators and expressions may appear in different contexts.  These are some examples of legal expressions:
```python
x = 3
y = 0.5 * x + 1
```
**Question**: How many expressions are there in the above example?

### Binary Mathematical Operators
In infix notation, a _**binary operator**_ appears between two operands.  In terms of mathematics, ```a + b```, ```a * b```, ```a / b``` are all examples of binary operators.

The binary mathematical operators are:
* ```a + b``` : Addition
* ```a - b``` : Subtraction
* ```a * b``` : Multiplication
* ```a / b``` : Floating point division
* ```a // b``` : Integer division
* ```a % b``` : Remainder (or modulus) of integer division
* ```a ** b``` : Raise ```a``` to the power ```b```


### Unary Mathematical Operators
In terms of mathematics, negation, _i.e._ ```-x```, is an example of a unary operator.  In infix notation, a _**unary operator**_ precedes the operand.

```python
a = -x          # the - sign is a unary operator
b = 2 + -y      # a unary operator can appear between a binary operator
```

### Grouping Operators
Parentheses act as _**grouping operators**_ just as they do in mathematical expressions and we can use grouping operators to supersede operator precedence.

```python
a = (2 + 1) * 4    # addition will occur before multiplication due to
                   # the grouping operators  
```

### Operator Precedence
[Operator Precedence Reference](https://docs.python.org/3/reference/expressions.html#operator-precedence)

Each operator has a precedence which is the same as that used in mathematics.
1. Grouping operators ```(``` and ```)```
2. Binary math operator ```**```
3. Unary math operator ```-```
4. Binary math operators ```*```, ```/```, ```//```, and ```%```
5. Binary math operators ```+``` and ```-```

> This list will grow as we introduce other types of operators.

### Binary Exponentiation (Power) Operator ```**```
The binary operator ```b ** e``` raises the base ```b``` to the exponent ```e```.

```python
x = 2 ** 4       # x will be assigned 16 or 2*2*2*2
```

### Unary Negation Operator ```-```
The unary operator ```-x``` negates the value of the operand ```x```.

```python
a = -1       # assign -1 to a
b = -x       # assign the negated value of x to b
```

### Binary Multiplication Operator ```*```
The binary operator ```a * b``` multiplies the operands ```a``` and ```b```.

```python
x = 2 * 3       # x will be assigned 6
```

### Binary Division Operator ```/```
The binary operator ```a / b``` divides the operands ```a``` and ```b``` using real number (floating point) division.

```python
x = 10 / 5       # x will be assigned 2
```

### Binary Integer Division Operator ```//```
The binary operator ```a // b``` divides the operands ```a``` and ```b``` using whole number (integer) division and returns the quotient.

```python
x = 10 // 3       # x will be assigned 3, the whole number  
```

### Binary Integer Division Operator ```%```
The binary operator ```a % b``` divides the operands ```a``` and ```b``` using whole number (integer) division and returns the remainder.

```python
x = 10 % 3       # x will be assigned 1, the whole number  
```

### Binary Addition Operator ```+```
The binary operator ```a + b``` adds the operands ```a``` and ```b```.

```python
x = 2 + 3       # x will be assigned 5
```

### Binary Subtraction Operator ```-```
The binary operator ```a - b``` subtracts the operands ```a``` and ```b```.

```python
x = 2 - 3       # x will be assigned -1
```

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


## Types
In our previous discussions, we have established that values whether literals or variables have a _**type**_ (shorthand for _**data type**_).  In Python, every value is treated as an _**object**_.  We will discuss objects more in depth later.

In the previous class, we established that operations produce output that conforms to types that are determined by the operation and/or the operands used in the operation.  In many other languages, data types are a critical concern and the programmer must explicitly specify the type of each variable.  In Python, data type is still an important concern but it is generally handled behind the scenes.  As a result, a Python programmer does not have to be as concerned with types as a programmer in one of these other languages, but a Python programmer still must be aware of issues involving types.

Programmers communicate _**intent**_ through types.  Computers are rather simple calculators that can perform a variety of calculations.  Last week, we discussed that expressions are combinations of operands and operators.  A program is simply a complex set of statements that are operated on in a specific order, _**sequentially from top to bottom**_, where each statement is composed of a number of expressions joined together by operators.  We will see that the same symbol can be interpreted as different operations depending on the _**context**_ in which that operator is used.  The context of the operator is dependent on the types of the operands associated with that operator.

The fundamental data types that we have been introduced to so far are integer, floating-point, and string.

#### Integer
In Python, the keyword ```int``` is used to specify an [integer](https://en.wikipedia.org/wiki/Integer_(computer_science%29) type.  The ```int``` type maps generally to the [Set of Integers](https://en.wikipedia.org/wiki/Integer); however, due to the natural limits imposed by computer hardware, not all integers can be represented, but we have to reach really large numbers (positive or negative) before we need to worry about whether an integer can be represented.

For example, a 32-bit integer can represent a range of more than 2 billion positive and negative numbers or a total range exceeding 4 billion numbers.  If we are working with whole numbers within these ranges, we do not need to be too concerned with numerical errors.  However, this does highlight an important consideration, memory and therefore representations are finite.

#### Floating-Point
In Python, the keyword ```float``` is used to specify a [floating-point](https://en.wikipedia.org/wiki/Floating-point_arithmetic) type.  The ```float``` type maps generally to the [Set of Real Numbers](https://en.wikipedia.org/wiki/Real_number); however, due to the natural limits of computer hardware, not all real numbers can be represented.  And due to the way computers represent these numbers, there is some inherent inaccuracy that will introduce error into floating point calculations.
necessarily
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

> Implicit and explicit errors are not limited to errors due to types, but a failure to manage type often leads to one or more bugs.  A bug may be caused by either explicit or implicit errors; however, with explicit errors there is at least an indication that an error is present.  With implicit errors, we may not know that a bug is present until significant consequences have arisen or even irreparable harm has been caused (see [Mars Polar Lander](https://en.wikipedia.org/wiki/Mars_Polar_Lander#Loss_of_communications), [Therac-25](https://en.wikipedia.org/wiki/Therac-25#Problem_description), [Y2K](https://en.wikipedia.org/wiki/Year_2000_problem#Resulting_bugs_from_date_programming), and [Boeing 737 MAX](https://en.wikipedia.org/wiki/Boeing_737_MAX#Worldwide_grounding)).  We must make sure that we properly and fully express our intent when writing code and we must take steps to validate results in order to eliminate implicit errors.   Debugging implicit errors is time consuming and difficult.
