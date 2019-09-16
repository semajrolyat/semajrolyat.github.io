---
layout: post
title:  "Types"
date:   2019-09-16 00:00:00 -0400
schedule:   2019-09-16 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
reading: "HtTLaCS 4.4-4.7"
term: "fa19"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

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

### Taking Input From the Console
While we have so far focused on writing programs that operate on hardcoded information, we need a way to be able to take input from a user.  Data is not hardcoded into programs and is typically loaded from a file or provided through user interaction.  We will focus on loading data files later, but for now we will look at a simple interface that allows a programmer to take input directly from the user.

The ```input(prompt)``` function allows a Python programmer to request input from a user at the command line.  The ```prompt``` parameter inside the parentheses for ```input(prompt)``` represents the message as a ```string``` that the programmer wishes to print in order to prompt the user for input.  For example, the following Python code prints "Enter a value: " to the terminal, waits for the user to enter information, and then assigns ```x``` when the user presses the *RETURN* or *ENTER* key on the keyboard:

```python
x = input("Enter a value: ")
```

In the above code, whatever information that was entered by the user before pressing the *ENTER* key is stored in the variable ```x```.

In order to use information input by the user, we must make sure that it is of the correct type.  The first question we must ask is what the inherent type of the information that was input.  The following code will make clear the inherent type of user input:

```python
x = input("Enter a value: ")
print(type(x))
```

If we run the above code several times and enter the following inputs:
```
1
1.0
abc
```
We will see that regardless of what values a user enters, the type is always reported as ```str``` or a string type.  If a programmer wishes to use a value entered by the user as a specific type, the programmer must cast the data returned from input as the desired type.

> A programmer may have specific expectations and may provide a very detailed prompt instructing the user to provide a value within a specific range of values; however, users may not follow instructions.  Regardless of whether a programmer requests an ```int```, a user does not have to enter a value that can be cast to an ```int``` which can break the program.  This can lead to a programmer including rather complex validation and error checking to make sure the user has entered a legal value.  We will generally avoid discussing this in detail; however, this is one of the most common source of bugs and errors in a system, _i.e._ a programmer builds a program around a limited set of assumptions which are easily circumvented by bad input.       

### String Concatenation
In lab, we explored printing complex strings using comma separated arguments.  An alternative approach is to build up a string over a number of operations and then print the single string as one argument.  We can combine two strings into one using the concatenation operator.  To concatenate means to append a new series onto the end of another series.  For example, if we concatenate ```def``` onto ```abc``` the result is ```abcdef```.

In Python, we can concatenate two strings using the concatenation operator ```+```.  Note that the concatenation operator is the same symbol as the mathematical addition operator.  This raises the question of how Python can discriminate between addition and concatenation if the same symbol is used for two different operations.  

The answer is that Python determines the operation based on the type of the operands.  The left operand dictates how the ```+``` operator is interpreted.  If the left operand is a string, then Python interprets the ```+``` operator as concatenation.  If the left operand is a numeric, then Python interprets the ```+``` operator as something else (addition if both operands are numeric).  For example:
```python
print("Hello" + "World")   # + interpreted as concatenation
print(1 + 2)               # + interpreted as addition
```
The above code produces the following output:
```
HelloWorld
3
```

A problem arises if the types of operands are mixed.  In this case, Python generates an error because the intent of the programmer is unclear.  For example, the following code causes Python to interpret the ```+``` operand as concatenation; however, Python errors because the right operand is not a string:

```python
print("Hello" + 1)
```
The above code produces the following error:
```
TypeError: can only concatenate str (not "int") to str
```
Conversely, if the left operand is a numeric, Python also generates an error because Python cannot perform addition on a number and a string.  The error is a little more ambiguous as Python cannot identify a ```+``` operation that is valid (this case is not actually interpreted as mathematical addition).  For example:
```python
print(1 + "Hello")
```
The above code produces the following error:
```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

We can clarify our intent and eliminate these errors by ensuring that the operands are converted to a type where Python can identify the correct operation.  Reconsider the first ```TypeError``` example above.  If our intent is to build a string consisting of ```Hello1```, then we would use the following approach:
```python
print("Hello" + str(1))
```
The above code eliminates the error because both operands are strings so Python can unambiguously interpret ```+``` as concatenation.

### Dynamically Building a String
We can store string information in a variable and build up content before printing it to the console.  For example:

```python
s = "Hello"
s = s + " "
s = s + "World"
print(s)
```
The above code produces the following output:

```
Hello World
```

We are not limited to printing a string on a single line.  Python (and many languages) use a special combination of characters to indicate a 'new line'.  The new line combination is ```\n```.  For example, the following code includes the new line character to split the output over multiple lines:

```python
s = "Hello"
s = s + "\n"
s = s + "World"
print(s)
```
The above code produces the following output:
```
Hello
World
```

### Program Structure

We can dynamically build strings from mixed type information, format as desired, and print it to the console when necessary.  Generally, programs are organized in the following way:

1. Take input
2. Perform computation
3. Generate output

This pattern forms the basic concept of an _**algorithm**_.  The formal definition of an algorithm is a little more abstract; however, all algorithms follow this basic structure.  

A program is just a rather large algorithm that combines a number of smaller algorithms together to perform computation.  While we may not always take all inputs at the beginning of the program and we may not always delay all outputs until the end of the program, we do need to set up the initial conditions (inputs) before performing computation and we do not typically have a meaningful result (outputs) until the computation is complete.
