#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:50:51 2024

@author: gelenag
"""

import numpy as np


def poisson_spike_trains(firing_rates, time_params):
   
    t_start, t_stop, dt = time_params
    
    time_array = np.arange(t_start, t_stop, dt)
    firing_rates = np.array(firing_rates)
    
    if firing_rates.ndim == 1:
        prob = np.random.uniform(0, 1, (time_array.size, len(firing_rates)))
    else:
        prob = np.random.uniform(0, 1, (time_array.size, firing_rates.shape[1]))
        
    spikes = np.less(prob, firing_rates*dt)
    return spikes.T