#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included). Go to the editor
"""
lst = []
for x in range(1500, 2701):
    if((x % 7 == 0) and (x %5 == 0)):
        lst.append(x)

print(lst)


# In[6]:


"""
2.	 Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ] 
Expected Output : 
60°C is 140 in Fahrenheit
45°F is 7 in Celsius 
"""

def FtoC(T):
    return 5*((T-32)/9)
def CtoF(T):
    return ((T/5)*9)+32
print(CtoF(60))
print(FtoC(45))


# In[2]:


"""
3.	 Write a Python program to guess a number between 1 to 9. Go to the editor
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
"""
from random import randint

randomNumber = randint(1,10)

guessed = False
while(not guessed):
    uinput = input()
    if(int(uinput) == randomNumber):
        print("Well guessed!")
        break;



# In[4]:


"""
4.
"""
str =""
for x in range(1,6):
    str += "*"*x
    str += "\n"
for x in range(4,0,-1):
    str += "*"*x
    str += "\n"
print(str)


# In[3]:


"""
6.    Write a Python program that accepts a word from the user and reverse it. Go to the editor
"""

userInput=input()
print(userInput[::-1])


# In[6]:


"""
7.	 Write a Python program to count the number of even and odd numbers from a series of numbers. Go to the editor
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output : 
Number of even numbers : 5
Number of odd numbers : 4
"""

# numbers is a set?
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
even = 0
odd = 0
for x in numbers:
    if (x % 2) == 0:
        even += 1
    else:
        odd += 1
print("Number of even numbers:", even)
print("Number of odd numbers:", odd)


# In[8]:


"""
8.	Write a Python program that prints each item and its corresponding type from the following list.
Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
 
"""
datalist = [1452, 11.23, 1+2, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for x in datalist:
    print(x)
    print(type(x))


# In[3]:


"""
9. datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
"""
string = ""
for x in range(0,7):
    if (x == 3 or x == 6):
        continue
    string += str(x)
    string += " "
print(string)


# In[ ]:




