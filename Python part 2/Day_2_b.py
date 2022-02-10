#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""
1.	Create a list with one number, one word and one float value. Display the output of the list.
"""
list1 = [1,"hello world",3.14]
print(list1)


# In[5]:


"""
2.	I have a nested list [1,1[1,2]], how to grab the value of 2 from the list.
"""

nestedlist = [1,1,[1,2]]
print(nestedlist[2][1])


# In[7]:


"""
3.	lst=['a','b','c'] What is the result of lst[1:]?
"""

lst = ['a','b','c']
print(lst[1:])


# In[8]:


"""
4.	Create a dictionary with weekdays an keys and week index numbers as values.do assign dictionary to a variable
"""

dct = {"monday":1, "tuesday":2, "wednesday":3, "thursday":4, "friday":5}
print(dct)


# In[13]:


"""
5.	D={‘k1’:[1,2,3]} what is the output of d[k1][1]
"""
D={'k1':[1,2,3]}
print(D['k1'][1])


# In[14]:


"""
6.	Can you create a list [1,[2,3]] into a tuple
"""

lst = [1,[2,3]]
print(tuple(lst))


# In[19]:


"""
7.	With a single set function can you turn the word ‘Mississippi’ to distinct character word.
"""
word = 'Mississippi'
st = set(word)
print(st)


# In[21]:


"""
8.	Can you add an element ‘X’ to the above created set
"""
st.add('X')
print(st)


# In[25]:


"""
9.	Output of set([1,1,2,3])
"""

st =([1,1,2,3])
print(set(st))


# In[26]:


"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included).
	The numbers obtained should be printed in a comma-separated sequence on a single line.
	Hints: 
	Consider use range(#begin, #end) method

"""

lst = []
for x in range(2000, 3201):
    if((x % 7 == 0) and (x %5 != 0)):
        lst.append(x)

print(lst)


# In[48]:


"""
	Write a program which can compute the factorial of a given numbers.
	The results should be printed in a comma-separated sequence on a single line.
	Suppose the following input is supplied to the program:
	8
	Then, the output should be:
	40320
	

	Hints:
	In case of input data being supplied to the question, it should be assumed to be a console input.

"""

def fact(x:int)->int:
    # base case
    if x == 0:
        return 1
    else:
        return x * fact(x-1)
# get user input

#x = int(raw_input())

print(fact(int(input())))


# In[49]:


"""
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
	Suppose the following input is supplied to the program:
	8
	Then, the output should be:
	{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
	

	Hints:
	In case of input data being supplied to the question, it should be assumed to be a console input.
	Consider use dict()

"""

def squaredict(i:int) -> dict:
    dct = dict()
    for x in range(1, i+1):
        dct[x] = x*x
    return(dct)

print(squaredict(int(input())))


# In[51]:


"""
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
	Suppose the following input is supplied to the program:
	34,67,55,33,12,98
	Then, the output should be:
	['34', '67', '55', '33', '12', '98']
	('34', '67', '55', '33', '12', '98')

"""

userInput = input()
userInput = userInput.split(",")

lst = userInput
tple =tuple(lst)

print(lst)
print(tple)


# In[57]:


"""
Question:
	Define a class which has at least two methods:
	getString: to get a string from console input
	printString: to print the string in upper case.
	Also please include simple test function to test the class methods.
	

	Hints:
	Use __init__ method to construct some parameters

"""

class printStringClass(object):
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())
def test():
    testObj = printStringClass()
    testObj.getString()
    testObj.printString()
test()


# In[ ]:




