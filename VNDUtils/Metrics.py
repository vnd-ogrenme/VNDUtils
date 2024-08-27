#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:57:21 2024

@author: gelenag
"""

import numpy as np
from scipy.signal import savgol_filter

def population_activity(spike_trains, dt, time_window, shift, savgol_len=5):
    """
    Calculate population activity.

    Parameters:
    spike_trains (list of lists or 2D numpy array): Spike trains from multiple neurons in a population.
    bin_width (float): Width of the time bin for the histogram.
    N (int): Number of neurons in the population.

    Returns:
    numpy array: Population activity values.
    """

    window_len = int(time_window / dt)
    shift_len = int(shift / dt)
    rates = []
    stop = int(spike_trains.shape[1]-window_len)
    shifts = np.arange(0, stop, shift_len)
    for i in shifts:
        windowed_spikes = spike_trains[:,i:i+window_len]
        rates.append(np.sum(windowed_spikes)/time_window/spike_trains.shape[0])
    
    rates = np.array(rates)
    return rates, savgol_filter(rates, savgol_len, 3)


def synchronization(x):
    # D. Hansel, G. Mato, C. Meunier, L. Neltner
    # On Numerical Simulations of Integrate-and-Fire Neural Networks. 
    # https://doi.org/10.1162/089976698300017845

    raise NotImplementedError()