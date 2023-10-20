import tkinter as tk
import signal_plot as plot
import task2


class TaskOne:

    def __init__(self):
        self.root_window = tk.Tk()
        self.root_window.geometry('500x300')
        self.button_frame = tk.Frame(self.root_window)

        self.open_file_button = tk.Button(self.button_frame, text='Open File', command=self.open_file, width=40)
        self.open_file_button.pack(pady=10)
        self.open_task_2_button = tk.Button(self.button_frame, text='Open Task2', command=self.open_task_2, width=40)
        self.open_task_2_button.pack()

        self.button_frame.pack(fill='x')
        self.root_window.mainloop()

    def open_file(self):
        indexes_one, values_one = plot.open_file()
        plot.generate_continuous_signal( indexes_one, values_one )
        plot.generate_discrete_signal( indexes_one, values_one )



    # def read_signal():
    #     signal = filedialog.askopenfile( filetypes=[("txt", "*.txt")] )
    #     # define the signal
    #     signal_type = int( signal.readline().strip() )
    #     is_periodic = int( signal.readline().strip() )
    #     num_samples = int( signal.readline().strip() )
    #     samples_one = [list( map( float, line.strip().split() ) ) for line in signal]
    #     indexes = [sample[0] for sample in samples_one]
    #     values = [sample[1] for sample in samples_one]
    #     return signal_type, is_periodic, num_samples, indexes, values
    def open_task_2(self):
        task2.Task2()
