# this code's sole purpose is to convert kilometers to miles
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#constant that contains the conversion multiplier
KM_TO_MI = 1.609

class KilometerToMile:
    # function that contains the whole application
    def __init__(self, root):
        root.title("km to mile converter")
        frame = LabelFrame(root,  padx=5, pady=5)
        frame.pack(padx=10, pady=10)

        # entry window where input for function is taken
        label = tk.Label(frame, text="Please enter value for km:") 
        label.grid(row=0, column=0)
        # binding 'self.km' and 'textBox' together
        self.km = StringVar()
        textBox = tk.Entry(frame, textvariable=self.km) 
        textBox.grid(row=0, column=1)
        textBox.focus()

        # 'convert' button that runs the 'km_to_mi' function
        convert = tk.Button(frame, text = "convert", command=self.converter)
        convert.grid(row=3, column=1)

        # 'quit' button that closes the program once clicked
        quit = tk.Button(frame, text = "quit", command = root.destroy)
        quit.grid(row=5, column=1)


        # configuring the height and width of the buttons
        convert.config(height=1, width=10)
        quit.config(height=1, width=10)

    #function that converts converts kilometers to miles
    def converter(self):
        # try except statment to display error message whenever invalid input is given
        try:
            mile = float(self.km.get()) * KM_TO_MI
            # formats float to 2 decimal places
            mile = "{:.2f}".format(mile)
            # info message box that displays result
            messagebox.showinfo ("result", (mile, "mile(s)"))
        except ValueError as e:
            messagebox.showerror("Title", e)
        finally:
            # resets the value 
            self.km.set("")

root = Tk()
KilometerToMile(root)
root.mainloop()