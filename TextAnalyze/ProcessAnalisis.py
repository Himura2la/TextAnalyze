import numpy as np

POSes = np.load("..\\POS.npy")

with open("..\\POS.txt", 'w') as f:
    for (w, POS), n in POSes:
        f.write(str(n) + "\t" + POS + "\t" + w + '\r\n')