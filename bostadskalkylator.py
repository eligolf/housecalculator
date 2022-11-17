# Calculator used to calculate future return from stock market investments
# 
# -------------------------------------------------------------------

import os
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import keyboard
import locale
import tkinter.font as font

from settings import *
from explanations import Expl

import tempfile, base64, zlib

# -------------------------------------------------------
# Classes
# -------------------------------------------------------

class Start:

    def __init__(self, window, x, y):
        # Init screen
        self.window = window

        self.x = x
        self.y = y

        self.window.geometry('%dx%d+%d+%d' % (round(WIDTH/2), round(HEIGHT/1.8), self.x, self.y))

        self.window.title(TITLE)
        self.window.configure(background=BG)
        self.window.iconbitmap(default=ICON_PATH)

        locale.setlocale(locale.LC_ALL, '')

        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        self.font = font.Font(family='Helvetica', size=12)

        # Position of window, updates later
        self.init_x = x
        self.init_y = y
    
    def run(self):
        self.menu()
        self.draw()

    def menu(self):
        # Menu bar
        menu = tk.Menu(self.window)
        self.window.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label='Start', menu=file_menu)
        file_menu.add_command(label='Meny', command=self.run)
        file_menu.add_separator()
        file_menu.add_command(label='Avsluta', command=self.quit_func)

        edit_menu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label='Hjälp', menu=edit_menu)
        edit_menu.add_command(label='Förklaringar', command=self.expl_menu)

        self.top_frame = tk.Frame(self.window, bg=LIGHTBLUE)

    def draw(self):
        # Title
        title = tk.Label(self.top_frame, text='Bostadskalkylator', font=(TITLE_FONT, int(TITLE_SIZE*2), 'bold'), bg=BG, fg=FG)
        title.grid(row=0, column=0, pady=(50, 20))

        # Knapp-text
        title = tk.Label(self.top_frame, text='Välj vilken typ av boende du vill räkna på:', font=(TITLE_FONT, int(TITLE_SIZE)), bg=BG, fg=FG)
        title.grid(row=1, column=0, pady=(50, 20))

        # Knappar
        b = tk.Button(self.top_frame, text='Bostadsrätt', bg=WHITE, activebackground=WHITE, command=self.bostad)
        b['font'] = self.font
        b.grid(row=2, column=0, pady=(5,7))

        h = tk.Button(self.top_frame, text='Hus', bg=WHITE, activebackground=WHITE, command=self.hus)
        h['font'] = self.font
        h.grid(row=3, column=0, pady=(7,20))
        
        # Draw frames
        self.top_frame.grid(row=0, column=0, sticky='N')

    def bostad(self):
        # Get position
        self.init_x = self.window.winfo_x()
        self.init_y = self.window.winfo_y()
        
        self.top_frame.destroy()
        self.window.destroy()
        Calc(tk.Tk(), self.init_x, self.init_y).run()

    def hus(self):
        # Get position
        self.init_x = self.window.winfo_x()
        self.init_y = self.window.winfo_y()
        
        self.top_frame.destroy()
        self.window.destroy()
        Calc_h(tk.Tk(), self.init_x, self.init_y).run()

    def quit_func(self):
        self.window.destroy()
        
    def expl_menu(self):
        # Get position
        maxW = self.window.winfo_screenwidth()
        maxH = self.window.winfo_screenheight()

        x = self.window.winfo_x() + (WIDTH/2 - WIDTH/2/2)
        y = min(maxH, self.window.winfo_y() + (HEIGHT/2 - HEIGHT/1.8/2))

        expl_window(x, y)
        
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Calc_h:

    def __init__(self, window, x, y):
        # Init screen
        self.x = x
        self.y = y

        self.window = window
        self.window.title(TITLE)
        self.window.iconbitmap(default=ICON_PATH)
        self.window.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, max(0, self.x - (WIDTH/2 - WIDTH/2/2)), max(0, self.y - (HEIGHT/2 - HEIGHT/1.8/2))))
        self.window.configure(background=BG)

        locale.setlocale(locale.LC_ALL, '')

        self.font = font.Font(family='Helvetica', size=11)
        self.font2 = font.Font(family='Helvetica', size=9)

    def run(self):
        self.menu()
        self.text()

    def menu(self):
        # Menu bar
        menu = tk.Menu(self.window)
        self.window.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label='Start', menu=file_menu)
        file_menu.add_command(label='Meny', command=self.back_main)
        file_menu.add_separator()
        file_menu.add_command(label='Avsluta', command=self.quit_func)

        edit_menu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label='Hjälp', menu=edit_menu)
        edit_menu.add_command(label='Förklaringar', command=self.expl_menu)

        self.left_frame = tk.Frame(self.window, bg=LIGHTBLUE)
        self.middle_frame = tk.Frame(self.window, bg=LIGHTBLUE)
        self.right_frame = tk.Frame(self.window, bg=WHITE, bd=3, relief='sunken')
        #self.bottom_frame = tk.Frame(self.window, bg=WHITE)

    def text(self):

