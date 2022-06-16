from pprint import pprint
import random
import time
import math

'''
Alliance
'''
class Alliance:
    def __init__(self, Ahealth, Aattack, Adefence, Aname):
        self.Ahealth = Ahealth
        self.Aattack = Aattack
        self.Adefence = Adefence
        self.Aname = Aname

    def gethealth(self):
        return self.Ahealth
    def getattack(self):
        return self.Aattack
    def getdefence(self):
        return self.Adefence
    def getname(self):
        return self.Aname

    def sethealth(self, newhealth):
        self.Ahealth = newhealth
    def setattack(self, newattack):
        self.Aattack = newattack
    def setdefence(self, newdefence):
        self.Adefence = newdefence
    def setname(self, newname):
        self.Aname = newname

class Clovek(Alliance):
    def __init__(self, Ahealth, Aattack, Adefence, Aname):
        super().__init__(Ahealth, Aattack, Adefence, Aname)

class Dwarf(Alliance):
    def __init__(self, Ahealth, Aattack, Adefence, Aname):
        super().__init__(Ahealth, Aattack, Adefence, Aname)


class NightElf(Alliance):
    def __init__(self, Ahealth, Aattack, Adefence, Aname):
        super().__init__(Ahealth, Aattack, Adefence, Aname)
#------------------------------------------------------------------------------------#

'''
Horda
'''
class Horde(Alliance):
    def __init__(self, Ahealth, Aattack, Adefence, Aname):
        super().__init__(Ahealth, Aattack, Adefence, Aname)   

class Orc(Alliance):
    def __init__(self, Ahealth, Aattack, Adefence, Aname):
        super().__init__(Ahealth, Aattack, Adefence, Aname)

class Undead(Alliance):
    def __init__(self, Ahealth, Aattack, Adefence, Aname):
        super().__init__(Ahealth, Aattack, Adefence, Aname)

class BloodElf(Alliance):
    def __init__(self, Ahealth, Aattack, Adefence, Aname):
        super().__init__(Ahealth, Aattack, Adefence, Aname)
#------------------------------------------------------------------------------------#

'''
Enemy
'''
class Enemy:
    def __init__(self, Ehealth, Eattack, Edefence, Especial, Ename):
        self.health = Ehealth
        self.attack = Eattack
        self.special = Especial
        self.defence = Edefence
        self.name = Ename

    def gethealth(self):
        return self.health
    def getattack(self):
        return self.attack
    def getSpecial (self):
        return self.special
    def getDefence(self):
        return self.defence
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
    def __init__(self, Ehealth, Eattack, Edefence, Especial,EsuperMove, Ename):
        super().__init__(Ehealth, Eattack, Edefence, Especial, Ename)

        self.superMove = EsuperMove

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


