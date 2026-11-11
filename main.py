# NOTE for next time:

import asyncio
import random
import pygame
import time
import textwrap

from pathlib import Path
from vars.classes import *
from map.johnson_hall import *
from map.tutorial import *
from vars.audio import *
from vars.actors import *

BASE_DIR = Path(__file__).parent
ASSET_DIR = BASE_DIR / "assets"
TEXT_DIR = ASSET_DIR / "text"

COMMAND_LIST = ["quit", "go", "look", "inventory", "take", "use", "examine", "attack", "drop", "equip", "unequip", "talk", "tutorial", "quit tutorial"]
DIRECTIONS = ["north", "north east", "east", "south east", "south", "south west", "west", "north west", "up", "down"]
def get_text(txt_file):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    return (TEXT_DIR / txt_file).read_text(encoding="utf-8").strip()

class TextAdventure:
    def __init__(self):
        self.current_room = john_bathroom_1
        self.previous_room = self.current_room
        self.health = 5
        self.max_health = 5
        self.monster_kills = 0
        self.npc_kills = 0
        self.current_weapon = fists
        self.treasures_list = []
        self.treasures = len(self.treasures_list)
        self.inventory = [first_aid_kit, revolver, revolver_ammo]
        self.messages = []

    def write(self, message=""):
        self.messages.append(str(message))

    def look(self):
        if not self.current_room.visited:
            self.write(f"    {get_room_desc(self.current_room.description)}")
            self.write()
            self.current_room.visited = True
        self.write(f"Available Paths: {self.current_room.list_connections()}")
        for way in DIRECTIONS:
            if self.current_room.get_connections(way):
                if self.current_room.get_connections(way).locked == True:
                    self.write(f"    There is a locked door to the {way}.")
        for actor in self.current_room.interactable:
            self.write(f"There is {actor.name} here.")
        for item in self.current_room.item_list:
            if type(item) == Actor.Object.Item:
                self.write(f"There is {get_item_desc(item.description)} here.")
            if type(item) == Actor.Object.Weapon.Melee or type(item) == Actor.Object.Weapon.Ranged:
                self.write(f"There is {get_weapon_desc(item.description)} here.")
        for monster in self.current_room.monster_list:
            self.write(f"There is {get_monster_desc(monster.description)} here.")
        for npc in self.current_room.npc_list:
            self.write(f"There is {get_npc_desc(npc.description)} here.")
        self.write()
        return

    def go(self, direction):
        next_room = self.current_room.get_connections(direction)
        if next_room:
            if next_room.locked == False:
                if self.current_room.monster_list != []:
                    self.monster_atk()
                    self.write()
                self.move_sound(direction)
                if next_room.part != self.current_room.part:
                    try:
                        prev_music = current_bg
                        music[prev_music].stop()
                        if next_room.part == "ext":
                            current_bg = "exterior"
                            music[current_bg].play(-1)
                    except UnboundLocalError:
                        if next_room.part == "ext":
                            current_bg = "exterior"
                            music[current_bg].play(-1)
                self.current_room = next_room
            else:
                self.write("You can't go that way.")
                sounds["locked"].play()
                self.write()
        else:
            self.write("You can't go that way.")
            self.write()
        
    def examine(self, name):
        if name == "self" or name == "myself":
            self.write(f"HP:             {self.health}/{self.max_health}")
            self.write(f"Current Weapon: {self.current_weapon.name}\n     Weapon Damage:  {self.current_weapon.min_damage}-{self.current_weapon.max_damage}")
            if self.monster_kills > 0:
                self.write(f"Enemies Defeated:    {self.monster_kills}")
            if self.npc_kills > 0:
                self.write(f"NPCs Killed:         {self.npc_kills}")
            if self.treasures > 0:
                self.write(f"Treasures:           {self.treasures}/(TBD)")
            return
        else:
            for item in self.inventory:
                if item.name.lower() == name:
                    if type(item) == Actor.Object.Item:
                        self.write(f"Item:   {item.name}")
                        self.write(f"{get_item_desc(item.description)}")
                        self.write(f"Uses:   {item.uses}")
                    if type(item) == Actor.Object.Heal:
                        self.write(f"Item:   {item.name}")
                        self.write(f"Health: {item.hp}")
                        self.write(f"Uses:   {item.uses}")
                        self.write(f"{get_item_desc(item.description)}")
                    if type(item) == Actor.Object.Weapon.Melee:
                        self.write(f"Weapon: {item.name}")
                        self.write(get_weapon_desc(item.description))
                    if type(item) == Actor.Object.Weapon.Ranged:
                        self.write(f"Weapon: {item.name}")
                        self.write(get_weapon_desc(item.description))
                        self.write(f"Ammo:   {item.ammo}/{item.max_ammo}")
                    if type(item) == Actor.Object.Interactable:
                        self.write(f"Item:   {item.name}")
                        actor = item
                        if actor.name.lower() == name.lower():
                            self.write(get_desc(actor.description))
                            for item in actor.item_list:
                                self.inventory.append(item)
                                actor.item_list.remove(item) 
                            actor.description = actor.description.replace(".txt", "0.txt")
                    self.write()
                    return


            for monster in self.current_room.monster_list:
                if monster.name.lower() == name:
                    self.write(f"Monster: {monster.name}")
                    self.write(f"    HP:      {monster.hp}/{monster.max_hp}")
                    self.write()
                    return

            for actor in self.current_room.interactable:
                if actor.name.lower() == name.lower():
                    self.write(get_desc(actor.description))
                    for item in actor.item_list:
                        self.current_room.item_list.append(item)
                        actor.item_list.remove(item)   
                        if actor.function != "text":
                            actor.description = actor.description.replace(".txt", "0.txt")

                    self.write()
                    return
            self.write(f"You do not have {name}.")
    def talk(self, name):
        for npc in self.current_room.npc_list:
            if npc.name.lower() == name.lower():
                self.write()
                while True:
                    with open(DIALOGUE_DIR / npc.dialogue, "r") as file:
                        text = file.read().split("\n\n")
                        number = npc.dialogue[-5]
                        try:
                            number = int(number)
                            end = npc.dialogue[-5:]
                        except ValueError:
                            end = npc.dialogue[-4:]
                        for line in text:
                            if line == "NAME":
                                npc.name = npc.interacted_name
                                npc.description = npc.description.replace(".txt", "0.txt")
                                continue
                            elif line == "ITEM":
                                for item in npc.item_list:
                                    self.inventory.append(item)
                                    npc.item_list.remove(item)
                                    continue
                            elif line == "OPTION":
                                ans = int(pygame.KEYDOWN)
                                if ans > 0:
                                    print(ans)
                                    #npc.dialogue = npc.dialogue.replace(end, str(ans)+".txt")
                                    break
                                else:
                                    self.write("You decided not to talk.")
                            elif line == "END":
                                npc.dialogue = npc.dialogue.replace(end, "0.txt")
                                continue
                            elif line.startswith("NEXT"):
                                next, number = line.split(" ")
                                npc.dialogue = npc.dialogue.replace(end, f"{number}.txt")
                            else:
                                if line.startswith("\""):
                                    self.write(line)
                                else:
                                    self.write(line)
                                self.write()
                        else:
                            return
        self.write(f"There is no {name} here.")
 
    def take(self, name):
        for objects in self.current_room.item_list:
            if objects.name.lower() == name:
                self.inventory.append(objects)
                self.current_room.item_list.remove(objects)
                self.write(f"You picked up the {objects.name}.")
                return
        for actor in self.current_room.interactable:
            if actor.name.lower() == name:
                if actor.takable == True:
                    self.inventory.append(actor)
                    self.current_room.interactable.remove(actor)
                    self.write(f"You picked up the {actor.name}")
                    return
        self.write(f"There is no {name} here.")

    def use(self, name):
        for item in self.inventory:
            if item.name.lower() == name:
                if type(item) == Actor.Object.Item:
                    self.use_item(item)
                if type(item) == Actor.Object.Heal:
                    self.use_heal(item)
                if type(item) == Actor.Object.Weapon.Melee:
                    self.equip(item)
                if type(item) == Actor.Object.Weapon.Ranged:
                    self.equip(item)
                if type(item) == Actor.Object.Interactable:
                    self.interact(item)
                return
        for actor in self.current_room.interactable:
            if actor.name.lower() == name:
                self.interact(actor)
                return
        self.write(f"You don't have {name}.")
        

    def interact(self, actor):
        if actor.function == "lever":
            sounds["lever"].play()     
            locked = actor.room_use.get_connections(actor.directional_use).locked
            actor.room_use.get_connections(actor.directional_use).locked = not locked
            self.write("You flipped the switch.")
        elif actor.function == "fix":
            self.fix(actor)

    def fix(self, actor):
        if actor in self.inventory:
            for broken in self.current_room.interactable:
                if broken.item_need == actor:
                    self.write(f"You repaired the {broken.name}!")
                    self.current_room.interactable.append(broken.fixed)
                    self.current_room.interactable.remove(broken)
                    self.inventory.remove(actor)

    def hint(self):
        if john_bathroom_1.locked == True:
            self.write("You hear weeping coming from the bathroom.")

    def use_heal(self, item):
        self.health += item.health
        if self.health > self.max_health:
            healed = self.health - self.max_health
            self.health = self.max_health
            self.write(f"You healed {healed} HP.")
        else:
            self.write(f"You healed {item.health}.")
    def use_item(self, item):
        if item.function == "key":
            self.use_key(item)
            return
        if item.function == "ammo":
            self.reload(item)

    def reload(self, item):
        if self.current_weapon == revolver and item == revolver_ammo:
            temp_ammo = self.current_weapon.max_ammo - self.current_weapon.ammo
            self.current_weapon.ammo = temp_ammo
            item.uses -= temp_ammo
            self.write(f"You reloaded the revolver. {self.current_weapon.ammo}/{self.current_weapon.max_ammo}")
            sounds[item.sound].play()
            if item.uses <= 0:
                self.write(f"You used up all your ammunition.")
                self.inventory.remove(item)
        else:
            self.write(f"You can't reload {self.current_weapon.name}.")

    def equip(self, item):
        if item in self.inventory:
            if self.current_weapon != fists:
                self.inventory.append(self.current_weapon)
            self.current_weapon = item
            self.write(f"You equipped the {item.name}.")
            self.inventory.remove(item)
        else:
            self.write(f"You don't have {item}.")

    def unequip(self):
        if self.current_weapon != fists:
            item = self.current_weapon
            self.inventory.append(item)
            self.current_weapon = fists
            self.write(f"You unequipped the {item.name}")
        else:
            self.write("You can't unequip your fists.")

    def use_key(self, item):
        if item.room_use == self.current_room:
            self.current_room.get_connections(item.direction_use).locked = False
            sounds["unlock"].play()
            self.write("You turned the key, and the door unlocked.")
            item.uses -= 1
            if item.uses <= 0:
                self.write("This key is no longer useful. You threw away the key.")
                self.inventory.remove(item)
            return
        if item.room_use == "any":
            for way in DIRECTIONS:
                if self.current_room.get_connections(way):
                    if self.current_room.get_connections(way).locked == True:
                        self.current_room.get_connections(way).locked = False
                        sounds["unlock"].play
                        item.uses -= 1
            self.write("You unlocked every door in the area.")
        else:                
            self.write("You can't use that here.")
        return

    def attack(self, target):
        hit = random.randint(1, self.current_weapon.accuracy)
        dmg = random.randint(self.current_weapon.min_damage, self.current_weapon.max_damage)
        if type(self.current_weapon) == Actor.Object.Weapon.Melee:
            self.melee_atk(target, hit, dmg)
        if type(self.current_weapon) == Actor.Object.Weapon.Ranged:
            self.ranged_atk(target, hit, dmg)  
        self.monster_atk()
            
    def melee_atk(self, target, hit, dmg):
        if hit != 0:
            if target == "self" or target == "myself":
                self.write("You hit yourself.")
                sounds[self.current_weapon.sound].play()
                self.write(f"You lost {dmg} HP.")
                self.health -= dmg
                return
            for monster in self.current_room.monster_list:
                if monster.name.lower() == target:
                    self.write(f"You swung at the {monster.name}.")
                    sounds[self.current_weapon.sound].play()
                    monster.hp -= dmg
                    if monster.hp <= 0:
                        self.write(f"You killed the {monster.name}!")
                        sounds["kill"].play()
                        monster.hp = monster.max_hp
                        self.current_room.monster_list.remove(monster)
                        self.monster_kills += 1
                    return
            for npc in self.current_room.npc_list:
                if npc.name.lower() == target:
                    self.write(f"You swung at {npc.name}.")
                    sounds[self.current_weapon.sound].play()
                    npc.health -= dmg
                    if npc.health <= 0:
                        self.write(f"You killed {npc.name}.")
                        sounds["kill"].play()
                        self.npc_kills += 1
                    return
            self.write(f"There is no {target} here.")
        else:
            self.write("You missed.")
            sounds["swoosh"].play()
            return
            
    def ranged_atk(self, target, hit, dmg):
        if hit != 0:
            if self.ammo > 0:
                if target == "self" or target == "myself":
                    self.write("You shot yourself.")
                    sounds[self.current_weapon.sound].play()
                    self.write(f"You lost {dmg} HP.")
                    self.health -= dmg
                    self.current_weapon.ammo -= 1
                    return
                for monster in self.current_room.monster_list:
                    if monster.name.lower() == target:
                        self.write(f"You shot the {monster.name}.")
                        sounds[self.current_weapon.sound].play()
                        monster.health -= dmg
                        self.current_weapon.ammo -= 1
                        if monster.health <= 0:
                            self.write(f"You killed the {monster.name}!")
                            sounds["kill"].play()
                            monster.health = monster.max_health
                            self.current_room.monster_list.remove(monster)
                            self.monster_kills += 1
                            return
                        return
                for npc in self.current_room.npc_list:
                    if npc.name.lower() == target:
                        self.write(f"You shot {npc.name}.")
                        sounds[self.current_weapon.sound].play()
                        npc.health -= dmg
                        self.current_weapon.ammo -= 1
                        if npc.health <= 0:
                            self.write(f"You killed {npc.name}.")
                            sounds["kill"].play()
                            self.npc_kills += 1
                        return
                self.write(f"There is no {target} here.")
        else:
            self.write("You missed.")
            self.current_weapon.ammo -= 1
            return
            
    def monster_atk(self):
        self.write()
        for monster in self.current_room.monster_list:
            hit = random.randint(1, monster.accuracy)
            dmg = random.randint(monster.min_damage, monster.max_damage)
            self.write(f"The {monster.name} attacked!")
            if hit != 0:
                self.write(f"You lost {dmg} HP.")
                self.health -= dmg
                sounds[monster.sound].play()
            else:
                self.write("It missed!")
                sounds["swoosh"].play()
            return

    def drop(self, name):
        if name == "fists":
            self.write("You can't drop your own hands.")
            return
        for objects in self.inventory:
            if objects.name.lower() == name and type(objects) != Actor.Object.Interactable:
                self.inventory.remove(objects)
                self.current_room.item_list.append(objects)
                self.write(f"You dropped the {name}.")
                return
        for actor in self.inventory:
            if actor.name.lower() == name and type(actor) == Actor.Object.Interactable:
                self.inventory.remove(actor)
                self.current_room.interactable.append(actor)
                self.write(f"You dropped the {name}.")
                return
        self.write(f"You don't have {name}.")

    def game_over(self):
        if self.health <= 0:
            self.write("GAME OVER")
            sounds["death"].play()
            return True

    def move_sound(self, direction):
        next_room = self.current_room.get_connections(direction)
        if next_room:
            if next_room.locked == True:
                sounds["locked"].play()
                self.write("The door is locked.")
            else:
                if next_room.part != self.current_room.part:
                    if next_room.part == "ext":
                        sounds["door"].play()
                        return
                    if self.current_room.part == "ext" and next_room.part != "ext":
                        sounds["door"].play()
                        return
                    if self.current_room.part == "stair" and next_room.part == "stiar":
                        sounds["stairs"].play()
                else: 
                    sounds["walk"].play()

    def handle_command(self, command):
        for word in COMMAND_LIST:
            if command.startswith(word):
                if word.lower() == "quit":
                    self.health = 0
                elif word.lower() == "go":
                    target = command[3:]
                    self.go(target)
                elif word.lower() == "look":
                    self.look()
                elif word.lower() == "inventory":
                    for item in self.inventory:
                        self.write(item.name)
                elif word.lower() == "take":
                    target = command[5:]
                    self.take(target)
                elif word.lower() == "use":
                    target = command[4:]
                    self.use(target)
                elif word.lower() == "examine":
                    target = command[8:]
                    self.examine(target)
                elif word.lower() == "attack":
                    target = command[7:]
                    self.attack(target)
                elif word.lower() == "talk":
                    target = command[5:]
                    self.talk(target)
                elif word.lower() == "drop":
                    target = command[5:]
                    self.drop(target)
                elif word.lower() == "equip":
                    target = command[6:]
                    self.equip(target)
                elif word.lower() == "unequip":
                    target = command[8:]
                    self.unequip()
                elif word.lower() == "tutorial":
                    back_room = self.current_room
                    self.current_room = tut_1
                elif word.lower() == "quit tutorial":
                    self.current_room = back_room
                return
        self.write(f"I dont know {command}")

    def list_commands(self):
        for words in COMMAND_LIST:
            self.write(words)

    async def run(self):
        pygame.init()
        screen = pygame.display.set_mode((960, 640))
        pygame.display.set_caption("SHROUDED DOMAIN")
        font = pygame.font.Font(None, 20)
        clock = pygame.time.Clock()
        command = ""
        running = True

        self.write("Welcome to SHROUDED DOMAIN.")
        self.write("press 'enter' to continue...")
        self.list_commands()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif not self.game_over():
                        if event.key == pygame.K_RETURN:
                            self.write("> " + command)
                            self.handle_command(command)
                            command = ""
                            if not self.game_over():
                                self.write(
                                    f"{self.current_room.name}"
                                )
                                self.look()
                        elif event.key == pygame.K_BACKSPACE:
                            command = command[:-1]
                        elif event.unicode.isprintable():
                            command = (command + event.unicode)[:60]

            screen.fill((20, 24, 32))

            lines = []
            for message in self.messages:
                lines.extend(textwrap.wrap(message, width=65) or [""])
            for index, line in enumerate(lines[-17:]):
                surface = font.render(line, True, (235, 235, 235))
                screen.blit(surface, (24, 20 + index * 30))
            if self.game_over():
                prompt = "Refresh to restart; 'Esc' closes the game."
            else:
                prompt = "> " + command + "_"
            surface = font.render(prompt, True, (150, 220, 180))
            screen.blit(surface, (24, 590))
            pygame.display.flip()
            clock.tick(30)
            await asyncio.sleep(0)

        pygame.quit()

