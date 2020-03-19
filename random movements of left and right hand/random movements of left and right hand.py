#!/usr/bin/env python
# coding: utf-8

# In[28]:


import matplotlib.pyplot as plt
import scipy.io as io
da = io.loadmat('Subject1_2D.mat')
x = da['LeftBackward1']
plt.plot(x)
plt.show()


# In[30]:


x1 = da['RightBackward1']
plt.plot(x1)
plt.show()


# In[5]:


da


# In[ ]:




