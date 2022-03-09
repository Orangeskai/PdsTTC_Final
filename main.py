from distutils import core
from this import d
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

#Untuk menentukan siapa yang main dulu (player 1 atau player 2)
KLIK = True
#Untuk menyimpan progress permainan
COUNT = 0

def start():
    """
    0 1 2 3
    1
    2
    3
    """
    #Cek jenis sistem
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

    #Untuk menyimpan progress permainan
    def tekan(tombol_yang_ditekan):
        global KLIK, COUNT
        if KLIK == True:
            if tombol_yang_ditekan == 1:
                b1.set("1")
                s1['state'] = 'disabled'
            elif tombol_yang_ditekan == 2:
                b2.set("1")
                s2['state'] = 'disabled'
            elif tombol_yang_ditekan == 3:
                b3.set("1")
                s3['state'] = 'disabled'
            elif tombol_yang_ditekan == 4:
                b4.set("1")
                s4['state'] = 'disabled'
            elif tombol_yang_ditekan == 5:
                b5.set("1")
                s5['state'] = 'disabled'
            elif tombol_yang_ditekan == 6:
                b6.set("1")
                s6['state'] = 'disabled'
            elif tombol_yang_ditekan == 7:
                b7.set("1")
                s7['state'] = 'disabled'
            elif tombol_yang_ditekan == 8:
                b8.set("1")
                s8['state'] = 'disabled'
            elif tombol_yang_ditekan == 9:
                b9.set("1")
                s9['state'] = 'disabled'
            elif tombol_yang_ditekan == 10:
                b10.set("1")
                s10['state'] = 'disabled'
            elif tombol_yang_ditekan == 11:
                b11.set("1")
                s11['state'] = 'disabled'
            elif tombol_yang_ditekan == 12:
                b12.set("1")
                s12['state'] = 'disabled'
            elif tombol_yang_ditekan == 13:
                b13.set("1")
                s13['state'] = 'disabled'
            elif tombol_yang_ditekan == 14:
                b14.set("1")
                s14['state'] = 'disabled'
            elif tombol_yang_ditekan == 15:
                b15.set("1")
                s15['state'] = 'disabled'
            elif tombol_yang_ditekan == 16:
                b16.set("1")
                s16['state'] = 'disabled'
            COUNT += 1
            KLIK = False
            cekmenang()
        
        else:
            if tombol_yang_ditekan == 1:
                b1.set("0")
                s1['state'] = 'disabled'
            elif tombol_yang_ditekan == 2:
                b2.set("0")
                s2['state'] = 'disabled'
            elif tombol_yang_ditekan == 3:
                b3.set("0")
                s3['state'] = 'disabled'
            elif tombol_yang_ditekan == 4:
                b4.set("0")
                s4['state'] = 'disabled'
            elif tombol_yang_ditekan == 5:
                b5.set("0")
                s5['state'] = 'disabled'
            elif tombol_yang_ditekan == 6:
                b6.set("0")
                s6['state'] = 'disabled'
            elif tombol_yang_ditekan == 7:
                b7.set("0")
                s7['state'] = 'disabled'
            elif tombol_yang_ditekan == 8:
                b8.set("0")
                s8['state'] = 'disabled'
            elif tombol_yang_ditekan == 9:
                b9.set("0")
                s9['state'] = 'disabled'
            elif tombol_yang_ditekan == 10:
                b10.set("0")
                s10['state'] = 'disabled'
            elif tombol_yang_ditekan == 11:
                b11.set("0")
                s11['state'] = 'disabled'
            elif tombol_yang_ditekan == 12:
                b12.set("0")
                s12['state'] = 'disabled'
            elif tombol_yang_ditekan == 13:
                b13.set("0")
                s13['state'] = 'disabled'
            elif tombol_yang_ditekan == 14:
                b14.set("0")
                s14['state'] = 'disabled'
            elif tombol_yang_ditekan == 15:
                b15.set("0")
                s15['state'] = 'disabled'
            elif tombol_yang_ditekan == 16:
                b16.set("0")
                s16['state'] = 'disabled'
            COUNT += 1
            KLIK = True
            cekmenang()

def cekmenang():
    global COUNT, KLIK
    print(COUNT) #untuk mengetahui jumlah klik
    """
    |-----------|
    |1 |2 |3 |4 |
    |5 |6 |7 |8 |
    |9 |10|11|12|
    |13|14|15|16|
    |-----------|
    """

    if(
        # Player 1 menang
        # Horizontal
        b1.get() == '1' and b2.get() == '1' and b3.get() == '1' and b4.get() == '1' or
        b5.get() == '1' and b6.get() == '1' and b7.get() == '1' and b8.get() == '1' or
        b9.get() == '1' and b10.get() == '1' and b11.get() == '1' and b12.get() == '1' or
        b13.get() == '1' and b14.get() == '1' and b15.get() == '1' and b16.get() == '1' or
        # Vertical
        b1.get() == '1' and b5.get() == '1' and b9.get() == '1' and b13.get() == '1' or
        b2.get() == '1' and b6.get() == '1' and b10.get() == '1' and b14.get() == '1' or
        b3.get() == '1' and b7.get() == '1' and b11.get() == '1' and b15.get() == '1' or
        b4.get() == '1' and b8.get() == '1' and b12.get() == '1' and b16.get() == '1' or
        # Diagonal
        b1.get() == '1' and b6.get() == '1' and b11.get() == '1' and b16.get() == '1' or
        b4.get() == '1' and b7.get() == '1' and b10.get() == '1' and b13.get() == '1'
        ):
        coret()
        pesan_menang(1)
        COUNT = 0
        KLIK = True
        kosongkan()

    elif(
        # Player 2 Menang
        # Horizontal
        b1.get() == '0' and b2.get() == '0' and b3.get() == '0' and b4.get() == '0' or
        b5.get() == '0' and b6.get() == '0' and b7.get() == '0' and b8.get() == '0' or
        b9.get() == '0' and b10.get() == '0' and b11.get() == '0' and b12.get() == '0' or
        b13.get() == '0' and b14.get() == '0' and b15.get() == '0' and b16.get() == '0' or
        # Vertical
        b1.get() == '0' and b5.get() == '0' and b9.get() == '0' and b13.get() == '0' or
        b2.get() == '0' and b6.get() == '0' and b10.get() == '0' and b14.get() == '0' or
        b3.get() == '0' and b7.get() == '0' and b11.get() == '0' and b15.get() == '0' or
        b4.get() == '0' and b8.get() == '0' and b12.get() == '0' and b16.get() == '0' or
        # Diagonal
        b1.get() == '0' and b6.get() == '0' and b11.get() == '0' and b16.get() == '0' or
        b4.get() == '0' and b7.get() == '0' and b10.get() == '0' and b13.get() == '0'
    ):
        coret()
        pesan_menang(0)
        COUNT = 0
        KLIK = True
        kosongkan()
    
    elif COUNT == 16:
        pesan_seri()
        COUNT = 0
        KLIK = True
        kosongkan()

def coret():
    pass
def pesan_seri():
    print("Seri")
def pesan_menang():
    print("Menang")
def kosongkan():
    pass

start()
root.mainloop()