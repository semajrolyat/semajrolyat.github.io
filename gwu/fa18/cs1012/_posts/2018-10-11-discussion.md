---
layout: post
title:  "While Loops and Loop Control"
date:   2018-10-11 00:00:00 -0400
schedule:   2018-10-11 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
reading: "HtTLaCS 9.1-9.14 (and 9.15-9.19)"
exercises: "/gwu/fa18/cs1012/2018/10/11/exercises.html"
term: "fa18"

---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

### Looping Control Structures
We have already discussed the ```for``` loop control structure which gives us the ability to iterate a number of times.  The ```for``` loop is the most widely used loop control structure because many times we know in advance that we will be iterating over a known range of numbers or on a data structure with a fixed size.

We have also studied variants of the ```if``` conditional which allows us to optionally branch the normal sequential flow of a Python script.

In addition to the ```for``` loop, we have a conditional loop structure that is defined using the ```while``` keyword.  A ```while``` loop has a structure that is more similar to the ```if``` conditional than the ```for``` structure.  The ```while``` loop has the following structure:
```python
while BOOLEAN_EXPRESSION:
    STATEMENTS
```

The following flow chart models the ```while``` control structure:
![While Flowchart]({{ "/gwu/fa18/cs1012/assets/10_11_2018/while.png" | absolute_url }})


If ```BOOLEAN_EXPRESSION``` evaluates as ```True```, then ```STATEMENTS``` will be executed.  Once the end of the loop body is reached, the process will go back up to the ```while``` statement and reevaluate ```BOOLEAN_EXPRESSION```.  If ```BOOLEAN_EXPRESSION``` is reevaluated as ```True``` the loop body will be processed again.  This behavior will repeat until some case inside ```STATEMENTS``` changes the state of the system such that ```BOOLEAN_EXPRESSION``` is evaluated as ```False```.  However, ```BOOLEAN_EXPRESSION``` will only be reevaluated when the process reaches the end of all statements inside the loop body.  For example, the following ```while``` loop will loop until ```x > 1000```:

```python
x = 1
while x < 1000:
  x = x * 2
```

A ```while``` loop can iterate an infinite number of times which is often called an _**inifinte loop**_, meaning that the loop will never terminate.  While it is possible, it is generally difficult to inadvertantly create an infinite ```for``` loop.  A programmer must be very careful and make sure that the logic that controls a terminating condition is correctly implemented when working with a ```while``` loop.

### ```for``` Is a ```while``` Loop
We can easily model the ```for``` loop using a ```while``` loop, and in actuality, a ```for``` loop is really a ```while``` loop underneath the hood.  Consider the following ```while``` loop example:

```python
i = 0
while i < 10:
  STATEMENTS
  i = i + 1
```
The above ```while``` loop achieves the same behavior as the following ```for``` loop example:
```python
for i in range(10):
  STATEMENTS
```
The ```for``` structure was introduced because most of the loops we create iterate over a finite range.  The ```for``` structure neatly encapsulates all of the logic necessary to achieve these types of loops and eliminates the possibility of a programmer forgetting a critical component like incrementing the loop variable ```i```.

> You will likely write 100 ```for``` loops for every ```while``` loop you might write, so most iterative problems will likely involve writing a ```for``` loop.  However, the ```while``` loop is capable of evaluating general conditional logic so it is more flexible and is more likely to be used if the number of iterations is indefinite.  Many problems deal with gathering an indefinite amount of data; however, once we have gathered the data, we generally know how many iterations are necessary.  The book has a contradictory stance and suggests that ```while``` loops are quite common.

### Nested Loops
Just like we could nest ```if``` statements and we can call a function from inside another function, we can also nest loops within one another.  For example, we can nest a ```for``` loop inside another ```for``` loop:

```python
for i in range(x):
  I_STATEMENTS1
  for j in range(y):
    J_STATEMENTS
  I_STATEMENTS2
```
We can nest ```while``` loops:
```python
i = 0
while(i < x):
  I_STATEMENTS1
  j = 0
  while(j < y):
    J_STATEMENTS
    j = j + 1
  I_STATEMENTS2
  i = i + 1
```
Or we can mix and match loop types:
```python
i = 0
while(i < x):
  I_STATEMENTS1
  for j in range(y):
    J_STATEMENTS
  I_STATEMENTS2
  i = i + 1
```


