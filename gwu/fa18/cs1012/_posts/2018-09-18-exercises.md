---
layout: post
title:  "Exercises"
date:   2018-09-18 00:00:00 -0400
schedule:   2018-09-18 00:00:00 -0400
categories: [GWU]
docclass: "exercises"
gwclass: "cs1012"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Exercises
Each exercise describes exactly what you must submit.  **DO NOT** submit individual files.  Save everything described into one folder, zip that folder, and submit the zip containing all files.

In your ```cs1012``` folder create a subfolder named ```09_18_2018```.  Save all of your work from today in this folder.  When you complete your work, zip the ```09_18_2018``` folder and submit it to blackboard.  These exercises are due before the next class.

You **MUST** include comments in your code.  If your code contains no comments, it is incomplete and will not receive credit.  Comments are as important to your code as the code itself.

#### Exercise 1 - Summation Function
Write a function with the definition ```sum_to(n)``` that returns the sum of all integers up to and including ```n```.  Save this script as ```sum_to.py```.

Your main program should be:
```python
print(sum_to(10))
print(sum_to(50))
print(sum_to(100))
```
The output from this script should be:
```
55
1275
5050
```

Submit ```sum_to.py```.

#### Exercise 2 - Regular Polygon Function
Recall in the previous exercises we implemented a script to draw a regular polygon.  Save this script as ```polyfun.py```.

In this exercise, you will implement a function to do draw a regular polygon.  This function should have the following declaration:

```python
def polygon(sides,length):
```

Given the above declaration, this function should draw a regular polygon where the ```sides``` parameter specifies the number of sides for the polygon and ```length``` specifies the length of a single side.

In the main body of the script, use the following code to draw three polygons on the screen:
```python
polygon(3,100)
polygon(6,50)
polygon(8,25)
```

Run your script and take a screenshot of the output.  Save this screenshot as ```polyfun.png```.

Submit ```polyfun.py``` and ```polyfun.png```.

#### Exercise 3 - Inset Squares
Write a program to draw ten squares inset into one another.  Save this script as ```insetsquares.py```.

Assume that the length of a side for the innermost square is 20 units and each successive square is 20 units larger than the previous square.  This script should center the squares.  The output of this program should look like the following image.

![Inset Squares Output]({{ "/gwu/fa18/cs1012/assets/09_18_2018/insetsquares.png" | absolute_url }})

Run your script and take a screenshot of the output.  Save this screenshot as ```insetsquares.png```.

Submit ```insetsquares.py``` and ```insetsquares.png```.

>Hint: You will probably want a function to draw a square and a function to reposition the turtle without drawing.
