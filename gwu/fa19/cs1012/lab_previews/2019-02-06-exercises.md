---
layout: post
title:  "Exercises"
date:   2019-02-06 00:00:00 -0400
schedule:   2019-02-06 00:00:00 -0400
categories: [GWU]
docclass: "exercises"
gwclass: "cs1012"
term: "sp19"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Exercises 3

### Due Date
**The solutions to these exercises must be submitted by the end of the day.**

### Instructions

Before trying to write any code, plan out how you will to use the primitives defined here to draw the solution.  If you don't plan, you may make a mistake and have to start over.  It's a good idea to have pen and paper available.

You are allowed to collaborate with your neighbor on these exercises.  Each of you must complete the programming tasks individually; however, you are encouraged to discuss and work together to design a solution to the problems.

Before beginning, make sure to create a new folder named ```NETID_lab03``` in your class folder.

Create a .zip archive containing all of your code files and submit the .zip archive to blackboard as your solutions to these exercises.

### String Concatenation
Rather than calling print with multiple comma separated values, we can build a single string using concatenation.  To concatenate is to append a new series onto the end of another series.  For example, if we concatenate ```def``` onto ```abc``` the result is ```abcdef```.

In Python, we can concatenate two strings using the concatenation operator ```+```.  Note that the concatenation operator is the same symbol as the mathematical addition operator.  This raises the question of how Python can discriminate between addition and concatenation if the same symbol is used for two different operations.  

The answer is that Python determines the operation based on the type of the operands.  The left operand dictates how the ```+``` operator is interpreted.  If the left operand is a string, then Python interprets the ```+``` operator as concatenation.  If the left operands is numerics, then Python interprets the ```+``` operator as something else (addition if both operands are numerics).  For example:
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

We can dynamically build strings from mixed type information, format as desired, and print it to the console when necessary.  Generally, programs are organized in the following way:

1. Take input
2. Perform calculations
3. Generate and print output

### Exercise 1 - Introduction
> This exercise uses input, strings, and formatted output.

Create a script named ```exercise1.py```.

Write a program that prompts the user to input their name.  The prompt should read ```What is your name?```.

Store the user's response in a variable.  Build a string that concatenates ```Hello ``` with the user input, and ```. I am Python.```.  Finally, print the entire string to the console.

**IMPORTANT:** Your output **must** be in this format:
```
What is your name? <user input>
Hello <concatenated user input>.  I am Python.
```

Run your program and make sure that your program produces the expected output.  For example, if ```John``` is entered in response to the prompt, interaction with the program would look like the following:
```
What is your name? John
Hello John.  I am Python.
```

### Exercise 2 - Quadratic Formula
> This exercise adds input and types to the quadratic exercise.

Create a script named ```exercise2.py```.

Last week we created a program that computed the roots of a Quadratic Equation; however, we hardcoded the coefficients into the program.  This means that we have to change the program every time that we wish to perform the computation.  Recall that one of our goals is **generalization**, so a more generalized program would have the flexibility to accept virtually any coefficients and calculate the roots.  To generalize the quadratic program, we will instead take the coefficients as user input.

Write a script that takes the user inputs ```a```, ```b```, and ```c``` for the Quadratic Equation.  Compute the two roots of the Quadratic using the Quadratic Formula, and print the roots to the console.

In the previous quadratic exercise, you were not required to use concatenation; however, in this exercise, create one string containing all of the calculated roots using concatenation and print this string once.

**IMPORTANT:** Your output **must** be in this format:
```
Input the coefficients for Quadratic Equation f(x):
a = <coefficient 1>
b = <coefficient 2>
c = <coefficient 3> 

The Quadratic Equation has the following roots:
root = <calculated root 1>
root = <calculated root 2>
```

We cannot successfully compute roots for all Quadratics because some of the roots will be imaginary.  We will only test our scripts using a narrow set of coefficients that we can compute so that we do not generate any errors.  You must take user input using the ```input``` function.  Format your output and test your script with the following examples:

```
Input the coefficients for Quadratic Equation f(x):
a = 1
b = 0
c = -1

The Quadratic Equation has the following roots:
root = 1
root = -1
```

```
Input the coefficients for Quadratic Equation f(x):
a = 4
b = -3
c = -2

The Quadratic Equation has the following roots:
root = 1.175390529679106
root = -0.42539052967910607
```

```
Input the coefficients for Quadratic Equation f(x):
a = 2
b = -1
c = -2

The Quadratic Equation has the following roots:
root = 1.2807764064044151
root = -0.7807764064044151
```

#### Exercise 3 - Temperature Conversions

> This exercise uses: **input**, **strings**, and **types**.

Create a script named ```exercise3.py```.

The United States commonly uses the **Fahrenheit** scale. For scientific calculations, **Celsius** is used.
The formula to convert from Fahrenheit to Celsius is:

```
C = (F - 32) * 5/9
```

Write a program that takes a **Fahrenheit** temperature as input and prints out the temperature converted to **Celsius**.  

Your program must use the following format for the prompts and output:
```
Enter a temperature in Fahrenheit: <input temp>
<input temp> degrees Fahrenheit is <computed temp> degrees Celsius.
``` 
**IMPORTANT:** The output string **must** be formed by concatenation.

Test your script with **all** of these examples:
```
Enter a temperature in Fahrenheit: 32
32.0 degrees Fahrenheit is 0.0 degrees Celsius.
```

```
Enter a temperature in Fahrenheit: 212
212.0 degrees Fahrenheit is 100.0 degrees Celsius.
```

```
Enter a temperature in Fahrenheit: 72
72.0 degrees Fahrenheit is 22.22222222222222 degrees Celsius.
```

```
Enter a temperature in Fahrenheit: -40
-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
```

> Note that the string representations of the numbers suggest the data types used in the calculation.

You will submit ```exercise1.py```, ```exercise2.py```, and ```exercise3.py```.
