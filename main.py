from tkinter import Tk, StringVar, Button
import konfig as kfg
import tkinter.messagebox as msgbox
import json, codecs, os
from random import randint

root = Tk()
root.title(kfg.JUDUL)
root.resizable(False, False)
root.configure(background=kfg.BGWINDOW)

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

if os.name == "posix":
    kfg.TINGGI = kfg.TINGGI + 1

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

    s1 = Button(root, height = kfg.TINGGI, width = kfg.LEBAR, font = kfg.FONT, relief = kfg.RELIEF, bg = kfg.BGTOMBOL, textvariable = b1, command = lambda: tekan(1), disabledforeground = kfg.BGTOMBOL_DITEKAN)
    s1.grid(row = 0, column = 0, padx = kfg.PADDINGX, pady = kfg.PADDINGY)
    s2 = Button(root, height = kfg.TINGGI, width = kfg.LEBAR, font = kfg.FONT, relief = kfg.RELIEF, bg = kfg.BGTOMBOL, textvariable = b2, command = lambda: tekan(2), disabledforeground = kfg.BGTOMBOL_DITEKAN)
    s2.grid(row = 0, column = 1, padx = kfg.PADDINGX, pady = kfg.PADDINGY)
    s3 = Button(root, height = kfg.TINGGI, width = kfg.LEBAR, font = kfg.FONT, relief = kfg.RELIEF, bg = kfg.BGTOMBOL, textvariable = b3, command = lambda: tekan(3), disabledforeground = kfg.BGTOMBOL_DITEKAN)
    s3.grid(row = 0, column = 2, padx = kfg.PADDINGX, pady = kfg.PADDINGY)
    s4 = Button(root, height = kfg.TINGGI, width = kfg.LEBAR, font = kfg.FONT, relief = kfg.RELIEF, bg = kfg.BGTOMBOL, textvariable = b4, command = lambda: tekan(4), disabledforeground = kfg.BGTOMBOL_DITEKAN)
    s4.grid(row = 0, column = 3, padx = kfg.PADDINGX, pady = kfg.PADDINGY)
    s5 = Button(root, height = kfg.TINGGI, width = kfg.LEBAR, font = kfg.FONT, relief = kfg.RELIEF, bg = kfg.BGTOMBOL, textvariable = b5, command = lambda: tekan(5), disabledforeground = kfg.BGTOMBOL_DITEKAN)
    s5.grid(row = 1, column = 0, padx = kfg.PADDINGX, pady = kfg.PADDINGY)
    s6 = Button(root, height = kfg.TINGGI, width = kfg.LEBAR, font = kfg.FONT, relief = kfg.RELIEF, bg = kfg.BGTOMBOL, textvariable = b6, command = lambda: tekan(6), disabledforeground = kfg.BGTOMBOL_DITEKAN)
    s6.grid(row = 1, column = 1, padx = kfg.PADDINGX, pady = kfg.PADDINGY)
    s7 = Button(root, height = kfg.TINGGI, width = kfg.LEBAR, font = kfg.FONT, relief = kfg.RELIEF, bg = kfg.BGTOMBOL, textvariable = b7, command = lambda: tekan(7), disabledforeground = kfg.BGTOMBOL_DITEKAN)
    s7.grid(row = 1, column = 2, padx = kfg.PADDINGX, pady = kfg.PADDINGY)
    s8 = Button(root, height = kfg.TINGGI, width = kfg.LEBAR, font = kfg.FONT, relief = kfg.RELIEF, bg = kfg.BGTOMBOL, textvariable = b8, command = lambda: tekan(8), disabledforeground = kfg.BGTOMBOL_DITEKAN)
    s8.grid(row = 1, column = 3, padx = kfg.PADDINGX, pady = kfg.PADDINGY)
    s9 = Button(root, height = kfg.TINGGI, width = kfg.LEBAR, font = kfg.FONT, relief = kfg.RELIEF, bg = kfg.BGTOMBOL, textvariable = b9, command = lambda: tekan(9), disabledforeground = kfg.BGTOMBOL_DITEKAN)
    s9.grid(row = 2, column = 0, padx = kfg.PADDINGX, pady = kfg.PADDINGY)
    s10 = Button(root, height = kfg.TINGGI, width = kfg.LEBAR, font = kfg.FONT, relief = kfg.RELIEF, bg = kfg.BGTOMBOL, textvariable = b10, command = lambda: tekan(10), disabledforeground = kfg.BGTOMBOL_DITEKAN)
    s10.grid(row = 2, column = 1, padx = kfg.PADDINGX, pady = kfg.PADDINGY)
    s11 = Button(root, height = kfg.TINGGI, width = kfg.LEBAR, font = kfg.FONT, relief = kfg.RELIEF, bg = kfg.BGTOMBOL, textvariable = b11, command = lambda: tekan(11), disabledforeground = kfg.BGTOMBOL_DITEKAN)
    s11.grid(row = 2, column = 2, padx = kfg.PADDINGX, pady = kfg.PADDINGY)
    s12 = Button(root, height = kfg.TINGGI, width = kfg.LEBAR, font = kfg.FONT, relief = kfg.RELIEF, bg = kfg.BGTOMBOL, textvariable = b12, command = lambda: tekan(12), disabledforeground = kfg.BGTOMBOL_DITEKAN)
    s12.grid(row = 2, column = 3, padx = kfg.PADDINGX, pady = kfg.PADDINGY)
    s13 = Button(root, height = kfg.TINGGI, width = kfg.LEBAR, font = kfg.FONT, relief = kfg.RELIEF, bg = kfg.BGTOMBOL, textvariable = b13, command = lambda: tekan(13), disabledforeground = kfg.BGTOMBOL_DITEKAN)
    s13.grid(row = 3, column = 0, padx = kfg.PADDINGX, pady = kfg.PADDINGY)
    s14 = Button(root, height = kfg.TINGGI, width = kfg.LEBAR, font = kfg.FONT, relief = kfg.RELIEF, bg = kfg.BGTOMBOL, textvariable = b14, command = lambda: tekan(14), disabledforeground = kfg.BGTOMBOL_DITEKAN)
    s14.grid(row = 3, column = 1, padx = kfg.PADDINGX, pady = kfg.PADDINGY)
    s15 = Button(root, height = kfg.TINGGI, width = kfg.LEBAR, font = kfg.FONT, relief = kfg.RELIEF, bg = kfg.BGTOMBOL, textvariable = b15, command = lambda: tekan(15), disabledforeground = kfg.BGTOMBOL_DITEKAN)
    s15.grid(row = 3, column = 2, padx = kfg.PADDINGX, pady = kfg.PADDINGY)
    s16 = Button(root, height = kfg.TINGGI, width = kfg.LEBAR, font = kfg.FONT, relief = kfg.RELIEF, bg = kfg.BGTOMBOL, textvariable = b16, command = lambda: tekan(16), disabledforeground = kfg.BGTOMBOL_DITEKAN)
    s16.grid(row = 3, column = 3, padx = kfg.PADDINGX, pady = kfg.PADDINGY)

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
        cek_coret()
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
        cek_coret()
        pesan_menang(0)
        COUNT = 0
        KLIK = True
        kosongkan()
    
    elif COUNT == 16:
        pesan_seri()
        COUNT = 0
        KLIK = True
        kosongkan()

def quote():
    f = codecs.open('data/quote.json', 'r', 'utf-8-sig')
    data = json.load(f)
    jumlah_data = len(data) - 1
    random_number = randint(0, jumlah_data)
    quote = data[random_number]

    #extrak data dari json
    quote_text = quote.get('text')
    quote_author = quote.get('from')

    #tampilkan quote
    msgbox.showinfo("QUOTE HARI INI", quote_text + "\n\n" + quote_author)
    f.close()

def coret(h,v,d):
    #cek value dan mensetting garis coretan
    if h == 1:
        b1.set("-") 
        b2.set("-")
        b3.set("-")
        b4.set("-")
    elif h == 2:
        b5.set("-") 
        b6.set("-")
        b7.set("-")
        b8.set("-")
    elif h == 3:
        b9.set("-") 
        b10.set("-")
        b11.set("-")
        b12.set("-")
    elif h == 4:
        b13.set("-") 
        b14.set("-")
        b15.set("-")
        b16.set("-")
    elif v == 1:
        b1.set("|") 
        b5.set("|") 
        b9.set("|") 
        b13.set("|")
    elif v == 2:
        b2.set("|") 
        b6.set("|") 
        b10.set("|") 
        b14.set("|")
    elif v == 3:
        b3.set("|") 
        b7.set("|") 
        b11.set("|") 
        b15.set("|")
    elif v == 4:
        b4.set("|") 
        b8.set("|") 
        b12.set("|") 
        b16.set("|")
    elif d == 1:
        b1.set("\\") 
        b6.set("\\") 
        b11.set("\\") 
        b16.set("\\")
    elif d == 2:
        b4.set("/") 
        b7.set("/") 
        b10.set("/") 
        b13.set("/")

def cek_coret():
    """
    |-----------|
    |1 |2 |3 |4 |
    |5 |6 |7 |8 |
    |9 |10|11|12|
    |13|14|15|16|
    |-----------|
    """
    # Cek value dari tombol dengan horizontal, vertical, diagonal kemungkinan untuk player 1
    # Horizontal
    if (b1.get() == '1' and b2.get() == '1' and b3.get() == '1' and b4.get() == '1'):
        coret(1, 0, 0)
    elif (b5.get() == '1' and b6.get() == '1' and b7.get() == '1' and b8.get() == '1'):
        coret(2, 0, 0)
    elif (b9.get() == '1' and b10.get() == '1' and b11.get() == '1' and b12.get() == '1'):
        coret(3, 0, 0)
    elif (b13.get() == '1' and b14.get() == '1' and b15.get() == '1' and b16.get() == '1'):
        coret(4, 0, 0)
    # Vertical
    elif (b1.get() == '1' and b5.get() == '1' and b9.get() == '1' and b13.get() == '1'):
        coret(0, 1, 0)
    elif (b2.get() == '1' and b6.get() == '1' and b10.get() == '1' and b14.get() == '1'):
        coret(0, 2, 0)
    elif (b3.get() == '1' and b7.get() == '1' and b11.get() == '1' and b15.get() == '1'):
        coret(0, 3, 0)
    elif (b4.get() == '1' and b8.get() == '1' and b12.get() == '1' and b16.get() == '1'):
        coret(0, 4, 0)
    # Diagonal
    elif (b1.get() == '1' and b6.get() == '1' and b11.get() == '1' and b16.get() == '1'):
        coret(0, 0, 1)
    elif (b4.get() == '1' and b7.get() == '1' and b10.get() == '1' and b13.get() == '1'):
        coret(0, 0, 2)


    # Cek value dari tombol dengan horizontal, vertical, diagonal kemungkinan untuk player 0
    # Horizontal
    elif (b1.get() == '0' and b2.get() == '0' and b3.get() == '0' and b4.get() == '0'):
        coret(1, 0, 0)
    elif (b5.get() == '0' and b6.get() == '0' and b7.get() == '0' and b8.get() == '0'):
        coret(2, 0, 0)
    elif (b9.get() == '0' and b10.get() == '0' and b11.get() == '0' and b12.get() == '0'):
        coret(3, 0, 0)
    elif (b13.get() == '0' and b14.get() == '0' and b15.get() == '0' and b16.get() == '0'):
        coret(4, 0, 0)
    # Vertical
    elif (b1.get() == '0' and b5.get() == '0' and b9.get() == '0' and b13.get() == '0'):
        coret(0, 1, 0)
    elif (b2.get() == '0' and b6.get() == '0' and b10.get() == '0' and b14.get() == '0'):
        coret(0, 2, 0)
    elif (b3.get() == '0' and b7.get() == '0' and b11.get() == '0' and b15.get() == '0'):
        coret(0, 3, 0)
    elif (b4.get() == '0' and b8.get() == '0' and b12.get() == '0' and b16.get() == '0'):
        coret(0, 4, 0)
    # Diagonal
    elif (b1.get() == '0' and b6.get() == '0' and b11.get() == '0' and b16.get() == '0'):
        coret(0, 0, 1)
    elif (b4.get() == '0' and b7.get() == '0' and b10.get() == '0' and b13.get() == '0'):
        coret(0, 0, 2)

def pesan_seri():
    msgbox.showinfo(kfg.JUDUL, "Permainan Seri")
    quote()
    start()

def pesan_menang(player):
    if player == 1:
        msgbox.showinfo(kfg.JUDUL, "Player 1 Menang !!!")
        quote()
        start()
    elif player == 0:
        msgbox.showinfo(kfg.JUDUL, "Player 0 Menang !!!")
        quote()
        start()

def kosongkan():
    b1.set(value="")
    b2.set(value="")
    b3.set(value="")
    b4.set(value="")
    b5.set(value="")
    b6.set(value="")
    b7.set(value="")
    b8.set(value="")
    b9.set(value="")
    b10.set(value="")
    b11.set(value="")
    b12.set(value="")
    b13.set(value="")
    b14.set(value="")
    b15.set(value="")
    b16.set(value="")

start()
root.mainloop()