# --------- Left Frame ----------------------------------------------------------------

        # Title
        tk.Label(self.left_frame, text='Allmänt', font=(TITLE_FONT, TITLE_SIZE, 'underline', 'bold'), bg=BG, fg=FG).grid(row=0, column=0, pady=10, sticky='SW')
      
        # Pris på bostad
        self.price = self.draw_text(self.left_frame, 'Pris på bostad:', TEXT_FONT, TEXT_SIZE, 2, 0, PRICE_H_, 'enabled')
        self.price.focus_set()

        # Boyta
        self.space = self.draw_text(self.left_frame, 'Boyta:', TEXT_FONT, TEXT_SIZE, 4, 0, SPACE_, 'enabled')

        # Personer i hushållet
        self.antal = self.draw_text(self.left_frame, 'Personer i hushållet:', TEXT_FONT, TEXT_SIZE, 6, 0, ANTAL_, 'enabled') 

        # Storlek på lån
        self.deposit = self.draw_text(self.left_frame, 'Storlek på lån:', TEXT_FONT, TEXT_SIZE, 8, 0, DEPOSIT_H_, 'enabled')

        # Ränta på lån
        self.interest = self.draw_text(self.left_frame, 'Ränta på lån:', TEXT_FONT, TEXT_SIZE, 10, 0, INTEREST_, 'enabled')

        # Antal år att bo
        self.years = self.draw_text(self.left_frame, 'Antal år att bo:', TEXT_FONT, TEXT_SIZE, 12, 0, YEARS_, 'enabled')

        # Heating (drop down list)
        tk.Label(self.left_frame, text='Värmesystem:', font=(TEXT_FONT, TEXT_SIZE), bg=BG, fg=FG).grid(row=14, column=0, sticky='SW', padx=10, pady=(5, 0))

        self.box_value = tk.StringVar()
        self.box = ttk.Combobox(self.left_frame, textvariable=self.box_value, width=int(ENTRY_WIDTH/1.059), state='readonly')
        self.box['values'] = ('Direktverkande el', 'Direktverkande el + värmepump', 'Pellets', 'Berg- eller jordvärme')
        self.box.current(0)
        self.box.configure(background=WHITE, foreground=FG)
        self.box.grid(row=15, column=0, padx=10, pady=(0, 5), sticky='SW')

        # Get change of dropdown list
        self.box_value.trace('w', self.change_dropdown)

        # Fastighetsskatt
        self.taxroof = self.draw_text(self.left_frame, 'Tak för fastighetsskatt:', TEXT_FONT, TEXT_SIZE, 16, 0, TAXROOF_, 'enabled')

        # Title
        tk.Label(self.left_frame, text='Engångskostnader', font=(TITLE_FONT, TITLE_SIZE, 'underline', 'bold'), bg=BG, fg=FG).grid(row=18, column=0, pady=(30, 10), sticky='SW')

        # Besiktning
        self.checkup = self.draw_text(self.left_frame, 'Besiktning :', TEXT_FONT, TEXT_SIZE, 20, 0, CHECKUP_, 'enabled')

        # Uppläggningsavgift lån
        self.interestprice = self.draw_text(self.left_frame, 'Uppläggningsavgift lån:', TEXT_FONT, TEXT_SIZE, 22, 0, INTERESTPRICE_, 'enabled')

        # Mäklararvode
        self.broker = self.draw_text(self.left_frame, 'Mäklararvode:', TEXT_FONT, TEXT_SIZE, 24, 0, BROKER_, 'enabled')

        # Pantbrev
        self.pant = self.draw_text(self.left_frame, 'Storlek på existerande pantbrev:', TEXT_FONT, TEXT_SIZE, 26, 0, PANT_, 'enabled')
        

# --------- Middle Frame ----------------------------------------------------------------

        # Title
        tk.Label(self.middle_frame, text='Övriga avgifter', font=(TITLE_FONT, TITLE_SIZE, 'underline', 'bold'), bg=BG, fg=FG).grid(row=0, column=0, pady=10, sticky='SW')

        # Underhållskostnad
        self.maintenance = self.draw_text(self.middle_frame, 'Underhållskostnad:', TEXT_FONT, TEXT_SIZE, 2, 0, MAINTENANCE_H_, 'enabled')

        # Tomträttsavgäld
        self.tomtgald = self.draw_text(self.middle_frame, 'Tomträttsavgäld:', TEXT_FONT, TEXT_SIZE, 4, 0, TOMTGALD_, 'enabled')

        # Bredband
        self.broadband = self.draw_text(self.middle_frame, 'Bredband:', TEXT_FONT, TEXT_SIZE, 6, 0, BROADBAND_, 'enabled')

        # TV/Telefoni
        self.tv = self.draw_text(self.middle_frame, 'TV/Telefoni:', TEXT_FONT, TEXT_SIZE, 8, 0, TV_, 'enabled')

        # Föreningsavgifter och liknande
        self.forening = self.draw_text(self.middle_frame, 'Föreningsavgifter:', TEXT_FONT, TEXT_SIZE, 10, 0, FORENING_, 'enabled')

        # Hemförsäkring
        self.forsakring = self.draw_text(self.middle_frame, 'Hemförsäkring:', TEXT_FONT, TEXT_SIZE, 12, 0, FORSAKRING_, 'enabled')

        # Sophämtning
        self.garbage = self.draw_text(self.middle_frame, 'Sophämtning:', TEXT_FONT, TEXT_SIZE, 14, 0, GARBAGE_, 'enabled')

        # Anslutning vatten/avlopp
        self.water = self.draw_text(self.middle_frame, 'Anslutningsavgift vatten/avlopp:', TEXT_FONT, TEXT_SIZE, 16, 0, WATER_, 'enabled')        

        # Hemlarm
        self.alarm = self.draw_text(self.middle_frame, 'Hemlarm:', TEXT_FONT, TEXT_SIZE, 18, 0, ALARM_H_, 'enabled')

        # Övriga löpande avgifter
        self.ovrigt = self.draw_text(self.middle_frame, 'Övriga löpande utgifter:', TEXT_FONT, TEXT_SIZE, 20, 0, OVRIGT_, 'enabled')

        # Calculation button
        b = tk.Button(self.middle_frame, text='Beräkna', bg=WHITE, activebackground=WHITE, command=self.calculate)
        b['font'] = self.font
        b.grid(row=22, column=0, pady = (30, 0), padx=10, sticky='S')
        
        back = tk.Button(self.middle_frame, text='Tillbaka', bg=WHITE, activebackground=WHITE, command=self.back_main)
        back['font'] = self.font2
        back.grid(row=23, column=0, pady = (15, 0), padx=10, sticky='S')


# --------- Place frames ----------------------------------------------------------------
        
        self.left_frame.grid(row=0, column=0, padx = (10, 0), sticky='N')
        self.middle_frame.grid(row=0, column=1, sticky='N')
        
# ------- Draw text ---------------------------------------------------------------------

    def draw_text(self, frame, text, font, size, row, col, placeholder, state):
        tk.Label(frame, text=text, font=(font, size), bg=BG, fg=FG).grid(row=row, column=col, sticky='SW', padx=10, pady=(5, 0))
        entry = ttk.Entry(frame, width=ENTRY_WIDTH)
        entry.insert(0, placeholder)
        entry.config(foreground=BLACK, state=state)
        entry.grid(row=row+1, column=col, padx=10, pady=(0, 5), sticky='SW')

        return entry

# -------------------------------------------------------
# Calculation
# -------------------------------------------------------

    def calculate(self):

        # Calculate heating
        heating_cost = [28.8, 23.04, 19.296, 12.96]  # Heating price per m^2 for corresponding values in drop down list.
        for i in range(len(self.box['values'])):
            if self.box_value.get() == self.box['values'][i]:
                heating = heating_cost[i] * float(self.space.get())  # Heating cost for house

        # Calculate water and electricity consumption
        water = 90 + 139.5 * int(self.antal.get())
        electricity = 90 + 172 * int(self.antal.get())

        # Lagfart and pantbrev (https://www.svenskfast.se/guider/pantbrev-lagfart/)
        lagfart = 825 + 0.015 * float(self.price.get())
        pantbrev = max(0, (float(self.deposit.get()) - float(self.pant.get())) * 0.02 + 375)

        # Amortering, https://www.lansforsakringar.se/jonkoping/privat/bank/lana/bolan/amortering/?gclid=Cj0KCQjww47nBRDlARIsAEJ34bkgh-3oXmZk_udVqMUd8Uscc8HHaqGoT-YrdkdXSJN9kO3RSOflfDgaAvLNEALw_wcB&gclsrc=aw.ds
        quota = 1 - (int(self.price.get()) - int(self.deposit.get())) / int(self.price.get())
        if quota > 0.7:
            amortering = float(self.deposit.get()) * 0.02 / 12
        if 0.5 < quota <= 0.7:
            amortering = float(self.deposit.get()) * 0.01 / 12
        if quota <= 0.5:
            amortering = 0

        # Percentages calculation
        brokerfee = self.broker.get()
        brokerfee = brokerfee.replace(',', '.')
        broker_fee = float(brokerfee) / 100 * float(self.price.get())
        
        interestrate = self.interest.get()
        interestrate = interestrate.replace(',', '.')
        loan_fee = float(interestrate) / 100 * float(self.deposit.get()) / 12

        # Fastighetsskatt
        fastighetsskatt = min(float(self.taxroof.get()), 0.0075 * float(self.price.get())) / 12

        # Skatteavdrag
        if loan_fee * 12 > 100000:
            skatteavdrag1 = -100000 * 0.3 / 12
            skatteavdrag2 = -((loan_fee * 12) - 100000) * 0.21 / 12
            skatteavdrag = skatteavdrag1 + skatteavdrag2
        else:
            skatteavdrag = -loan_fee * 0.3  

        # Totalt
        # Engångs per månad
        engangs = (float(self.checkup.get()) + float(self.interestprice.get()) + broker_fee + lagfart + pantbrev) / float(self.years.get()) / 12
    
        # Löpande utan amortering
        lopande = loan_fee + fastighetsskatt + float(self.tomtgald.get()) + float(self.maintenance.get()) + float(self.broadband.get()) + float(self.tv.get()) + float(self.forening.get()) + float(self.forsakring.get()) + float(self.garbage.get()) + float(self.water.get()) + float(self.alarm.get()) + electricity + heating + water

        # Löpande med amortering
        lopande_amortering = lopande + amortering

        # Totalt
        totalt = engangs + lopande_amortering + skatteavdrag

        # Draw result on screen
        self.draw_results(lagfart, pantbrev, heating, water, electricity, amortering, fastighetsskatt, totalt, engangs, lopande, lopande_amortering, loan_fee, broker_fee, skatteavdrag)


