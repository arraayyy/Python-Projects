from msilib.schema import Directory
from textwrap import fill
from turtle import width
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

def play(): # defines the play function
    pygame.mixer.music.load(playlist.get(tk.ACTIVE)) # loads the song into the mixer
    var.set(playlist.get(tk.ACTIVE)) # sets the variable to the song that is currently playing
    pygame.mixer.music.play() # plays the song

def stop(): # defines the stop function
    pygame.mixer.music.stop() # stops the song

def pause(): # defines the pause function
    pygame.mixer.music.pause() # pauses the song

def unpause(): # defines the unpause function
    pygame.mixer.music.unpause() # unpauses the song

Button1 = tk.Button(musicPlayer, width = 5, height = 3, text = "Play", font = "Helvetica 12 bold",
                    command = play, bg = "red", fg = "white") # creates a play button
Button2 = tk.Button(musicPlayer, width = 5, height = 3, text = "Stop", font = "Helvetica 12 bold",
                    command = stop, bg = "purple", fg = "white") # creates a stop button
Button3 = tk.Button(musicPlayer, width = 5, height = 3, text = "Pause", font = "Helvetica 12 bold",
                    command = pause, bg = "green", fg = "white") # creates a pause button
Button4 = tk.Button(musicPlayer, width = 5, height = 3, text = "Unpause", font = "Helvetica 12 bold",
                    command = unpause, bg = "blue", fg = "white") # creates an unpause button 

var = tk.StringVar() # creates a variable
songtitle = tk.Label(musicPlayer, textvariable = var, font = "Helvetica 12 bold") # creates a label

songtitle.pack() # packs the label
Button1.pack(fill = tk.X) # packs the play button
Button2.pack(fill = tk.X) # packs the stop button
Button3.pack(fill = tk.X) # packs the pause button
Button4.pack(fill = tk.X) # packs the unpause button
playlist.pack(fill = "both", expand = "yes") # packs the listbox

musicPlayer.mainloop()