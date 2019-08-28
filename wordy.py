from argparse import ArgumentParser
from collections import Counter
import os, re

dirpath = os.path.realpath(__file__)

def removing_stop_words(raw_list):
    '''Get the stop words list and return a cleaned list'''
    clean_list = []
    try:
        #Retrieving stop words from file
        stop_word_list = re.findall(r'\w+', open(dirpath + "/stop_words_list.txt").read().lower())
        #Make a clean list 
        clean_list = [value for value in raw_list if value not in stop_word_list]
    except OSError:
         print('No stop words defined. Define stop_words_list.txt file in this same folder')
         clean_list = raw_list
    return clean_list;

def get_minimum_word_count():
    '''Retrieve the minimum count of words'''
    minimum = 1
    try:
        #Retrieving stop words from file
        rd_file = open(dirpath + "/minimum.txt", 'r')
        value = rd_file.readline()
        minimum = int(value) if str.isdigit(value) else 1
        rd_file.close()
    except OSError:
         print('No minimum word count defined. Define minimum.txt file in this same folder')
         minimum = 1
    return minimum;

def main():
    #Defining filename as a required parameter for the script
    parser = ArgumentParser()
    parser.add_argument('filename', help='Text file to process')
    #Requesting the appropiate argument
    args = parser.parse_args()

    try:
        #Matching only alphanumeric characters
        wordfile = re.findall(r'\w+', open(args.filename).read().lower())
        #Creating a Counter Object for counting the elements in the clean list
        c = Counter()
        #Get the minimun word count
        min_value = get_minimum_word_count()
        for word in removing_stop_words(wordfile):
            c[word] += 1
        #Convert Counter to a simple Dict
        report = dict(c)
        #Comprehension for printing out required values
        print({k:v for (k,v) in sorted(report.items(), reverse=True) if v >= min_value})

    except OSError as e:
        print('Wordy Severe Error: ' + str(e))

main()
