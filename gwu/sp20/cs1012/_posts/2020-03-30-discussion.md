---
layout: post
title:  "Collections and Sequence Types (Strings, Lists, Tuples, Dictionaries)"
date:   2020-03-30 00:00:00 -0400
schedule:   2020-03-30 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
term: "sp20"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

### Introduction
In the previous [discussion on strings]({{ "/gwu/sp20/cs1012/2020/03/23/discussion.html" | absolute_url }}) we looked at indexing a string using the square brackets, ```[``` and ```]```, and we used the following diagram to represent how the data is organized within a string:

![HELLO WORLD LIST]({{ "/gwu/fa18/cs1012/assets/10_23_2018/helloworldarray.png" | absolute_url }})

A string represents a _**set**_ of characters.  A string is actually a specialized type of set because it has an _**order**_ or a _**sequence**_.  We often describe an ordered set as a _**list**_.  A character in a string is ordered by the position at which that character appears.

This concept of order or sequence plays an important role in the structuring of data.  We have regularly used variables to represent singular values; however, the management of many individual variables can increase the amount and complexity of code considerably which can also increase the amount of specificity and therefore decrease generalization and therefore decrease reusability.  We also wish to reduce code complexity wherever possible in order to minimize the possibility of bugs.

There are a number of Python _**sequence types**_ that allow programmers to represent sets of data in a few variables.  The fundamental positional sequence types discussed here are the _**string**_, _**list**_, and _**tuple**_.  This discussion will also introduce a sophisticated associative type called a _**map**_ or _**dictionary**_ that allows programmers to associate a _**key**_ with a value which allows a value to be retrieved the key rather than by position.

#### An Application
To motivate this discussion, let's consider how we would build a Python program that might hold movie information.  All movies share some classes of information so we want generalization.  For example, all movies have a title, a director, a number of actors, a production year, and a running time among other information.  Let's look at some concrete data that represents part of the information associated with the movie "Titanic":

```python
title = "Titanic"
director = "James Cameron"
actor1 = "Leonardo Dicaprio"
actor2 = "Kate Winslet"
actor3 = "Billy Zane"
year = 1997
length = 194
```

> Considering that movies involve hundreds of people on the production crew, we are only representing a small part of the data for each movie in these examples and we would need tens or hundreds of variables to give credit to everyone who contributed to a movie's production.  We will have a significant problem managing all the variables needed to credit everyone involved with one movie let alone a database of movies like IMDB if we use individual variables.

If we look at the overall movies that have been made, we quickly realize there are very few movies, if any, where all of the specific movie information is the same even if all movies share similar classes of information.  For example, there is only one and will ever only be one movie "Titanic (1997) directed by James Cameron starring Leonardo DiCaprio".  Even if there is a remake of the movie, that movie will share only some information like the title but both will be unique movies, made unique by the differences between contributors, years, and other production aspects.

While the above set of variables reflects some of the movie information, we will have a number of problems if we need to maintain data for more than one movie.  We have used the variable ```title``` to represent the title of "Titanic", but if we wish to represent an additional movie, we either have to overwrite ```title``` and lose information for "Titanic" or we have to create another set of variables that makes it more difficult to reuse our code.  For example, suppose we consider adding a second movie like "The Godfather" to our program, do we try to reuse the same variables that we used before:

```Python
title = "Titanic"
director = "James Cameron"
actor1 = "Leonardo Dicaprio"
actor2 = "Kate Winslet"
actor3 = "Billy Zane"
year = 1997
length = 194

title = "The Godfather"
director = "Francis Ford Coppola"
actor1 = "Marlon Brando"
actor2 = "Al Pachino"
actor3 = "Robert Duvall"
year = 1972
length = 175
```

By reusing the variables to hold information for "The Godfather", we have overwritten and lost the information for "Titanic".  If we need to store information for both, this approach will not work.

We might try to invent different variables; however, given that there are a number of variables that together hold the overall movie information, we would need to invent a new variable for each field.  The following code illustrates this approach:

```Python
movie1_title = "Titanic"
movie1_director = "James Cameron"
movie1_actor1 = "Leonardo Dicaprio"
movie1_actor2 = "Kate Winslet"
movie1_actor3 = "Billy Zane"
movie1_year = 1997
movie1_length = 194

movie2_title = "The Godfather"
movie2_director = "Francis Ford Coppola"
movie2_actor1 = "Marlon Brando"
movie2_actor2 = "Al Pachino"
movie2_actor3 = "Robert Duvall"
movie2_year = 1972
movie2_length = 175
```

