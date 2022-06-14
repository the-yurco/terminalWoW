from pprint import pprint
import random
import time
import math

'''
Alliance
'''
class Alliance:
    def __init__(self, Ahealth, Aattack, Aluck, Arange, Adefence, Amagic, Aname):
        self.health = Ahealth
        self.attack = Aattack
        self.range = Arange
        self.luck = Aluck
        self.defence = Adefence
        self.magic = Amagic
        self.name = Aname

    def gethealth(self):
        return self.health
    def getattack(self):
        return self.attack
    def getluck(self):
        return self.luck
    def getrange(self):
        return self.range
    def getdefence(self):
        return self.defence
    def getMagic(self):
        return self.magic
    def getname(self):
        return self.name

    def sethealth(self, newhealth):
        self.health = newhealth
    def setattack(self, newattack):
        self.attack = newattack
    def setluck(self, newluck):
        self.luck = newluck
    def setrange(self, newrange):
        self.range = newrange
    def setdefence(self, newdefence):
        self.defence = newdefence
    def setMagic(self, newMagic):
        self.magic = newMagic
    def setname(self, newname):
        self.name = newname

class Clovek(Alliance):
    def __init__(self, Ahealth, Aattack, Aluck, Arange, Adefence, Amagic, Aname):
        super().__init__(Ahealth, Aattack, Aluck, Arange, Adefence, Amagic, Aname)

class Dwarf(Alliance):
    def __init__(self, Ahealth, Aattack, Aluck, Arange, Adefence, Amagic, Aname):
        super().__init__(Ahealth, Aattack, Aluck, Arange, Adefence, Amagic, Aname)


class NightElf(Alliance):
    def __init__(self, Ahealth, Aattack, Aluck, Arange, Adefence, Amagic, Aname):
        super().__init__(Ahealth, Aattack, Aluck, Arange, Adefence, Amagic, Aname)
#------------------------------------------------------------------------------------#

'''
Horda
'''
class Horde:
    def __init__(self, Hhealth, Hattack, Hrange, Hluck, Hmagic, Hdefence, Hname):
        self.health = Hhealth
        self.attack = Hattack
        self.range = Hrange
        self.luck = Hluck
        self.defence = Hdefence
        self.magic = Hmagic
        self.name = Hname

    def gethealth(self):
        return self.health
    def getattack(self):
        return self.attack
    def getluck(self):
        return self.luck
    def getrange(self):
        return self.range
    def getdefence(self):
        return self.defence
    def getMagic(self):
        return self.magic
    def getname(self):
        return self.name

    def sethealth(self, newhealth):
        self.health = newhealth
    def setattack(self, newattack):
        self.attack = newattack
    def setluck(self, newluck):
        self.luck = newluck
    def setrange(self, newrange):
        self.range = newrange
    def setdefence(self, newdefence):
        self.defence = newdefence
    def setMagic(self, newMagic):
        self.magic = newMagic
    def setname(self, newname):
        self.name = newname

class Orc(Horde):
    def __init__(self, Hhealth, Hattack, Hrange, Hluck, Hmagic, Hdefence, Hname):
        super().__init__(Hhealth, Hattack, Hrange, Hluck, Hmagic, Hdefence, Hname)

class Undead(Horde):
    def __init__(self, Hhealth, Hattack, Hrange, Hluck, Hmagic, Hdefence, Hname):
        super().__init__(Hhealth, Hattack, Hrange, Hluck, Hmagic, Hdefence, Hname)

class BloodElf(Horde):
    def __init__(self, Hhealth, Hattack, Hrange, Hluck, Hmagic, Hdefence, Hname):
        super().__init__(Hhealth, Hattack, Hrange, Hluck, Hmagic, Hdefence, Hname)
#------------------------------------------------------------------------------------#

'''
Enemy
'''
class Enemy:
    def __init__(self, Ehealth, Eattack, Especial, Ename):
        self.health = Ehealth
        self.attack = Eattack
        self.special = Especial
        self.name = Ename

    def gethealth(self):
        return self.health
    def getattack(self):
        return self.attack
    def getSpecial (self):
        return self.special
    def getname(self):
        return self.name

    def sethealth(self, newhealth):
        self.health = newhealth
    def setattack(self, newattack):
        self.attack = newattack
    def setSpecial(self, newSpecial):
        self.special = newSpecial
    def setname(self, newname):
        self.name = newname
