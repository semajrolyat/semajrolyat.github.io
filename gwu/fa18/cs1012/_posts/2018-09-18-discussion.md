---
layout: post
title:  "Functions"
date:   2018-09-18 00:00:00 -0400
schedule:   2018-09-18 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
reading: "HtTLaCS 6.4-6.9"
exercises: "/gwu/fa18/cs1012/2018/09/18/exercises.html"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

### Calling a Function
We have used a number of built in Python functions throughout our work so far which have generally been described as "commands", but the more correct name is _function_.  Functions also sometimes called _methods_.

For example, we have called the ```forward``` function from the turtle module to move the turtle forward.  The ```forward``` function accepts one parameter, _i.e._ a value inside the parentheses, that tells the turtle how many units to move forward.  For example, the following code instructs the turtle to move forward 100 units:
```python
from turtle import *
forward(100)
```
Likewise, we have used the ```left``` and ```right``` functions to turn the turtle and the ```penup``` and ```pendown``` functions to control whether or not the turtle draws when the turtle is instructed to move.

We _call_ a function by specifying the function name followed by a pair of parenthesis which may contain one or more parameters.

When we call ```forward```, we are calling the ```forward``` function in the [Python turtle module](https://docs.python.org/3/library/turtle.html#turtle.forward).  The ```forward``` function has the following declarion:
```python
def forward(distance):
```
The value we have been providing to the ```forward``` function inside the parentheses is handled inside the ```forward``` function as a variable named ```distance```.

The ```forward``` function _encapsulates_ all of the operations necessary to move the turtle forward which includes all the drawing operations needed to draw on the window.  We do not need to know how the turtle draws, we only need to know how to call ```forward``` in order to move the turtle and draw.  This is known as _information hiding_.

> Functions are one means of _encapsulation_ and _information hiding_.  We will talk about this in more detail when we discuss classes and object oriented programming.

Functions promote _reusability_ and _generalizability_ which we have established as an important tenet of programming.

_________
### Defining our own Functions
We can define our own Python functions using the function _definition_ structure:
```python
def name(parameters):
    statements
```

The definition for a Python function has the following requirements:
* A function definition must begin with the ```def``` keyword.
* A function definition must have a ```name``` which follows the same naming rules as variables.
* A function definition must include a set of parentheses following the ```name```.
* The parentheses must be followed by a colon ```:``` character.
* Everything inside the body of the function must be indented.
* Inside the parentheses, parameters may be specified.

> The first line of a function definition, from the ```def``` keyword to the colon ```:```, is also known as the function _declaration_.

_________
### Functions must be defined before they can be used
Recall that Python is processed sequentially.  Functions must be defined before they can be called.  In other words, a function must be defined in the script above where they are used.

#### ERROR Attempting to use a function before it is defined
In this example, the function ```foo``` is defined after it is called.  Because the Python Interpreter has not encountered a definition for ```foo``` yet, the program generates an error:
```python
# main program
foo()

def foo():
    print("called foo")
```
The Python interpreter will produce the following error if the above program is run:
```
NameError: name 'foo' is not defined
```
#### Correctly defining a function before using it
```python
def foo():
    print("called foo")

# main program
foo()
```
Python scripts are typically structured such that all functions are defined at the beginning of the script and the "main" program is defined at the end of the script.

_________
### Parameters
Parameters are specified as a number of comma separated variables inside the parentheses following the function ```name```; however, a function does not have to require parameters.  For functions that accept no parameters, the parentheses will have nothing in between them:
```python
def ex_noparams():
    print("This function has no parameters")
```

Conversely, a function may accept a variety of parameters separated by commas inside the parentheses:
```python
def ex_twoparams(p1, p2):
    print("This function accepts two parameters named p1 and p2", p1, p2)
```
Parameters are treated as variables that are locally defined for a function.

> There is an upper limit on the number of parameters that you can specify for a function; however, this number is sufficiently large that the actual limitation is irrellevant.  What is more important is that defining a function with too many parameters makes the function more difficult to use and is usually a sign of poor design.  We will discuss how to appropriately manage the number of parameters later in the term.

#### Arguments and Parameters
The terms _argument_ and _parameter_ have slightly different connotations but are often used interchangably.  The difference is somewhat trivial in terms of the objectives of this course and we will make no real distinction between these terms in this course so you can consider these terms to by synonyms.

To clarify the two terms a bit, an "argument" is a value passed to a function from the calling context and a "parameter" is the field that is received in the function.  The distinction arises because parameters are represented locally in the function as variables but the arguments passed to the function may be variable or literal.  However, to make this more confusing, the term "parameter" is used interchangeably in the context of "argument".

If you see the term argument in these pages, the context will always be in terms of a value passed to a function from the calling side.

```python
def ex_argsvsparams(param1, param2):
    # inside the function, "arguments" are parameters which are variables
    print("Hello")

arg1 = "arg1"
ex(arg1, "arg2")  # arguments can be variables and/or literals
```

> In other languages, the programmer typically specifies the type of the parameter, but in Python we do not.  A parameter will have the same type as the argument passed to it.  You may have to use type conversion to make sure a parameter has the correct type.


### Position determines parameter assignment
Arguments are mapped to parameters depending on the position at which they appear inside the parentheses.  This allows variables that are passed to a function to be remapped/renamed to a different variable name.  This can be very confusing for new programmers.  For example, consider the following script:

```python
def myfun(x,y):
    print(x,y)

x = 5
y = 10
myfun(y,x)
print(x,y)
```
This script produces the following output:
```
10 5
5 10
```
This might seem nonsensical, but it is entirely consistent if you remember that parameters are assigned based on the position of the argument and not based on any name an argument might have had before the function was called.  The ambiguity with names is eliminated if we simply rename the parameters in the previous example:

```python
def myfun(p,q):
    print(p,q)

x = 5
y = 10
myfun(y,x)
print(x,y)
```
This example is the exact same program and helps to illustrate that there is no relationship between the parameters inside the function and the variables outside the function other than what is specified by the positioning of the arguments when the function is called.

A trace of the previous example may help show how the system is operating:
```python
def myfun(p,q):
    print(p,q)

x = 5            # x = 5
y = 10           # x = 5, y = 10
myfun(y,x)       # x = 5, y = 10 -> myfun(10,5) -> myfun's p = 10, q = 5
print(x,y)       # x = 5, y = 10 -> print(5,10)
```
If we take a step back to the original example, we might now see that the parameters for ```myfun``` remap the names ```x``` and ```y``` and the only association between the ```x``` and ```y``` outside of ```myfun``` and the ```x``` and ```y``` inside ```myfun``` is the position of the parameter and the position of the argument.  Here is the trace in the original context:
```python
def myfun(x,y):
    print(x,y)

x = 5            # (global) x = 5
y = 10           # (global) x = 5, y = 10
myfun(y,x)       # (global) x = 5, y = 10 -> (myfun) x = 10, y = 5
print(x,y)       # (global) x = 5, y = 10 -> print(5,10)
```

_________
### The ```return``` Keyword
The ```return``` keyword allows the normal control flow of functions to be superceded.  If a statement begins with ```return```, the function will immediately return back to the calling context.
```python
def biz():
  a = 1
  return     # biz() returns to the calling context here because of the return
  b = 2      # due to the previous statement, this statement is unreachable

biz()
```

There is an implicit ```return``` at the end of all functions.  For example, the following code:
```python
def buz():
  a = 1

biz()
```

Is actually processed like this:
```python
def buz():
  a = 1
  return     # this return is not necessary because it is implied at the end of all functions

biz()
```

Until we look a little deeper at branching, usage of ```return``` in this way will seem a little unnecessary; however, ```return``` is dual usage and for our immediate needs ```return``` offers us the ability to return data from a function to the calling context.

_________
### Returning data from a function
Functions can perform computations and _return_ the results of those computations using the ```return``` keyword.  Any expression that appears to the right of the ```return``` keyword is evaluated and the function immediately jumps back to the calling context with that value.  In other words, ```return``` assigns a value to the function itself which can be used in an expression in the calling context.

For example, in the following function, the value of ```10``` is returned from the function ```bar()``` and ```x``` is assigned the value of ```10``` that was returned from ```bar()```:

```python
def bar():
    return 10
x = bar()       # this is the calling context
```

When we wrote our scripts for the diamond exercises, we needed to compute the hypotenuse of a right triangle.  We could use our own function to compute the hypotenuse instead:

```python
"""
returns the length of the hypotenuse for a right triangle given side1 and side2
"""
def hypotenuse(side1,side2):
    return sqrt(side1**2 + side2**2)
radius = 50
length = hypotenuse(radius,radius)
```

Recall that in assignment, the right side is evaluated first, and therefore in the final statement ```length = hypotenuse(radius,radius)```, the ```hypotenuse``` function is called first.  The ```hypotenuse``` function performs its computations and the value is returned back to the calling context.  The assignment of ```length``` is then performed and ```length``` is assigned whatever value was computed by calling ```hypotenuse(radius,radius)```.

To illustrate further, consider the following code:
```python
def fiz():
    return 3;
def buz():
    return 2;
def jaz():
    return -1;

result = fiz() + buz() * jaz()
```
Recall that expressions are computed from left to right.  When the last line ```result = fiz() + buz() * jaz()```, the operations proceed in the following order:
1. The expression on the right side of the assignment is computed first.
   1. The expression is scanned from left to right and any precedence rules are applied.
   1. Binary multiplication has the highest precedence, so the two operands needed for multiplication are evaluated:
      1. ```buz()``` is the left multiplication operand, so ```buz()``` is called and its return value ```2``` is used as the left operand.
      2. ```jaz()``` is the right multiplication operand, so ```jaz()``` is called and its return value ```-1``` is used as the right operand.
      3. Multiplication is performed on the results of the calls to ```buz()``` and ```jaz()``` which produces the single value of ```-2```.
   2. Binary addition has the highest precedence of the remaining operations, so the two operands needed for addition are evaluated:
      1. ```fiz()``` is the left addition operand, so ```fiz()``` is called and its return value ```3``` is used as the left operand.
      2. ```-2``` is the right operand which was computed from the previous operation.
      3. Addition is performed on the result of the call to ```fiz()``` and the previous multiplication which produces the single value of ```1```.
5. The right side expression contains no more operators to evaluate and has been resolved as a value, so that value is assigned to the left side, ```result = 1```.

> One novel aspect of Python is that functions may return multiple values.  Most languages only allow one value to be returned from a function.

_________
### Scope
The term _scope_ is used to describe the _visibility_ and _lifespan_ of variables and functions.

A variable is only visible and only lives within the scope that it is defined.  For example, variables that are defined inside a function are only visible and only live inside the body of that function.  This means that variables defined inside a function have _local scope_ and are _local variables_ of that function.  In other words, variables that are defined inside a function have no meaning outside of the function in which they are defined.  Parameters are always _local variables_.

Variables that have been used outside a function are generally not visible inside a function.  This is beneficial because we can reuse the same names in different contexts.  Sometimes we do wish to make variables from other contexts available to functions.  We can do this by either making a variable global or by passing a variable to a function as a parameter.

A _global variable_ is a variable that is defined outside the scope of all functions or at _global scope_.  It is possible to access a global variable from inside a function, but it is not advised.

```python
myglobal = 10     # myglobal has global scope
def fun(p1):      # p1 is has scope local to fun.
    mylocal = 5   # mylocal has scope local to fun.  mylocal is undefined outside of fun
    x = 2         # a variable named x at local scope.  It is not the same as the 'global x'
x = 1             # a variable named x at global scope
fun(1)
```

The following example is intended to illustrate an attempt to access a variable that is defined at a global scope from inside a function.  This type of approach should almost **never** be used.  It is possible, but deeply discouraged...

```python
myglobal = 10            # myglobal has global scope
def fun2():
    mylocal = myglobal   # the intent here appears to be to assign a local variable from the global variable
fun2()
```
The correct way to implement the intent illustrated by ```fun2``` is to pass the global into the function using a parameter which will make the variable a local.  For example:
```python
myglobal = 10            # myglobal has global scope
def fun3(mylocal):
    # do stuff
    return
fun3(myglobal)
```

```fun3``` is the correct approach because ```fun3``` forces the users of the function to explicitly assign all parameters and a local copy of the global will be made.  There will be no possibility of mysterious changes to ```myglobal``` by ```fun3``` and the programmer who uses ```fun3``` will know exactly what parameters must be provided.  A programmer still has the option of updating ```myglobal``` in a more controlled and safer way if the updated value is returned by the function.  For example, if the intent is for the function to produce an answer that should update ```myglobal```, the code should be designed this way:
```python
myglobal = 10            # myglobal has global scope
def fun4(mylocal):
    # do stuff like updata mylocal
    return mylocal
myglobal = fun4(myglobal)
```

> Passing data to a function outside of parameters, _i.e._ by using a global variable instead, is discouraged.  If a function contains a global variable inside its body, the function cannot be reused in other contexts.  There are some exceptions to this guideline, but as new programmers, you should avoid attempting to access a variable that is defined outside a function from inside that function.  We will discuss how to pass a large number of values to a function without needing to enumerate them all which is often the best approach rather than attempting to access a global variable from inside a functions or by adding too many extra parameters.

### Documenting functions
While we do not need to know how a function works, we do need to know how to use a function.  Every function should have a block comment describing what the function does, what each parameter means, and what the function returns.  A block comment can be provided using hash comments or triple quotes and it should precede the function declaration.

Recall our hypotenuse function from before:
```python
"""
returns the length of the hypotenuse for a right triangle given side1 and side2
"""
def hypotenuse(side1,side2):
    return sqrt(side1**2 + side2**2)
radius = 50
length = hypotenuse(radius,radius)
```
The comments that document the function precede the function declaration and the comments are concise yet detail the parameters, what the function does, and what the function returns.

> Many programmers do not document their code enough.  Without documentation, it is very unlikely that anyone will ever use your code.  Documentation is simply another task that is necessary during software development.

### Parameters are "passed by value".
Consider the following code:
```python
def swap(x,y):
    tmp = x
    x = y
    y = tmp
    print(x,y)

x = 2
y = 11
swap(x,y)
print(x,y)
```
> What do you expect will be printed for the above?  What is actually printed?  Why does the above print what it does?

Parameters are copies of the arguments that are supplied by the calling context.  This means that if we change the value associated with a parameter inside the function, it will **NOT** update the value of the argument in the calling context.  For example, in the following code, changes to the local variable ```i``` inside the function ```ex_byvalue``` has no affect on the value of ```i``` in the calling context:
```python
def ex_byvalue(i):
    i = i + 1
    print(i)

i = 1
ex_byvalue(i)
print(i)
```
The code above produces the following output:
```
2
1
```
Note that the value of the local ```i``` is incremented, but the value of the ```i``` in the calling context remains what it was before the function ```ex_byvalue``` was called.

### Functions within Functions
Recall the code we have so far used to draw a square:
```python
from turtle import *

x = 100
for i in range(4)
    forward(x)
    left(90)

done()
```
This code works because it repeatedly calls the functions ```forward``` and ```left``` from the ```turtle``` module.  We can write our own function so that we can reuse this square code without needing to write it more than once.  For example, the following code accomplishes the same goal, but it enables us to draw squares without needing to write the same ```for``` loop multiple times:
```python
from turtle import *
def square(length):
  for i in range(4):
      forward(length)
      left(90)

square(100)
done()
```
We are calling the ```forward``` and ```left``` functions from within our own function.  Code mostly consists of calling functions from other functions.

### Reuse
We may draw many squares by calling the same function repeatedly.  By allowing the ```length``` to be provided through a parameter, we can draw any sized square by supplying a different argument.  In the following code, we call the square function multiple times with different lengths:
```python
from turtle import *
def square(length):
  for i in range(4):
      forward(length)
      left(90)

square(100)
square(80)
square(60)
square(40)
square(20)
done()
```
The above code produces the following drawing:

![Turtle Squares]({{ "/gwu/fa18/cs1012/assets/09_18_2018/squares.png" | absolute_url }})

_________
### Optional Parameters
Parameters can be specified to be optional by providing a _default value_.  The default value is specified by assigning a value to the parameter in the function declaration.  An optional parameter may be omitted when calling the function.  If an optional parameter is omitted, the parameter will be set to the default value. Optional parameters must appear at the end the parameter declarations.

```python
def opts(p1, p2, p3=0):
    print("parameters p1 and p2 are required but p3 is optional")

# main program
opts(1,2)      # calls with the values (p1=1, p2=2, p3=0)
opts(1,2,3)    # calls with the values (p1=1, p2=2, p3=3)
```
_________
### Functions with the same name

Two functions can have the same name but they must have a different number of parameters.
Optional parameters are not considered when comparing two function declarations.

```python
def baz():
    print("called baz with no parameters")

def baz(p1):
    print("called baz with one parameter")

def baz(p1, p2, p3=0):
    print("called baz with two + optional parameters")

# main program
baz()     # calls baz with no parameters
baz(1)    # calls baz with one parameter
baz(1,2)  # calls baz with two and optional parameters
```
