import signal_plot as plot
import tkinter as tk
from tkinter import filedialog
import task1
import task3
import task4
import Fourierr_task
def open_task_one():
    task1.TaskOne()
def open_task_two():
    task3.SignalOperation()

def open_task_three():
    task4.Quantize()

def open_Fourier_task():
    Fourierr_task.FourierTransform()
main_screen = tk.Tk()
main_screen.geometry('600x400')
task_1 = tk.Button(main_screen, text='Task One', command=open_task_one, width=40)
task_1.pack(anchor='w', padx=10, pady=30)

task_2 = tk.Button(main_screen, text='Task Two', command=open_task_two, width=40)
task_2.pack(anchor='w', padx=10, pady=5)

task_3 = tk.Button(main_screen, text='Task Three', command=open_task_three, width=40)
task_3.pack(anchor='w', padx=10, pady=5)
task_4 = tk.Button(main_screen, text='Fourier Transform', command=open_Fourier_task, width=40)
task_4.pack(anchor='w', padx=10, pady=5)
main_screen.mainloop()
