import matplotlib.pyplot as plt
import tkinter as tk
import os
from tkinter import filedialog


def generate_discrete_signal(x, y):
    plt.stem( x, y )
    plt.title( "Discrete Signal" )
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