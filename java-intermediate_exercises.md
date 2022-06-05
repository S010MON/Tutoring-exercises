# Intermediate Level Exercises

## 1 FizzBuzz
 Create a method that takes in an integer number **n** and prints out a count from **0 to n** with the following rules applied:
 
 1. Numbers divisible by 3: print `Fizz`
 2. Numbers divisible by 5: print `Buzz`
 3. Numbers divisible by 3 and 5: print `FizzBuzz`

Method definition should take the form:
```java
public static void fizz_buzz(int n)
{
    // TODO Your code here
}
```

Example output for the function:
```
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

Create a function `zip` that takes in two sorted arrays `list1` and `list2` and returns as an output both arrays merged together in order.  You can assume that list1 and list2 are already sorted in accending order.

Function definition should take the form:
```java
public static int[] zip(int[] list1, int[] list_2)
{
    // TODO your code here
}
```

Example output for the function:
```java
list1 = {1,3,4,7,9,18};
list2 = {2,4,6,8,10};
listOut = zip(list1, list2);
System.out.println(listOut);

>>> [1,2,3,4,4,6,7,8,9,10,18]           ## Note that numbers that appear in both lists are repeated
```

## 3 Squared Distance

Create a function that takes in two points as tuples and returns the ![euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between them.  At first just find the distance between two points with only two dimensions so that the tuples look like: `(x1, y1)` and `(x2, y2)`.  Then try and extend your code to work for tuples of all sizes.

Function definition should take the form:
```java
public static Vector dist(Vector point1, Vector point2)
{
    // TODO Your code here
}
```

Where a vector is the following class:
```java

public class Vector
{
    private double[] v;

    /** Constructor 
     *  create and n-dimensional vector by passing in numbers seperated by commas example: 
     *  Vector v = new Vector(1, 2, 3, 4); 
     */
    public Vector(double... v)
    {
        this.v = new double[v.length];
        for (int i = 0; i < v.length; i++)
        {
            this.v[i] = v[i];
        }
    }

    /** Returns the number of dimensions in the vector */
    public int dims()
    {
        return v.length;
    }

    /** Gets the value at index `i` for the vector */
    public double get(int i)
    {
        if (i >= v.length)
            throw new RuntimeException("Cannot access dim " + i + " in vector length " + v.length);
        return v[i];
    }
}
```


Example output for the function:
```java
Vector point1 = new Vector(0, 10);
Vector point2 = new Vector(0, 20);
d = dist(point1, point2);
System.out.println(d);

>>> 10.0
```
Or for a more complex example
```java
Vector point1 = new Vector(5, 10, 13);
Vector point2 = new Vector(7, 20, 18);
d = dist(point1, point2);
System.out.println(d);

>>> 11.3578
```

## 4 Palindrome
Write a function that, given a string, checks whether the string is a palindrome (same forwards as backwards) and returns `true` or `false` if it is, or isn't, respectively.
```java
public static boolean isPalindrome(String s)
{
   // TODO Your code here
}
```

Example output for the function:
```java
isPalindrome("hello world");
>>> false

isPalindrome("bob");
>>> true

isPalindrome("a man a plan a canal panama");
>>> true
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
```java
public static  int roman2Decimal(String numeral)
{
    // Your code here
}
```
Assume that Roman Numerals are always in decending order for addition, (so VI = 5 + 1 = 5)  and in acending order for subtraction (so IV = 5 - 1 = 4) to make the numbers not included in the numerals list.

Examples:
```
roman2Decimal("MI")
>>> 1001
roman2Decimal("XIV")
>>> 14
roman2Decimal("MCMXCIV")
>>> 1994
```


## 6 Line Intersection
Write a function that takes in Vectors (from the class given ![above](https://github.com/S010MON/Tutoring-exercises/edit/main/intermediate_exercises.md#3-squared-distance)) that represent coordinates on an x-y plane `(x1,y1),(x2,y2),(x3,y3),(x4,y4)` where the first two coordinates are the line A - B  and the second two are the line C - D.  Return a boolean value of `True` if the lines AB and CD intersect, and a `False` if they don't. _Hint: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection_

```java 
public static boolean intersect(Vector a, Vector b, Vector c, Vector d)
{
   // TODO Your code here
}
```

Example output for the function:
```
>>> a = (10, 0)
>>> b = (10, 20)
>>> c = (0, 10)
>>> d = (30, 10)
>>> intersect(a, b, c, d)
true
```
False example:
```
>>> a = (0, 0)
>>> b = (0, 10)
>>> c = (10, 10)
>>> d = (30, 30)
>>> intersect(a, b, c, d)
false
```
