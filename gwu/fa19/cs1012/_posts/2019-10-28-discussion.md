---
layout: post
title:  "Strings"
date:   2019-10-28 00:00:00 -0400
schedule:   2019-10-28 00:00:00 -0400
categories: [GWU]
docclass: "discussion"
gwclass: "cs1012"
reading: "HtTLaCS 10.1-10.14"
term: "fa19"
---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

### Introduction
We introduced strings in our first discussions; however, we did not dive very deep into how they are represented, how to manipulate them, and how to use them.  This discussion will look at strings in much more depth.

### Strings
A string represents a _**set**_ of characters.  A string is actually a specialized type of set because it has an _**order**_ or a _**sequence**_.  We often describe an ordered set as a _**list**_.  A Python string is also _**immutable**_  meaning "unchangable" which we will put into context and discuss in more detail when we discuss lists.

A string's order is defined from left-to-right.  The book describes a string as "a collection data type" which means that a string type is a container that consists of smaller pieces where the smaller pieces are characters.

We have so far discussed ```int```, ```float```, and ```bool``` types.  These are called _**primitive**_ types meaning that these are fundamental types whose representations are not composed of any other types.  Types that are composed of other types may be considered "collections" or "containers".

A string is not a primitive; because, it consists of characters.  You can think of a string as a sequence of smaller strings that each consist of a single character.

>Some languages have an explicit, primitive character type; however, Python does not.  In Python, a string with a length of 1 contains one character.  And we might need to perform a few operations to gain access to the underlying character data stored in a string of length 1.

It is legal for a string to have a length of zero.  We refer to a zero length string as an _**empty string**_.  An empty string is equivalent to an empty set also known as the null set.  An empty string is represented with either ```''``` (a pair of single quotes) or ```""``` (a pair of double quotes) with nothing in between the pair of quotes.

#### Characters
Python encodes characters using Unicode.  Unicode is an extension of the older ASCII character encoding standard.  You do not need to know too many details about these encoding schemes; however, the important takeaway is that underneath the hood, all characters are actually represented as numbers.  For example, ```'A'``` is actually represented by the number ```65```, ```'a'``` is actually represented by the number ```97```, and ```'0'``` is actually represented by the number ```48```.  This helps to explain why ```'0' != 0``` and why ```'A' != 'a'```.

The following is the most relevant information from the ASCII table.  The character codes ```0-31``` are primarily specialized system characters that are non-printable; however, a few exceptions are provided for context.  Codes beginning at ```32``` are mostly the printable codes that we are familiar with.  

