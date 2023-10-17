from tkinter import *
from tkinter import ttk
import numpy as np

window = Tk()
window.geometry("500x300")

signal_type_combo = ttk.Combobox( window, values=["Option 1", "Option 2", "Option 3"] )
combo_box.pack()

Aplitude_label = Label( window, text="Amplitude " )
Aplitude_label.pack()

Amplitude_field = Entry( window )
Amplitude_field.pack()

phase_shift_label = Label( window, text="Phase_Shift " )
phase_shift_label.pack()

phase_shift_field = Entry( window )
phase_shift_field.pack()

angular_frequency_label = Label( window, text="Angular Frequency" )
angular_frequency_label.pack()

angular_frequency_field = Entry( window )
angular_frequency_field.pack()

sampling_frequency_label = Label( window, text="Sampling Frequency" )
sampling_frequency_label.pack()

sampling_frequency_field = Entry( window )
sampling_frequency_field.pack()

plot_signal_button = Button(window, text='Generate Signal')
window.mainloop()





def generate_signal(
        amplitude,
        phase_shift,
        angular_frequency,
        sampling_frequency,
        signal_type
):
    omega = none
    if sampling_frequency == 0:
        x = np.arange(
            0,
            2 * angular_frequency,
            0.01
        )
        omega = 2 * np.pi * angular_frequency

        if signal_type == 'sine':

            y = amplitude * np.sin( omega + phase_shift )
        elif signal_type == 'cosine':
            y = amplitude * np.cos(
                omega + phase_shift
            )

    else:
        x = np.arange( 0, sampling_frequency, 1 )
        omega = 2 * np.pi * (angular_frequency / sampling_frequency)
        if signal_type == 'sine':
            y = amplitude * np.sin( omega + phase_shift )
        elif signal_type == 'cosine':
            y = amplitude * np.cos( omega + phase_shift )

    return x, y

x, y = generate_signal(
    amplitude= sampling_frequency_field.get(),
    phase_shift= phase_shift_field.get(),
    angular_frequency= angular_frequency_field.get(),
    sampling_frequency= sampling_frequency_field.get(),
    signal_type = signal_type_combo.get()
)

