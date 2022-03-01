from msilib.schema import Directory
import pygame # module for creating video games, includse computer graphics and sound libraries
import tkinter as tk # module for creating GUI applications
from tkinter.filedialog import askdirectory # module for opening a directory
import os # provides functions for interacting with the operating system

musicPlayer = tk.Tk() # creates a window
musicPlayer.title("Music Player") # sets the title of the window
musicPlayer.geometry("450 X 350") # sets the size of the window, parameters(width, height)

directory = askdirectory() # opens a directory
os.chdir(directory) # changes the current working directory to the specified path, takes only a single argument
songlist = os.listdir() # returns a list of the names of the entries in the directory given by path
playlist = tk.Listbox(musicPlayer, font = "Helvetica 12 bold", bg = "yellow", selectmode = tk.SINGLE) # creates a listbox


for item in songlist: # loops through the songlist
    pos = 0 # sets the position of the songlist
    playlist.insert(pos, item) # inserts the songlist into the listbox
    pos = pos + 1 # increments the position of the songlist

pygame.init() # initializes pygame
pygame.mixer.init() # initializes the mixer, which allows the program to play music