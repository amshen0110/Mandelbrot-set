#!/usr/bin/env python
# coding: utf-8

# In[4]:


complex(1,2)


# In[26]:


#recrusive formula
def f1(c,z):
    return z**2 + c #exponent changes the "folds" of mandelbrot plots


# In[27]:


c1 = complex(1,2)
z0 = 0 #z starts at zero when you count
f1(c1,z0)


# In[28]:


z1= f1(c1,z0)
z2= f1(c1,z1)
z3= f1(c1,z2)

f1(c1,z3)
#the absolute value divergies thus not in mandelbrot set


# In[29]:


def diverges(c,z=0, niter=20, b= 20000):#c* = of arbitrary size
    #20 000 is the boundary and n inter in the number of iterations
    c = complex(*c)
    for i in range(niter):
        z=f1(c,z)
        if abs(z) > b: return 1 #this means diverges
    return 0    
    


# In[30]:


diverges(*c1) #testing whether or not the result is diverging


# In[31]:


diverges(complex(0,0)) #testing whether or not non divergence works


# In[32]:


from matplotlib import pyplot as plt
import numpy as np


# In[66]:


res= 100#ls wide/200 points between minimum and maximum
xmin, xmax= -1.2,1.2
ymin,ymax = -1.2,1.2

xx, yy = np.meshgrid(np.linspace(xmin, xmax, res), #returns two outputs, last part of np.linspace is resolution/pixels
                     np.linspace(ymin, ymax, res))


# In[67]:


np.set_printoptions(2) #changing the print options


# In[68]:


xx #display, the axis is just the matrix of the shape of the whole grid, shows all the x coordinates


# In[69]:


yy #shows all the y coordinates


# In[ ]:





# In[70]:


#pairs up all x and y, so get a list of all the points
#numpy.dot_c function is conventional for doing this

p= np.c_[xx.ravel(), yy.ravel()]
#this pairs up all possible coordinates


# In[71]:


p.shape


# In[72]:


#for each point can calculate whether or not diverges

mandelbrot=[diverges(c) for c in p]


# In[73]:


mandelbrot= np.array(mandelbrot).reshape(res, res)
#change from list into array first


# In[74]:


plt.contourf(mandelbrot)


# In[75]:


#another function that distorts functions
plt.contourf(mandelbrot)


# In[76]:


#write a loop for points
#can save image at each point
#make a gif out of it


# In[104]:


def plot_mandelbrot(k):
    def f1(c,z,k):
        return z**k + c
    
    def diverges(c,z=0, niter=20, b= 20000):
        c = complex(*c)
        for i in range(niter):
            z=f1(c,z,k)
            if abs(z) > b: return 1 #this means diverges
        return 0    

    mandelbrot=[diverges(c) for c in p]
    mandelbrot= np.array(mandelbrot).reshape(res, res)
    plt.contourf(mandelbrot)
    plt.savefig(f'mandelbrot_{k}.png')


# In[105]:


plot_mandelbrot(2.2)


# In[106]:


ks= np.linspace(1,8,100)
for k in ks:
    plot_mandelbrot(k)
    
    


# In[107]:


fns = [f'mandelbrot_{k}.png' for k in ks]


# In[108]:


import imageio


# In[111]:


#imageio make gif
images = []
for file_name in fns:
        images.append(imageio.imread(file_name))
imageio.mimsave("output.gif", images)


# In[ ]:




