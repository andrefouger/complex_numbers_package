# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:46:16 2020

@author: AndreFougeront
"""

# exemples d'utilisation

#import de la classe
import complex_number

#création d'un complexe
z1=complex_number.ComplexNumberClass(1,2)
#création d'un deuxième complexe
z2=complex_number.ComplexNumberClass(-1,2.5)
#addition des deux complexes
z12=complex_number.addition(z1,z2)
#récupération du module de l'addition
m=z12.get_Module()
#récupération de l'argument de l'addition
p=z12.get_Phase()

#multiplication des complexes z1 z2
z12_mult=complex_number.multiplication(z1,z2)

#Complexe z1 divisé par complexe z2
z12_div=complex_number.division_part1_dividedby_part2(z1,z2)

#Complexe z2 soustrait au complexe z1
z12_subst=complex_number.substraction_part1_less_part2(z1,z2)

