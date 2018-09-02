---
layout: post
title:  "Variables"
date:   2018-08-28 00:00:00 -0400
schedule:   2018-08-30 00:00:00 -0400
categories: [GWU, CS1012]
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Review

### Scripts

## Introduction
So far, we have issued Python Turtle commands using fixed numbers.  For example, the following python script draws a square 100 units on a side:
{% highlight python %}
from turtle import *
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
done()
{% endhighlight %}
Any time you write a number (or a _string_) into a program, that value is called a _literal_ and is sometimes described as being a value that is _hardcoded_ into the program.  In the above example, we use the literal 100 for the length of a side and the literal 90 for the angle of the turn.
> We will define what the term "string" means later.  The term "hardcoded" implies that the value cannot be changed once the program is started.

We can accomplish a lot using literals and they are necessary; however, if we only use literals, it will be difficult to modify the program later to draw a square of any size other than 100 units.  

> Programmers strive to reuse software as much as possible.  Generalization promotes code reuse, reduces the size of code, and is a fundamental principle of programming. Less code is usually better because there is less opportunity to make a mistake.

Instead of hardcoding 100 as the length of a side, we can use a _variable_ insted.  Compare the following python script to the preceding python script:

{% highlight python %}
from turtle import *
length = 100
forward(length)
left(90)
forward(length)
left(90)
forward(length)
left(90)
forward(length)
done()
{% endhighlight %}

**Question**: Do these two python scripts produce drawings that are equivalent?

## Variables

### Variable Assignment

## Expressions

## Exercises

## Reflection
