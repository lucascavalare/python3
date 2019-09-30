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
    
print(sorted(set([sanitize(t) for t in James]))[0:3])
print(sorted(set([sanitize(t) for t in Julie]))[0:3])
print(sorted(set([sanitize(t) for t in Mikey]))[0:3])
print(sorted(set([sanitize(t) for t in Sarah]))[0:3])
