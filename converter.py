#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 09:48:22 2018

@author: Gabriele Felici
"""
BYTEDIM = 8
 
''' Funzione che converte un valore intero in una stringa "0/1" '''        
def convertinbits(value, numbits):
    B = ''
    for _ in range(0,numbits):
        B = str(int(value)%2) + B
        value = int(value)/2
    return B

''' Funzione che converte una stringa "0/1" in un valore intero '''    
def convertinint(bits, numbits):
    value = 0
    for i in range(0,numbits):
        bit = bits[numbits-1-i]
        value = value + (2**i) * int(bit)
    return value

''' Funzione che dato in ingresso una stringa rappresentante un byte, torna il valore numerico di quel byte '''
def number_from_bytestring(bitstring):
    v = 0
    power = [2**i for i in range(0,BYTEDIM)]
    for j in range(0,BYTEDIM):
        v = v + int(bitstring[j])*power[BYTEDIM-1-j]
    return v



