---
layout: post
title:  "Classes and Objects"
date:   2019-04-22 00:00:00 -0400
schedule:   2019-04-22 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
term: "sp19"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

### Introduction
A "paradigm" is a model that guides how information is structured.  We use the term "[programming paradigm](https://en.wikipedia.org/wiki/Programming_paradigm)" to describe the structural approach prescribed by a language.

So far, we have followed the _**procedural programming paradigm**_.  The procedural paradigm relies on functions (procedure is just another name for function) as the principle organizational component in the programming language.  The procedural approach is one of the first models developed to provide coding structure; however, there have been additional paradigms introduced into programming languages in order to address specific organizational needs.

In the 1980's the _**[object-oriented programming paradigm](https://en.wikipedia.org/wiki/Object-oriented_programming)**_, abbreviated as _**OOP**_, became widely adopted.  OOP relies on the _**```class```**_ as a fundamental organizational component for software development.  OOP revolves around the use of and interaction between objects, _i.e._ instances of classes, to organize and execute.  OOP is best suited to very large programs, so applying OOP to very small programs is generally unnecessary and can significantly increase the amount and complexity of code.  

>Some programming languages are structured entirely on one programming paradigm while others enable a programmer to select the best applicable paradigm for their needs.  For example, Java is entirely based in the object-oriented paradigm so users must conform in order to use the language.  C++ and Python allow the programmer to mix procedural and object oriented paradigms as needed so these languages are designed to conform to the programmer's needs.

For some applications, an OOP approach adds significant amounts of work that returns little in terms of capability.  For example, if a program will only be run once or must be developed very quickly, an object oriented approach may impede development by adding in additional work.  A procedural approach is often good enough to develop small applications with very specific goals and a limited range of user inputs.

#### Paradigms in Python

In this course, we have focused on the fundamental concepts of programming and on Python specific features.  The fundamental concepts have taught you a foundation that will be applicable in any programming language and the Python specific features have taught you aspects of Python that are novel and powerful.

Due to the Python language's design, Python can be written using a mixture of procedural and object-oriented approaches.  OOP is introduced here so that you may be aware of the object model and its organizational nature; however, OOP is not a necessary feature to produce many Python programs as we have demonstrated so far.

This discussion is provided as a primer for future programming with Python or other languages.  We introduce OOP here because whether you know it or not, we have assumed and relied on OOP in our earlier work and this discussion may help answer lingering questions from some of the previous topics.

If this course has stimulated your interest in programming, you are encouraged to study classes as they will be a critical component to many languages or large projects.

### Objects as Instances
An object is a unique instance.  We discussed this in the context of the [```turtle``` module]({{"gwu/fa18/cs1012/2018/09/25/discussion.html" | absolute_url }}).  Recall the following code presented in the section titled **Creating Unique Instances of ```turtle``` Objects**:

```python
import turtle

tina = turtle.Turtle()     # create an instance of a turtle named tina
# these statements explicitly control the instance of tina
tina.left(90)
tina.forward(100)
tina.left(90)
tina.forward(100)

turtle.done()
```

In the above code, we created an _**instance**_ of a ```turtle``` named ```tina```.  When we create an instance, we create a unique object.  For example, consider the following code:
```python
import turtle
tina = turtle.Turtle()     # create an instance of a turtle named tina
print(type(tina))
turtle.done()
```

The above code produces the following output:

```
<class 'turtle.Turtle'>
```

In short, when we check the type of ```tina```, Python indicates that ```tina``` is an instance of the ```turtle.Turtle```  class.

Instancing allows us to create objects that are unique and that can be operated on independent of other object instances.  ```tina``` is a unique ```Turtle``` that we can command independently of any other ```Turtle``` objects or any other types of objects.

For example, the following code creates two ```Turtle``` objects named ```alice``` and ```bob```.  We can issue different commands to ```alice``` and ```bob```, and they will respond independent of the commands issued to any other instances:

```python
import turtle
alice = turtle.Turtle()     # create an instance of a turtle named alice
bob = turtle.Turtle()    # create an instance of a turtle named bob
alice.color('red')
alice.forward(100)
bob.color('blue')
bob.backward(100)
turtle.done()
```
The above code draws the following image:

![Alice and Bob]({{"/gwu/fa18/cs1012/assets/12_04_2018/aliceandbob.png" | absolute_url }})

We can see that there are two separate turtles on the screen and we can see that each has responded to a different set of commands.  The commands given to ```alice``` have resulted in the ```alice``` instance of a ```Turtle``` being drawn in red and moving forward.  The commands given to ```bob``` have resulted in the ```bob``` instance of a ```Turtle``` being drawn in blue and moving backward.

### Python Object Policy
It may not be clear yet, but Python actually treats everything as an object.  This is made suggested when we use the ```type()``` function to query the type of a variable.

We have worked primarily with primitive or built in types such as ```int```, ```string```, and ```list```.  If we use the ```type()``` function to query the type of any variables that are of the these types we get an indication that these variables belong to a ```class```.

For example, the following code establishes variables of the above types and then queries Python for the types of the variables:

```python
i = 0
print(type(i))
s = 'hello'
print(type(s))
l = [1,2,3,4]
print(type(l))
```

The above code produces the following output:
```
<class 'int'>
<class 'str'>
<class 'list'>
```

### State and Methods
Every object has a _**state**_ and a set of _**actions**_ that can be performed on that object.  The state is represented by a set of variables associated with the object and the actions are represented by a set of functions or _**methods**_ that can be performed on that object.

The following diagram shows that there is a fundamental difference between state and methods; however, they are both members of the same classification.

![Classification]({{"/gwu/fa18/cs1012/assets/12_04_2018/classification.png" | absolute_url }})

A more concrete example comes from ```Turtle```.

![Turtle Classification]({{"/gwu/fa18/cs1012/assets/12_04_2018/concreteclass.png" | absolute_url }})

We are most familiar with the actions/methods that can be performed on a ```Turtle``` which appear in the outer ring; however, each instance of a ```Turtle``` also has a number of attributes that hold the state of a ```Turtle``` instance at a given time such as ```pos```, ```color```, and ```heading```.

```Python
import turtle
# a function to print the state of a turtle
def printState(t):
    print(t.pos(),t.color(),t.heading())

# the main program
chuck = turtle.Turtle()
printState(chuck)
chuck.color('red')
chuck.forward(100)
printState(chuck)

turtle.done()
```

The above code produces the following output:

```
(0.00,0.00) ('black', 'black') 0.0
(100.00,0.00) ('red', 'red') 0.0
```

When ```printState``` is called at different steps in the program, the internal state of ```chuck``` has changed.  We did not manipulate ```pos``` directly.  It was through calling the ```forward``` associated with ```chuck``` that the internal state of ```chuck``` was changed.  Because ```chuck``` keeps track of its own position, we do not even need to know that there exists a variable that maintains position.

#### State as Attributes
An attribute is a variable defined for an object which is attached to and holds a value for the object's instance.  An object can have a large number of attributes of various types.

> The terms _**attribute**_, _**property**_, _**field**_, and _**member variable**_ are synonyms in terms of objects.  These terms are regularly used interchangably.  Some programming languages may officially adopt a particular nomenclature; however, these terms are generally understood to mean the same thing regardless of language.

Two instances differ from one another because the values stored in their attributes are unique to each instance.  Even if two instances have the same attributes, they are still distinctly different objects.  We might compare two objects to see if their attributes are the same and if the attributes are the same the objects may be equivalent; however, even if two instances are equivalent, they are still unique objects.

As an object's internal variables change, the state of the object evolves.  The state is really the snapshot of all internal variables for an object at a single given time.  We see this in the output from the above example with ```chuck```:

```
(0.00,0.00) ('black', 'black') 0.0
(100.00,0.00) ('red', 'red') 0.0
```

The first time that ```printState``` is called, ```chuck``` is positioned at (0,0), is assigned the color 'black', and has a heading of 0.  The second time that ```printState``` is called, ```chuck``` is positioned at (100,0), is assigned the color 'red', and has a heading of 0.  Between these two calls to ```printState```, the state of ```chuck``` has changed due to the calls to ```forward``` and ```color```.  The value for ```heading``` has not changed because the code does not call ```left``` or ```right```.

#### Actions through Methods
The term _**method**_ is another term for function; however, it describes functions that are specifically attached to an instance.

> The terms _**method**_ and _**member function**_ are synonyms in terms of objects.  These terms are regularly used interchangably.  Some programming languages may officially adopt a particular nomenclature; however, these terms are generally understood to mean the same thing regardless of language.

For general functions, we are able to pass variables and objects to the function as arguments and operate on those arguments within the function.  For example, in the example with ```chuck```, ```printState``` is just a function that takes in a ```turtle``` and reads data from the instance:

```python
def printState(t):
    print(t.pos(),t.color(),t.heading())
```

The turtle is specified as a parameter, _i.e._ ```t```, to the function.  This is in contrast to how the turtle actions are carried out.  For example, in the main program, ```chuck``` moves forward on this line:

```Python
chuck.forward(100)
```

```forward``` is a method defined in the ```Turtle``` class.  ```chuck``` is not passed to the forward method in the same way as the functions that we have typically defined in this course.  ```chuck``` is specified using the dot ```.``` operator instead.  This code is effectively asking ```chuck``` to move itself forward rather than asking a function to move ```chuck``` forward.  This distinction may not be entirely clear, but it is very powerful.

A method is associated with a specific instance.  In short, a method knows which instance is to be operated on without providing the object as a parameter.  Each object is responsible for managing its own internal state, and methods provide a clear definition of how that object can be interacted with.  Methods do not necessarily limit the types of actions and interactions that we can have with an object, but they typically define the most common and necessary actions that an object must support.

#### The dot operator
As mentioned above, the dot operator, ```.```, gives access to the underlying members.  We preceed the dot with the object name and follow the dot with the method or attribute that we wish to work with.

This should be somewhat familiar to you because we have used this nomenclature throughout the course to make use of features from the ```Turtle``` class, the Python ```math``` and ```random``` modules, and most recently using the ```numpy``` and ```matplotlib``` modules.  We have actually avoided using class instances in many so far; however, the dot operator works the same way to access functions that are defined inside a module as with objects.

One recent case where we have unknowingly accessed methods of a class are with the ```numpy.ndarray```.  We used the ```sum``` method of an ```numpy.ndarray``` to ask the array to compute its own mean value.  For example:

```Python
import numpy as np
a = np.arange(10)
print(a.sum())
```
In the above code, a has the type of ```numpy.ndarray``` and is an instance of an ```ndarray```.  The ```ndarray``` has a ```sum``` method defined inside its class definition that iterates through the array, accumulates the sum of all values in the array, and returns the accumulated total.  We do not need to write our own summation function nor implement any summation code ourselves to use this function.  If we create an instance of an array (one is created for us through the call to ```arange```), we can invoke any of the methods defined in the object's class.

### The ```class``` as a blueprint
We can think of the class definition as the blueprint for a model.  The class describes all of the aspects that an instance can have by providing all of the attributes and methods that are applicable to an instance.  Each instance has its own unique values for each attribute and therefore a unique state.  A method will typically operate on the state stored inside the instance.

In order to define our own class, we use the ```class``` keyword.  The following example demonstrates a class definition for a two dimensional point named ```Point``` and then uses an instance of the class:

```Python
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

# main program creates a point and prints its coordinates
p = Point()
print(p.x, p.y)
```

The above code creates an instance of the point on the line ```pt = Point()```.  This line calls the strange line that looks like a function in the ```Point``` class ```def __init__(self):```.  The strange not-a-function ```__init__``` is called a _**Constructor**_ because it constructs an instance of the class.

In the above code, we rely on the user to build containing the information stored inside the class.

While the point class definition is simple it offers significant capabilities: we can build our own custom data types, we can define methods that operate on the state stored in an instance of the class, and we can create multiple instances of a class.

