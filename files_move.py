# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 13:45:09 2018

@author: directory created in additional to files move and copy
"""

import os, glob, shutil

for f in glob.glob('*.py'):
    (name, ext) = f.split('.')
    if not os.path.exists(name):
# create targeted name directory
        os.mkdir(name)
        print('mkdir', name)
    
    if os.path.isfile(f) and os.access(f, os.R_OK):
# move files into targeted name directory
#        shutil.move(f, name)
#        print('mv', f, name)
# copy files into targeted name directory       
        shutil.copy2(f, name)
#        print('cp', f, name)
    


