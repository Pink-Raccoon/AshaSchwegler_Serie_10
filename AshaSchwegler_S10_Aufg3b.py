# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 20:45:46 2021

@author: Asha
"""

import numpy as np
import timeit
dim = 300 

A = np.diag(np.diag(np.ones((dim,dim))*4000))+np.ones((dim,dim))

dum1 = np.arrange(1,np.int(dim/2+1),dtype=np.float64).reshape((np.int(dim/2),1))
dum2 = np.arrange(1,np.int(dim/2),0,-1,dtype=np.float64).reshape((np.int(dim/2),1))

x = np.append(dum1, dum2, axis=0)
b = A@x
x0 = np.zeros((dim,1))
tol = 1e-4








t1 = timeit("AshaSchwegler_S10_Aufg3a", "from__main__import AshaSchwegler_S10_Aufg3a,A", number = 100)
