from vars.classes import Room
from vars.descriptions import *

#    ==================================
#            JOHNSON HALL ROOMS
#    ==================================

    #Johnson Exterior ROOMS
john_front          =   Room("Infront of Johnson Hall", "JH (Ext) Front.txt",       "ext")
john_side_n         =   Room("North of Johnson Hall",   "JH (Ext) North Side.txt",  "ext")
john_back           =   Room("Behind Johnson Hall",     "JH (Ext) Back.txt",        "ext")

    #Johnson 1st Floor ROOMS
john_lobby          =   Room("Lobby",                           "JH (1st) Lobby.txt",           "1st")
john_common         =   Room("Common Room",                     "JH (1st) Common Room.txt",     "1st")
john_hall_1         =   Room("Hallway",                         "JH (1st) Hallway.txt",         "1st")
john_kitchen        =   Room("Kitchen",                         "JH (1st) Kitchen.txt",         "1st")
john_1stair_n       =   Room("1st Floor Northern Staircase",    "JH (1st) North Stairs.txt",    "stair")
john_1stair_n.locked    =   True
john_1stair_s       =   Room("1st Floor Southern Staircase",    "JH (1st) South Stairs.txt",    "stair")
john_1stair_s.locked    =   True
john_hall_1sub      =   Room("Hallway",                         "JH (1st) Hallway Subarea.txt", "1st")
john_hall_1_long1   =   Room("Long Hallway",                    "JH (1st) Long Hall 1.txt",     "1st")
john_hall_1_long2   =   Room("Long Hallway",                    "JH (1st) Long Hall 2.txt",     "1st")
john_hall_1_long3   =   Room("Long Hallway",                    "JH (1st) Long Hall 3.txt",     "1st")
john_bathroom_1     =   Room("Bathroom",                        "JH (1st) Bathroom.txt",        "1st")
john_bathroom_1.locked  =   True
john_suite          =   Room("Matron's Suite",                  "JH (1st) Suite.txt",           "1st")
john_room1          =   Room("Room 1",                          "JH (1st) Room 1.txt",          "1st")
john_room2          =   Room("Room 2",                          "JH (1st) Room 2.txt",          "1st")
john_room3          =   Room("Room 3",                          "JH (1st) Room 3.txt",          "1st")
john_room4          =   Room("Room 4",                          "JH (1st) Room 4.txt",          "1st")
john_room4.locked       =   True
john_room5          =   Room("Room 5",                          "JH (1st) Room 5.txt",          "1st")
john_room7          =   Room("Room 7",                          "JH (1st) Room 7.txt",          "1st")
john_room8          =   Room("Room 8",                          "JH (1st) Room 8.txt",          "1st")

    #Johnson 2nd Floor ROOMS
john_2stair_n       =   Room("2nd Floor Northern Staircase",    "JH (2nd) North Stairs.txt",   "stair")
john_2stair_s       =   Room("2nd Floor Southern Staircase",    "JH (2nd) South Stairs.txt",   "stair")
john_hall_2_long1   =   Room("Long Hallway",                    "JH (2nd) Long Hall 1.txt",    "2nd")
john_hall_2_long2   =   Room("Long Hallway",                    "JH (2nd) Long Hall 2.txt",    "2nd")
john_hall_2_long3   =   Room("Long Hallway",                    "JH (2nd) Long Hall 3.txt",    "2nd")
john_hall_2_long4   =   Room("Long Hallway",                    "JH (2nd) Long Hall 4.txt",    "2nd")
john_hall_2_long5   =   Room("Long Hallway",                    "JH (2nd) Long Hall 5.txt",    "2nd")
john_hall_2_long6   =   Room("Long Hallway",                    "JH (2nd) Long Hall 6.txt",    "2nd")
john_hall_2_long7   =   Room("Long Hallway",                    "JH (2nd) Long Hall 7.txt",    "2nd")
john_hall_2_long8   =   Room("Long Hallway",                    "JH (2nd) Long Hall 8.txt",    "2nd")
john_room20         =   Room("Room 20",                         "JH (2nd) Room 20.txt",        "2nd")
john_room21         =   Room("Room 21",                         "JH (2nd) Room 21.txt",        "2nd")
john_room22         =   Room("Room 22",                         "JH (2nd) Room 22.txt",        "2nd")
john_room23         =   Room("Room 23",                         "JH (2nd) Room 23.txt",        "2nd")
john_room24         =   Room("Room 24",                         "JH (2nd) Room 24.txt",        "2nd")
john_room25         =   Room("Room 25",                         "JH (2nd) Room 25.txt",        "2nd")
john_room26         =   Room("Room 26",                         "JH (2nd) Room 26.txt",        "2nd")
john_room27         =   Room("Room 27",                         "JH (2nd) Room 27.txt",        "2nd")
john_room28         =   Room("Room 28",                         "JH (2nd) Room 28.txt",        "2nd")
john_room29         =   Room("Room 29",                         "JH (2nd) Room 29.txt",        "2nd")
john_room30         =   Room("Room 30",                         "JH (2nd) Room 30.txt",        "2nd")
john_room31         =   Room("Room 31",                         "JH (2nd) Room 31.txt",        "2nd")
john_room32         =   Room("Room 32",                         "JH (2nd) Room 32.txt",        "2nd")
john_room33         =   Room("Room 33",                         "JH (2nd) Room 33.txt",        "2nd")
john_bathroom_2     =   Room("Bathroom",                        "JH (2nd) Bathroom.txt",       "2nd")

    #Johnson 3rd Floor ROOMS