We are now able to retain all the information for both movies; however, we have a large number of variables that must remain grouped together and we are losing some generalization by introducing a prefix onto each movie.  It is difficult to maintain all of the data with the individual variables and we need to write functions that take a large number of parameters which makes our code longer and more unwieldy.  For example, if we include a function to print the movie information, we have to pass each variable as its own parameter:

```Python
def printMovie(title, director, actor1, actor2, actor3, year, length):
    print(title, director, actor1, actor2, actor3, year, length)

movie1_title = "Titanic"
movie1_director = "James Cameron"
movie1_actor1 = "Leonardo Dicaprio"
movie1_actor2 = "Kate Winslet"
movie1_actor3 = "Billy Zane"
movie1_year = 1997
movie1_length = 194

movie2_title = "The Godfather"
movie2_director = "Francis Ford Coppola"
movie2_actor1 = "Marlon Brando"
movie2_actor2 = "Al Pachino"
movie2_actor3 = "Robert Duvall"
movie2_year = 1972
movie2_length = 175

printMovie(movie1_title, movie1_director, movie1_actor1, movie1_actor2, movie1_actor3, movie1_year, movie1_length)
printMovie(movie2_title, movie2_director, movie2_actor1, movie2_actor2, movie2_actor3, movie2_year, movie2_length)
```

Structuring the data as individual variables poses a number of its own problems.  The following assumptions are built into the structure:
1. All movies have only one director.
2. All movies have only three actors.
3. All movies have no other attributes other than the ones already listed.

These assumptions do not hold for all movies.  In order to represent movie data, we really need to be able to store movie data in a more flexible data structure.  Our data structure needs to be accommodate the variable nature of movie information from movie to movie and we would like to be able to use a single variable to hold and maintain movie information to simplify the interfaces to functions.  The remainder of this discussion will focus on how we can accomplish these goals.

### Terminology
Before addressing the specifics of the movie data structure problem, this section will first clarify some of the terminology that forms the basis of this discussion.

#### Collection
_**Collection**_ is a fancy word for a _**set**_.  A set is a pool of data that is used during computation.  All of the types in this discussion are collections of one form or another.

#### Sequence type
A _**sequence**_ is an _**ordered set**_.  A sequence is therefore a set and a collection with the constraint that it is also ordered.  A _**sequence type**_ is a data structure that is specifically designed to contain an _**ordered set**_.  The Python types _**string**_, _**list**__, and _**tuple**_ are all sequence types.  Each of these types is ordered by position, _i.e._ the position of the item in the set.

#### Map
A _**map**_ is a collection that allows a _**key**_ to be associated with a _**value**_.  The Python type _**dictionary**_ is a map.  A dictionary is ordered by key and provides fast retrieval of data from the map if the key is known.  

#### Mutability
_**Mutablity**_ describes whether data inside a variable can change once an initial value has been assigned to the variable.  A type can be _**mutable**_ meaning that data stored in a variable of that type can be changed after creation or a type can be _**immutable**_ meaning that data stored in a variable of that type cannot be changed after creation.  A developer may choose to use an immutable type to ensure that data is protected in certain usages.

Variables of type ```int``` and ```float``` are mutable while the ```string``` type as immutable.  We will revisit this concept with regard to various sequence types in this discussion.

### The Python List
A list is a sequence type that allows a programmer to store a number of values in a single variable.  A Python list is created using the square brackets.  For example, the following code creates a list ```lst``` of ```int```s:

```Python
lst = [1,3,4,7]
```

One unique aspect of Python is values in the Python list do not have to have the same type, _i.e._ we can store a list of ```int```s or ```float```s or we can store a list containing ```int```s, ```float```s, ```string```s, or even other sequence types.  For example, the following code creates a list that contains a mixed variety of data types.

```Python
lst = [5, 2.1, "hello", [1,3,4,7]]
```

Given the above capability, we can now revisit our movie example and condense the movie data significantly.  If we use a list, we do not need to maintain a large number of variables and we can even embed fields with varied length inside the list by using another list.  For example, we can express the movie data for examples in the following way:

```Python
titanic = ["Titanic", ["James Cameron"], ["Leonardo Dicaprio", "Kate Winslet", "Billy Zane"], 1997, 194]

godfather = ["The Godfather", ["Francis Ford Coppola"], ["Marlon Brando", "Al Pachino", "Robert Duvall"], 1972, 175]
```

By using a list, we have addressed many of the concerns raised in the introduction.  This new data structure expresses the director data as a list so it is possible to store more than one director in the director field.  This new data structure also expresses the actors as a list so we can store a different number of actors to reflect the different sizes of casts for different movies.  We have reduced the number of variables down to one, so we no longer have to maintain or pass many different values to handle a single movie.

We have applied a structure to our movie information.  The generalized structure is:
```
[<title>, <director(s)>, <actor(s)>, <year>, <length>]
```
If we design our programs to interact with this structure, we can pass a lot of information to and from functions using one list or one _**record**_.  IMDB is simply a comprehensive set of movie records.

#### Counting the Number of Elements in a List
We can ask a list how many values are stored in the list by using the ```len``` function.  For example:

```Python
a = [1,3,4,7]
n = len(a)
print(n)
```
The above code produces the following output:
```
4
```

> Note that we already found that we can use ```len``` with strings.  Strings are sequence types and ```len``` returns the length of a sequence type.  Because both strings and lists are sequence types, there are a number of functions that operate on both types (and any other sequence type).

With ```len```, we can ask Python to count the number of fields in our movie data structure.  For example:

```Python
titanic = ["Titanic", ["James Cameron"], ["Leonardo Dicaprio", "Kate Winslet", "Billy Zane"], 1997, 194]

print(len(titanic))
```

The above code produces the following output:
```
5
```

The count is ```5``` because the second and third fields are lists and count as a single value in terms of the length.  We can count the lengths of these fields individually to find out how many directors or actors are associated with a movie; however, we will need to be able to access individual elements in order to do so.

#### Accessing List Elements
We can access elements in the list using the same _**indexing operators**_, _i.e._ square brackets ```[``` and ```]```, that we used to access individual characters in a string.  The brackets are also used to create the list; however, _the context of list creation is different than the context of list access or indexing_.  It is important to remember that we count from ```0``` in programming, so the first element is at position ```0```, the second element is at position ```1```, and the last element is at position ```n-1```.  For example, the following code accesses various elements in the list:

```Python
a = [1,3,4,7]
n = len(a)
print(a[0])      # prints the first element 1
print(a[1])      # prints the second element 3
print(a[n-1])    # prints the last element 7
```

The context of the square brackets in accessing is different than the context when used for creation and the syntax used for these two different contexts is distinct which clarifies the context to Python.  In creation, we are assigning a variable to the set inside the square brackets, _e.g._ ```a = [1,3,4,7]```.  When accessing, the square brackets are accompanied by the variable name, _e.g._ ```print( a[0] )```.  Even though we use the same bracket symbols in the code, the behavior is different because of the context provided by the syntax.  By providing a label preceding the open bracket, the context is interpreted as accessing the list as opposed to creation.  This contextual difference should not be too alien because we saw that the ```+``` operator in math is interpreted as addition while it is interpreted as concatentation when dealing with strings.

> We use the square brackets to access information stored in any collection type even though we may use different symbols to specify different sequence types.

We can also use negative numbers to access elements from the end of the list; however, there is a slight difference between the ways we count forwards and backwards.  When we count forwards, we count from ```0``` and ```0``` represents the first element.  Because there is no ```-0```, we use ```-1``` to represent the first element at the end of the list.  For example:

```Python
a = [1,3,4,7]
print(a[0])      # prints the first element 1
print(a[-1])     # prints the last element 7
```

In the context of the movie example, we need to be able to access the information stored in the list.  We can access certain fields using the brackets:

```Python
titanic = ["Titanic", ["James Cameron"], ["Leonardo Dicaprio", "Kate Winslet", "Billy Zane"], 1997, 194]

print( titanic[0] )     # prints the title "Titanic"
print( titanic[2] )     # prints the list of actors
print( titanic[4] )     # prints the running time 194
```

#### Checking List Membership
We may need to determine whether a value exists in the list or not.  Python provides the ```in``` keyword for this purpose.

You should be more than a little familiar with ```in``` because we have already used it when working with ```for``` loops.  For example, when we implement a ```for``` loop to count to ten we use ```in``` to express that ```i``` is in the sequence generated by ```range```:

```python
for i in range(10):
    print(i)
```

The ```in``` keyword has more utility and can be used to ask whether a value exists in a sequence:

```python
a = [1,3,4,7]
print( 4 in a )
```

The above code produces the following output:
```
True
```

The ```True``` result is printed because ```4``` exists in the list ```a```.

Conversely, we can also combine ```in``` with the logical operator ```not``` to ask whether a value does not exist in a list:

```python
a = [1,3,4,7]
print( 5 not in a )
```

The above code produces the following output:
```
True
```

The ```True``` result is printed because ```5``` does not exist in the list ```a```.

We can combine ```in``` with a ```for``` loop when iterating over a list in the same way that we did with integers in order to retrieve every element in the list regardless of the type of the element.  We iterate over our own list of integers:

```python
a = [1,3,4,7]
for i in a:
  print(i)
```

Or we can iterate over a more diverse list such as our movie data structure:

```python
titanic = ["Titanic", ["James Cameron"], ["Leonardo Dicaprio", "Kate Winslet", "Billy Zane"], 1997, 194]

for field in titanic:
  print(field)
```

#### Lists are Mutable
Lists are mutable meaning that we can change a value that was initially stored in the list.  Recall that strings are immutable meaning that we cannot change a character in a string after the string is created.  Mutability is important when we are trying to assign a value to an element in a list using the accessor, _i.e._ square brackets.  For example, this example assigns a different value to the third element in the list:

```python
a = [1,3,4,7]
a[2] = 10
```

Practically speaking, mutability describes whether or not an accessor can appear on the left side of the assignment operator.  Strings are immutable, so we cannot assign a particular element using an accessor (A string accessor cannot appear on left side of the assignment operator); however, we can retrieve a particular element (A string accessor can appear on the right side of the assignment operator).  Lists are mutable, so we can both assign and retrieve a particular element using an accessor (A list accessor can appear on either the left or the right side of the assignment operator).

Mutability for our movie example means that we can update a field.  For example, if we realize that we made a mistake, we can fix the mistake:

```python
titanic = ["Avatar", ["James Cameron"], ["Leonardo Dicaprio", "Kate Winslet", "Billy Zane"], 1997, 194]

titanic[0] = "Titanic"   # replace the movie name
```

Because the list is mutable, it is legal for us to reassign the first element after the list is created.

#### Concatentation and Append
We may wish to insert new fields into a list after it has been created.  In fact, we may wish to start with an empty list and progressively add data until we have built up the list that we need.  In order to support this, we have the ability to use _**concatenation**_ or _**appending**_.

Concatentation relies on the ```+``` operator and it works the same way it did with strings.  The ```append``` method gives a slightly different way to also add data to the end of a list.  These two approaches allow us to produce a similar result, but there is a subtle difference between the two that is important to consider.

Concatenation of a list involves concatenating another list onto the end of the other list.  This operation is **not** performed "in place" meaning that you must assign the new list to a variable even if it was the original variable.  Here is an example:

```python
a = [1,2]        # the initial list
b = a + [3,4]    # concatentate onto a and assign as b
print(b)
```

The above code produces the following output:
```
[1,2,3,4]
```
Note that concatenation merged the two lists into a single list.

Appending to a list involves inserting a new element at the end of the list.  This operation is performed "in place" meaning that the original list is altered.  Here is an example:

```python
a = [1,2]
a.append(3)
a.append(4)
print(a)
```
The above code produces the following output:
```
[1,2,3,4]
```

Contrast the two examples given above.  Concatentation preserved the original list and requires assignment to determine where to store the new list and appending altered the original list.  We were able to join two entire lists in one operation using concatenation while appending required an individual operation for each element we joined to the list.

If we had attempted to append the second set of elements as a list, we would have ended up with something quite different than the first example:

```python
a = [1,2]
a.append([3,4])
print(a)
```

Produces the following output:

```
[1, 2, [3, 4]]
```

This second set of code has produced a list inside the list.  The third element is actually a list containing two elements and does not reflect the same structure that was produced by the first two examples.

#### Slicing
We may wish to access more than one value in a list.  We could accomplish through looping and copying values into another list; however, Python provides a convenient way to access multiple elements using one notation which is called _**slicing**_.

Slicing notation is a form of shorthand.  We have so far accessed elements in a list by providing the index or position of the element to access.  Instead of an index, we can use the slicing notation in the accessor to specify a range of values that we wish to access.

The colon ```:``` indicates a range of values.  If the colon appears alone, it means all values in the range.  For example:

```python
a = [1,2,3,4]
b = a[:]        # b will contain everything in a
```

The colon is more flexible than just expressing all.  It can be combined with various indices to represent different subsets.  If a number precedes the colon, then the number indicates the index where the slice will start, and if a number follows the colon, the number indicates the index after where the slice will end.

