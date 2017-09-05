import tkinter as tk
import random

def izberi_vescino():
    okno = tk.Tk()
    vescina = tk.Label(okno, text = 'Pozdravljen/a v Učenje računanja s Tobijem! Sem Tobi in tu sem zato, da ti bom pomagal, ko se ti bo kaj zataknilo. Kaj se želiš naučiti danes?')
    vescina.pack()
    sesetvanje = tk.Button(okno, text = 'SEŠTEVANJE', command = sestevanje)
    sestevanje.pack()
    odstevanje = tk.Button(okno, text = 'ODŠTEVANJE', command = odstevanje)
    odstevanje.pack()
    mnozenje = tk.Button(okno, text = 'MNOŽENJE', command = mnozenje)
    mnozenje.pack()
    deljenje = tk.Button(okno, text = 'DELJENJE', command = deljenje)
    deljenje.pack()

def ocena(odstotki):
    if odstotki < 49:
        return 'Še veliko dela te čaka...'
    elif 50 < odstotki < 64:
        return 'Lahko bi se bolj potrudil/a...'
    elif 65 < odstotki < 78:
        return 'Še malo vadi, ampak si na dobri poti!'
    elif 79 < odstotki < 89:
        return 'Že kar veliko znaš!'
    elif 90 < odstotki:
        return 'Super si, to veščino že obvladaš!'

def nadaljevanje():
    odgovor = input('Želiš nadaljevati z učenjem? (Da / Ne)')
    if odgovor == 'DA' or odgovor == 'da' or odgovor == 'Da':
        print('Super! Sedaj si lahko izbereš novo veščino.')
        return izberi_vescino()
    elif odgovor == 'NE' or odgovor == 'ne' or odgovor == 'Ne':
        print('Škoda! Se vidiva prihodnjič, adijo!')


def sestevanje():
    pravilni1 = 0
    reseni_deset1 = 0
    reseni_sto1 = 0
    reseni_tisoc1 = 0
    print('''Izbral/a si SEŠTEVANJE. Nič hudega, če še ne veš, kaj točno je to. Tu sem vendar zato, da ti pomagam. Predstavljaj si, da Janu babica podari dve jabolki,
          Maši pa eno. Maša jabolk ne mara, zato da svojega Janu. Koliko jabolk ima sedaj Jan? Odgovor je sseveda tri. Sedaj pa poglej, kako to izgleda zapisano z
          matematičnimi znaki: 2 + 1 = 3. Poskusi še sam/a rešiti nekaj takih računov, v pomoč si predtavljaj, da ta števila pomenijo, koliko jabolk imata Jan in Maša.
          Srečno!''')
    while reseni_deset1 < 2:#11
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        a_plus_b = a + b
        rezultat_ab = input(str(a) + '+' + str(b) + '=')
        if int(rezultat_ab) == a_plus_b:
            print('Bravo, tvoj odgovor je pravilen!')
            pravilni1 += 1
            reseni_deset1 += 1
        else:
            print('Nekaj ni v redu, naslednjič se bolj potrudi!')
            reseni_deset1 += 1
    while reseni_sto1 < 2:#11
        c = random.randint(0, 100)
        d = random.randint(0, 100)
        c_plus_d = c + d 
        rezultat_cd = input(str(c) + '+' + str(d) + '=')
        if int(rezultat_cd) == c_plus_d:
            print('Bravo, tvoj odgovor je pravilen!')
            pravilni1 += 1
            reseni_sto1 += 1
        else:
            print('Nekaj ni v redu, naslednjič se bolj potrudi!')
            reseni_sto1 += 1
    while reseni_tisoc1 < 2:#11
        e = random.randint(0, 1000)
        f = random.randint(0, 1000)
        e_plus_f = e + f
        rezultat_ef = input(str(e) + '+' + str(f) + '=')
        if int(rezultat_ef) == e_plus_f:
            print('Bravo, tvoj odgovor je pravilen!')
            pravilni1 += 1
            reseni_tisoc1 += 1
        else:
            print('Nekaj ni v redu, naslednjič se bolj potrudi!')
            reseni_tisoc1 += 1
    odstotki_sestevanja1 = (int(pravilni1) / int(reseni_deset1 + reseni_sto1 + reseni_tisoc1)) * 100
    print('Pravilno si rešil/a ' + str(pravilni1) + ' od ' + str(reseni_deset1 + reseni_sto1 + reseni_tisoc1) + ' računov.')
    print((ocena(odstotki_sestevanja1)))
    return nadaljevanje()
    
