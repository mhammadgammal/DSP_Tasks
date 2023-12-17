import matplotlib.pyplot as plt
import tkinter as tk
import os
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def generate_discrete_signal(x, y):
    plt.stem( x, y )
    plt.title( "Discrete Signal" )
    plt.show()

def plot_discrete_signal(x, y, x_label, y_label, signal_label):
    plt.stem(x, y)
    plt.title( signal_label )
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
def generate_continuous_signal(x, y):
    plt.plot( x, y )
    plt.title( "Continuous Signal" )
    plt.show()


def open_file():

    file_path = filedialog.askopenfilename(
        filetypes=[('TextFiles', '*.txt')]
    )

    if file_path:
        with open( file_path, 'r' ) as f:
            int( f.readline().strip() )
            int( f.readline().strip() )
            int( f.readline().strip() )
            samples_one = [list( map( float, line.strip().split() ) ) for line in f]
            print('signals', samples_one)
            file_name = os.path.basename(f.name)
            print(file_name)
        indexes_one = [sample[0] for sample in samples_one]
        values_one = [sample[1] for sample in samples_one]
        return indexes_one, values_one, file_name
def read_signal():
    signal = filedialog.askopenfile(filetypes=[("txt", "*.txt")])
    # define the signal
    signal_type = int(signal.readline().strip())
    is_periodic = int(signal.readline().strip())
    num_samples = int(signal.readline().strip())
    samples = [list(map(float, line.strip().split())) for line in signal]
    indexes = [sample[0] for sample in samples]
    values = [sample[1] for sample in samples]
    return signal_type, is_periodic, num_samples, indexes, values
def plot_original_and_affected(root_window, original_signal, signal_after_effect, original_signal_label, signal_after_effect_label):
        # Create a figure and axis
        fig, (original_signal_plt, signal_after_effect_plt)  = plt.subplots(2, 1, figsize=(5, 3))
        original_signal_plt.plot(original_signal, label=original_signal_label)
        original_signal_plt.legend()
        signal_after_effect_plt.plot(signal_after_effect, label=signal_after_effect_label)
        signal_after_effect_plt.legend()
            
        # Embed the figure in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=root_window)
        canvas_widget = canvas.get_tk_widget()
        # canvas_widget.grid(row=1, column=0, padx=10, pady=10)
        canvas_widget.pack(fill='both')
        root_window.canvas_widget = canvas_widget

def read_signal_from_file(file_name):
    signal = open(file_name)
    # define the signal
    signal_type = int(signal.readline().strip())
    is_periodic = int(signal.readline().strip())
    num_samples = int(signal.readline().strip())
    samples = [list(map(float, line.strip().split())) for line in signal]
    indexes = [sample[0] for sample in samples]
    values = [sample[1] for sample in samples]
    return signal_type, is_periodic, num_samples, indexes, values    

def read_signal(file_path):
    signal = open(file_path)
    # define the signal
    signal_type = int(signal.readline().strip())
    is_periodic = int(signal.readline().strip())
    num_samples = int(signal.readline().strip())
    samples = [list(map(float, line.strip().split())) for line in signal]
    indexes = [sample[0] for sample in samples]
    values = [sample[1] for sample in samples]
    return signal_type, is_periodic, num_samples, indexes, values

def read_filter_specifications():
    file_path = filedialog.askopenfilename(
        filetypes=[('TextFiles', '*.txt')]
    )
    
    try:
        filter_specs = {} 
        with open(file_path, 'r') as file:
            file_lines = file.readlines()
        
        for line in file_lines:
            file_line = line.split('=')
            filter_spec_key = file_line[0]
            filter_spec_value = file_line[1]
            filter_specs[filter_spec_key] = filter_spec_value

        return filter_specs
    except Exception as exp:
        print(str(exp))