
#Code by Benstitou Sofiane (carrelebo), start the 12/21/2021
#Terminal interface experimentation for futur python libraries

#code editor and system that I used during tge development:
#-app : Vim (code editor), OS : Regolith Linux (Ubuntu 20.04.3 based)

#version of the program make for unix systems : Mac OS, Linux and BSD

import os

print("\nwelcome to carre's bakery, for more informations type 'help' on the shell.\n")

#global variables:

wallet = 50

have_bread = 0
have_croissant = 0

def bakery():
    global wallet
    global have_bread
    global have_croissant

    no_else_bug = False #for not have error message with other conditions

    bread = 10
    croissant = 20
    
    bread_price = bread / 2
    croissant_price = croissant / 2

    shell = input("carré's bakery$ ")

#help command------------------------------------------------------------

    if 'help' in shell:
        if len(shell) == 4:
            no_else_bug = True
            print("""
avaible commands:

[help] -> to see avaible and correct commands

[exit] -> for quit the program

[clear] -> for clear the terminal program (depends on your OS)

[article] -> to see avaible articles on the bakery

[money] -> to see how much money have you on your wallet

[buy (article)] -> to buy an avaible bakery's article and their prices

[inventory] -> to see what's are they on your invertory

[sell (article)] -> to sell an article

""")
        if len(shell) != 4:
            no_else_bug = True
            print(f"\nError, '{shell}' is not the correct command -> the correct command is 'help'.\n")

#exit command------------------------------------------------------------

    if 'exit' in shell:
        if len(shell) == 4:
            no_else_bug = True
            print("\nS e e ~ y o u ~ s o o n . . .\n")
            quit()
    
        if len(shell) != 4:
            no_else_bug = True
            print(f"\nError, '{shell}' is not the correct command -> the correct command is 'exit'\n")

#clear command-----------------------------------------------------------

    if 'clear' in shell:
        if len(shell) == 5:
            no_else_bug = True
            os.system('clear')
        if len(shell) != 5:
            no_else_bug = True
            print(f"\nError, '{shell}' is not the correct command -> 'clear' is the correct command.\n")

#article command---------------------------------------------------------

    if 'article' in shell:
        if len(shell) == 7:
            no_else_bug = True
            print(f"""
articles:

-bread: 
buy price -> {bread}$
sell price -> {bread_price}$

-croissant :
buy price -> {croissant}$
sell price -> {croissant_price}$
""")
        if len(shell) != 7:
            no_else_bug = True
            print(f"\nError, '{shell}' is not the correct command -> the correct command is 'article'.\n")

#money command-----------------------------------------------------------
    
    if 'money' in shell:
        if len(shell) == 5:
            no_else_bug = True
            print(f"\nYou've {wallet}$ on your wallet.\n")
        
        if len(shell) != 5:
            no_else_bug = True
            print(f"\nError, '{shell}' is not the correct command -> the correct command is 'money'.\n")
#buy commands-----------------------------------------------------------

#-1 buy bread------------------------------------------------------------
    
    if 'buy bread' in shell or shell == 'buybread':
        if len(shell) == 9:

            if wallet < bread:
                print("\nYou've not enough money to buy a bread -> more informations with 'money' and 'article' commands\n")
                bakery()

            no_else_bug = True
            wallet -= bread
            have_bread += 1
            print(f"\nYou're having bought 1 bread -> you've now {wallet}$ on your wallet, and {have_bread} bread in your inventory\n")

        if len(shell) > 9 or len(shell) < 9 or 'buybread' in shell:
            no_else_bug = True
            print(f"\nError, '{shell}' is not the correct command -> the correct command is 'buy bread'.\n")

#-2 buy croissant--------------------------------------------------------

    if 'buy croissant' in shell or shell == 'buycroissant':
        if len(shell) == 13:

            if wallet < croissant:
                print("\nYou've not enough money to buy a croissant -> more informations with 'money' and 'article' commands.\n")
                bakery()

            no_else_bug = True
            wallet -= croissant
            have_croissant += 1
            print(f"\n You're having bought 1 croissant -> you've now {wallet}$ in your wallet and {have_croissant} croissant on your inventory\n")

        if len(shell) < 13 or len(shell) > 13 or 'buycroissant' in shell:
            no_else_bug = True
            print(f"\nError, '{shell}' is not the correct command -> the correct command is 'buy croissant'.\n")

#inventory command-------------------------------------------------------

    if 'inventory' in shell:
        if len(shell) == 9:
            no_else_bug = True
            print(f"""
Your inventory :

-number of bread : {have_bread}

-number of croissant : {have_croissant}

""")
        if len(shell) != 9:
            no_else_bug = True
            print(f"\nError, '{shell}' is not the correct command -> the correct command is 'inventory\n")


#sell commands-----------------------------------------------------------

#-1 sell bread command------------------------------------------------------
    if 'sell bread' in shell or shell == 'sellbread':

        if len(shell) == 10:
            if have_bread <= 0:
                
                print("\nYou've not enough bread to sell one -> more informations with 'inventory' command\n")
                bakery()
                
            no_else_bug = True
            have_bread -= 1
            wallet += bread_price
            print(f"\nYou're having sold a bread -> you've now {wallet}$ on your wallet and {have_bread} bread in your inventory\n")

        if len(shell) < 10 or len(shell) > 10 or 'sellbread' in shell:
            no_else_bug = True
            print(f"\nError, '{shell}' is not the correct command -> the correct command is 'sell bread'.\n")


#-2 sell croissant--------------------------------------------------------  
    if 'sell croissant' in shell or shell == 'sellcroissant':
        
        if len(shell) == 14:

            if have_croissant <= 0:
                print("\nYou've not enough croissant to sell one -> more informations with 'inventory' command.\n")
                bakery()

            no_else_bug = True
            have_croissant -= 1
            wallet += croissant_price
            print(f"\nYou're having sold a croissant -> you've now {wallet}$ on your wallet and {have_croissant} croissant on your invontory.\n")

        if len(shell) < 14 or len(shell) > 14 or 'sellcroissant' in shell:
            no_else_bug = True
            print(f"\nError, {shell} is not the correct command -> the correct command is 'sell croissant'\n")
            
#else any----------------------------------------------------------------
    if no_else_bug != True:
        print(f"\nError, '{shell}' is not an avaible or correct command -> more informations with 'help' command.\n")

    bakery()

bakery()
