# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 18:11:00 2021

@author: Asha
"""

import numpy as np
from scipy.linalg import solve

"""==================== INPUT ===================="""

A = np.array([[8, 5,2], [5, 9, 1], [4, 2, 7]])
b = [19, 5, 34]
x_0 = [1.0, -1.0, 3.0]


D = np.diag(A).T * np.eye(A.shape[0])
L = np.tril(A)
R = np.triu(A)

D_inv = np.linalg.pinv(D)
D_L = D + L
D_L_inv = np.linalg.inv(D+L)
L_R = L + R

B_jacobi = np.dot(-D_inv,L_R)
B_jacobi_inf = np.linalg.norm(B_jacobi,np.inf)

B_GaussSeidel = np.dot(-D_L_inv,R)
B_GaussSeidel_inf = np.linalg.norm(B_GaussSeidel, np.inf)





"""==============================================="""
np.set_printoptions(precision=4)
np.set_printoptions(suppress=True)



"""==============================================="""

jacobi = True
gauss = True
        



def AshaSchwegler_S10_Aufg3a(A, b, x, tol, opt):
    
    condition = True
    while condition == True:  

        if opt == jacobi:            
            
            for i in range(100):
                x = np.dot(np.linalg.inv(D),(b - np.dot(R, x)))
                print("Schritt " + str(i) +":" + str(x))                
                if i == 1:
                    x_1 = x
            condition = i <= np.log(tol*(1-B_jacobi_inf)/(np.linalg.norm(abs(x_0-x_1), np.inf)))/np.log(B_jacobi_inf)
                
            return x , x_1
        
        if opt == gauss:
            
            for j in range(100):
               x = np.dot(np.linalg.inv(L), b - np.dot(R, x))
               print ("Schritt " + str(j) +":" + str(x))
               if j == 1:
                    x_1 = x
            condition = i <= np.log(tol*(1-B_GaussSeidel_inf)/(np.linalg.norm(abs(x_0-x_1), np.inf)))/np.log(B_GaussSeidel_inf)

            return x, x_1                     
            




xn = AshaSchwegler_S10_Aufg3a(A, b, x_0, 0.0001, jacobi)
xn1 = AshaSchwegler_S10_Aufg3a(A, b, x_0, 0.0001, gauss)
print("Lösung: " + str(solve(A,x_0)))
