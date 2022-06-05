# Intermediate Level Exercises

## 1 FizzBuzz
 Create a function that takes in an integer number **n** and prints out a count from **0 to n** with the following rules applied:
 
 1. Numbers divisible by 3: print `Fizz`
 2. Numbers divisible by 5: print `Buzz`
 3. Numbers divisible by 3 and 5: print `FizzBuzz`

Function definition should take the form:
```python
def fizz_buzz(n: int) -> None:
    # Your code here
```

Example output for the function:
```
>>> fizz_buzz(16)
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
```

## 2 Merge Two Lists

Create a function `zip` that takes in two sorted lists `list_1` and `list_2` and returns as an output both lists merged together in order.  You can assume that list1 and list2 are already sorted in accending order.

Function definition should take the form:
```python
def zip(list_1, list_2) -> list:
    # Your code here
```

Example output for the function:
```
>>> list_1 = [1,3,4,7,9,18]
>>> list_2 = [2,4,6,8,10]
>>> zip(list_1, list_2)
[1,2,3,4,4,6,7,8,9,10,18]           ## Note that numbers that appear in both lists are repeated
```

## 3 Squared Distance

Create a function that takes in two points as tuples and returns the ![euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between them.  At first just find the distance between two points with only two dimensions so that the tuples look like: `(x1, y1)` and `(x2, y2)`.  Then try and extend your code to work for tuples of all sizes.

Function definition should take the form:
```python
def dist(point_1: tuple, point_2: tuple) -> float:
    # Your code here
```


Example output for the function:
```
>>> point_1 = (0, 10)
>>> point_2 = (0, 20)
>>> dist(point_1, point_2)
10.0
```
Or for a more complex example
```
>>> point_1 = (5, 10, 13)
>>> point_2 = (7, 20, 18)
>>> dist(point_1, point_2)
11.3578
```

## 4 Palindrome
Write a function that, given a string, checks whether the string is a palindrome (same forwards as backwards) and returns `True` or `False` if it is, or isn't, respectively.
```python
def is_palindrome(s: str) -> bool:
```

Example output for the function:
```
>>> is_palindrome('hello world')
False

>>> is_palindrome('bob')
True

>>> is_palindrome('a man a plan a canal panama')
True
```

## 5 Roman Numerals
Write a function that takes in a set of Roman Numerals as a string and outputs the correct Arabic number as an integer.  Use the following guide:

```
Symbol | Value
-------|------------
  I    |   1
  V    |   5
  X    |   10
  L    |   50
  C    |   100
  D    |   500
  M    |   1000
```
And example function definition:
```python
def rom_to_dec(roman: str) -> int:
    # Your code here
```
Assume that Roman Numerals are always in decending order for addition, (so VI = 5 + 1 = 5)  and in acending order for subtraction (so IV = 5 - 1 = 4) to make the numbers not included in the numerals list.

Examples:
```
>>> rom_to__dec('MI')
1001
>>> rom_to__dec('XIV')
14
>>> rom_to__dec('MCMXCIV')
1994
```


## 6 Line Intersection
Write a function that takes in four tuples that represent coordinates on an x-y plane `(x1,y1),(x2,y2),(x3,y3),(x4,y4)` where the first two coordinates are the line A - B  and the second two are the line C - D.  Return a boolean value of `True` if the lines AB and CD intersect, and a `False` if they don't. _Hint: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection_

```python 
def intersect(a, b, c, d) -> bool:
   # Your code here
```

Example output for the function:
```
>>> a = (10, 0)
>>> b = (10, 20)
>>> c = (0, 10)
>>> d = (30, 10)
>>> intersect(a, b, c, d)
True
```
False example:
```
>>> a = (0, 0)
>>> b = (0, 10)
>>> c = (10, 10)
>>> d = (30, 30)
>>> intersect(a, b, c, d)
False
```