# -------------------------------------------------------
# Extra functions
# -------------------------------------------------------

    def back_main(self):
        # Get position
        maxW = self.window.winfo_screenwidth()
        maxH = self.window.winfo_screenheight()

        self.init_x = min(maxW, self.window.winfo_x() + (WIDTH/2 - WIDTH/2/2))
        self.init_y = min(maxH, self.window.winfo_y() + (HEIGHT/2 - HEIGHT/1.8/2))
        
        self.window.destroy()
        main(tk.Tk(), self.init_x, self.init_y)

    def change_dropdown(self, *args):
        self.heating = self.box_value.get()

    def quit_func(self):
        self.window.destroy()

    def expl_menu(self):
        # Get position
        maxW = self.window.winfo_screenwidth()
        maxH = self.window.winfo_screenheight()

        x = self.window.winfo_x() + (WIDTH/2 - WIDTH/2/2)
        y = min(maxH, self.window.winfo_y() + (HEIGHT/2 - HEIGHT/1.8/2))

        expl_window(x, y)
            

# -------------------------------------------------------
# Draw
# -------------------------------------------------------  

    def draw_results(self, lagfart, pantbrev, heating, water, electricity, amortering, fastighetsskatt, totalt, engangs, lopande, lopande_amortering, loan_fee, broker_fee, skatteavdrag):               

        self.right_frame.destroy()
        self.right_frame = tk.Frame(self.window, bg=WHITE, bd=3, relief='sunken')

        paddx = 10  # Padding left/right on results canvas

        # Engångskostnader
        tk.Label(self.right_frame, text='Engångskostnader', font=(TITLE_FONT, TITLE_SIZE, 'underline', 'bold'), bg=WHITE, fg=FG).grid(row=0, column=0, sticky='NW', padx=paddx, pady=(15, 2))

        text_engangs = ['Lagfart', str('{:,d}'.format(round(lagfart))) + '  kr', 'Pantbrev', str('{:,d}'.format(round(pantbrev))) + '  kr', 'Mäklararvode', str('{:,d}'.format(round(broker_fee))) + '  kr']
        for i in range(int(len(text_engangs)/2)):
            tk.Label(self.right_frame, text=text_engangs[2*i], font=(TEXT_FONT, TEXT_SIZE), bg=WHITE, fg=FG).grid(row=i+1, column=0, sticky='SW', padx=paddx, pady=(5, 0))
            tk.Label(self.right_frame, text=text_engangs[2*i+1], font=(TEXT_FONT, TEXT_SIZE), bg=WHITE, fg=FG).grid(row=i+1, column=1, sticky='SE', padx=paddx, pady=(5, 0))
        
        # Löpande utgifter
        start_row = int(len(text_engangs)/2) + 1
        tk.Label(self.right_frame, text='Löpande utgifter', font=(TITLE_FONT, TITLE_SIZE, 'underline', 'bold'), bg=WHITE, fg=FG).grid(row=start_row, column=0, sticky='NW', padx=paddx, pady=(15, 2))
        
        text_lopande = ['Uppvärmning', str('{:,d}'.format(round(heating))) + '  kr/mån', 'Hushållsel', str('{:,d}'.format(round(electricity))) + '  kr/mån', 'Vattenförbrukning', str('{:,d}'.format(round(water))) + '  kr/mån']
        for i in range(int(len(text_lopande)/2)):
            tk.Label(self.right_frame, text=text_lopande[2*i], font=(TEXT_FONT, TEXT_SIZE), bg=WHITE, fg=FG).grid(row=start_row + i + 1, column=0, sticky='SW', padx=paddx, pady=(5, 0))
            tk.Label(self.right_frame, text=text_lopande[2*i+1], font=(TEXT_FONT, TEXT_SIZE), bg=WHITE, fg=FG).grid(row=start_row + i + 1, column=1, sticky='SE', padx=paddx, pady=(5, 0))       

        # Lån och skatt
        start_row = int(len(text_engangs)/2) + int(len(text_lopande)/2) + 2
        tk.Label(self.right_frame, text='Lån och skatter', font=(TITLE_FONT, TITLE_SIZE, 'underline', 'bold'), bg=WHITE, fg=FG).grid(row=start_row, column=0, sticky='NW', padx=paddx, pady=(15, 2))
        
        text_loan = ['Lån', str('{:,d}'.format(round(loan_fee))) + '  kr/mån', 'Amorteringskrav', str('{:,d}'.format(round(amortering))) + '  kr/mån', 'Fastighetsskatt', str('{:,d}'.format(round(fastighetsskatt))) + '  kr/mån']
        for i in range(int(len(text_loan)/2)):
            tk.Label(self.right_frame, text=text_loan[2*i], font=(TEXT_FONT, TEXT_SIZE), bg=WHITE, fg=FG).grid(row=start_row + i + 1, column=0, sticky='SW', padx=paddx, pady=(5, 0))
            tk.Label(self.right_frame, text=text_loan[2*i+1], font=(TEXT_FONT, TEXT_SIZE), bg=WHITE, fg=FG).grid(row=start_row + i + 1, column=1, sticky='SE', padx=paddx, pady=(5, 0))       

        # Totalt
        start_row = int(len(text_engangs)/2) + int(len(text_lopande)/2) + int(len(text_loan)/2) + 3
        tk.Label(self.right_frame, text='Sammanställning', font=(TITLE_FONT, TITLE_SIZE, 'underline', 'bold'), bg=WHITE, fg=FG).grid(row=start_row, column=0, sticky='NW', padx=paddx, pady=(15, 2))

        text_totalt = ['Engångskostnader', str('{:,d}'.format(round(engangs))) + '  kr/mån', 'Löpande utgifter', str('{:,d}'.format(round(lopande) - round(loan_fee))) + '  kr/mån', 'Lån & amortering', str('{:,d}'.format(round(loan_fee) + round(amortering))) + '  kr/mån', 'Skatteavdrag', str('{:,d}'.format(round(skatteavdrag))) + '  kr/mån', '___________________', ' ', 'Totalt', str('{:,d}'.format(round(totalt))) + '  kr/mån']
        for i in range(int(len(text_totalt)/2)):
            if i < int(len(text_totalt)/2) - 1:
                tk.Label(self.right_frame, text=text_totalt[2*i], font=(TEXT_FONT, TEXT_SIZE), bg=WHITE, fg=FG).grid(row=start_row + i + 1, column=0, sticky='SW', padx=paddx, pady=(5, 0))
                tk.Label(self.right_frame, text=text_totalt[2*i+1], font=(TEXT_FONT, TEXT_SIZE), bg=WHITE, fg=FG).grid(row=start_row + i + 1, column=1, sticky='SE', padx=paddx, pady=(5, 0))       
            else:
                tk.Label(self.right_frame, text=text_totalt[2*i], font=(TITLE_FONT, TITLE_SIZE - 1, 'bold'), bg=WHITE, fg=FG).grid(row=start_row + i + 1, column=0, sticky='SW', padx=paddx, pady=(0, 15))
                tk.Label(self.right_frame, text=text_totalt[2*i+1], font=(TITLE_FONT, TITLE_SIZE - 1, 'bold'), bg=WHITE, fg=FG).grid(row=start_row + i + 1, column=1, sticky='SE', padx=paddx, pady=(0, 15))       

        
        # Place right frame
        self.right_frame.grid(row=0, column=2, padx=20, pady = 20, sticky='N')        

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Calc:

    def __init__(self, window, x, y):
        self.x = x
        self.y = y
        # Init screen
        self.window = window
        self.window.title(TITLE)
        self.window.iconbitmap(default=ICON_PATH)
        self.window.geometry('%dx%d+%d+%d' % (WIDTH, round(HEIGHT*0.85), max(0, self.x - (WIDTH/2 - WIDTH/2/2)), max(0, self.y - (HEIGHT/2 - HEIGHT/1.8/2))))
        self.window.configure(background=BG)

        locale.setlocale(locale.LC_ALL, '')

        self.font = font.Font(family='Helvetica', size=11)
        self.font2 = font.Font(family='Helvetica', size=9)

    def run(self):
        self.menu()
        self.text()

    def menu(self):
        # Menu bar
        menu = tk.Menu(self.window)
        self.window.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label='Start', menu=file_menu)
        file_menu.add_command(label='Huvudmeny', command=self.back_main)
        file_menu.add_separator()
        file_menu.add_command(label='Avsluta', command=self.quit_func)

        edit_menu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label='Hjälp', menu=edit_menu)
        edit_menu.add_command(label='Förklaringar', command=self.expl_menu)

        self.left_frame = tk.Frame(self.window, bg=LIGHTBLUE)
        self.middle_frame = tk.Frame(self.window, bg=LIGHTBLUE)
        self.bottom_frame = tk.Frame(self.window, bg=LIGHTBLUE)
        self.right_frame = tk.Frame(self.window, bg=WHITE, bd=3, relief='sunken')

    def text(self):