| code | char | code | char | code | char | code | char |
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
|   0  | null |  32  | space|  64  |   @  |  96  |   `  |
|   1  |      |  33  |   !  |  65  |   A  |  97  |   a  |
|   2  |      |  34  |   "  |  66  |   B  |  98  |   b  |
|   3  |      |  35  |   #  |  67  |   C  |  99  |   c  |
|   4  |      |  36  |   $  |  68  |   D  | 100  |   d  |
|   5  |      |  37  |   %  |  69  |   E  | 101  |   e  |
|   6  |      |  38  |   &  |  70  |   F  | 102  |   f  |
|   7  |      |  39  |   '  |  71  |   G  | 103  |   g  |
|   8  |      |  40  |   (  |  72  |   H  | 104  |   h  |
|   9  | TAB  |  41  |   )  |  73  |   I  | 105  |   i  |
|  10  |  LF  |  42  |   *  |  74  |   J  | 106  |   j  |
|  11  |      |  43  |   +  |  75  |   K  | 107  |   k  |
|  12  |      |  44  |   ,  |  76  |   L  | 108  |   l  |
|  13  |  CR  |  45  |   -  |  77  |   M  | 109  |   m  |
|  14  |      |  46  |   .  |  78  |   N  | 110  |   n  |
|  15  |      |  47  |   /  |  79  |   O  | 111  |   o  |
|  16  |      |  48  |   0  |  80  |   P  | 112  |   p  |
|  17  |      |  49  |   1  |  81  |   Q  | 113  |   q  |
|  18  |      |  50  |   2  |  82  |   R  | 114  |   r  |
|  19  |      |  51  |   3  |  83  |   S  | 115  |   s  |
|  20  |      |  52  |   4  |  84  |   T  | 116  |   t  |
|  21  |      |  53  |   5  |  85  |   U  | 117  |   u  |
|  22  |      |  54  |   6  |  86  |   V  | 118  |   v  |
|  23  |      |  55  |   7  |  87  |   W  | 119  |   w  |
|  24  |      |  56  |   8  |  88  |   X  | 120  |   x  |
|  25  |      |  57  |   9  |  89  |   Y  | 121  |   y  |
|  26  |      |  58  |   :  |  90  |   Z  | 122  |   z  |
|  27  |      |  59  |   ;  |  91  |   [  | 123  |   {  |
|  28  |      |  60  |   <  |  92  |   \  | 124  |  \|  |
|  29  |      |  61  |   =  |  93  |   ]  | 125  |   }  |
|  30  |      |  62  |   >  |  94  |   ^  | 126  |   ~  |
|  31  |      |  63  |   ?  |  95  |   _  | 127  |delete|

#### Converting to and from Character Codes
Because a character is really a numeric, we may need to explicitly instruct Python to convert a code to a character or to convert character to a code.  There are two built in functions that help to convert back and forth between a character and its numeric (or _**ordinal**_) code representation.

> 'ordinal' is a term borrowed from mathematics that describes an element's position in a series.  The ordinal position of ```'A'``` is its position in the ASCII/Unicode table, _i.e._ ```65```.

The function ```ord``` converts a string consisting of one character to its corresponding integer representation.  The following code demonstrates the usage of ```ord```:
```python
print(type(ord('A')))
print(ord('A'))
```
The above code, produces the following output:
```
<class 'int'>
65
```

The function ```chr``` converts an integer from its Unicode value to a string consisting of that character.  The following code demonstrates the usage of ```chr```:
```python
print(type(chr(65)))
print(chr(65))
```
The above code, produces the following output:
```
<class 'str'>
A
```
> Both ```ord``` and ```chr``` take one parameter.  In the case of ```ord```, the length of the string must be 1.

### String Operators
Mathematical operations cannot be performed on strings.  For example, the following mathematical operations are nonsensical and will generate an error because at least one operand is a string:
```python
"hello" - 1
"hello" / 2
"hello" * "world"
"50" + 2                # "50" looks like a number, but it is a string
```

While the above operations are nonsensical, Python allows the operators ```+``` and ```*``` to be used with strings; however, in the context of strings, these operators are not interpreted as mathematical operators but as string operators.

#### Concatenation : using the ```+``` string operator
To _**concatenate**_ two strings means to join the following string to the leading string into a single string.

If Python interprets one of the binary operands for the ```+``` operator as a string, Python will attempt to concatenate the two operands; however, both operands must be interpreted as strings for the concatenation to succeed.

The following code demonstrates how to successfully concatenate strings.
```python
print("hello" + "world")
print("50" + str(2))
```
The above code produces the following output:
```
helloworld
502
```
> In the earlier example, ```"50" + 2``` is illegal because only one of the operands is a string.  In the subsequent example, we clarified the intent by type converting the integer to a string which allows Python to interpret the ```+``` as the concatentation operator.  If our intent was to mathematically add fifty and two, then we would have to convert the string ```"50"``` to its numeric representation so that Python intepretes both operands as numbers.

Concatentation allows a programmer to programmatically build a string.  For example suppose that a program takes input from a user.  There is often a need to print that information back to the user.
```python
x = int(input("Enter an integer: "))
msg = "You entered " + str(x)
print(msg)
```

#### Repetition : using the ```*``` string operator
If Python interprets one of the binary operands for the ```*``` operator as a string and the other as an integer, Python will repeat the string as many times as specified by the integer.

The following code demonstrates usage of the repetition string operator.
```python
print("hello" * 3)
print(3 * "hello")
```
The above code produces the following output:
```
hellohellohello
hellohellohello
```
> If Python interprets one operand as a float and the other as a string, Python will generate an error.

#### String operator precedence
The string operators ```+``` and ```*``` are evaluated using the same precedence rules as their corresponding mathematical operators.  Therefore, repetition has higher precedence than concatenation.  If your intent is to perform concatenation before repetition, you must use parentheticals to group the operations in the intended order.

### Indexing a string
The _**indexing operators**_ are square brackets, _i.e._ ```[``` and ```]```, and they allow a single character in a string to be selected based on its position or _**index**_ within the string.  For example:
```python
msg = "HELLO WORLD"
print( msg[0] )
print( msg[1] )
print( msg[2] )
```
The above code prints:
```
H
E
L
```
Recall that Python begins indexing at the zero position, hence ```E``` is printed because it is in index ```1``` or the second position beginning from left-to-right.
There are 11 characters in the string ```msg```, which means that characters in ```msg``` can be indexed using numbers from 0 to 10.

> To generalize, a string of length ```n``` can be indexed from left-to-right using values from ```0``` to ```n-1```

The indexing of the variable ```msg``` can be visualized with the following:

![HELLO WORLD LIST]({{ "/gwu/fa18/cs1012/assets/10_23_2018/helloworldarray.png" | absolute_url }})

Alternatively, the string can be indexed from right-to-left by using negative numbers.  When indexing from right-to-left, ```-1``` indexes the rightmost character, ```-2``` indexes the character to the left of the rightmost character, and so forth.  For example:
```python
msg = "HELLO WORLD"
print( msg[-1] )
print( msg[-2] )
print( msg[-3] )
```
The above code prints:
```
D
L
R
```
When indexing a string, a new string consisting of the characters specified is returned.

We refer to the number used to select the position of a character (or a value in a list) as the _**index**_.

### Length of a string
Python provides a built in function that can be used to determine the length of a string.  The ```len(<string>)``` function returns the number of characters in the string.  For example, the following code prints the length of the string ```s```:
```Python
s = "Hello World"
n = len(s)
print(n)
```
The above code produces the following output:
```
11
```

### Slicing a String
As stated above, a string is really a list or a sequence type (We will talk more about sequence types next week).  As a sequence type, we have the ability to _**slice**_ a string.  Before we talk about slicing in detail, first recall the structure of the ```range()``` function with three parameters.

The three parameter ```range(start, stop, step)``` function allows us to specify where a range should start and stop and how large the step between numbers should be.  This pattern, _i.e._ ```start, stop, step```, is a recurring theme in Python and is used here in the context of slicing.

A slice is a sub-sequence extracted from another sequence.  The indexing operators can specify more than a single value in a string if the colon ```:``` is used as a delimiter.  When a colon is used, the statement inside the indexing operators is interpreted as a specification of ```start : stop : step```.  Here is an example:

```python
s = "Hello World!"
print(s[0:5:1])
```
The output from the above program is:
```
Hello
```
The above program specified that the substring of ```s``` starts at the ```0``` position, stops before the ```5``` position, and steps ```1``` position at a time.  

Note that just like with the range function, the step is by default ```1```, so we can actually omit this field with the slice instruction.  For example, the following program produces the same result as the above program:

```Python
s = "Hello World!"
print(s[0:5])
```

We will dive much deeper into slicing in subsequent discussions.

### Example - Palindrome
A palindrome is a string that has the same sequence of characters regardless of whether the string is read forwards or backwards.  There are a number of ways to implement an algorithm that checks whether or not a string is a palindrome.  This example illustrates one method where each character from the front is checked against its corresponding character from the back of the string:

```Python
# allow the user to input a string
s = input("Input a string: ")

# compute half the length of the string
mid = len(s)//2

# assume the string is a palindrome
ispalindrome = True

# iterate up to half the length of the string
for i in range(mid):
    # compare the ith character from the front with the ith character from the back
    if s[i] != s[-(i+1)]:
        # if the characters do not match, the string is not a palidrome
        ispalindrome = False
        break

# if we never proved that the string is not a palindrome
# then we assume it is
if ispalindrome:
    print(s + " is a palindrome")
else:
    print(s + " is not a palindrome")
```

The above program begins with the assumption that the candidate string is a palindrome.  The algorithm iterates up to half the length of the string.  Recall that this uses integer division, so both half of 7 and 6 is 3.  This is nice because we do not have to consider a difference between odd and even length strings.  During iteration, the algorithm compares the ith character from the front with the ith character from the back of the string, and if the characters are different then we have proven that the string is not a palindrome.  If we finish iteration without determining that the candidate string is not a palidrome, then we can assume that it is.

### References

The [Wikepedia ASCII article](https://en.wikipedia.org/wiki/ASCII) contains an extensive amount of information on ASCII codes; however, the [list of printable characters](https://en.wikipedia.org/wiki/ASCII#Printable_characters) is important reference content that you should be aware of.

The [Python HOWTO Unicode](https://docs.python.org/3.7/howto/unicode.html#definitions) reference discusses character representation in Python.

The [Python String Documentation](https://docs.python.org/3.7/library/string.html) reference should help you locate different string operations that are not explicitly part of this discussion.
