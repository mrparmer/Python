# Math Ops

Addition

```
>>> 1 + 3.5
4.5
```



Subtraction

```
>>> 1 - 3.5
-2.5
```



Multiplication

```
>>> 1 * 3.5
3.5
```



Division

```
>>> 1 / 3.5
0.2857142857142857
```



Exponentiation (3 * 3 * 3 * 3)

```
>>> 3 ** 4
81
```

The order of operations is exponentiation, multiplication, division, addition,subtraction. For example, in the following expression we have exponentiation, multiplication and addition:

```
>>> 1 + 2 * 10**2
201
```

You get 201 because first we get 100 from 10**2 (exponentiation), and then we get 200 from 2 * 100 (multiplication), and finally 201 from 1 + 200 (addition).

However you can control what to execute first by using parenthesis:

```
>>> (1 + 2) * 10**2
300
```

You get 300 because first we get 3 from 1 + 2, and then we get 100 from 10**2 and then 300 from 3 * 100.

# Data Types

float("100.10")
100.1

round(10.6)
11

str(10)
'10'

![1537496247096](C:\Users\Mparmer-Desk\AppData\Roaming\Typora\typora-user-images\1537496247096.png)

1. List

   ​	syntax: name = [xxx,yyy,zzz]

# Functions

len()
​	gives length of item within ().

