#!/usr/bin/python3

import sys
import json
from collections import namedtuple

class bloodDie():
    ''' Checks simularity between words blood and die in several languages and prints where same word is used for both words '''

    def __init__(self, jsonFile):
        self.json = self.decodeJSON(jsonFile)
        self.tuples = self.makeTuples(self.json)

    def decodeJSON(self, jsonFile):
        ''' Opens and decodes the JSON file '''
        
        try:
            infile = open(jsonFile, "r")
            return json.load(infile)
        except:
            print("Error: cannot open \"{}\", please specify a valid JSON file".format(argv[1]), file=sys.stderr)
            exit(-1)

    def makeTuples(self, json):
        ''' Converts the JSON to a list with namedtuples '''
        
        langBloodDie = namedtuple('langBloodDie', 'langName, langClass, langBloodWords, langDieWords')
        bloodDie = []
        for item in json:
            bloodDie.append(langBloodDie(item[0],
                                         item[1],
                                         [x.strip() for x in item[2].split(',')],
                                         [x.strip() for x in item[3].split(',')]))
        return bloodDie

    def sameWords(self, tuples):
        ''' Returns a the language name and class that has words that are used as both a word for blood and die '''
        
        return [(e.langName, e.langClass) for e in tuples if any(x in e.langBloodWords for x in e.langDieWords)]
    
    def __str__(self):
        ''' Print out a nice list with the languages that have the same words for blood and die '''
        
        output = '\nLanguages with the same words for Blood and Die\n'
        output += '==============================================='
        for langName, langClass in self.sameWords(self.tuples):
            output += "\n\nLanguage: {}\nLanguage Classification: {}".format(langName, langClass)
        return output
            

def main(argv):
    if(len(argv) != 2):
        print("Usage: blood-die.py <path to json file>", file=sys.stderr)
        exit(-1)

    print(bloodDie(argv[1]))

if __name__ == "__main__":
    main(sys.argv)
