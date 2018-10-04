---
layout: post
title:  "Boolean Logic and Conditionals"
date:   2018-10-02 00:00:00 -0400
schedule:   2018-10-02 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
reading: "HtTLaCS 8.1-8.7"
exercises: "/gwu/fa18/cs1012/2018/10/02/exercises.html"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

### Boolean Values
A boolean value has one of two values: ```True``` or ```False```.  In Python ```True``` and ```False``` are keywords.  Recall that Python is case sensitive, so these values must be capitalized.  Evaluating the following code produces the subsequent output:

```python
print(True)
print(type(True))
print(type(False))
```
```
True
<class 'bool'>
<class 'bool'>
```

Note that boolean values are of type ```bool```.

### Comparison Operators
We can also form expressions using comparison operations.

**Question**: What type of answer does a comparison produce?  For example, what possible values could be assigned to ```r``` by the expression ```r = a > b```?

A boolean expression evaluates to a boolean value.  The equality operator ```==``` compares whether or not two values are equal and produces a boolean result.  For example:
```python
print(2 == 2)
print(2 == 5)
```
```
True
False
```
In the first case, ```2``` equals ```2```, so the expression evaluates to ```True```, and in the second case, ```2``` does not equal ```5```, so the expression evaluates to ```False```.

> The equality operator ```==``` is different than the assignment operator ```=```.  These operators are interpeted differently.  Remember that computers are dumb and only do what you tell them.  Do not confuse the two.  If you use assignment in place of equality or vice-versa, your program will not operate in the way that you expected.

The comparison operators are the following binary operators:
* ```a == b``` : Is ```a``` equal to ```b```?
* ```a != b``` : Is ```a``` not equal to ```b```?
* ```a > b``` : Is ```a``` greater than ```b```?
* ```a >= b``` : Is ```a``` greater than or equal to ```b```?
* ```a < b``` : Is ```a``` less than ```b```?
* ```a <= b``` : Is ```a``` less than or equal to ```b```?

> Recall that in assignment, _i.e._ ```=```, the variable must appear on the left side.  In comparison, the order of left or right does not matter to the computer, so ```x == 1``` is the same expression as ```1 == x```.  However, to a human, ```1 == x``` is difficult to interpret, so it is always recommeded that you structure your comparisons as ```x == 1``` for readability.

### Boolean Operators
There are three boolean operators: ```not```, ```and```, and ```or```.  ```not``` is a unary operator, and ```and``` and ```or``` are binary operators.  The semantics of these operators is similar to the semantics of these words in English.

#### Boolean ```and```
The boolean ```and``` operator is a binary operator.  In an ```and``` operation, the expression is ```True``` only if _**all**_ operands evaluate to ```True``` and the expression is ```False``` if _**any**_ operand evaluates to ```False```.  The following table summarizes the evaluation of ```and``` given the truth value of the operators:

| ```p```     | ```q```     | ```p and q``` |
|:----------- |:-----------:|:-------------:|
| ```True```  | ```True```  | ```True```    |
| ```True```  | ```False``` | ```False```   |
| ```False``` | ```True```  | ```False```   |
| ```False``` | ```False``` | ```False```   |

The expression ```x > 0 and x < 5``` means that ```x``` must be greater than ```0``` and ```x``` must also be less than ```5```.  This means that ```x``` must be exclusively between ```0``` and ```5```, _i.e._ ```x``` cannot be equal to either.  If ```x``` is between ```0``` and ```5``` the expression will evaluate to ```True``` and otherwise will evaluate to ```False```.

#### Boolean ```or```
The boolean ```or``` operator is a binary operator.  In an ```or``` operation, the expression is ```True``` if _**any**_ operand evaluates to ```True``` and the expression is ```False``` if _**all**_ of the operands evaluate to ```False```.  The following table summarizes the evaluation of ```or``` given the truth value of the operators:

| ```p```     | ```q```     | ```p or q```  |
|:-----------:|:-----------:|:-------------:|
| ```True```  | ```True```  | ```True```    |
| ```True```  | ```False``` | ```True```    |
| ```False``` | ```True```  | ```True```    |
| ```False``` | ```False``` | ```False```   |

The expression ```n % 2 == 0 or n % 3 == 0``` evaluates to ```True``` if ```n``` is a divisible by either 2 or 3 and otherwise evaluates to ```False```.

> Consider the example given for ```and``` but replaced with ```or```, _i.e._ ```x > 0 or x < 5```.  For what values of ```x``` would thie evaluate to ```True```?  The answer suggests that you must be very careful when designing conditional logic.

#### Boolean ```not```
The boolean ```not``` operator is a unary operator.  In a ```not``` operation, the expression is ```True``` if the operand is ```False``` and the expression is ```False``` if the operand is ```True```.  Conceptually, the ```not``` operation is the boolean equivalent to the mathematical unary ```-``` operator.  The following table summarizes the evaluation of ```not``` given the truth value of the operator:

| ```p```     | ```not p``` |
|:-----------:|:-----------:|
| ```True```  | ```False``` |
| ```False``` | ```True```  |

```not  x > y``` is ```True``` if ```x > y``` is ```False```, that is, if ```x``` is less than or equal to ```y```.

#### Warnings on Boolean Expressions
Remember that comparisons and most boolean operators are "binary" operations meaning that they operate on the operands that appear to the immediate left and right of the operator.  We must therefore structure logic to make binary operations.  If we wish to check whether "a variable n is equal to 5, 6, or 7", we must structure our logic correctly for the computer.  The correct way to structure this comparison is either ```n == 5 or n == 6 or n == 7``` or ```n >= 5 and n <= 7```.

Another common mistake deals with comparison of floating point values.  Recall that the representation of floating point values relies on approximate values.  The consequence of this is that a floating point value is rarely equal to another value if one of those values is computed, and therefore it is very likely that equality comparisons will fail.  You should structure your logic to accommodate this error if you are performing comparisons on floats.  For example, consider the output from the following code:

```python
x = 0.0
dx = 0.0001
for i in range(10000):
  x = x + dx
print(x == 1.0)
print(x)
```
```
False
0.9999999999999062
```
Analytically, the above code should be equivalent to ```0.00001*10000``` which should produce a result that is equal to ```1.0```, but due to floating point approximation, it is not.  If a comparison depends on the exactness of this answer, it will fail.

### Operator Precedence
Boolean operators have lower precedence than mathematical operators and each of the boolean operators have different precedence from one another.  The easiest way to remember the precedence among boolean operators is to consider the ```not``` is like mathematical negation, ```and``` is like multiplication, and ```or``` is like addition.

Grouping operators, _i.e._ parentheses, can be used in boolean expressions to control the order of operations just like in mathematical expressions.

Each operator has a precedence which is the same as that used in mathematics.
1. Grouping operators ```(``` and ```)```
2. Binary math operator ```**```
3. Unary math operator ```-```
4. Binary math operators ```*```, ```/```, ```//```, and ```%```
5. Binary math operators ```+``` and ```-```
6. Binary comparison operators ```<```, ```<=```, ```>```, ```>=```, ```!=```, and ```==```
7. Unary boolean ```not```
8. Binary boolean ```and```
9. Binary boolean ```or```

[Python Operator Reference](https://docs.python.org/3/reference/expressions.html#operator-precedence)

_________

### Conditionals
We introduced _**flow control**_ with the ```for``` loop.  We can also control the flow of execution by checking conditions and changing a program's behavior according to the state of a condition.  _**Conditional statements**_ control the _**branching**_ of a program depending on whether a condition is true or false.

#### "if" Conditional
The most basic form of conditional statement is indicated by the ```if``` keyword which is followed by a boolean expression.  The basic conditional statement has the following structure:

```python
if BOOLEAN_EXPRESSION:
    # This block or branch is only processed if BOOLEAN_EXPRESSION is True
    STATEMENTS
```
In the above ```if``` statement, the body of the ```if``` statement is only evaluated if ```BOOLEAN_EXPRESSION``` is evaluated as ```True```.  Note that the structure of the ```if``` block follows the same conventions that have been established with both the ```for``` and ```def``` structures, _i.e._ the ```if``` statement must end with a colon and the body of the block must be indented.

> The book refers to this as a "unary conditional"

#### "if-else" Conditional

The ```if``` statement may also be accompanied by an ```else``` block to form an "if-else" conditional structure.  Statements in the ```else``` block are only evaluated if the ```BOOLEAN_EXPRESSION``` in the ```if``` statement is evaluated to ```False```.  An "if-else" conditional has the following structure:
```python
if BOOLEAN_EXPRESSION:
    # This block is only processed if BOOLEAN_EXPRESSION is True
    STATEMENTS1
else:
    # This block is only processed if BOOLEAN_EXPRESSION is False
    STATEMENTS2
```
Note that the ```else``` block follows the same conventions as the ```if``` block.

> The book refers to this as a "binary conditional"

#### "if-else if-else" Conditional
A conditional ```if``` can also be followed by a number of "else if" statements that are indicated by the ```elif``` keyword to form an "if-else if-else" conditional structure.  An ```elif``` is both an ```else``` and an ```if``` conditional, so the ```elif``` must be followed by a boolean expression that controls whether the ```elif``` block is processed.  An "if-else if-else" conditional has the following structure:
```python
if BOOLEAN_EXPRESSION1:
    # This block is only processed if BOOLEAN_EXPRESSION1 is True
    STATEMENTS1
elif BOOLEAN_EXPRESSION2:
    # This block is only processed if BOOLEAN_EXPRESSION1 is True
    STATEMENTS2
else:
    # This block is only processed if BOOLEAN_EXPRESSION1 and BOOLEAN_EXPRESSION2 are False
    STATEMENTS3
```
Only one of the branches will be exectuted, _i.e._ the first branch where the conditional evaluates to ```True``` or the ```else``` block if none of the conditionals evaluate to ```True```.

> The book refers to this as a "chained conditional"

### Nested Conditionals
```python
if BOOLEAN_EXPRESSION:
    # This block or branch is only processed if BOOLEAN_EXPRESSION is True
    STATEMENTS
    if NESTED_BOOLEAN_EXPRESSION:
        # This block or branch is only processed if NESTED_BOOLEAN_EXPRESSION is True
        NESTED_STATEMENTS
```

### Boolean Functions
Functions can return a boolean value.  Suppose that we are writing a program that regularly checks whether a value is odd or not.  We can write a function that explicitly checks the condition and returns the corresponding truth value.  For example, the following function ```isOdd(x)``` returns ```False``` if the parameter ```x``` is even and returns ```True``` if ```x``` is odd:
```python
def isOdd(x):
    if x % 2 == 0:
        result = False
    else:
        result = True
    return result
```
We can use this function in a conditional statement.  Suppose we need to branch our program one way if the variable ```y``` is odd and another way if ```y``` is even.  The following code illustrates this usage of ```isOdd```:
```python
def isOdd(x):
    if x % 2 == 0:
        result = False
    else:
        result = True
    return result

y = int(input("Enter a number: "))
if isOdd(y):
    print("You entered an odd number.")
else:
    print("You entered an even number.")
```
If you enter ```1```, ```isOdd``` returns ```True``` and the main program decends into the ```if``` branch; however, if you enter ```2```, ```isOdd``` returns ```False``` and the main program decends into the ```else``` branch.

### Structuring Functions that Contain Conditionals
Now that we have established conditionals, you should see that ```return``` does not have to appear at the end of a function.  We have also established that when the ```return``` keyword is encountered, the function immediately exits.

We can return inside the branches themselves as in the following example:
```python
def isOdd2(x):
    if x % 2 == 0:
        return False
    else:
        return True
```
Or we can limit the number of branches by assuming a return value if the branch conditions fail.  The following example demonstrates this concept:

```python
def isOdd3(x):
    if x % 2 == 0:
        return False
    return True
```

The structures of ```isOdd``` or ```isOdd3``` are generally the safest models.  If conditionals are nested at multiple levels inside one another, it is difficult to debug and it is easy to overlook a return case.
