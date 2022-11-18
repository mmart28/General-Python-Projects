#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Madeline Martine

import re
import pyperclip

part_no = re.compile(r'(H)(\d)-(\d\d\d\d)') #identifying part numbers and grouping to extract supply line
no_units = re.compile(r'(#)(\d\d\d)') #identifying number of units and grouping to extract only the numerical value

#list containing supply line names
Area_Designation = ['Tango','Sierra','Victor','Foxtrot','Xray','Hotel','Delta','Romeo','India','Echo']

#using pyperclip to paste in the transcripts from clipboard
transcript = str(pyperclip.paste())

matchparts = part_no.findall(transcript) #store all part numbers from transcript in a list
matchunits = no_units.findall(transcript) #stoer all number of units from transcript in a list

#the for loop will take only the group from the part numbers containing the supply line identifier and store them in a list
designations = []
for i in range(len(matchparts)):
    designations.append(matchparts[i][1])

#the for loop will take only the group from the number of units containing the numerical value and store them in a list
units = []
for i in range(len(matchunits)):
    units.append(matchunits[i][1])
    
def supplyLineMatch(number):
    '''The function will take in the supply line identifier number and return the name from the list of names'''
    return Area_Designation[int(number)]

#the for loop will create a dictionary where the keys are the supply line identifier numbers and the values are the sum of units
counter = {}
for x,y in enumerate(designations):
    y = int(y)
    if y in counter.keys():
        counter[y] = int(counter[y]) + int(units[x]) #if the supply line appears more than once in the transcript the additional corresponding number of units is added to the total
    if y not in counter.keys(): #keys are created and the number of units corresponding to the supply line number is set as the value
        counter[y] = int(units[x])

#the for loop matches supply line identifiers to their name using the defined function and prints them (in order) along with the sum of units
for i in range(10):
    if i in counter.keys():
        name = supplyLineMatch(i)
        sum_units = counter[i]
        print('Supply Line '+name+'-----> '+str(sum_units)+'\n')


# In[ ]:




