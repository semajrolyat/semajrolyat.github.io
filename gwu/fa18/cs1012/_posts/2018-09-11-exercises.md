---
layout: post
title:  "Exercises"
date:   2018-09-11 00:00:00 -0400
schedule:   2018-09-11 00:00:00 -0400
categories: [preview]
docclass: "exercises"
gwclass: "cs1012"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Generalizing a Regular Polygon
We have seen that in drawing the square, we used the same operations multiple times:

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

Drawing the square is a process of repeatedly drawing an edge and then turning to prepare to draw the next edge.  We can reduce the code needed to draw a square by using a ```for``` loop along with the ```range``` function:
```python
from turtle import *
length = 100
# Draw a square with edges of length
for i in range(4):
    forward(length)
    left(90)

done()
```
A square is a regular polygon --- it is both equilateral and equiangular --- and drawing any regular polygon involves the same basic procedure.

The values used for the angles are determined by the fact that a square is by definition fully enclosed and has four sides of equal length (equilateral).  From this definition, we know a square must also have four angles, _i.e._ an angle between each pair of adjacent edges, of equal degree (equiangular).

The degree of the internal angle for a regular polydon is defined by the following formula:

>```internal angle = 180(1-2/n)``` where ```n``` is the number of sides.

Therefore, the internal angle for a square is computed as:

>```internal angle = 90 (degrees per angle) = 180(1/2) = 180(1-2/4)```

However, consider that in order to turn the turtle with the correct angle, the turtle **does not** turn along the internal angle but instead turns along the external angle.  The folloing image illustrates how the turtle must turn:

![Turtle turn angle in a regular polygon]({{ "/gwu/fa18/cs1012/assets/09_11_2018/polygon-angle.png" | absolute_url }})

This implies that to compute the external angle along which the turtle must turn, we change the internal angle formula to the following:

 >```external angle = 180 - 180(1-2/n)```

 which simplifies to:

 >```external angle = 360/n```

We can generalize the code for drawing a square a step further by computing the turn angle for the turtle, _i.e._ the external angle, using above formula:
```python
from turtle import *

length = 100
angle = 360 / 4
# Draw a square with edges of length
for i in range(4):
    forward(length)
    left(angle)
done()
```

**Question**: In the above code, we see the literal ```4``` repeated, but what does that ```4``` really represent?  If you gave ```4``` a name and treated it as a variable, what would you name it?  What type should that variable have?

## Exercises
Each exercise describes exactly what you must submit.  **DO NOT** submit individual files.  Save everything described into one folder, zip that folder, and submit the zip containing all files.

In your ```cs1012``` folder create a subfolder named ```09_11_2018```.  Save all of your work from today in this folder.  When you complete your work, zip the ```09_11_2018``` folder and submit it to blackboard.  These exercises are due before the next class.

You **MUST** include comments in your code.  If your code contains no comments, it is incomplete and will not receive credit.  Comments are as important to your code as the code itself.

#### Exercise 1 - Draw a Regular Polygon
Write a script using spyder to draw a regular polygon.  Save this script as ```polygon.py```.
Your script must take the length of an edge as user input and your script must also take the number of sides as user input.  Given these two values, use a ```for``` loop to draw the regular polygon specified by the user.

1. Run your script and provide ```100``` for the length of the side and ```3``` for the number of sides.  This should draw an equilateral triangle.  Take a screenshot of the drawing and save the image as ```triangle.png```
2. Run your script and provide ```50``` for the length of the side and ```6``` for the number of sides.  This should draw a regular hexagon.  Take a screenshot of the drawing and save the image as ```hexagon.png```
3. Run your script and provide ```25``` for the length of the side and ```8``` for the number of sides.  This should draw a regular octogon.  Take a screenshot of the drawing and save the image as ```octogon.png```

Submit ```polygon.py```, ```triangle.png```, ```hexagon.png``` and ```octogon.png```.

> This exercise will allow you to work with expressions, variables, types, user input, and the ```for``` loop using the ```range``` function.
