#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:36:51 2019

@author: Gabriele Felici
"""
from src.stdati import trie, lzw_dict
from src.converter import convertinbits
import time

def timer(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        f = func(*args, **kwargs)
        t2 = time.time()
        print('Compress Algorithm took {} seconds'.format(t2-t1))
        return f
    return inner


def Compress(input_File, char):
    '''Funzione che, dati in input un file e il tipo di compressione mediante d or t
    comprime sequenzialmente codificando carattere per carattere il file in input.
    Per ogni carattere le strutture dati valutano se può fare parte di una sequenza
    più grande, e al check (quando il carattere non può più essere 'aggregato')
    viene scritto il valore che rappresenta la sequenza.'''
    
    stringa_compressa = []
    bitstring = ""
    if char == "D" or char == "d" :
        T = lzw_dict()
    
    elif char == "T" or char == "t" :
        T = trie()

    else :
        T = lzw_dict()        
        
    dim = len(input_File)
    counter = 0
    numbits = 9
    #ciclo che esamina ogni carattere   
    for C in input_File:
        #provo a cercare il prossimo carattere
        val = T.search(C)
        counter = counter + 1 #incremento il contatore dei caratteri
        
        if T.check() :
            stringa_compressa.append(val)
            if T.dim-1 == 2**numbits: #dim è ora il prossimo valore che verrà associato, il valore massimo attuale è T.dim-1:
                numbits = numbits + 1 #so di avere valori fino a T.dim-1
                
            bitstring = bitstring + convertinbits(val,numbits)
            val = T.search(C)
        
        #siamo arrivati alla fine e ci troviamo in un nodo intermedio, scriviamo il valore
        if counter == dim :
            stringa_compressa.append(val) #non è necessario controllare T.dim
            bitstring = bitstring + convertinbits(val,numbits)
    
    stringa_compressa.append(256);
    bitstring = bitstring + convertinbits(256,numbits)

    return stringa_compressa, bitstring 
