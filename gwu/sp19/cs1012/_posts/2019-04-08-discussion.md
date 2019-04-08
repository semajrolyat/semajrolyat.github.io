---
layout: post
title:  "Introduction to numpy"
date:   2019-04-08 00:00:00 -0400
schedule:   2019-04-08 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
term: "sp19"
---

Python has a broad array of applications, but the most widely used area of Python use involves data manipulation and analysis.

To support data analysis and plotting, [```scipy```](https://www.scipy.org/), _i.e._ scientific python library, includes are variety of modules.  The two modules in ```scipy``` library that we will focus on are [```numpy```](http://www.numpy.org/) and [```matplotlib```](https://matplotlib.org/).

## Working with ```numpy```

### [```numpy.ndarray```](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.ndarray.html)

> NOTE: do not get caught up with how complex creating an ```ndarray``` appears to be in the examples in this section.  We will show some much simpler ways further down.

The ```numpy.ndarray``` is an ```n``` dimensional array which means that it can have a variable number of dimensions, _i.e._ ```n``` dimensions.  A Python ```list``` can model an ```ndarray``` but it requires a significant number of statements to iterate over many dimensions or to change the structure of the data in the ```list```.  The motivation behind ```numpy``` is to reduce the number of steps necessary to perform data manipulations on ```n``` dimensional data.  Therefore, the ```ndarray``` type has a large number of operations built into it to support data manipulation.  For example, the following code generates an ```ndarray``` that has 2 elements and contains random floating point data.

```python
import numpy as np
a = np.ndarray(shape=(2,), dtype=float)
print(a)
```
The above code produces the following output:
```
[432. 288.]
```

> The ```dtype``` argument is shorthand for 'data-type'.  One of the restrictions on the ```ndarray``` is that all cells in the array must contain the same type of data.  When creating the ```ndarray```, you specify the type of data that will be stored in the array using the ```dtype``` argument.

Note how the shape of the array is specified using a ```tuple``` when we create the ```ndarray```.  In the above example, the ```ndarray``` contains ```2``` elements and the way the ```ndarray``` is printed resembles a ```list```.  It is important to note that an ```ndarray``` has a distinctly different type than a ```list``` even if it resembles a ```list```.

The following code contrasts a ```list``` with an ```ndarray``` by first creating a ```list``` containing integers and then the same data is used to create an ```ndarray```:

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

> The call to ```np.ndarray``` in the second example includes a ```buffer``` argument where the first example omitted this argument.  The above example of the ```buffer``` argument converts the Python list to a ```numpy``` compatible array first using the ```array``` function and then assigns the cells in the ```ndarray``` from the compatible array.  The ```array``` function is discussed in more detail below.

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

The ```arange``` function returns evenly spaced values within a given interval.  It is similar to the built in Python ```range``` function.  For example, the following code shows usage of ```arange``` in ways similar to how we have been using ```range```:

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

* ```start``` is optional and represents the start of the interval. The interval includes this value. The default start value is ```0```.
* ```stop``` is the end of interval and does not include this value, except in some cases where ```step``` is not an integer and floating point round-off affects the length of the ```ndarray``` generated.
* ```step``` is the spacing between values. For any output, this is the distance between two adjacent values. The default step size is ```1```.
* ```dtype``` The type of the output array. If ```dtype``` is not given, ```arange``` will infer the data type from the other input arguments.


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

We really do not need to consider any parameters other than ```object``` as the defaults are sufficient for most of our purposes.  The ```object``` parameter can be any sequence or array like object.

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

> Note that we use the 'dot' operator to access functions that are attached to the object itself.  This is similar to how we have used the dot operator for accessing functions that are in a particular module.  However, when accessing a function attached to an object, the operations will typically be performed solely on that object from which we accessed the method,

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

The first line is the original array ```a``` which is 'flat' or has only one dimension which is reflected by the output on the second line produced by asking for the shape of ```a```, _i.e._ ```4```.  The third and fourth lines are the new array ```b``` which is a copy of ```a``` with a different shape, _i.e._ ```(2,2)``` meaning two rows and two columns.  On the fifth line, the shape of ```b```, _i.e._ 2x2, is printed.

Conversely, we can 'flatten' or reshape a multi-dimensional ```ndarray``` into a one dimensional ```ndarray```:
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

Keep in mind that an ```ndarray``` is n-dimensional.  It is often convenient for us to think of arrays in at most two dimensions; however, the number of dimensions for the ```ndarray``` can be arbitrary.  For example, the following code creates a three dimensional array:
```Python
import numpy as np

a = np.arange(27)
b = a.reshape(3,3,3)
print(b)
```
The above code produces the following output:
```
[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]]

 [[ 9 10 11]
  [12 13 14]
  [15 16 17]]

 [[18 19 20]
  [21 22 23]
  [24 25 26]]]
```
In this example, it may become difficult to visualize the structure of the array but we might conceptualize it as giving the array depth in addition to the height (rows) and width (columns).

### Indexing an ```ndarray```
We index an ```ndarray``` using a similar approach to how we indexed Python sequence types; however, the usage is slightly different while being more capable.

There is no difference between indexing a ```list``` with no nesting and a one dimensional ```ndarray```; however, there is a significant difference between indexing a nested ```list``` and a multidimensional ```ndarray```.  Recall that when we accessed nested ```list```s, _i.e._ a lists of lists, we used a pair of square brackets for each level of nesting.  The ```ndarray``` is indexed using a si2ngle pair of square brackets regardless of the number of dimensions in the ```ndarray``` with the index into each dimension separated by commas.  For example, a list of lists is indexed using the following approach:
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
Note the usage of one pair of brackets and the comma separation in the ```numpy``` array (second example).

### Slicing an ```ndarray```

We slice an ```ndarray``` using a similar approach to how we sliced lists; however, the usage follows the indexing format for ```ndarray```'s.

> We saw some anomalous behavior when we tried to slice a list of lists.  These issues are resolved in ```ndarrays```.

We can slice across any dimension of an ```ndarray```.  We can therefore slice rows or columns (or some arbitrary dimension for ```ndarray```'s that have more than two dimensions).

The following code demonstrates slicing rows and columns:
```python
import numpy as np

a = np.array([[1,2],[3,4]])  # create a 2x2 ndarray
r1 = a[1,:]  # slice the 2nd row
print(r1)
c0 = a[:,0]  # slice the 1st column
print(c0)
```
The above code produces the following output:
```
[3 4]
[1 3]
```
In the output above, the first line represents the slice of row 1 (the second row) and the second line represents the slice of column 0 (the first column).

Using these slicing techniques, we can easily extract one or more rows or columns as needed from any ```ndarray```.  We are actually slicing smaller arrays from the larger ```ndarray```, and we can slice an arbitrary array from the original array.  For example:

```Python
import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])  # create a 3x3 ndarray
b = a[1:,:2]
print(b)
```   
The above code produces the following output:
```
[[4 5]
 [7 8]]
```
The interpretation of the slice generated by ```a[1:,:2]``` is to begin at the second row and slice to the end row, ```1:```, and to begin at the first column and slice up to but not including the last column, ```:2```.   

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
The above program computes the l2 norm of vector ```a``` and then normalizes that vector in a few clean operations.  If we needed to compute the l2 norm ourselves, we would need to sum the squares of each element in the vector and then take the square root of the sum.  Instead, we can use one operation on the entire vector.

> What is the l2 norm?  Draw a right triangle with sides of the length provided in ```a```.  You will see that the value stored in ```l2``` is the length of the hypoteneuse.  The final step of normalizing ```a``` by dividing it by ```l2``` gives the length of the sides of that triangle when projected onto the unit circle.

## Built in ```ndarray``` functions a.k.a. methods
We have not focused on classes in this course.  If there is time at the end of the term, we will.  However, the term _**method**_ is used to describe a function that is attached to an object.  We access a method using the dot operator in the exact same way that we access functions for ```numpy```.  We won't focus too much on the differences between accessing a module function and a class function right now and we will instead assume that they are generally the same.

For example, the following code uses the dot operator ```.``` between the ```np``` module name and the call to the ```array``` function:
```python
import numpy as np
a = np.array([3,4])
```
A call to method looks exactly the same.  For example, we can call the transpose method for an ```ndarray``` using the following code:

```python
import numpy as np
a = np.arange(10)
b = a.transpose()
```

When a method is called, it typically operates on the data stored in the object that called it (whatever object precedes the dot operator).  In the above example, the data in ```a``` is transposed and the result is stored in ```b```.

### Transposing a numpy array
Transpose is a term that is borrowed from linear algebra which means to flip a matrix across the diagonal.  For more information on the transpose operation, look at the [Transpose Wikipedia article](https://en.wikipedia.org/wiki/Transpose).  The practical application of transpose is to convert rows to columns and columns to rows without otherwise changing the structure or contents of an array.  In order to carry out an operation, we may need to change an array from row major format to column major format meaning we may need to swap rows to columns and vice versa.

```Python
import numpy as np

a = np.arange(10)        # arange produces a 1 dimensional array
a = a.reshape((2,5))     # reshape a into a 2 dimensional array
b = a.transpose()        # transpose a into a 5x2 array
print(b)
```
The output from the above is as follows:
```
[[0 5]
 [1 6]
 [2 7]
 [3 8]
 [4 9]]
```
On the surface, it may appear that we could achieve the same result by reshaping the array; however, this is not often the case.  For example, the following code attempts to reshape the array to produce the same structure as the above code:
```Python
import numpy as np

a = np.arange(10)        # arange produces a 1 dimensional array
a = a.reshape((2,5))     # reshape a into a 2 dimensional array
b = a.reshape((5,2))     # attempt to reshape into a 5x2 array
print(b)
```
The above code produces the following output:
```
[[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]
```
Note how the second output differs from the first.  Make sure that you are using the correct method for your intent.

Transpose is often the better choice instead of reshape as we do not need to explicitly know the dimensions of the array to use ```transpose``` while we do when we use ```reshape```.

The ```T``` property of an ```ndarray``` already holds the transpose and produces the same result as calling the ```transpose()``` function.
```Python
import numpy as np

a = np.arange(10)        # arange produces a 1 dimensional array
a = a.reshape((2,5))     # reshape a into a 2 dimensional array
b = a.T                  # transpose a into a 5x2 array
print(b)
```

### Find the minimum or maximum value in a ```numpy``` array
We can ask a ```numpy``` array to return its minimum and maximum values by calling the ```min``` and ```max``` methods respectively.

For example, the following code generates a 3x3 array within the range [0,8] and then copies the minimum value and the maximum value into ```Amin``` and ```Amax```:

```python
import numpy as np
A = np.arange(9)
A = A.reshape((3,3))
Amin, Amax = A.min(), A.max()
print(Amin, Amax)
```
The above code produces the following output:
```
0 8
```
You should see that the first value printed in the output reflects the minimum value in the array and the second value in the output reflects the maximum value in the array.

> This line ```Amin, Amax = A.min(), A.max()``` should draw your attention.  Yes, you can have multiple variables to the left of the assignment operator.  This operation is effectively assigning both ```Amin``` and ```Amax``` simultaneously.  This capability is very unique and there are few languages that support the ability to assign multiple variables to different values in one step.

### Find the mean value in a ```numpy``` array
We can ask a ```numpy``` array to return the mean (average) of all values by calling the ```mean``` method.

For example, the following code generates a 3x3 array within the range [0,8] and then asks the array for the mean of all values in the array:
```Python
import numpy as np
A = np.arange(9)
A = A.reshape((3,3))
print(A)
print(A.mean())
```
The above code produces the following output:
```
[[0 1 2]
 [3 4 5]
 [6 7 8]]
4.0
```
The value ```4.0``` is the average of all values in the array.

Because a slice is itself an array, we can slice the array and ask the slice for its own mean:
```Python
import numpy as np
A = np.arange(9)
A = A.reshape((3,3))
print(A)
print(A[:,2].mean())
```
The above code produces the following output:
```
[[0 1 2]
 [3 4 5]
 [6 7 8]]
5.0
```
In the above example, we sliced the last column from ```A``` and then computed the mean for that column.  You should see that ```5.0``` is the average of all values in the last column.

## Other ```numpy``` Mathematical Functions
There a broad variety of [mathematical](https://docs.scipy.org/doc/numpy-1.15.0/reference/routines.math.html), [linear algebra](https://docs.scipy.org/doc/numpy-1.15.0/reference/routines.linalg.html), and [randomization](https://docs.scipy.org/doc/numpy-1.15.0/reference/routines.random.html) functions in ```numpy```.  Some of these functions are also implemented in the Python ```math``` module or in the core of Python; however, the ```numpy``` based functions are explicitly designed to operate on ```ndarray```'s very efficiently.  In many cases, we can use these functions on an entire ```ndarray``` in a single operation without the need to iterate.

We cannot cover all functions in ```numpy```, so you should consult the [```numpy``` mathematical function reference page](https://docs.scipy.org/doc/numpy-1.15.0/reference/routines.math.html) before attempting to use a more basic technique that requires you to iterate over an ```ndarray```.  The following section details using some typically used functions which should help you generally understand how you can use the ```numpy``` mathematical functions without iteration.

Many of these functions are intended to work on vectors only.  A one dimensional array is also known as a _**vector**_.

### Computing the Median using [```numpy.median```](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.median.html)

We may need to find the middle (median) value in a row or column in an array.  In order to do this, we can use the ```median``` function.  The median function has the following declaration:
```Python
numpy.median(a, axis=None, out=None, overwrite_input=False, keepdims=False)
```
We can use median without any of the optional parameters if we pass a row or column as the argument ```a```.  For example, the following code generates a simple matrix and uses slicing to retrieve the median of the first row and the first column:

```python
import numpy as np
A = np.arange(9)
A = A.reshape((3,3))
print(A)
print(np.median(A[0,:]))   # get the median of the first row
print(np.median(A[:,0]))   # get the median of the first column
```
The above code produces the following output:
```
[[0 1 2]
 [3 4 5]
 [6 7 8]]
1.0
3.0
```

### Computing the standard deviation using [```numpy.std```](https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.std.html)

For statistical analysis, we may need to find the standard deviation for a set of data.  ```numpy``` provides the ```std``` function to compute the standard deviation on an array.  The declaration for ```std``` is as follows:

```Python
numpy.std(a, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>)
```
The ```std``` function computes the standard deviation on the distribution of values in the array.  In many cases, we wish to compute the standard deviation for a row or column.  We can slice the array (rows or columns) and pass the slice to the ```std``` function so that we can compute the standard deviation on a subset of the original array.  For example, the following computes the standard deviation for the first column in the array:
```python
import numpy as np
A = np.arange(100)
A = A.reshape((10,10))
print(np.std(A[0,:]))
```
The above code produces the following output:
```
2.8722813232690143
```

### Computing a Difference using [```numpy.diff```](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.diff.html)

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
a = np.loadtxt('data.txt')
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
