---
layout: post
title:  "For Loop"
date:   2019-02-11 00:00:00 -0400
schedule:   2019-02-11 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
reading: "HtTLaCS 3.1-3.5 & 6.1-6.3"
term: "sp19"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>


### Iteration
The code we have so far written to draw a square consists of the same instructions repeated multiple times:

```python
forward(x)
left(90)
forward(x)
left(90)
forward(x)
left(90)
forward(x)
```

There is a clear pattern in this code and we would like to reduce it if possible.

Programmers generally seek to reduce the overall amount of code.  We do this to limit the possibility of introducing bugs and to generalize code wherever possible. Less code promotes _**reliability**_ and generalization promotes _**reusability**_.

Programming languages provide structures that allow code to loop or _**iterate**_ over one or more statements so that those actions can be performed a number of times.  Python has multiple ways to loop; however, the most widely used and fundamental type of loop is called a ```for``` loop.

> As a rule of thumb, you will probably write 100 ```for``` loops for any other type of loop you might consider.

For example, we can write a Python ```for``` loop to print out the contents of a list:
```python
for student in ["Elise", "Charlie", "Bob", "Alice", "David"]:
    print("Welcome", student, "to Introduction to Programming with Python")
```

The Python ```for``` loop operates on a list.  In the above example:
* The list is specified by the strings inside the square brackets, _i.e._ ```[``` and ```]```, so the list contains the strings ```["Elise", "Charlie", "Bob", "Alice", "David"]```.
* The variable ```student``` is called the _**loop variable**_ and contains the name from the list that is currently being operated on.  Each item in the list will be assigned to the loop variable once in the order that they appear from left to right.
* To make it more clear, it might help you to read the loop statement as "for each student in the list".
* The line where the loop is defined must end in a colon ```:```
* Everything inside the body of the loop --- beginning at the ```print``` statement --- must be indented.  **Indentation is important in Python**.
* When the bottom of the loop body is reached, the interpreter will jump back up to the ```for``` statement and assign the next item in the list to loop variable.
* The _**terminating condition**_ for a loop determines when the loop ends.  In a ```for``` loop, the terminating condition occurs when the end of the list is reached.
* When the terminating condition is reached, the loop terminates and the loop body is bypassed and the interpreter jumps to the next statement following the loop body.


### Control Flow
Without special instructions, the Python interpreter will process a script line-by-line from top to bottom, or _**sequential**_.  Certain keywords allow a programmer to change this behavior and control the _**flow of execution**_  --- the terms _**control flow**_ and _**branching**_ are synonyms for "flow of execution".  Through control flow, we can jump back up to an earlier statement or choose to optionally process statements.  We will talk more about other ways to control the flow of execution soon, but for now, we will focus on the ```for``` loop.

The following flow chart summarizes the flow control for the ```for``` loop:

![For Flowchart]({{ "/gwu/sp19/cs1012/assets/fordiscussion/for_flowchart.png" | absolute_url }})

### The ```range()``` Object
We can iterate on a list composed of any data type; however, ```for``` loops very frequently iterate over a range of integers.  For example, the following code loops four times:

```python
for i in [0,1,2,3]:
    # Do some operations based on i
```

For loops over a list of integers, ```i``` is a very common name for a loop variable and ```i``` is often referred to as the _**index**_.  This convention is borrowed from [Sigma notation](https://en.wikipedia.org/wiki/Summation).

The ```0``` appearing at the beginning of the list above is very normal in computer science; however, the explanation for why computer scientists count from zero is beyond the scope of our discussion at the moment.  One point of confusion that often arises is the first element in the list corresponds to the ```0``` index.

Rather than hardcoding our list of integers for a ```for``` loop, we can use a ```range()``` object instead.  For example, the following code produces behavior equivalent to the code above:
```python
for i in range(4):
    # Do some operations based on i
```
Both of the above code examples will iterate over the values ```[0,1,2,3]```.

By combining ```for``` and ```range```, we can reduce the code for drawing our simple square from:

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

To:

```python
from turtle import *
length = 100
# Draw a square with edges of length
for i in range(4):
    forward(length)
    left(90)

done()
```

When ```range``` is specified with only one value inside the parenthesis, _e.g._ ```range(4)```, the value provided to range specifies the value before which to stop the range or how many values should be in the range.  The Python documentation describes this usage as ```range(stop)```.

```range``` can also be specified with up to three values, _e.g._ ```range(1,4,1)```.  The Python documentation describes this usage as ```range(start, stop[, step])```.  This usage should be interpreted as ```start``` is the first number in the range, ```stop``` is the value before which to stop the range, and ```step``` is an optional value specifying how to step across the sequence.

Even though the second form of range can accept three values, _i.e._ ```range(start, stop[, step])```, it will still work if only two are provided.  If we omit the optional ```step``` value, the range will increment by one for each value in the sequence.  For example, the following code will iterate over the values ```[1,2,3,4]```:
```python
for i in range(1,5):
    # Do some operations based on i
    print(i)
```

If we wish to loop over only even integers up to and including ten, we can specify the ```step``` value as ```2``` to increment by two each step:
```python
n = 10
for i in range(2,n+1,2):
    # Do some operations based on i
    print(i)
```

We can also use a negative value for ```step``` to count backwards:
```python
n = 10
for i in range(n,0,-1):
    # Do some operations based on i
    print(i)
```

> The ```range(start, stop[, step])``` form may seem a little weird.  It is likely that you will rarely need it; however, it does introduce two ideas: 1) there can be multiple forms of the same function and 2) some functions can have optional parameters, _e.g._ ```step```.  We will talk about this much more in depth when we take a closer look at functions.


[Python documentation on ```range()```](https://docs.python.org/3/library/stdtypes.html#ranges)
