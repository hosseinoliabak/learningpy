#If section 1 is not easy to understand, jump to Section 2
#----------------------------------Section 1------------------------------------
'''
Terminology:
Attributes: data associated with a class
Methods: functions associated with a class
Using Objects
It turns out we have been using objects all along in this class. Python provides
us with many built-in objects. Here is some simple code where the first few lines
should feel very simple and natural to you.
+---------------------------------------------+
|stuff = list()                               |
|stuff.append('python')                       |
|stuff.append('chuck')                        |
|stuff.sort()                                 |
|                                             |
|# The following lines are equivalent         |
|print (stuff[0])                             |
|print (stuff.__getitem__(0))                 |
|print (list.__getitem__(stuff,0))            |
|                                             |
|# Code: http://www.py4e.com/code3/party1.py  |
+---------------------------------------------+
But instead of focusing on what these lines accomplish, lets look at what is
really happening from the point of view of object-oriented programming. Don't
worry if the following paragraphs don't make any sense the first time you read
them because we have not yet defined all these terms.

The first line is constructing an object of type list, the second and third
lines are calling the append() method, the fourth line is calling the sort()
method, and the fifth line is retrieving the item at position 0.
The sixth line is calling the __getitem__() method in the stuff list with a
parameter of zero.
The seventh line is an even more verbose way of retrieving the 0th item in the
list. In this code, we care calling the __getitem__ method in the list class
and passing in the list (stuff) and the item we want retrieved from the list as
parameters.
We can take a look into the capabilities of an object by looking at the output
of the dir() function:
+--------------------+
|lStuff = list()     |
|print(type(lStuff)) |
|print(dir(lStuff))  |
+--------------------+
+------------------------------------Output------------------------------------+
|<class 'list'>                                                                |
|['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',        |
|'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',   |
|'__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',      |
|'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',    |
|'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',               |
|'__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',       |
|'__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend',  |
|'index', 'insert', 'pop', 'remove', 'reverse', 'sort']                        |
+------------------------------------------------------------------------------+
The precise definition of dir() is that it lists the methods and attributes of
a Python object.

Objects
May read this link to have understanding about objects:
https://docs.oracle.com/javase/tutorial/java/concepts/object.html

Classes
Class: A class is the blueprint from which individual objects are created.
In the real world, you'll often find many individual objects all of the same
kind. There may be thousands of cars in existence, all of the same make and
model. Each car was built from the same set of blueprints and therefore contains
the same components. In object-oriented terms, we say that your car is an
instance of the class of objects known as cars.

Classes and Object in Python
+--------------------------------+
|class PartyAnimal:              |
|   x = 0                        |
|                                |
|   def party(self):             |
|     self.x = self.x + 1        |
|     print("So far",self.x)     |
|                                |
|objAnimal = PartyAnimal()       |
|objAnimal.party()               |
|objAnimal.party()               |
|objAnimal.party()               |
|PartyAnimal.party(objAnimal)    |
+--------------------------------+
Each method looks like a function, starting with the def keyword and consisting
of an indented block of code. This example has one attribute (x) and
one method (party). The methods have a special first parameter that we name
by convention self. You can even change 'self' to anything not reserved like
"this", and it will work fine. But people like to use "self", as it has now
become a bit of a convention.

Classes as Types
As we have seen, in Python, all variables have a type. And we can use the
built-in dir function to examine the capabilities of a variable. We can use type
and dir with the classes that we create.
+----------------------------------------------+
|class PartyAnimal:                            |
|   x = 0                                      |
|                                              |
|   def party(self):                           |
|     self.x = self.x + 1                      |
|     print("So far",self.x)                   |
|                                              |
|objAnimal = PartyAnimal()                     |
|print ("Type", type(objAnimal))               |
|print ("Dir ", dir(objAnimal))                |
|print ("Type", type(objAnimal.x))             |
|print ("Type", type(objAnimal.party))         |
|                                              |
|# Code: http://www.py4e.com/code3/party3.py   |
+----------------------------------------------+
+------------------------------------Output------------------------------------+
|Type <class '__main__.PartyAnimal'>                                           |
|Dir  ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', |
|'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', |
|'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',   |
|'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',       |
|'__str__', '__subclasshook__', '__weakref__', 'party', 'x']                   |
|Type <class 'int'>                                                            |
|Type <class 'method'>                                                         |
+------------------------------------------------------------------------------+
You can see that using the class keyword, we have created a new type. From the
dir output, you can see both the x integer attribute and the party method are
available in the object.

Object Lifecycle
n the previous examples, we are defining a class (template) and using that class
to create an instance of that class (object) and then using the instance. When
the program finishes, all the variables are discarded. Usually we don't think
much about the creation and destruction of variables, but often as our objects
become more complex, we need to take some action within the object to set things
up as the object is being constructed and possibly clean things up as the object
is being discarded.

If we want our object to be aware of these moments of construction and
destruction, we add specially named methods to our object:
+----------------------------------------------+
|class PartyAnimal:                            |
|   x = 0                                      |
|                                              |
|   def __init__(self):                        |
|     print('I am constructed')                |
|                                              |
|  def party(self) :                           |
|     self.x = self.x + 1                      |
|     print('So far',self.x)                   |
|                                              |
|   def __del__(self):                         |
|     print('I am destructed', self.x)         |
|                                              |
|objAnimal = PartyAnimal()                     |
|objAnimal.party()                             |
|objAnimal.party()                             |
|objAnimal = 42                                |
|print('an contains',objAnimal)                |
|                                              |
|# Code: http://www.py4e.com/code3/party4.py   |
+----------------------------------------------+
+----------Output---------+
|I am constructed         |
|So far 1                 |
|So far 2                 |
|I am destructed 2        |
|objAnimal contains 42    |
+-------------------------+
As Python is constructing our object, it calls our __init__ method to give us a
chance to set up some default or initial values for the object. When Python
encounters the line: objAnimal = 42 it actually 'thows our object away' so it
can reuse the objAnimal variable to store the value 42. Just at the moment when
our objAnimal object is being 'destroyed' our destructor code (__del__) is
called. We cannot stop our variable from being destroyed, but we can do any
necessary cleanup right before our object no longer exists.

When developing objects, it is quite common to add a constructor to an object
to set in initial values in the object, it is relatively rare to need a
destructor for an object.

Let's look at another example:
+----------------------------------------------+
|class character(object):                      |
|    def__init__(self, name, initial_health):  |
|        self.name = name                      |
|        self.health= initial_health           |
|        self.inventory= []                    |
|    def grab(self, item):                     |
|        self.inventory.append(item)           |
|    def get_health(self):                     |
|        return self.health                    |
+----------------------------------------------+
Let's create instances of our class:
+---------------------------------+---------------------------------+
|char01 = character(“Zelda”, 10)  |  char02 = character(“Mario”, 8) |
|---------------------------------|---------------------------------|
|Name: “Zelda”                    |  Name: “Mario”                  |
|Health: 10                       |  Health: 8                      |
|Inventory: []                    |  Inventory: []                  |
|---------------------------------|---------------------------------|
|grab(item)                       |  grab(item)                     |
|get_health()                     |  get_health()                   |
+---------------------------------+---------------------------------+
'''
#----------------------------------Section 1------------------------------------
# Learn Python OOP through codes
"""
#1 Classes and instances
class Employee:
    pass # We just want to skip for now (no atributes and no methods)

emp1 = Employee()
emp1.name = "Hossein"
emp1.last = "Oliabak"
emp1.pay = 64000
emp1.email = "hossein.oliabak@company.com"

emp2 = Employee()
emp2.name = "Iman"
emp2.last = "Gh"
emp2.pay = 60000
emp2.email = "iman.gh@company.com"
print('{} {}'.format(emp1.name, emp2.name))

print(Employee.__dict__)
print(emp1.__dict__)
print(emp2.__dict__)
"""

