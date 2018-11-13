---
layout: post
title:  "Introduction to numpy"
date:   2018-11-13 00:00:00 -0400
schedule:   2018-11-13 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
---

Python has a broad array of applications, but the most widely used area of Python use involves data manipulation and analysis.

To support data analysis and plotting, [```scipy```](https://www.scipy.org/), _i.e._ scientific python library, includes are variety of modules.  The two modules in ```scipy``` library that we will focus on are [```numpy```](http://www.numpy.org/) and [```matplotlib```](https://matplotlib.org/).

## Working with ```numpy```

### The Python [```tuple```](https://docs.python.org/3.1/tutorial/datastructures.html#tuples-and-sequences)
The ```tuple``` is similar to a Python ```list``` except that a ```tuple``` is immutable while a ```list``` is mutable.  A ```tuple``` therefore shares characteristics with the Python ```string``` type.

In Python, a ```tuple``` is constructed using parentheses rather than using the square brackets used for a ```list```, and when a ```tuple``` is printed, it will be printed in parentheses.  For example, the following code creates a ```tuple``` named ```t```:
```Python
t = (1,2,3)        # define t as a tuple
print(t)           # print the tuple t
print(type(t))     # print the type of t
print(len(t))      # print the length of t
print(t[0])        # print the first element of t
```
The above code produces the following output:
```
(1, 2, 3)
<class 'tuple'>
3
1
```
Note that we can use the built in ```len``` function to find the length of a ```tuple``` and we can access elements of the ```tuple``` using the same square bracket notation that is used to access members of a ```list```.  The main difference between a ```list``` and a ```tuple``` is that we cannot change a value in a tuple after it has been created.  For example, the following code produces an error:
```python
t = (1,2,3)        # define t as a tuple
t[0] = 0           # attempt to reassign an element of t
```
The error produced is:
```
TypeError: 'tuple' object does not support item assignment
```
### [```numpy.ndarray```](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.ndarray.html)

> NOTE: do not get caught up with how complex creating an ```ndarray``` appears to be in the examples in this section.  We will show some much simpler ways further down.

The ```numpy.ndarray``` is an ```n``` dimensional array which means that it can have a variable number of dimensions.  A Python ```list``` can model an ```ndarray``` but it requires a significant number of statements to iterate over many dimensions or to change the structure of the data in the ```list```.  The motivation behind ```numpy``` is to reduce the number of steps necessary to perform a data manipulations on ```n``` dimensional data.  Therefore, the ```ndarray``` type has a large number of operations built into it to support data manipulation.  For example, the following code generates an ```ndarray``` that has 2 elements and contains random floating point data.

```python
import numpy as np
a = np.ndarray(shape=(2,), dtype=float)
print(a)
```
The above code produces the following output:
```
[432. 288.]
```

Note how the shape of the array is specified using a ```tuple``` when we create the ```ndarray```.  In the above example, the ndarray contains ```2``` elements and the way the ```ndarray``` is printed resembles a ```list```.  It is important to note that an ```ndarray``` has a distinctly different type than a ```list``` even if it resembles a ```list```.

The following code contrasts a ```list``` with an ```ndarray``` where we create a ```list``` containing integers and that data is then used to create an ```ndarray```:

```python
import numpy as np

l = [1,2]
print(l)
print("l is of type", type(l))
a = np.ndarray(shape=(2,), buffer=np.array(l), dtype=int)
print(a)
print("a is of type", type(l))
```
The above code produces the following output:
```
[1, 2]
l is of type <class 'list'>
[1 2]
a is of type <class 'numpy.ndarray'>
```

Note that the string produced when printing a ```list``` looks similar to the string produced when printing a ```numpy ndarray```; however, there is one subtle difference, there are commas in the ```list``` string and no commas in the ```numpy ndarray``` string.  The output from the calls to the ```type``` function makes it more clear that Python handles a ```list``` and an ```ndarray``` as distinctly different types.

Building an ```ndarray``` directly can be fairly confusing, so ```numpy``` also provides a number of helper functions that generate an ```ndarray``` using simple approaches.

### [```numpy.zeros```](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.zeros.html)

We can automatically create an ```ndarray``` entirely populated with zeros by using the ```zeros``` function.  For example, the following code generates an ```ndarray``` with one dimension and five elements where all values are initialized to zero:

```Python
import numpy as np
a = np.zeros(5)
print(a)
```
The above code produces the following output:
```
[0. 0. 0. 0. 0.]
```

We may need to instead create an array with multiple dimensions.  For example, the following code creates an ```ndarray``` with two rows and three columns and with all values initialized to zero:

```python
import numpy as np
shape = (2,3)         # shape is (rows, columns) by default
a = np.zeros(shape)
print(a)
```
The above code produces the following output:
```
[[0. 0. 0.]
 [0. 0. 0.]]
```

The ```zeros``` function has the following function declaration:
```Python
numpy.zeros(shape, dtype=float, order='C')
```

* ```shape``` can be an ```int``` as in the first example or a ```tuple``` of ```int```s as in the second example.
* The data type, ```dtype``` is assumed to be a ```float``` unless otherwise specified.
* ```order``` determines whether the ```ndarray``` is stored in row major, ```'C'``` default, or column major format, ```'F'```.

### [```numpy.arange```](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.arange.html)

The ```arange``` function returns evenly spaced values within a given interval.  It is similar to the built in Python ```range``` function.  For example, the the following code shows usage of ```arange``` in ways similar to how we have been using ```range```:

```Python
import numpy as np
print(np.arange(3))
print(np.arange(3.0))
print(np.arange(3,7))
print(np.arange(3,7,2))
```
```
[0 1 2]
[0. 1. 2.]
[3 4 5 6]
[3 5]
```

Unlike the ```range``` function, ```arange``` can generate a sequence of floating point values.  For example, the following code produces an ```ndarray``` that contains a sequence from ```0.0``` to ```0.9``` with a step size of ```0.1```:

```python
import numpy as np

x = np.arange(0.0, 1.0, 0.1)

print(x)
print(type(x))
```
The above program produces the following output:
```
[0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]
<class 'numpy.ndarray'>
```

```arange``` has the following function declaration:
```python
numpy.arange([start, ]stop, [step, ]dtype=None)
```

* ```start``` is optional and represents the start of the interval. The interval includes this value. The default start value is 0.
* ```stop``` is the end of interval and does not include this value, except in some cases where step is not an integer and floating point round-off affects the length of the ```ndarray``` generated.
* ```step``` is the spacing between values. For any output, this is the distance between two adjacent values. The default step size is 1.
* ```dtype``` The type of the output array. If dtype is not given, ```arange``` will infer the data type from the other input arguments.


### [```numpy.array```](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.array.html)

We may already have data in a ```list``` type that we would like to convert to an ```ndarray```.  The ```array``` function allows us to generate an ```ndarray``` from a sequence type, whether ```list``` or ```tuple```.  For example, the following code copies the ```list``` ```l``` into the ```ndarray``` ```a``` using the ```array``` function:

```Python
import numpy as np

l = [1,2,3]
a = np.array(l)

print(l)
print(a)

print(type(l))
print(type(a))
```
Produces the following output:
```
[1, 2, 3]
[1 2 3]
<class 'list'>
<class 'numpy.ndarray'>
```

```array``` has the following function declaration:
```Python
numpy.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)
```
We really do not need to consider any parameters other than ```object``` as the defaults are sufficient for most of our purposes.  The ```object``` parameter is any sequence or array like object.

```array``` is not limited to generating one dimensional arrays.  If the ```object``` parameter contains nested sequence information, the ```ndarray``` generated will reflect the structure of the sequence object.  For example, the following code converts a list of lists into a two dimensional array:
```Python
import numpy as np

l = [[1,2],[3,4]]
a = np.array(l)
print(a)
```
The above code produces the following output:
```
[[1 2]
 [3 4]]
```

#### [```numpy.ndarray.shape```](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.ndarray.shape.html)

The ```ndarray``` is a smart object that has a number of functions that are attached to it.  One of those functions allows us to ask any ```ndarray``` what its shape is.  This function is called ```shape``` and returns a ```tuple```.  For example, the following code creates an array and queries the ```ndarray``` for its ```shape```:

```Python
import numpy as np
a = np.array([1,2,3,4])  # create a ndarray of 4 elements
print(a)                 # print the contents of the ndarray
print(type(a))           # print the array's type
print(a.shape)           # print the shape of the ndarray
```
The above code produces the following output:
```
[1 2 3 4]
<class 'numpy.ndarray'>
(4,)
```
We see on the last line of output that ```shape``` reported that the array ```a``` has a shape of ```(4,)``` meaning that it is one dimensional and contains 4 elements.

#### [```numpy.reshape```](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.reshape.html)

We may need to change the shape of an ```ndarray``` in order to work with the data in a particular way.  The following code shows how we can change a one dimensional ```ndarray``` into a two dimensional ```ndarray```:

```Python
import numpy as np

a = np.array([1,2,3,4])  # create the ndarray a with 4 elements

print(a)                 # print the contents of a
print(a.shape)           # print the shape of a
b = a.reshape((2,2))     # copy a into b with a different shape
print(b)                 # print the contents of b
print(b.shape)           # print the shape of b
```
The above code produces the following output:
```
[1 2 3 4]
(4,)
[[1 2]
 [3 4]]
(2, 2)
```

The first line is the original array ```a```.  The second line is the shape of ```a```, _i.e._ ```4```.  The third and fourth lines are the new array ```b``` which is a copy of ```a``` with a different shape.  On the fifth line, the shape of ```b```, _i.e._ 2x2, is printed.

Conversely, we can reshape a multi-dimensional ```ndarray``` into a one dimension ```ndarray```:
```Python
import numpy as np

a = np.array([[1,2],[3,4]])  # create a 2x2 ndarray
b = a.reshape((4,))          # flatten a into b
print(b)                     # print the contents of b
print(b.shape)               # print the shape of b
```
The above code produces the following output:
```
[1 2 3 4]
(4,)
```

### Indexing an ```ndarray```
We index an ```ndarray``` using a similar approach to how we indexed; however, the usage is slightly different yet more capable.

There is no difference between indexing a ```list``` with no nesting and a one dimensional ```ndarray```; however, there is a significant difference between indexing a nested ```list``` and a multidimensional ```ndarray```.  Recall that when we accessed nested ```list```s, _i.e._ a lists of lists, we used a pair of square brackets for each level of nesting.  ```ndarray```'s are indexed using a single pair of square brackets regardless of the number of dimensions in the ```ndarray```.  For example, a list of lists is indexed using the following approach:
```Python
l = [[1,2],[3,4]]
print( l[0][0] )
```
Note that two pairs of square brackets are required to access the first element in the nested ```list```.  Contrast the following code with the previous code:
```Python
import numpy as np
a = np.array([[1,2],[3,4]])
print(a[0,0])
```

### Slicing an ```ndarray```

We slice an ```ndarray``` using a similar approach to how we sliced lists; however, the usage follows the indexing format for ```ndarray```'s.

> We saw some anomalous behavior when we tried to slice a list of lists.  These issues are resolved in ```ndarrays```.

We can slice across any dimension of an ```ndarray```.  We can therefore slice rows or columns (or some arbitrary dimension for ```ndarray```'s that have more than two dimensions).

The following code demonstrates slicing rows and columns:
```python
import numpy as np

a = np.array([[1,2],[3,4]])  # create a 2x2 ndarray
r1 = a[1,:]
print(r1)
c0 = a[:,0]
print(c0)
```
The above code produces the following output:
```
[3 4]
[1 3]
```
In the output above, the first line represents the slice of row 1 (the second row) and the second line represents the slice of column 0 (the first column).

Using these slicing techniques, we can easily extract a row or column as needed from any ```ndarray```.

## Mathematical Operations on ```ndarrays```
While we have focused on iteration as a fundamental of programming, Python's most powerful features are designed to avoid operating on individual elements.  ```numpy``` allows us to take advantage of bulk operations and will help us reduce the amount of code needed to perform complex operations.  If we use the built in ```numpy``` functions we can write sophisticated data processing programs that might take tens or hundreds of lines in another language or in vanilla Python.

### Using Mathematical Operators

Much of the power offered by ```numpy``` comes from the ability to perform a mathematical operation on all cells in an ```ndarray``` using a single statement.  The following code illustrates we can add a constant to all cells in the ```ndarray```:
```Python
import numpy as np

a = np.array([1,2,3])
b = a + 1
print("a=",a)
print("b=",b)
```
The above code produces the following output:
```
a= [1 2 3]
b= [2 3 4]
```

While it may not be that useful to add a constant to each cell, this ability to perform a set of bulk mathematical operations can be very powerful.  Consider the following code:
```Python
import numpy as np
a = np.array([3,4])
l2 = np.linalg.norm(a)
print(a)
print(l2)
print(a/l2)
```
The above code produces the following output:
```
[3 4]
5.0
[0.6 0.8]
```
The above program computes the l2 norm of a vector and then normalizes that vector.

> What is the l2 norm?  Draw a right triangle with sides of the length provided in ```a```.  You will see that the value stored in ```l2``` is the length of the hypoteneuse.  The final step of normalizing ```a``` by dividing it by ```l2``` gives the length of the sides of that triangle when projected onto the unit circle.

### Other ```numpy``` Mathematical Functions
There a broad variety of [mathematical](https://docs.scipy.org/doc/numpy-1.15.0/reference/routines.math.html), [linear algebra](https://docs.scipy.org/doc/numpy-1.15.0/reference/routines.linalg.html), and [randomization](https://docs.scipy.org/doc/numpy-1.15.0/reference/routines.random.html) functions in ```numpy```.  Some of these functions are also implemented in the Python ```math``` module or in the core of Python; however, the ```numpy``` based functions are explicitly designed to operate on ```ndarray```'s very efficiently.  In many cases, we can use these functions on an entire ```ndarray``` in a single operation without the need to iterate.

We cannot cover all functions in ```numpy```, so you should consult the [```numpy``` mathematical function reference page](https://docs.scipy.org/doc/numpy-1.15.0/reference/routines.math.html) before attempting to use a more basic technique that requires you to iterate over an ```ndarray```.  The following section details using the ```diff``` function which should help you generally understand how you can use the ```numpy``` mathematical functions without iteration.

#### Computing a Difference using [```numpy.diff```](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.diff.html)

We may need to compute the change between two samples.  We could accomplish this by iterating over an ```ndarray``` and computing the difference between each neighboring record; however, ```numpy``` provides a built in function that performs this calculation in one statement and is highly flexible, _i.e._ ```diff```.  For example, if we wish to compute the difference along the first column of an ```ndarray```, we can use the following approach:

```python
import numpy as np
a = np.array([1,2,4])
delta = np.diff(a)
print(delta)
```
The above code produces the following output:
```
[1 2]
```
The output represents the difference between each neighbor in the ```ndarray``` ```a```.  Let's double check:

* For any set of ```n``` elements, the total count of differences between neighbors should be ```n-1```.  Original array ```a``` consists of 3 elements and the ```delta``` difference array consists of 2 elements, so this is consistent.
* The difference between the first and second element is ```2-1``` which is represented as ```1``` in ```delta```, and the difference between the second and third element is ```4-2``` which is represented as ```2``` in ```delta```, so this is also consistent.

The ```diff``` function is not limited to one dimensional ```ndarray```s.  For example, the following code computes the difference between neighboring cells for each row:
```Python
import numpy as np

a = np.array([[1,2],[3,4],[5,6]])
print(a)
delta = np.diff(a)
print(delta)
```
The above code produces the following output:
```
a= [[1 2]
 [3 4]
 [5 6]]
delta= [[1]
 [1]
 [1]]
```
In the above output, the result is consistent because we expect to have three rows in ```delta``` because we computed the difference across rows, we expect to have one value in ```delta``` for each row because each row of ```a``` has two values,  and the values in ```delta``` should be ```1``` because the neighboring values in ```a``` are sequential.

However, we might instead need to compute the difference between each neighboring cells for each column.  We can do this by explicitly setting the axis argument for ```diff```.  For example:
```Python
import numpy as np

a = np.array([[1,2],[3,4],[5,6]])
print(a)
delta = np.diff(a,axis=0)
print(delta)
```
The above code produces the following output:
```
a= [[1 2]
 [3 4]
 [5 6]]
delta= [[2 2]
 [2 2]]
```

In the above output, the result is consistent because we expect to have two rows in ```delta``` because we computed the difference between rows, we expect to have two values in ```delta``` for each row because each row of ```a``` has two values,  and the values in ```delta``` should be ```2``` because the neighboring values from row-to-row in ```a``` have a difference of ```2```.

We can also use slicing to compute the difference within some subset of the original data.  For example, the following code computes the difference in the first column by using a slice:
```Python
import numpy as np
a = np.array([[1,2],[3,4],[5,6]])
print("a=",a)
delta = np.diff(a[:,0])
print("delta=",delta)
```
 The above code produces the following output:
```
 a= [[1 2]
 [3 4]
 [5 6]]
delta= [2 2]
```

## Reading and Writing Data
All of the programs we have developed so far have used data that we have hardcoded into our programs in one way or another.  In reality, we will need to operate on data that is stored on the hard drive.  Typically, data is generated by one or more experimental processes and that data is stored for later processing in some way.  Data that is stored long term is written onto a storage medium such as a hard drive.  In order to process data stored on the hard drive, we will need to first load that data into memory in a format that we can work with.  We also may need to write our own data to the hard drive once we have processed it in some way.

There are a wide variety of hard drive reading and writing capabilities built into the Python ```os``` module; however, the author's of ```numpy``` included functions that are specifically designed to easily read data into Python when the programmer needs to use ```numpy``` operations.  It will be much easier to rely on the ```numpy``` reading and writing functions than it will be to learn all the nuances involved with using the ```os``` module.  There are a number of functions in ```numpy``` for reading data from a file and writing data to a file; however, we will focus on using [```numpy.loadtxt```](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.loadtxt.html).  For writing data, we will focus on using [```numpy.savetxt```](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.savetxt.html).

### ```numpy.loadtxt```
The function declaration for ```loadtxt``` is the following:
```python
numpy.loadtxt(fname, dtype=<class 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0, encoding='bytes')
```
The above declaration has a significant number of parameters; however, for files that are space delimited, _i.e._ there is a space between each record, we can generally call ```loadtxt``` with only one parameter: the path to the file.  ```loadtxt``` will return an ```ndarray``` containing the data.

For example, if the file we wish to load is located in the same directory as the python script and the file is name ```data.txt```, we can load it into an array ```a``` using the following code:
```Python
import numpy as np
a = loadtxt('data.txt')
```

### ```numpy.savetxt```
The function declaration for ```savetxt``` is the following:
```python
numpy.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None)
```
The declaration for ```savetxt``` also has a large number of parameters; however, we can generally call ```savetxt``` with two parameters: the path to the file to write and the array to write.

For example, if we wish to save the array ```a``` in a file named 'out.txt', we can use the following code:
```Python
import numpy as np
a = np.zeros(5)
np.savetxt('out.txt', a)
```