#------------------------------------------------------------------------------------#
"""
Boss
"""
class Boss (Enemy):
    def __init__(self, Bhealth, Battack, Bspecial, Bchance, Bname, BsuperMove):
        super().__init__(Bhealth, Battack, Bspecial, Bchance, Bname)

        self.superMove = BsuperMove

    def getSuper(self):
        return self.superMove
    
    def setSuper(self, newSuperMove):
        self.superMove = newSuperMove

#------------------------------------------------------------------------------#

def welcomescreen():
    print("       WELCOME IN GAME NAMED WORLD OF WARCRAFT       ")
    print("*---------------------------------------------------*")
    print("##      ##      ##                 ##      ##      ##")
    print(" ##    ####    ##                   ##    ####    ## ")
    print("  ##  ##  ##  ##        #####        ##  ##  ##  ##  ")
    print("    # #    # #        #       #       # #      # #   ")
    print("     #      #           #####          #        #    ")
    print("*---------------------------------------------------*")
    print("“This is Azeroth.... ")
    print("A dangerous, beautiful, magical, and inspiring world. A world filled with discovery, innovation, and wonder. ")
    print("A world worth fighting for. A world worth protecting.”")
    print("")
    print("")
    time.sleep(0.2)
    email = input("ENTER YOUR EMAIL: ")
    password = input("ENTER YOUR PASSWORD: ")


