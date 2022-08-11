from tkinter import *
from tkinter import messagebox
import Codes.Start_Threading
from Codes.Start_Sorting import *
from Codes.Start_Searching import *

class Window:
    def __init__(self, root):

        # Main Window
        self.root = root

        # Warning sign for close
        self.root.protocol("WM_DELETE_WINDOW", self.Close)

        # Main Window Size and Center Aligned in the screen
        self.wx, self.wy = 300, 220
        self.wxs, self.wys = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.WINDOW_X, self.WINDOW_Y = (self.wxs / 2) - (self.wx / 2), (self.wys / 2) - (self.wy / 2)
        self.root.geometry('%dx%d+%d+%d' % (self.wx, self.wy, self.WINDOW_X, self.WINDOW_Y))
        self.root.config(bg="#7BD1F2")
        self.root.resizable(False, False)

        # Title And Icon
        self.root.title("Algorithm Visualizer")
        try:
            self.root.iconbitmap("Images/algorithm.ico")
        except:
            img = PhotoImage("Images/algorithm.ico")
            self.root.tk.call('wm', 'iconphoto', self.root._w, img)

        # Heading of the main window
        self.MainLabel = Label(self.root, text='Algorithm Visualizer', bg="#B01E21", fg="blue4",
                               font=("calibri italic", 20))
        self.MainLabel.pack(pady=15)

        # Dictionary On types of Algorithms and their lists
        self.Algo = {'Searching': ['Linear Search', 'Binary Search'],
                     'Sorting': ['Selection Sort', 'Insertion Sort', 'Bubble Sort', 'Merge Sort', 'Quick Sort',
                                 'Heap Sort', 'Radix Sort'],
                    }

        # Two dropdown menu on algorithm type and algorithm name
        self.AlgoTypeVar = StringVar()
        self.AlgoNameVar = StringVar()

        # for automatic update on the second list if something is chosen on the 1st list
        self.AlgoTypeVar.trace('w', self.update_options)

        # two drop down menus configurations
        self.AlgoTypeList = OptionMenu(self.root, self.AlgoTypeVar, *self.Algo.keys())
        self.AlgoTypeList.config(bg="#3498DB", activebackground="hot pink", cursor="hand2")
        self.AlgoNameList = OptionMenu(self.root, self.AlgoNameVar, 'None')
        self.AlgoNameList.config(bg="#3498DB", activebackground="hot pink", cursor="hand2")
        # label of the two dropdown menus
        self.AlgoTypeVar.set("Select Algorithm Type")
        self.AlgoNameVar.set("Select Algorithm")
        self.AlgoTypeList.pack(pady=2)
        self.AlgoNameList.pack(pady=2)

        # next button
        self.NextButton = Button(self.root, text="Next>", bg="pale green", activebackground="lime green",
                                 command=self.Run1)
        self.NextButton.pack(pady=20)

    # for automatic update on the 2nd list if something is chosen on the 1st list
    def update_options(self, *args):
        try:
            algo_list = self.Algo[self.AlgoTypeVar.get()]
        except:
            algo_list = ["None"]
        self.AlgoNameVar.set("Select Algorithm")
        menu = self.AlgoNameList['menu']
        menu.delete(0, 'end')
        for algo in algo_list:
            menu.add_command(label=algo, command=lambda x=algo: self.AlgoNameVar.set(x))

    # Exit button
    def Exit(self):
        self.root.destroy()

    # Close warning
    def Close(self):
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            self.root.destroy()
            exit()

    # Secondary window back button
    def Back(self):
        self.root.destroy()
        Process = Codes.Start_Threading.START()
        Process.start()

    # For running the algorithms
    def Run2(self):
        # If Sorting is selected
        if self.AlgoTypeVar.get() == "Sorting":
            # create a new window for sorting algorithm
            sort_window = Tk()
            # send it to Start_Sort.py file
            Sorting(sort_window, self.AlgoNameVar.get())
            sort_window.mainloop()

        # If Sorting is selected
        elif self.AlgoTypeVar.get() == "Searching":
            # create a new window for sorting algorithm
            search_window = Tk()
            # send it to Start_Sort.py file
            Searching(search_window, self.AlgoNameVar.get())
            search_window.mainloop()

    # For running the secondary window
    def Run1(self):

        # If nothing is selected show an error box
        if self.AlgoTypeVar.get() == "Select Algorithm Type":
            messagebox.showerror("Error!", "Please select Algorithm Type.")

        # If sorting is selected
        elif self.AlgoTypeVar.get() == "Sorting":
            # Destroy the main window
            self.root.destroy()
            # Go to run() function
            self.Run2()

        
        elif self.AlgoTypeVar.get() == "Searching":
            # Destroy the main window
            self.root.destroy()
            # Go to run() function
            self.Run2()
