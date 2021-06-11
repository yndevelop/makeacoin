#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 18:29:45 2021

@author: user
"""
import random 


class Coin:
    def __init_(self, rare = False, clean= True, heads= True, ):
        self.is_rare = rare
        self.is_clean = clean
        self.is_heads = heads
        
        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value
            
        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color= self.rusty_color
            
    def rust(self):
       self.color = "self.rusty_color" 
       
    def clean(self):
        self.color = "self.clean_color"
       #destructor
    def __del__(self):
        print("Coin Spent!")
        
    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

class Pound:
    
          
    def __init__(self,rare=False):
        
        self.rare = rare
           
        if self.rare: 
            self.value = 1.25
        else:
            self.value = 1.00
        
        self.color = "bronze"
        self.numb_edges = 1
        self.diameter = 22.5 #mm
        self.thickness = 3.15 #mm
        self.heads = True
    
        #destructor
    def __del__(self):
        print("Coin Spent!")
        
    def rust(self):
       self.color = "greenish" 
    
    def clean(self):
        self.clean = "bronze"
        
    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice
    
    
    
    
        
    
    

