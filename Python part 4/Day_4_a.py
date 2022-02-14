#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""
1.Create a function func() which prints a text ‘Hello World’
"""

def func():
    print("Hello World")
func()


# In[5]:


"""
2.Create a function which func1(name)  which takes a value name and prints the output “Hi My name is Google’
"""
def func1(name):
    print('Hi My name is {name}'.format(name=name))
func1("Google")


# In[6]:


"""
3.Define a function func3(x,y,z) that takes three arguments x,y,z where z is true it will return x and when z is false it should return y . func3(‘hello’goodbye’,false)
"""
def func3(x,y,z):
    if z:
        return x
    else:
        return y
func3("hello", "good bye", False)


# In[7]:


"""
4.define a function func4(x,y) which returns the product of both the values.
"""
def func4(x,y):
    return x*y
func4(4,5)


# In[8]:


"""
5.define a function called as is_even that takes one argument , which returns true when even values is passed and false if it is not."""
def is_even(x):
    if(x%2 == 0):
        return True
    else:
        return False
is_even(2)


# In[9]:


"""
6.define a function that takes two arguments ,and returns true if the first value is greater than the second value and returns false if it is less than or equal to the second.
"""

def six(x,y):
    if(x>y):
        return True
    else:
        return False


# In[13]:


"""
7.Define a function which takes arbitrary number of arguments and returns the sum of the arguments.
"""

def seven(*argv):
    sum = 0
    for i in argv:
        sum += i
    return sum
seven(5,5,5,5,10)


# In[15]:


"""
8.Define a function which takes arbitrary number of arguments and returns a list containing only the arguments that are even.
"""

def eight(*argv):
    evenlst = []
    for i in argv:
        if (i % 2 ==0):
            evenlst.append(i)
    return evenlst
eight(1,2,3,4,5,6,7,8,9)


# In[27]:


"""
9.Define a function that takes a string and returns a matching string where every even letter is uppercase and every odd letter is lowercase 
"""

def nine(inputstr):
    strbuilder = ""
    flag = True
    for i in range(len(inputstr)):
        if i %2 ==0:
            strbuilder = strbuilder + inputstr[i].upper()
        else:
            strbuilder = strbuilder + inputstr[i].lower()
    return strbuilder
nine("ABCDEFG")


# In[28]:


"""
10.Write a function which gives lesser than a given number if both the numbers are even, but returns greater if one or both or odd.
"""

def ten(x,y):
    if (x %2 ==0 and y%2==0):
        if (x > y):
            return y
        else:
            return x
    else:
        if (x > y):
            return x
        else:
            return y
ten(5,10)


# In[33]:


"""
11.Write a function which takes  two-strings and returns true if both the strings start with the same letter.
"""
def eleven(a,b):
    if a[0] == b[0]:
        return True
    else:
        return False
eleven("abc","ads")


# In[61]:


"""
12.Given a value,return a value which is twice as far as other side of 7
"""
def twelve(x):
    difference = x -7
    return ((0-(difference))*2) + 7
twelve(0)


# In[66]:


"""
13.A function that capitalizes first and fourth character of a word in a string.
"""
def thirteen(x):
    return x[0].upper() + x[1:3] + x[3:4].upper() + x[4:]
thirteen("asdfasdfasdf")


# In[ ]:




