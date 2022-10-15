import pyxel
from Minigame1 import minigame1
from Minigame2 import minigame2
from Minigame3 import minigame3

pyxel.init(128, 128, title="Projet Tri3")


player_x = 64 - 6.25
player_y = 64 - 6.25
minigame = 0
def player_mouvement(x, y):
    if pyxel.btn(pyxel.KEY_D):
        if (x < 140):
            x = x + 8
    if pyxel.btn(pyxel.KEY_A):
        if (x > 0):
            x = x - 8
    if pyxel.btn(pyxel.KEY_S):
        if (y < 118):
            y = y + 8
    if pyxel.btn(pyxel.KEY_W):
        if (y > 0):
            y = y - 8
    return x, y

def colision():
    global minigame, player_x, player_y   
    if ( 87.5 <= player_x + 6.25 ) and ( 87.5 <= player_y + 6.25 ) and ( 87.5 + 6.25 >= player_x) and \
       ( 87.5 + 6.25 >= player_y):
        minigame = 1
    if ( 25 <= player_x + 6.25 ) and ( 25 <= player_y + 6.25 ) and ( 25 + 6.25 >= player_x) and \
       ( 25 + 6.25 >= player_y):
        minigame = 2
    if ( 25 <= player_x + 6.25 ) and ( 87.5 <= player_y + 6.25 ) and ( 25 + 6.25 >= player_x) and \
       ( 87.5 + 6.25 >= player_y):
        minigame = 3

def update():
    global player_x, player_y, minigame
    colision()
    player_x, player_y = player_mouvement(player_x, player_y)
    if minigame == 1:
        minigame = minigame1.update1()
        if minigame == 0:
            player_x = 64 - 6.25
            player_y = 64 - 6.25
    if minigame == 2:
        minigame = minigame2.update2()
        if minigame == 0:
            player_x = 64 - 6.25
            player_y = 64 - 6.25
    if minigame == 3:
        minigame = minigame3.update3()
        if minigame == 0:
            player_x = 64 - 6.25
            player_y = 64 - 6.25

def draw():
    pyxel.cls(0)
    pyxel.rect(player_x, player_y, 6.25, 6.25, 7)
    pyxel.rect(87.5, 87.5, 6.25, 6.25, 7) 
    pyxel.rect(25, 25, 6.25, 6.25, 9)
    pyxel.rect(25, 87.5, 6.25, 6.25, 5)
    if minigame == 1:
        minigame1.draw1()
    if minigame == 2:
        minigame2.draw2()
    if minigame == 3:
        minigame3.draw3()
        
pyxel.run(update, draw)