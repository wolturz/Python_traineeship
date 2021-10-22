import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.button = tk.Button(text = 'quit', command = self.quit)
        
        
        self.entrythingy = tk.Entry()
        self.entrythingy.pack()
        self.button.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())
    
    def quit(self):
        root.destroy()


root = tk.Tk()
myapp = App(root)
print(myapp.print_contents)
myapp.mainloop()
