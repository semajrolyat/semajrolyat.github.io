---
layout: post
title:  "Strings"
date:   2018-10-23 00:00:00 -0400
schedule:   2018-10-23 00:00:00 -0400
categories: [preview]
docclass: "discussion"
gwclass: "cs1012"
reading: "HtTLaCS 9.1-9.14 (and 9.15-9.19)"
exercises: "/gwu/fa18/cs1012/2018/10/23/exercises.html"

---
<head>
  <link href="/css/syntax.css" rel="stylesheet">
</head>

### Introduction
We introduced strings in our first discussions; however, we did not dive very deep into how they are represented, how to manipulate them, and how to use them.  This discussion will look at strings in much more depth.

### Strings
A string is an ordered (sequential) list of characters whose order is defined from left-to-right.  The book describes a string as "a collection data type" which means that a string type is a container that consists of smaller pieces where the smaller pieces are characters.

We have so far discussed ```int```, ```float```, and ```bool``` types.  These are called _**primitive**_ types meaning that their representations are not composed of any other other types.  Types that are contain other types may be considered "collections" or "containers".

A string is not a primitive; because, it consists of characters.  You can think of a string as a sequence of smaller strings that each consist of a single character.

>Some languages have an explicit, primitive character type; however, Python does not.  In Python, a string with a length of 1 contains one character.  And we might need to perform a few operations to gain access to the underlying character data stored in a string of length 1.

It is legal for a string to have a length of zero.  We refer to a zero length string as an _**empty string**_.  An empty string is equivalent to an empty set.  An empty string is represented with either ```''``` (a pair of single quotes) or ```""``` (a pair of double quotes) with nothing in between the pair of quotes.

#### Characters
Python encodes characters using Unicode.  Unicode is an extension of the older ASCII character encoding standard.  You do not need to know too many details about these encoding schemes; however, the important takeaway is that underneath the hood, all characters are actually represented as numbers.  For example, ```'A'``` is actually represented by the number ```65```, ```'a'``` is actually represented by the number ```97```, and ```'0'``` is actually represented by the number ```48```.  This helps to explain why ```'0' != 0``` and why ```'A' != 'a'```.

