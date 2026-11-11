from map.johnson_hall import *
from map.tutorial import *
from vars.classes import *
from vars.descriptions import *

#===================
#       ITEMS
#===================

#----------------
#      Keys
#----------------
universal_key = Actor.Object.Item("Skeleton Key", "universal key.txt", "key", "any", "any", 999)

key_004 = Actor.Object.Item("Key 004", "JH (item) Key 004.txt", "key", john_1stair_n, "east", 1)
bathroom_key = Actor.Object.Item("Bathroom Key", "JH (item) Key Bathroom.txt", "key", john_hall_1_long2, "west", 1)

#----------------
#     Melee
#----------------
fists = Actor.Object.Weapon.Melee("Fists", "fists.txt", 2, 1, 10, "punch")
fire_poker = Actor.Object.Weapon.Melee("Fire Poker", "fire poker.txt", 3, 2, 15, "sword hit")
john_common.item_list.append(fire_poker)

#----------------
#     Ranged
#----------------
revolver = Actor.Object.Weapon.Ranged("Revolver", "revolver.txt", 5, 2, 6, 0, 15, "revolver")
revolver_ammo = Actor.Object.Item("Revolver Ammo", "revolver ammo.txt", "ammo", None, None, 15, "r reload")

#----------------
#    Monsters
#----------------
base_mutant = Actor.NPC.Foe("Amalgamation", "base_mutant.txt", 4, 4, 4, 1, 4, "punch")
john_room4.monster_list.append(base_mutant)

#-----------------
#     Healing
#-----------------
first_aid_kit = Actor.Object.Heal("First Aid Kit", "medkit.txt", 2, 3)

#----------------
#     Random
#----------------

#----------------
#     Actor
#----------------
dead_cat = Actor.Object.Interactable("cat", "dead_cat.txt", "item")
john_room8.interactable.append(dead_cat)
dead_cat.item_list.append(bathroom_key)

#----------------
#      NPCs
#----------------
Madeline = Actor.NPC.Friendly("girl", "npc_madeline.txt", 5, "Madeline", None, "madeline.txt")
Madeline.item_list.append(key_004)
john_bathroom_1.npc_list.append(Madeline)

#-------------------------
#      Tutorial Shit
#-------------------------
tut_ur_key = Actor.Object.Item("N Key", "TUT Key North.txt", "key", tut_2, "north", 1)
tut_3.item_list.append(tut_ur_key)
tut_tr_key = Actor.Object.Item("T Key", "TUT Key Talk.txt", "key", tut_7, "north", 1)
tut_5.item_list.append(tut_tr_key)

tut_lever_handle = Actor.Object.Interactable("lever handle", "lever_handle.txt", "fix", None, tut_8)

tut_lever = Actor.Object.Interactable("lever", "lever.txt", "lever", None, None, tut_4, "east")
tut_6.interactable.append(tut_lever)

tut_fixed_lever = Actor.Object.Interactable("lever", "fixed_lever.txt", "lever", None, None, tut_6, "north")
tut_broken_lever = Actor.Object.Interactable("broken lever", "broken_lever.txt", "broken", tut_lever_handle, tut_fixed_lever)
tut_8.interactable.append(tut_broken_lever)

Tutorial = Actor.NPC.Friendly("guy", "npc_tutorial.txt", 999, "John", None, "tutorial.txt")
tut_8.npc_list.append(Tutorial)
Tutorial.item_list.append(tut_lever_handle)
tut_8.item_list.append(tut_lever_handle)

tut_inscription1 = Actor.Object.Interactable("inscription", "tut_inscription1.txt", "text")
tut_4.interactable.append(tut_inscription1)