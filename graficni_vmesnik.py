__author__ = 'KorosecN13'

# Pikice in skatle
from tkinter import *
from igra import Igra


class Vmesnik():

    def __init__(self, master):

        # Ozadje
        master.configure(background='gold3')

        # Glavni meni
        menu = Menu(master)
        master.config(menu=menu)

        # File
        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)

        # Dodamo izbire v file_menu
        # file_menu.add_command(label="Nastavi velikost", command=self.nastavi_velikost)
        file_menu.add_command(label="Nova igra", command=self.nova_igra)
        file_menu.add_command(label="Izhod", command=master.destroy)

        # Velikost polja
        self.vrstice = 8
        self.stolpci = 8

        # Naredimo spremenljivke, ki hranijo vrednosti polj
        self.ime_igralec1 = StringVar(master, value='Igralec 1')
        self.ime_igralec2 = StringVar(master, value='Igralec 2')

        self.barva1 = 'light blue'
        self.barva2 = 'orange'

        # Kaj moramo povedati programu
        polje_ime_igralec1 = Entry(master, width=10, textvariable=self.ime_igralec1, background=self.barva1)
        polje_ime_igralec2 = Entry(master, width=10, textvariable=self.ime_igralec2, background=self.barva2)

        # Umestimo jih na glavno okno
        polje_ime_igralec1.grid(row=1, column=0)
        polje_ime_igralec2.grid(row=1, column=1)

        # spremenljivke, ki stejejo trenutni rezultat igre
        self.stevec_igralec1 = IntVar(master, value=0)
        self.stevec_igralec2 = IntVar(master, value=0)

        # Oznake za stevce
        oznaka_ime_igralec1 = Label(master, textvariable=self.stevec_igralec1, background=self.barva1)
        oznaka_ime_igralec2 = Label(master, textvariable=self.stevec_igralec2, background=self.barva2)

        # Umestimo jih na glavno okno
        oznaka_ime_igralec1.grid(row=2, column=0)
        oznaka_ime_igralec2.grid(row=2, column=1)

        # Igralno polje
        self.polje = Canvas(master, width=450, height=450)
        self.polje.grid(columnspan=2, row=3, column=0)

        # prilagodi velikost vrstic in stolpcev, če spremenimo velikost okna
        for i in range(2):
            master.columnconfigure(i, weight=3)
        for i in range(4):
            master.rowconfigure(i, weight=3)

        for i in range(8):
            for j in range(8):
                self.polje.create_oval(50*(i+1)-5, 50*(j+1)-5, 50*(i+1)+5, 50*(j+1)+5, fill='gold4', width=0)
        self.igra = Igra(self)
        self.zacni_igro()

    # def nastavi_velikost(self):
    #    pass

    def nova_igra(self):
        self.zacni_igro()

    def zacni_igro(self):
        self.na_potezi = self.ime_igralec1
        self.polje.bind('<Button-1>', self.klik)

    def klik(self, event):
        x, y = event.x, event.y
        # doloci kdo je na potezi
        self.igra.povleci_potezo(x, y)

    def narisi_crto(self, k, i, j, barva):
        """ narisi crto med ustrezna krogca na igralnem polju """
        if k == 'vodoravno':
            self.polje.create_line(50*(j+1)+5, 50*(i+1), 50*(j+2)-5, 50*(i+1), fill=barva, width=3)
        else:
            self.polje.create_line(50*(j+1), 50*(i+1)+5, 50*(j+1), 50*(i+2)-5, fill=barva, width=3)

    def pobarvaj_kvadratek(self, j, i, barva):
        self.polje.create_rectangle(50*i+5, 50*j+5, 50*i+45, 50*j+45, fill=barva, width=0)

    def zmaga(self):
        if self.stevec_igralec1.get() > self.stevec_igralec2.get():
            zmagovalec = self.ime_igralec1.get()
        else:
            zmagovalec = self.ime_igralec2.get()
        self.polje.create_rectangle(100, 150, 350, 300, fill='green yellow')
        self.polje_id1 = self.polje.create_text(225,200,font=("Purisa", 20))
        self.polje.itemconfig(self.polje_id1 ,text='Zmagal je')
        self.polje_id1 = self.polje.create_text(225,250,font=("Purisa", 20))
        self.polje.itemconfig(self.polje_id1 ,text='{0}'.format(zmagovalec))


root = Tk()
root.title('Pikice in Skatle')
aplikacija = Vmesnik(root)
root.mainloop()