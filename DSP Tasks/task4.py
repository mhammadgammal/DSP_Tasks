import tkinter as tk
import signal_plot as plot
import math
from QuanTest1 import QuantizationTest1
from QuanTest2 import QuantizationTest2
class Quantize:

    def __init__(self):
        print( 'Task 4 begins' )
        self.root = tk.Tk()
        self.test_button = tk.Button( self.root, text='Test' )
        self.test_button.pack()
        self.radio_frame = tk.Frame( self.root )
        self.selected_event = tk.StringVar( self.radio_frame, '' )
        self.radio_levels = tk.Radiobutton( self.radio_frame, text='Levels', value='levels',
                                            variable=self.selected_event )
        self.radio_levels.pack( side='left' )
        self.radio_bits = tk.Radiobutton( self.radio_frame, text='Bits', value='bits',
                                          variable=self.selected_event )
        self.radio_bits.pack( side='left' )

        self.entry = tk.Entry( self.root )
        self.radio_frame.pack( fill='x' )
        self.entry.pack( fill='x' )
        self.root.mainloop()

    def generate_bits_quantized_signal(self):
        x, y, file_name = plot.open_file()
        levels = int( self.entry.get() )
        _min = min( y )
        _max = max( y )
        delta = (_max - _min) / pow( 2, levels )

        quantized = []
        ra = []
        min_array = []
        max_array = []
        for i in range( pow( 2, levels ) ):
            tmp = round( float( _min + delta ), 4 )
            mid = round( float( tmp + _min ) / 2, 4 )
            quantized.append( mid )
            min_array.append( _min )
            max_array.append( tmp )

        for i in range( len( y ) ):
            for x in range( pow( 2, levels ) ):
                if min_array[x] <= y[i] <= max_array[x]:
                    ra.append( x )
                    break

        result_array = []
        for i in range( len( ra ) ):
            result_array.append( quantized[ra[i]] )

        print( result_array )

        encoded_array = []
        reverse_binary_digits = lambda binary_digit: ''.join(
            reversed( [str( (binary_digit >> bit) & 1 ) for bit in range( int( self.entry.get() ) )] ) )

        for i in range( len( ra ) ):
            encoded_array.append( reverse_binary_digits( ra[i] ) )

        print( encoded_array )

        QuantizationTest1( "Quan1_Out.txt", encoded_array, result_array )
    def generate_levels_quantized_signal(self):
        x, y, file_name = plot.open_file()
        levels = int( self.entry.get() )
        _min = min( y )
        _max = max( y )
        delta = round((_max - _min) / math.log( levels, 2 ), 3)

        quantized = []
        ra = []
        min_array = []
        max_array = []
        for i in range( len( y ) ):
            tmp = round( float( _min + delta ), 3 )
            mid = round( float( tmp + _min ) / 2, 3 )
            quantized.append( mid )
            min_array.append( _min )
            max_array.append( tmp )

        for i in range( len( y ) ):
            for x in range( pow( 2, levels ) ):
                if min_array[x] <= y[i] <= max_array[x]:
                    ra.append( x )
                    break

        result_array = []
        for i in range( len( ra ) ):
            result_array.append( quantized[ra[i]] )

        print( result_array )

        encoded_array = []

        reverse_binary_digits = lambda binary_digit: ''.join(
            reversed( [str( (binary_digit >> bit) & 1 ) for bit in range( int( self.entry.get() ) )] ) )

        for i in range( len( ra ) ):
            encoded_array.append( reverse_binary_digits( ra[i] ) )
        er = []
        for i in range( len( ra ) ):
            a = float( result_array[i] - y[i] )
            a = round( a, 3 )
            er.append( a )
        for i in range( len( ra ) ):
            ra[i] = ra[i] + 1
        print( ra )
        print( encoded_array )
        print( result_array )
        print( er )
        print( encoded_array )
        QuantizationTest2( "Quan2_Out.txt", ra, encoded_array, result_array, er )