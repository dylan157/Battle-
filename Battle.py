#!/usr/bin/env python
import time
import random
from sys import platform
import os
# Notes: add defensive fight option/ add defence to dictionary/ [add items, add a quest]
# Reminder: I know it can be improved.

if platform == "linux" or platform == "linux2":
    clear = lambda: os.system('clear')
elif platform == "darwin":
    clear = lambda: os.system('clear')
elif platform == "win32":
    clear = lambda: os.system('cls')

ran = random.randint 

#Player stats
player = {
    "health": 100,
    "attack": 100
    }
enemy = {
    "health": 100,
    "attack": 80
    }



# These functions are only here for re-using
def attack(attack):
    damage = attack / ran(1, 10) 
    return damage

def hit(attack, enattack):
    chance = attack - enattack + 5 * ran(1, 5)
    enchance = attack - enattack + 5 * ran(1, 5)
    if chance > enchance:
        return True
    else:
        return False
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    


#
def fight():
    
    def hit(attack, enattack):
        chance = attack - enattack + 5 * ran(1, 5)
        enchance = attack - enattack + 5 * ran(1, 5)
        if chance > enchance:
            return True
        else:
            return False

    def attack(attack):
        damage = attack / ran(1, 10)
        return damage

    time.sleep(1)
    clear()
    print "You have chosen to fight!" 
    time.sleep(1)
    battle = True

    while battle == True:
        if player["health"] <= 0:
            clear()
            print "You Are Dead"
            battle = False
        elif enemy["health"] <= 0: 
            clear()
            print "You killed the enemy!"
            battle = False

        def playerattack():

            def hit(attack, enattack):
                chance = attack - enattack + 5 * ran(1, (player["attack"] / 2)) # all the comments are written in enemy attack.
                enchance = attack - enattack + 4 * ran(1, (enemy["attack"] / 2))
                if chance > enchance:
                    return True
                else:
                    return False

            def attack(attack):
                damage = attack / ran(1, 10)
                return damage

            if player["health"] > 0 and enemy["health"] > 0:
                clear()
                print "You throw a punch!" #add more items!!!!
                time.sleep(1)
                if hit(player["attack"], enemy["attack"]):
                    hit = attack(player["attack"])
                    enemy["health"] -= hit
                    if enemy["health"] <= 0:
                        enemy["health"] = 0
                        

                    print "you hit the enemy with " + str(hit) + " points of damage!  -" + str(enemy["health"]) + " HP Remaining"
                    time.sleep(1)
                else:

                    print "You missed!"
            else:
                battle = False
                return battle


        def enemyattack():

            if enemy["health"] > 0 and player["health"] > 0:

                def hit(attack, enattack): # decides if current fighter will hit depending on compared attack levels.
                    chance = attack - enattack + 5 * ran(1, (enemy["attack"] / 2))
                    enchance = attack - enattack + 4 * ran(1, (player["attack"] / 2))
                    if chance > enchance:
                        return True
                    else:
                        return False

                def attack(attack): # decides attack damage
                    damage = attack / ran(1, 10)
                    return damage


                print "The enemy lunges at you!!" #add attack methods!!!
                time.sleep(1)
                if hit(enemy["attack"], player["attack"]):# If player 'hit':
                    hit = attack(enemy["attack"]) # Decide attack damage
                    player["health"] -= hit
                    if player["health"] <= 0: # If player health is negative, health = 0 (No more -### health after large attacks)
                        player["health"] = 0
                    

                    print "The enemy hit you with " + str(hit) + " points of damage!  -" + str(player["health"]) + " #HP Remaining"
                    time.sleep(1)
                else:

                    print "They missed!"
                
            else:
                battle = False
                return battle


        who = ran(1, 2)# 50/50 turn chance despite attack level.
        #print str(who) + " = Decider" #debugger
        if who == 1:
            playerattack()
        else:
            enemyattack()

    print player
    print enemy

    

def game(): # Welcome to game blah blah
    clear()
    print "Welcome to battle!"
    
    time.sleep(1)#
    clear()
    print "You are up against an enemy!"
    time.sleep(1)

    def q1():
        clear()
        d1 = raw_input("Do you 'fight' or 'run'?")
        if d1 == 'fight' or d1 == "f":
            fight()
        elif d1 == 'run': # hi james
            print "r"
        elif d1 == "edit":
            player["health"]
        else:
            print 'what?'
            q1()
    q1()

game()

# 185L  This program is my first automatic pvm game. The mechanics are to be expanded but are usefull for re-using.
