# Python Notes

## Math Ops

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

## Data Types

float("100.10")
100.1

round(10.6)
11

str(10)
'10'

![1537496247096](C:\Users\Mparmer-Desk\AppData\Roaming\Typora\typora-user-images\1537496247096.png)

1. List

   ​	syntax: name = [xxx,yyy,zzz]
   ​				     0	   1    2  positive indexing
   ​				    -3   -2  -1   negative indexing



## List Slicing Examples

Let's suppose we have the following list in our Python shell:

```
>>> days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
```

Here is how to access the first three items (from first to third):
`>>> days[0:3]` 

Output:
`['Mon', 'Tue', 'Wed']` 

Access items from first to fourth:
`>>> days[0:4]` 
`['Mon', 'Tue', 'Wed', 'Thu']` 

Exactly the same as above
`>>> days[:4]` 
`['Mon', 'Tue', 'Wed', 'Thu']` 

No boundaries
`>>> days[:]` 
`['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']` 

From first to second-to-last
`>>> days[0:-1]` 
`['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']` 

From first to third-to-last
`>>> days[:-2]` 
`['Mon', 'Tue', 'Wed', 'Thu', 'Fri']` 

From third-to-last to second-to-last
`>>> days[-3:-1]` 
`['Fri', 'Sat']` 

From third-to-last to last
`>>> days[-3:]` 
`['Fri', 'Sat', 'Sun']` 

## List Methods

​	listName.method()

## Functions

len()
​	gives length of item within ().

## Tuples

Section 2, Lecture 17

There's another datatype in Python called a `tuple` :

```
mytuple = (1, 2, "Three")
```

It's exactly like a `list`  except:

\1. You use round brackets instead of square brackets to define it.

\2. A tuple is not mutable which means you can't append or remove items from tuples, unlike lists. Trying to do append to a tuple would throw an error:

```
>>> mytuple = (1, 2, "Three") >>> mytuple.append("Four")Traceback (most recent call last):  File "<stdin>", line 1, in <module>AttributeError: 'tuple' object has no attribute 'append'
```

Tuples are rarely used but if you ever want to have a sequence that you really don't want to be changed, then tuples might be a good idea to use.

