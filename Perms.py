# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 17:29:41 2019

@author: William Keilsohn
"""

'''
Calculate the number of possible permutations of a string/list.
'''

# I am just going to import another file. 
folderLoc = 'C://Users//kingw//Documents//Python Projects//Short Answers'
exec(open(folderLoc + '//factorial.py').read())

# Define functions
def perms(lst):
    length = len(lst)
    return factorial(length)

inList = list(input('Please enter a string/sequence of letters: '))

print('\n')
print('There are a total of ', str(perms(inList)), 'permutatuons that can be created.')