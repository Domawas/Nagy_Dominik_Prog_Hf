import math
import random

def elso_feladat():
    szam:int = int(input("Kérem adjon meg egy egész számot [200, 920] intervallumban: "))
    if 200 <= szam <= 920:
        elso_szamjegy = int(str(szam)[0])
        print("A szám első számjegye:", elso_szamjegy)
    else:
        print("Hiba: A szám nincs a [200, 920] intervallumban!")

    
def masodik_feladat(ora):
    if ora < 1:
        print("Be se jövök!")
    elif ora == 1:
        print("Még 90% on vagyunk!")
    elif ora in [2, 3]:
        print("Még bírjuk (60%)")
    elif ora in [4, 5, 6, 7]:
        print("Progit tanulunk, töltődünk! 70%")
    elif ora in [8, 9]:
        print("Lassan nem bírjuk tovább! 50%")
    else:
        print("Ez már tényleg túlzás.")


def harmadik_feladat():
    napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek"]
    nap = input("Add meg a napot: ")
    while nap not in napok:
        print("Hiba: érvénytelen nap.")
        nap = input("Próbáld újra: ")
    
    ora = input("Add meg az órát: ")
    if nap == "hétfő":
        print("alszik")
    elif nap == "kedd":
        if ora == "hittan":
            print("figyel")
        else:
            print("alszik")
    elif nap == "szerda":
        if ora == "programozás":
            print("dolgozik")
        else:
            print("nincs info")
    elif nap == "csütörtök":
        print("figyel")
    elif nap == "péntek":
        print("félig van jelen")


def negyedik_feladat():
    szam:int = int(input("Adj meg egy valós számot: "))

    if szam >= 0:
        gyokvonas = math.sqrt(szam)
        print("A szám négyzetgyöke:", gyokvonas)
    else:
        print("Hiba! Indok: Negatív szám!")


def otodik_feladat():
    oldal1 = float(input("Add meg az első oldalt: "))
    oldal2 = float(input("Add meg a második oldalt: "))
    while oldal1 <= 0 or oldal2 <= 0:
        print("Hiba: A téglalap oldalainak pozitívnak kell lenniük.")
        oldal1 = float(input("Próbáld újra az első oldalt: "))
        oldal2 = float(input("Próbáld újra a második oldalt: "))
    kerulet = 2 * (oldal1 + oldal2)
    terulet = oldal1 * oldal2
    print(f"Kerület: {kerulet:.2f}, Terület: {terulet:.2f}")


def feladat1():
    szektor = input("Add meg a szektort (A-H): ").upper()
    while szektor not in "ABCDEFGH":
        print("HIBA: Adjon meg egy betűt A-H-ig!")
        szektor = input("Próbáld újra: ").upper()

    if szektor == "A":
        print("Nemzetközi Csarnok, World Conservation Forum 2021")
    elif szektor in ["B", "E"]:
        print("Kereskedelmi Csarnok")
    elif szektor == "C":
        print("Konferencia-központ Innovációs Showroom")
    elif szektor == "D":
        print("Hal, Víz és Ember")
    elif szektor == "F":
        print("Hagyományos Vadászati Módok Csarnoka")
    elif szektor == "G":
        print("Hazai és nemzetközi Trófeakiállítás, 12. Nyílt Európai Taxiderma-bajnokság, Vadászat 21. században kiállítás")
    elif szektor == "H":
        print("Központi Magyar Kiállítás")


def hatodik_feladat():
    szamok=[]
    i=0
    while i<13:
        szam:int=int(random.random()*17)-5 
        szamok.append(int(szam))
        i+=1
    return szamok
def kerdes1(szamok):
    negativ=len([szam for szam in szamok if szam<0])
    pozitiv=len([szam for szam in szamok if szam>0])

    return pozitiv, negativ
def kerdes2(szamok):
    ossz =0
    for szam in szamok:
        if szam %2==0:
            ossz+=szam
    return ossz

def kerdes3(szamok):
    paratlan=0
    paros=0
    for szam in szamok:
        if szam %2==0:
            paros+=szam
        else:
            paratlan+=szam
    return paratlan, paros

def kerdes4(szamok):
    atlag=0
    for szam in szamok:
        atlag+=szam
    if len(szamok)==0:
        return 0
    return atlag/len(szamok)

def kerdes5(szamok):
    if len(szamok)==0:
        return
    max=szamok[0]
    for szam in szamok:
        if szam>max:
            max=szam
    return max

