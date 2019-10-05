import random
import matplotlib.pyplot as plt
import os


class Player:
  def __init__(self, property_list, properties,money,position, name):
    self.property_list = property_list
    self.properties = properties
    self.money = money
    self.position = position
    self.name = name


def simuleer_groot_aantal_potjes_monopoly(aantal_potjes, startgeld_speler_1, startgeld_speler_2):
    games_list = []
    cnt = 0
    for i in range(0, aantal_potjes):
        cnt += 1
        street_difference = simuleer_potje_monopoly(startgeld_speler_1, startgeld_speler_2)
        games_list.append(street_difference)
        if cnt >= 500:
            cnt = 0
            os.system("cls")
            print("{}/5 met {} euro start geld".format(int(((startgeld_speler_2-startgeld_speler_1)/50)+1),startgeld_speler_2))
            print(round(((i/aantal_potjes)*100),1),"'%' complete")
    avg_more_streets = (sum(games_list)/aantal_potjes)
    '''
    print("Monopoly simulator: twee spelers, {} potjes".format(aantal_potjes))
    print("player 1: {} euro startgeld".format(startgeld_speler_1))
    print("player 2: {} euro startgeld".format(startgeld_speler_2))
    print("Gemiddeld heeft speler 1 {} meer straten in bezit als alle straten verdeeld zijn".format(avg_more_streets))
    '''
    return avg_more_streets
    
def simuleer_potje_monopoly(startgeld_speler_1, startgeld_speler_2):
    board_values =  [0, 60,  0,   60,  -200,  200, 100, 0,   100, 120, 
                    0, 140, 150, 140, 160, 200, 180, 0,   180, 200,
                    0, 220, 0,   220, 240, 200, 260, 260, 150, 280,
                    0, 300, 300, 0,   320, 200, 0,   350, -100,400]

    p1 = Player([0]*40,0,startgeld_speler_1,0,"michael")
    p2 = Player([0]*40,0,startgeld_speler_2,0,"slang")

    dice = []
    throws = 0

    # !!!cp means current player, I used an abbreviation to make the code more readable
    cp = p1

    while (p1.properties+p2.properties < 28):
        throws += 1
        dice = worp_met_twee_dobbelstenen()
        cp.position = cp.position + dice
        if (cp.position > 39):
            cp.money += 200
            cp.position = cp.position - 40
        if (board_values[cp.position] != 0):
            if (board_values[cp.position] < 0):
                cp.money += board_values[cp.position]
            elif cp.property_list [cp.position] == 0 and cp.money >= board_values[cp.position]:
                cp.money -= board_values[cp.position]
                board_values[cp.position] = 0
                cp.property_list [cp.position] = board_values[cp.position]
                cp.properties += 1
        if (cp.name == p1.name):
            cp = p2
        elif (cp.name == p2.name):
            cp = p1
    cp = p1
    '''
    for i in range(2):
        print("##########################")
        print("player", cp.name)
        print("throws:",throws)
        print("money:",cp.money)
        print("property:",cp.properties)
        cp = p2
    '''
    #street_difference = p1.properties - p2.properties
    return p1.properties - p2.properties

def worp_met_twee_dobbelstenen():
    total = random.randint(1,6)
    total += random.randint(1,6)
    return total

def evenwicht():
    money_p2 = 1500
    street_difference_list = []
    for i in range (5):
        street_difference = (simuleer_groot_aantal_potjes_monopoly(5000,1500,money_p2))
        street_difference_list.append(street_difference)
        money_p2 += 50
        plt.plot(money_p2-1500, street_difference, 'go')
    plt.show()      
    plt.xlabel('extra start geld')
    plt.ylabel('verschil in straaten')
    return street_difference_list


avg_list = evenwicht()
print (avg_list)