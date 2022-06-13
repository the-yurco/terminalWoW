from pprint import pprint
import random
import time
import math

'''
Aliance
'''
class Clovek:
    def __init__(self, Azivoty, Autok, Avzdialenost, Aobrana, Ameno):
        self.zivoty = Azivoty
        self.utok = Autok
        self.vzdialenost = Avzdialenost
        self.obrana = Aobrana
        self.meno = Ameno

    def getzivoty(self):
        return self.zivoty
    def getutok(self):
        return self.utok
    def getvzdialenost(self):
        return self.vzdialenost
    def getobrana(self):
        return self.obrana
    def getmeno(self):
        return self.meno

    def setzivoty(self, newzivoty):
        self.zivoty = newzivoty
    def setutok(self, newutok):
        self.utok = newutok
    def setvzdialenost(self, newvzdialenost):
        self.vzdialenost = newvzdialenost
    def setobrana(self, newobrana):
        self.obrana = newobrana
    def setmeno(self, newmeno):
        self.meno = newmeno

class Dwarf(Clovek):
    def __init__(self, Azivoty, Autok, Hluck, Avzdialenost, Hobrana, Ameno):
        super().__init__(Azivoty, Autok, Hluck, Avzdialenost, Hobrana, Ameno)


class NightElf(Clovek):
    def __init__(self, Azivoty, Autok, Hluck, Avzdialenost, Hobrana, Ameno):
        super().__init__(Azivoty, Autok, Hluck, Avzdialenost, Hobrana, Ameno)
#------------------------------------------------------------------------------------#

'''
Horda
'''
class Orc:
    def __init__(self, Hzivoty, Hutok, Hvzdialenost, Hobrana, Hmeno):
        self.zivoty = Hzivoty
        self.utok = Hutok
        self.vzdialenost = Hvzdialenost
        self.obrana = Hobrana
        self.meno = Hmeno

    def getzivoty(self):
        return self.zivoty
    def getutok(self):
        return self.utok
    def getvzdialenost(self):
        return self.vzdialenost
    def getobrana(self):
        return self.obrana
    def getmeno(self):
        return self.meno

    def setzivoty(self, newzivoty):
        self.zivoty = newzivoty
    def setutok(self, newutok):
        self.utok = newutok
    def setvzdialenost(self, newvzdialenost):
        self.vzdialenost = newvzdialenost
    def setobrana(self, newobrana):
        self.obrana = newobrana
    def setmeno(self, newmeno):
        self.meno = newmeno

class Undead(Orc):
    def __init__(self, Hzivoty, Hutok, Hvzdialenost, Hobrana, Hmeno):
        super().__init__(Hzivoty, Hutok, Hvzdialenost, Hobrana, Hmeno)

class BloodElf(Orc):
    def __init__(self, Hzivoty, Hutok, Hvzdialenost, Hobrana, Hmeno):
        super().__init__(Hzivoty, Hutok, Hvzdialenost, Hobrana, Hmeno)
#------------------------------------------------------------------------------------#

'''
Enemy
'''
class Enemy:
    def __init__(self, Ezivoty, Eutok, Especial, Emeno):
        self.zivoty = Ezivoty
        self.utok = Eutok
        self.special = Especial
        self.meno = Emeno

    def getzivoty(self):
        return self.zivoty
    def getutok(self):
        return self.utok
    def getSpecial (self):
        return self.special
    def getmeno(self):
        return self.meno

    def setzivoty(self, newzivoty):
        self.zivoty = newzivoty
    def setutok(self, newutok):
        self.utok = newutok
    def setSpecial(self, newSpecial):
        self.special = newSpecial
    def setmeno(self, newmeno):
        self.meno = newmeno
#------------------------------------------------------------------------------------#

def privitaciaobrazovka():
    print("")


def vytvoreniepostavy():
    print("*--------------------------------------*")
    pohlavie = input("CHOOSE YOUR GENDER(man/woman): ")
    while pohlavie != "man" and pohlavie != "woman":
        print("Ivalid input...")
        pohlavie = input("CHOOSE YOUR GENDER(man/woman): ")

    print("")
    print("")
    print("*---------------RASES---------------*")
    print("1. Aliance ")
    print("2. HORDA ")
    print("*----------------------------------*")
    rase = input("CHOOSE YOUR RASE: ")
    while rase != "1" and rase != "2":
        print("Zadal si nieco zle...")
        pohlavie = input("CHOOSE YOUR RASE: ") 

    if rase == "1":
        print("")
        print("")
        print("*---------------Aliance---------------*")
        print("1. Clovek ")
        print("2. Dwarf ")
        print("3. Night Elf ")
        print("*--------------------------------------*")
        Aliance = input("VYBER SI CHARAKTER Z ALIENCIE: ")
        while Aliance != "1" and Aliance != "2" and Aliance != "3":
            print("Zadal si nieco zle...")
            Aliance = input("VYBER SI CHARAKTER Z ALIENCIE: ")

        if Aliance == "1":
            print("")
            print("")
            print("*---------------HUMAN---------------*")
            print("1. Warrior ")
            print("2. Paladin ")
            print("3. Hunter ")
            print("4. Rogue ")
            print("*--------------------------------------*")
            classs = input("CHOOSE YOUR CLASS: ")
            while classs != "1" and classs != "2" and classs != "3" and classs != "4":
                print("Invalin input...")
                Aliance = input("CHOOSE YOUR CLASS: ")

        if Aliance == "2":
            print("")
            print("")
            print("*---------------DWARF---------------*")
            print("1. Warrior ")
            print("2. Paladin ")
            print("3. Hunter ")
            print("4. Rogue ")
            print("*--------------------------------------*")
            classs = input("CHOOSE YOUR CLASS: ")
            while classs != "1" and classs != "2" and classs != "3" and classs != "4":
                print("Zadal si nieco zle...")
                Aliance = input("CHOOSE YOUR CLASS: ")

        if Aliance == "3":
            print("")
            print("")
            print("*---------------NIGHT ELF---------------*")
            print("1. Mage ")
            print("2. Druid ")
            print("3. Hunter ")
            print("4. Rogue ")
            print("*--------------------------------------*")
            classs = input("CHOOSE YOUR CLASS: ")
            while classs != "1" and classs != "2" and classs != "3" and classs != "4":
                print("Zadal si nieco zle...")
                Aliance = input("CHOOSE YOUR CLASS: ")

    if rase == "2":
        print("")
        print("")
        print("*---------------Hord---------------*")
        print("1. Clovek ")
        print("2. Dwarf ")
        print("3. Night Elf ")
        print("*--------------------------------------*")
        Aliance = input("VYBER SI CHARAKTER Z ALIENCIE: ")
        while Aliance != "1" and Aliance != "2" and Aliance != "3":
            print("Zadal si nieco zle...")
            Aliance = input("VYBER SI CHARAKTER Z ALIENCIE: ")

def main():
    privitaciaobrazovka()
    vytvoreniepostavy()

main()