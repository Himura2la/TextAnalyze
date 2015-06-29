from pattern.en import *
import numpy as np
import sys

sents = np.load("..\\sents.npy")
sents = list(sents)


complexity = []
i=0
for sent in sents:
    complexity.append(0)
    s = parsetree(sent, relations=True)
    for sentence in s:
        for chunk in sentence.chunks:
            #print [w.string for w in chunk.words], "-", chunk.relations
            try:
                for ch in chunk.relations:
                    if ch[0] > complexity[i]:
                        complexity[i] = ch[0]
            except: pass
    sys.stdout.write("\n\n[%d]\n" % complexity[i])
    print(sent)
    i+=1
