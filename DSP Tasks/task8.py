import Fourierr_task as FourierTransform
import tkinter as tk
class FastOperation:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title('Choose Task')
        self.root.geometry('800x500')
        self.button_frame = tk.Frame(self.root)
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.task1_btn = tk.Button(self.button_frame, text='Fast Correlation', command=self.on_fast_corr_btn_pressed)
        self.task1_btn.grid(row=0, column=0, sticky=tk.W + tk.E, padx=10)
        self.task1_btn = tk.Button(self.button_frame, text='Fast Convolution', command=self.on_fast_conv_btn_pressed)
        self.task1_btn.grid(row=0, column=1, sticky=tk.W + tk.E, padx=10)
        self.button_frame.pack(fill='x', pady=10)
        self.root.mainloop()
    
    def on_fast_corr_btn_pressed(self):
        signal1 = [1, 0, 0, 1]
        signal2 = [0.5, 1, 1, 0.5]
        correlation = self.fast_correlation(signal1, signal2)
        print(correlation)

    def on_fast_conv_btn_pressed(self):
        signal1 = []
        signal2 = []
        convolution = self.fast_convolution(signal1, signal2)
        print(convolution)
    def fast_correlation(self, signal1, signal2):
        # fourier_transform = FourierTransform.FourierTransform()
        signal1_dft = FourierTransform.FourierTransform.calculate_dft(signal1)
        signal2_dft = FourierTransform.FourierTransform.calculate_dft(signal2)
        tmp = []
        for complex_num in signal1:
            tmp.append(complex_num.conjugate())
        result_fast_correlates_signal = []
        for x, y in zip(signal1_dft, signal2_dft):
            result_fast_correlates_signal.append(x*y)
        result_fast_correlates_signal = FourierTransform.FourierTransform.calculate_idft(result_fast_correlates_signal)
        result_fast_correlates_signal = []
        for x in result_fast_correlates_signal:
            result_fast_correlates_signal.append(x / len(signal1))
        return result_fast_correlates_signal

    def fast_convolution(self, signal1, signal2):
        signal1_dft = FourierTransform.FourierTransform.calculate_dft(signal1)
        signal2_dft = FourierTransform.FourierTransform.calculate_dft(signal2)
        result_conv_signal = []
        for x, y in zip(signal1_dft, signal2_dft):
            result_conv_signal.append(x*y)
        result_conv_signal = FourierTransform.FourierTransform.calculate_idft(result_conv_signal)
        return result_conv_signal

fastOperation = FastOperation()