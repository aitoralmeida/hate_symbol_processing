# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 15:52:25 2018

@author: aitor
"""

import os

FILE_PRE = '????'
PATH = '?????'
SEP = '_'

def rename_files ():
    cont = 1
    for old_filename in os.listdir(PATH):
        try:
            name, extension = os.path.splitext(old_filename)
            new_filename = FILE_PRE + SEP + str(cont) + extension
            os.rename(PATH+old_filename, PATH+new_filename) 
            cont += 1        
        except: 
            print old_filename


if __name__ == "__main__":
    print 'Starting'
    rename_files()
    print 'fin'