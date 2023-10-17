import matplotlib.pyplot as plt


class PlotSignal:
    def __init__(self):
        print('PlotSignal start')
    @staticmethod
    def plot_signals(x_values, y_values):
        plt.plot( x_values, y_values )
        plt.xlabel( 'time' )
        plt.ylabel( 'velocity' )
        plt.title( 'Continuous Signal Plot' )
        plt.grid( True )
        plt.show()

    @staticmethod
    def stem_signals(x_values, y_values):
        plt.stem( x_values, y_values )
        plt.xlabel( 'time' )
        plt.ylabel( 'velocity' )
        plt.title( 'Discrete Signal Plot' )
        plt.grid( True )
        plt.show()
