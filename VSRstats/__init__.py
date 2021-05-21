import numpy as np
import matplotlib.pyplot as plt
from peakutils import peak
from struct import unpack
import math
import os

import pyhrv.tools as tools

from VSRstats.time_domain import time_domain
from VSRstats.frequency_domain import frequency_domain
from VSRstats.nonlinear import nonlinear
from VSRstats.pars_rating import pars_rating

# Util for display peaks on signal
def showPeaks(signal):
    peaks = getPeaks(signal);
    fig = plt.figure(figsize=(30, 3))
    plt.scatter(x=peaks, y=[signal[j] for j in peaks],
                            color='red', marker = '*')
    plt.plot(signal)
    plt.show()

# func to get peaks of signal
def getPeaks(signal):
    return peak.indexes(signal, min_dist=56, thres=0.16)

# Read signal from file
def loadSignal(filepath):
    
    file = open(filepath, "rb").read()
    ufile = unpack('10000H', file)
    arr = np.array(ufile)
    
    return arr
    
class VSR:
    
    def __init__(self, data):

        if type(data) == list:
            self.data = data = np.array(data)
            
        if type(data) == np.ndarray:
            buffer = {}
            self.stats = (self.computeSignal(data) if
                           data.ndim == 1 else self.computeSignals(data))
        else:
            raise TypeError('Signal should be an np.ndarray')

    def __clearkeys(self, obj, keys):
        for k in keys:
            if type(obj) == dict:
                if not (k in obj.keys()):
                    [self.__clearkeys(obj[i], keys) for i in obj.keys()] 
                else:
                    del obj[k]

    def computeSignals(self, signals):
        return np.array([self.computeSignal(s) for s in signals])

    def computeSignal(self, signal):
        obj = {}
            
        obj['time_domain'] = time_domain(signal).stats
        
        obj['frequency_domain'] = frequency_domain(signal).stats
        self.__clearkeys(obj['frequency_domain'], ['freq', 'power', 'freq_i'])
        
        obj['nonlinear'] = nonlinear(signal).stats
        del obj['nonlinear']['poincare']['ellipse']
        del obj['nonlinear']['ACF']
        
        obj['pars_rating'] = pars_rating(signal).stats
        
        return obj
        
