import numpy as np
import math
import tkinter as tk
import os
import signal_plot
from tkinter import messagebox
class Task7:
    def __init__(self):
        print('Task 7 Started')
        self.normalized_corr()
        self.time_analysis()
        self.root = tk.Tk()
        self.root.geometry('700x500')
        self.root.title('Correlation')
        self.correlate_btn = tk.Button(self.root, text='correlate', command=self.on_corr_click)
        self.time_analysis_btn = tk.Button(self.root, text='Time Analysis', command=self.on_time_analysis_click)
        self.match_btn = tk.Button(self.root, text='Match', command=self.template_matching)
        self.correlate_btn.pack()
        self.time_analysis_btn.pack()
        self.match_btn.pack()
        self.root.mainloop()

    def on_corr_click(self): 
        corr, indicates = self.normalized_corr()
        corr_tst_rslt = self.Compare_Signals('correalation_inputs,outputs/CorrOutput.txt', indicates, corr)
        messagebox.showinfo(title='correlation test', message=corr_tst_rslt)

    def on_time_analysis_click(self):
        time_analysis_result = self.time_analysis()
        messagebox.showinfo(title='Time Analysis value', message=time_analysis_result)

    def template_matching(self):
        value = self.get_correlation_of_test()
        new_value = f'{value[0]} \n {value[1]}'
        messagebox.showinfo(title='Template Matching', message=new_value)

    def calculate_cross_correlation_element(self, signal1, signal2):

        summ = 0
        n = len(signal2)
        for i in range(n):
            summ += signal1[i] * signal2[i]
        return summ

    def calc_cross_correlation(self, signal1, signal2):
        cross_correlation = []
        shifted_signal = signal2
        
        for i in range(len(signal2)):
            corr_val = self.calculate_cross_correlation_element(signal1, shifted_signal) / len(signal1)
            first_val = shifted_signal[0]
            shifted_signal = shifted_signal[1:]
            shifted_signal.append(first_val)
            cross_correlation.append(corr_val)
        
        return cross_correlation

    def normalized_corr(self):

        _, _, _, indicates, signal1 = signal_plot.read_signal('correalation_inputs,outputs/Corr_input signal1.txt')
        _, _, _, indicates, signal2 = signal_plot.read_signal('correalation_inputs,outputs/Corr_input signal2.txt')
        
        element1 = self.calculate_cross_correlation_element(signal1, signal1)
        element2 = self.calculate_cross_correlation_element(signal2, signal2)
        denominator = math.sqrt((element1 * element2)) / len(signal1)
        corr = self.calc_cross_correlation(signal1, signal2)
        normalized_cross_correlation_signal = [x/denominator for x in corr]
        print('normalized_cross_correlation_signal:',normalized_cross_correlation_signal)
        return normalized_cross_correlation_signal, indicates
    
    def time_analysis(self, fs = 100):
        _, _, _, indicates, signal1 = signal_plot.read_signal('time_analysis_files/TD_input signal1.txt')
        _, _, _, indicates, signal2 = signal_plot.read_signal('time_analysis_files/TD_input signal2.txt')
        calc_correlation = self.calc_cross_correlation(signal1, signal2)
        abs_value = [abs(x) for x in calc_correlation]
        max_value = max(abs_value)
        the_lag = indicates[abs_value.index(max_value)]
        ts = 1 / fs
        print(the_lag * ts)
        return the_lag * ts

    def get_signal_of_class(self, folder_path):
        means_list = []
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path) and filename.endswith('.txt'):
                # Read numbers from the text file
                with open(file_path, 'r') as file:
                    lines = file.readlines()

                # Convert lines to integers
                numbers = [int(line.strip()) for line in lines]

                # Calculate mean and append to means_list
                mean_value = sum(numbers) / len(numbers)
                means_list.append(mean_value)
        return means_list

    def get_correlation_of_test(self):
        with open('test_signals/Test1.txt', 'r') as file:
            lines1 = file.readlines()

        with open('test_signals/Test2.txt', 'r') as file:
            lines2 = file.readlines()

        # test signal
        signal_test_1 = [int(line.strip()) for line in lines1]
        signal_test_2 = [int(line.strip()) for line in lines2]

        # class signals
        signal_class_1 = self.get_signal_of_class('class_1_files')
        signal_class_2 = self.get_signal_of_class('class_2_files')
        signal_class = signal_class_1 + signal_class_2

        correlation1 = self.calc_cross_correlation(signal_test_1, signal_class)
        correlation2 = self.calc_cross_correlation(signal_test_2, signal_class)

        maxx1 = np.argmax(correlation1)
        maxx2 = np.argmax(correlation2)

        if maxx1 > maxx2:
            return 'Test Signal 1 belongs to class 2 (UP)', 'Test Signal 2 belongs to class 1 (Down)'
        else:
            return 'Test Signal 2 belongs to class 2 (UP)', 'Test Signal 1 belongs to class 1 (Down)'
    def Compare_Signals(self, file_name, Your_indices, Your_samples):
        expected_indices = []
        expected_samples = []
        with open(file_name, 'r') as f:
            line = f.readline()
            line = f.readline()
            line = f.readline()
            line = f.readline()
            while line:
                # process line
                L = line.strip()
                if len(L.split(' ')) == 2:
                    L = line.split(' ')
                    V1 = int(L[0])
                    V2 = float(L[1])
                    expected_indices.append(V1)
                    expected_samples.append(V2)
                    line = f.readline()
                else:
                    break
        print("Current Output Test file is: ")
        print(file_name)
        print("\n")
        if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
            return ("Shift_Fold_Signal Test case failed, your signal have different length from the expected one")

        for i in range(len(Your_indices)):
            if (Your_indices[i] != expected_indices[i]):
                return ("Shift_Fold_Signal Test case failed, your signal have different indicies from the expected one")
                return
        for i in range(len(expected_samples)):
            if abs(Your_samples[i] - expected_samples[i]) < 0.01:
                continue
            else:
                return ("Correlation Test case failed, your signal have different values from the expected one")
                return
        return ("Correlation Test case passed successfully")
