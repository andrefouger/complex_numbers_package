# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 09:07:37 2020

@author: AndreFougeront
"""
import numpy as np
import math

class ComplexNumberClass:
    def __init__(self,realZ,imaginaryZ):
        """
            Create class objects that are composed of two attributes : real part, imaginary part.
        """
        self.real=realZ
        self.imaginary=imaginaryZ
        
    def get_Real_Part(self):
        """
            Method to Get the real part of a class object.
        """
        return self.real
    
    def get_Imaginary_Part(self):
        """
            Method to Get the imaginary part of a class object.
        """
        return self.imaginary
    
    def get_Module(self):
        """
            Method to retrieve tha value corresponding to the module, it is not an attribute of the objects of the class.
        """
        module=np.sqrt(self.real**2+self.imaginary**2)
        return module
    
    def get_Phase(self):
        """
            Method to retrieve tha value corresponding to the phase argument, it is not an attribute of the objects of the class
            the phase arg calcul is different if the real part or the imaginary part or both are/is equal to zero.
        """
        if self.imaginary==0 and self.real==0:
            phase=0
        elif self.imaginary==0:
            phase=((np.sign(-self.real))*math.pi+math.pi)/2
        elif self.real==0:
            phase=math.pi/2*np.sign(self.imaginary)
        else :
            phase=np.arctan2(self.imaginary,self.real)
        return phase