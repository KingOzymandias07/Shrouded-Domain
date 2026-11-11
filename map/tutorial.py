from vars.classes import Room
from vars.descriptions import *

tut_1 = Room("Entrance", "TUT EnR.txt", "TUT")
tut_2 = Room("North Room", "TUT NR.txt", "TUT")
tut_3 = Room("West Room", "TUT WR.txt", "TUT")
tut_4 = Room("East Room", "TUT ER.txt", "TUT")
tut_5 = Room("Unlocked Room", "TUT UR.txt", "TUT")
tut_5.locked = True
tut_6 = Room("Lever Room", "TUT LR.txt", "TUT")
tut_7 = Room("A Different Room", "TUT DR.txt", "TUT")
tut_7.locked = True
tut_8 = Room("Talk Room", "TUT TR.txt", "TUT")
tut_8.locked = True
tut_9 = Room("Exit Room", "TUT ExR.txt", "TUT")
tut_9.locked = True

tut_1.add_connections("north", tut_2)
tut_1.add_connections("east", tut_4)
tut_1.add_connections("west", tut_3)

tut_2.add_connections("north", tut_5)
tut_2.add_connections("south", tut_1)
tut_2.add_connections("west", tut_6)

tut_3.add_connections("north", tut_6)
tut_3.add_connections("east", tut_1)

tut_4.add_connections("east", tut_7)
tut_4.add_connections("west", tut_1)

tut_5.add_connections("south", tut_2)

tut_6.add_connections("north", tut_9)
tut_6.add_connections("east", tut_2)
tut_6.add_connections("south", tut_3)

tut_7.add_connections("north", tut_8)
tut_7.add_connections("west", tut_4)

tut_8.add_connections("south", tut_7)

tut_9.add_connections("south", tut_6)