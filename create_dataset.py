# -*- coding: utf-8 -*-
"""
Created on Sun May  1 08:22:04 2016

@author: rahulkumar
"""
import re

def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()



dataset = list(open("/Users/rahulkumar/Desktop/QA_set.txt", "r").readlines())
dataset = [s.strip() for s in dataset]
dataset = [clean_str(sent) for sent in dataset]
x_text = [s.split(" ") for s in dataset]
dataset = [s[2:] for s in x_text]
dataset_clean = []
for s in dataset:
    dataset_clean.append( [' '.join(ww for ww in s)])
 


        
for s in dataset_clean:
    for w in s:
        if 'who' in w:
            f = open('/Users/rahulkumar/Desktop/qa_data.who','a').write(w + '\n')
        if 'what' in w:
            f = open('/Users/rahulkumar/Desktop/qa_data.what','a').write(w + '\n')
        if 'when' in w:
            f = open('/Users/rahulkumar/Desktop/qa_data.when','a').write(w + '\n')
        if 'affirmation' in w:
            f = open('/Users/rahulkumar/Desktop/qa_data.affirmation','a').write(w + '\n')
            
    