"""
#2 Classes and instances
class Employee:

    def __init__(this, sFirst, sLast, fPay):
        this.first = sFirst
        this.last = sLast
        this.pay = fPay
        this.email = str.lower(sFirst) + '.' + str.lower(sLast) + '@company.com'

emp1 = Employee('Hossein', 'Oliabak', 64000)
emp2 = Employee('Iman', 'Gh', 60000)
print('{} {}'.format(emp1.email, emp2.email))

print(Employee.__dict__)
print(emp1.__dict__)
print(emp2.__dict__)
"""

"""
#3 Classes and instances
class Employee:

    def __init__(this, sFirst, sLast, fPay):
        this.first = sFirst
        this.last = sLast
        this.pay = fPay
        this.email = str.lower(sFirst) + '.' + str.lower(sLast) + '@company.com'

    def fullname(this):
        return '{} {}'.format(this.first, this.last)

emp1 = Employee('Hossein', 'Oliabak', 64000)
emp2 = Employee('Iman', 'Gh', 60000)

print(Employee.fullname(emp1))
print(emp2.fullname())

print(Employee.__dict__)
print(emp1.__dict__)
print(emp2.__dict__)
"""

"""
#4 Class Variables
class Employee:

    raise_amount = 1.04

    def __init__(this, sFirst, sLast, fPay):
        this.first = sFirst
        this.last = sLast
        this.pay = fPay
        this.email = str.lower(sFirst) + '.' + str.lower(sLast) + '@company.com'

    def fullname(this):
        return '{} {}'.format(this.first, this.last)

    def apply_raise(this):
        this.pay = float(this.pay * this.raise_amount)

emp1 = Employee('Hossein', 'Oliabak', 64000)
emp2 = Employee('Iman', 'Gh', 60000)

print('Before raise', emp2.pay)
emp2.apply_raise()
print('After raise', emp2.pay)
print('All employees raise amount:', Employee.raise_amount)
print('emp1 raise amount', emp1.raise_amount)
print('emp2 raise amount', emp2.raise_amount)

emp2.raise_amount = 1.05
print('All employees raise amount:', Employee.raise_amount)
print('emp1 raise amount', emp1.raise_amount)
print('emp2 raise amount', emp2.raise_amount)
"""

