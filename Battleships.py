# Gemaakt door Jeroen Vijgen
# Klas ICT-11

import string;
import random;
import datetime, time;

#   Main functie om de game te starten m.b.v. een keuzemenu.#
#
#   VAR     |   TYPE        |   EXPLANATION
# -------------------------------------------------------------------------------------
#   NONE    |   NONE        |   NONE
# 
def main():
    print("Welkom bij Zeeslag!");
    print("Je kunt kiezen uit SinglePlayer(S), Two Player Game(T) of Quit(Q). Of \"Cheat\" jij?");
    select = input("Maak een keuze(S/T/Q):");
    if(select.upper() == "S"):
        createSinglePlayerGame();
    elif(select.upper() == "T"):
        createMultiPlayerGame();
    elif(select.upper() == "CHEAT"):
        createSinglePlayerGame(True);
    elif(select.upper() == "Q"):
        print("Dankjewel voor het spelen van Zeeslag! Doei!");
        input();
        exit();
    else:
        print("Dat was geen geldige input vriend, probeer het opnieuw!");
        main();

#   Creëren van een singleplayer instantie.
#
#   VAR     |   TYPE        |   EXPLANATION
# -------------------------------------------------------------------------------------
#   CHEATING|   BOOLEAN     |   Cheaten? (0/1)   

def createSinglePlayerGame(cheating = False):
    c = cheating;
    startTime = time.time();
    spBoard = createBoard();
    printBoard(spBoard);
    obj = [randomShip(0, createShips()[0][1][0], random.randrange(0,2)),
           randomShip(1, createShips()[1][1][0], random.randrange(0,2)),
           randomShip(2, createShips()[2][1][0], random.randrange(0,2)),
           randomShip(3, createShips()[3][1][0], random.randrange(0,2)),
           randomShip(4, createShips()[4][1][0], random.randrange(0,2))];
    i = False;
    attemptsMadeByUser = 0;
    while(i != True):
        attemptsMadeByUser += 1;
        placeBoard(playerInput(), spBoard, obj, c);
        i = checkWon(spBoard, obj);
    print(time.time()-startTime);
    print("U heeft", attemptsMadeByUser,"gebruikt om alles te raden");
    print("Daarnaast heeft u alles geraden in: ", time.time()-startTime,"second(en)");

#   Creëren van een multiplayer instantie.
#   LET OP: DIT WERKT NOG NIET.
#   VAR     |   TYPE        |   EXPLANATION
# -------------------------------------------------------------------------------------
#   NONE    |   NONE        |   NONE
# 

def createMultiPlayerGame():
    keuze = input("Wilt u een (E)igen bord maken, of met een (R)andom bord spelen?");
    if(keuze.upper() == "E"):
        print("Deze werkt nog niet");
    elif(keuze.upper() == "R"):
        print("Deze werkt nog");
    else:
        print("Dit klopt niet, probeer opnieuw.");
        createSinglePlayerGame();
    print("");

#   playerInput :           Het uit elkaar halen van de spelerinput voor een X/Y coördinaat
#   VAR     |   TYPE        |   EXPLANATION
# -------------------------------------------------------------------------------------
#   NONE    |   NONE        |   NONE
# -------------------------------------------------------------------------------------
#   Returns : X/Y coördinaat in LIJST vorm.
def playerInput():
    playerInput = input("Voer een veld in waar je een (B)om wilt plaatsen(Bijv A01):");
    if(len(playerInput) > 3 or not playerInput.strip(" ") or len(playerInput) < 2):
        print("Hier klopt iets niet!?");
        print("Probeer opnieuw!");
    x = playerInput[0];
    if(ord(x.upper())-65 < 0 or ord(x.upper())-65 > 9):
        print("Hier klopt iets niet, de rij bestaat niet.");
    else:
        x = ord(x.upper())-65;
    if(playerInput[1:3] is None or playerInput[1:3]==''):
        print("Hier klopt iets niet, de rij bestaat niet.");
        createSinglePlayerGame();
    y = int(playerInput[1:3])-1;
    if(y > 10):
        print("Hier klopt iets niet, probeer het opnieuw.")
        playerInput();
    return [x, y];

#   createBoard :           Creëren van een multiplayer instantie.
#   VAR     |   TYPE        |   EXPLANATION
# -------------------------------------------------------------------------------------
#   NONE    |   NONE        |   NONE
# -------------------------------------------------------------------------------------
#   Returns :   10 bij 10 grid van '.'tjes in een LIST.
#
def createBoard():
    board = [['.' for x in range(10)] for y in range(10)];
    return board;

#   printBoard  :           Creëren van een multiplayer instantie.
#   VAR     |   TYPE        |   EXPLANATION
# -------------------------------------------------------------------------------------
#   NONE    |   NONE        |   NONE
# -------------------------------------------------------------------------------------
#   Returns :   Print het bord van 10 bij 10. Daarnaast voegt hij de hoofdletters van A t/m J in, en 1 t/m 10 aan de onderkant.
#

def printBoard(board):
    i = 0;
    for i in range(len(board)):
        print(string.ascii_uppercase[i], board[i][0], board[i][1], board[i][2], board[i][3], board[i][4], board[i][5], board[i][6], board[i][7], board[i][8], board[i][9]); 
    print("  1 2 3 4 5 6 7 8 9 10");

#   placeBoard      :   Checkt of boten geraakt zijn of niet.
#   VAR             |   TYPE        |   EXPLANATION
# -------------------------------------------------------------------------------------
#   coordinates     |   ARRAY       |   Gebruiker ingevulde X/Y coördinaat.
#   board           |   ARRAY       |   Bord in LIJST vorm.
#   filledInShips   |   ARRAY       |   De ingevulde schepen in LIJST vorm.
#   cheating        |   BOOLEAN     |   Cheaten? (Y/N)
# -------------------------------------------------------------------------------------
#   

