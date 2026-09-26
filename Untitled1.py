#!/usr/bin/env python
# coding: utf-8

# In[34]:


n=5
for i in range (1,6):
    for j in range (1, 6):
        print ("*",end=" ")
    print()
    
    


# In[35]:


n = 5
for i in range(1, 6):
    for j in range(1, 6):
        if i == 1 or i == 5 or j == 1 or j == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# In[36]:


n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()


# In[38]:


n = 4
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()


# In[40]:


n = 4
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        if i==1 or i==n or k==0 or k==(2*i-1)-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

