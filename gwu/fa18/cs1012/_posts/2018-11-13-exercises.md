---
layout: post
title:  "Exercises"
date:   2018-11-13 00:00:00 -0400
schedule:   2018-11-13 00:00:00 -0400
categories: [GWU]
docclass: "exercises"
gwclass: "cs1012"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

## Exercises
Each exercise describes exactly what you must submit.  **DO NOT** submit individual files.  Save everything described into one folder, zip that folder, and submit the zip containing all files.

In your ```cs1012``` folder create a subfolder named ```11_13_2018```.  Save all of your work from today in this folder.  When you complete your work, zip the ```11_13_2018``` folder and submit it to blackboard.  These exercises are due before the next Tuesday class.

You **MUST** include comments in your code.  If your code contains no comments, it is incomplete and will not receive credit.  Comments are as important to your code as the code itself.


#### Exercise 1 - Compute statistical data for the last column in ```data.txt```

In this exercise, you will compute the statistical information for the last column of the provided [```data.txt```]({{"/gwu/fa18/cs1012/assets/11_13_2018/data.txt" | absolute_url }}).  The statistical information that you need to compute is the minimum, maximum, mean, and standard deviation.  You are required to read the file into an array, compute the values, and print the calculations to the console.

Save this script as ```stats.py```

Make sure to download [```data.txt```]({{"/gwu/fa18/cs1012/assets/11_13_2018/data.txt" | absolute_url }}) and save it into the directory containing ```stats.py```.

The output for your program should be:
```
min 0.00017756529318890824
max 0.9902558418244373
mean 0.4926828278976004
stddev 0.29062456165935907
```

Submit ```stats.py```

#### Exercise 2 - Sum the difference between each record in each column
In this exercise, you will compute the difference between each record in each column in [```data.txt```]({{"/gwu/fa18/cs1012/assets/11_13_2018/data.txt" | absolute_url }}).  You will then sum the differences such that you have one total for each column and you will store this value in an array.  Print the array once the sum is calculated.

Save this script as ```diffsum.py```

Make sure to download [```data.txt```]({{"/gwu/fa18/cs1012/assets/11_13_2018/data.txt" | absolute_url }}) and save it into the directory containing ```diffsum.py```.

> Hint: You can reduce the amount of statements by using the optional parameter ```axis``` for both ```diff``` and ```sum```.  The axis parameter controls which axis (rows or columns) over which to perform the operation.  The ```axis``` is equal to ```0``` when operating on rows, and the ```axis``` is 1 when operating on columns.

The output for your program should be:
```
[ 0.48649163 -0.16240036  0.77426417 -0.36291086 -0.65425832]
```

Submit ```diffsum.py```

#### Exercise 3 - Generate a square multiplication table in a ```numpy``` array
In this exercise, you will write a function that computes a square multiplication table, stores the table in a ```numpy``` array, and saves the file to disk.  The first row and first column should contain the number that is multiplied.  As a result, the size of the array (number of rows and columns) will actually be larger than the size requested.

Save this script as ```multtable.py```

Your function must have the following declaration where ```sz``` is the largest multiplier in the table:
```python
def multtable(sz):
```
Your main program should look like this:
```Python
print(multtable(3))
print(multtable(5))
```
Your output should look like this:
```
[[0. 1. 2. 3.]
 [1. 1. 2. 3.]
 [2. 2. 4. 6.]
 [3. 3. 6. 9.]]
[[ 0.  1.  2.  3.  4.  5.]
 [ 1.  1.  2.  3.  4.  5.]
 [ 2.  2.  4.  6.  8. 10.]
 [ 3.  3.  6.  9. 12. 15.]
 [ 4.  4.  8. 12. 16. 20.]
 [ 5.  5. 10. 15. 20. 25.]]
 ```

The file that is produced must be named ```multtable<sz>.txt``` where ```<sz>``` is replaced by the value passed into the ```multtable``` function.  For example, if ```multtable``` is called with the parameter ```5```, the file that must be written is ```multtable5.txt```.

There are many ways to accomplish this goal.  The key requirements that must be met are 1) the function must be generalized such that it can generate a multiplication table of any arbitrary size specified by the ```sz``` parameter, and 2) the function must return a ```numpy``` ```ndarray```.

Submit ```multtable.py```
