# VSRstats
Sphygmogram VSR compute util

Install next packages: `pip install pyhrv numpy pandas peakutils matplotlib`  
Define required libraries:
```python
from struct import unpack
import numpy as np
import VSR
```

Define loading signal function:
```python
def loadSignal(filepath):
    
    file = open(filepath, "rb").read()
    ufile = unpack('10000H', file)
    arr = np.array(ufile)
    
    return arr
```

Usage for 1 signal:
```python
filepath = './data/d0001' # path to signal
signal = loadSignal(filepath)
stats = VSR(signal).stats
print(stats)
```
> {'nni_counter': 125, 'nni_mean': 79.92, 'nni_min': 66.0, 'nni_max': 88.0, 'hr_mean': 752.1562922784314, 'hr_min': 681.8181818181819, 'hr_max': 909.0909090909091, 'hr_std': 33.27091439584001, 'nni_diff_mean': 2.5161290322580645, 'nni_diff_min': 0, 'nni_diff_max': 14, 'sdnn': 3.4139183806408457, 'sdnn_index': nan, 'sdann': nan, 'rmssd': 3.4734012335220155, 'sdsd': 2.404209962584576, 'nn50': 0, 'pnn50': 0.0, 'nn20': 0, 'pnn20': 0.0, 'tinn_n': 62.5, 'tinn_m': 85.9375, 'tinn': 23.4375, 'tri_index': 1.6025641025641026}

Usage example for signals:
```python
filepathes = ['./data/d0001', './data/d0002', './data/d0003'] # Signals
signals = np.array([loadSignal(f) for f in filepathes])
stats = VSR(signals).stats
print(len(stats))
```
> 3
