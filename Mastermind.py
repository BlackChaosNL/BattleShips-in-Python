import turtle
import random
import time


def vierkant(fcolor, size, pcolor, psize):
    t.pen(fillcolor=fcolor, pencolor=pcolor, pensize=psize)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()


def raster(lijst, startx, starty, movex, movey, aanty, aantx, size, fcolor, pcolor, psize):
    startcoor = [startx, starty]
    for y in range(aanty):
        rij = []
        for x in range(aantx):
            goto(startcoor)
            rij.append([startcoor[0], startcoor[1]])
            if fcolor == "kleur":
                vierkant(fcolor=kleuren[x], size=size, pcolor=kleuren[x], psize=psize)
            else:
                vierkant(fcolor=fcolor, size=size, pcolor=pcolor, psize=psize)
            startcoor[0] += movex
        startcoor[0] = startx
        startcoor[1] -= movey
        lijst.append(rij)


def speelveld():
    generatecode()
    print(code)
    raster(lijst=raster1, startx=-225, starty=325, movex=50, movey=50, aanty=12, aantx=4, size=35, fcolor="black", pcolor="grey", psize=3)
    raster(lijst=raster2, startx=-20, starty=318, movex=30, movey=50, aanty=12, aantx=4, size=20, fcolor="black", pcolor="grey", psize=2)
    raster(lijst=raster3, startx=-225, starty=-280, movex=58, movey=0, aanty=1, aantx=6, size=25, fcolor="kleur", pcolor="grey", psize=2)
    berekencoordinaten(invoer=raster3, uitvoer=coorraster3)


def goto(coor):
    t.penup()
    t.goto(coor)
    t.pendown()


def generatecode():
    gencode = []
    code.clear()
    for i in range(4):
        gencode.append(kleuren[r(0, 5)])
    append(lijst=gencode, bestemming=code)


def append(lijst, bestemming):
    plaats = 0
    for posities in lijst:
        bestemming.append(lijst[plaats])
        plaats += 1


def animatie():
    for i in pogingcode:
        window.bgcolor(i)
        time.sleep(0.5)
    window.bgcolor("black")


def klik(x, y):
    global positierij, positiekolom
    print(checkkleur(x=x, y=y))
    if checkkleur(x=x, y=y) and positiekolom <= 11:
        kleur = checkkleur(x=x, y=y)[1]
        pogingcode.append(kleur)
        goto(raster1[positiekolom][positierij])
        vierkant(fcolor=kleur, size=35, pcolor="black", psize=3)
        positierij += 1
        if positierij >= 4:
            # bevestiging()
            if pogingcode == code:
                resetpositie()
                speelveld()
                animatie()
            else:
                if positiekolom >= 11:
                    resetpositie()
                    speelveld()
                else:
                    positiekolom += 1
                    positierij = 0
            pogingcode.clear()


#def bevestiging():
#    raster(lijst=None, startx=0, starty=0, movex=0, movey=0, aantx=1, aanty=1, size=35, fcolor="green", pcolor="green", psize=3)



def resetpositie():
    global positiekolom, positierij
    positierij = 0
    positiekolom = 0


def checkkleur(x, y):
    for i in range(6):
        if [x, y] in coorraster3[i]:
            return True, kleuren[i]


def berekencoordinaten(invoer, uitvoer):
    teller = 0
    while teller != 6:
        lijst = []
        xcoor = invoer[0][teller][0]
        ycoor = invoer[0][teller][1]
        for y in range(25):
            for x in range(25):
                xcoor += 1
                lijst.append([xcoor, ycoor])
            xcoor = invoer[0][teller][0]
            ycoor -= 1
        uitvoer.append(lijst)
        teller += 1


positierij = 0
positiekolom = 0
r = random.randint
kleuren = ["yellow", "green", "red", "blue", "purple", "orange"]
raster1 = []
raster2 = []
raster3 = []
coorraster3 = []
pogingcode = []
code = []
t = turtle
t.setup(width=500, height=700, startx=0, starty=0)
t.speed("fastest")
t.delay(0)
t.hideturtle()
window = t.Screen()
window.title("Crack the master's mind!  -  Build 0.1.3")
window.bgcolor("black")
goto([-200, 330])
speelveld()
window.onclick(klik)
window.mainloop()