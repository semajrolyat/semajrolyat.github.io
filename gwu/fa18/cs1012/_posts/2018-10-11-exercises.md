---
layout: post
title:  "Exercises"
date:   2018-10-11 00:00:00 -0400
schedule:   2018-10-11 00:00:00 -0400
categories: [GWU]
docclass: "exercises"
gwclass: "cs1012"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Exercises
Each exercise describes exactly what you must submit.  **DO NOT** submit individual files.  Save everything described into one folder, zip that folder, and submit the zip containing all files.

In your ```cs1012``` folder create a subfolder named ```10_11_2018```.  Save all of your work from today in this folder.  When you complete your work, zip the ```10_11_2018``` folder and submit it to blackboard.  These exercises are due before the next Tuesday class.

You **MUST** include comments in your code.  If your code contains no comments, it is incomplete and will not receive credit.  Comments are as important to your code as the code itself.

#### Exercise 1 - Modeling the ```for``` loop with a ```while``` loop
Let's model a ```for``` loop using a ```while``` loop.  Previously, we created the summation function.  Recall that the summation process was modeled with the following code:
```python
x = 0.0
dx = 0.0001
for i in range(10000):
  x = x + dx
```
And the summation function was defined by the following definition:
```python
def summation(start, step, iterations):
```

Rewrite the summation function using a ```while``` loop instead of a ```for``` loop and save this script as ```sumusingwhile.py```

Test your summation function using the following main program:

```python
# Add together 0.1 10 times
print(summation(0.0,0.1,10))
# Add together 0.0001 10,000 times
print(summation(0.0,0.0001,10000))
# Add together 0.00000001 100,000,000 times
# Note: this will be slow
print(summation(0.0,0.00000001,100000000)
```

Your program should produce output similar to the following:
```
0.9999999999999999
0.9999999999999062
1.0000000022898672
```

Submit ```sumusingwhile.py```

#### Exercise 2 - Using ```break```
Write a script that contains an infinite ```while``` loop.  Use an accumulator ```i``` to count each iteration of the ```while``` loop.  Before the loop, initialize ```i``` to zero and at the top of the loop body increment ```i``` by 1.

Inside the loop, generate an integer random number in the interval ```[0,100]``` and store the value that is randomly generated in a variable named ```x```.  If ```x``` is equal to a desired value of ```50```, break the loop using the ```break``` statement.  After the loop, print ```x``` to show how many iterations of the loop were required until the desired value was generated.

Save this script as ```usingbreak.py``` and submit it.

#### Exercise 3 - Using ```continue```
Write a script that uses a ```while``` loop to sum all odd numbers between 0 and 100.  We could implement this loop using either a ```for``` loop or a ```while``` loop; however, this exercise must be implemented using a ```while``` loop.  Print the answer only when the ```while``` loop exits.

Save this script as ```usingcontinue.py```

In this exercise, you must use ```continue```.  Inside your ```while``` loop, check to see if the counter variable is even.  If the counter is even, then ```continue```; otherwise, add the counter variable to the accumulated sum.

In other words, inside the ```while``` loop, your code should use the following conditional pattern:
```python
if i_IS_EVEN:
  continue
sum = sum + i
```
> Note that if the ```if``` conditional is ```True```, the remaining code in the body of the loop is unreachable due to the ```continue``` statement.  Even though we do not have an ```else``` statement, we have created an implicit ```else``` by using ```continue```.

Submit ```usingcontinue.py```