john_3stair_n       =   Room("3rd Floor Northern Staircase",    "JH (3rd) North Stairs.txt",   "stair")
john_3stair_s       =   Room("3rd Floor Southern Staircase",    "JH (3rd) South Stairs.txt",   "stair")
john_hall_3_long1   =   Room("Long Hallway",                    "JH (3rd) Long Hall 1.txt",    "3rd")
john_hall_3_long2   =   Room("Long Hallway",                    "JH (3rd) Long Hall 2.txt",    "3rd")
john_hall_3_long3   =   Room("Long Hallway",                    "JH (3rd) Long Hall 3.txt",    "3rd")
john_hall_3_long4   =   Room("Long Hallway",                    "JH (3rd) Long Hall 4.txt",    "3rd")
john_room40         =   Room("Room 40",                         "JH (3rd) Room 20.txt",        "3rd")
john_room41         =   Room("Room 41",                         "JH (3rd) Room 20.txt",        "3rd")
john_room42         =   Room("Room 42",                         "JH (3rd) Room 20.txt",        "3rd")
john_room43         =   Room("Room 43",                         "JH (3rd) Room 20.txt",        "3rd")
john_room44         =   Room("Room 44",                         "JH (3rd) Room 20.txt",        "3rd")
john_room45         =   Room("Room 45",                         "JH (3rd) Room 20.txt",        "3rd")
john_room46         =   Room("Room 46",                         "JH (3rd) Room 20.txt",        "3rd")
john_room47         =   Room("Room 47",                         "JH (3rd) Room 20.txt",        "3rd")
john_room48         =   Room("Room 48",                         "JH (3rd) Room 20.txt",        "3rd")
john_room49         =   Room("Room 49",                         "JH (3rd) Room 20.txt",        "3rd")
john_bathroom_3     =   Room("Bathroom",                        "JH (3rd) Bathroom.txt",       "3rd")

### Johnson Exterior CONNECTIONS ###

    #Johnosn Front 
john_front.add_connections("north", john_side_n)
john_front.add_connections("west",  john_lobby)

    #Johnson Back 
john_back.add_connections("north",  john_side_n)
john_back.add_connections("east",   john_hall_1sub)

    #North of Johnson Hall 
john_side_n.add_connections("east", john_front)
john_side_n.add_connections("west", john_back)


### Johnson 1st Floor CONNECTIONS ###

    #Johnson Lobby 
john_lobby.add_connections("east",  john_front)
john_lobby.add_connections("south", john_common)
john_lobby.add_connections("west",  john_hall_1)

    #Johnson Common Room 
john_common.add_connections("north",    john_lobby)
john_common.add_connections("west",     john_kitchen)

    #Johnson Hall 1 
john_hall_1.add_connections("north",    john_hall_1_long1)
john_hall_1.add_connections("east",     john_lobby)
john_hall_1.add_connections("south",    john_1stair_s)
john_hall_1.add_connections("west",     john_hall_1sub)

    #Johnson Kitchen
john_kitchen.add_connections("east",    john_common)

    #Johnson Northern Staircase 
john_1stair_n.add_connections("up",     john_2stair_n)
john_1stair_n.add_connections("east",   john_room4)
john_1stair_n.add_connections("south",  john_hall_1_long3)

    #Johnson Southern Staircase 
john_1stair_s.add_connections("up",     john_2stair_s)
john_1stair_s.add_connections("north",  john_hall_1)

    #Johnson Hall Sub Area 
john_hall_1sub.add_connections("north",         john_suite)
john_hall_1sub.add_connections("east",          john_hall_1)
john_hall_1sub.add_connections("south east",    john_room8)
john_hall_1sub.add_connections("south west",    john_room7)
john_hall_1sub.add_connections("west",          john_back)

    #Johnson 1st Long Hall Pt. 1 
john_hall_1_long1.add_connections("north",  john_hall_1_long2)
john_hall_1_long1.add_connections("east",   john_room1)
john_hall_1_long1.add_connections("south",  john_hall_1)

    #Johnson 1st Long Hall Pt. 2 
john_hall_1_long2.add_connections("north",  john_hall_1_long3)
john_hall_1_long2.add_connections("east",   john_room2)
john_hall_1_long2.add_connections("south",  john_hall_1_long1)
john_hall_1_long2.add_connections("west",   john_bathroom_1)

    #Johnson 1st Long Hall Pt. 3 
john_hall_1_long3.add_connections("north",  john_1stair_n)
john_hall_1_long3.add_connections("east",   john_room3)
john_hall_1_long3.add_connections("south",  john_hall_1_long2)
john_hall_1_long3.add_connections("west",   john_room5)

    #Johnson Rooms
john_suite.add_connections("south",         john_hall_1sub)
john_room1.add_connections("west",          john_hall_1_long1)
john_room2.add_connections("west",          john_hall_1_long2)
john_room3.add_connections("west",          john_hall_1_long3)
john_room4.add_connections("west",          john_1stair_n)
john_room5.add_connections("east",          john_hall_1_long3)
john_room7.add_connections("north east",    john_hall_1sub)
john_room8.add_connections("north west",    john_hall_1sub)

    #Johnson Bathroom
john_bathroom_1.add_connections("east",     john_hall_1_long2)


### Johnson 2nd Floor CONNECTIONS ###

    #Johnson Northern Staircase
john_2stair_n.add_connections("up",     john_3stair_n)
john_2stair_n.add_connections("down",   john_1stair_n)
john_2stair_n.add_connections("east",   john_room24)
john_2stair_n.add_connections("south",  john_hall_2_long1)

    #Johnson 2nd Long Hall Pt. 1
john_hall_2_long1.add_connections("north",  john_2stair_n)
john_hall_2_long1.add_connections("east",   john_room23)
john_hall_2_long1.add_connections("south",  john_hall_2_long2)
john_hall_2_long1.add_connections("west",   john_room25)

    #Johnson 2nd Long Hall Pt. 2
john_hall_2_long2.add_connections("north",  john_hall_2_long1)
john_hall_2_long2.add_connections("east",   john_room22)
john_hall_2_long2.add_connections("south",  john_hall_2_long3)
john_hall_2_long2.add_connections("west",   john_bathroom_2)

    #Johnson 2nd Long Hall Pt. 3
john_hall_2_long3.add_connections("north",  john_hall_2_long2)
john_hall_2_long3.add_connections("east",   john_room21)
john_hall_2_long3.add_connections("south",  john_hall_2_long4)
john_hall_2_long3.add_connections("west",   john_room26)

    #Johnson 2nd Long Hall Pt. 4
john_hall_2_long4.add_connections("north",  john_hall_2_long3)
john_hall_2_long4.add_connections("east",   john_room20)
john_hall_2_long4.add_connections("south",  john_hall_2_long5)
john_hall_2_long4.add_connections("west",   john_room27)

    #Johnson 2nd Long Hall Pt. 5
john_hall_2_long5.add_connections("north",  john_hall_2_long4)
john_hall_2_long5.add_connections("east",   john_2stair_s)
john_hall_2_long5.add_connections("south",  john_hall_2_long6)
john_hall_2_long5.add_connections("west",   john_room28)

    #Johnson 2nd Long Hall Pt. 6
