# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 16:45:51 2019

@author: William Keilsohn
"""

'''
Calculate the total number of possiblities avable to select from a given population.
'''

# First here is the statistical formula:
# P(n,r) = n!/(n-r)!

## Now there are no packages I want to use, but I do have another script I want to import:
folderLoc = 'C://Users//kingw//Documents//Python Projects//Short Answers'
exec(open(folderLoc + '//factorial.py').read())

## Define the function(s):
def combs(num1, num2):
    top = factorial(num1)
    num3 = factorial(num1 - num2)
    bottom = factorial(num2) * num3
    val = top // bottom # Statistically speaking, this should be a whole number. 
    return val

population = int(input('What is the total size of the population?: '))
print('\n')
sample = int(input('How many are you sampling at a time?: ' ))
print('\n')
print('There are a total of: ', str(combs(population, sample)))