# --------- Left Frame ----------------------------------------------------------------

        # Title
        tk.Label(self.left_frame, text='Allmänt', font=(TITLE_FONT, TITLE_SIZE, 'underline', 'bold'), bg=BG, fg=FG).grid(row=0, column=0, pady=(20, 2), padx=10, sticky='SW')
      
        # Pris på bostad
        self.price = self.draw_text(self.left_frame, 'Pris på bostad:', TEXT_FONT, TEXT_SIZE, 2, 0, PRICE_, 'enabled')
        self.price.focus_set()

        # Månadsavgift
        self.manadsavgift = self.draw_text(self.left_frame, 'Månadsavgift:', TEXT_FONT, TEXT_SIZE, 4, 0, AVGIFT_, 'enabled')

        # Boyta
        self.space = self.draw_text(self.left_frame, 'Boyta:', TEXT_FONT, TEXT_SIZE, 6, 0, SPACE_, 'enabled')

        # Personer i hushållet
        self.antal = self.draw_text(self.left_frame, 'Personer i hushållet:', TEXT_FONT, TEXT_SIZE, 8, 0, ANTAL_, 'enabled') 

        # Storlek på lån
        self.deposit = self.draw_text(self.left_frame, 'Storlek på lån:', TEXT_FONT, TEXT_SIZE, 10, 0, DEPOSIT_, 'enabled')

        # Ränta på lån
        self.interest = self.draw_text(self.left_frame, 'Ränta på lån:', TEXT_FONT, TEXT_SIZE, 12, 0, INTEREST_, 'enabled')

        # Antal år att bo
        self.years = self.draw_text(self.left_frame, 'Antal år att bo:', TEXT_FONT, TEXT_SIZE, 14, 0, YEARS_, 'enabled')

        # Title
        tk.Label(self.left_frame, text='Engångskostnader', font=(TITLE_FONT, TITLE_SIZE, 'underline', 'bold'), bg=BG, fg=FG).grid(row=16, column=0, pady=(15, 2), padx=10, sticky='SW')

        # Besiktning
        self.checkup = self.draw_text(self.left_frame, 'Besiktning:', TEXT_FONT, TEXT_SIZE, 18, 0, CHECKUP_, 'enabled')

        # Uppläggningsavgift lån
        self.interestprice = self.draw_text(self.left_frame, 'Uppläggningsavgift lån:', TEXT_FONT, TEXT_SIZE, 20, 0, INTERESTPRICE_, 'enabled')

        # Mäklararvode
        self.broker = self.draw_text(self.left_frame, 'Mäklararvode:', TEXT_FONT, TEXT_SIZE, 22, 0, BROKER_, 'enabled')
        

