#!/usr/bin/python3

import sys
import xml.etree.ElementTree as ET

class spontalFilter():
    ''' Checks points from the Spontal corpus and outputs corrected file '''

    def __init__(self, inputFile, outputFile):
        self.tree = self.readFile(inputFile)
        self.root = self.tree.getroot()
        self.checkValues(self.root)
        self.writeFile(outputFile)

    def readFile(self, inputFile):
        ''' Try to init the ElementTree and read the specified XML file '''
        
        try:
            tree = ET.ElementTree()
            tree.parse(inputFile)
            return tree
        except:
            print("Error: cannot parse \"{}\", please specify a valid xml file".format(inputFile), file=sys.stderr)
            exit(-1)

    def checkValues(self, root):
        ''' Removes the points where FO_START and FO_END are not within the BOTTOM_HZ and TOP_HZ '''
        
        for point in root.findall('POINT'):
            if(float(point.find('F0_START').text) < float(point.find('BOTTOM_HZ').text) or
               float(point.find('F0_START').text) > float(point.find('TOP_HZ').text) or
               float(point.find('F0_END').text) < float(point.find('BOTTOM_HZ').text) or
               float(point.find('F0_END').text) > float(point.find('TOP_HZ').text)):             
                self.root.remove(point)

    def writeFile(self, outputFile):
        ''' Writes the checked corpus to a new XML file '''
        
        try:
            self.tree.write(outputFile)
        except:
            print("Error: cannot write to \"{}\", please writable output path".format(outputFile), file=sys.stderr)
            exit(-1)
        
def main(argv):
    if(len(argv) != 3):
        print("Usage: spontal_filter.py <input file> <output file>", file=sys.stderr)
        exit(-1)

    spontalFilter(argv[1], argv[2])    

if __name__ == "__main__":
    main(sys.argv)