def odstevanje():
    pravilni2 = 0
    reseni_deset2 = 0
    reseni_sto2 = 0
    reseni_tisoc2 = 0
    print('''Izbral/a si ODŠTEVANJE. Nič hudega, če še ne veš, kaj točno je to. Tu sem vendar zato, da ti pomagam. Predstavljaj si, da ima Jan pet jabolk, nato pa
          tri podari Maši. Koliko jabolk ima sedaj Jan? Odgovor je: Jan ima sedaj dve jabolki. Sedaj pa poglej, kako to izgleda z matematičnimi znaki: 5 - 3 = 2.
          Poskusi še sam/a rešiti nekaj takih računov, v pomoč si predtavljaj, da ta števila pomenijo, koliko jabolk imat Jan.
          Srečno!''')
    while reseni_deset2 < 2:#11
        g = random.randint(0, 10)
        h = random.randint(0, 10)
        if g < h:
            h_minus_g = h - g
            rezultat_hg = input(str(h) + '-' + str(g) + '=')
            if int(rezultat_hg) == h_minus_g:
                print('Bravo, tvoj odgovor je pravilen!')
                pravilni2 += 1
                reseni_deset2 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni_deset2 += 1
        else:
            g_minus_h = g - h
            rezultat_gh = input(str(g) + '-' + str(h) + '=')
            if int(rezultat_gh) == g_minus_h:
                print('Bravo, tvoj odgovor je pravilen!')
                pravilni2 += 1
                reseni_deset2 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni_deset2 += 1
    while reseni_sto2 < 2:#11
        i = random.randint(0, 100)
        j = random.randint(0, 100)
        if i < j: 
            j_minus_i = j - i
            rezultat_ji = input(str(j) + '-' + str(i) + '=')
            if int(rezultat_ji) == j_minus_i:
                print('Bravo, tvoj odgovor je pravilen!')
                pravilni2 += 1
                reseni_sto2 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni_sto2 += 1
        else:
            i_minus_j = i - j
            rezultat_ij = input(str(i) + '-' + str(j) + '=')
            if int(rezultat_ij) == i_minus_j:
                print('Bravo, tvoj odgovor je pravilen!')
                pravilni2 += 1
                reseni_sto2 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni_sto2 += 1
    while reseni_tisoc2 < 2:#11
        m = random.randint(0, 1000)
        n = random.randint(0, 1000)
        if m < n:
            n_minus_m = n - m
            rezultat_nm = input(str(n) + '-' + str(m) + '=')
            if int(rezultat_nm) == n_minus_m:
                print('Bravo, tvoj odgovor je pravilen!')
                pravilni2 += 1
                reseni_tisoc2 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni_tisoc2 += 1
        else:
            m_minus_n = m - n
            rezultat_mn = input(str(m) + '-' + str(n) + '=')
            if int(rezultat_mn) == m_minus_n:
                print('Bravo, tvoj odgovor je pravilen!')
                pravilni2 += 1
                reseni_tisoc2 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni_tisoc2 += 1
    odstotki_sestevanja2 = (int(pravilni2) / int(reseni_deset2 + reseni_sto2 + reseni_tisoc2)) * 100
    print('Pravilno si rešil/a ' + str(pravilni2) + ' od ' + str(reseni_deset2 + reseni_sto2 + reseni_tisoc2) + ' računov. ' + str(ocena(odstotki_sestevanja2)))
    return nadaljevanje()

def mnozenje():
    pravilni3 = 0
    reseni_deset3 = 0
    reseni_sto3 = 0
    print('''Izbral/a si MNOŽENJE. Nič hudega, če še ne veš, kaj točno je to. Tu sem vendar zato, da ti pomagam. Predstavljaj si, da otroci na igrišču želijo
          igrati med dvema ognjema, zato se razdelijo v dve ekipi, v vsaki ekipi pa so štirje otroci. Koliko otrok igra med dvema ognjema? Odgovor je seveda osem.
          Sedaj pa poglej, kako to izgleda z matematičnimi znaki: 2 * 4 = 8.
          Poskusi še sam/a rešiti nekaj takih računov, v pomoč si za vsak primer predstavljaj, da ena številka pomeni, koliko je ekip, druga pa, koliko otrok je v
          vsaki ekipi. Srečno!''')
    while reseni_deset3 < 2:
        faktor1 = random.randint(0, 10)
        faktor2 = random.randint(0, 10)
        zmnozek12 = faktor1 * faktor2
        rezultat_f1f2 = input(str(faktor1) + '*' + str(faktor2) + '=')
        if int(rezultat_f1f2) == zmnozek12:
            print('Bravo, tvoj odgovor je pravilen!')
            pravilni3 += 1
            reseni_deset3 += 1
        else:
            print('Nekaj ni v redu, naslednjič se bolj potrudi!')
            reseni_deset3 += 1 
    while reseni_sto3 < 2:
        faktor3 = random.randint(0, 10)
        faktor4 = random.randint(0, 100)
        zmnozek34 = faktor3 * faktor4
        rezultat_f3f4 = input(str(faktor3) + '*' + str(faktor4) + '=')
        if int(rezultat_f3f4) == zmnozek34:
            print('Bravo, tvoj odgovor je pravilen!')
            pravilni3 += 1
            reseni_sto3 += 1
        else:
            print('Nekaj ni v redu, naslednjič se bolj potrudi!')
            reseni_sto3 += 1
    odstotki_sestevanja3 = (int(pravilni3) / int(reseni_deset3 + reseni_sto3)) * 100
    print('Pravilno si rešil/a ' + str(pravilni3) + ' od ' + str(reseni_deset3 + reseni_sto3) + ' računov. ' + str(ocena(odstotki_sestevanja3)))
    return nadaljevanje()

def deljenje():
    pravilni4 = 0
    reseni4 = 0
    reseni_vecji4 = 0
    print('''Izbral/a si DELJENJE. Nič hudega, če še ne veš, kaj točno je to. Tu sem vendar zato, da ti pomagam. Predstavljaj si, da je na igrišču deset otrok, ki
          želijo igrati igro med dvema ognjema. Koliko otrok bo v vsaki ekipi, če se razdelijo na dve ekipi? Odgovor: v vsaki ekipi bo pet otrok
          Sedaj pa poglej, kako to izgleda z matematičnimi znaki: 10 / 2 = 5.
          Poskusi še sam/a rešiti nekaj takih računov, v pomoč si za vsak primer predstavljaj, da ena številka pomeni, koliko je vseh otrok, druga pa, v koliko ekip
          se bodo razdelili. Srečno!''')
    while reseni4 < 10:
        n = random.randint(1, 20)
        if n % 8 == 0:
            resen8 = int(n / 8)
            resen88 = input(str(n) + ' /' + ' 8' + ' =')
            if int(resen88) == resen8:
                print('Bravo, tvoj odgovor je pravilen!')
                reseni4 += 1
                pravilni4 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni4 += 1
        elif n % 9 == 0:
            resen9 = int(n / 9)
            resen99 = input(str(n) + ' /' + ' 9' + ' =')
            if int(resen99) == resen9:
                print('Bravo, tvoj odgovor je pravilen!')
                reseni4 += 1
                pravilni4 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni4 += 1
        elif n % 10 == 0:
            resen10 = int(n / 10)
            resen1010 = input(str(n) + ' /' + ' 10' + ' =')
            if int(resen1010) == resen10:
                print('Bravo, tvoj odgovor je pravilen!')
                reseni4 += 1
                pravilni4 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni4 += 1
        elif n % 5 == 0:
            resen5 = int(n / 5)
            resen55 = input(str(n) + ' /' + ' 5' + ' =')
            if int(resen55) == resen5:
                print('Bravo, tvoj odgovor je pravilen!')
                reseni4 += 1
                pravilni4 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni4 += 1
        elif n % 6 == 0:
            resen6 = int(n / 6)
            resen66 = input(str(n) + ' /' + ' 6' + ' =')
            if int(resen66) == resen6:
                print('Bravo, tvoj odgovor je pravilen!')
                reseni4 += 1
                pravilni4 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni4 += 1
        elif n % 7 == 0:
            resen7 = int(n / 7)
            resen77 = input(str(n) + ' /' + ' 7' + ' =')
            if int(resen77) == resen7:
                print('Bravo, tvoj odgovor je pravilen!')
                reseni4 += 1
                pravilni4 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni4 += 1
        elif n % 3 == 0:
            resen3 = int(n / 3)
            resen33 = input(str(n) + ' /' + ' 3' + ' =')
            if int(resen33) == resen3:
                print('Bravo, tvoj odgovor je pravilen!')
                reseni4 += 1
                pravilni4 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni4 += 1
        elif n % 4 == 0:
            resen4 = int(n / 4)
            resen44 = input(str(n) + ' /' + ' 4' + ' =')
            if int(resen44) == resen4:
                print('Bravo, tvoj odgovor je pravilen!')
                reseni4 += 1
                pravilni4 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni4 += 1
        elif n % 2 == 0:
            resen2 = int(n / 2)
            resen22 = input(str(n) + ' /' + ' 2' + ' =')
            if int(resen22) == resen2:
                print('Bravo, tvoj odgovor je pravilen!')
                reseni4 += 1
                pravilni4 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni4 += 1
    while reseni_vecji4 < 10:
        x = random.randint(1, 100)
        if x % 8 == 0:
            resen8 = int(x / 8)
            resen88 = input(str(x) + ' /' + ' 8' + ' =')
            if int(resen88) == resen8:
                print('Bravo, tvoj odgovor je pravilen!')
                reseni_vecji4 += 1
                pravilni4 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni_vecji4 += 1
        elif x % 9 == 0:
            resen9 = int(x / 9)
            resen99 = input(str(x) + ' /' + ' 9' + ' =')
            if int(resen99) == resen9:
                print('Bravo, tvoj odgovor je pravilen!')
                reseni_vecji4 += 1
                pravilni4 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni_vecji4 += 1
        elif x % 10 == 0:
            resen10 = int(x / 10)
            resen1010 = input(str(x) + ' /' + ' 10' + ' =')
            if int(resen1010) == resen10:
                print('Bravo, tvoj odgovor je pravilen!')
                reseni_vecji4 += 1
                pravilni4 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni_vecji4 += 1
        elif x % 5 == 0:
            resen5 = int(x / 5)
            resen55 = input(str(x) + ' /' + ' 5' + ' =')
            if int(resen55) == resen5:
                print('Bravo, tvoj odgovor je pravilen!')
                reseni_vecji4 += 1
                pravilni4 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni_vecji4 += 1
        elif x % 6 == 0:
            resen6 = int(x / 6)
            resen66 = input(str(x) + ' /' + ' 6' + ' =')
            if int(resen66) == resen6:
                print('Bravo, tvoj odgovor je pravilen!')
                reseni_vecji4 += 1
                pravilni4 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni_vecji4 += 1
        elif x % 7 == 0:
            resen7 = int(x / 7)
            resen77 = input(str(x) + ' /' + ' 7' + ' =')
            if int(resen77) == resen7:
                print('Bravo, tvoj odgovor je pravilen!')
                reseni_vecji4 += 1
                pravilni4 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni_vecji4 += 1
        elif x % 3 == 0:
            resen3 = int(x / 3)
            resen33 = input(str(x) + ' /' + ' 3' + ' =')
            if int(resen33) == resen3:
                print('Bravo, tvoj odgovor je pravilen!')
                reseni_vecji4 += 1
                pravilni4 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni_vecji4 += 1
        elif x % 4 == 0:
            resen4 = int(x / 4)
            resen44 = input(str(x) + ' /' + ' 4' + ' =')
            if int(resen44) == resen4:
                print('Bravo, tvoj odgovor je pravilen!')
                reseni_vecji4 += 1
                pravilni4 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni_vecji4 += 1
        elif x % 2 == 0:
            resen2 = int(x / 2)
            resen22 = input(str(x) + ' /' + ' 2' + ' =')
            if int(resen22) == resen2:
                print('Bravo, tvoj odgovor je pravilen!')
                reseni_vecji4 += 1
                pravilni4 += 1
            else:
                print('Nekaj ni v redu, naslednjič se bolj potrudi!')
                reseni_vecji4 += 1
    odstotki_sestevanja4 = (int(pravilni4) / int(reseni4 + reseni_vecji4)) * 100
    print('Pravilno si rešil/a ' + str(pravilni4) + ' od ' + str(reseni4 + reseni_vecji4) + ' računov. ' + str(ocena(odstotki_sestevanja4)))
    return nadaljevanje()

def uspeh(): #uvali ga še v veščine!!!!!!!
    novo = (odstotki_sestevanja1 + odstotki_sestevanja2 + odstotki_sestevanja3 + odstotki_sestevanja4) / 4
    print('Tvoja skupna opisna ocena:' + ocena(novo) + '. Sedaj lahko izbereš novo veščino!')
    return izberi_vescino()
    

    

    


    
        
    
    
    
        
        