# --------- Middle Frame ----------------------------------------------------------------

        # Title
        tk.Label(self.middle_frame, text='Övriga avgifter', font=(TITLE_FONT, TITLE_SIZE, 'underline', 'bold'), bg=BG, fg=FG).grid(row=0, column=0, pady=(20, 2), padx=10, sticky='SW')

        # Underhållskostnad
        self.maintenance = self.draw_text(self.middle_frame, 'Underhållskostnad:', TEXT_FONT, TEXT_SIZE, 2, 0, MAINTENANCE_, 'enabled')

        # Bredband
        self.broadband = self.draw_text(self.middle_frame, 'Bredband:', TEXT_FONT, TEXT_SIZE, 4, 0, BROADBAND_, 'enabled')

        # TV/Telefoni
        self.tv = self.draw_text(self.middle_frame, 'TV/Telefoni:', TEXT_FONT, TEXT_SIZE, 6, 0, TV_, 'enabled')

        # Hemförsäkring
        self.forsakring = self.draw_text(self.middle_frame, 'Hemförsäkring:', TEXT_FONT, TEXT_SIZE, 8, 0, FORSAKRING_, 'enabled')    

        # Övriga kostnader
        self.alarm = self.draw_text(self.middle_frame, 'Övriga löpande utgifter:', TEXT_FONT, TEXT_SIZE, 10, 0, OVRIGT_, 'enabled')        

        # Calculation and back buttons
        b = tk.Button(self.middle_frame, text='Beräkna', bg=WHITE, activebackground=WHITE, command=self.calculate)
        b['font'] = self.font
        b.grid(row=20, column=0, pady = (30, 0), padx=10, sticky='S')
        
        back = tk.Button(self.middle_frame, text='Tillbaka', bg=WHITE, activebackground=WHITE, command=self.back_main)
        back['font'] = self.font2
        back.grid(row=21, column=0, pady = (15, 0), padx=10, sticky='S')


# --------- Place frames ----------------------------------------------------------------
        
        self.left_frame.grid(row=0, column=0, padx = 10, sticky='N')
        self.middle_frame.grid(row=0, column=1, sticky='N')
        
# ------- Draw text ---------------------------------------------------------------------

    def draw_text(self, frame, text, font, size, row, col, placeholder, state):
        tk.Label(frame, text=text, font=(font, size), bg=BG, fg=FG).grid(row=row, column=col, sticky='SW', padx=10, pady=(5, 0))
        entry = ttk.Entry(frame, width=ENTRY_WIDTH)
        entry.insert(0, placeholder)
        entry.config(foreground=BLACK, state=state)
        entry.grid(row=row+1, column=col, padx=10, pady=(0, 5), sticky='SW')

        return entry