def vytvoreniepostavy():
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
        print("1. Human ")
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
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 10")
                print("DEFENCE: 10")
                print("HEALTH: 100")
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "2":
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 15")
                print("DEFENCE: 8")
                print("HEALTH: 100")
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "3":
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 17")
                print("DEFENCE: 8")
                print("HEALTH: 100")
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "4":
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")

                name = input("NAME OF YOUR CHARACTER: ")
                print("NAME: ", name)
                print("ATTACK: 15")
                print("DEFENCE: 8")
                print("HEALTH: 100")
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
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 10")
                print("DEFENCE: 10")
                print("HEALTH: 100")
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "2":
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 15")
                print("DEFENCE: 8")
                print("HEALTH: 100")
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "3":
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 17")
                print("DEFENCE: 8")
                print("HEALTH: 100")
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "4":
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("NAME: ", name)
                print("ATTACK: 12")
                print("DEFENCE: 12")
                print("HEALTH: 100")
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
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")

                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 9")
                print("DEFENCE: 15")
                print("HEALTH: 100")
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "2":
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 15")
                print("DEFENCE: 6")
                print("HEALTH: 100")
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "3":
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 17")
                print("DEFENCE: 8")
                print("HEALTH: 100")
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "4":
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 12")
                print("DEFENCE: 12")
                print("HEALTH: 100")
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
                    print("")
                    print("")
                    print("Look, you got your first tasks...")
                    print("--------------------TASKS--------------------")
                    print("1. Kill 2 enemies...")
                    print("2. Move to the next city and take from the bank 2000 g and bring them back to Palace...")
                    print("--------------------------------------------")
                    print("")
                    choose = input("CHOOSE (1/2): ")
                    while choose != "1" and choose != "2":
                        print("Invalid input...")
                        choose = input("CHOOSE (1/2): ")

                    if choose == "1":
                        print("")
                        print("[TASK 1 STARTED]")
                        print("You are out of the bank...")
                        print("Ah, look there are some enemies...")
                        print("They want to attack you..")
                        print("")
                        a = input("")
                        print("player: [ " ,name, " ] took -20 of his 100 health points")
                        print("player: [ " ,name, " ] killed an enemy")
                        print("player: [ " ,name, " ] took -12 of his 100 health points")
                        print("player: [ " ,name, " ] killed an 2nd enemy")
                        print("")
                        print("[TASK 1 COMPLETED]")
                        a = input()
                        print("")
                        print("[TASK 2 STARTED]")
                        print("Lets go to the next city...")
                        print("player: [ " ,name, " ] moved to the next city")
                        print("player: [ " ,name, " ] took 2000 g from bank")
                        print("player: [ " ,name, " ] brought 2000 g came back to his city")
                        print("player: [ " ,name, " ] moved to the Palace")
                        print("player: [ " ,name, " ] gave 2000 g to the Palace")
                        print("[TASK 2 COMPLETED]")
                        print("")
                        print("")
                        print("You made great job today !!!")
                        print("You can go to the pub and drink some beer...")
                        print("player: [ " ,name, " ] moved to the pub")
                        print("player: [ " ,name, " ] drank a beer")
                        print("player: [ " ,name, " ] drank next beer")
                        print("player: [ " ,name, " ] drank next beer")
                        print("player: [ " ,name, " ] came back to home")
                        c = input()
                        print("")
                        print("In front of your house is some Horde enemie...")
                        print("He wants to kill you...")
                        
                        print("")
                        player = Alliance(100, 21, 20, "Human")
                        player.gethealth(100)
                        player.getattack(21)
                        player.getdefence(20)
                        player.getname("Warrior")
                        
                        player2 = Alliance(100, 20, 10, "Skeleton")
                        player2.gethealth(100)
                        player2.getattack(20)
                        player2.getdefence(10)
                        player2.getname("Skeleton")
                        damage = player.gethealth - player2.getattack + player.getdefence
                        damage2 = player2.gethealth - player.getattack + player2.getdefence
                        print("player: [",name,"] started fight")
                        print("player2: [Horde] started fight")
                        print("player: [",name,"] get a damage ", damage)
                        print("player2: [Horde] get a damage ", damage2)
                        print("")

                            

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

                    print("")
                    print("")
                    print("Look, you got your first tasks...")
                    print("--------------------TASKS--------------------")
                    print("1. Kill 2 enemies...")
                    print("2. Move to the next city and take from the bank 2000 g and bring them back to Palace...")
                    print("--------------------------------------------")
                    print("")

                    choose = input("CHOOSE (1/2): ")
                    while choose != "1" and choose != "2":
                        print("Invalid input...")
                        choose = input("CHOOSE (1/2): ")

                    if choose == "1":
                        print("")
                        print("[TASK 1 STARTED]")
                        print("You are out of the bank...")
                        print("Ah, look there are some enemies...")
                        print("They want to attack you..")
                        print("")
                        a = input("")
                        print("player: [ " ,name, " ] took -20 of his 100 health points")
                        print("player: [ " ,name, " ] killed an enemy")
                        print("player: [ " ,name, " ] took -12 of his 100 health points")
                        print("player: [ " ,name, " ] killed an 2nd enemy")
                        print("")
                        print("[TASK 1 COMPLETED]")
                        a = input()
                        print("")
                        print("[TASK 2 STARTED]")
                        print("Lets go to the next city...")
                        print("player: [ " ,name, " ] moved to the next city")
                        print("player: [ " ,name, " ] took 2000 g from bank")
                        print("player: [ " ,name, " ] brought 2000 g came back to his city")
                        print("player: [ " ,name, " ] moved to the Palace")
                        print("player: [ " ,name, " ] gave 2000 g to the Palace")
                        print("[TASK 2 COMPLETED]")
                        print("")
                        print("")
                        print("You made great job today !!!")
                        print("You can go to the pub and drink some beer...")
                        print("player: [ " ,name, " ] moved to the pub")
                        print("player: [ " ,name, " ] drank a beer")
                        print("player: [ " ,name, " ] drank next beer")
                        print("player: [ " ,name, " ] drank next beer")
                        print("player: [ " ,name, " ] came back to home")
                        c = input()
                        print("")
                        print("In front of your house is some Horde enemie...")
                        print("He wants to kill you...")
                        
                        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##
                        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##
                        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##

                    elif choose == "2":
                        print("")
                        print("[TASK 1 STARTED]")
                        print("Lets go to the next city...")
                        print("player: [ " ,name, " ] moved to the next city")
                        print("player: [ " ,name, " ] took 2000 g from bank")
                        print("player: [ " ,name, " ] brought 2000 g came back to his city")
                        print("player: [ " ,name, " ] moved to the Palace")
                        print("player: [ " ,name, " ] gave 2000 g to the Palace")
                        print("[TASK 1 COMPLETED]")
                        a = input()
                        print("")
                        print("[TASK 1 STARTED]")
                        print("You are out of the bank...")
                        print("Ah, look there are some enemies...")
                        print("They want to attack you..")
                        print("")
                        a = input("")
                        print("player: [ " ,name, " ] took -20 of his 100 health points")
                        print("player: [ " ,name, " ] killed an enemy")
                        print("player: [ " ,name, " ] took -12 of his 100 health points")
                        print("player: [ " ,name, " ] killed an 2nd enemy")
                        print("")
                        print("[TASK 1 COMPLETED]")
                        print("")
                        print("")
                        print("You made great job today !!!")
                        print("You can go to the pub and drink some beer...")
                        print("player: [ " ,name, " ] moved to the pub")
                        print("player: [ " ,name, " ] drank a beer")
                        print("player: [ " ,name, " ] drank next beer")
                        print("player: [ " ,name, " ] drank next beer")
                        print("player: [ " ,name, " ] came back to home")
                        c = input()
                        print("")
                        print("In front of your house is some Horde enemie...")
                        print("He wants to kill you...")

                        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##
                        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##
                        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##

            elif yn == "n":
                print("")
                print("You are now in the city...")
                print("Here we go, lets go to the barbershop...")
                print("player: [", name, "] goes to the barbershop")
                print("player: [", name, "] took a seat")
                print("player: [", name, "] took red hair")
                print("player: [", name, "] took a long hair")
                print("player: [", name, "] took a big beard")
                print("player: [", name, "] took a red T-hirt")
                print("player: [", name, "] took a black shorts")
                print("player: [", name, "] exited the barbershop")
                print("player: [", name, "] went to the pub")
                print("player: [", name, "] took a beer")
                print("player: [", name, "] took a next beer")
                print("player: [", name, "] is drunk")
                print("")
                b = input()
                print("You are very drunnk now...")
                print("Move to your house and go sleep...")
                print("player: [", name, "] went to the house")
                print("player: [", name, "] went sleep")
                a = input()
                print("Good Morning!!!")
                print("You are very tired now...")
                print("Go to Pet shop and buy a pet...")
                c = input()
                print("player: [", name, "] went to the pet shop")
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

                print("Move fast to your house, someone burned your house...")
                print("player: [", name, "] went to the house")
                print("")
                print("Look at the house, it is very burnt...")
                print("There is running some Horde player...")
                print("Try to catch him !!!")
                print("")
                print("player: [", name, "] caught the Horde player")
                print("player: [", name, "] started fighting")

                ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##
                ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##
                ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##

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
                    v = input()
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
                    a = input()
                    print("You need to go to buy some HEALTHKIT...")
                    print("player: [", name, "] bought a HEALTHKIT")
                    print("")
                    b = input() 
                    print("[TASK 2 STARTED]")
                    c = input()
                    print("Welcome in the Central !!!")
                    print("There is a quest waiting for you...")
                    print("")
                    print("Guest: I need to go to the bridge...")
                    print(name, " : Ok, I will do it...")
                    print("")
                    print("Here we are, the bridge !!!")
                    print("[TASK 2 COMPLETED]")
                    print("")
                    print("")
                    print("You made great job today !!!")
                    print("You can go to the pub and drink some beer...")
                    print("player: [ " ,name, " ] moved to the pub")
                    print("player: [ " ,name, " ] drank a beer")
                    print("player: [ " ,name, " ] drank next beer")
                    print("player: [ " ,name, " ] drank next beer")
                    print("player: [ " ,name, " ] came back to home")
                    c = input()
                    print("")
                    print("In front of your house is some Horde enemie...")
                    print("He wants to kill you...")

                    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##
                    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##
                    ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##


                elif choose == "2":
                    print("")
                    print("[TASK 1 STARTED]")
                    print("Welcome in the Central !!!")
                    print("There is a quest waiting for you...")
                    print("")
                    print("Guest: I need to go to the bridge...")
                    print(name, " : Ok, I will do it...")
                    print("")
                    print("Here we are, the bridge !!!")
                    print("[TASK 1 COMPLETED]")
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
                    print("")
                    print("You made great job today !!!")
                    print("You can go to the pub and drink some beer...")
                    print("player: [ " ,name, " ] moved to the pub")
                    print("player: [ " ,name, " ] drank a beer")
                    print("player: [ " ,name, " ] drank next beer")
                    print("player: [ " ,name, " ] drank next beer")
                    print("player: [ " ,name, " ] came back to home")
                    c = input()
                    print("")
                    print("In front of your house is some Horde enemie...")
                    print("He wants to kill you...")
            
            elif yn == "n":
                print("You are out of the Pet shop")
                print("You are going to Pub...")
                print("player: [",name,"] came to the Pub")
                print("player: [",name,"] drank a beer")
                print("player: [",name,"] drank next beer")
                print("player: [",name,"] drank next beer")
                print("")
                c = input()
                print("You are out lets go home..")
                print("player: [",name,"] came back in front of home")
                print("")
                print("In front of your house is some Horde enemie...")
                print("He wants to kill you...")

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
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 10")
                print("DEFENCE: 10")
                print("HEALTH: 100")
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "2":
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 15")
                print("DEFENCE: 8")
                print("HEALTH: 100")
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "3":
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 17")
                print("DEFENCE: 8")
                print("HEALTH: 100")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "4":
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("NAME: ", name)
                print("ATTACK: 12")
                print("DEFENCE: 12")
                print("HEALTH: 100")
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
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")

                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 10")
                print("DEFENCE: 10")
                print("HEALTH: 100")
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "2":
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 16")
                print("DEFENCE: 8")
                print("HEALTH: 100")
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "3":
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 17")
                print("DEFENCE: 8")
                print("HEALTH: 100")
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "4":
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 12")
                print("DEFENCE: 12")
                print("HEALTH: 100")
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
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 10")
                print("DEFENCE: 12")
                print("HEALTH: 100")
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "2":
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 16")
                print("DEFENCE: 8")
                print("HEALTH: 100")
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "3":
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 17")
                print("DEFENCE: 8")
                print("HEALTH: 100")
                print("")
                print("Now we can start to play your own adventure.... WELCOME")

            elif classs == "4":
                player = Alliance(100, 21, 20, "Human")
                player.gethealth(100)
                player.getattack(21)
                player.getdefence(20)
                player.getname("Warrior")
                
                player2 = Alliance(100, 20, 10, "Skeleton")
                player2.gethealth(100)
                player2.getattack(20)
                player2.getdefence(10)
                player2.getname("Skeleton")
                print("")
                name = input("NAME OF YOUR CHARACTER: ")
                print("")
                print("NAME: ", name)
                print("ATTACK: 12")
                print("DEFENCE: 12")
                print("HEALTH: 100")
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

    if Alicity == "1":
        print("")
        print("You have chosen Orgrimmar")
        print("")
        print("You have chosen to start your journey in the city of Orgrimmar")
        print("Tell me where you want to go?: ")
        print("1. Pet shop ")
        choose = input("CHOOSE YOUR PATH: ")
        while choose != "1":
            print("Invalid input...")
            choose = input("CHOOSE YOUR PATH: ")

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
        print("1. Kill the Worgen")
        print("2. Go to the Palace of the Sunstrider and take the poison...")
        print("--------------------------------------------")
        choose = input("CHOOSE (1/2): ")
        while choose != "1" and choose != "2":
            print("Invalid input...")
            choose = input("CHOOSE (1/2): ")

        if choose == "1":
            print("Look, there is a Worgen in the forest...")
            print("You need to kill him...")
            print("[TASK 1 STARTED]")
            print("")
            print("player: [" , name , "] gave to Worgen -50 hp")
            print("player: [" , name , "] gave to Worgen -18 hp")
            print("NPC: [ Worgen ] gave to [" ,name, "] -20 hp")
            print("player: [" , name , "] killed the Worgen")
            print("[TASK 1 COMPLETED]")
            print("")
            print("Here you got your second task...")
            enter = input()
            print("")
            print("[TASK 2 STARTED]")
            print("You need to go to the Palace of the Sunstrider and take the poison...")
            print("Bring the poison to the small house where lives the magician...")
            print("")
            enter = input()
            print("")
            print("player: [" , name , "] came to the Palace of the Sunstrider")
            print("player: [" , name , "] took the poison")
            print("player: [" , name , "] came to small house")
            print("player: [" , name , "] gave to Magician the poison")
            print("[TASK 2 FINISHED]")
            print("")
            print("You made great job today !!!")
            print("You can go to the pub and drink some beer...")
            print("player: [ " ,name, " ] moved to the pub")
            print("player: [ " ,name, " ] drank a beer")
            print("player: [ " ,name, " ] drank next beer")
            print("player: [ " ,name, " ] drank next beer")
            print("player: [ " ,name, " ] came back to home")
            c = input()
            print("")
            print("In front of your house is some Horde enemie...")
            print("He wants to kill you...")


            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##

        elif choose == "2":
            print("")
            print("[TASK 1 STARTED]")
            print("You need to go to the Palace of the Sunstrider and take the poison...")
            print("Bring the poison to the small house where lives the magician...")
            print("")
            enter = input()
            print("")
            print("player: [" , name , "] came to the Palace of the Sunstrider")
            print("player: [" , name , "] took the poison")
            print("player: [" , name , "] came to small house")
            print("player: [" , name , "] gave to Magician the poison")
            print("[TASK 1 FINISHED]")
            print("Here you got your second task...")
            enter = input()
            print("Look, there is a Worgen in the forest...")
            print("You need to kill him...")
            print("[TASK 1 STARTED]")
            print("")
            print("player: [" , name , "] gave to Worgen -50 hp")
            print("player: [" , name , "] gave to Worgen -18 hp")
            print("NPC: [ Worgen ] gave to [" ,name, "] -20 hp")
            print("player: [" , name , "] killed the Worgen")
            print("[TASK 1 COMPLETED]")
            print("")
            print("")
            print("You made great job today !!!")
            print("You can go to the pub and drink some beer...")
            print("player: [ " ,name, " ] moved to the pub")
            print("player: [ " ,name, " ] drank a beer")
            print("player: [ " ,name, " ] drank next beer")
            print("player: [ " ,name, " ] drank next beer")
            print("player: [ " ,name, " ] came back to home")
            c = input()
            print("")
            print("In front of your house is some Horde enemie...")
            print("He wants to kill you...")
                
        

            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##
            ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##

    elif Alicity == "2":
        print("")
        print("You have chosen Silvermoon City")
        print("")
        print("You have chosen to start your journey in the city of Silvermoon City")
        print("Tell me where you want to go?: ")
        print("1. Bank ")
        print("2. Pet Shop")
        choose = input("CHOOSE YOUR PATH: ")
        while choose != "1":
            print("Invalid input...")
            choose = input("CHOOSE YOUR PATH: ")

        

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
    vytvoreniepostavy()
main()