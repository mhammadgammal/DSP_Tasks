import numpy as np
import tkinter as tk
from tkinter import ttk
import signal_plot
import Shift_Fold_Signal as sh
import DerivativeSignal as dv
import math
import comparesignal2 as cmpre
import ConvTest
import matplotlib.pyplot as plt
from tkinter import messagebox
class TimeDomain:
    def __init__(self):
        print('Time Domain Class Started')

        self.root = tk.Tk()
        self.root.geometry( '700x500' )
        self.root.title('Time Domain')
        items = ['Smoothing[Moving Average Filter]', 'Sgarpenning', 'Shifting', 'Folding and Shifting Folding', 'Remove DC component', 'convolve']
        self.combobox = ttk.Combobox(self.root, values=items)
        self.combobox.pack(fill='x')
        self.combobox.set(items[0])
        self.combobox.bind('<<ComboboxSelected>>', self.on_combo_selected)

        self.open_file_button = tk.Button(self.root, text='pick singal', command=self.on_file_button_pressed)
        self.open_file_button.pack(anchor='center')
        self.window_size_frame = tk.Frame(self.root)
        self.window_size_label = tk.Label(self.window_size_frame, text='Window Size')
        self.window_size_entry = tk.Entry(self.window_size_frame)
        self.window_size_label.pack(side='left')
        self.window_size_entry.pack(side='left')
        self.window_size_frame.pack(fill='x')
        self.root.mainloop()

    def on_combo_selected(self, event):
        print(self.combobox.get())
        cmb_val = self.combobox.get()
        if cmb_val == 'Sgarpenning':
            self.open_file_button.config(text='Sharpen the signal')
            self.window_size_frame.pack_forget()
        elif cmb_val == 'Shifting':
            self.window_size_frame.pack(fill='x')
            self.window_size_label.config(text='shifing ammount')
        elif cmb_val == 'Folding and Shifting Folding':
            pass
        elif cmb_val == 'Remove DC component':
            self.open_file_button.config(text='Remove')
        elif cmb_val == 'convolve':
            self.open_file_button.config(text='Convolve')
    
    def on_file_button_pressed(self):
        cmb_val = self.combobox.get()
        if cmb_val == 'Smoothing[Moving Average Filter]':
            indecies , signal, _ = signal_plot.open_file()
            self.smmoth_signal(signal, int(self.window_size_entry.get()))
        elif cmb_val == 'Sgarpenning':
            self.sharpen()
        elif cmb_val == 'Shifting':
            indecies , signal, _ = signal_plot.open_file()
            self.shifting(indecies, signal, int(self.window_size_entry.get()))
        elif cmb_val == 'Folding and Shifting Folding':
            indecies , signal, _ = signal_plot.open_file()
            folded_signal = self.fold_signal(indecies, signal)
            if self.window_size_entry.get() != '' and int(self.window_size_entry.get()) > 0:
                self.shift_folded_signal(indecies, folded_signal, int(self.window_size_entry.get()))
        elif cmb_val == 'Remove DC component':
            _ , signal, _ = signal_plot.open_file()
            self.remove_dc(signal)
        elif cmb_val == 'convolve':
            _ , signal, _ = signal_plot.open_file()
            self.convolve()

    def smmoth_signal(self, signal, kernel):
        smoothed_signal = np.zeros_like(signal)

        for n in range(len(signal)):
            tmp = signal[n:kernel]
            avg_index = (len(tmp) - 1) + 1
            smoothed_signal[avg_index] = sum(tmp)/kernel

        # signal_plot.plot_original_and_affected(self.root, signal, smoothed_signal, 'original signal', 'Smoothed Signal')
        return smoothed_signal
    
    def shifting(self,indecies, signal, k):
        # y = x[n] - k
        # k positive --> delay
        # k negative --> Advance
        print(signal)
        shifted_signal = []
        for i in range(len(signal)):
            
            shifted_signal.append(signal[i - k])
        print(shifted_signal)
        return shifted_signal

    def fold_signal(self,indecies, signal):
        signal.reverse()
        sh.Shift_Fold_Signal('Task 6\TestCases\Shifting and Folding\Output_fold.txt', indecies, signal)
        return signal
    
    def shift_folded_signal(self, indecies, signal, k):
        shifted_folded_signal=[]
        for i in range(len(indecies)):
            shifted_folded_signal.append(indecies[i] + k)
        
        if k == 500:
            sh.Shift_Fold_Signal('Task 6\TestCases\Shifting and Folding\Output_ShifFoldedby500.txt', shifted_folded_signal, signal)
        elif k == -500:
            sh.Shift_Fold_Signal('Task 6\TestCases\Shifting and Folding\Output_ShiftFoldedby-500.txt', shifted_folded_signal, signal)
    
    def sharpen(self):
        dv.DerivativeSignal(self.root)

    def remove_dc(self, signal):
        
        dft_signal = self.calculate_dft(signal)
        dft_signal[0] = 0
        result_signal = self.calculate_idft(dft_signal)
        print(f'result_signal: {result_signal}')
        x = cmpre.SignalSamplesAreEqual('DSP Tasks\DC_component_output.txt', result_signal)
        messagebox.showinfo('Test case Result', x)
        return result_signal
    
    def calculate_dft(self, signal_values):
        out_signal = []
        for k in range(len(signal_values)):
            harmonic = self.calculate_harmonic(k, signal_values, 'dft')
            out_signal.append(harmonic)
        return out_signal

    def calculate_idft(self, signal_values):
        out_signal = []
        for k in range(len(signal_values)):
            harmonic = self.calculate_harmonic(k, signal_values, 'idft')
            out_signal.append(round(harmonic.real, 3))
        return out_signal

    def calculate_harmonic(self, k, signal_values, signal_type):
        
        N = len(signal_values)
        summ = 0
        for n in range(N):
            summ += self.calculate_one_element(n, k, signal_values, signal_type)
        if signal_type == 'idft':
            return summ * (1 / N)
        return summ
    
    def calculate_one_element(self, n, k, values, signal_type):
            if values[n] == 0:
                return 0
            rtn = values[n] * self.calculate_exp(n, k, len(values), signal_type)
            if signal_type == 'idft':
                rtn = (rtn.real + (rtn.imag * 1j))
            return rtn
    
    def calculate_exp(self,n, k , N, signal_type):
        pow = (1j * 2 * n * k) / N
        if pow.imag == 0:
            return 1 + 0j

        sin_value = float(math.sin(math.pi * abs(pow.imag)))
        cos_value = float(math.cos(math.pi * abs(pow.imag)))

        if signal_type == 'dft':
            sin_value *= -1j
        else:
            sin_value *= 1j
        e = cos_value  + sin_value

        return e

    def convolve(self):
        _, _, len_signal_1, indexes_1, signal_1 = signal_plot.read_signal_from_file('Task 6\TestCases\Convolution\Input_conv_Sig1.txt')
        _, _, len_signal_2, indexes_2, signal_2 = signal_plot.read_signal_from_file('Task 6\TestCases\Convolution\Input_conv_Sig2.txt')
        # Length of the output signal
        len_output_signal = len_signal_1 + len_signal_2 - 1
        output_signal = []
        for i in range(len_output_signal):
            output_signal.append(0)

        for n in range(len_output_signal):
            for k in range(max(0, n - len_signal_2 + 1), min(len_signal_1, n + 1)):
                output_signal[n] += signal_1[k] * signal_2[n - k]

        output_indexes = indexes_1 + indexes_2
        x = list(set(output_indexes))
        x.sort()
        ConvTest.ConvTest(x, output_signal)
        return x, output_signal


