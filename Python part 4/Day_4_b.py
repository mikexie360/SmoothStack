#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
1.	Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this: 
Order Number	Book Title and Author	Quantity	Price per Item
34587	Learning Python, Mark Lutz	4	40.95
98762	Programming Python, Mark Lutz	5	56.80
77226	Head First Python, Paul Barry	3	32.95
88112	Einführung in Python3, Bernd Klein	3	24.99

"""
"""
Write a Python program, which returns a list with 2-tuples. Each tuple consists of a the order number and the product of the price per items and the quantity. The product should be increased by 10,- € if the value of the order is smaller than 100,00 €. 
Write a Python program using lambda and map.
"""

lst = [["Order Number", "Book Title and Author", "Quantity","Price per Item"],[34587,"Learning Python, Mark Lutz", 4, 40.95],[98762,"Programming Python, Mark Lutz",5,56.80],[77226,"Head First Python, Paul Barry", 3,32.95],[88112,"Einfuhrung in Python3, Bernd Klein", 3, 24.99]]
print(lst)


# In[6]:


def func(lst):
    returnlst = []
    for i in lst:
        totalcost = i[2] * i[3]
        if (totalcost < 100):
            totalcost += 10
        tuplebuilder = (i[0], totalcost)
        returnlst.append(tuplebuilder)
    return returnlst
func(lst[1:])


# In[9]:


"""
3.	The same bookshop, but this time we work on a different list. The sublists of our lists look like this: 
[ordernumber, (article number, quantity, price per unit), ... (article number, quantity, price per unit) ] 
Write a program which returns a list of two tuples with (order number, total amount of order).
"""
lst2 = [[34587,("Learning Python, Mark Lutz", 4, 40.95)],[98762,("Programming Python, Mark Lutz",5,56.80)],[77226,("Head First Python, Paul Barry", 3,32.95)],[88112,("Einfuhrung in Python3, Bernd Klein", 3, 24.99)]]
print(lst2)


# In[11]:


def func(lst):
    returnlst = []
    for i in lst:
        totalcost = i[1][1] * i[1][2]
        if (totalcost < 100):
            totalcost += 10
        tuplebuilder = (i[0], totalcost)
        returnlst.append(tuplebuilder)
    return returnlst
func(lst2)


# In[ ]:




