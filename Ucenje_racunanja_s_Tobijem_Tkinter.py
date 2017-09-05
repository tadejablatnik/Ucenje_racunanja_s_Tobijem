import tkinter as tk
from tkinter import messagebox
import random

SEZNAM = ['''Izbral/a si SEŠTEVANJE. Nič hudega, če še ne veš, kaj točno je to. Tu sem vendar zato, da ti pomagam. Predstavljaj si, da Janu babica podari dve jabolki,
          Maši pa eno. Maša jabolk ne mara, zato da svojega Janu. Koliko jabolk ima sedaj Jan? Odgovor je seveda tri. Sedaj pa poglej, kako to izgleda zapisano z
          matematičnimi znaki: 2 + 1 = 3. Poskusi še sam/a rešiti nekaj takih računov! V pomoč si predstavljaj, da ta števila pomenijo, koliko jabolk imata Jan in Maša.
          Srečno!''', '''Izbral/a si ODŠTEVANJE. Nič hudega, če še ne veš, kaj točno je to. Tu sem vendar zato, da ti pomagam. Predstavljaj si, da ima Jan pet jabolk, nato pa
          tri pa podari Maši. Koliko jabolk ima sedaj Jan? Pravilen odgovor je: Jan ima sedaj dve jabolki. Sedaj pa poglej, kako to izgleda zapisano z matematičnimi znaki: 5 - 3 = 2.
          Poskusi še sam/a rešiti nekaj takih računov! V pomoč si predstavljaj, da ta števila pomenijo, koliko jabolk ima Jan.
          Srečno!''', '''Izbral/a si MNOŽENJE. Nič hudega, če še ne veš, kaj točno je to. Tu sem vendar zato, da ti pomagam. Predstavljaj si, da otroci na igrišču želijo
          igrati košarko, zato se razdelijo v dve ekipi, v vsaki ekipi pa so štirje otroci. Koliko otrok igra med dvema ognjema? Pravilen odgovor je seveda osem.
          Sedaj pa poglej, kako to izgleda zapisano z matematičnimi znaki: 2 * 4 = 8.
          Poskusi še sam/a rešiti nekaj takih računov! V pomoč si za vsak primer predstavljaj, da ena številka pomeni, koliko je ekip, druga pa, koliko otrok je v
          vsaki ekipi. Srečno!''', '''Izbral/a si DELJENJE. Nič hudega, če še ne veš, kaj točno je to. Tu sem vendar zato, da ti pomagam. Predstavljaj si, da je na igrišču deset otrok, ki
          želijo igrati košarko. Koliko otrok bo v vsaki ekipi, če se razdelijo na dve ekipi? Pravilen odgovor: V vsaki ekipi bo pet otrok.
          Sedaj pa poglej, kako to izgleda z matematičnimi znaki: 10 / 2 = 5.
          Poskusi še sam/a rešiti nekaj takih računov! V pomoč si za vsak primer predstavljaj, da ena številka pomeni, koliko je vseh otrok, druga pa, v koliko ekip
          se bodo razdelili. Srečno!''']

NOVO_OKNO = ''

class Izberi_vrednost:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, bg='light steel blue')
        vescina = tk.Label(self.frame, text = 'Pozdravljen/a v aplikaciji Učenje računanja s Tobijem! Moje ime je Tobi in tu sem zato, da ti bom pomagal, ter te naučil osnovnih matematičnih operacij. Katero se želiš naučiti danes?', bg='light steel blue')
        vescina.pack()
        sestevanjeg = tk.Button(self.frame, text = 'SEŠTEVANJE', command = lambda: self.operacija(0), bg="light goldenrod")
        sestevanjeg.pack()
        odstevanjeg = tk.Button(self.frame, text = 'ODŠTEVANJE', command = lambda: self.operacija(1), bg="light salmon")
        odstevanjeg.pack()
        mnozenjeg = tk.Button(self.frame, text = 'MNOŽENJE', command = lambda: self.operacija(2), bg="dark turquoise")
        mnozenjeg.pack()
        deljenjeg = tk.Button(self.frame, text = 'DELJENJE', command = lambda: self.operacija(3), bg="spring green")
        deljenjeg.pack()
        self.frame.pack()

    def operacija(self, gumb):
        global NOVO_OKNO
        NOVO_OKNO = tk.Toplevel(self.master)
        self.aplikacija = Racunanje(NOVO_OKNO, gumb)
        

class Racunanje:
    def __init__(self, master, gumb):
        self.gumb = gumb
        self.master = master
        self.frame = tk.Frame(self.master, bg='light steel blue')
        self.razlaga = tk.Label(self.frame, text=SEZNAM[gumb], bg='light steel blue')#razlaga
        self.razlaga.grid(row=0, column=0, columnspan=3)#pozicija razlage
        self.racun = tk.Label(self.frame, text='', bg='green yellow')#racun
        self.racun.grid(row=1, column=1)#pozicija racuna
        self.rezultat = tk.StringVar(self.frame)#prostor da vneses rezultat
        izracunano = tk.Entry(self.frame, textvariable=self.rezultat)#vnesen rezultat
        izracunano['width'] = 10#velikost prostorcka za rezultat
        izracunano.grid(row=1, column=2)#pozicija prosorcka
        self.naslednji = tk.Button(self.frame, text='NAPREJ', command=self.resitev, bg='green yellow')
        self.naslednji.grid(row=1, column=3)
        self.pravilni = 0
        self.reseni_deset = 0
        self.reseni_sto = 0
        self.reseni_tisoc = 0
        self.pravilno = ''
        self.frame.pack()
        if self.gumb == 0:
            self.sestevanje()
        elif self.gumb == 1:
            self.odstevanje()
        elif self.gumb == 2:
            self.mnozenje()
        elif self.gumb == 3:
            self.deljenje()

    def resitev(self):
        try:
            vrednost = int(self.rezultat.get())
            if vrednost == self.pravilno:
                self.pravilni += 1
            if self.gumb == 0:
                self.sestevanje()
            elif self.gumb == 1:
                self.odstevanje()
            elif self.gumb == 2:
                self.mnozenje()
            elif self.gumb == 3:
                self.deljenje()
        except:
            pass

    def sestevanje(self):
        if self.reseni_deset < 5:
            a = random.randint(0, 10)
            b = random.randint(0, 10)
            self.pravilno = a + b
            self.racun['text'] = str(a) + '+' + str(b) + '=' #napise racun
            self.rezultat.set('')#vpises rezultat
            self.reseni_deset += 1 #enega vec si resil...
        elif self.reseni_sto < 5:
            a = random.randint(0, 100)
            b = random.randint(0, 100)
            self.pravilno = a + b
            self.racun['text'] = str(a) + '+' + str(b) + '='
            self.rezultat.set('')
            self.reseni_sto += 1
        elif self.reseni_tisoc < 5:
            a = random.randint(0, 1000)
            b = random.randint(0, 1000)
            self.pravilno = a + b
            self.racun['text'] = str(a) + '+' + str(b) + '='
            self.rezultat.set('')
            self.reseni_tisoc += 1
        else:
            global NOVO_OKNO
            odstotki = (int(self.pravilni) / int(self.reseni_deset + self.reseni_sto + self.reseni_tisoc)) * 100
            besedilo = 'Pravilno si rešil/a ' + str(self.pravilni) + ' od ' + str(self.reseni_deset + self.reseni_sto + self.reseni_tisoc) + ' računov. '
            if messagebox.showwarning('Tvoj uspeh', besedilo):
                NOVO_OKNO.destroy()

    def odstevanje(self):
        if self.reseni_deset < 5:
            a = random.randint(0, 10)
            b = random.randint(0, 10)
            if a < b:
                self.pravilno = b - a
                self.racun['text'] = str(b) + '-' + str(a) + '='
                self.rezultat.set('')
                self.reseni_deset += 1
            else:
                self.pravilno = a - b
                self.racun['text'] = str(a) + '-' + str(b) + '='
                self.rezultat.set('')
                self.reseni_deset += 1
        elif self.reseni_sto < 5:
            a = random.randint(0, 100)
            b = random.randint(0, 100)
            if a < b:
                self.pravilno = b - a
                self.racun['text'] = str(b) + '-' + str(a) + '='
                self.rezultat.set('')
                self.reseni_sto += 1
            else:
                self.pravilno = a - b
                self.racun['text'] = str(a) + '-' + str(b) + '='
                self.rezultat.set('')
                self.reseni_sto += 1
        elif self.reseni_tisoc < 5:
            a = random.randint(0, 1000)
            b = random.randint(0, 1000)
            if a < b:
                self.pravilno = b - a
                self.racun['text'] = str(b) + '-' + str(a) + '='
                self.rezultat.set('')
                self.reseni_tisoc += 1
            else:
                self.pravilno = a - b
                self.racun['text'] = str(a) + '-' + str(b) + '='
                self.rezultat.set('')
                self.reseni_tisoc += 1
        else:
            global NOVO_OKNO
            odstotki = (int(self.pravilni) / int(self.reseni_deset + self.reseni_sto + self.reseni_tisoc)) * 100
            besedilo = 'Pravilno si rešil/a ' + str(self.pravilni) + ' od ' + str(self.reseni_deset + self.reseni_sto + self.reseni_tisoc) + ' računov. '
            if messagebox.showwarning('Tvoj uspeh', besedilo):
                NOVO_OKNO.destroy()



    def mnozenje(self):
        if self.reseni_deset < 5:
            a = random.randint(0, 10)
            b = random.randint(0, 10)
            self.pravilno = a * b
            self.racun['text'] = str(a) + '*' + str(b) + '=' #napise racun
            self.rezultat.set('')#vpises rezultat
            self.reseni_deset += 1 #enega vec si resil...
        elif self.reseni_sto < 5:
            a = random.randint(0, 100)
            b = random.randint(0, 100)
            self.pravilno = a * b
            self.racun['text'] = str(a) + '*' + str(b) + '='
            self.rezultat.set('')
            self.reseni_sto += 1
        elif self.reseni_tisoc < 5:
            a = random.randint(0, 1000)
            b = random.randint(0, 1000)
            self.pravilno = a * b
            self.racun['text'] = str(a) + '*' + str(b) + '='
            self.rezultat.set('')
            self.reseni_tisoc += 1
        else:
            global NOVO_OKNO
            odstotki = (int(self.pravilni) / int(self.reseni_deset + self.reseni_sto + self.reseni_tisoc)) * 100
            besedilo = 'Pravilno si rešil/a ' + str(self.pravilni) + ' od ' + str(self.reseni_deset + self.reseni_sto + self.reseni_tisoc) + ' računov. '
            if messagebox.showwarning('Tvoj uspeh', besedilo):
                NOVO_OKNO.destroy()

    def deljenje(self):
        if self.reseni_deset < 5:
            n = random.randint(1, 20)
            if n % 8 == 0:
                self.pravilno = int(n / 8)
                self.racun['text'] = str(n) + '/' + '8' + '=' #napise racun
                self.rezultat.set('')#vpises rezultat
                self.reseni_deset += 1 #enega vec si resil...
            elif n % 9 == 0:
                self.pravilno = int(n / 9)
                self.racun['text'] = str(n) + '/' + '9' + '='
                self.rezultat.set('')
                self.reseni_deset += 1
            elif n % 10 == 0:
                self.pravilno = int(n / 10)
                self.racun['text'] = str(n) + '/' + '10' + '='
                self.rezultat.set('')
                self.reseni_deset += 1
            elif n % 5 == 0:
                self.pravilno = int(n / 5)
                self.racun['text'] = str(n) + '/' + '5' + '='
                self.rezultat.set('')
                self.reseni_deset += 1
            elif n % 6 == 0:
                self.pravilno = int(n / 6)
                self.racun['text'] = str(n) + '/' + '6' + '='
                self.rezultat.set('')
                self.reseni_deset += 1
            elif n % 7 == 0:
                self.pravilno = int(n / 7)
                self.racun['text'] = str(n) + '/' + '7' + '='
                self.rezultat.set('')
                self.reseni_deset += 1
            elif n % 3 == 0:
                self.pravilno = int(n / 3)
                self.racun['text'] = str(n) + '/' + '3' + '='
                self.rezultat.set('')
                self.reseni_deset += 1
            elif n % 4 == 0:
                self.pravilno = int(n / 4)
                self.racun['text'] = str(n) + '/' + '4' + '='
                self.rezultat.set('')
                self.reseni_deset += 1
            elif n % 2 == 0:
                self.pravilno = int(n / 2)
                self.racun['text'] = str(n) + '/' + '2' + '='
                self.rezultat.set('')
                self.reseni_deset += 1
            elif n % 1 == 0:
                self.pravilno = int(n / 1)
                self.racun['text'] = str(n) + '/' + '1' + '='
                self.rezultat.set('')
                self.reseni_deset += 1
        elif self.reseni_sto < 5:
            n = random.randint(1, 100)
            if n % 8 == 0:
                self.pravilno = int(n / 8)
                self.racun['text'] = str(n) + '/' + '8' + '=' 
                self.rezultat.set('')
                self.reseni_sto += 1 
            elif n % 9 == 0:
                self.pravilno = int(n / 9)
                self.racun['text'] = str(n) + '/' + '9' + '='
                self.rezultat.set('')
                self.reseni_sto += 1
            elif n % 10 == 0:
                self.pravilno = int(n / 10)
                self.racun['text'] = str(n) + '/' + '10' + '='
                self.rezultat.set('')
                self.reseni_sto += 1
            elif n % 5 == 0:
                self.pravilno = int(n / 5)
                self.racun['text'] = str(n) + '/' + '5' + '='
                self.rezultat.set('')
                self.reseni_sto += 1
            elif n % 6 == 0:
                self.pravilno = int(n / 6)
                self.racun['text'] = str(n) + '/' + '6' + '='
                self.rezultat.set('')
                self.reseni_sto += 1
            elif n % 7 == 0:
                self.pravilno = int(n / 7)
                self.racun['text'] = str(n) + '/' + '7' + '='
                self.rezultat.set('')
                self.reseni_sto += 1
            elif n % 3 == 0:
                self.pravilno = int(n / 3)
                self.racun['text'] = str(n) + '/' + '3' + '='
                self.rezultat.set('')
                self.reseni_sto += 1
            elif n % 4 == 0:
                self.pravilno = int(n / 4)
                self.racun['text'] = str(n) + '/' + '4' + '='
                self.rezultat.set('')
                self.reseni_sto += 1
            elif n % 2 == 0:
                self.pravilno = int(n / 2)
                self.racun['text'] = str(n) + '/' + '2' + '='
                self.rezultat.set('')
                self.reseni_sto += 1
            elif n % 1 == 0:
                self.pravilno = int(n / 1)
                self.racun['text'] = str(n) + '/' + '1' + '='
                self.rezultat.set('')
                self.reseni_sto += 1
        else:
            global NOVO_OKNO
            odstotki = (int(self.pravilni) / int(self.reseni_deset + self.reseni_sto)) * 100
            besedilo = 'Pravilno si rešil/a ' + str(self.pravilni) + ' od ' + str(self.reseni_deset + self.reseni_sto) + ' računov. '
            if messagebox.showwarning('Tvoj uspeh', besedilo):
                NOVO_OKNO.destroy()
            

def main():
    root = tk.Tk()
    app = Izberi_vrednost(root)
    root.mainloop()

if __name__ == '__main__':
    main()

