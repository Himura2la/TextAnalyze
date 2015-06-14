import nltk
import numpy as np
import itertools
from nltk.tokenize import *
from nltk.probability import FreqDist
from collections import Counter
from multiprocessing import Pool

def POSe(sent): 
    return nltk.pos_tag(word_tokenize(sent))

if __name__ == '__main__':
    print("Reading started")

    with open("..\\China_39_s_Military_UAV_Industry_14_June_2013.txt", "r") as f:
        raw = f.read()
    
    print("Raw symbols: %d" % len(raw))

    #tokens = word_tokenize(raw)
    #text = nltk.Text(tokens)
    sents = sent_tokenize(raw)#[80:90]

    print("Sentencies: %d" % len(sents))

    pool = Pool(8)
    print("Pool processing started!")
    map = pool.map(POSe, sents)

    print("Map size: %d" % len(map))

    POSed = [i for i in itertools.chain.from_iterable(map)] # Connect sentensies
    POSed = sorted([(w.lower(), p) for w, p in POSed])      # To Lower
    
    print("Lemmatization...")
    wnl = nltk.WordNetLemmatizer()
    POSed = sorted([(wnl.lemmatize(w), p) for w, p in POSed])      # Lemmatization
    
    print("Counting...")
    POSed = Counter(POSed).most_common()
    print("POSed size: %d" % len(POSed))

    print("Saving...")

    np.save("..\\POS.npy", np.array(POSed))
    with open("..\\POS.txt", 'w') as f:
        for (w, POS), n in POSed:
            f.write(str(n) + "\t" + POS + "\t" + w + '\r\n')