"""
#5 Class Variables
class Employee:

    num_of_emps = 0

    def __init__(this, sFirst, sLast, fPay):
        this.first = sFirst
        this.last = sLast
        this.pay = fPay
        this.email = str.lower(sFirst) + '.' + str.lower(sLast) + '@company.com'

        Employee.num_of_emps += 1

print(Employee.num_of_emps)
emp1 = Employee('Hossein', 'Oliabak', 64000)
emp2 = Employee('Iman', 'Gh', 60000)
print(Employee.num_of_emps)
print(emp1.first)
"""

"""
#6 regular methods, class methods, and static methods (part 1: classmethos)
'''
Regular methods (the most used methods): automatically take the instance as the
first argument. and by convention we were calling this "self".
Class methods: take the class as the first argument. we add @classmethod decorator
to the top line of the method.
'''

class Employee:

    raise_amount = 1.04

    def __init__(self, sFirst, sLast, fPay):
        self.first = sFirst
        self.last = sLast
        self.pay = fPay
        self.email = str.lower(sFirst) + '.' + str.lower(sLast) + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = float(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, fAmount):
        cls.raise_amount = fAmount

emp1 = Employee('Hossein', 'Oliabak', 64000)
emp2 = Employee('Iman', 'Gh', 60000)

Employee.set_raise_amount(1.05)

print('All employees raise amount:', Employee.raise_amount)
print('emp1 raise amount', emp1.raise_amount)
print('emp2 raise amount', emp2.raise_amount)
"""

"""
#7 regular methods, class methods, and static methods (part 2: classmethods as
#alternative constructors)
'''
Class methods as alternative constructors: use of classmethods in order to
provide multiple of creating our objects
'''
class Employee:

    def __init__(self, sFirst, sLast, fPay):
        self.first = sFirst
        self.last = sLast
        self.pay = fPay
        self.email = str.lower(sFirst) + '.' + str.lower(sLast) + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

emp_str_1 = 'Hossein-Oliabak-64000'
emp_str_2 = 'Iman-Gh-60000'

emp1 = Employee.from_string(emp_str_1)
print(emp1.email)
"""

"""
#8 regular methods, class methods, and static methods (part 2: staticmethods)
'''
Static methods don't pass anything automatically. They don't depend on any
specific instance or class variable. We include them in the class because they
have some logical connection with the class.
'''
class Employee:

    def __init__(self, sFirst, sLast, fPay):
        self.first = sFirst
        self.last = sLast
        self.pay = fPay
        self.email = str.lower(sFirst) + '.' + str.lower(sLast) + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))
"""

# @ https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
