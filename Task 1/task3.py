import tkinter as tk
import signal_plot as plot


class SignalOperation:

    def __init__(self):
        self.signal_1_indexes = []
        self.signal_1_values = []
        self.signal_2_indexes = []
        self.signal_2_values = []
        self.result_signals_values = []
        self.signal_1_file_name = None
        self.signal_2_file_name = None
        self.root = tk.Tk()
        self.root.geometry( '500x300' )
        self.radio_frame = tk.Frame( self.root )
        self.signal_1_frame = tk.Frame( self.root )
        self.signal_2_frame = tk.Frame( self.root )
        self.selected_event = tk.StringVar( self.radio_frame, '' )

        self.addition = tk.Radiobutton( self.radio_frame, text='Addition',
                                        variable=self.selected_event, value='addition', command=self.on_radio_change )
        self.addition.pack( side='left' )
        self.subtract = tk.Radiobutton( self.radio_frame, text='Subtransition',
                                        variable=self.selected_event, value='subtraction',
                                        command=self.on_radio_change )
        self.subtract.pack( side='left' )
        self.mutliply = tk.Radiobutton( self.radio_frame, text='Mutliplication',
                                        variable=self.selected_event, value='mutliplication',
                                        command=self.on_radio_change )
        self.mutliply.pack( side='left' )
        self.square = tk.Radiobutton( self.radio_frame, text='Squaring',
                                      variable=self.selected_event, value='squaring', command=self.on_radio_change )
        self.square.pack( side='left' )
        self.shifting = tk.Radiobutton( self.radio_frame, text='Shifting',
                                        variable=self.selected_event, value='shifting', command=self.on_radio_change )
        self.shifting.pack( side='left' )
        self.normalize = tk.Radiobutton( self.radio_frame, text='Normalize',
                                         variable=self.selected_event, value='normalize', command=self.on_radio_change )
        self.normalize.pack( side='left' )
        self.addition.select()

        self.select_signal_1_button = tk.Button( self.signal_1_frame, text='select signal 1',
                                                 command=self.select_signal_1_file )
        self.select_signal_1_button.pack( side='left' )
        self.signal_1_label = tk.Label( self.signal_1_frame, text='signal 1 label' )
        self.signal_1_label.pack( side='left', padx=20 )

        self.select_signal_2_button = tk.Button( self.signal_2_frame, text='select signal 2',
                                                 command=self.select_signal_2_file )
        self.select_signal_2_button.pack( side='left' )
        self.signal_2_label = tk.Label( self.signal_2_frame, text='signal 2 label' )
        self.signal_2_label.pack( side='left', padx=20 )

        self.generate = tk.Button( self.root, text='generate', command=self.generate_result_signal )

        self.radio_frame.pack( fill='x' )

        self.signal_1_frame.pack( fill='x', padx=10, pady=5 )
        self.signal_2_frame.pack( fill='x', padx=10, pady=5 )
        self.generate.pack()
        self.root.mainloop()

    def on_radio_change(self):
        print(self.selected_event.get())

    def select_signal_1_file(self):
        (self.signal_1_indexes,
         self.signal_1_values,
         self.signal_1_file_name) = plot.open_file()
        print(self.signal_1_file_name)
        print('Signal 1 indexes', self.signal_1_indexes)
        self.signal_1_label.config(text=self.signal_1_file_name)

    def select_signal_2_file(self):
        (self.signal_2_indexes,
         self.signal_2_values,
         self.signal_2_file_name) = plot.open_file()
        print(self.signal_2_file_name)
        print('Signal 2 indexes', self.signal_2_indexes)
        self.signal_2_label.config(text=self.signal_2_file_name)

    def generate_result_signal(self):
        if self.selected_event.get() == 'addition':
            self.add_signals()
        else:
            print('Please select an event')

    def add_signals(self):
        print( self.signal_1_indexes )
        max_index = [index for index in range(max( len( self.signal_1_indexes ), len( self.signal_2_indexes ) ))]
        print(max_index)
        print('Signal 1 values:', self.signal_1_values)
        print('Signal 2 values:', self.signal_2_values)

        for signal_value in range(max(len(self.signal_1_values), len(self.signal_2_values))):
            self.result_signals_values.append(self.signal_1_values[signal_value] + self.signal_2_values[signal_value])
        print(f'result signal:', self.result_signals_values)
        plot.generate_continuous_signal(max_index, self.result_signals_values )
        plot.generate_discrete_signal( max_index, self.result_signals_values )
