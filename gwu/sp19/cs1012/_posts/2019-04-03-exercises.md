---
layout: post
title:  "Exercises"
date:   2019-04-03 00:00:00 -0400
schedule:   2019-04-03 00:00:00 -0400
categories: [GWU]
docclass: "exercises"
gwclass: "cs1012"
term: "sp19"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Exercises 8

### Due Date
**The solutions to these exercises must be submitted by the end of the day.**

### Instructions

You are allowed to collaborate with your neighbor on these exercises.  Each of you must complete the programming tasks individually; however, you are encouraged to discuss and work together to design a solution to the problems.

Before beginning, make sure to create a new folder named ```exercises08``` in your class folder.

Create a .zip archive containing all of your code files and any written solutions and submit the .zip archive to blackboard as your solutions to these exercises.

You **MUST** include comments in your code.  For each function, you must also provide a block comment that precedes the function and describes every input to the function if it accepts any parameters, what the function does, and what the function returns if it returns a value.  If your code contains no comments, it is incomplete and will not receive credit.  Comments are as important to your code as the code itself.  You must include a comment in the header portion of the file that summarizes what the program does.  You must include comments inline with code to describe the steps in natural language.

#### Exercise 1 - Averaging a list of integers
Create a file named ```exercise1.py```.

Write a function that computes the average of a list of numbers.

Your function must have the following definition where ```l``` is the list to average, and your function must compute and return the _**floating point**_ average of the list:
```python
def average(l):
```

Test your function with the following cases in a main program:

1. Create a list containing the integers in the range [1,9], pass the list to the ```average``` function, and print the value that is returned from the function.
2. Generate a list of 100 random integers in the range [0, 1000] using the random module.  You will need to use append to append integers to the list.  Pass this list of random numbers to the ```average``` function and print the value that is returned from the function.

Submit ```exercise1.py```.

#### Exercise 2 - Count words of a specific length in a list of strings
Create a file named ```exercise2.py```.

In this exercise, you will write a function that counts the number of words in a list that are of a specified length.

Your function must have the following definition where ```l``` is the list of words to evaluate and ```sz``` is the length of the words to count, and your function must return the total number of words in the list that have that length:
```python
def countwords(l, sz):
```

Test your function using the following main program:

```python
# validate that countwords returns zero if no words in set share length
words = ["hi", "me", "you", "they", "day", "night", "week", "hour", "hello", "class", "home", "work", "relax"]
r = countwords(words,1)
if r != 0:
  print("countwords(...) failed to properly count words of length 1.  Expected 0 instead returned " + str(r))

# validate that countwords returns the expected value for words in the set that do share that length
r = countwords(words,4)
if r != 5:
  print("countwords(...) failed to properly count words of length 4.  Expected 5 instead returned " + str(r))

r = countwords(words,5)
if r != 4:
  print("countwords(...) failed to properly count words of length 5.  Expected 4 instead returned " + str(r))

print("Test completed")
```

If your program produces any output other than:
```
Test completed
```
You have an error in ```countwords``` and you will need to debug your function.

Submit ```exercise2.py```.

#### Exercise 3 - Find the position of a sub-sequence in a sequence
Create a file named ```exercise3.py```.

Write a function that finds the starting position of a smaller sub-sequence within another sequence using slicing.  If the sub-sequence is found, your function will return the starting position of where the sub-sequence appears within the sequence that is searched.  If the sub-sequence is not found, return ```-1``` to indicate that the operation failed to find the sub-sequence within the sequence that is searched.

> Above the general term 'sequence' is used, but you can just think of this as list which is reflected in the change to the term 'list' below.  If your function is written using slicing, it the specific type of sequence operated on is irrelevant as they all use the same slicing nomenclature.  

Your function must have the following definition where ```haystack``` is the list to search and ```needle``` is the sub-list to search for, and your function must return either the position of ```needle``` in ```haystack``` if ```needle``` is found or ```-1``` if ```needle``` is not found:

```python
def find(haystack, needle):
```

Remember that you must solve this problem using slicing.

Test your function with the following main program:

```Python
# validate that find will locate a sublist that exists in a list
l = [0,1,2,3,4,5,6,7,8,9,10]
r = find(l,[9,10])
if r != 9:
  print("find(...) failed to find the list [9,10] in " + str(l))

# validate that find will not locate a sublist that does not exist
r = find(l,[2,1])
if r != -1:
  print("find(...) found the list [2,1] in " + str(l))

# validate that find will locate a substring that exists in a string
l = "abcdefghijklmnopqurstuvwxyz"
r = find(l,"mno")
if r != 12:
  print("find(...) failed to find the string 'mno' in " + l)

# validate that find will locate a subtuple that exists in a tuple
l = (0,1,2,3,4,5,6,7,8,9,10)
r = find(l,(9,10))
if r != 9:
  print("find(...) failed to find the tuple (9,10) in " + str(l))

print("Test completed")
```

Submit ```exercise3.py```.
