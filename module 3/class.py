import random
import matplotlib.pyplot as plt
import os


class Player:
  def __init__(self, property_list, properties,money,position):
    self.property_list = property_list
    self.properties = properties
    self.money = money
    self.position = position

def simuleer_potje_monopoly(startgeld_speler):
    board_values =  [0, 60,  0,   60,  0,  200, 100, 0,   100, 120, 
                    0, 140, 150, 140, 160, 200, 180, 0,   180, 200,
                    0, 220, 0,   220, 240, 200, 260, 260, 150, 280,
                    0, 300, 300, 0,   320, 200, 0,   350, 0,   400]

    p1 = Player([0]*40,0,startgeld_speler,0)
    p2 = Player([0]*40,0,startgeld_speler,0)

    dice = []
    position = 0
    throws = 0

    # !!!cp means current player, I used an abbreviation to make the code more readable
    cp = p1
    print("throws:",throws)
    print("money:",cp.money)
    print("property:",cp.properties)
    while (p1.properties+p2.properties < 28):
        throws += 1
        dice = worp_met_twee_dobbelstenen()
        cp.position = cp. position + dice
        if (cp.position > 39):
            cp.money += 200
            cp.position = cp.position - 39
        #if (board_values[position] == 0):
            #print("Na worp ",throws,": positie",position, "(leeg)")
        if (board_values[cp.position] != 0):
            cp.properties += 1
            cp.property_list [position] = 1
            print("throws:",throws)
            print("money:",cp.money)
            print("property:",cp.properties)
            '''
            if cp.property_list [cp.position] == 0 and cp.money >= board_values[cp.position]:
                cp.money -= board_values[cp.position]
                cp.property_list [position] = 1
                cp.properties += 1
                print("player", cp)
                print("throws:",throws)
                print("money:",cp.money)
                print("property:",cp.properties)
                #print ("trump heeft huis",position," in zijn bezit, er zijn nog ", 28-trump_porperty," huizen te koop")
                '''
    return throws

def worp_met_twee_dobbelstenen():
    total = random.randint(1,6)
    total += random.randint(1,6)
    return total

#simuleer_groot_aantal_potjes_monopoly(1,1500)
simuleer_potje_monopoly(1500)