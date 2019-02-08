#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:44:17 2019
@author: Biagio
"""

import argparse
import src.File_Manager, src.converter
from pathlib import Path


parser = argparse.ArgumentParser()  # Creiamo il nostro parser
parser.add_argument('file',help='lista file o dir da comprimere con lzw', nargs = '+', action = 'store') #aggiungo l'argomento di tipo lista da usare per la compressione/decompressione file/dir
gruppo_r = parser.add_argument_group() # Creiamo il gruppo necessario per le opzioni ricorsive 
gruppo_stdati = parser.add_mutually_exclusive_group() #gruppo opzioni dict o trie
gruppo_v = parser.add_argument_group() #opzione verbose
gruppo_r.add_argument("-r", "--ricorsivo", action="store_true", help = 'opzione per la ricerca ricorsiva all interno di dir') #argomento -r che permette la ricerca ricorsiva se file = dir
gruppo_stdati.add_argument("-t","--trie", action="store_true", help = 'opzione per usare LZW tramite struttura Trie') #argomento st_dati trie
gruppo_stdati.add_argument("-d","--dict", action="store_true", help = 'opzione per usare LZW tramite struttura Dict')#argomento st_dati dict
parser.add_argument("-v","--verbose", action="store_true", help = 'opzione per visualizzare la verbose ')

arg = parser.parse_args() #parse degli argomenti passati 

for _ in arg.file: 
    if not Path(_).exists() :
        print(_,' Not Found !!')
    else :
    
        if arg.verbose and arg.dict:
           verb = src.File_Manager.percent_compressed(src.File_Manager.write_file)
           verb(_,'d',True,arg.ricorsivo)
        elif arg.verbose and arg.trie:
           verb = src.File_Manager.percent_compressed(src.File_Manager.write_file)
           verb(_,'t',True,arg.ricorsivo)
        elif arg.verbose :
           verb = src.File_Manager.percent_compressed(src.File_Manager.write_file)
           verb(_,'t',True,arg.ricorsivo)    
        
        if arg.trie:
            src.File_Manager.write_file(_,'t',arg.verbose,arg.ricorsivo)
        elif arg.dict :
            src.File_Manager.write_file(_,'d',arg.verbose,arg.ricorsivo)
        else:
            src.File_Manager.write_file(_,'t',arg.verbose,arg.ricorsivo)
        
        
        