import matplotlib.pyplot as plt
import tkinter as tk
import os
from tkinter import filedialog


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