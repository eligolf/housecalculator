# Explanations for the file

import os
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import keyboard
import locale
import tkinter.font as font

from settings import *

# --------------------------------------
# Transparent icon
_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)

    
class Expl(tk.Frame):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = round(WIDTH/2)
        self.height = round(HEIGHT/1.8)

        self.window = tk.Toplevel()

        self.window.wm_geometry('%dx%d+%d+%d' % (self.width, self.height, max(0, self.x - (WIDTH/2 - WIDTH/2/2)), max(0, self.y - (HEIGHT/2 - HEIGHT/1.8/2))))
        self.window.title('Förklaringar')
        self.window.configure(background=BG)
        self.window.iconbitmap(default=ICON_PATH)

        tk.Frame.__init__(self, self.window)
        myframe=tk.Frame(self.window, width=self.width, height=self.height, bd=1, background=BG)
        myframe.place(x=10,y=10)

        self.canvas = tk.Canvas(self.window, borderwidth=0, background=BG)        
        self.frame = tk.Frame(self.canvas, background=BG)
        self.vsb = tk.Scrollbar(self.window, orient="vertical", command=self.canvas.yview)
        self.hsb = tk.Scrollbar(self.window, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.canvas.configure(xscrollcommand=self.hsb.set)
        self.canvas.bind_all("<MouseWheel>", self.onmousewheel)

        self.frame.bind("<Configure>", self.myfunction)
        self.frame.bind("<Configure>", self.onFrameConfigure)
        #self.canvas.bind("<Configure>", self.on_canvas_configure)

        self.vsb.pack(side="right", fill="y")
        self.hsb.pack(side="bottom", fill="x")
        self.canvas.create_window((0,0),window=self.frame,anchor='nw')
        self.canvas.pack(side="left", fill="both", expand=True)

        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        self.draw()

##    def on_canvas_configure(self, event):
##        self.text.on_configure(event)
        
    def myfunction(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def onmousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/60)), "units")

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def draw(self):
        pad_x = 10
        pad_y = 15
        
        # Over titles
        font = TITLE_FONT
        size = TITLE_SIZE
        row_h = 2*len(TEXT_ALL) + 1
        row_br = row_h + 2*len(TEXT_H) + 2
        row = [0, row_h, row_br]

        for i in range(len(OVER_TITLES)):
            tk.Label(self.frame, text=OVER_TITLES[i], font=(font, size, 'bold', 'underline'), bg=BG).grid(row=row[i], column=0, sticky='sw', padx=pad_x, pady=(pad_y, 0))

        # Titles
        font = TITLE_FONT
        size = TEXT_SIZE
        
        for i in range(len(TITLES_ALL)):
            tk.Label(self.frame, text=TITLES_ALL[i], font=(font, size, 'bold'), bg=BG).grid(row=2*i+1, column=0, sticky='sw', padx=pad_x, pady=(pad_y/2, 0))
          
        for i in range(len(TITLES_H)):
            tk.Label(self.frame, text=TITLES_H[i], font=(font, size, 'bold'), bg=BG).grid(row=row_h+2*i+1, column=0, sticky='sw', padx=pad_x, pady=(pad_y/2, 0))
            
        for i in range(len(TITLES_BR)):
            tk.Label(self.frame, text=TITLES_BR[i], font=(font, size, 'bold'), bg=BG).grid(row=row_br+2*i+1, column=0, sticky='sw', padx=pad_x, pady=(pad_y/2, 0))
       

        # Text
        font = TITLE_FONT
        size = TEXT_SIZE
        
        for i in range(len(TEXT_ALL)):
            tk.Label(self.frame, text=TEXT_ALL[i], font=(font, size), bg=BG).grid(row=2*i+2, column=0, sticky='sw', padx=pad_x)
    
        for i in range(len(TEXT_H)):
            tk.Label(self.frame, text=TEXT_H[i], font=(font, size), bg=BG).grid(row=row_h+2*i+2, column=0, sticky='sw', padx=pad_x)
      
        for i in range(len(TEXT_BR)):
            if i == len(TEXT_BR) - 1:
                tk.Label(self.frame, text=TEXT_BR[i], font=(font, size), bg=BG).grid(row=row_br+2*i+2, column=0, sticky='sw', padx=pad_x, pady=(0, pad_y))
            else:
                tk.Label(self.frame, text=TEXT_BR[i], font=(font, size), bg=BG).grid(row=row_br+2*i+2, column=0, sticky='sw', padx=pad_x)
       

##class WrappingLabel(tk.Label):
##    def __init__(self, master=None, **kwargs):
##        tk.Label.__init__(self, master, **kwargs)
##
##    def on_configure(self, event):
##        widget = event.widget
##        if isinstance(widget, tk.Canvas):
##            width = widget.winfo_width()
##            border = 4
##            scrollbar = 12
##            self.config(wraplength=width - (border + scrollbar))
