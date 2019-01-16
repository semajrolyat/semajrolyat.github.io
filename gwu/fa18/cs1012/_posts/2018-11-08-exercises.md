---
layout: post
title:  "Exercises"
date:   2018-11-08 00:00:00 -0400
schedule:   2018-11-08 00:00:00 -0400
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

In your ```cs1012``` folder create a subfolder named ```11_08_2018```.  Save all of your work from today in this folder.  When you complete your work, zip the ```11_08_2018``` folder and submit it to blackboard.  These exercises are due before the next Tuesday class.

You **MUST** include comments in your code.  If your code contains no comments, it is incomplete and will not receive credit.  Comments are as important to your code as the code itself.

#### Exercise 1 - Remove all instances of a character from a string
In this exercise, you will write a function that removes all instances of a character from a string and returns the resulting string.

Your function must have the following definition where ```s``` is the string to remove characters from and ```c``` is the character to remove from ```s```, and your function must return the string without any instances of ```c```:
```python
def trimchar(s, c):
```

Save this script as ```trimchar.py```

Test your function using the following main program:

```python
print(trimchar('Hello World!','l'))
print(trimchar('Introduction to programming with python','o'))
print(trimchar('HtTLaCS is short for "How to Think Like a Computer Scientist"','T'))
```

Your program should produce the following output:
```
Heo Word!
Intrductin t prgramming with pythn
HtLaCS is short for "How to hink Like a Computer Scientist"
```

Submit ```trimchar.py```

#### Exercise 2 - Averaging a list of integers
In this exercise, you will write a function that computes the average of a list of numbers.

Your function must have the following definition where ```l``` is the list to average, and your function must compute and return the _**floating point**_ average of the list:
```python
def average(l):
```

Save this script as ```average.py```

Test your function with the following cases in a main program:

1. Create a list containing the integers in the range [1,9], pass the list to the ```average``` function, and print the value that is returned from the function.
2. Generate a list of 100 random integers in the range [0, 1000] (You will need to use append).  Pass this list of random numbers to the ```average``` function and print the value that is returned from the function.

Submit ```average.py```.

#### Exercise 3 - Count words
In this exercise, you will write a function that counts the number of words in a list that are of a specified length.

Your function must have the following definition where ```l``` is the list of words to evaluate and ```sz``` is the length of the words to count, and your function must return the total number of words in the list that have that length:
```python
def countwords(l, sz):
```

Save this script as ```countwords.py```

Test your function using the following main program:

```python
words = ["hi", "me", "you", "they", "day", "night", "week", "hour", "hello", "class", "home", "work", "relax"]
print(countwords(words,1))
print(countwords(words,4))
print(countwords(words,5))
```

Your program should produce the following output:
```
0
5
4
```

Submit ```countwords.py```.
