# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:37:44 2024

@author: s_decrusch22

lower() und isalpha()
"""
wort = "berlin"

def vokon_zählen(wort):
    vokale = "aeiou"
    wort_lower = wort.lower()
     
    wort_buchstaben = [i for i in wort_lower if i.isalpha()]
    vokale = [i for i in wort_buchstaben if i in vokale ]
    print (f"es gibt {len(vokale)} vokale und {len(wort_buchstaben)-len (vokale)}Konstanten.")
   # return [len(wort_buchstaben), len(vokale)]
  
vokon_zählen(wort)