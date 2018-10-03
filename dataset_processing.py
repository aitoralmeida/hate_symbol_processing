# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 15:52:25 2018

@author: aitor
"""
from random import shuffle
from shutil import copyfile
import os

TRUE_EXAMPLES = ['antisemitism', 'homophobia', 'inmigrants', 'islamophobia', 'racism']
FALSE_EXAMPLES = ['no_hate']
PATH_RENAMED = './2_renamed/'
PATH_TRAIN = './train/'
PATH_VAL = './val/'
PATH_TEST = './test/'
PATHS = ['antisemitism/', 'homophobia/', 'inmigrants/', 'islamophobia/', 
         'no_hate_comic/', 'no_hate_david_star/', 'no_hate_flags/', 
         'no_hate_inmigrants/', 'no_hate_meme/', 'no_hate_pexels/', 
         'no_hate_propaganda/', 'no_hate_sign/', 'no_hate_tattoo/', 
         'racism/']

LABEL_FILE = 'labels.txt'
TRAIN_SPLIT = 0.60
VAL_SPLIT = 0.20
TEST_SPLIT = 0.20

def create_labels():
    for root, dirs, files in os.walk('.'):
        for name in files:
            if FALSE_EXAMPLES[0] in name:
                print 0
            else:
                print 1

def rename_files ():
    FILE_PRE = 'no_hate_pexels'
    PATH = './no_hate_pexels/'
    SEP = '_'

    cont = 1
    for old_filename in os.listdir(PATH):
        try:
            name, extension = os.path.splitext(old_filename)
            new_filename = FILE_PRE + SEP + str(cont) + extension
            os.rename(PATH+old_filename, PATH+new_filename) 
            cont += 1        
        except: 
            print old_filename
            
def create_train_val_test():
    for path in PATHS:
        filenames = os.listdir(PATH_RENAMED + path)  
        shuffle(filenames)
        total_files = len(filenames)
        train_total =  int(total_files * TRAIN_SPLIT)
        val_total = int(total_files * VAL_SPLIT)
        test_total = int(total_files * TEST_SPLIT)
        train_filenames = filenames[:train_total]
        val_filenames = filenames[train_total:train_total+val_total]
        test_filenames = filenames[train_total+val_total:]
        print path
        print 'Train: ' + str(len(train_filenames))
        print 'Val: ' + str(len(val_filenames))
        print 'Test: ' + str(len(test_filenames))
        for filename in train_filenames:
            copyfile(PATH_RENAMED + path + filename, PATH_TRAIN + filename)
        for filename in val_filenames:
            copyfile(PATH_RENAMED + path + filename, PATH_VAL + filename)
        for filename in test_filenames:
            copyfile(PATH_RENAMED + path + filename, PATH_TEST + filename)
        
        
        
    


if __name__ == "__main__":
    print 'Starting'
    create_train_val_test()
    print 'fin'