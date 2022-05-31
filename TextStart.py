

#Initialisierung:
def showInstructions():
    print('''
    Willkommen im Spukschloss

     .-.
    (o o) boo!
    | O |
    \   \\
     `~~~'

    ////////////////////////////////////////////////////////

    Entkomme über den Garten mit Zaubertrank und Schlüssel
    oder aus der Bibliothek mit dem Beam Of Mat und dem Buch des Lebens. 

    Etwas jagd dich in den Schatten. Lass dich nicht beißen.

    Commands:
        go [Richtung] (north, south, east, west)
        get[item] (Von Raum)
                    ''') 

#Status, Start und Funktionen:
def showStatus():
    #Zeige aktuellen Raum an
    print('---------------------------')
    print('You are in the ' + currentRoom)
    #Gebe Inventar aus
    print('Inventory : ' + str(Inventory))
    #Zeige Items im Raum
    if "item" in rooms[currentRoom]:
        print('You see ' + rooms[currentRoom]['item'])
    print("---------------------------") 

#Variablen zum Start:
#Inventar
Inventory = ['Coconut', 'Holy Handgrenade of Antioch']

#Dictionary für Räume
rooms = {
            'Hall'        : {  'south' : 'Kitchen',
                               'east' : 'Dining Room',
                               'north' :  'Office',
                               'west' : 'Lavatory',
                               'item'  : 'Key'
                },        
            'Kitchen'     : {  'north' : 'Hall',
                               'west' :  'Laboratory'
                                ##'item'  : 'monster
                },
            'Dining Room' : {   'west'  : 'Hall',
                                'south' : 'Garden',
                                'item'  : 'potion'
                },
            'Garden'      : {   'north' : 'Dining Room',
                                'south' : 'Libary'
                },
            'Laboratory'  : {    'east' : 'Kitchen',
                                 'item' : 'Beam-O-Mat'
                 },
            'Office'      : {    'south': 'Hall',
                                 'east': 'The Backrooms',
                                 'item' : 'Beer'

                 },
            'Libary'       : {   'north' : 'Garden',
                                 'item'  :  'BookOfLife'
                 },
            'Lavatory'     : {   'east' : 'Hall',
                                 'south' : 'The Backrooms'  
                 },
            'The Backrooms': {   'north' : 'Lavatory',
                                  'west' : 'Office'

            }

         }
#Startpunkt des Spielers
currentRoom = 'Hall'

#Monster in zufälligen Raum setzen
import random
MonsterRaum = random.choice(list(rooms))

#Initialisierung der Spielschleife
showInstructions()
while True:
    showStatus()
    ##Bewegung im Spiel, Pro Zug 1 Move, Auslesen von Fehler und Exit
    move = ''
    ##Start der Bewegungsschleife
    while move == '':
    ##Eingabe der Bewegungsrichtung und Angleich GroßkleinSchreibung
        move = input('>')
    move = move.lower().split()
    ##Spieler beendet mit Eingabe von Exit
    if move[0] == "exit":
        break
    ##Spieler gibt Richtung der Bewegung ein. Richtung wird mit Dictionary Rooms abgeglichen
    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
    ##Abgleich mit Dictionary Rooms ist falsch oder Eingabe ungültig
            print('Dort kannst du nicht weitergehen')
    ##Aufheben von Gegenständen, Pro Aufheben 1 Zug, Auslesen von Fehlern
    if move[0] == 'get' :
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            Inventory += [move[1]]
            print(move[1] + ' got!')
            del rooms[currentRoom]['item']
        else:
            print('Can\'t get ' + move[1] + '!')
    ##Extra Leben: Setze Monster um und entferne Handgranate und renne Weg
    if currentRoom == MonsterRaum and 'Holy Handgrenade of Antioch' in Inventory:
        print('''THE MIGHTY RABBIT OF CAERBANNOG LURKS IN THE SHADOW OF THE ROOM...
              ADVENTOURUS AS YOU ARE YOU ATTEMPT TO SCARE IT AWAY

        
              And the Lord spake, saying, "First shalt thou take out the Holy Pin.
              Then, shalt thou count to three. No more. No less. 
              Three shalt be the number thou shalt count, and the number of the counting shall be three.
              Four shalt thou not count,
              nor either count thou two, excepting that thou then proceed to three.
              Five is right out. Once the number three, being the third number, be reached,  
              then, lobbest thou thy Holy Hand Grenade of Antioch towards thy foe, who,
              being naughty in My sight, shall snuff it."

            The Monster moved someplace else. You ran away
            ''')
        #Verändere Spielwelt: Entferne Handgranate, gehe zurück zur Halle, Neuer Raum für Monster
        Inventory.pop(1)
        currentRoom = 'Hall'
        MonsterRaum = random.choice(list(rooms))
    ##Verlierbedingungen Hase kriegt dich
    if currentRoom == MonsterRaum and 'Holy Handgrenade of Antioch' not in Inventory:
        print('The Rabbit of Caerbannog has got you... GAME OVER!')
        break
    ##Siegbedingung Garten mit Schlüssel 
    if currentRoom == 'Garden' and 'Key' in Inventory and 'potion' in Inventory:
        print('You escaped the Spukschloss... YOU WIN!')
        break
    ##Siegbedingung Labor mit Beamer und Buch
    if currentRoom == 'Laboratoy' and 'Beam-O-Mat' in Inventory and 'BookOfLife' in Inventory:
        print('You escaped the Spukschloss... YOU WIN!')
        break

