---
layout: post
title:  "Exercises"
date:   2019-04-17 00:00:00 -0400
schedule:   2019-04-17 00:00:00 -0400
categories: [GWU]
docclass: "exercises"
gwclass: "cs1012"
term: "sp19"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Exercises 10

### Due Date
**The solutions to these exercises must be submitted by the end of the day.**

### Instructions

You are allowed to collaborate with your neighbor on these exercises.  Each of you must complete the programming tasks individually; however, you are encouraged to discuss and work together to design a solution to the problems.

Before beginning, make sure to create a new folder named ```exercises10``` in your class folder.

Create a .zip archive containing all of your code files and any written solutions and submit the .zip archive to blackboard as your solutions to these exercises.

You **MUST** include comments in your code.  For each function, you must also provide a block comment that precedes the function and describes every input to the function if it accepts any parameters, what the function does, and what the function returns if it returns a value.  If your code contains no comments, it is incomplete and will not receive credit.  Comments are as important to your code as the code itself.  You must include a comment in the header portion of the file that summarizes what the program does.  You must include comments inline with code to describe the steps in natural language.


#### Exercise 1 - Plot polynomials

Create a file named ```exercise1.py```

In this exercise, you will plot two polynomials on a single figure.  One polynomial is quadratic and the other is cubic.  Your figure must include labels for the x and y axes and the plot must span the x-interval [-10.0,10.0].

The quadratic must have the coefficients [10.0,10.0,-2.0] and the cubic must have the coefficients [1.0,2.0,2.0,4.0].  Plot both of these functions on the same figure.

Your script must also save the figure as an image file with the file name ```exercise1.png``` at a resolution of 120 dpi.  Your image should look like the following image:

![Polynomial Plot]({{"/gwu/sp19/cs1012/assets/exercises10/exercise1.png" | absolute_url }})

Submit both ```exercise1.py``` and ```exercise1.png```.

#### Exercise 2 - Plot signal data

Create a file named ```exercise2.py```

In this exercise, you will plot experimental data against the expected, ideal data on a single figure.  The experimental data is provided in the file [```signaldata.txt```]({{"/gwu/sp19/cs1012/assets/exercises10/signaldata.txt" | absolute_url }}).  The ideal data is represented by a sine function over the interval [0,2*pi].  Consider the x-axis to be time and the y-axis to be amplitude.  The data file contains two columns that represent the measured time and amplitude from an experiment.  You will plot the data contained in the file as a scatter plot and you will plot the ideal function as a line plot on the same figure.  Your figure must include a title, labels for the x and y axes, and a legend.

Make sure to download
[```signaldata.txt```]({{"/gwu/sp19/cs1012/assets/exercises10/signaldata.txt" | absolute_url }}) and save it into the directory containing ```exercise2.py```.

Your script must also save the figure as an image file with the file name ```exercise2.png``` at a resolution of 120 dpi.  Your image should look like the following image:

![Signal Data Plot]({{"/gwu/sp19/cs1012/assets/exercises10/exercise2.png" | absolute_url }})

Submit both ```exercise2.py``` and ```exercise2.png```.

#### Exercise 3 - Plot error in the signal data

Create a file named ```exercise3.py```

In this exercise, you will plot the error in the experimental data with respect to the expected data, and you will also plot the mean and standard deviation for the error.  You will use the same [```signaldata.txt```]({{"/gwu/sp19/cs1012/assets/exercises10/signaldata.txt" | absolute_url }}) from Exercise 2.  Recall that the ideal data is represented by a sine function over the interval [0,2*pi].  In this case, consider the x-axis to be the sample number and the y-axis to be the error between the ideal value and the measured value.  You will plot the error as a scatter plot and you will plot the mean and standard deviation as line plots overlaying the error.  Your figure must include a title, labels for the x and y axes, and a legend.

> Note that the x-axis represents the sample number and not time as in the first plot.  I recommend that you use the ```arange``` function to generate the values on the x-axis.  

Make sure to download
[```signaldata.txt```]({{"/gwu/sp19/cs1012/assets/exercises10/signaldata.txt" | absolute_url }}) and save it into the directory containing ```exercise3.py```.

Your script must also save the figure as an image file with the file name ```exercise3.png``` at a resolution of 120 dpi.  Your image should look like the following image:

![Signal Error Plot]({{"/gwu/sp19/cs1012/assets/exercises10/exercise3.png" | absolute_url }})

Submit both ```exercise3.py``` and ```exercise3.png```.
