#!/usr/bin/env python
# coding: utf-8

# 

# In[97]:


#10 Hz Frequency
import numpy as np
import matplotlib.pyplot as plt
from math import pi

fs=1000
t=np.arange(0,1,1/fs)
f=10

y=np.sin(2*pi*f*t)
plt.figure(figsize=(16,6))
plt.title('Sine Wave-10 Hz sampled at 1000 Hz/sec',size=16)
plt.xlabel('Time(s)',size=16)
plt.ylabel('Amplitude',size=16)

plt.plot(t,y)


# In[55]:


from scipy.fftpack import fft

n=np.size(t)
fr=(fs/2)*np.linspace(0,1,n/2)

yf=fft(y)
ym=abs(yf[0:np.size(fr)])
plt.figure(figsize=(16,6))
plt.title('FFT of 10Hz sine wave',size=16)
plt.xlabel('frequency(Hz)',size=16)
plt.ylabel('Magnitude',size=16)
plt.plot(fr,ym)


# In[98]:


#100 Hz frequency
t=np.arange(0,1,1/fs)
f=100

y=np.sin(2*pi*f*t)
plt.figure(figsize=(16,6))
plt.title('Sine Wave-100 Hz sampled at 1000 Hz/sec',size=16)
plt.xlabel('Time(s)',size=16)
plt.ylabel('Amplitude',size=16)

plt.plot(t,y)


# In[57]:


n=np.size(t)
fr=(fs/2)*np.linspace(0,1,n/2)

yf=fft(y)
ym=abs(yf[0:np.size(fr)])
plt.figure(figsize=(16,6))
plt.title('FFT of 100Hz sine wave',size=16)
plt.xlabel('frequency(Hz)',size=16)
plt.ylabel('Magnitude',size=16)
plt.plot(fr,ym)


# In[99]:


#1 Khz frequency
fs=3000
t=np.arange(0,1,1/fs)
f=1000

y=np.sin(2*pi*f*t)
plt.figure(figsize=(16,6))
plt.title('Sine Wave-1 kHz sampled at 3000 Hz/sec',size=16)
plt.xlabel('Time(s)',size=16)
plt.ylabel('Amplitude',size=16)

plt.plot(t,y)


# In[64]:


n=np.size(t)
fr=(fs/2)*np.linspace(0,1,n/2)

yf=fft(y)
ym=abs(yf[0:np.size(fr)])
plt.figure(figsize=(16,6))
plt.title('FFT of 1kHz sine wave',size=16)
plt.xlabel('frequency(Hz)',size=16)
plt.ylabel('Magnitude',size=16)
plt.plot(fr,ym)


# In[109]:


#10 Hz square wave
from scipy import signal
import numpy as np

t = np.linspace(0,1,1000)
plt.figure(figsize=(16,6))
y= signal.square(2 * np.pi * 10 * t)
plt.plot(t,y)
plt.title('Sqaure wave - 10 Hz sampled at 1000 Hz /second',size=16)
plt.xlabel('Time(s)',size=16)
plt.ylabel('Amplitude',size=16)
plt.xlim(0,2)
plt.ylim(-2, 2)


# In[117]:


from scipy.fftpack import fft
n=np.size(t)
fr=np.linspace(0,1,n/2)

yf=fft(y)
ym=abs(yf[0:np.size(fr)])
plt.figure(figsize=(16,6))
plt.title('FFT of 10 Hz square wave',size=16)
plt.xlabel('frequency(Hz)',size=16)
plt.ylabel('Magnitude',size=16)
plt.plot(fr,ym)


# In[111]:


#100 Hz square wave
from scipy import signal
import numpy as np

t = np.linspace(0,1,1000)
plt.figure(figsize=(16,6))
y1=signal.square(2 * np.pi * 100 * t)
plt.plot(t,y1)
plt.title('Sqaure wave - 100 Hz sampled at 1000 Hz /second',size=16)
plt.xlabel('Time(s)',size=16)
plt.ylabel('Amplitude',size=16)
plt.xlim(0,2)
plt.ylim(-2,2)


# In[118]:


n=np.size(t)
fr=np.linspace(0,1,n/2)

yf=fft(y1)
ym=abs(yf[0:np.size(fr)])
plt.figure(figsize=(16,6))
plt.title('FFT of 100 Hz square wave',size=16)
plt.xlabel('frequency(Hz)',size=16)
plt.ylabel('Magnitude',size=16)
plt.plot(fr,ym)


# In[ ]:




