---
layout: post
title:  "Conditional Control Structures"
date:   2019-09-30 00:00:00 -0400
schedule:   2019-09-30 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
reading: "HtTLaCS 3.1-3.5 & 6.1-6.3"
term: "fa19"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

### Boolean Values
A _**boolean value**_ has one of two values: ```True``` or ```False```.  In Python ```True``` and ```False``` are keywords.  Recall that Python is case sensitive, so these values must be capitalized.  Evaluating the following code produces the subsequent output:

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

Note that boolean values are of type ```bool``` and Python has a ```bool``` conversion function which allows non-boolean values to be converted to boolean values.  For example:

```python
x = 0
print(x,type(x))
x = bool(x)
print(x,type(x),"\n")

y = 1
print(y,type(y))
y = bool(y)
print(y,type(y),"\n")

z = -1
print(z,type(z))
z = bool(z)
print(z,type(z),"\n")
```

The above code produces the following output:
```
0 <class 'int'>
False <class 'bool'>

1 <class 'int'>
True <class 'bool'>

-1 <class 'int'>
True <class 'bool'>
```

The last set of operations on ```z``` may seem a little off.  How does -1 equate to ```True```?  Logic is based on the concept of 'false' and 'not false' where zero represents our accepted numerical representation of 'false'; therefore, 'not false' is any number that is not equal to zero.

> This premise of 'false' and 'not false' is the foundation of logical reasoning, _e.g._ the basis for scientific and legal arguments, and as a result all knowledge is provisional.  An argument is only sound if it is deeply explored and has not been disproven.

### Boolean Expression
A mathematical or numerical expression evaluates to a numeric value while a _**boolean expression**_ evaluates to a boolean value.  A boolean expression can simply consist of one boolean value or it may be composed of comparison operations, logical operations and boolean values.    

### Comparison Operators
We can also form a boolean expression using comparison operations expressed by _**comparison operators**_.  Some comparison operators resemble mathematical operators like greater than and less than while others like not equal are more unfamiliar.

**Question**: What type of answer does a comparison produce?  For example, what possible values could be assigned to ```r``` by the expression ```r = a > b```?

The equality operator ```==``` compares whether or not two values are equal and evaluates to a boolean value.  For example:
```python
print(2 == 2)
print(2 == 5)
```
```
True
False
```
In the first case, ```2``` equals ```2```, so the expression evaluates to ```True```, and in the second case, ```2``` does not equal ```5```, so the expression evaluates to ```False```.

> The equality operator ```==``` is different than the assignment operator ```=```.  These operators are interpreted differently.  Remember that computers are dumb and only do what you tell them.  Do not confuse the two.  If you use assignment in place of equality or vice-versa, your program will not operate in the way that you expected.

The comparison operators are the following binary operators:
* ```a == b``` : Is ```a``` equal to ```b```?
* ```a != b``` : Is ```a``` not equal to ```b```?
* ```a > b``` : Is ```a``` greater than ```b```?
* ```a >= b``` : Is ```a``` greater than or equal to ```b```?
* ```a < b``` : Is ```a``` less than ```b```?
* ```a <= b``` : Is ```a``` less than or equal to ```b```?

> Recall that in assignment, _i.e._ ```=```, the variable must appear on the left side.  In comparison, the order of left or right does not matter to the computer, so ```x == 1``` is the same expression as ```1 == x```.  However, to a human, ```1 == x``` is difficult to interpret, so it is always recommended that you structure your comparisons as ```x == 1``` for readability.

### Logical Operators
Logical operators join boolean expressions into more complex logical expressions.  There are three logical operators: ```not```, ```and```, and ```or```.  ```not``` is a unary operator, and ```and``` and ```or``` are binary operators.  The semantics of these operators is similar to the semantics of these words in English.

#### Logical ```and```
The logical ```and``` operator is a binary operator.  In an ```and``` operation, the expression is ```True``` only if _**all**_ operands evaluate to ```True``` and the expression is ```False``` if _**any**_ operand evaluates to ```False```.  The following table summarizes the evaluation of ```and``` given the truth value of the operators:

