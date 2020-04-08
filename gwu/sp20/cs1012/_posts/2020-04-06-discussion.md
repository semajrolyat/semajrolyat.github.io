---
layout: post
title:  "Introduction to numpy"
date:   2020-04-06 00:00:00 -0400
schedule:   2020-04-06 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
term: "sp20"
---

The most widely used and in demand application of Python is for data manipulation and analysis.  What do these terms mean from a practical standpoint and how do we perform these tasks with Python?

To answer the first part of that question, consider why Excel is so widely used in business applications.  Excel is a type of program known as a spreadsheet which allows a user to embed computations derived from business logic into a set of data and then make an analysis of the data using mathematical manipulations, statistical tools, and graphical visualizations.  Excel dominates the spreadsheet market because it is a part of Microsoft Office which has established market share within the office productivity application market, so Excel is the defacto data analysis tool for the majority of businesses simply because it is installed on the most business machines.  

Spreadsheets are often good enough to fulfill the data analysis role for most applications; however, spreadsheets can introduce new problems that may be difficult and time consuming to work around.  The biggest drawback of a spreadsheet is that data and logic are tightly bound together which typically makes it more difficult and complex to change data and logic for future applications.  In essence, by building a complex spreadsheet that is critical to our business operations, an analytical tool becomes more specialized and less generalized which makes it difficult to adapt that tool when presented with new data or new business rules (calculations).  By divorcing data from business rules, we can build into our analytical tools the expectation that both data and business rules are individual entities that can change independent of one another.

> Divorcing logic (business rules) from data does not come without certain levels of organization.  When we segregate the two, we are storing data in one file and logic (code) in another file.  In order for the code to work properly on data, data must be consistently structured, _i.e._ rows are generally thought of as records while columns are thought of as common fields for all records.

The role of the ```numpy``` module (```numpy``` is short for 'numerical python') is to provide Python with the tools to perform operations on large data sets that allow programmers to manipulate and perform complex computations on large, structured data sets.  Basically, ```numpy``` gives us the ability to manipulate large sets of data and to run operations on subsets of that data (what we might think of as rows, columns, or individual cells in a data set) and is somewhat analogous to creating formulas in a spreadsheet.  Rather than embedding the business rules in the file containing the data as we would in a spreadsheet, we are instead writing a Python program that implements the business rules and can operate on any data set with the correct data structure.

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

The ```arange``` function has the following declaration:
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

The ```array``` function has the following declaration:

```Python
numpy.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)
```

We really do not need to consider any parameters other than ```object``` as the defaults are sufficient for most of our purposes.  The ```object``` parameter can be any sequence or array like object.

An ```array``` is not limited to one dimensional arrays.  If the ```object``` parameter contains nested sequence information, the ```ndarray``` generated will reflect the structure of the sequence object.  For example, the following code converts a list of lists into a two dimensional array:

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

> What is the l2 norm?  Draw a right triangle with sides of the length provided in ```a```.  You will see that the value stored in ```l2``` is the length of the hypotenuse.  The final step of normalizing ```a``` by dividing it by ```l2``` gives the length of the sides of that triangle when projected onto the unit circle.