def placeBoard(coordinates, board, filledInShips, cheating = False):
    c = 0;
    oceaan = positioningShip(filledInShips);
    if(cheating == True):
            print("U bent nu aan het cheaten.");
            while(c != 17):
                board[oceaan[c][0]][oceaan[c][1]] = "#"
                c += 1;
    board[coordinates[0]][coordinates[1]] = "B"
    printBoard(board);
    n = input("Weet u zeker dat u hier een bom wilt plaatsen?(Y/N)");
    if(n.upper() == "Y"):
        if coordinates in oceaan:
            board[coordinates[0]][coordinates[1]] = "#";
        else:
            board[coordinates[0]][coordinates[1]] = "-";
        printBoard(board);
    elif(n.upper() == "N"):
        board[coordinates[0]][coordinates[1]] = ".";
        printBoard(board);
    else:
        print("Je hebt iets ingegeven wat niet klopt, probeer het opnieuw.")

#   randomShip      :   "Out of Bounds" check schepen
#   VAR             |   TYPE        |   EXPLANATION
# -------------------------------------------------------------------------------------
#   shipId          |   ARRAY       |   Enkel schip in LIJST vorm.
#   size            |   INT         |   Size van de boot in INT vorm. ( Om mee te tellen )
#   orientation     |   BOOLEAN     |   Z coördinaat. ( 0 Horizontaal, 1 Verticaal. )
# -------------------------------------------------------------------------------------
#   returns         :   Schip met een "Out of Bounds" check, dit betekent dat een boot van vijf maar maximaal kan randomen van 0 tot 5.
#

def randomShip(shipId, size, orientation):
    if(orientation == 0):
        a = 10-size+1;
        x = random.randrange(0,9);
        y = random.randrange(0,a);
        return setShip(createShips()[shipId], x, y, orientation);
    else:
        a = 10-size+1;
        x = random.randrange(0,a);
        y = random.randrange(0,9);
        return setShip(createShips()[shipId], x, y, orientation);

#   UItschrijven van de posities van de schepen
#   VAR     |   TYPE        |   EXPLANATION
# -------------------------------------------------------------------------------------
#   boat    |   ARRAY        |   Een lijst met ingevulde boten.
# -------------------------------------------------------------------------------------
#   Returns :   LIST met de uitgevulde coördinaten van alle schepen op het bord.
#

def positioningShip(boat):
    boatPos = [];
    i = 0;
    while(i != len(boat)):
        length = boat[i][1][0];
        x = boat[i][1][1];
        y = boat[i][1][2];
        z = boat[i][1][3];
        p = 0;
        if(z == 1):
            p == 0;
            while(p != length):
                boatPos.append([x+p,y]);
                p += 1;
        else:
            p == 0;
            while(p != length):
                boatPos.append([x,y+p]);
                p += 1;
        i += 1;
    return boatPos;

#   createShips :           Creëren van de boten die op het schip komen te staan in een lijst.
#   VAR     |   TYPE        |   EXPLANATION
# -------------------------------------------------------------------------------------
#   NONE    |   NONE        |   NONE
# -------------------------------------------------------------------------------------
#   Returns :   Een lijst met beschikbare boten.
#

def createShips():
    availableShips = [];
    createShips = 0;
    battleShip = 0;
    cruzerShip = 0;
    fregatShip = 0;
    minesweeperShip = 0;
    x = 0; # Kolom 
    y = 0; # Item in kolom ( rij )
    z = 0; # Positionering ( Horizontaal(0) / Verticaal(1) )
    while(createShips != 5):
        while(battleShip != 1):
            availableShips.append(["battleship",[5, x, y, z]]);
            battleShip += 1;
        while(cruzerShip != 1):
            availableShips.append(["cruzer",[4, x, y, z]]);
            cruzerShip += 1;
        while(fregatShip != 2):
            availableShips.append(["fregat"+str(fregatShip),[3, x, y, z]]);
            fregatShip += 1;
        while(minesweeperShip != 1):
            availableShips.append(["minesweeper",[2, x, y, z]]);
            minesweeperShip += 1;
        createShips += 1
    return availableShips;

#   setShip :   Setten van het X/Y/Z coördinaat van een boot in een lijst.
#   VAR     |   TYPE        |   EXPLANATION
# -------------------------------------------------------------------------------------
#   obj     |   ARRAY       |   Boot.
#   x       |   INT         |   X coördinaat op het bord.
#   y       |   INT         |   Y coördinaat op het bord.
#   z       |   INT         |   Z coördinaat. ( 0 Horizontaal, 1 Verticaal. )
# -------------------------------------------------------------------------------------
#   Returns :   Schip met ingevulde coördinaten in lijst vorm.
#

def setShip(obj, x, y, z):
    obj[1][1] = x;
    obj[1][2] = y;
    obj[1][3] = z;
    return obj;

#   checkWon:   Check op het bord of een speler gewonnen heeft of niet.
#   VAR     |   TYPE        |   EXPLANATION
# -------------------------------------------------------------------------------------
#   board   |   ARRAY       |   Bord in lijst vorm ( Waar #, - en . op geplot worden )
#   obj     |   ARRAY       |   Lijst met op het bord bestaande boten.
# -------------------------------------------------------------------------------------
#   Returns :   True: Niet gewonnen of False: Wel gewonnen ( Om de loop te doorbreken )
#

def checkWon(board, obj):
    i = 0;
    hit = 0;
    while(i != len(board)):
        u = 0;
        while(u != 9):
            if(board[i][u] == "#"):
                hit+=1;
            u += 1;
        i += 1;
    if(hit >= 16):
        return True;
    else:
        return False;
# Initialiseer het programma.
main();
