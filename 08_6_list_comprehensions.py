'''
Python supports a concept called "list comprehensions". It can be used to
construct lists in a very natural, easy way, like a mathematician is used to do.
For example, assume we want to create a list of squares, like:
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

We can obtain the same result with:
squares = [x**2 for x in range(10)]

A list comprehension consists of brackets containing an expression followed by
a for clause, then zero or more for or if clauses. The result will be a new list
resulting from evaluating the expression in the context of the for and if
clauses which follow it. For example, this listcomp combines the elements of two
lists if they are not equal:
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

7.3 Consider the following list:
list1 = [1,2,3,4]
Multiply everything larger than 2 by 3, and the rest leave as is:
'''
list1 = list(range(1,5)) # or list1 = [1,2,3,4]
lModifiedList1 = [(item * 3 if item > 2 else item) for item in list1]
print(lModifiedList1)
