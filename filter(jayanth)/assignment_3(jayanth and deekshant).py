#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np


# In[6]:


data = np.loadtxt('datameditation200.txt')


# In[7]:


import matplotlib.pyplot as plt


# In[8]:


data


# In[9]:


data.size


# In[10]:



plt.plot(data)
plt.title("RAW data in meditating state   FP2-F4")


# In[30]:


from scipy import signal
from scipy.signal import butter, iirnotch, lfilter



def butter_highpass(cutoff, fs, order):
    nyq = 0.5*fs
    normal_cutoff = cutoff/nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False, output='ba')
    return b, a

def highpass(data, fs, order,cutoff_high):
    b,a = butter_highpass(cutoff_high,fs, order=order)
    x = lfilter(b,a,data)
    return x


fs = 1000
order = 5


hsignal = highpass(data, fs, order,5)




plt.plot(hsignal)


# In[28]:


from scipy import signal
from scipy.signal import butter, iirnotch, lfilter

def butter_lowpass(cutoff, fs, order,):
    nyq = 0.5*fs
    normal_cutoff = cutoff/nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False, output='ba')
    return b, a



def lowpass(data, fs, order, cutoff_low):
    b,a = butter_lowpass(cutoff_low, fs, order=order)
    y = lfilter(b,a,data)
    return y



fs = 1000
order = 5
cutoff_low=90
lsignal = lowpass(hsignal, fs, order,cutoff_low)

plt.plot(lsignal)


# In[39]:



def bandpass(data,fs,order,fl,fh):
    hsignal = highpass(data, fs, order,fl)
    lsignal = lowpass(hsignal, fs, order,fh)
    
    plt.plot(lsignal)
    
    
bandpass(data,fs,order,8,12)


# In[ ]:





# In[ ]:




