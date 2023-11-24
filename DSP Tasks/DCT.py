import math
from scipy.fftpack import dct
import numpy as np
import signal_plot
import comparesignal2
import matplotlib.pyplot as plt
import tkinter as tk

from tkinter import messagebox
class DctTransfrom:
    def __init__(self):
        print('DCT Transform started')
        
        self.root = tk.Tk()
        self.root.geometry( '700x500' )
        self.radio_buttons_frame = tk.Frame(self.root)
        self.selected_event = tk.StringVar(self.radio_buttons_frame, '')
        self.dct_radio_button = tk.Radiobutton(self.radio_buttons_frame, text='DCT', variable=self.selected_event, value='dct', command=self.on_radio_change)
        self.dct_radio_button.pack(side='left')
        self.remove_dc_radio = tk.Radiobutton(self.radio_buttons_frame, text='remove DC component', variable=self.selected_event, value='dc', command=self.on_radio_change)
        self.remove_dc_radio.pack(side='left')
        self.pick_signal_button = tk.Button(self.root, text='Pick a signal', command=self.on_signal_picked)
        self.radio_buttons_frame.pack( anchor='center')
        self.coeffitient_frame = tk.Frame(self.root)
        self.coeffitients_entry = tk.Entry(self.coeffitient_frame)
        self.coeffitients_entry.pack(side='left')
        self.save_button = tk.Button(self.coeffitient_frame, text='Save Coeffitients', command=self.save_coeffitients)
        self.save_button.pack(side='left')
        self.dct_radio_button.select()
        self.pick_signal_button.pack()
        self.coeffitient_frame.pack(anchor='sw')
        self.root.mainloop()

    def on_radio_change(self):
        if hasattr(self.root, 'canvas_widget'):
            self.root.canvas_widget.destroy()

        if  self.selected_event.get() == 'dc':
            self.coeffitient_frame.pack_forget()
            self.coeffitients_entry.pack_forget()
            self.save_button.pack_forget()
        elif self.selected_event.get() == 'dct':
            self.coeffitient_frame.pack(anchor='sw')
            self.coeffitients_entry.pack(side='left')
            self.save_button.pack(side='left')
    def on_signal_picked(self):
        if self.selected_event.get() == 'dct':
            print('radio button value:', self.selected_event.get())
            print(self.selected_event.get())
            self.dct = self.dct_transform()
        elif  self.selected_event.get() == 'dc':
            print('radio button value:', self.selected_event.get())
            self.coeffitient_frame.pack_forget()
            self.coeffitients_entry.pack_forget()
            self.save_button.pack_forget()
            print(self.selected_event.get())
            self.remove_dc_component()
    def save_coeffitients(self):
        m = int(self.coeffitients_entry.get())
        coeff = self.dct[:m]
        with open('saved_coeffitients.txt', 'a') as file:
            file.write('\n0 \n')
            file.write('0 \n')
            file.write(f'{m}\n')
            for i in range(m):
                file.write(f'{i} {coeff[i]}\n')
            file.write('-------------------------------------------------\n')
    def dct_transform(self):
        _, signal, _ = signal_plot.open_file()
        N = len(signal)
        y = []
        print(signal)
        signal = [round(i, 5) for i in signal]
        for k in range(N):
            # Cummulative from n = 0 -> N-1 (Correction: Change 2*N to 2*n)
            cumm_sum = 0.0
            for n in range(N):
                radian_angle = (np.pi/(4*N)) * (2*n - 1) * (2*k - 1)
                # Sum(x(n) * cos(pi/N (2n+1)k))
                cumm_sum += signal[n] * math.cos(radian_angle)
            y_k = np.sqrt(2/N) * cumm_sum
            y.append(y_k)
        test_result = comparesignal2.SignalSamplesAreEqual('DCT_output.txt', y)
        messagebox.showinfo('Test case Result', str(test_result))
        signal_plot.plot_original_and_affected(signal, y, 'Original Signal', 'DCT')
        return y
    def remove_dc_component(self):
        _, dc, _ = signal_plot.open_file()
        N = len(dc)
        y = []
        print(dc)
        # Cummulative from n = 0 -> N-1 (Correction: Change 2*N to 2*n)            
        for n in range(N):
            removed_dc = dc - np.mean(dc)
        test_result = comparesignal2.SignalSamplesAreEqual('DC_component_output.txt', list(removed_dc))
        messagebox.showinfo('Test case Result', test_result)
        signal_plot.plot_original_and_affected(dc, removed_dc, 'Original Signal', 'DC')
        return list(removed_dc)

