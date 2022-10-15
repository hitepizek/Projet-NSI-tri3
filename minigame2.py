import pyxel, random

minigame = 2
player_x = 512 - 5
player_y = 512 + 50
ennemi_list = []
tir_list = []
score = 0
vie = 3

def player_mouvement(x):
    global player_x
    if pyxel.btn(pyxel.KEY_D):
        if (x < 128 - 50):
            x = x + 15
    if pyxel.btn(pyxel.KEY_A):
        if (x > 0):
            x = x - 15
    return x

def ennemi_creation(ennemi_list):
    if pyxel.frame_count % 5 == 0:
        spawn = random.randint(0, 128 - 5)
        ennemi_list.append([spawn, 0])
        
def ennemi_mouvement(ennemi_list):
    global vie
    for ennemi in ennemi_list:
        ennemi[1] += 5
        if ennemi[1] >= 128:
            ennemi_list.remove(ennemi)
            vie -= 1
    return ennemi_list

def colision(tab):
    global vie, ennemi_list
    for ennemi in tab:
        if (ennemi[0] <= player_x + 50) and (ennemi[1] <= player_y + 50) and (ennemi[0] + 5 >= player_x)and \
           ( ennemi[1] + 5 >= player_y):
            ennemi_list.remove(ennemi)
            vie -= 1

def tir_creation(tir_list):
    global player_x, player_y
    if pyxel.btnp(pyxel.KEY_SPACE):
        tir_list.append([player_x + 25 - 5, player_y])


def tir_mouvement(tir_list):
    for tir in tir_list:
        tir[1] -= 10
        if tir[1] <= 0:
            tir_list.remove(tir)
    return tir_list

def tir_colision(tir_list):
    global ennemi_list, score
    for tir in tir_list:
        for ennemi in ennemi_list:
            if (tir[0] <= ennemi[0] + 5) and (tir[1] <= ennemi[1] + 5) and (tir[0] + 10 >= ennemi[0])and \
               ( tir[1] + 20 >= ennemi[1]):
                score += 1
                ennemi_list.remove(ennemi)
                tir_list.remove(tir)
                
def update_score():
    global score
    
    with open("Leaderboard/minigame2.txt", 'r') as fichier:
        text = fichier.read()
        if text == "":
            max_score = 0
        else:   
            max_score = int(text)
        if score > max_score:
            with open("Leaderboard/minigame2.txt", 'w') as fichier:
                fichier.write(str(score))
   
def update2():
    global player_x, player_y, ennemi_list, vie, minigame, tir_list, score
    minigame = 2
    player_x = player_mouvement(player_x)
    ennemi_creation(ennemi_list)
    ennemi_mouvement(ennemi_list)
    colision(ennemi_list)
    tir_creation(tir_list)
    tir_mouvement(tir_list)
    tir_colision(tir_list)
    update_score()
    if vie <= 0:
        ennemi_list = []
        tir_list = []
        minigame = 0
        vie = 3
        score = 0
        player_x = 512 - 5
        player_y = 512 + 50

    return minigame
    
def draw2():
    pyxel.cls(0)
    pyxel.rect(player_x, player_y, 50, 50, 7)
    for tir in tir_list:
        pyxel.rect(tir[0], tir[1], 10, 20, 7)
    for ennemi in ennemi_list:
        pyxel.rect(ennemi[0], ennemi[1], 5, 5, 8)