# -------------------------------------------------------
# Calculation
# -------------------------------------------------------

    def calculate(self):

        # Calculate electricity consumption
        electricity = 90 + 172 * int(self.antal.get())

        # Amortering, https://www.lansforsakringar.se/jonkoping/privat/bank/lana/bolan/amortering/?gclid=Cj0KCQjww47nBRDlARIsAEJ34bkgh-3oXmZk_udVqMUd8Uscc8HHaqGoT-YrdkdXSJN9kO3RSOflfDgaAvLNEALw_wcB&gclsrc=aw.ds
        quota = 1 - (int(self.price.get()) - int(self.deposit.get())) / int(self.price.get())
        if quota > 0.7:
            amortering = float(self.deposit.get()) * 0.02 / 12
        if 0.5 < quota <= 0.7:
            amortering = float(self.deposit.get()) * 0.01 / 12
        if quota <= 0.5:
            amortering = 0

        # TV, bredband och telefoni
        self.tbt = float(self.broadband.get()) + float(self.tv.get())

        # Percentages calculation (replace , with . in case user uses that as separator)
        brokerfee = self.broker.get()
        brokerfee = brokerfee.replace(',', '.')

        if float(brokerfee) > 100:
            broker_fee = float(brokerfee)
        else:
            broker_fee = float(brokerfee) / 100 * float(self.price.get())
        
        interestrate = self.interest.get()
        interestrate = interestrate.replace(',', '.')
        loan_fee = float(interestrate) / 100 * float(self.deposit.get()) / 12

        # Månadsavgift
        manadsavgift = float(self.manadsavgift.get())

        # Skatteavdrag
        if loan_fee * 12 > 100000:
            skatteavdrag1 = -100000 * 0.3 / 12
            skatteavdrag2 = -((loan_fee * 12) - 100000) * 0.21 / 12
            skatteavdrag = skatteavdrag1 + skatteavdrag2
        else:
            skatteavdrag = -loan_fee * 0.3

        # Totalt
        # Engångs per månad
        engangs = (float(self.checkup.get()) + float(self.interestprice.get()) + broker_fee) / float(self.years.get()) / 12
    
        # Löpande utan amortering
        lopande = loan_fee + manadsavgift + float(self.maintenance.get()) + float(self.broadband.get()) + float(self.tv.get()) + float(self.forsakring.get()) + float(self.alarm.get()) + electricity

        # Löpande med amortering
        lopande_amortering = lopande + amortering

        # Totalt
        totalt = engangs + lopande_amortering + skatteavdrag

        # Draw result on screen
        self.draw_results(electricity, amortering, totalt, engangs, lopande, lopande_amortering, loan_fee, broker_fee, skatteavdrag)


# -------------------------------------------------------
# Extra functions
# -------------------------------------------------------

    def back_main(self):
        # Get position
        maxW = self.window.winfo_screenwidth()
        maxH = self.window.winfo_screenheight()

        self.init_x = min(maxW, self.window.winfo_x() + (WIDTH/2 - WIDTH/2/2))
        self.init_y = min(maxH, self.window.winfo_y() + (HEIGHT/2 - HEIGHT/1.8/2))
        
        self.window.destroy()
        main(tk.Tk(), self.init_x, self.init_y)

    def new_calc(self):
        pass

    def quit_func(self):
        self.window.destroy()

    def expl_menu(self):
        # Get position
        maxW = self.window.winfo_screenwidth()
        maxH = self.window.winfo_screenheight()

        x = self.window.winfo_x() + (WIDTH/2 - WIDTH/2/2)
        y = min(maxH, self.window.winfo_y() + (HEIGHT/2 - HEIGHT/1.8/2))

        expl_window(x, y)
        