john_hall_2_long6.add_connections("north",  john_hall_2_long5)
john_hall_2_long6.add_connections("east",   john_hall_2_long7)
john_hall_2_long6.add_connections("south",  john_room30)
john_hall_2_long6.add_connections("west",   john_room29)

    #Johnson 2nd Long Hall Pt. 7
john_hall_2_long7.add_connections("east",   john_hall_2_long8)
john_hall_2_long7.add_connections("south",  john_room31)
john_hall_2_long7.add_connections("west",   john_hall_2_long6)

    #Johnson 2nd Long Hall Pt. 8
john_hall_2_long8.add_connections("east",   john_room33)
john_hall_2_long8.add_connections("south",  john_room32)
john_hall_2_long8.add_connections("west",   john_hall_2_long7)

    #Johnson Southern Staircase
john_2stair_s.add_connections("up",     john_3stair_s)
john_2stair_s.add_connections("down",   john_1stair_s)
john_2stair_s.add_connections("west",   john_hall_2_long5)

    #Johnson Rooms
john_room20.add_connections("west",     john_hall_2_long4)
john_room21.add_connections("west",     john_hall_2_long3)
john_room22.add_connections("west",     john_hall_2_long2)
john_room23.add_connections("west",     john_hall_2_long1)
john_room24.add_connections("west",     john_2stair_n)
john_room25.add_connections("east",     john_hall_2_long1)
john_room26.add_connections("east",     john_hall_2_long3)
john_room27.add_connections("east",     john_hall_2_long4)
john_room28.add_connections("east",     john_hall_2_long5)
john_room29.add_connections("east",     john_hall_2_long6)
john_room30.add_connections("north",    john_hall_2_long6)
john_room31.add_connections("north",    john_hall_2_long7)
john_room31.add_connections("north",    john_hall_2_long8)
john_room33.add_connections("west",     john_hall_2_long8)

    #Johnson Bathroom
john_bathroom_2.add_connections("east",     john_hall_2_long2)


### Johnson 3rd Floor CONNECTIONS ###

    #Johnson Northern Staircase
john_3stair_n.add_connections("down",   john_2stair_n)
john_3stair_n.add_connections("east",   john_room43)
john_3stair_n.add_connections("south",  john_hall_3_long1)

    #Johnson 3rd Long Hall Pt. 1
john_hall_3_long1.add_connections("north",  john_3stair_n)
john_hall_3_long1.add_connections("east",   john_room42)
john_hall_3_long1.add_connections("south",  john_hall_3_long2)
john_hall_3_long1.add_connections("west",   john_room44)

    #Johnson 3rd Long Hall Pt. 2
john_hall_3_long2.add_connections("north",  john_hall_3_long1)
john_hall_3_long2.add_connections("east",   john_room41)
john_hall_3_long2.add_connections("south",  john_hall_3_long3)
john_hall_3_long2.add_connections("west",   john_bathroom_3)

    #Johnson 3rd Long Hall Pt. 3
john_hall_3_long3.add_connections("north",  john_hall_3_long2)
john_hall_3_long3.add_connections("east",   john_room40)
john_hall_3_long3.add_connections("south",  john_hall_3_long4)
john_hall_3_long3.add_connections("west",   john_room45)

    #Johnson 3rd Long Hall Pt. 4
john_hall_3_long4.add_connections("north",      john_hall_3_long3)
john_hall_3_long4.add_connections("east",       john_3stair_s)
john_hall_3_long4.add_connections("south east", john_room48)
john_hall_3_long4.add_connections("south west", john_room47)
john_hall_3_long4.add_connections("west",       john_room46)

    #Johnson Rooms
john_room40.add_connections("west",         john_hall_3_long3)
john_room41.add_connections("west",         john_hall_3_long2)
john_room42.add_connections("west",         john_hall_3_long1)
john_room43.add_connections("west",         john_3stair_n)
john_room49.add_connections("west",         john_room48)
john_room44.add_connections("east",         john_hall_3_long1)
john_room45.add_connections("east",         john_hall_3_long3)
john_room46.add_connections("east",         john_hall_3_long4)
john_room48.add_connections("east",         john_room49)
john_room48.add_connections("north west",   john_hall_3_long4)
john_room47.add_connections("north east",   john_hall_3_long4)

    #Johnson Bathroom
john_bathroom_3.add_connections("east",     john_hall_3_long2)


