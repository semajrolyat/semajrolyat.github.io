---
layout: post
title:  "Exercises"
date:   2018-11-20 00:00:00 -0400
schedule:   2018-11-20 00:00:00 -0400
categories: [GWU]
docclass: "exercises"
gwclass: "cs1012"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Exercises
Each exercise describes exactly what you must submit.  **DO NOT** submit individual files.  Save everything described into one folder, zip that folder, and submit the zip containing all files.

In your ```cs1012``` folder create a subfolder named ```11_20_2018```.  Save all of your work from today in this folder.  When you complete your work, zip the ```11_20_2018``` folder and submit it to blackboard.  These exercises are due before the next Tuesday class.

You **MUST** include comments in your code.  If your code contains no comments, it is incomplete and will not receive credit.  Comments are as important to your code as the code itself.


#### Exercise 1 - Plot polynomials

In this exercise, you will plot two polynomials on a single figure.  One polynomial is quadratic and the other is cubic.  Your figure must include labels for the x and y axes and the plot must span the x-interval [-10.0,10.0].

Save this script as ```polynomial.py```

The quadratic has the coefficients [10.0,10.0,-2.0] and the cubic has the coefficients [1.0,2.0,2.0,4.0].  Plot both of these functions on the same figure.

Your script must also save the figure as an image file with the file name ```polynomial.png``` at a resolution of 120 dpi.  Your image should look like the following image:

![Polynomial Plot]({{"/gwu/fa18/cs1012/assets/11_20_2018/polynomial.png" | absolute_url }})

Submit both ```polynomial.py``` and ```polynomial.png```.

#### Exercise 2 - Plot signal data

In this exercise, you will plot experimental data against the expected, ideal data on a single figure.  The experimental data is provided in the file [```signaldata.txt```]({{"/gwu/fa18/cs1012/assets/11_20_2018/signaldata.txt" | absolute_url }}).  The ideal data is represented by a sine function over the interval [0,2*pi].  Consider the x-axis to be time and the y-axis to be amplitude.  The data file contains two columns that represent the measured time and amplitude from an experiment.  You will plot the data contained in the file as a scatter plot and you will plot the ideal function as a line plot on the same figure.  Your figure must include a title, labels for the x and y axes, and a legend.

Save this script as ```signaldata.py```

Make sure to download
[```signaldata.txt```]({{"/gwu/fa18/cs1012/assets/11_20_2018/signaldata.txt" | absolute_url }}) and save it into the directory containing ```signaldata.py```.

Your script must also save the figure as an image file with the file name ```signaldata.png``` at a resolution of 120 dpi.  Your image should look like the following image:

![Signal Data Plot]({{"/gwu/fa18/cs1012/assets/11_20_2018/signaldata.png" | absolute_url }})

Submit both ```signaldata.py``` and ```signaldata.png```.

#### Exercise 3 - Plot error in the signal data

In this exercise, you will plot the error in the experimental data with respect to the expected data, and you will also plot the mean and standard deviation for the error.  You will use the same [```signaldata.txt```]({{"/gwu/fa18/cs1012/assets/11_20_2018/signaldata.txt" | absolute_url }}) from Exercise 2.  Recall that the ideal data is represented by a sine function over the interval [0,2*pi].  In this case, consider the x-axis to be the sample number and the y-axis to be the error between the ideal value and the measured value.  You will plot the error as a scatter plot and you will plot the mean and standard deviation as line plots overlaying the error.  Your figure must include a title, labels for the x and y axes, and a legend.

> Note that the x-axis represents the sample number and not time as in the first plot.  I recommend that you use the ```arange``` function to generate the values on the x-axis.  

Save this script as ```signalerror.py```

Make sure to download
[```signaldata.txt```]({{"/gwu/fa18/cs1012/assets/11_20_2018/signaldata.txt" | absolute_url }}) and save it into the directory containing ```signalerror.py```.

Your script must also save the figure as an image file with the file name ```signalerror.png``` at a resolution of 120 dpi.  Your image should look like the following image:

![Signal Error Plot]({{"/gwu/fa18/cs1012/assets/11_20_2018/signalerror.png" | absolute_url }})

Submit both ```signalerror.py``` and ```signalerror.png```.
