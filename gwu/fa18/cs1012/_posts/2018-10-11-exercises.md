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

## Warning
If you make a mistake with the design of a ```while``` loop, it is very easy to end up in an inifinte loop.  If this happens, your program will run forever.  It can be difficult to determine whether your program is looping in this way.

It is a good idea to include a print statement inside a ```while``` loop when initially designing a program so that you can see that it is not making progress.  We might call these debugging statements.  I'll note in these exercises where you might want to include a debugging statements.  When you have fully debugged your program, comment out any debugging statements so that they are not processed by the actual program.

If your program enters an infinite loop, you must interrupt the program so that it does not continue to run forever.  To interrupt a program in spyder, click in the interactive terminal (bottom right) and use the key combination ```Ctrl-C``` on Windows or Linux or use the key combination ```Cmd-C``` on OSX.  These key combinations send a command to your operating system to force the current program to quit in a terminal window.

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

> To debug your ```while``` loop, you should include a print statement inside the loop that prints out the loop index ```i``` each time through the loop.  I would recommend only testing the program initially using the first call to ```summation``` in the main program.  Once you have verified that the loop works properly, comment out the debug print statement and allow the program to compute all three summations in the main program.

Submit ```sumusingwhile.py```

#### Exercise 2 - Using ```break```
In this exercise, you will write a function that "guesses" a number that is provided as a parameter.  This function should contain an infinite loop as we cannot predict how many guesses are required.  Your function will have the following definition:

```python
def countguesses(target):
```

In order to guess, use the ```randint``` function from the ```random``` mondule.  ```randint(start, stop)``` works just like ```randrange(start,stop)```; however, the range for ```randint``` is inclusive for both the ```start``` and ```stop``` parameters.

In ```countguesses```, use a variable ```guess``` to accumulate the number of guesses.  Initialize ```guess``` to zero before the loop and increment ```guess``` at the top of the loop body.

Inside the loop body, generate a random integer in the interval ```[1,100]``` and store the random value in a variable named ```x```.  If ```x``` is equal to a desired value which is passed in as the parameter ```target```, break the loop using the ```break``` statement.

After the loop, return ```x``` as the answer to how many guesses/iterations were required to randomly generate a number equal to the ```target```.

Save this script as ```usingbreak.py```.

Your main program should look like this:
```python
target = 50
print("To guess", target, "took", countguesses(target), "random guesses")
target = 15
print("To guess", target, "took", countguesses(target), "random guesses")
target = 2
print("To guess", target, "took", countguesses(target), "random guesses")
```
The main program calls ```countguesses``` a number of times with different target values and prints out how many guesses were required for each attempt to guess a number.

When you run your program, it should produce output that looks like the following (The number of guesses will be different):
```
To guess 50 took 55 random guesses
To guess 15 took 141 random guesses
To guess 2 took 75 random guesses
```
> To debug your ```while``` loop, you should include a print statement inside the loop that prints out the loop index ```guess``` each time through the loop.  I would recommend only testing the program initially using the first call to ```countguesses``` in the main program.  Once you have verified that the loop works properly, comment out the debug print statement and allow the program to all three numbers in the main program.

Submit ```usingbreak.py```.

#### Exercise 3 - Using ```continue```
Write a script that uses a ```while``` loop to sum all numbers between 0 and 100 that are evenly divisible by either 2 or 3.  For example, 2 is evenly divisible by 2, so 2 should be added to your accumulated sum.  Likewise, 15 is evenly divisible by 3, so 15 should be added to your accumulated sum.

We could implement this loop using either a ```for``` loop or a ```while``` loop; however, this exercise must be implemented using a ```while``` loop.  Print the answer only when the ```while``` loop exits.

Save this script as ```usingcontinue.py```

We can implement the logic required in a number of different ways; however, we are going to implement this using logic that is somewhat opposite of how you might think about it.  Rather than checking to see if the current number is divisible by 2 or 3, check to see if the current number is not divisible by both 2 and 3.  If the number is not divisible by 2 and is not divisible by 3, then we will continue to the next number.

In other words, inside the ```while``` loop, your code should use the following conditional pattern:
```python
if i_IS_NOT_DIVISIBLE_BY_2_AND_IS_NOT_DIVISIBLE_BY_3:
  continue
x = x + i     # i is the loop variable and x is the sum
```
> Note that if the ```if``` conditional is ```True```, the remaining code in the body of the loop is unreachable due to the ```continue``` statement.  Even though we do not have an ```else``` statement, we have created an implicit ```else``` by using ```continue```.

At the end of your program, use the following statement to print out the sum where ```x``` is the accumulator used to sum our numbers:
```
print("The sum of integers evenly divisible by either 2 or 3 between 0 and 100 is", x)
```
Your program should produce the following output:
```
The sum of integers evenly divisible by either 2 or 3 between 0 and 100 is 3317
```
> To debug your ```while``` loop, you should include a print statement inside the loop that prints out the loop index ```i``` each time through the loop.  You might also use a smaller loop (0 to 10 rather than 0 to 100) to start with; however, make sure to use to correct range in your final solution.  Once you have verified that the loop works properly, comment out the debug print statement.

Submit ```usingcontinue.py```
