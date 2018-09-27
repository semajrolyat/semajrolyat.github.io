---
layout: post
title:  "Exercises"
date:   2018-09-25 00:00:00 -0400
schedule:   2018-09-25 00:00:00 -0400
categories: [GWU]
docclass: "exercises"
gwclass: "cs1012"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Exercises
Each exercise describes exactly what you must submit.  **DO NOT** submit individual files.  Save everything described into one folder, zip that folder, and submit the zip containing all files.

In your ```cs1012``` folder create a subfolder named ```09_25_2018```.  Save all of your work from today in this folder.  When you complete your work, zip the ```09_25_2018``` folder and submit it to blackboard.  These exercises are due before the next class.

You **MUST** include comments in your code.  If your code contains no comments, it is incomplete and will not receive credit.  Comments are as important to your code as the code itself.

#### Exercise 1 - Circle Functions
Write two functions, ```circumference(radius)``` and ```area_of_circle(radius)```.  Use your functions to compute the circumference and area of circles with radius 1, 5, and 10.  Save this script as ```circleops.py```.

Your main program should be:
```python
print("circumference(1):", circumference(1))
print("area_of_circle(1):", area_of_circle(1))

print("circumference(5):", circumference(5))
print("area_of_circle(5):", area_of_circle(5))

print("circumference(10):", circumference(10))
print("area_of_circle(10):", area_of_circle(10))
```
Your script should produce the following output
```
circumference(1): 6.283185307179586
area_of_circle(1): 3.141592653589793
circumference(5): 31.41592653589793
area_of_circle(5): 78.53981633974483
circumference(10): 62.83185307179586
area_of_circle(10): 314.1592653589793
```

Submit ```circleops.py```

#### Exercise 2 - Rolling a 2 dice
Write a script to simulate rolling 2 six-sided dice.  Save this script as ```dicethrow.py```

Write two functions named ```rolldie``` and ```roll2dice```.  ```rolldie``` takes no parameters and returns a random value in the range from 1 to 6.  ```roll2dice``` takes no parameters and returns no values; however, ```roll2dice``` prints the outcome of rolling two individual dice.

Your main program should test ```roll2dice``` by iterating 10 times and calling ```roll2dice``` each time.  Confirm that the outcome of each throw produces a pair of values with the total of each pair in the range of 2 to 12.

Submit ```dicethrow.py```

#### Exercise 3 - Generating Random Floating Point Numbers
Write a script that generates ten random floating point numbers between -20.0 and 20.0 and prints out each generated number.  Save this script as ```randomfloats.py```.

Write a function named ```randomfloat``` that takes a range as two parameters.  The definition for this function should be:

```python
def randomfloat(low,high):
```
```randomfloat``` generates a floating point value in the range of [low, high) and returns the generated value.  Your main program will iterate ten times, and each iteration, it will call ```randomfloat``` to generate a random number in the range of [-20.0,20.0) and print out the randomly generated value returned by ```randomfloat```.

Submit ```randomfloats.py```
