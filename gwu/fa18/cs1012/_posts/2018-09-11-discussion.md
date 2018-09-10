---
layout: post
title:  "For Loop"
date:   2018-09-11 00:00:00 -0400
schedule:   2018-09-11 00:00:00 -0400
categories: [preview]
docclass: "discussion"
gwclass: "cs1012"
reading: "HtTLaCS 2.4-2.7"
exercises: "/gwu/fa18/cs1012/preview/2018/09/11/exercises.html"
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

Programmers generally seek to reduce the overall amount of code.  We do this to limit the possiblity of introducing bugs and to generalize code wherever possible. Less code promotes _reliability_ and generalization promotes _reusabiltiy_.

Programming languages provide structures that allow code to loop or _iterate_ over one or more statements so that those actions can be performed a number of times.  Python has multiple ways to loop; however, the most widely used and fundamental type of loop is called a ```for``` loop.

> As a rule of thumb, you will probably write 100 ```for``` loops for any other type of loop you might consider.

For example, we can write a Python ```for``` loop to print out the contents of a list:
```python
for student in ["Elise", "Charlie", "Bob", "Alice", "David"]:
    print("Welcome", student, "to Introduction to Programming with Python")
```

The Python ```for``` loop operates on a list.  In the above example:
* The list is specified by the strings inside the square brackets, _i.e._ ```[``` and ```]```, so the list contains the strings ```["Elise", "Charlie", "Bob", "Alice", "David"]```.
* The variable ```student``` is called the _loop variable_ and contains the name from the list that is currently being operated on.  Each item in the list will be assigned to the loop variable once in the order that they appear from left to right.
* The line where the loop is defined must end in a colon ```:```
* Everything inside the body of the loop --- beginning at the ```print``` statement --- must be indented.  **Indentation is important in Python**.
* When the bottom of the loop body is reached, the interpreter will jump back up to the ```for``` statement and assign the next item in the list to loop variable.
* The _terminating condition_ for a loop determines when the loop ends.  In a ```for``` loop, the terminating condition occurs when the end of the list is reached.
* When the terminating condition is reached, the loop terminates and the loop body is bypassed and the interpreter jumps to the next statement following the loop body.


### Control Flow
Without special instructions, the Python interpreter will process a script line-by-line from top to bottom, or _sequential_.  Certain keywords allow a programmer to change this behavior and control the _flow of execution_  --- the terms _control flow_ and _branching_ are synonyms for "flow of execution".  Through control flow, we can jump back up to an earlier statement or choose to optionally process statements.  We will talk more about other ways to control the flow of execution soon, but for now, we will focus on the ```for``` loop.

![For Flowchart]({{ "/gwu/fa18/cs1012/assets/09_11_2018/for_flowchart.png" | absolute_url }})
