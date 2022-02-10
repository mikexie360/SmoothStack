#!/usr/bin/env python
# coding: utf-8

# In[6]:


""" 
1.	Write a string that returns just the letter ‘r’ from ‘Hello World’
For example, ‘Hello World’[0] returns ‘H’.You should write one line of code. Don’t assign a variable name to the string.
"""
print('Hello World'[8])


# In[7]:


"""
2.	String slicing to grab the word ‘ink’ from the word  ‘thinker’
"""
print('thinker'[2:5])


# In[8]:


"""
S=’hello’,what is the output of h[1]
"""
S='hello'
print(S[1])


# In[9]:


"""
3.	S=’Sammy’ what is the output of s[2:]”
"""
S="Sammy"
print(S[2:])


# In[10]:


"""
3.	S=’Sammy’ what is the output of s[2:]”
"""
print(set('Mississippi'))


# In[11]:


"""
5.	The word or whole phrase which has the same sequence of letters in both directions is called a palindrome. Here are few examples:

Stats
Amore, Roma
No 'x' in Nixon
Was it a cat I saw?

As you see, case of the letters is ignored. Spaces and punctuations are ignored too.
Your goal in this programming exercise is to determine, whether the phrase represents a palindrome or not.
Input data contains number of phrases in the first line.
Next lines contain one phrase each.
Answer should have a single letter (space separated) for each phrase: Y if it is a palindrome and N if not.
Example:
input data:
3
Stars
O, a kak Uwakov lil vo kawu kakao!
Some men interpret nine memos

answer:
N Y Y

Can you please derive a python code.
"""

# import regular expressions
import re

def palindromeChecker(inputString: str) -> str:
    # get rid of space
    mystr = inputString.replace(" ","")
    # get rid of punctuations
    mystr = re.sub(r'[\W]', "", mystr)
    # make all lower case
    mystr = mystr.lower()
    # check
    i = 0
    j = len(mystr) - 1
    while (i < j):
        if (mystr[i] != mystr[j]):
            return 'N'
        i += 1
        j -= 1
    return 'Y'

print(palindromeChecker("Stars")) # N
print(palindromeChecker("O, a kak Uwakov lil vo kawu kakao!")) # Y
print(palindromeChecker("Some men interpret nine memos")) # Y


# In[ ]:





# In[ ]:




