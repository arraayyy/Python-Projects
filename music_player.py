import pygame # module for creating video games, includse computer graphics and sound libraries
import tkinter as tk # module for creating GUI applications
from tkinter.filedialog import askdirectory # module for opening a directory
import os # provides functions for interacting with the operating system

musicPlayer = tk.Tk() # creates a window
musicPlayer.title("Music Player") # sets the title of the window
musicPlayer.geometry("450 X 350") # sets the size of the window, parameters(width, height)