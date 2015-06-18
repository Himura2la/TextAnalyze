import nltk
import numpy as np
import itertools
from nltk.tokenize import *
from nltk.probability import FreqDist
from collections import Counter
from multiprocessing import Pool
import os
from nltk.parse.dependencygraph import DependencyGraph

if __name__ == '__main__':
    print("Reading started")

    with open("..\\China_39_s_Military_UAV_Industry_14_June_2013.txt", "r") as f:
        raw = f.read()
    print("Raw symbols: %d" % len(raw))

    sents = sent_tokenize(raw)[20:21]
    print("Sentencies: %d" % len(sents))

    os.environ["MALT_PARSER"] = "C:\\Python34\\maltparser-1.8.1"
    parser = nltk.parse.malt.MaltParser(working_dir="C:\\Python34\\maltparser-1.8.1", 
                                        mco="engmalt.linear-1.7")


    for sent in sents:
        sent = word_tokenize(sent)
        trees = parser.parse(sent, verbose=True)
        for t in trees:
            tr = t.tree()
            tr.pprint()