### ```break```
The ```break``` keyword allows a loop, _i.e._ ```for``` or ```while```, to break out of the loop without reaching its terminating condition.  When a ```break``` statement is encountered, the program immediately jumps to the end of the current loop body and the program proceeds from that line.

```python
x = 1             # initialize the accumulator
for i in range(1,100):
  x = x * i       # do some computation
  if x > 1000:    # if the computation exceeds some limit
    break         #    then break out of the loop
```
Recall that we can express the same problem using a ```while``` loop which may be more fitting given the nature of the terminating condition:
```python
x = 1             # initialize the accumulator
i = 1             # initialize the loop variable (this was automatic in the for loop)
while(x < 1000):  # models the if statement in the above for loop
  x = x * i       # do some computation
  i = i + 1       # don't forget to increment the loop variable
```
Or we could more faithfully model the original ```for``` loop with the following ```while``` loop:
```python
x = 1             # initialize the accumulator
i = 1             # initialize the loop variable (this was automatic in the for loop)
while(i < 100):   # this is the same terminating condition as the above for loop
  x = x * i       # do some computation
  i = i + 1       # don't forget to increment the loop variable
  if x > 1000:    # if the computation exceeds some limit
    break         #    then break out of the loop
```

If a ```break``` statement is encountered in a nested loop, the ```break``` will only ```break``` out of the loop body in which it is located, meaning that if the ```break``` is inside the inner loop, the program will jump to the end of the inner loop and will then begin interpreting any statements in the outer loop.  For example:

```python
for i in range(100):
  for j in range(100):
    break         # breaks only the inner j loop
```

In order to break both loops, you may need to include additional logic.  For example:
```python
done = False      # a boolean that overrides the stop condition for both loops
for i in range(100):
  for j in range(100):
    if j == 50:
      done = True # set the override condition
      break       # breaks only the inner j loop
  if done:        # check the override condition
    break         # if the override condition is True then break the outer i loop
```

### ```continue```
A ```continue``` statement allows the loop to skip the rest of the loop body and immediately jump back up to the top of the loop.  For example:
```python
x = 0
for i in range(100):
  if i >= 10 and i <= 20:
    continue      # skip the rest of the loop if i is between 10 and 20
  x = x + i
```

```continue``` is valuable when we will only operate on some elements in a set.  We will discuss this concept in more detail later.  For now, just remember that ```continue``` instructs Python to immediately jump back to the top of the loop in which the ```continue``` appears, and if the loop is a ```for``` loop, then the loop variable is updated to the next element in the list.

### A "main loop"
Many programs will run through a number operations repeatedly until an exit condition arises.

For example, suppose you write a program that reads inputs until the user types an input that reads "exit".  You cannot predict when the user will type "exit" and your program must keep reading inputs until that condition arises.  Your program must loop to keep taking input until the exit condition is read.  Because there is no way to predict how many iterations the program must make, the correct looping structure to use is a ```while``` loop.

Programs that share similar to the above hypothetical program contain what is called a "main loop".  In this case, an infinite loop is called for and they are typically structured in the following way:
```python
while(True):
  MAIN_PROGRAM_STATEMENTS
```

When will the above loop exit?  Never according to the loop's terminating condition; however, this does not mean that it is impossible to terminate the loop.  Recall that ```break``` stops the loop and causes the program to jump down below the loop body.  We can use an ```if``` statement that contains a ```break``` statement to terminate the loop.  For example, the following is an example of the hypothetical program described above.

```python
while(True):      # the main loop will loop forever
  s = input("Enter a string (type exit to quit): ")
  print(s)
  if s == "exit": # check for the exit condition
    break         # break out of the loop
```

This program will repeatedly ask the user for input and will only exit if the user inputs exactly "exit".  The loop is designed to loop forever; however, it is still possible to break out of the loop if the exit condition arises.
