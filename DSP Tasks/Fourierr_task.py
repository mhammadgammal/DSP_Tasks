import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import numpy as np
import math
import matplotlib.pyplot as plt
import signal_plot
class FourierTransform:
    def __init__(self):
        self.signal_phase = None
        self.signal_ampl = None
        self.root = tk.Tk()
        self.root.geometry('800x500')
        self.signal_type = ''
        self.main_frame = tk.Frame(self.root)
        self.choose_signal_file = tk.Button(self.main_frame, text='Choose signal file', command=self.read_signal)
        self.choose_signal_file.pack()
        self.signal_type_label = tk.Label(self.main_frame, text=self.signal_type)
        self.signal_type_label.pack()
        self.frequency_label = tk.Label(self.main_frame, text='Enter Sampling Frequency')
        self.frequency_label.pack()
        self.frequency_entry = tk.Entry(self.main_frame)
        self.frequency_entry.pack()
        self.amplitude_label = tk.Label(self.main_frame, text='Enter Amplitude')
        self.amplitude_label.pack()
        self.amplitude_entry = tk.Entry(self.main_frame)
        self.amplitude_entry.pack()
        self.phase_label = tk.Label(self.main_frame, text='Enter phase')
        self.phase_label.pack()
        self.phase_entry = tk.Entry(self.main_frame)
        self.phase_entry.pack()
        self.dft_button = tk.Button(self.main_frame, text='DFT', command=self.calc)
        self.dft_button.pack()
        self.idft_button = tk.Button(self.main_frame, text='idft', command=self.calc)
        self.idft_button.pack()
        self.main_frame.pack(fill='x')
        self.root.mainloop()

    def read_signal(self):
        self.signal_one_type, self.signal_type, self.num_samples_one, self.signal_ampl, self.signal_phase = (
        signal_plot.read_signal())
    def save_file_in_polar(sefl,ampl, phase):
        with open('polar_form.txt', 'w') as file:
            file.write('0 \n')
            file.write('1 \n')
            file.write(f'{len(ampl)}\n')
            for i in range(len(ampl)):
                file.write(f'{ampl[i]} {phase[i]}\n')


    def save_file(self,data):
        with open('signal_to_recontruct.txt', 'w') as file:
            file.write('0 \n')
            file.write('0 \n')
            file.write(f'{len(data)}\n')
            for i in range(len(data)):
                file.write(f'{i} {data[i]}\n')

    def calc(self):
        if self.signal_type == 0:
            self.sampling_freq_value = float(self.frequency_entry.get())
            self.signal_type = 'dft'
            values = self.signal_phase
            print(f" values {values}")
            fundamentel_freq = self.calculate_fundamentel_freq(self.sampling_freq_value,
                                                                                       len(values))
            data = self.calculate_dft(values)
            print('data:',data)
            x = self.calculate_amplitude(data)
            y = self.calculate_phase_shift(data)
            print(x)
            print(y)
            self.save_file(data)
            self.save_file_in_polar(x, y)
            self.edit_ampl = self.amplitude_entry.get()
            self.edit_theta = self.phase_entry.get()
            if self.edit_ampl and self.edit_theta:
                for i in range(len(x)):
                    x[i] *= int(self.edit_ampl)
                for i in range(len(y)):
                    y[i] *= int(self.edit_theta)
            elif self.edit_theta:
                for i in range(len(y)):
                    y[i] *= int(self.edit_theta)
            elif self.edit_ampl:
                for i in range(len(x)):
                    x[i] *= int(self.edit_ampl)

            self.plot_freq_domain(fundamentel_freq, x, y)
        else:
            self.signal_type = 'idft'
            values = self.convert_from_polar_form(self.signal_ampl, self.signal_phase)
            print(values)
            data = self.calculate_idft(values)
            self.plot_time_domain(data)
    def reconstruct_signal(self):
        signal = open("signal_to_recontruct.txt")
        int(signal.readline().strip())
        int(signal.readline().strip())
        num_samples = int(signal.readline().strip())
        signal_values = []
        for i in range(int(num_samples)):
            signal_values.append(complex(signal.readline().strip().split()[1]))

        x = self.calculate_dft(signal_values)
        self.plot_time_domain(x)
    def on_dft_click(self):
        self.calculate_dft(self.signal_phase)
    def on_idft_click(self):
        self.calculate_idft(self.signal_phase)
    @staticmethod
    def calculate_dft( signal_values):
        out_signal = []
        for k in range(len(signal_values)):
            harmonic = FourierTransform.calculate_harmonic(k, signal_values, 'dft')
            out_signal.append(harmonic)
        return out_signal
    @staticmethod
    def calculate_idft( signal_values):
        out_signal = []
        for k in range(len(signal_values)):
            harmonic = FourierTransform.calculate_harmonic(k, signal_values, 'idft')
            out_signal.append(int(harmonic.real))
        return out_signal
    @staticmethod
    def calculate_harmonic(k, signal_values, signal_type):
        
        N = len(signal_values)
        summ = 0
        for n in range(N):
            summ += FourierTransform.calculate_one_element(n, k, signal_values, signal_type)
        if signal_type == 'idft':
            return summ * (1 / N)
        return summ
    @staticmethod
    def calculate_one_element(n, k, values, signal_type):
        if values[n] == 0:
            return 0
        rtn = values[n] * FourierTransform.calculate_exp(n, k, len(values), signal_type)
        if signal_type == 'idft':
            rtn = (rtn.real.__round__() + (rtn.imag.__round__() * 1j))
        return rtn
    @staticmethod
    def calculate_exp(n, k , N, signal_type):
        pow = (1j * 2 * n * k) / N
        if pow.imag == 0:
            return 1 + 0j

        sin_value = float(math.sin(math.pi * abs(pow.imag)))
        cos_value = float(math.cos(math.pi * abs(pow.imag)))

        if signal_type == 'dft':
            sin_value *= -1j
        else:
            cos_value = cos_value.__round__()
            sin_value *= 1j
        e = cos_value  + sin_value

        return e
    @staticmethod
    def calculate_fundamentel_freq(self, sampling_freqency, length_of_signal):
        periodic_time = 1 / sampling_freqency
        down_term = length_of_signal * periodic_time
        up_term = 2 * math.pi
        return up_term / down_term
    @staticmethod
    def calculate_amplitude(self, data):

        ampl = []
        for i in range(len(data)):
            powered_real_number = data[i].real * data[i].real
            powered_imag_number = data[i].imag * data[i].imag
            summ = powered_real_number + powered_imag_number
            ampl.append(math.sqrt(float(summ)))
        return ampl
    @staticmethod
    def calculate_phase_shift(self, data):
        phases = []
        for i in range(len(data)):
            phases.append(float(math.atan2(data[i].imag, data[i].real)))
        return phases

    def signal_representation(sefl, x, amp_y, theta_y):
        plt.subplot(2, 1, 1)
        signal_plot.plot_discrete_signal(x, amp_y, 'Frequency',
                                            'Amplitude',
                                            'Frequency Domain with Amplitude')
        plt.subplot(2, 1, 2)
        signal_plot.plot_discrete_signal(x, theta_y, 'Frequency',
                                            'Phase Shift',
                                            'Frequency Domain with Phase Shift')

    def plot_freq_domain(self, fundamentel_freq, amp_y, theta_y):
        x = []
        for i in range(len(amp_y)):
            x.append(i * fundamentel_freq)
        self.signal_representation(x, amp_y, theta_y)
    def plot_time_domain(self, y):
        x = []
        for i in range(len(y)):
            x.append(i)

        signal_plot.plot_discrete_signal(x, y, 'time', 'samples', 'Time Domain')
        plt.tight_layout()
        plt.show()

    def convert_from_polar_form(self, ampl, theta):
        outputs = []
        for i in range(len(ampl)):
            img = ampl[i] * math.sin(theta[i]) * 1j
            real = ampl[i] * math.cos(theta[i])
            complex_num = img + real
            outputs.append(complex_num)
        return outputs

