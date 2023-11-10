import tkinter as tk
import signal_plot as plot
import math
from QuanTest1 import QuantizationTest1
from QuanTest2 import QuantizationTest2
class Quantize:

    def __init__(self):
        print( 'Task 4 begins' )
        self.root = tk.Tk()
        self.root.geometry( '500x300' )
        self.radio_frame = tk.Frame( self.root )
        self.selected_event = tk.StringVar( self.radio_frame, '' )
        self.radio_levels = tk.Radiobutton( self.radio_frame, text='Levels', value='levels',
                                            variable=self.selected_event, command=self.on_radio_change )
        self.radio_levels.pack( side='left' )
        self.radio_bits = tk.Radiobutton( self.radio_frame, text='Bits', value='bits',
                                          variable=self.selected_event, command=self.on_radio_change )
        self.radio_bits.pack( side='left' )
        self.label = tk.Label( self.root, text='Please Enter a number' )
        self.label.pack()
        self.entry = tk.Entry( self.root )
        self.radio_frame.pack( fill='x' )
        self.entry.pack( fill='x' )
        self.generate_button = tk.Button( self.root, text='generate' )
        self.generate_button.pack()
        self.radio_levels.select()
        self.root.mainloop()

    def on_radio_change(self):
        if self.selected_event.get() == 'levels':
            self.custom_layout( label_text='Enter number of levels',
                                button_command=self.generate_levels_quantized_signal )
        if self.selected_event.get() == 'bits':
            self.custom_layout( label_text='Enter number of bits', button_command=self.generate_bits_quantized_signal )

    def custom_layout(self, label_text, button_command):
        self.label.config( text=label_text )
        self.generate_button.config( command=button_command )

    def generate_bits_quantized_signal(self):
        x, y, file_name = plot.open_file()
        print( 'x:', x )
        print( 'y:', y )
        bits = int( self.entry.get() )
        print( f'bits = {bits}' )
        _min = min( y )
        _max = max( y )
        delta = (_max - _min) / pow( 2, bits )

        quantized = []
        interval_index = []
        min_array = []
        max_array = []
        # for i in range( pow( 2, bits ) ):
        #     tmp = round( float( _min + delta ), 4 )
        #     mid = round( float( tmp + _min ) / 2, 4 )
        #     quantized.append( mid )
        #     min_array.append( _min )
        #     max_array.append( tmp )
        min_value = _min
        while min_value < _max:
            min_array.append( round( float( min_value ), 4 ) )
            max_array.append( round( float( min_value + delta ), 4 ) )
            min_value += delta

        encoded_array = []
        reverse_binary_digits = lambda binary_digit: ''.join(
            reversed( [str( (binary_digit >> bit) & 1 ) for bit in range( int( self.entry.get() ) )] ) )
        for i in range( len( y ) ):
            for x in range( pow( 2, bits ) ):
                if min_array[x] <= y[i] <= max_array[x]:
                    interval_index.append( x )
                    encoded_array.append( reverse_binary_digits( interval_index[i] ) )

                    mid = round( float( min_array[x] + max_array[x] ) / 2, 2 )
                    quantized.append( mid )
                    break

        print( 'quantized', type(quantized) )
        print( 'quantized', quantized )
        print( 'interval_index:', interval_index )
        result_array = []
        for i in range( len( interval_index ) ):
            result_array.append( quantized[interval_index[i]] )

        print( f'result_array: {result_array}' )

        encoded_array = []
        reverse_binary_digits = lambda binary_digit: ''.join(
            reversed( [str( (binary_digit >> bit) & 1 ) for bit in range( int( self.entry.get() ) )] ) )

        for i in range( len( interval_index ) ):
            encoded_array.append( reverse_binary_digits( interval_index[i] ) )

        print( 'encoded_array:', encoded_array )

        QuantizationTest1( 'Quan1_Out.txt', encoded_array, quantized )

    def generate_levels_quantized_signal(self):
        x, y, file_name = plot.open_file()
        print( 'x:', x )
        print( 'y:', y )
        levels = int( self.entry.get() )
        print( f'levels = {levels}' )
        _min = min( y )
        _max = max( y )
        delta = (_max - _min) / levels

        quantized = []
        interval_index = []
        min_array = []
        max_array = []
        min_value = _min
        while min_value < _max:
            min_array.append( round( float( min_value ), 4 ) )
            max_array.append( round( float( min_value + delta ), 4 ) )
            min_value += delta

        encoded_array = []
        # reverse_binary_digits = lambda binary_digit: ''.join(
        #     reversed( [str( (binary_digit >> bit) & 1 ) for a bit in range( int( self.entry.get() ) )] ) )
        # encoding signal
        encoded_bits = math.log(levels, 2)
        binary_values = [bin( i )[2:].zfill( int( encoded_bits ) ) for i in range( 2 ** int( encoded_bits ) )]
        int_values = [int( b, 2 ) + 1 for b in binary_values]
        encoded_values = dict( zip( int_values, binary_values ) )
        for i in range( len( y ) ):
            for x in range( len(min_array) ):
                if min_array[x] <= y[i] <= max_array[x]:
                    interval_index.append( x + 1 )
                    encoded_array.append( encoded_values[x + 1] )

                    mid = round( float( min_array[x] + max_array[x] ) / 2, 3 )
                    quantized.append( mid )
                    break

        print( 'quantized', quantized )
        print('encoded_array:', encoded_array)
        print( 'interval_index:', interval_index )

        errorofn = [round(float( er - xn ), 3) for er, xn in zip( quantized, y )]

        print('errorofn:', errorofn)

        QuantizationTest2( 'Quan2_Out.txt',interval_index,  encoded_array, quantized,  errorofn)