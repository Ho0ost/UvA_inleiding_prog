import random
import matplotlib.pyplot as plt
import os

def simuleer_groot_aantal_potjes_monopoly(aantal_potjes, startgeld_speler):
    games_list = []
    cnt = 0
    for i in range(0, aantal_potjes):
        cnt += 1
        ammount_of_throws = simuleer_potje_monopoly(startgeld_speler)
        games_list.append(ammount_of_throws)
        if cnt >= 500:
            cnt = 0
            os.system("cls")
            print(round(((i/aantal_potjes)*100),1),"percent complete")
    average_throws = sum(games_list)/aantal_potjes
    print("Monopoly simulator: 1 speler,",startgeld_speler,"euro startgeld", aantal_potjes,"potjes gespeeld")
    print("Gemiddeld duurde het",average_throws,"worpen voor de speler alle straten in zijn bezit had")
    plt.hist(games_list, bins=50)
    plt.show()

    return average_throws
    
def simuleer_potje_monopoly(startgeld_speler):
    board_values =  [0, 60,  0,   60,  0,  200, 100, 0,   100, 120, 
                    0, 140, 150, 140, 160, 200, 180, 0,   180, 200,
                    0, 220, 0,   220, 240, 200, 260, 260, 150, 280,
                    0, 300, 300, 0,   320, 200, 0,   350, 0,   400]
    player_property_list = [0]*40
    player_porperty = 0
    player_money = startgeld_speler
    dice = []
    position = 0
    throws = 0
    while (player_porperty < 28):
        dice = worp_met_twee_dobbelstenen()
        throws += 1
        position += dice
        if (position > 39):
            player_money += 200
            position = position - 40

        if (board_values[position] != 0):
            if player_property_list [position] == 0 and player_money >= board_values[position]:
                player_money -= board_values[position]
                player_property_list [position] = 1
                player_porperty += 1

    return throws

def worp_met_twee_dobbelstenen():
    total = random.randint(1,6)
    total += random.randint(1,6)
    return total

simuleer_groot_aantal_potjes_monopoly(10000,1500)