def game():
    print("*--------------------------------------*")
    pohlavie = input("CHOOSE YOUR GENDER(man/woman): ")
    while pohlavie != "man" and pohlavie != "woman":
        print("Ivalid input...")
        pohlavie = input("CHOOSE YOUR GENDER(man/woman): ")

    print("")
    print("")
    print("*---------------RASES---------------*")
    print("1. ALLIANCE ")
    print("2. HORDE ")
    print("*----------------------------------*")
    rase = input("CHOOSE YOUR RASE: ")
    while rase != "1" and rase != "2":
        print("Zadal si nieco zle...")
        pohlavie = input("CHOOSE YOUR RASE: ") 

    if rase == "1":
        print("")
        print("")
        print("*---------------ALLIANCE---------------*")
        print("1. Clovek ")
        print("2. Dwarf ")
        print("3. Night Elf ")
        print("*--------------------------------------*")
        Aliance = input("CHOOSE YOUR CHARACTER FROM ALLIANCE: ")
        while Aliance != "1" and Aliance != "2" and Aliance != "3":
            print("Zadal si nieco zle...")
            Aliance = input("CHOOSE YOUR CHARACTER FROM ALLIANCE: ")

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

            if classs == "1":
                warriorattack = 10
                warriordefence = 7
                warriorluck = 4
                warriorrange = 4
                warriormagic = 1
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", warriorattack)
                print("DEFENCE: ", warriordefence)
                print("LUCK: ", warriorluck)
                print("RANGE: ", warriorrange)
                print("MAGIC: ", warriormagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "2":
                paladinattack = 10
                paladindefence = 8
                paladinluck = 4
                paladinrange = 3
                paladinmagic = 4
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", paladinattack)
                print("DEFENCE: ", paladindefence)
                print("LUCK: ", paladinluck)
                print("RANGE: ", paladinrange)
                print("MAGIC: ", paladinmagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "3":
                hunterattack = 10
                hunterdefence = 7
                hunterluck = 2
                hunterrange = 5
                huntermagic = 2
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", hunterattack)
                print("DEFENCE: ", hunterdefence)
                print("LUCK: ", hunterluck)
                print("RANGE: ", hunterrange)
                print("MAGIC: ", huntermagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "4":
                rogueattack = 8
                roguedefence = 8
                rogueluck = 3
                roguerange = 6
                roguemagic = 5
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("NAME: ", name)
                print("ATTACK: ", rogueattack)
                print("DEFENCE: ", roguedefence)
                print("LUCK: ", rogueluck)
                print("RANGE: ", roguerange)
                print("MAGIC: ", roguemagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

        elif Aliance == "2":
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
                print("Invalid input...")
                Aliance = input("CHOOSE YOUR CLASS: ")

            if classs == "1":
                warriorattack = 10
                warriordefence = 7
                warriorluck = 4
                warriorrange = 4
                warriormagic = 1
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", warriorattack)
                print("DEFENCE: ", warriordefence)
                print("LUCK: ", warriorluck)
                print("RANGE: ", warriorrange)
                print("MAGIC: ", warriormagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "2":
                paladinattack = 10
                paladindefence = 8
                paladinluck = 4
                paladinrange = 3
                paladinmagic = 4
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", paladinattack)
                print("DEFENCE: ", paladindefence)
                print("LUCK: ", paladinluck)
                print("RANGE: ", paladinrange)
                print("MAGIC: ", paladinmagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "3":
                hunterattack = 10
                hunterdefence = 7
                hunterluck = 2
                hunterrange = 5
                huntermagic = 2
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", hunterattack)
                print("DEFENCE: ", hunterdefence)
                print("LUCK: ", hunterluck)
                print("RANGE: ", hunterrange)
                print("MAGIC: ", huntermagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "4":
                rogueattack = 8
                roguedefence = 8
                rogueluck = 3
                roguerange = 6
                roguemagic = 5
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("NAME: ", name)
                print("ATTACK: ", rogueattack)
                print("DEFENCE: ", roguedefence)
                print("LUCK: ", rogueluck)
                print("RANGE: ", roguerange)
                print("MAGIC: ", roguemagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

        elif Aliance == "3":
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
                print("Invalid input...")
                Aliance = input("CHOOSE YOUR CLASS: ")

            if classs == "1":
                mageattack = 9.5
                magedefence = 6
                mageluck = 5
                magerange = 9
                magemagic = 8
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", mageattack)
                print("DEFENCE: ", magedefence)
                print("LUCK: ", mageluck)
                print("RANGE: ", magerange)
                print("MAGIC: ", magemagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "2":
                druidattack = 9
                druiddefence = 5
                druidluck = 7
                druidrange = 8
                druidmagic = 7
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", druidattack)
                print("DEFENCE: ", druiddefence)
                print("LUCK: ", druidluck)
                print("RANGE: ", druidrange)
                print("MAGIC: ", druidmagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "3":
                hunterattack = 10
                hunterdefence = 7
                hunterluck = 2
                hunterrange = 5
                huntermagic = 2
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", hunterattack)
                print("DEFENCE: ", hunterdefence)
                print("LUCK: ", hunterluck)
                print("RANGE: ", hunterrange)
                print("MAGIC: ", huntermagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "4":
                rogueattack = 8
                roguedefence = 8
                rogueluck = 3
                roguerange = 6
                roguemagic = 5
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", rogueattack)
                print("DEFENCE: ", roguedefence)
                print("LUCK: ", rogueluck)
                print("RANGE: ", roguerange)
                print("MAGIC: ", roguemagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")
                
        
        print("")
        print("WELCOME IN THE WORLD OF AZEROTH....")
        print("CHOOSE YOUR CITY WHERE YOU WILL BEGIN YOUR JOURNEY")
        print("1. Darnassus ")
        print("2. Erodar ")
        print("")
        Alicity = input("CHOOSE YOUR CITY: ")
        print("")
        while Alicity != "1" and Alicity != "2":
            print("Invalid input...")

        if Alicity == "1":
            print("")
            print("WELCOME TO DARNASSUS !!!")
            print("Oh, look you spawned right in front of the bank...")
            yn = input("Do you want to go inside the bank (y/n)?: ")
            print("")
            while yn != "y" and yn != "n":
                print("Invalid input...")
                yn = input("Do you want to go inside the bank (y/n)?: ")

            if yn == "y":
                money = 500
                backpackmoney = 20
                print("")
                print("You are now in the bank...")
                print("*---------------BANK---------------*")
                print("BANK ACC: ", money, " g")
                print("BACKPACK: ", backpackmoney, " g")
                print("")
                print("1. WITHDRAW: ")
                print("2. DEPOSIT: ")
                print("*----------------------------------*")
                choose = input("CHOOSE (1/2): ")
                while choose != "1" and choose != "2":
                    print("Invalid input...")
                    choose = input("CHOOSE (1/2): ")

                if choose == "1":
                    print("")
                    withdraw = int(input("WITHDRAW: "))
                    while withdraw > money:
                        print("You don't have enough money...")
                        withdraw = int(input("WITHDRAW: "))
                    money = money - withdraw
                    backpackmoney = backpackmoney + withdraw
                    print("*---------------BANK---------------*")
                    print("BANK ACC: ", money, " g")
                    print("BACKPACK: ", backpackmoney, " g")
                    print("")
                    print("1. WITHDRAW: ")
                    print("2. DEPOSIT: ")
                    print("*----------------------------------*")

                elif choose == "2":
                    print("")
                    money = backpackmoney + depositmoney
                    backpackmoney = backpackmoney - depositmoney
                    depositmoney = int(input("DEPOSIT: "))
                    print("*---------------BANK---------------*")
                    print("BANK ACC: ", money, " g")
                    print("BACKPACK: ", backpackmoney, " g")
                    print("")
                    print("1. WITHDRAW: ")
                    print("2. DEPOSIT: ")
                    print("*----------------------------------*")


            elif yn == "n":
                print("")
                print("You are now out of the bank...")

        elif Alicity == "2":
            print("")
            print("WELCOME TO ERODAR !!!")
            print("Oh, look you spawned right in front of the Pet shop...")
            yn = input("Do you want to go inside the Pet shop (y/n)?: ")
            print("")
            while yn != "y" and yn != "n":
                print("Invalid input...")
                yn = input("Do you want to go inside the Pet shop (y/n)?: ")

            if yn == "y":
                petsmoney = 500
                print("")
                print("You are now in the Pet shop...")
                print("*---------------PET SHOP---------------*")
                print("1. Wolf: 80 g             money: 500 g")
                print("2. Raptor: 100 g")
                print("3. Worm: 120 g")
                print("4. DragonHawk: 150 g")
                print("5. Riverbeast: 200 g")
                print("6. Dragon: 300 g")
                print("*--------------------------------------*")
                choose = input("CHOOSE (1/2/3/4/5/6): ")
                while choose != "1" and choose != "2" and choose != "3" and choose != "4" and choose != "5" and choose != "6":
                    print("Invalid input...")
                    choose = input("CHOOSE (1/2/3/4/5/6): ")

                if choose == "1":
                    print("")
                    print("You bought a Wolf...")
                    petsmoney = petsmoney - 80

                elif choose == "2":
                    print("")
                    print("You bought a Raptor...")
                    petsmoney = petsmoney - 100

                elif choose == "3":
                    print("")
                    print("You bought a Worm...")
                    petsmoney = petsmoney - 120

                elif choose == "4":
                    print("")
                    print("You bought a DragonHawk...")
                    petsmoney = petsmoney - 150

                elif choose == "5":
                    print("")
                    print("You bought a Riverbeast...")
                    petsmoney = petsmoney - 200

                elif choose == "6":
                    print("")
                    print("You bought a Dragon...")
                    petsmoney = petsmoney - 300

                print("")
                print("This is your start in this game so the pet will be very useful...")
                print("You need to move fast around the map to find and take your tasks faster...")
                print("Hewre you are, you can also use the pet to help you...")
                print("")
                print("Look, you got your first tasks...")
                print("--------------------TASKS--------------------")
                print("1. Kill 4 enemies...")
                print("2. Go to the central and take there the quest, bring him to the bridge...")
                print("--------------------------------------------")
                print("")

                print("Which one of the tasks do you want to do?")
                choose = input("CHOOSE (1/2): ")

                while choose != "1" and choose != "2":
                    print("Invalid input...")
                    choose = input("CHOOSE (1/2): ")

                if choose == "1":
                    print("")
                    print("Welcome in the WILSONS FOREST !!!")
                    print("On the way you see a group of enemies...")
                    print("They will try to attack you but you need to kill them...")
                    print("They are 4")
                    print("")
                    print("")
                    print("player: [", name, "] killed enemie 1")
                    print("player: [", name, "] took small damage from enemie 2")
                    print("player: [", name, "] killed enemie 2")
                    print("player: [", name, "] killed enemie 3")
                    print("player: [", name, "] took -50 damage from enemie 3 and 2")
                    print("player: [", name, "] killed enemie 4")
                    print("")
                    print("[TASK 1 COMPLETED]")
                    print("Very nice job, you killed 4 enemies...")
                    print("")
                    print("You need to go to buy some HEALTHKIT...")
                    print("player: [", name, "] bought a HEALTHKIT")
                    print("")
                    print("[TASK 2 STARTED]")
                    print("Welcome in the Central !!!")
                    print("There is a quest waiting for you...")
                    print("")
                    print("Guest: I need to go to the bridge...")
                    print(name, " : Ok, I will do it...")
                    print("")
                    print("Here we are, the bridge !!!")
                    print("[TASK 2 COMPLETED]")

                elif choose == "2":
                    print("")
                    print("Welcome in the Central !!!")
                    print("There is a quest waiting for you...")
                    print("")
                    print("Guest: I need to go to the bridge...")
                    print(name, " : Ok, I will do it...")
                    print("")
                    print("Here we are, the bridge !!!")
                    print("[TASK 2 COMPLETED]")
                    print("")
                    print("[TASK 2 STARTED]")
                    print("Welcome in the WILSONS FOREST !!!")
                    print("On the way you see a group of enemies...")
                    print("They will try to attack you but you need to kill them...")
                    print("They are 4")
                    print("")
                    print("")
                    print("player: [", name, "] killed enemie 1")
                    print("player: [", name, "] took small damage from enemie 2")
                    print("player: [", name, "] killed enemie 2")
                    print("player: [", name, "] killed enemie 3")
                    print("player: [", name, "] took -50 damage from enemie 3 and 2")
                    print("player: [", name, "] killed enemie 4")
                    print("")
                    print("[TASK 1 COMPLETED]")
                    print("Very nice job, you killed 4 enemies...")
                    print("")
                    print("You need to go to buy some HEALTHKIT...")
                    print("player: [", name, "] bought a HEALTHKIT")
                    print("")

    elif rase == "2":
        print("")
        print("")
        print("*---------------HORDE---------------*")
        print("1. Orc ")
        print("2. Undead ")
        print("3. Blood Elf ")
        print("*--------------------------------------*")
        Horde = input("CHOOSE YOUR CHARACTER FROM HORDE: ")
        while Horde != "1" and Horde != "2" and Horde != "3":
            print("Zadal si nieco zle...")
            Horde = input("CHOOSE YOUR CHARACTER FROM HORDE: ")

        if Horde == "1":
            print("")
            print("")
            print("*---------------ORC---------------*")
            print("1. Warrior ")
            print("2. Paladin ")
            print("3. Hunter ")
            print("4. Rogue ")
            print("*--------------------------------------*")
            classs = input("CHOOSE YOUR CLASS: ")
            while classs != "1" and classs != "2" and classs != "3" and classs != "4":
                print("Invalin input...")
                Aliance = input("CHOOSE YOUR CLASS: ")

            if classs == "1":
                warriorattack = 10
                warriordefence = 7
                warriorluck = 4
                warriorrange = 4
                warriormagic = 1
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", warriorattack)
                print("DEFENCE: ", warriordefence)
                print("LUCK: ", warriorluck)
                print("RANGE: ", warriorrange)
                print("MAGIC: ", warriormagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "2":
                paladinattack = 10
                paladindefence = 8
                paladinluck = 4
                paladinrange = 3
                paladinmagic = 4
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", paladinattack)
                print("DEFENCE: ", paladindefence)
                print("LUCK: ", paladinluck)
                print("RANGE: ", paladinrange)
                print("MAGIC: ", paladinmagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "3":
                hunterattack = 10
                hunterdefence = 7
                hunterluck = 2
                hunterrange = 5
                huntermagic = 2
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", hunterattack)
                print("DEFENCE: ", hunterdefence)
                print("LUCK: ", hunterluck)
                print("RANGE: ", hunterrange)
                print("MAGIC: ", huntermagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "4":
                rogueattack = 8
                roguedefence = 8
                rogueluck = 3
                roguerange = 6
                roguemagic = 5
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("NAME: ", name)
                print("ATTACK: ", rogueattack)
                print("DEFENCE: ", roguedefence)
                print("LUCK: ", rogueluck)
                print("RANGE: ", roguerange)
                print("MAGIC: ", roguemagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

        elif Horde == "2":
            print("")
            print("")
            print("*---------------UNDEAD---------------*")
            print("1. Warrior ")
            print("2. Priest ")
            print("3. Hunter ")
            print("4. Rogue ")
            print("*--------------------------------------*")
            classs = input("CHOOSE YOUR CLASS: ")
            while classs != "1" and classs != "2" and classs != "3" and classs != "4":
                print("Invalid input...")
                Aliance = input("CHOOSE YOUR CLASS: ")

            if classs == "1":
                warriorattack = 10
                warriordefence = 7
                warriorluck = 4
                warriorrange = 4
                warriormagic = 1
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", warriorattack)
                print("DEFENCE: ", warriordefence)
                print("LUCK: ", warriorluck)
                print("RANGE: ", warriorrange)
                print("MAGIC: ", warriormagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "2":
                priestattack = 7
                priestdefence = 6
                priestluck = 6.5
                priestrange = 8
                priestmagic = 7
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", priestattack)
                print("DEFENCE: ", priestdefence)
                print("LUCK: ", priestluck)
                print("RANGE: ", priestluck)
                print("MAGIC: ", priestmagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "3":
                hunterattack = 10
                hunterdefence = 7
                hunterluck = 2
                hunterrange = 5
                huntermagic = 2
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", hunterattack)
                print("DEFENCE: ", hunterdefence)
                print("LUCK: ", hunterluck)
                print("RANGE: ", hunterrange)
                print("MAGIC: ", huntermagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "4":
                rogueattack = 8
                roguedefence = 8
                rogueluck = 3
                roguerange = 6
                roguemagic = 5
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", rogueattack)
                print("DEFENCE: ", roguedefence)
                print("LUCK: ", rogueluck)
                print("RANGE: ", roguerange)
                print("MAGIC: ", roguemagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

        elif Horde == "3":
            print("")
            print("")
            print("*---------------BLOOD ELF---------------*")
            print("1. Mage ")
            print("2. Druid ")
            print("3. Hunter ")
            print("4. Rogue ")
            print("*--------------------------------------*")
            classs = input("CHOOSE YOUR CLASS: ")
            while classs != "1" and classs != "2" and classs != "3" and classs != "4":
                print("Invalid input...")
                Aliance = input("CHOOSE YOUR CLASS: ")

            if classs == "1":
                mageattack = 9.5
                magedefence = 6
                mageluck = 5
                magerange = 9
                magemagic = 8
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", mageattack)
                print("DEFENCE: ", magedefence)
                print("LUCK: ", mageluck)
                print("RANGE: ", magerange)
                print("MAGIC: ", magemagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "2":
                druidattack = 9
                druiddefence = 5
                druidluck = 7
                druidrange = 8
                druidmagic = 7
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", druidattack)
                print("DEFENCE: ", druiddefence)
                print("LUCK: ", druidluck)
                print("RANGE: ", druidrange)
                print("MAGIC: ", druidmagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "3":
                hunterattack = 10
                hunterdefence = 7
                hunterluck = 2
                hunterrange = 5
                huntermagic = 2
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", hunterattack)
                print("DEFENCE: ", hunterdefence)
                print("LUCK: ", hunterluck)
                print("RANGE: ", hunterrange)
                print("MAGIC: ", huntermagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "4":
                rogueattack = 8
                roguedefence = 8
                rogueluck = 3
                roguerange = 6
                roguemagic = 5
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: ", rogueattack)
                print("DEFENCE: ", roguedefence)
                print("LUCK: ", rogueluck)
                print("RANGE: ", roguerange)
                print("MAGIC: ", roguemagic)
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

    print("")
    print("WELCOME IN THE WORLD OF AZEROTH....")
    print("CHOOSE YOUR CITY WHERE YOU WILL BEGIN YOUR JOURNEY")
    print("1. Orgrimmar ")
    print("2. Silvermoon City ")
    print("")
    Alicity = input("CHOOSE YOUR CITY: ")
    print("")
    while Alicity != "1" and Alicity != "2":
        print("Invalid input...")

def enemyGen(levelBoss):
    temp = []
    file = open("adjective.txt","r")
    lines = file.readlines()
    adjective = lines[random.randint(0,len(lines)-1)][:-1]
    file.close
    file = open("animal.txt","r")
    lines = file.readlines()
    animal = lines[random.randint(0,len(lines)-1)][:-1]
    file.close

    if levelBoss == False:
        health = random.randint(50,100)
        attack = random.randint(10,15)
        special = random.randint(10,20)
        chance = random.randint(1,10)

        return Enemy(health, attack, special, chance, adjective+" "+animal)

    else:
        health = random.randint(200,250)
        attack = random.randint(20,40)
        special = random.randint(50,60)
        chance = random.randint(1,8)
        superMove = random.randint(100,200)

        return Boss(health, attack, special, chance, adjective+" "+animal, superMove)



def main():
    welcomescreen()
    game()
main()