### THE GAME ###

"""async def main():
    pygame.init()
    pygame.mixer.init()
    running = TextAdventure()
    command_list = ["quit", "go", "look", "inventory", "take", "use", "examine", "attack/kill", "drop", "equip", "unequip", "talk", "tutorial"]
    self.write(get_text("title screen.txt"))
    self.write("(press 'enter' to begin...)")
    intro = open(TEXT_DIR / "intro.txt", "r")
    skip = input().lower()
    self.write()
    if skip != "skip":
        with intro as file:
            text = file.read().split("\n\n")
            for line in text:
                if line != "END":
                    if line.startswith("\""):
                        self.write(line)
                        input()
                    else:
                        self.write(line)
                        input()
                else:
                    continue


    play = "yes"
    running.current_room.visited = True
    self.write()
    self.write("Press enter to begin. (If you are stuck enter 'hint')")
    self.write("For a command list enter 'help'")
    self.write("For a tutorial enter 'tutorial'")
    self.write()
    self.write(running.current_room.name)
    running.look()

    while play == "yes":

        if running.health <= 0:
            play = running.death()
            if play != "yes":
                break
            os.system('cls')
            self.write("")
            os.execl(sys.executable, sys.executable, *sys.argv)        
                    
        command = input("> ").lower()

        if command == "quit":
            play = "no"

        elif command.startswith("go"):
            direction = command[3:]
            running.go(direction)

        elif command == "look":
            running.look()

        elif command == "inventory":
            for thing in running.inventory:
                self.write(thing.name)

        elif command.startswith("take"):
            name = command[5:]
            running.take(name)

        elif command.startswith("use"):
            name = command[4:]
            running.use(name)

        elif command == "help":
            self.write("")
            self.write("Helpful commands:")
            self.write(", ".join(command_list))
            self.write("")
            self.write(running.current_room.name)

        elif command.startswith("examine"):
            name = command[8:]
            if name == "":
                self.write("What are you examining?")
                name = input("> ").lower()
            running.examine(name)

        elif command.startswith("attack") or command.startswith("kill"):
            if command.startswith("attack"):
                target = command[7:]
            if command.startswith("kill"):
                target= command[5:]
            if target == "":
                self.write("What are you attacking?")
                target = input("> ").lower
            running.attack(target)

        elif command.startswith("drop"):
            name = command[5:]
            if name == "":
                self.write("What are you dropping?")
                name = input("> ").lower
            running.drop(name)

        elif command.startswith("equip"):
            name = command[6:]
            if name == "":
                self.write("What are you equipping?")
                name = input("> ").lower
            for item in running.inventory:
                if item.name.lower() == name.lower():
                    running.equip(item)

        elif command.startswith("unequip"):
            running.unequip()

        elif command.startswith("talk"):
            name = command[5:]
            running.talk(name)

        elif command.startswith("tutorial"):
            back_room = running.current_room
            running.current_room = tut_1
            running.current_room.visited = True
            self.write(running.current_room.name)
            running.look()

        elif command.startswith("exit"):
            if command[5:] == "tutorial":
                running.current_room = back_room
            if back_room.part == "TUT":
                running.current_room = john_front

        else:
            self.write(f"I don't know '{command}'.")
    await asyncio.sleep(0)"""

if __name__ == "__main__":
    game = TextAdventure()
    asyncio.run(game.run())
