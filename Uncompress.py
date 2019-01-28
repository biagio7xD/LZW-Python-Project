#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 17:29:17 2019

@author: Gabriele Felici
"""
from stdati import trie_uncompression,Dict_uncompression
from converter import convertinint
from File_Manager import search #da togliere
import os #idem sopra
from pathlib import Path #idem

def Uncompress(bitstring,td):
    #MANCA IL CASO PARTICOLARE
    
    if td == 't' or 'T' or 'trie' :
        T = trie_uncompression()
    elif td == 'd' or 'D' or 'dict' :
        T = Dict_uncompression()
    else:
        T = trie_uncompression()
        
    numbits = 9
    val = convertinint(bitstring[0:numbits],numbits)
    string = chr(val)

    T.lastencoded = string
    T.last = val #nel caso del trie salva l'ultimo nodo, nel dict non fa nulla
    indexiniziale = 0
    indexfinale = 9
    
    while val != 256:       
        if T.dim + 1 == 2**numbits:
            numbits = numbits+1      
        indexiniziale = indexfinale
        indexfinale = indexfinale + numbits
        valstring = bitstring[indexiniziale:indexfinale]
        val = convertinint(valstring, numbits)
 
        if val != 256:
            string = string + T.find(val)
    
    return string


def Uncompress_file(filename,dt):
    i = 0
    bin_cod,path = search(filename) #richiamo la funzione di ricerca file/dir
    
    for _ in bin_cod :
        dec = Uncompress(_,dt) #ottengo stringa decompressa
        name = Path(path[i]) #estraggo path del file decompresso
        f = open(os.path.join(name.parent,name.stem+'.txt'), 'w') #creazione nuovo file decompresso
        f.write(dec)
        f.close()
        name.unlink() #rimuovo il file compresso
        i += 1
        
#Uncompress_file('Compressed','d')