```python
a = [1,2,3,4]
b = a[2:]        # b will contain [3,4]
c = a[:2]        # c will contain [1,2]
d = a[1:3]       # d will contain [2,3]
```

One last shorthand of note for slicing that is provided is to reverse the slice automatically.  To do this, we use two colons together followed by ```-1```.  For example, the following code generates a slice that has the reverse ordering of ```a```:

```python
a = [1,3,4,7]
print(a[::-1])
```

#### Lists as Parameters
Just like any other types, we can pass a lists as a parameter to a function.  This can greatly simplify the way we define functions.  As an example, let's revisit the earlier ```printMovie``` example.

Our original implementation required that all fields be passed individually.  For example:

```Python
def printMovie(title, director, actor1, actor2, actor3, year, length):
    print(title, director, actor1, actor2, actor3, year, length)

title = "Titanic"
director = "James Cameron"
actor1 = "Leonardo Dicaprio"
actor2 = "Kate Winslet"
actor3 = "Billy Zane"
year = 1997
length = 194

printMovie(title, director, actor1, actor2, actor3, year, length)
```

This implementation is very cumbersome.  We have shown that all movie data can be built into a single list, so we could significantly reduce the amount of code if pass the list to ```printMovie``` instead:

```Python
def printMovie(movie):
    print(movie[0], movie[1][0], movie[2][0], movie[2][1], movie[2][2], movie[3], movie[4])

titanic = ["Titanic", ["James Cameron"], ["Leonardo Dicaprio", "Kate Winslet", "Billy Zane"], 1997, 194]

printMovie(titanic)
```

The above approach has greatly reduced the amount of Python code needed to achieve the same goal.  There are still some issues that we will need to address such as the assumption in ```printMovie``` that all movies have one director and all movies have only three actors.  If we build a string and iterate over the different fields, the ```printMovie``` function will better accommodate variability in the fields:

```Python
def printMovie(movie):
    s = ""
    s += movie[0]
    for director in movie[1]:
        s += " " + director
    for actor in movie[2]:
        s += " " + actor
    s += " " + str(movie[3])
    s += " " + str(movie[4])
    print(s)

titanic = ["Titanic", ["James Cameron"], ["Leonardo Dicaprio", "Kate Winslet", "Billy Zane"], 1997, 194]

printMovie(titanic)
```

### The Python [```tuple```](https://docs.python.org/3.1/tutorial/datastructures.html#tuples-and-sequences)
Python provides another sequence type that is very similar to the list called the _**tuple**_.  The same features, _e.g._ accessors and slicing, and functions, _e.g._ ```len```, work on tuples; however, there is one key difference, _a tuple is immutable like a string_.

In Python, a tuple is constructed using parentheses rather than using the square brackets used for a list, and when a tuple is printed, it will be printed in parentheses.  For example, the following code creates a tuple named ```t```:
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
Note that we can use the built in ```len``` function to find the length of a tuple and _we can access elements of the tuple using the same square bracket notation that is used to access members of a list_.  The main difference between a list and a tuple is that we cannot change a value in a tuple after it has been created.  For example, the following code produces an error:
```python
t = (1,2,3)        # define t as a tuple
t[0] = 0           # attempt to reassign an element of t
```
The error produced is:
```
TypeError: 'tuple' object does not support item assignment
```

> We have used parentheses in multiple contexts throughout the course.  Parentheses are grouping operators in expressions and they are used in both function definition and function calling.  How does Python know how to interpret parentheses?  It is handled just like the square brackets.  If parentheses are encountered with a label preceding the open parenthesis, it is interpreted as related to a function, if parentheses are encountered in an expression, they are interpreted as grouping operators, and otherwise parentheses are interpreted as creating a tuple.

### The Python Dictionary
There is one final issue with the movie data that is difficult to resolve with the list structure and that is what if the movie definition has a slightly different structure.  We will attempt to accommodate the possible variability of the structure using a _**dictionary**_.

A _**dictionary**_ is both a collection and a sequence type.  It is a special type of collection called a _**map**_.  A map associates a unique string _**key**_ with a value of any type.  As an illustration, consider how the English dictionary is organized: the words in the English dictionary are the keys and the definitions of a word are the values that we look up.

In terms of ordering, the Python dictionary will be ordered on the keys regardless of the order in which items were added to the dictionary.  This is in contrast to the ordering of lists and tuples which are ordered on which position a value was inserted into the data structure.

