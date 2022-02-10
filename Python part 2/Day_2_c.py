#!/usr/bin/env python
# coding: utf-8

# In[8]:


"""
Three is a Crowd
•	Make a list of names that includes at least four people.
•	Write an if test that prints a message about the room being crowded, if there are more than three people in your list.
•	Modify your list so that there are only two people in it. Use one of the methods for removing people from the list, don't just redefine the list.
•	Run your if test again. There should be no output this time, because there are less than three people in the list.
•	Bonus: Store your if test in a function called something like crowd_test.
"""
def crowd_test(lst):
    if len(lst) > 3:
        print("Crowded")

def ThreeIsaCrowd():
    lstNames = ["Abe", "Bob", "Charlie","David"]
    crowd_test(lstNames)
    lstNames.pop()
    lstNames.pop()
    crowd_test(lstNames)
    return ""
print(ThreeIsaCrowd())


# In[11]:


"""
Three is a Crowd - Part 2
•	Save your program from Three is a Crowd under a new name.
•	Add an else statement to your if tests. If the else statement is run, have it print a message that the room is not very crowded.
"""

def crowd_test_Part2(lst):
    if len(lst) > 3:
        print("Crowded")
    else:
        print("Not Crowded")

def ThreeIsaCrowdPart2():
    lstNames = ["Abe", "Bob", "Charlie","David"]
    crowd_test_Part2(lstNames)
    lstNames.pop()
    lstNames.pop()
    crowd_test_Part2(lstNames)
    return ""
print(ThreeIsaCrowdPart2())


# In[14]:


"""
Three is a Crowd - Part 2
•	Save your program from Three is a Crowd under a new name.
•	Add an else statement to your if tests. If the else statement is run, have it print a message that the room is not very crowded.
"""

def crowd_test_Part3(lst):
    if len(lst) > 5:
        print("Mob")
    elif len(lst) >= 3:
        print("Crowded")
    elif len(lst) >= 1:
        print("Not Crowded")
    else:
        print("Empty")

def SixIsaMob():
    lstNames = ["Abe", "Bob", "Charlie","David","Eve","Fred"]
    crowd_test_Part3(lstNames)
    lstNames.pop()
    lstNames.pop()
    crowd_test_Part3(lstNames)
    lstNames.pop()
    lstNames.pop()
    crowd_test_Part3(lstNames)
    lstNames.pop()
    lstNames.pop()
    crowd_test_Part3(lstNames)
    return ""
print(SixIsaMob())


# In[ ]:




