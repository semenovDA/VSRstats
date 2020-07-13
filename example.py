import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from struct import unpack

from VSRstats import VSR # Custom class for stats of baevsky

import warnings
warnings.filterwarnings("ignore")

d_path = './data' # data path
s_path = './submission.xls' # submission path

submission = pd.read_excel(s_path)

df = pd.DataFrame()

def loadSignal(filepath):
    # Read signal from file
    file = open(filepath, "rb").read()
    ufile = unpack('10000H', file)
    return np.array(ufile) 

signals = []
for index, row in submission.iterrows():
    filepath = d_path + '/' + row['Имя файла']
    signals.append(loadSignal(filepath))
  
    if index % int(len(submission) / 10) == 0:
        print('[{}/{} processed]'.format(index, len(submission)))

stats = VSR(signals).stats        
print(len(stats))
output = pd.concat([pd.DataFrame(results), submission], axis=1)

# output.to_excel('./result.xls')


