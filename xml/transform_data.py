#!python3

import re
import os
import fnmatch
import xml.etree.ElementTree as ET

rex = re.compile(r"""(?P<title>TY
                       |A1
                       |T1
                       |Y1
                       |JO
                       |V1
                       |VL
                       |IS
                       |SP
                       |EP
                       |RP
                       |A2
                       |T2  
                       |CY
                       |PB
                       |KW
                       |KW
                       |KW
                       |KW
                       |KW
                       |KW
                       |U1
                       |T3
                       |Y2
                       |M1
                       |M2
                       |N1
                       |N2 
                       |SN
                       |T3
                       |ER
                     )
                     \s*-?\s*
                     (?P<value>.*)
                     """, re.VERBOSE)

''' Will look for the file in the directory and will do match if the file has .ris externsion.'''
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.ris'):

        # Set the root element as <I2E_Document> as requested.
        root = ET.Element('I2E_Document')
        root.text = '\n'

        
        # Open any filename as .ris extension.
        with open(file) as f:
            Article = ET.SubElement(root, 'Article')
            Article.text = '\n'   # A new line before the collected element.
            Article.tail = '\n\n' # An empty line after the Article element.          

            for line in f:
            
                # A new Article element will start after an empty line. 
                if line.isspace():
                    Article = ET.SubElement(root, 'Article')
                    Article.text = '\n'
                    Article.tail = '\n\n'
                            
                m = rex.search(line) # Process the wanted data, if the line contains it.               
                if m:
                    # Group the title as tag name.
                    title = m.group('title')
                     
                    # Set the title of the Article with UPPER chars. 
                    e = ET.SubElement(Article, title.upper())
                    e.text = m.group('value')
                    e.tail = '\n'
                            
            # Debbugging display
            ET.dump(root)

            tree = ET.ElementTree(root)
            tree.write('task.xml', encoding='utf-8', xml_declaration=True)
    
    else:
        print('****************** THIS FILE IS NOT TO BE USED! *****************')