| ```p```     | ```q```     | ```p and q``` |
|:----------- |:-----------:|:-------------:|
| ```True```  | ```True```  | ```True```    |
| ```True```  | ```False``` | ```False```   |
| ```False``` | ```True```  | ```False```   |
| ```False``` | ```False``` | ```False```   |

The expression ```x > 0 and x < 5``` means that ```x``` must be greater than ```0``` and ```x``` must also be less than ```5```.  This means that ```x``` must be exclusively between ```0``` and ```5```, _i.e._ ```x``` cannot be equal to either.  If ```x``` is between ```0``` and ```5``` the expression will evaluate to ```True``` and otherwise will evaluate to ```False```.

#### Logical ```or```
The logical ```or``` operator is a binary operator.  In an ```or``` operation, the expression is ```True``` if _**any**_ operand evaluates to ```True``` and the expression is ```False``` if _**all**_ of the operands evaluate to ```False```.  The following table summarizes the evaluation of ```or``` given the truth value of the operators:

| ```p```     | ```q```     | ```p or q```  |
|:-----------:|:-----------:|:-------------:|
| ```True```  | ```True```  | ```True```    |
| ```True```  | ```False``` | ```True```    |
| ```False``` | ```True```  | ```True```    |
| ```False``` | ```False``` | ```False```   |

The expression ```n % 2 == 0 or n % 3 == 0``` evaluates to ```True``` if ```n``` is a divisible by either 2 or 3 and otherwise evaluates to ```False```.

> Consider the example given for ```and``` but replaced with ```or```, _i.e._ ```x > 0 or x < 5```.  For what values of ```x``` would thie evaluate to ```True```?  The answer suggests that you must be very careful when designing conditional logic.

#### Logical ```not```
The logical ```not``` operator is a unary operator.  In a ```not``` operation, the expression is ```True``` if the operand is ```False``` and the expression is ```False``` if the operand is ```True```.  Conceptually, the ```not``` operation is the boolean equivalent to the mathematical unary ```-``` operator.  The following table summarizes the evaluation of ```not``` given the truth value of the operator:

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


### Formulating Logical Expressions

A _**logical expression**_ is like a mathematical expression in that it is a compound boolean expression where individual boolean expressions are joined together by logical operators.  Where a mathematical expression resolves as a numerical value, a logical expression resolves as a truth value.

#### Example 1

The expression ```a and b``` depends on the truth values of ```a``` and ```b``` at the time the expression is evaluated.  We can also think of ```a``` as a symbolic placeholder for a more complex boolean or logical expression.  For example, consider how to form a logical statement for the following natural language definition...

> The statement is true when all of the conditions are true, ```x``` is non-zero, ```y``` is positive; otherwise, the statement is false.

We can break down each of the individual components are write boolean expressions for each and then join these boolean expressions with logical operators to form a logical expression that operates according to the rules outlined in the description.

"```x``` is non-zero" can be expressed with the boolean expression ```x != 0``` (It could also be expressed as ```not(x == 0)```, but this may be a little more difficult to understand).

"```y``` is positive" can be expressed with the boolean expression ```y > 0``` (Similar to the previous example, there are other ways to express this logical relationship).

We now need to formulate a logical expression using a logical operator that joins each of the individual boolean expressions and produces a result consistent with the desired logic.  In this case, we will join the two expressions using ```and```; because all of the conditions must be true in order for the overall statement to be true.  Our logical expression is therefore:

```python
x != 0 and y > 0
```

How can we prove that this logical expression is consistent with the intent of the original expression?  Let's use a truth table...

| ```x``` | ```y```  | ```x != 0``` | ```y > 0``` | ```x != 0 and y > 0``` |
|:-------:|:--------:|:------------:|:-----------:|:----------------------:|
| ```1``` | ```1```  | ```True```   | ```True```  | ```True```             |
| ```1``` | ```-1``` | ```True```   | ```False``` | ```False```            |
| ```0``` | ```1```  | ```False```  | ```True```  | ```False```            |
| ```0``` | ```-1``` | ```False```  | ```False``` | ```False```            |

We can use the symbolic placeholders ```a``` and ```b``` for the individual boolean expressions to see how this maps to the original ```and``` truth table.  Let's replace ```x != 0``` with the symbol ```a``` and ```y > 0``` with the symbol ```b```.  The truth table generated (the right hand side of the above table) is exactly the same as the ```and``` truth table defined earlier...

