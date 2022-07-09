## Python Simple Exercises

1) Write a for loop that counts from 0 to 10

2) Write a for loop that counts from 1 to 10

3) Write a for loop that counts from 10 to 1

4) Using two for loops, print out the below 7 sets of asterisks
```python
*
**
***
****
*****
******
*******
```
5) Using two for loops, print out the inverted triangle of asterisks
```python
*******
******
*****
****
***
**
*
```

6) Write a function that takes in a number (n) and counts n
```python
def count_to(n: int) -> None:
```
example:
```python
>>> count_to(5)
1
2
3
4
5
```

7)  Write a function that takes in a string (s) and prints out each letter on a new line
```python
def write_letters(s: int) -> None:
```
example:
```python
>>> write_letters("hello")
h
e
l
l
o
```

8) Write a function using only addition and subtractrionthat takes in two numbers m and n (where m >= n) and returns the number of times n fits into m (completely).  _hint: use a while loop to achieve this!_ 
```python
def whole_multiples(m, n) -> int:
```
example:
```python
>>> whole_multiples(50,7)
 7
```
9) Edit the above function so that it checks if m >= n and prints an error message if m < n.
example:
```python
>>> whole_multiples(7,10)
M must be greater than N!
```

10) Write a function that, when given a list of integers l, returns the largest element
```python
def max_element(l: list) -> int:
```
example:
```python
>>> l = [1, 4, 6, 2, 3, 4, 8]
>>> max_element(l)
8
```
