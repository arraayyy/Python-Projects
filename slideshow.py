from itertools import cycle # itertools - module contains functions for creating iterators for efficient looping
                            # cycle - creates an iterator that returns elements from the iterable
import tkinter as tk

class App(tk.Tk):
    def __init__(self, image_files, x, y, delay):
        tk.Tk.__init__(self)
        self.geometry('+{}+{}'.format(x, y))
        self.delay = delay
        self.pictures = cycle((tk.PhotoImage(file=image), image) # PhotoImage - class for Tkinter images
        for image in image_files)
        self.pictures_display = tk.Label(self)
        self.pictures_display.pack()

    def show_slides(self):
        img_object, img_name = next(self.pictures)
        self.pictures_display.config(image=img_object)
        self.title(img_name)
        self.after(self.delay, self.show_slides) # after - schedules a function to be called after the given time

    def run(self):
        self.mainloop()

    delay = 3500

    image_files = [
        '1.jpg',
        '2.gif',
        '3.gif',
    ]

x = 100
y = 50
app = App(image_files, x, y, delay)
app.show_slides()
app.run()


# NOT WORKING