To access data in the dictionary, we use the same accessor that we use with lists, _i.e._ square brackets; however, we do not provide an index in the accessor but instead provide the key.  We can iterate over a dictionary using the same approach used with lists or tuples; however, we iterate over the keys only.

In order to specify to Python that we are defining a dictionary, we use curly braces, _i.e._ ```{``` and ```}```, instead of the square brackets we use for lists and the parentheses we use for tuples.  For example, we can declare that ```d``` is a dictionary using the following code:

```python
d = {}      # d is a dictionary
```

A dictionary is mutable, so we can add new values into the dictionary by assigning a value to a specific key.  For example, the following code adds the key ```'hello'``` to the dictionary and assigns it the value ```'world'```:

```python
d = {}
d['hello'] = 'world'
print( d['hello'] )
```

The above code produces that following output:

```
world
```

We can define these associations on the fly as we did above, or we can define these associations when we create the dictionary.  When defining an association on creation, we use the colon ```:``` to show the association between key and value.  For example, the following code produces the same output as the previous example, except the association is made when the dictionary is created:

```python
d = {'hello':'world'}
print( d['hello'] )
```

We can add more key value pairs by separating each pair with a comma:

```python
d = {'hello':'world', 'cs1012':'introduction to programming with python'}
print( d['hello'] )
print( d['cs1012'] )
```

If we wish to retrieve all values stored in the dictionary, we have to iterate over the keys and then retrieve the associated values.  The following code demonstrates one way that we can retrieve all key-value pairs in the dictionary:

```python
d = {'a':1, 'b':2, 'c':3}

for k in d:
    print(k, d[k])
```

With respect to our movie example, we can now define a very sophisticated data structure that mixes dictionaries and lists to store all of our movie information.  If each movie is stored as a dictionary, we can attach labels to each field and the ordering of the fields becomes irrelevant.  For example, our last iteration of the movie structure looked like the following:

```Python
def printMovie(movie):
    s = ""
    s += movie[0]
    for director in movie[1]:
        s += " " + director
    for actor in movie[2]:
        s += " " + actor
    s += " " + str(movie[3])
    s += " " + str(movie[4])
    print(s)

titanic = ["Titanic", ["James Cameron"], ["Leonardo Dicaprio", "Kate Winslet", "Billy Zane"], 1997, 194]

printMovie(titanic)
```

When we call ```printMovie```, all of the fields have to be present and have to fall in the correct location in the list.  We can add more flexibility in if we associate keys with the fields.  For example:

```Python
titanic = { "title":"Titanic",
            "directors":["James Cameron"],
            "actors": ["Leonardo Dicaprio", "Kate Winslet", "Billy Zane"],
            "year": 1997,
            "time": 194 }
```

This new structure can better accommodate special cases where a movie has unique properties, _e.g._ an additional field or a missing field.
s
If we adjust ```printMovie``` to recieve a dictionary we can handle variations a little more robustly and we can label all fields:

```Python
def printMovie(movie):
    s = ""
    s += movie['title']
    for director in movie['directors']:
        s += " " + director
    for actor in movie['actors']:
        s += " " + actor
    s += " " + str(movie['year'])
    s += " " + str(movie['time'])
    print(s)

titanic = {
    "year": 1997,
    "actors": ["Leonardo Dicaprio", "Kate Winslet", "Billy Zane"],
    "directors":["James Cameron"],
    "title":"Titanic",
    "time": 194
}

printMovie(titanic)
```

Finally, we take this even a step further by creating a dictionary of movies.  If we do so, we no longer need individual variables to reference specific movies.  We can instead use on variable to represent all movies.  For example:

```Python
def printMovie(movie):
    s = ""
    s += movie['title']
    for director in movie['directors']:
        s += " " + director
    for actor in movie['actors']:
        s += " " + actor
    s += " " + str(movie['year'])
    s += " " + str(movie['time'])
    print(s)

movies = {
           "titanic": {
             "title":"Titanic",
             "directors":["James Cameron"],
             "actors": ["Leonardo Dicaprio", "Kate Winslet", "Billy Zane"],
             "year": 1997,
             "time": 194
           },
           "godfather": {
             "title":"The Godfather",
             "directors":["Francis Ford Coppola"],
             "actors": ["Marlon Brando", "Al Pachino", "Robert Duvall"],
             "year": 1972,
             "time": 175
           },
         }

for key in movies:
    printMovie(movies[key])
```
