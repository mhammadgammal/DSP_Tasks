from tkinter import *
# from tkinter import ttk
# import numpy as np
# import signal_plot as plot
#
#
# def init_widgets() -> (str, str, str, str, str):
#     root_window = Tk()
#     root_window.geometry( "500x300" )
#     signal_type_combo = ttk.Combobox( root_window, values=['Sine', 'cosine'] )
#     signal_type_combo.set( 'Sine' )
#     signal_type_combo.pack()
#
#     Aplitude_label = Label( root_window, text="Amplitude " )
#     Aplitude_label.pack()
#
#     Amplitude_field = Entry( root_window )
#     Amplitude_field.pack()
#
#     phase_shift_label = Label( root_window, text="Phase_Shift " )
#     phase_shift_label.pack()
#
#     phase_shift_field = Entry( root_window )
#     phase_shift_field.pack()
#
#     angular_frequency_label = Label( root_window, text="Angular Frequency" )
#     angular_frequency_label.pack()
#
#     angular_frequency_field = Entry( root_window )
#     angular_frequency_field.pack()
#
#     sampling_frequency_label = Label( root_window, text="Sampling Frequency" )
#     sampling_frequency_label.pack()
#
#     sampling_frequency_field = Entry( root_window )
#     sampling_frequency_field.pack()
#
#     plot_signal_button = Button( root_window, text='Generate Signal', command=generate_signal)
#     plot_signal_button.pack()
#
#     root_window.mainloop()
#     return (signal_type_combo.get(),
#             amplitude.get(),
#             phase_shift_field.get(),
#             angular_frequency_field.get(),
#             sampling_frequency_field.get())
#
#
# def define_signal(
#         amplitude,
#         phase_shift,
#         angular_frequency,
#         sampling_frequency,
#         signal_type
# ):
#
#     if sampling_frequency == 0:
#         x = np.arange(
#             0,
#             2 * angular_frequency,
#             0.01
#         )
#         omega = 2 * np.pi * angular_frequency
#
#         if signal_type == 'sine':
#
#             y = amplitude * np.sin( omega + phase_shift )
#         elif signal_type == 'cosine':
#             y = amplitude * np.cos(
#                 omega + phase_shift
#             )
#
#     else:
#         x = np.arange( 0, sampling_frequency, 1 )
#         omega = 2 * np.pi * (angular_frequency / sampling_frequency)
#         if signal_type == 'sine':
#             y = amplitude * np.sin( omega + phase_shift )
#         elif signal_type == 'cosine':
#             y = amplitude * np.cos( omega + phase_shift )
#
#     return x, y
#
#
# def generate_signal(x_values, y_values):
#     plot.PlotSignal.plot_signals(x_values, y_values)
#     plot.PlotSignal.stem_signals(x_values, y_values)
#
#
# signal_type, amplitude, phase_shift, angular_frequency, sampling_frequency = init_widgets()
# x, y = define_signal(
#     signal_type=signal_type,
#     amplitude=amplitude,
#     phase_shift=phase_shift,
#     angular_frequency=angular_frequency,
#     sampling_frequency=sampling_frequency
# )


def fun(x):
    root = Tk()
    Button(root, command=x).pack()
    root.mainloop()


def test():
    print('Hello')

fun(test)