# -------------------------------------------------------
# Draw
# -------------------------------------------------------  

    def draw_results(self, electricity, amortering, totalt, engangs, lopande, lopande_amortering, loan_fee, broker_fee, skatteavdrag):               

        self.right_frame.destroy()
        self.right_frame = tk.Frame(self.window, bg=WHITE, bd=3, relief='sunken')

        paddx = 10  # Padding left/right on results canvas

        # Engångskostnader
        tk.Label(self.right_frame, text='Engångskostnader', font=(TITLE_FONT, TITLE_SIZE, 'underline', 'bold'), bg=WHITE, fg=FG).grid(row=0, column=0, sticky='NW', padx=paddx, pady=(15, 2))

        text_engangs = ['Mäklararvode', str('{:,d}'.format(round(broker_fee))) + '  kr']
        for i in range(int(len(text_engangs)/2)):
            tk.Label(self.right_frame, text=text_engangs[2*i], font=(TEXT_FONT, TEXT_SIZE), bg=WHITE, fg=FG).grid(row=i+1, column=0, sticky='SW', padx=paddx, pady=(5, 0))
            tk.Label(self.right_frame, text=text_engangs[2*i+1], font=(TEXT_FONT, TEXT_SIZE), bg=WHITE, fg=FG).grid(row=i+1, column=1, sticky='SE', padx=paddx, pady=(5, 0))
        
        # Löpande utgifter
        start_row = int(len(text_engangs)/2) + 1
        tk.Label(self.right_frame, text='Löpande utgifter', font=(TITLE_FONT, TITLE_SIZE, 'underline', 'bold'), bg=WHITE, fg=FG).grid(row=start_row, column=0, sticky='NW', padx=paddx, pady=(15, 2))
        
        text_lopande = ['Hushållsel', str('{:,d}'.format(round(electricity))) + '  kr/mån', 'TV/Bredband/Telefoni', str('{:,d}'.format(round(self.tbt))) + '  kr/mån']
        for i in range(int(len(text_lopande)/2)):
            tk.Label(self.right_frame, text=text_lopande[2*i], font=(TEXT_FONT, TEXT_SIZE), bg=WHITE, fg=FG).grid(row=start_row + i + 1, column=0, sticky='SW', padx=paddx, pady=(5, 0))
            tk.Label(self.right_frame, text=text_lopande[2*i+1], font=(TEXT_FONT, TEXT_SIZE), bg=WHITE, fg=FG).grid(row=start_row + i + 1, column=1, sticky='SE', padx=paddx, pady=(5, 0))       

        # Lån och amortering
        start_row = int(len(text_engangs)/2) + int(len(text_lopande)/2) + 2
        tk.Label(self.right_frame, text='Lån och amortering', font=(TITLE_FONT, TITLE_SIZE, 'underline', 'bold'), bg=WHITE, fg=FG).grid(row=start_row, column=0, sticky='NW', padx=paddx, pady=(15, 2))
        
        text_loan = ['Lån', str('{:,d}'.format(round(loan_fee))) + '  kr/mån', 'Amorteringskrav', str('{:,d}'.format(round(amortering))) + '  kr/mån']
        for i in range(int(len(text_loan)/2)):
            tk.Label(self.right_frame, text=text_loan[2*i], font=(TEXT_FONT, TEXT_SIZE), bg=WHITE, fg=FG).grid(row=start_row + i + 1, column=0, sticky='SW', padx=paddx, pady=(5, 0))
            tk.Label(self.right_frame, text=text_loan[2*i+1], font=(TEXT_FONT, TEXT_SIZE), bg=WHITE, fg=FG).grid(row=start_row + i + 1, column=1, sticky='SE', padx=paddx, pady=(5, 0))       

        # Totalt
        start_row = int(len(text_engangs)/2) + int(len(text_lopande)/2) + int(len(text_loan)/2) + 3
        tk.Label(self.right_frame, text='Sammanställning', font=(TITLE_FONT, TITLE_SIZE, 'underline', 'bold'), bg=WHITE, fg=FG).grid(row=start_row, column=0, sticky='NW', padx=paddx, pady=(15, 2))

        text_totalt = ['Engångskostnader', str('{:,d}'.format(round(engangs))) + '  kr/mån', 'Löpande utgifter', str('{:,d}'.format(round(lopande) - round(loan_fee))) + '  kr/mån', 'Lån & amortering', str('{:,d}'.format(round(loan_fee) + round(amortering))) + '  kr/mån', 'Skatteavdrag', str('{:,d}'.format(round(skatteavdrag))) + '  kr/mån', '___________________', ' ', 'Totalt', str('{:,d}'.format(round(totalt))) + '  kr/mån']
        for i in range(int(len(text_totalt)/2)):
            if i < int(len(text_totalt)/2) - 1:
                tk.Label(self.right_frame, text=text_totalt[2*i], font=(TEXT_FONT, TEXT_SIZE), bg=WHITE, fg=FG).grid(row=start_row + i + 1, column=0, sticky='SW', padx=paddx, pady=(5, 0))
                tk.Label(self.right_frame, text=text_totalt[2*i+1], font=(TEXT_FONT, TEXT_SIZE), bg=WHITE, fg=FG).grid(row=start_row + i + 1, column=1, sticky='SE', padx=paddx, pady=(5, 0))       
            else:
                tk.Label(self.right_frame, text=text_totalt[2*i], font=(TITLE_FONT, TITLE_SIZE - 1, 'bold'), bg=WHITE, fg=FG).grid(row=start_row + i + 1, column=0, sticky='SW', padx=paddx, pady=(0, 15))
                tk.Label(self.right_frame, text=text_totalt[2*i+1], font=(TITLE_FONT, TITLE_SIZE - 1, 'bold'), bg=WHITE, fg=FG).grid(row=start_row + i + 1, column=1, sticky='SE', padx=paddx, pady=(0, 15))       

        
        # Place right frame
        self.right_frame.grid(row=0, column=2, padx=20, pady = 20, sticky='N')

# -------------------------------------------------------
# Draw helper window
# -------------------------------------------------------

def expl_window(x, y):
    Expl(x, y)

# -------------------------------------------------------
# Main program
# -------------------------------------------------------
def main(window, x, y):

    Start(window, x, y).run()
    window.mainloop()
    
# -------------------------------------------------------
# Run
# -------------------------------------------------------

if __name__ == "__main__":
    window = tk.Tk()

    # Get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate position x and y coordinates
    x = (screen_width/2) - (WIDTH/2/2)
    y = (screen_height/2) - (HEIGHT/2/1.8)

    # Transparent icon
    global ICON_PATH
    _, ICON_PATH = tempfile.mkstemp()
    with open(ICON_PATH, 'wb') as icon_file:
        icon_file.write(ICON)
    
    main(window, x, y)

