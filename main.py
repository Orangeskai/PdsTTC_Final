from tkinter import Tk, StringVar, Button
from config import *
import os

root = Tk()
root.title(JUDUL)
root.resizable(False, False)
root.configure(background=BGWINDOW)

b1 = StringVar(value='')
b2 = StringVar(value='')
b3 = StringVar(value='')
b4 = StringVar(value='')
b5 = StringVar(value='')
b6 = StringVar(value='')
b7 = StringVar(value='')
b8 = StringVar(value='')
b9 = StringVar(value='')
b10 = StringVar(value='')
b11 = StringVar(value='')
b12 = StringVar(value='')
b13 = StringVar(value='')
b14 = StringVar(value='')
b15 = StringVar(value='')
b16 = StringVar(value='')

def start():
    """
    0 1 2 3
    1
    2
    3
    """
    #cek jenis sistem
    if os.name == 'posix':
        LEBAR = 7
        #FONT = ("Dyuthi", 20, 'bold')
        #FONT = ("Avenir", 20, 'bold') 
        #FONT = ("Helvetica", 20, 'bold')

    s1 = Button(root, height = TINGGI, width = LEBAR, font = FONT, relief = RELIEF, bg = BGTOMBOL, textvariable = b1, command = lambda: tekan(1), disabledforeground = BGTOMBOL_DITEKAN)
    s1.grid(row = 0, column = 0, padx = PADDINGX, pady = PADDINGY)
    s2 = Button(root, height = TINGGI, width = LEBAR, font = FONT, relief = RELIEF, bg = BGTOMBOL, textvariable = b2, command = lambda: tekan(2), disabledforeground = BGTOMBOL_DITEKAN)
    s2.grid(row = 0, column = 1, padx = PADDINGX, pady = PADDINGY)
    s3 = Button(root, height = TINGGI, width = LEBAR, font = FONT, relief = RELIEF, bg = BGTOMBOL, textvariable = b3, command = lambda: tekan(3), disabledforeground = BGTOMBOL_DITEKAN)
    s3.grid(row = 0, column = 2, padx = PADDINGX, pady = PADDINGY)
    s4 = Button(root, height = TINGGI, width = LEBAR, font = FONT, relief = RELIEF, bg = BGTOMBOL, textvariable = b4, command = lambda: tekan(4), disabledforeground = BGTOMBOL_DITEKAN)
    s4.grid(row = 0, column = 3, padx = PADDINGX, pady = PADDINGY)
    s5 = Button(root, height = TINGGI, width = LEBAR, font = FONT, relief = RELIEF, bg = BGTOMBOL, textvariable = b5, command = lambda: tekan(5), disabledforeground = BGTOMBOL_DITEKAN)
    s5.grid(row = 1, column = 0, padx = PADDINGX, pady = PADDINGY)
    s6 = Button(root, height = TINGGI, width = LEBAR, font = FONT, relief = RELIEF, bg = BGTOMBOL, textvariable = b6, command = lambda: tekan(6), disabledforeground = BGTOMBOL_DITEKAN)
    s6.grid(row = 1, column = 1, padx = PADDINGX, pady = PADDINGY)
    s7 = Button(root, height = TINGGI, width = LEBAR, font = FONT, relief = RELIEF, bg = BGTOMBOL, textvariable = b7, command = lambda: tekan(7), disabledforeground = BGTOMBOL_DITEKAN)
    s7.grid(row = 1, column = 2, padx = PADDINGX, pady = PADDINGY)
    s8 = Button(root, height = TINGGI, width = LEBAR, font = FONT, relief = RELIEF, bg = BGTOMBOL, textvariable = b8, command = lambda: tekan(8), disabledforeground = BGTOMBOL_DITEKAN)
    s8.grid(row = 1, column = 3, padx = PADDINGX, pady = PADDINGY)
    s9 = Button(root, height = TINGGI, width = LEBAR, font = FONT, relief = RELIEF, bg = BGTOMBOL, textvariable = b9, command = lambda: tekan(9), disabledforeground = BGTOMBOL_DITEKAN)
    s9.grid(row = 2, column = 0, padx = PADDINGX, pady = PADDINGY)
    s10 = Button(root, height = TINGGI, width = LEBAR, font = FONT, relief = RELIEF, bg = BGTOMBOL, textvariable = b10, command = lambda: tekan(10), disabledforeground = BGTOMBOL_DITEKAN)
    s10.grid(row = 2, column = 1, padx = PADDINGX, pady = PADDINGY)
    s11 = Button(root, height = TINGGI, width = LEBAR, font = FONT, relief = RELIEF, bg = BGTOMBOL, textvariable = b11, command = lambda: tekan(11), disabledforeground = BGTOMBOL_DITEKAN)
    s11.grid(row = 2, column = 2, padx = PADDINGX, pady = PADDINGY)
    s12 = Button(root, height = TINGGI, width = LEBAR, font = FONT, relief = RELIEF, bg = BGTOMBOL, textvariable = b12, command = lambda: tekan(12), disabledforeground = BGTOMBOL_DITEKAN)
    s12.grid(row = 2, column = 3, padx = PADDINGX, pady = PADDINGY)
    s13 = Button(root, height = TINGGI, width = LEBAR, font = FONT, relief = RELIEF, bg = BGTOMBOL, textvariable = b13, command = lambda: tekan(13), disabledforeground = BGTOMBOL_DITEKAN)
    s13.grid(row = 3, column = 0, padx = PADDINGX, pady = PADDINGY)
    s14 = Button(root, height = TINGGI, width = LEBAR, font = FONT, relief = RELIEF, bg = BGTOMBOL, textvariable = b14, command = lambda: tekan(14), disabledforeground = BGTOMBOL_DITEKAN)
    s14.grid(row = 3, column = 1, padx = PADDINGX, pady = PADDINGY)
    s15 = Button(root, height = TINGGI, width = LEBAR, font = FONT, relief = RELIEF, bg = BGTOMBOL, textvariable = b15, command = lambda: tekan(15), disabledforeground = BGTOMBOL_DITEKAN)
    s15.grid(row = 3, column = 2, padx = PADDINGX, pady = PADDINGY)
    s16 = Button(root, height = TINGGI, width = LEBAR, font = FONT, relief = RELIEF, bg = BGTOMBOL, textvariable = b16, command = lambda: tekan(16), disabledforeground = BGTOMBOL_DITEKAN)
    s16.grid(row = 3, column = 3, padx = PADDINGX, pady = PADDINGY)

    def tekan():
        pass

start()
root.mainloop()