| ```a```     | ```b```     | ```a and b``` |
|:-----------:|:-----------:|:-------------:|
| ```True```  | ```True```  | ```True```    |
| ```True```  | ```False``` | ```False```   |
| ```False``` | ```True```  | ```False```   |
| ```False``` | ```False``` | ```False```   |

#### Example 2

Let's now consider forming a negative statement from a natural language definition.  Given the statement...

> The statement is false when any of the conditions are true, ```m``` is non-negative, ```n``` is even; otherwise, the statement is true.

This is confusing at first glance.  It is easiest to focus on the individual boolean expressions first and then build up the logical expression from the constituent boolean expressions.  

"```m``` is non-negative" can be expressed with the boolean expression ```m >= 0``` and "```n``` is even" can be expressed with the boolean expression ```n%2 == 0``` (Again, these can be expressed in a variety of ways).

So, how do we join these two expressions?  The keyword _any_ suggests that we use ```or``` which gives us the logical expression:

```Python
m >= 0 or n%2 == 0
```

However, if we draw this truth table, we will see that there is an inconsistency.  The original language suggests that the overall statement should be false if any of the constituent statements are true.  The solution is rather simple, we can simply use a ```not``` operator to change the invert the result of the statement...

```Python
not(m >= 0 or n%2 == 0)
```

Let's check this with a truth table:

| ```m``` | ```n``` | ```m >= 0``` | ```n%2 == 0``` | ```m >= 0 or n%2 == 0``` | ```not(m >= 0 or n%2 == 0)``` |
|:-------:|:-------:|:------------:|:--------------:|:------------------------:|:--------------------------------:|
| ```1``` | ```2``` | ```True```   | ```True```     | ```True```               | ```False```                   |
| ```1``` | ```1``` | ```True```   | ```False```    | ```True```               | ```False```                   |
| ```0``` | ```2``` | ```False```  | ```True```     | ```True```               | ```False```                   |
| ```0``` | ```1``` | ```False```  | ```False```    | ```False```              | ```True```                    |

Now, double check the logical consistency between the original natural language description and the result indicated by the truth table.  Based on the original description, the logical expression should be false anywhere that either of the constituent boolean expressions are true, so is this the case?  Yes it is.  What about the other cases where the logical statement should be true, _i.e._ when none of the constituent boolean expressions are true, is this the case?  Yes.

Rather than trying to contort the expression, we can simply interprete it then invert the result using ```not```.

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

The following flow chart models the ```if``` conditional structure:

![If Flowchart]({{ "/gwu/fa19/cs1012/assets/discussion05/if.png" | absolute_url }})

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

The following flow chart models the ```if-else``` conditional structure:

![If-Else Flowchart]({{ "/gwu/fa19/cs1012/assets/discussion05/if_else.png" | absolute_url }})

#### "if-else if-else" Conditional
A conditional ```if``` can also be followed by a number of "else if" statements that are indicated by the ```elif``` keyword to form an "if-else if-else" conditional structure.  An ```elif``` is both an ```else``` and an ```if``` conditional, so the ```elif``` must be followed by a boolean expression that controls whether the ```elif``` block is processed.  An "if-else if-else" conditional has the following structure:
```python
if BOOLEAN_EXPRESSION1:
    # This block is only processed if BOOLEAN_EXPRESSION1 is True
    STATEMENTS1
elif BOOLEAN_EXPRESSION2:
    # This block is only processed if BOOLEAN_EXPRESSION1 is False and BOOLEAN_EXPRESSION2 is True
    STATEMENTS2
else:
    # This block is only processed if BOOLEAN_EXPRESSION1 and BOOLEAN_EXPRESSION2 are False
    STATEMENTS3
```
Only one of the branches will be exectuted, _i.e._ the first branch where the conditional evaluates to ```True``` or the ```else``` block if none of the conditionals evaluate to ```True```.

> The book refers to this as a "chained conditional"

The following flow chart models the ```if-elif-else``` conditional structure:

![If-Elif-Else Flowchart]({{ "/gwu/fa19/cs1012/assets/discussion05/if_elif_else.png" | absolute_url }})

### Nested Conditionals
```python
if BOOLEAN_EXPRESSION:
    # This block or branch is only processed if BOOLEAN_EXPRESSION is True
    STATEMENTS
    if NESTED_BOOLEAN_EXPRESSION:
        # This block or branch is only processed if NESTED_BOOLEAN_EXPRESSION is True
        NESTED_STATEMENTS
```

The following flow chart models the nested ```if``` conditional structure:

![Nested If Flowchart]({{ "/gwu/fa19/cs1012/assets/discussion05/nested_if.png" | absolute_url }})

### Looping Control Structures
We have already discussed the ```for``` loop control structure which gives us the ability to iterate a number of times.  The ```for``` loop is the most widely used loop control structure because many times we know in advance that we will be iterating over a known range of numbers or on a data structure with a fixed size.

We have also studied variants of the ```if``` conditional which allows us to optionally branch the normal sequential flow of a Python script.

In addition to the ```for``` loop, we have a conditional loop structure that is defined using the ```while``` keyword.  A ```while``` loop has a structure that is more similar to the ```if``` conditional than the ```for``` structure.  The ```while``` loop has the following structure:
```python
while BOOLEAN_EXPRESSION:
    STATEMENTS
```

The following flow chart models the ```while``` control structure:

![While Flowchart]({{ "/gwu/fa19/cs1012/assets/discussion05/while.png" | absolute_url }})


If ```BOOLEAN_EXPRESSION``` evaluates as ```True```, then ```STATEMENTS``` will be executed.  Once the end of the loop body is reached, the process will go back up to the ```while``` statement and reevaluate ```BOOLEAN_EXPRESSION```.  If ```BOOLEAN_EXPRESSION``` is reevaluated as ```True``` the loop body will be processed again.  This behavior will repeat until some case inside ```STATEMENTS``` changes the state of the system such that ```BOOLEAN_EXPRESSION``` is evaluated as ```False```.  However, ```BOOLEAN_EXPRESSION``` will only be reevaluated when the process reaches the end of all statements inside the loop body.  For example, the following ```while``` loop will loop until ```x > 1000```:

```python
x = 1
while x < 1000:
  x = x * 2
```

A ```while``` loop can iterate an infinite number of times which is often called an _**inifinte loop**_, meaning that the loop will never terminate.  While it is possible, it is generally difficult to inadvertantly create an infinite ```for``` loop.  A programmer must be very careful and make sure that the logic that controls a terminating condition is correctly implemented when working with a ```while``` loop.

### ```for``` Is a ```while``` Loop
We can easily model the ```for``` loop using a ```while``` loop, and in actuality, a ```for``` loop is really a ```while``` loop underneath the hood.  Consider the following ```while``` loop example:

```python
i = 0
while i < 10:
  STATEMENTS
  i = i + 1
```
The above ```while``` loop achieves the same behavior as the following ```for``` loop example:
```python
for i in range(10):
  STATEMENTS
```
The ```for``` structure was introduced because most of the loops we create iterate over a finite range.  The ```for``` structure neatly encapsulates all of the logic necessary to achieve these types of loops and eliminates the possibility of a programmer forgetting a critical component like incrementing the loop variable ```i```.

> You will likely write 100 ```for``` loops for every ```while``` loop you might write, so most iterative problems will likely involve writing a ```for``` loop.  However, the ```while``` loop is capable of evaluating general conditional logic so it is more flexible and is more likely to be used if the number of iterations is indefinite.  Many problems deal with gathering an indefinite amount of data; however, once we have gathered the data, we generally know how many iterations are necessary.  The book has a contradictory stance and suggests that ```while``` loops are quite common.

### Nested Loops
Just like we could nest ```if``` statements and we can call a function from inside another function, we can also nest loops within one another.  For example, we can nest a ```for``` loop inside another ```for``` loop:

```python
for i in range(x):
  I_STATEMENTS1
  for j in range(y):
    J_STATEMENTS
  I_STATEMENTS2
```
We can nest ```while``` loops:
```python
i = 0
while(i < x):
  I_STATEMENTS1
  j = 0
  while(j < y):
    J_STATEMENTS
    j = j + 1
  I_STATEMENTS2
  i = i + 1
```
Or we can mix and match loop types:
```python
i = 0
while(i < x):
  I_STATEMENTS1
  for j in range(y):
    J_STATEMENTS
  I_STATEMENTS2
  i = i + 1
```


### ```break```
The ```break``` keyword allows a loop, _i.e._ ```for``` or ```while```, to break out of the loop without reaching its terminating condition.  When a ```break``` statement is encountered, the program immediately jumps to the end of the current loop body and the program proceeds from that line.

```python
x = 1             # initialize the accumulator
for i in range(1,100):
  x = x * i       # do some computation
  if x > 1000:    # if the computation exceeds some limit
    break         #    then break out of the loop
```
Recall that we can express the same problem using a ```while``` loop which may be more fitting given the nature of the terminating condition:
```python
x = 1             # initialize the accumulator
i = 1             # initialize the loop variable (this was automatic in the for loop)
while(x < 1000):  # models the if statement in the above for loop
  x = x * i       # do some computation
  i = i + 1       # don't forget to increment the loop variable
```
Or we could more faithfully model the original ```for``` loop with the following ```while``` loop:
```python
x = 1             # initialize the accumulator
i = 1             # initialize the loop variable (this was automatic in the for loop)
while(i < 100):   # this is the same terminating condition as the above for loop
  x = x * i       # do some computation
  i = i + 1       # don't forget to increment the loop variable
  if x > 1000:    # if the computation exceeds some limit
    break         #    then break out of the loop
```

If a ```break``` statement is encountered in a nested loop, the ```break``` will only ```break``` out of the loop body in which it is located, meaning that if the ```break``` is inside the inner loop, the program will jump to the end of the inner loop and will then begin interpreting any statements in the outer loop.  For example:

```python
for i in range(100):
  for j in range(100):
    break         # breaks only the inner j loop
```

In order to break both loops, you may need to include additional logic.  For example:
```python
done = False      # a boolean that overrides the stop condition for both loops
for i in range(100):
  for j in range(100):
    if j == 50:
      done = True # set the override condition
      break       # breaks only the inner j loop
  if done:        # check the override condition
    break         # if the override condition is True then break the outer i loop
```

### ```continue```
A ```continue``` statement allows the loop to skip the rest of the loop body and immediately jump back up to the top of the loop.  For example:
```python
x = 0
for i in range(100):
  if i >= 10 and i <= 20:
    continue      # skip the rest of the loop if i is between 10 and 20
  x = x + i
```

```continue``` is valuable when we will only operate on some elements in a set.  We will discuss this concept in more detail later.  For now, just remember that ```continue``` instructs Python to immediately jump back to the top of the loop in which the ```continue``` appears, and if the loop is a ```for``` loop, then the loop variable is updated to the next element in the list.

### A "main loop"
Many programs will run through a number operations repeatedly until an exit condition arises.

For example, suppose you write a program that reads inputs until the user types an input that reads "exit".  You cannot predict when the user will type "exit" and your program must keep reading inputs until that condition arises.  Your program must loop to keep taking input until the exit condition is read.  Because there is no way to predict how many iterations the program must make, the correct looping structure to use is a ```while``` loop.

Programs that share similar to the above hypothetical program contain what is called a "main loop".  In this case, an infinite loop is called for and they are typically structured in the following way:
```python
while(True):
  MAIN_PROGRAM_STATEMENTS
```

When will the above loop exit?  Never according to the loop's terminating condition; however, this does not mean that it is impossible to terminate the loop.  Recall that ```break``` stops the loop and causes the program to jump down below the loop body.  We can use an ```if``` statement that contains a ```break``` statement to terminate the loop.  For example, the following is an example of the hypothetical program described above.

```python
while(True):      # the main loop will loop forever
  s = input("Enter a string (type exit to quit): ")
  print(s)
  if s == "exit": # check for the exit condition
    break         # break out of the loop
```

This program will repeatedly ask the user for input and will only exit if the user inputs exactly "exit".  The loop is designed to loop forever; however, it is still possible to break out of the loop if the exit condition arises.
