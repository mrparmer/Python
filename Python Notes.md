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

# List Slicing Examples



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

List

​	syntax: name = [xxx,yyy,zzz]
​				     0	   1    2  positive indexing
​				    -3   -2  -1   negative indexing

​	Lists contain 1 value/entry separated by a comma.

​	

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

# Dictionary Info

Dictionaries are similar to lists, however they contain linked entries, separated by a colon, like on line 2 in the	 			 

image above you have a key/value, and it's linked value/definition.

number indexing does not work. 
​	pins[0] would give an error.
​	pins["Mike"] returns the value linked to the key, so 1234.
​	To see all of the keys in a dictionary dict_name.keys()
​	To see all of the values assigned to the keys dict_name.values()

Let's say we have the following dictionary:

```
>>> person97 = {"name":"Jack", "surname":"Smith", "age":"29"}
```

Removing pair *"name":"Jack"*
`>>> person97.pop("name")` 
`'Jack'` 
`>>> person97` 
`{'surname': 'Smith', 'age': '29'}` 

Adding new pair *"name":"Jack"*
`>>> person97["name"] = "Jack"` 
`>>> person97` 
`{'surname': 'Smith', 'age': '29', 'name': 'Jack'}` 

Changing an existing value
`person97["age"] = 30` 
`person97` 
`{'surname': 'Smith', 'age': 30, 'name': 'Jack'}` 

Mapping two lists to a dictionary:



keys = ["a", "b", "c"] 
values = [1, 2, 3] 
mydict = dict(zip(keys, values)) 
mydict 
{'a': 1, 'b': 2, 'c': 3} 

# Conditionals

## if/else

​	if var in list/dict/array
​	    action #4 spaces before first work in second line
​	else:
​	    action



```python
user_input = float(input("Enter a number: "))
if user_input > 100:
    print("Greater")
elif user_input < 100:
    print("Lesser")
elif user_input == 100:
    print("Equal")
```





# Custom Functions

Python has many built in functions, like len(), that are predefined within the language. 

Python also gives the developer the ability to define custom functions. See image below

![1537920007561](C:\Users\Mparmer-Desk\AppData\Roaming\Typora\typora-user-images\1537920007561.png)

This is a custom function from basics.py. It opens the file sample.txt reads the file into the fruits variable, then .splitlines converts the data from the .txt into a list that can be searched by the program. The conditional statement then takes the results of the searched list and applies that logic to the function, printing out the message required.

Functions are similar to Methods in C#

Functions always start with def (define)

### 





