import math
from scipy.fftpack import dct
import numpy as np
import signal_plot
import comparesignal2
class DctTransfrom:
    def __init__(self):
        print('DCT Transform started')
        _, signal, file_name = signal_plot.open_file()

        print(signal)
        signal = [round(i, 5) for i in signal]
        self.dct = self.dct_transform(signal)
        print(f'dct: {self.dct}')
        
        comparesignal2.SignalSamplesAreEqual('DCT_output.txt', self.dct)
    def dct_transform(self, signal):
        N = len(signal)
        y = []

        for k in range(N):
            # Cummulative from n = 0 -> N-1 (Correction: Change 2*N to 2*n)
            cumm_sum = 0.0
            for n in range(N):
                # K = k
                radian_angle = (np.pi/(4*N)) * (2*n - 1) * (2*k - 1)
                
                # Sum(x(n) * cos(pi/N (2n+1)k))
                cumm_sum += signal[n] * math.cos(radian_angle)
            
            y_k = np.sqrt(2/N) * cumm_sum
            y.append(y_k)

        return y
    
    # def dct_transform(self, input_signal):
    #     # Initialize variables
    #     N = len(input_signal)
    #     y = np.zeros(N)

    #     # Calculate DCT
    #     for k in range(N):
    #         for n in range(N):
    #             y[k] += input_signal[n] * np.cos(np.pi * k * (n + 0.5) / N)

    #     return y
    

dct = DctTransfrom()