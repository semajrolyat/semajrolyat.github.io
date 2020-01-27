---
layout: post
title:  "For Loops"
date:   2020-02-03 00:00:00 -0400
schedule:   2019-02-03 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
reading: "HtTLaCS 7.1-7.8 & 8.1-8.7"
term: "sp20"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

### Iteration
The code we have so far written to draw a square consists of the same instructions repeated multiple times:

```python
x = 100
forward(x)
left(90)
forward(x)
left(90)
forward(x)
left(90)
forward(x)
left(90)
```

There is a clear pattern in this code and we would like to reduce it if possible.

Programmers generally seek to reduce the overall amount of code.  We do this to limit the possibility of introducing bugs and to generalize code wherever possible. Less code promotes _**reliability**_ and generalization promotes _**reusability**_.

> Why does code reduction promote reliability?  If we copy code, we may not recognize that it is necessary to change code in multiple locations to fix a problem.  Code complexity creates more places for bugs to hide and repetitious code is a form of complexity.  

Programming languages provide structures that allow code to loop or repeat over one or more statements so that those actions can be performed a number of times.  We call repeating over the same statements a number of times _**iteration**_ or _**to iterate**_.  Python has multiple ways to loop; however, the most widely used and easiest to use is a fundamental type of loop called a ```for``` loop.

> As a rule of thumb, you will probably write 100 ```for``` loops for any other type of loop you might consider, and in Python, you might write 1000 ```for``` loops before considering another approach.

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
* Everything inside the body of the loop --- beginning at the ```print``` statement --- must be indented.  **In Python, indentation defines a block of code and is very important**.
* When the bottom of the loop body is reached, the Python interpreter will jump back up to the ```for``` statement and assign the next item in the list to loop variable.
* The _**terminating condition**_ for a loop determines when the loop ends.  In a ```for``` loop, the terminating condition occurs when the end of the list is reached.
* When the terminating condition is reached, the loop terminates, the loop body is bypassed, and the interpreter jumps to the next statement following the loop body.


### Control Flow
Without special instructions, the Python interpreter will process a script line-by-line from top to bottom, or _**sequentially**_.  Certain keywords allow a programmer to change this behavior and control the _**flow of execution**_  or the program _**control flow**_.   The terms _**iteration**_ and _**branching**_ are forms of control flow.  Through control flow, we can jump back up to an earlier statement, iteration, or choose to optionally process statements, branching.  We will talk more about other ways to control the flow of execution soon, but for now, we will focus on iteration using the ```for``` loop.

The following flow chart summarizes the flow control for the ```for``` loop:

![For Flowchart]({{ "/gwu/fa19/cs1012/assets/discussion04/for_flowchart.png" | absolute_url }})



### The ```range()``` Object
We can iterate on a list composed of any data type; however, ```for``` loops very frequently iterate over a range of integers.  For example, the following code loops four times:

```python
for i in [0,1,2,3]:
    # Do some operations based on i
```

In the above example, the loop variable ```i``` is initially assigned the value of ```0```.  Each time the loop finishes, ```i``` is assigned the next value in the list.  If there are no more items in the list, the loop bypasses the loop body and the program continues sequentially until it reaches either the end of the program and exits or another control flow element modifies the flow of execution.

For loops over a list of integers, ```i``` is a very common name for a loop variable and ```i``` is often referred to as the _**index**_.  This convention is borrowed from [Sigma notation](https://en.wikipedia.org/wiki/Summation).  Additionally, we often think of the number of times the loop iterates to be ```n``` which is also borrowed from Sigma notation.

The ```0``` appearing at the beginning of the list above is very normal in computer science; however, the explanation for why computer scientists count from zero is beyond the scope of our discussion at the moment.  One point of confusion that often arises is the first element in the list corresponds to the ```0``` index.  Because we count from ```0```, we typically count up to ```n-1``` which means that the loop iterates ```n``` times.

> If we count from ```1``` we would count up to and include ```n``` to iterate ```n``` times.  Because we subtract one from our starting number, _i.e._ we start at ```0``` not ```1```, we also subtract one from our ending number to ensure that we count only ```n``` times.  Therefore, programmers typically count from ```0``` to ```n-1```.

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
left(90)

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

> Note that by using the loop, we have the repetitive process that required eight lines of code is reduced to three lines on code instead.

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
for i in range(2, n+1, 2):
    # Do some operations based on i
    print(i)
```

We can also use a negative value for ```step``` to count backwards:

```python
n = 10
for i in range(n, 0,-1):
    # Do some operations based on i
    print(i)
```

> The ```range(start, stop[, step])``` form may seem a little weird.  It is likely that you will rarely need it for a ```for``` loop; however, it does introduce two ideas: 1) there can be multiple forms of the same function and 2) some functions can have optional parameters, _e.g._ ```step```.  We will talk about this much more in depth when we take a closer look at functions.  It also introduces a pattern that models how we slice lists which will be very important when we start to look at large data sets.

[Python documentation on ```range()```](https://docs.python.org/3/library/stdtypes.html#ranges)

### The Accumulator Pattern
As suggested above, the notations ```i``` and ```n``` are borrowed from Sigma notation which is describes summation over a large number of elements.  We fulfill this mathematical model using the _**accumulator**_ pattern inside a loop.  An accumulator is simply a variable that is reassigned repeatedly to itself combined with some mathematical operation inside a loop.  For example:

```python
x = 0
for i in range(10):
  x = x + i        # x is an accumulator
```

In the above example, ```x``` is an accumulator.  Each pass through the loop, the value of ```x``` is updated, _i.e._ reassigned, with the "running total" of the summation and the process adds all the numbers between in the interval [0,9] and computes and stores the summation in ```x```.  

Note that before the loop begins, the accumulator is assigned an initial value to establish the variable ```x```.  If ```x``` is not assigned a value before the loop begins, then the right side of the assignment in the accumulation step, _i.e._ the ```x + i``` part of ```x = x + i```, is illegal because ```x``` would be unknown.

Accumulators are not limited to summation; however, it is the most common form that accumulators are expressed in.