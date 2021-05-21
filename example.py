from struct import unpack
import numpy as np
from VSRstats import VSR

import warnings
warnings.filterwarnings("ignore")

def loadSignal(filepath):
    file = open(filepath, "rb").read()
    ufile = unpack('10000H', file)
    arr = np.array(ufile)
    return arr

# Compute signal
filepath = './data/d338_f_90' # path to signal
signal = loadSignal(filepath)
stats = VSR(signal).stats
print(stats)

# Display peaks
from VSRstats import showPeaks
showPeaks(signal)

# Compute signals
filepathes = ['./data/d338_f_90', './data/d418_f_270', './data/d419_f_280'] # Signals
signals = np.array([loadSignal(f) for f in filepathes])
vsr = VSR(signals)
print(len(vsr.stats))
