# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:10:24 2024

@author: xtang
"""

import os

class Tutorial:
    
    def indicate_directories(): 
        
        print(f'File is in : {os.path.dirname(os.path.realpath(__file__))}')
        print(f'Working directory is in : {os.getcwd()}')

        return 
    



def make_a_function():
    return 'Hello_world'


def make_an_explicit_function(a,b):
    """
    Function description :
        Simple function to add a with b.
        That also prints 'Hello World'.. for reasons.
    
    Inputs : 
        a : int or float variable
        b : int or float variable
    
    Returns : 
        The sum of a+b
    
    """
    
    c = a+b
    
    
    print('Hello World!')
    
    return c 
