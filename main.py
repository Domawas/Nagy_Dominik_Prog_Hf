import metodusok


e=metodusok.elso_feladat()
print(e)

ora = int(input("Add meg az órát (1-9): "))
metodusok.masodik_feladat(ora)

metodusok.harmadik_feladat()

e=metodusok.negyedik_feladat()
print(e)

metodusok.otodik_feladat()

metodusok.feladat1()

e=metodusok.hatodik_feladat()
print(e)

pozitiv, negativ=metodusok.kerdes1(e)
print("Pozitív számok:", pozitiv)
print("Negatív számok:",negativ)

ossz=metodusok.kerdes2(e)
print("A páros számok összege:", ossz)

paratlan, paros=metodusok.kerdes3(e)
print("Páros számok összege:",paros)
print("Páratlan számok összege:", paratlan)

atlag=metodusok.kerdes4(e)
print("Átlag:", atlag)

max=metodusok.kerdes5(e)
print("A legnagyobb szám: ", max)

nevek = metodusok.hetedik_feladat()
metodusok.eredmenyek_kiirasa(nevek)

metodusok.nyolcadik_feladat()

metodusok.kilencedik_feladat()

metodusok.tizedik_feladat(5522)

metodusok.tizenegyedik_feladat(78)

metodusok.tizenkettedik_feladat()

metodusok.tizenharmadik_feladat(48, 18)

szam1 = 12
szam2 = 15
eredmeny = metodusok.utolso_feladat(szam1, szam2)
print(f"A {szam1} és {szam2} legkisebb közös többszöröse: {eredmeny}")