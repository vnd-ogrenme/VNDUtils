#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:57:29 2024

@author: gelenag
"""

from VNDUtils.Metrics import population_activity
from VNDUtils.Generators import poisson_spike_trains

import matplotlib.pyplot as plt
import numpy as np

# Parameters
duration = 1  # duration in seconds
dt = 0.1e-3  # time step in seconds
time_params = (0, duration, dt)
rates = [10,20,8]  # firing rate in Hz

rates = np.random.randint(15,80,10) + 10*np.random.randn(np.arange(0, duration, dt).size, 10)

# Generate spike train
spikes = poisson_spike_trains(rates, time_params)
spike_times = np.argwhere(spikes)

# Plotting
plt.figure()
plt.plot(spike_times[:,1], spike_times[:,0], '.', markersize=2, color='darkred')
plt.title('Poisson Spike Train')
plt.xlabel('Time (s)')
plt.ylabel('Spikes')
plt.show()

pa, pf = population_activity(spike_trains=spikes, dt=dt, time_window=100e-3, shift=5e-3, savgol_len=20)
plt.figure()
plt.plot(pa)
plt.plot(pf)
plt.legend(['original', 'smoothed'])
plt.ylabel('Firing Rate of Population (Hz)')
