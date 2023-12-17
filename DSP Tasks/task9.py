import tkinter as tk
import numpy as np 
import signal_plot 

def determine_window_type(stop_band):
    int(stop_band)
    window_type = {
        21: 'rectangular',
        44: 'hanning',
        53: 'hamming',
        74: 'blackman'
    }
    print(window_type.items)
    print(f'filter specifications keys {window_type.keys}')
    for band in window_type.keys:
        if stop_band >= band:
            return window_type[band]

def determine_filter_type(filter_type_from_file):
    return filter_type_from_file

def get_N(norm_fc, window_type):
    def handle_N(N):
        if (N % 2 == 0):
            return np.ceil(N) + 1
        else:
            return np.ceil(N) 
    if(window_type == 'rectangular'):
        return handle_N(0.9 * norm_fc) 
    elif window_type == 'hanning':
        return handle_N(3.1 * norm_fc)
    elif window_type == 'hamming':
        return handle_N(3.3 * norm_fc)
    elif window_type == 'blackman':
        return handle_N(5.5 * norm_fc)
filter_specs = signal_plot.read_filter_specifications()
print(filter_specs)