There are two built in functions that help to convert back and forth between a character and its numerical (or _**ordinal**_) representation.

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
To _**concatenate**_ two strings means to join the following string to the leading string.

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
print( msg[1] )
```
The above code prints:
```
E
```
Recall that Python begins indexing at the zero position, hence ```E``` is printed because it is in index ```1``` or the second position.  The indexing of the variable ```msg``` can be visualized with the following:

![HELLO WORLD LIST]({{ "/gwu/fa18/cs1012/assets/10_23_2018/helloworldarray.png" | absolute_url }})



The indexing operator (Python uses square brackets to enclose the index) selects a single character from a string. The characters are accessed by their position or index value. For example, in the string shown below, the 14 characters are indexed left to right from postion 0 to position 13.

index values
It is also the case that the positions are named from right to left using negative numbers where -1 is the rightmost index and so on. Note that the character at index 6 (or -8) is the blank character.

The expression school[2] selects the character at index 2 from school, and creates a new string containing just this one character. The variable m refers to the result.

Remember that computer scientists often start counting from zero. The letter at index zero of "Luther College" is L. So at position [2] we have the letter t.

If you want the zero-eth letter of a string, you just put 0, or any expression with the value 0, in the brackets. Give it a try.

The expression in brackets is called an index. An index specifies a member of an ordered collection. In this case the collection of characters in the string. The index indicates which character you want. It can be any integer expression so long as it evaluates to a valid index value.

Note that indexing returns a string — Python has no special type for a single character. It is just a string of length 1.

### String Methods (9.5)
We previously saw that each turtle instance has its own attributes and a number of methods that can be applied to the instance. For example, we wrote tess.right(90) when we wanted the turtle object tess to perform the right method to turn to the right 90 degrees. The “dot notation” is the way we connect the name of an object to the name of a method it can perform.

Strings are also objects. Each string instance has its own attributes and methods. The most important attribute of the string is the collection of characters. There are a wide variety of methods. Try the following program.

In this example, upper is a method that can be invoked on any string object to create a new string in which all the characters are in uppercase. lower works in a similar fashion changing all characters in the string to lowercase. (The original string ss remains unchanged. A new string tt is created.)

In addition to upper and lower, the following table provides a summary of some other useful string methods. There are a few activecode examples that follow so that you can try them out.

Method	Parameters	Description
upper	none	Returns a string in all uppercase
lower	none	Returns a string in all lowercase
capitalize	none	Returns a string with first character capitalized, the rest lower
strip	none	Returns a string with the leading and trailing whitespace removed
lstrip	none	Returns a string with the leading whitespace removed
rstrip	none	Returns a string with the trailing whitespace removed
count	item	Returns the number of occurrences of item
replace	old, new	Replaces all occurrences of old substring with new
center	width	Returns a string centered in a field of width spaces
ljust	width	Returns a string left justified in a field of width spaces
rjust	width	Returns a string right justified in a field of width spaces
find	item	Returns the leftmost index where the substring item is found, or -1 if not found
rfind	item	Returns the rightmost index where the substring item is found, or -1 if not found
index	item	Like find except causes a runtime error if item is not found
rindex	item	Like rfind except causes a runtime error if item is not found
format	substitutions	Involved! See String Format Method, below
You should experiment with these methods so that you understand what they do. Note once again that the methods that return strings do not change the original. You can also consult the Python documentation for strings.

#### String Format (9.5.1)

### ```len``` (9.6)
The ```len``` function, when applied to a string, returns the number of characters in a string.

To get the last letter of a string, you might be tempted to try something like this:

That won’t work. It causes the runtime error IndexError: string index out of range. The reason is that there is no letter at index position 6 in "Banana". Since we started counting at zero, the six indexes are numbered 0 to 5. To get the last character, we have to subtract 1 from the length. Give it a try in the example above.

Alternatively in Python, we can use negative indices, which count backward from the end of the string. The expression fruit[-1] yields the last letter, fruit[-2] yields the second to last, and so on. Try it! Most other languages do not allow the negative indices, but they are a handy feature of Python!

### Slicing strings
A substring of a string is called a slice. Selecting a slice is similar to selecting a character:

The slice operator [n:m] returns the part of the string from the n’th character to the m’th character, including the first but excluding the last. In other words, start with the character at index n and go up to but do not include the character at index m. This behavior may seem counter-intuitive but if you recall the range function, it did not include its end point either.

If you omit the first index (before the colon), the slice starts at the beginning of the string. If you omit the second index, the slice goes to the end of the string.

There is no Index Out Of Range exception for a slice. A slice is forgiving and shifts any offending index to something legal.

### String Comparison
The comparison operators also work on strings. To see if two strings are equal you simply write a boolean expression using the equality operator.

Other comparison operations are useful for putting words in lexicographical order. This is similar to the alphabetical order you would use with a dictionary, except that all the uppercase letters come before all the lowercase letters.

It is probably clear to you that the word apple would be less than (come before) the word banana. After all, a is before b in the alphabet. But what if we consider the words apple and Apple? Are they the same?

It turns out, as you recall from our discussion of variable names, that uppercase and lowercase letters are considered to be different from one another. The way the computer knows they are different is that each character is assigned a unique integer value. “A” is 65, “B” is 66, and “5” is 53. The way you can find out the so-called ordinal value for a given character is to use a character function called ord.

When you compare characters or strings to one another, Python converts the characters into their equivalent ordinal values and compares the integers from left to right. As you can see from the example above, “a” is greater than “A” so “apple” is greater than “Apple”.

Humans commonly ignore capitalization when comparing two words. However, computers do not. A common way to address this issue is to convert strings to a standard format, such as all lowercase, before performing the comparison.

There is also a similar function called chr that converts integers into their character equivalent.

One thing to note in the last two examples is the fact that the space character has an ordinal value (32). Even though you don’t see it, it is an actual character. We sometimes call it a nonprinting character.

### Strings are Immutable
One final thing that makes strings different from some other Python collection types is that you are not allowed to modify the individual characters in the collection. It is tempting to use the [] operator on the left side of an assignment, with the intention of changing a character in a string. For example, in the following code, we would like to change the first letter of greeting.

Instead of producing the output Jello, world!, this code produces the runtime error TypeError: 'str' object does not support item assignment.

Strings are immutable, which means you cannot change an existing string. The best you can do is create a new string that is a variation on the original.

The solution here is to concatenate a new first letter onto a slice of greeting. This operation has no effect on the original string.

### Processing a String (or list) using the ```for``` loop
A lot of computations involve processing a collection one item at a time. For strings this means that we would like to process one character at a time. Often we start at the beginning, select each character in turn, do something to it, and continue until the end. This pattern of processing is called a traversal.

We have previously seen that the for statement can iterate over the items of a sequence (a list of names in the case below)

Recall that the loop variable takes on each value in the sequence of names. The body is performed once for each name. The same was true for the sequence of integers created by the range function.

Since a string is simply a sequence of characters, the for loop iterates over each character automatically.

The loop variable achar is automatically reassigned each character in the string “Go Spot Go”. We will refer to this type of sequence iteration as iteration by item. Note that it is only possible to process the characters one at a time from left to right.

### Processing a String by index
It is also possible to use the range function to systematically generate the indices of the characters. The for loop can then be used to iterate over these positions. These positions can be used together with the indexing operator to access the individual characters in the string.

The index positions in “apple” are 0,1,2,3 and 4. This is exactly the same sequence of integers returned by range(5). The first time through the for loop, idx will be 0 and the “a” will be printed. Then, idx will be reassigned to 1 and “p” will be displayed. This will repeat for all the range values up to but not including 5. Since “e” has index 4, this will be exactly right to show all of the characters.

In order to make the iteration more general, we can use the len function to provide the bound for range. This is a very common pattern for traversing any sequence by position. Make sure you understand why the range function behaves correctly when using len of the string as its parameter value.

You may also note that iteration by position allows the programmer to control the direction of the traversal by changing the sequence of index values. Recall that we can create ranges that count down as well as up so the following code will print the characters from right to left.

Trace the values of idx and satisfy yourself that they are correct. In particular, note the start and end of the range.

### Processing a String using a ```while``` loop
The while loop can also control the generation of the index values. Remember that the programmer is responsible for setting up the initial condition, making sure that the condition is correct, and making sure that something changes inside the body to guarantee that the condition will eventually fail.

The loop condition is position < len(fruit), so when position is equal to the length of the string, the condition is false, and the body of the loop is not executed. The last character accessed is the one with the index len(fruit)-1, which is the last character in the string.

Here is the same example in codelens so that you can trace the values of the variables.

### The ```in``` and ```not in``` Operators
The in operator tests if one string is a substring of another:

Note that a string is a substring of itself, and the empty string is a substring of any other string. (Also note that computer scientists like to think about these edge cases quite carefully!)

The not in operator returns the logical opposite result of in.

### The accumulator pattern with Strings
Combining the in operator with string concatenation using + and the accumulator pattern, we can write a function that removes all the vowels from a string. The idea is to start with a string and iterate over each character, checking to see if the character is a vowel. As we process the characters, we will build up a new string consisting of only the nonvowel characters. To do this, we use the accumulator pattern.

Remember that the accumulator pattern allows us to keep a “running total”. With strings, we are not accumulating a numeric total. Instead we are accumulating characters onto a string.

Line 5 uses the not in operator to check whether the current character is not in the string vowels. The alternative to using this operator would be to write a very large if statement that checks each of the individual vowel characters. Note we would need to use logical and to be sure that the character is not any of the vowels.

if eachChar != 'a'  and eachChar != 'e'  and eachChar != 'i'  and
   eachChar != 'o'  and eachChar != 'u'  and eachChar != 'A'  and
   eachChar != 'E'  and eachChar != 'I'  and eachChar != 'O'  and
   eachChar != 'U':

     sWithoutVowels = sWithoutVowels + eachChar
Look carefully at line 6 in the above program (sWithoutVowels = sWithoutVowels + eachChar). We will do this for every character that is not a vowel. This should look very familiar. As we were describing earlier, it is an example of the accumulator pattern, this time using a string to “accumulate” the final result. In words it says that the new value of sWithoutVowels will be the old value of sWithoutVowels concatenated with the value of eachChar. We are building the result string character by character.

Take a close look also at the initialization of sWithoutVowels. We start with an empty string and then begin adding new characters to the end.

### References

The [Wikepedia ASCII article](https://en.wikipedia.org/wiki/ASCII) contains an extensive amount of information on ASCII codes; however, the [list of printable characters](https://en.wikipedia.org/wiki/ASCII#Printable_characters) is important reference content that you should be aware of.

The [Python HOWTO Unicode](https://docs.python.org/3.7/howto/unicode.html#definitions) reference discusses character representation in Python.

The [Python String Documentation](https://docs.python.org/3.7/library/string.html) reference should help you locate different string operations that are not explicitly part of this discussion.
