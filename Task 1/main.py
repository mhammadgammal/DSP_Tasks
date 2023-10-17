import signal_plot as plot
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt


def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[('TextFiles', '*.txt')]
    )

    if file_path:
        with open( file_path, 'r' ) as f:
            signal_one_type = int( f.readline().strip() )
            is_periodic_one = int( f.readline().strip() )
            num_samples_one = int( f.readline().strip() )
            samples_one = [list( map( float, line.strip().split() ) ) for line in f]
            indexes_one = [sample[0] for sample in samples_one]
            values_one =  [sample[1] for sample in samples_one]

        plot.plot_signals( indexes_one, values_one )
        stem_signals(indexes_one, values_one)



root_window = tk.Tk()
root_window.geometry("500x300")
open_file_button = tk.Button(root_window, text='Open File', command=open_file)

open_file_button.pack()   
root_window.mainloop()
