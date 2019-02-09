#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Feb  3 17:21:59 2019

@author: rr


password generator

simple algorithm that creates pseudo-random passwords
in groups of *consonant-vowel-consonant-digit*
where one of the alpha characters at random will be capitalised

10 passwords are generated, separated by carriage returns, and written to a text file

EXAMPLES

mIr0duP3Dud8Hyk5
Syv0Wuv8Zyq0jOs2
etc.

"""


import random

def generatepassword(number_groups_in_each_password):

    myfile = open('passwordoutput.txt', 'a+')
    
    lowerconsonantstring = 'bcdfghjklmnpqrstvwxz'
    upperconsonantstring = 'BCDFGHJKLMNPQRSTVWXZ'

    lowervowelstring = 'aeiouy'
    uppervowelstring = 'AEIOUY'

    password = ''

    for i in range (0,number_groups_in_each_password):
    
        capitalisationselector = random.randint(0,2)
        if capitalisationselector == 0:
            stringlist = [upperconsonantstring, lowervowelstring, lowerconsonantstring]
        if capitalisationselector == 1:
            stringlist = [lowerconsonantstring, uppervowelstring, lowerconsonantstring]
        if capitalisationselector == 2:
            stringlist = [lowerconsonantstring, lowervowelstring, upperconsonantstring]
                      
        for j in range (0,3):
    
            teststring = stringlist[j]
            randomindex = random.randint(0,len(teststring)-1)
            randomcharacter = teststring[randomindex]
            password = password + randomcharacter

        password = password + str(random.randint(0,9))

    print (password)
    myfile.write(password + '\n')
    myfile.close()
    
# call the function in a loop - if you need 10 pwds call it 10 times

# the integer passed to the function is the number of groups in each password

for a in range(0,10):
    generatepassword(4)
    

    