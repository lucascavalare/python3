#!/usr/bin/env python3

''' Function to transform the data in the list when finding chars to make the sorted method difficult to work. 
    The function processes the string to replace any dashes or colons found and returns the sanitized string.'''
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)


''' Open each of the data files in turn, read the line of data from the file, 
    and create a list from the line of data.''' 
with open('james.txt') as James:        # Open the file.
    data1 = James.readline()            # Read the line of data.
    James = data1.strip().split(',')    # Convert the data to a list.

with open('julie.txt') as Julie:
    data2 = Julie.readline()
    Julie = data2.strip().split(',')

with open('mikey.txt') as Mikey:
    data3 = Mikey.readline()
    Mikey = data3.strip().split(',')

with open('sarah.txt') as Sarah:
    data4 = Sarah.readline()
    Sarah = data4.strip().split(',')
    
''' Replaces each of the data items within unordered and non-uniform data with the sorted, sanitized copy.'''
James = sorted([sanitize(t) for t in James]))
Julie = sorted([sanitize(t) for t in Julie]))
Mikey = sorted([sanitize(t) for t in Mikey]))
Sarah = sorted([sanitize(t) for t in Sarah]))

''' Create new lists for each Athlete, and then populate it with the unique items found in each existing list.'''
    
unique_James = []
    for each_t in James:                   # Iterate over the existing data. 
        if each_t not in unique_James:     # If the data item ISN'T already in the new list.
            unique_James.append(each_t)    # Append the unique data item to new list. 
print(unique_James[0:3])                   # Slice the first three data items from the list and display them.  

unique_Julie = []
    for each_t in Julie:                   
        if each_t not in unique_Julie:
            unique_Julie.append(each_t)
print(unique_Julie[0:3]) 

unique_Mikey = []
    for each_t in Mikey:                    
        if each_t not in unique_Mikey:
            unique_Mikey.append(each_t)
print(unique_Mikey[0:3]) 

unique_Sarah = []
    for each_t in Sarah:                    
        if each_t not in unique_Sarah:
            unique_Sarah.append(each_t)
print(unique_Sarah[0:3]) 

