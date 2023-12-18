import signal_plot as plot
import tkinter as tk
from tkinter import filedialog
import task1
import task3
import task4
import Fourierr_task
import DCT
import task_6
import task_7
import task9 as t
import CompareSignal
# def open_task_one():
#     task1.TaskOne()
# def open_task_two():
#     task3.SignalOperation()

# def open_task_three():
#     task4.Quantize()

# def open_Fourier_task():
#     Fourierr_task.FourierTransform()

# def open_task_5():
#     DCT.DctTransfrom()

# def open_task_6():
#     task_6.TimeDomain()

# def open_task_7():
#     task_7.Task7()

# main_screen = tk.Tk()
# main_screen.title('DSP Framework')
# main_screen.geometry('600x400')
# task_1 = tk.Button(main_screen, text='Task One', command=open_task_one, width=40)
# task_1.pack(anchor='w', padx=10, pady=30)

# task_2 = tk.Button(main_screen, text='Task Two', command=open_task_two, width=40)
# task_2.pack(anchor='w', padx=10, pady=5)

# task_3 = tk.Button(main_screen, text='Task Three', command=open_task_three, width=40)
# task_3.pack(anchor='w', padx=10, pady=5)

# task_4 = tk.Button(main_screen, text='Fourier Transform', command=open_Fourier_task, width=40)
# task_4.pack(anchor='w', padx=10, pady=5)

# task_5 = tk.Button(main_screen, text='DCT', command=open_task_5, width=40)
# task_5.pack(anchor='w', padx=10, pady=5)

# task_6_btn = tk.Button(main_screen, text='Time Domain', command=open_task_6, width=40)
# task_6_btn.pack(anchor='w', padx=10, pady=5)

# task_7_btn = tk.Button(main_screen, text='Correlation', command=open_task_7, width=40)
# task_7_btn.pack(anchor='w', padx=10, pady=5)

# main_screen.mainloop()

m,n = t.resampling(factor_m = 2, factor_l = 0)
CompareSignal.Compare_Signals(
    'Sampling_Down.txt', m ,n
)

