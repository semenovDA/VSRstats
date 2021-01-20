import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from peakutils import peak
from struct import unpack
import math
import os
from pyhrv import tools

import pyhrv.frequency_domain as fd

class frequency_domain:
    
    def __init__(self, data):

        self.bands = {'ulf': (0.0, 0.015),
                     'vlf':(0.015, 0.04),
                     'lf':(0.04, 0.15),
                     'hf':(0.15, 0.4) }

        if type(data) == list:
            data = np.array(data)
            
        if type(data) == np.ndarray:

            self.stats = (self._computeSignal(data) if
                           data.ndim == 1 else self._computeSignals(data))
            
        else:
            raise TypeError('Signal should be an np.ndarray')

    def _welch_psd(self, nni, peaks):
        params, freq, power = fd.welch_psd(nni=nni, fbands=self.bands,
                                  rpeaks=peaks, show=False, mode='dev')
        
        _, freq_i = fd._compute_parameters('fft', freq, power, self.bands)
        
        return {'params': dict(params.__dict__), 'freq': freq,
                'power': power / 10**6, 'freq_i': freq_i}
    
    def _lomb_psd():
        pass
    
    def _ar_psd():
        pass

    def _computeSignals(self, signals):
        return np.array([self.computeSignal(s) for s in signals])

    def _computeSignal(self, signal):
        obj = {}

        # Best min_dist & thres for sphygmogram signal
        peaks = peak.indexes(signal, min_dist=56, thres=0.16)
        
        # Ignore un normal signls (with no peaks)
        if(len(peaks) == 0): return obj
            
        nn = tools.nn_intervals(peaks)
        
        # Ignore un normal signls (with no NN)
        if(len(nn) == 0): return obj

        obj['welch'] = self._welch_psd(nn, peaks)
          
        return obj

        
