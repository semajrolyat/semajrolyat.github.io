---
layout: post
title:  "Lab"
date:   2019-09-4 00:00:00 -0400
schedule:   2019-09-4 00:00:00 -0400
categories: [GWU]
docclass: "lab"
gwclass: "cs1012"
term: "sp19"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

##

Lab 2 - Triangles & Circles


###Goals:
- Dive deeper into geometry using the **Turtle** package
- Draw a right triangle with **2** equal sides
- Draw a flower pattern using **circle()**
- Draw a diamond inside a circle

##

### Exercise 1 - Draw a right triangle with 2 equal sides

You may choose any length to make the triangle sides.

**Keep in mind:** In a right triangle, the **hypotenuse** will always be larger than the other two sides. How is this calculated? Pythagorean Theorem!
``` a² + b² = c² ```

What about inner angles?

**Keep in mind:** All inner angles in a triangle add up to **180°**. How can you use this information to draw a hypotenuse?

```exercise1.png``` should look like this:

![lab2ex1]({{ "/gwu/sp19/cs1012/assets/lab02/triangle.png" | absolute_url }})

##

### Exercise 2 - Flowered Circles


**New function:** ``circle(radius) ``

Remember how the ``forward(numPixels)`` function moved **numPixels**? This values is called a **parameter**, or **argument**.

The **radius** parameter in ``circle()`` refers to the number of pixels in the radius when drawing.

Try to call ``circle()`` with different values for the radius to get an idea for the function.

For exercise 2, you will draw a flower pattern this this:

![lab2ex2]({{ "/gwu/sp19/cs1012/assets/lab02/circles.png" | absolute_url }})


You **only** need the turtle commands you already know, as well as the new ``circle()`` function.

There **must** be 5 'petals' in the flower pattern.

**Hint:** look at (0,0). Notice that every circle touches at this point

##

### Exercise 3 - Diamond inside Circle

Using the turtle functions you already know, as well as ``circle``, you will draw a diamond circumscribed in a circle like this:

![lab2ex3]({{ "/gwu/sp19/cs1012/assets/lab02/diamond.png" | absolute_url }})


**keep in mind:** as you saw in exercise 2, calling ``circle()`` draws the circle starting from the edge, **90°** to the left of turtle's view direction.

**Hint:** The distance from one corner of the diamond to another is the same as the diameter of the circle.

##

###Deliverables:
- Your final submission will be ```netid_lab02.zip```
- This zip **must** contain:
  - **Python Scripts:** ```exercise1.py```, ```exercise2.py```, ```exercise3.py```
  - **Screenshots of output:** ```exercise1.png```,
```exercise2.png```, ```exercise3.png```