from tkinter import *
from tkinter import ttk
import numpy as np
import signal_plot as plot


class Task2:
    def __init__(self):
        self.x = ''
        self.y = ''
        self.amplitude = None
        self.phase_shift = None
        self.angular_frequency = None
        self.sampling_frequency = None
        self.signal_type = None
        self.root_window = Tk()
        self.root_window.geometry( "500x300" )
        self.signal_type_combo = ttk.Combobox( self.root_window, values=['Sine', 'cosine'] )
        self.signal_type_combo.set( 'Sine' )
        self.signal_type_combo.pack()

        self.amplitude_label = Label( self.root_window, text="Amplitude " )
        self.amplitude_label.pack()

        self.amplitude_field = Entry( self.root_window )
        self.amplitude_field.pack()

        self.phase_shift_label = Label( self.root_window, text="Phase_Shift " )
        self.phase_shift_label.pack()

        self.phase_shift_field = Entry( self.root_window )
        self.phase_shift_field.pack()

        self.angular_frequency_label = Label( self.root_window, text="Angular Frequency" )
        self.angular_frequency_label.pack()

        self.angular_frequency_field = Entry( self.root_window )
        self.angular_frequency_field.pack()

        self.sampling_frequency_label = Label( self.root_window, text="Sampling Frequency" )
        self.sampling_frequency_label.pack()

        self.sampling_frequency_field = Entry( self.root_window )
        self.sampling_frequency_field.pack()

        self.plot_signal_button = Button( self.root_window, text='Generate Signal', command=self.generate_signal )
        self.plot_signal_button.pack()

        self.root_window.mainloop()

    def define_signal(self):
        self.signal_type = self.signal_type_combo.get()
        self.amplitude = float( self.amplitude_field.get() )
        self.phase_shift = float( self.phase_shift_field.get() )
        self.angular_frequency = float( self.angular_frequency_field.get() )
        self.sampling_frequency = float( self.sampling_frequency_field.get() )

        if self.sampling_frequency == 0:
            self.sampling_frequency = 2 * self.angular_frequency
            self.x = np.arange( 0, self.sampling_frequency, 1 )
            if self.signal_type == 'Sine':
                self.y = self.amplitude * np.sin( (2 * np.pi * self.angular_frequency) * self.x + self.phase_shift )
            elif self.signal_type == 'cosine':
                self.y = self.amplitude * np.cos( (2 * np.pi * self.angular_frequency) * self.x + self.phase_shift )
        elif self.sampling_frequency < 2 * self.angular_frequency:
            print( 'Invalid sampling frequency' )
        else:
            # x(n) = A sin(2 pi f n + theta)
            self.x = np.arange( 0, self.sampling_frequency, 1 )
            omega = 2 * np.pi * (self.angular_frequency / self.sampling_frequency)
            if self.signal_type == 'Sine':
                self.y = self.amplitude * np.sin( omega * self.x + self.phase_shift )
            elif self.signal_type == 'cosine':
                self.y = self.amplitude * np.cos( omega * self.x + self.phase_shift )

    def generate_signal(self):
        self.define_signal()
        plot.generate_continuous_signal(self.x, self.y)
        plot.generate_discrete_signal(self.x, self.y)


