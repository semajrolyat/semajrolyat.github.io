---
layout: post
title:  "Exercises"
date:   2018-10-02 00:00:00 -0400
schedule:   2018-10-02 00:00:00 -0400
categories: [GWU]
docclass: "exercises"
gwclass: "cs1012"
term: "fa18"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Exercises
Each exercise describes exactly what you must submit.  **DO NOT** submit individual files.  Save everything described into one folder, zip that folder, and submit the zip containing all files.

In your ```cs1012``` folder create a subfolder named ```10_02_2018```.  Save all of your work from today in this folder.  When you complete your work, zip the ```10_02_2018``` folder and submit it to blackboard.  These exercises are due before the next class.

You **MUST** include comments in your code.  If your code contains no comments, it is incomplete and will not receive credit.  Comments are as important to your code as the code itself.

#### Exercise 1 - Boolean Logic
In a file named ```booleanlogic.txt```, write logical expressions for the following questions:

1. Write logical expressions that evaluate to ```True``` if the following conditions are ```True```.
   1. ```x``` is negative.
   2. ```y``` is between ```5``` and ```10``` inclusively.
   3. ```z``` is either positive or negative.
2. Write logical expressions that evaluate to ```False``` if the following conditions are ```True```:
   1. ```a``` is equal to one of the following values: ```3```, ```4```, ```5```
   2. ```b``` is between ```2``` and ```8``` inclusively
   3. ```c``` is non-negative
3. Write logical expressions that are logical opposites of the following _**without**_ using the not operator:
   1. ```x < 20```
   2. ```y >= 5```
   3. ```z > 2 and z <= 12```
   4. ```p <= 0 or q > 10```

Submit ```booleanlogic.txt```

#### Exercise 2 - Computing Leap Years
3 criteria must be taken into account to identify leap years:
* The year is evenly divisible by 4;
* If the year can be evenly divided by 100, it is NOT a leap year, unless;
* The year is also evenly divisible by 400. Then it is a leap year.

Write a script based on the above algorithm and implement a function that checks whether a year is a leap year with the following signatures:
```python
def is_leap(year):
```
```is_leap``` will return ```True``` if ```year``` is a leap year; otherwise, ```is_leap``` returns ```False```.

Test your script with the following main program:
```python
# 1900 is evenly divisible by 100 but not by 400
print(1900, is_leap(1900))
# 1900 is evenly divisible by 100 and by 400
print(2000, is_leap(2000))
# 2001 is not evenly divisible by 4
print(2001, is_leap(2001))
# 2016 is evenly divisible by 4
print(2016, is_leap(2016))
# 2018 is not evenly divisible by 4
print(2018, is_leap(2018))
```
The main program should produce the following output:
```
1900 False
2000 True
2001 False
2016 True
2018 False
```

Save this script as ```leapyear.py```


#### Exercise 3 - Equality for Floating Points
We have established that floating points are inaccurate with the following example.

```python
x = 0.0
dx = 0.0001
for i in range(10000):
  x = x + dx
print(x == 1.0)
print(x)
```
```
False
0.9999999999999062
```

Given the above summation of ```x```, how can you check to see if the result of the summation is approximately equal to ```10.0```?

> Hint: You should check the error between ```x``` and the desired value.

Write a script based on the above Python code and implement two functions with the following signatures:
```python
def summation(start, step, iterations):
def is_equal(actual, expected, epsilon=1e-12):
```
Save this script as ```fpequality.py```

```summation``` computes a summation over a number of iterations just like the sample that was provided and returns the total sum.  In the example, ```start``` is the initial value assigned to the accumulator, ```step``` is amount that is added to the accumulator each iteration, and ```iterations``` is the number of iterations over which to sum.  Unlike the example code, ```summation``` should not print inside the body of the function.

> Note: The ```summation``` operation models how we would integrate in code.

```is_equal``` returns ```True``` if ```actual``` and ```expected``` are approximately equal to one another and otherwise returns ```False```.  The optional parameter ```epsilon``` represents the error tolerance of the comparison.

> The floating point absolute value function from the math module is named ```fabs```.

In your main program call ```summation``` and ```is_equal``` repeatedly and print the results using the following code:
```python
# Analytically all of these should be equivalent to 1.0
y = 1.0
# Add together 0.1 10 times
result = summation(0.0,0.1,10)
print(is_equal(result, y), result, y)
# Add together 0.0001 10,000 times
result = summation(0.0,0.0001,10000)
print(is_equal(result, y), result, y)
# Add together 0.00000001 100,000,000 times
# Note: this will be slow
result = summation(0.0,0.00000001,100000000)
print(is_equal(result, y), result, y)
```

Your program should produce output similar to the following:
```
True 0.9999999999999999 1.0
True 0.9999999999999062 1.0
False 1.0000000022898672 1.0
```

Submit ```fpequality.py```