def hetedik_feladat():
    nevek = []
    while True:
        nev = input("Adj meg egy nevet (vagy @ a kilépéshez): ")
        if nev == "@":
            return nevek
        
        nevek.append(nev)
def van_a_betus(nevek):

    if len(nevek) == 0:
        return False
    else:
        if nevek[0][0].upper() == 'A':
            return True
        else:
            return van_a_betus(nevek[1:])  # Rekurzív hívás a lista maradékával

def leghosszabb_nev(nevek, max_nev=""):

    if len(nevek) == 0:
        return max_nev
    else:
        if len(nevek[0]) > len(max_nev):
            max_nev = nevek[0]
        return leghosszabb_nev(nevek[1:], max_nev)  # Rekurzív hívás a lista maradékával

def eredmenyek_kiirasa(nevek):
    print(f"Összesen {len(nevek)} nevet adtál meg.")
    

    if van_a_betus(nevek):
        print("Van A betűvel kezdődő név!")
    else:
        print("Nincs A betűvel kezdődő név.")
    
    # Megkeressük a leghosszabb nevet
    leghosszabb = leghosszabb_nev(nevek)
    print(f"A leghosszabb név: {leghosszabb}")



def nyolcadik_feladat():
    f_szamlalo = 0
    leghosszabb_f_sorozat = 0
    jelenlegi_f = 0
    probalkozasok = 0

    while probalkozasok < 10:
        beker = input("Add meg a jelet ('f' vagy 'i'): ")

        # Érvényes bemenet ellenőrzése
        while beker not in ['f', 'i']:
            print("Érvénytelen bemenet! Kérlek, adj meg 'f' vagy 'i' betűt.")
            beker = input("Add meg a jelet ('f' vagy 'i'): ")

        # Érték feldolgozása
        if beker == 'f':
            f_szamlalo += 1
            jelenlegi_f += 1
            leghosszabb_f_sorozat = max(leghosszabb_f_sorozat, jelenlegi_f)
        else:
            jelenlegi_f = 0

        probalkozasok += 1


    print(f"Hányszor adtál meg 'f' betűt: {f_szamlalo}")
    print(f"Mekkora a leghosszabb 'f' sorozat: {leghosszabb_f_sorozat}")



def kilencedik_feladat():
    for i in range(1, 11):  # 1-től 10-ig terjedő külső ciklus
        for j in range(1, 11):  # 1-től 10-ig terjedő belső ciklus
            print(f"{i * j:4}", end=' ')
        print() 


def tizedik_feladat(szam):

    if szam < 0:
        print("Kérlek, adj meg egy pozitív egész számot!")
        return

    egyesek = 0
    tizesek = 0
    szazak = 0
    ezrek = 0
    

    egyesek = szam % 10 
    szam //= 10  
    tizesek = szam % 10  
    szam //= 10  
    szazak = szam % 10 
    szam //= 10
    ezrek = szam  


    print(f"Egyesek: {egyesek}, Tizesek: {tizesek}, Százak: {szazak}, Ezrek: {ezrek}")



def tizenegyedik_feladat(szam):
    eredmeny = 0
    eredeti_szam = szam 
    while szam > 0:
        eredmeny += szam % 10

        szam //= 10
    print(f"{eredeti_szam} számjegyeinek összege: {eredmeny}")



def tizenkettedik_feladat():
    szam = int(input("Adj meg egy pozitív egész számot: "))

    osztok_osszege = 0
    oszto = 1

    while oszto <= szam:
        if szam % oszto == 0:
            osztok_osszege += oszto
        oszto += 1

    if osztok_osszege == 2 * szam:
        print(f"A {szam} tökéletes szám.")
    else:
        print(f"A {szam} nem tökéletes szám.")


def tizenharmadik_feladat(szam1, szam2):

    if szam1 <= 0 or szam2 <= 0:
        print("Kérlek, adj meg két pozitív egész számot!")
        return
    

    kisebb_szam = min(szam1, szam2)
    
    # Visszafelé keresünk közös osztót
    for i in range(kisebb_szam, 0, -1):
        if szam1 % i == 0 and szam2 % i == 0:
            print(f"A legnagyobb közös osztó: {i}")
            return


def utolso_feladat(a, b):
    # Meghatározzuk a nagyobb számot
    nagyobb = max(a, b)
    
    # Induljunk a nagyobb számtól
    while True:
        # Ellenőrizzük, hogy a nagyobb szám osztója-e mindkét számnak
        if nagyobb % a == 0 and nagyobb % b == 0:
            return nagyobb  # Visszatérünk a legkisebb közös többszörössel
        nagyobb += 1  # Növeljük a számot

