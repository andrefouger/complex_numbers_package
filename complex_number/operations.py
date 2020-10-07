# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:03:53 2020

@author: AndreFougeront
"""

import numpy as np

from .ComplexNumberClass import ComplexNumberClass


def addition(z1,z2):
    """
        Method called to add one ComplexNumberClassClass object to another by separating the calculs with the real and the imaginary part.
        After the calculs a new class object is created with the new attributes val.
    """
    z3_Real=z1.real+z2.real
    z3_Imaginary=z1.imaginary+z2.imaginary
    z3=ComplexNumberClass(z3_Real,z3_Imaginary)
    return z3

def substraction_part1_less_part2(z1,z2):
    """
        Method called to substract one ComplexNumberClassClass object to another by separating the calculs with the real and the imaginary part.
        It is the second input that is substracted to the first input.
        After the calculs a new class object is created with the new attributes val.
        
    """
    z3_Real=z1.real-z2.real
    z3_Imaginary=z1.imaginary-z2.imaginary
    z3=ComplexNumberClass(z3_Real,z3_Imaginary)
    return z3

def multiplication(z1,z2):
    """
        Method called to multiply one ComplexNumberClassClass object to another by separating the calculs with the real and the imaginary part.
        After the calculs a new class object is created with the new attributes val.
    """
    z3_Real=z1.real*z2.real-z1.imaginary*z2.imaginary
    z3_Imaginary=z1.real*z2.imaginary+z1.imaginary*z2.real
    z3=ComplexNumberClass(z3_Real,z3_Imaginary)
    return z3

def division_part1_dividedby_part2(z1,z2):
    """
        Method called to divide one ComplexNumberClassClass object to another by substracting the phases arguments and dividing the module arguments,
        and then reconstruct a new class object.
        Separate the case when the dividing input is equal to zero.
        
    """
    z2_Module=z2.get_Module()
    if z2_Module==0:
       return "division impossible"
    z1_Module=z1.get_Module()
    z3_Module=z1_Module/z2_Module
    z3_Phase=z1.get_Phase()-z2.get_Phase()
    z3=ComplexNumberClass(z3_Module*np.cos(z3_Phase),z3_Module*np.sin(z3_Phase))
    return z3
