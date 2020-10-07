# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 09:21:00 2020

@author: AndreFougeront
"""

import complex_number
import numpy as np
import random
import pytest

#test set creation

# two possibles val for z1 real part: 0 and a random val in [0 10]
absListZ1TestReal=[0,random.uniform(0,10)]
# two possibles val for z1 imaginary part: 0 and a random val in [0 10]
absListZ1TestImaginary=[0,random.uniform(0,10)]
#the two associated signs possible for the real and the imaginary parts of z1
Signs=[1,-1]

#empty list filled with all the possible cases of value of z1 real and imaginary parts
z1TestList=[]

for kx in Signs:
    for x in absListZ1TestReal:
        for ky in Signs:
            for y in absListZ1TestImaginary:
               z1TestList.append([kx*x,ky*y])

# same creation for z2
absListZ2TestReal=[0,random.uniform(0,10)]
absListZ2TestImaginary=[0,random.uniform(0,10)]
z2TestList=[]

for kx in Signs:
    for x in absListZ2TestReal:
        for ky in Signs:
            for y in absListZ2TestImaginary:
               z2TestList.append([kx*x,ky*y])                               

# z2 shuffle to change possibles pair between z1 and z2
random.shuffle(z2TestList)

#empty list, final list of put z1 z2 real and imaginary part inside a class object and ordered in pairs (z1,z2) for each list element
test_z1_z2_List=[]
for k in range(len(z1TestList)):
    complexNumberToCreateZ1=complex_number.ComplexNumberClass(z1TestList[k][0],z1TestList[k][1])
    complexNumberToCreateZ2=complex_number.ComplexNumberClass(z2TestList[k][0],z2TestList[k][1])
    test_z1_z2_List.append([complexNumberToCreateZ1,complexNumberToCreateZ2])

#Creation of the same list of number but not created with the new built class but with the exiting modules instead
 # this list will be used as the output to compare with the output of the method tested
test_z1_z2_List_complex=[[z1TestList[k][0]+z1TestList[k][1]*1j,z2TestList[k][0]+z2TestList[k][1]*1j] for k in range(len(z1TestList))]


#entry of the tests, composed of the two lists, for each test case, there is z1,z2 of the test set 
#and z1,z2 of the list used to verify the results of the new methods
entry__expected_result_list = [(test_z1_z2_List[k],test_z1_z2_List_complex[k]) for k in range(len(z1TestList))]

@pytest.mark.parametrize("entry,expected_result", entry__expected_result_list) 
def test_get_real_part(entry,expected_result):
    assert entry[0].get_Real_Part()==np.real(expected_result[0])

#get_imaginary_part
@pytest.mark.parametrize("entry,expected_result", entry__expected_result_list)
def test_get_imaginary_part(entry,expected_result):
    assert entry[0].get_Imaginary_Part()==np.imag(expected_result[0])

#get_Modulo
@pytest.mark.parametrize("entry,expected_result", entry__expected_result_list)
def test_get_Module(entry,expected_result):
    assert entry[0].get_Module()==np.abs(expected_result[0])

#get_Phase
@pytest.mark.parametrize("entry,expected_result", entry__expected_result_list)
def test_get_Phase(entry,expected_result):
    assert entry[0].get_Phase()==np.angle(expected_result[0])

#addition
@pytest.mark.parametrize("entry,expected_result", entry__expected_result_list)
def test_Addition(entry,expected_result):
    additionOfEntries=complex_number.addition(entry[0],entry[1])
    assert additionOfEntries.get_Real_Part()+1j*additionOfEntries.get_Imaginary_Part()==expected_result[0]+expected_result[1]
    
#substraction_part1_less_part2
@pytest.mark.parametrize("entry,expected_result", entry__expected_result_list)
def test_Substraction_part1_less_part2(entry,expected_result):
    substraction_Entry1_less_Entry2=complex_number.substraction_part1_less_part2(entry[0],entry[1])
    assert substraction_Entry1_less_Entry2.get_Real_Part()+1j*substraction_Entry1_less_Entry2.get_Imaginary_Part()==expected_result[0]-expected_result[1]
    
#multiplication
@pytest.mark.parametrize("entry,expected_result", entry__expected_result_list)
def test_multiplication(entry,expected_result):
    multiplicationOfEntries=complex_number.multiplication(entry[0],entry[1])
    assert multiplicationOfEntries.get_Real_Part()+1j*multiplicationOfEntries.get_Imaginary_Part()==expected_result[0]*expected_result[1]

#division_part1_dividedby_part2

#here the case of divided by zero is not completely tested
@pytest.mark.parametrize("entry,expected_result", entry__expected_result_list)
def test_division_part1_dividedby_part2(entry,expected_result):
    division_Entry1_dividedby_Entry2=complex_number.division_part1_dividedby_part2(entry[0],entry[1])
    if expected_result[1]!=0:
        expected_Division=expected_result[0]/expected_result[1]
        if np.real(expected_Division)-10**(-14)<division_Entry1_dividedby_Entry2.get_Real_Part()<np.real(expected_Division)+10**(-14) and np.imag(expected_Division)-10**(-14)<division_Entry1_dividedby_Entry2.get_Imaginary_Part()<np.imag(expected_Division)+10**(-14):
            assert True
        else:
            assert False
    else:
        assert True
