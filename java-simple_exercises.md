## Java Simple Exercises

1. Write a for loop that counts from 0 to 10

2. Write a for loop that counts from 1 to 10

3. Write a for loop that counts from 10 to 1

4. Using two for loops, print out the below 7 sets of asterisks
```
*
**
***
****
*****
******
*******
```
5. Using two for loops, print out the inverted triangle of asterisks
```
*******
******
*****
****
***
**
*
```

6. Write a method that takes in a number (n) and counts n
```java
public void countTo(int n)
```
example input:
```java
count_to(5)
```
example output:
```
1
2
3
4
5
```

7.  Write a function that takes in a string (s) and prints out each letter on a new line
```java
public void writeLetters(String s)
```
example:
```java
writeLetters("hello")
```
example output:
```
h
e
l
l
o
```

8. Write a method using only addition and subtractrionthat takes in two numbers m and n (where m >= n) and returns the number of times n fits into m (completely).  _hint: use a while loop to achieve this!_ 
```java
public int wholeMultiples(int m, int n)
```
example:
```java
wholeMultiples(50,7)
```
example output:
```
 7
```
9. Edit the above method so that it checks if m >= n and prints an error message if m < n.
example:
```java
wholeMultiples(7,10)
```
example output:
```
M must be greater than N!
```

10. Write a method that, when given a list of integers l, returns the largest element
```java
public int maxElement(int[] list)
```
example:
```java
l = [1, 4, 6, 2, 3, 4, 8]
max_element(l)
```
example output:
```
8
```