> Note the indentation within the examples in this section and the following subsections.  In order to show Python what belongs to a class, we must indent everything that is inside of the class.

#### Defining a Method

We may instead wish to provide a method that produces a string that contains all of the class state instead.  For example:

```Python
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0
    def toString(self):
        s = "(" + str(self.x) + ", " + str(self.y) + ")"
        return s
# main program creates a point and prints its coordinates
p = Point()
print(p.toString())
```
The above program produces the following output:

```
(0, 0)
```

In the above example, the ```toString``` method creates a formatted string consisting of all of the relevant member variables (state) and then returns the string.

#### Creating Multiple Instances
With the ```Point``` class, we have the ability to create many instances of the ```Point``` class.  For example:

```Python
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0
    def toString(self):
        s = "(" + str(self.x) + ", " + str(self.y) + ")"
        return s
# main program creates a point and prints its coordinates
p = Point()
q = Point()
p.x = 1
p.y = 2
q.x = 11
q.y = 12
print("p", p.toString())
print("q", q.toString())
```
The above program produces the following output:

```
p (1, 2)
q (11, 12)
```

The output shows that ```p``` and ```q``` are unique instances.  Manipulation of one does not affect the other.

### The benefits of Object-Oriented Programming
OOP is based on three principles that are supported by the ```class```:
1. Encapsulation
2. Inheritance
3. Polymorphism

A deep discussion of these principles is beyond the scope of this class; however, the following cursory explanations will suffice for our purposes.

#### Encapsulation
Encapsulation means to enclose and to summarize.  Encapsulation promotes reusability and information hiding by hiding the gory details while exposing enough information to make use of the processes involved.

In the context of functions, we discussed that we only need to know what a function does and how to interact with it in order to use it.  We do not need to know exactly how a function works.  For example, I don't need to know either how to compute the standard deviation or how to operate on a ```numpy.ndarray``` in order to use the ```numpy.std``` function.  All I need to know is how to pass an array to the function and that it computes the standard deviation for an ```numpy.ndarray```.

Classes allow entire concepts to be encapsulated into a single object.  We do not need to know the details of the classes; however, we do need to know how to interact with it.  The manual for how to interact with the class is provided through the member functions.

The ```numpy.ndarray``` is a class.  We don't really know how it works; however, we do know that we can call the ```ndarray.mean()``` function and the ```ndarray``` will compute the average of all values in the array.  We do not need to know the details of how the ```ndarray``` is maintained or how the mean is actually computed within the ```ndarray``` data structure in order to get the requested information.  We simply have to call the exposed ```mean``` method and the ```ndarray``` class does all of the heavy lifting.

#### Inheritance
Inheritance is a way to express a relationship between two types of objects and allows us to reuse features from another class.  Inheritance is a "is a" or "parent-child" relationship.

Consider a case involving shapes.  Both a ```square``` and a ```circle``` are specific types of ```shape```.  There are certain rules or features associated with a ```shape``` that are intrinsic to all specific types of shape.  All shapes have an area and perimeter and we may wish to draw each shape.  We can express the fundamental requirements or characteristics of shape in ```shape``` class and we can express the relationship between a square or circle by inheriting our ```square``` class and or ```circle``` class from the ```shape``` class.

#### Polymorphism
Polymorphism means "many forms".  Due to inheritance, an object can be classified as both a ```shape``` and a ```square```.  Polymorphism is powerful feature that allows us to store different types of things in one data structure.  While the details are normally hidden from us, because Python treats all data as objects, we can store any type of object in a list.  For example, the following code stores a variety of types in a single list:

```Python
l = [1, 'hello',[1,2,3,4]]
for e in l:
    print(type(e),e)
```

The above code produces the following output:

```
<class 'int'> 1
<class 'str'> hello
<class 'list'> [1, 2, 3, 4]
```

It is through Polymorphism that this is possible.  Regardless of specific type, every type is also an object.  Lists are defined to store objects, so a list is able to store any type of value.
