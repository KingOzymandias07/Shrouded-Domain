class Room:
    def __init__(self, name, description, part, sound=None):
        self.name = name
        self.description = description
        self.part = part
        self.sound = sound
        self.locked = False
        self.visited = False
        self.connections = {}
        self.item_list = []
        self.monster_list = []
        self.npc_list = []
        self.interactable = []
    def add_connections(self, direction, room):
        self.connections[direction] = room 

    def get_connections(self, direction):
        return self.connections.get(direction)
    
    def list_connections(self):
        available_connections = []
        for direction, room in self.connections.items():
            if room.locked == False:
                available_connections.append(direction)
        return ", ".join(available_connections)

class Actor:
    class Object:
        class Item:
            def __init__(self, name, description, function, room_use, direction_use, uses, sound=None):
                self.name = name
                self.description = description
                self.function = function
                self.type = "item"
                self.room_use = room_use
                self.direction_use = direction_use
                self.uses = uses
                self.sound = sound
                
        class Weapon:
            class Melee:
                def __init__(self, name, description, max_damage, min_damage, accuracy, sound=None):
                    self.name = name
                    self.description = description
                    self.max_damage = max_damage
                    self.min_damage = min_damage
                    self.accuracy = accuracy
                    self.sound = sound
            class Ranged:
                def __init__(self, name, description, max_damage, min_damage, max_ammo, ammo, accuracy, sound=None):
                    self.name = name
                    self.description = description
                    self.max_damage = max_damage
                    self.min_damage = min_damage
                    self.max_ammo = max_ammo
                    self.ammo = ammo
                    self.accuracy = accuracy
                    self.sound = sound
        class Heal:
            def __init__(self, name, description, health, uses, sound=None):
                self.name = name
                self.description = description
                self.hp = health
                self.uses = uses
                self.sound = sound
        class Interactable:
            def __init__(self, name, description, function=None, item_need=None, fix_item=None, room_use=None, directional_use=None):
                self.name = name
                self.description = description
                self.function = function
                self.item_need = item_need
                self.fixed = fix_item
                self.room_use = room_use
                self.directional_use = directional_use
                self.item_list = []
                self.activated = False
        class Treasure:
            def __init__(self, name, description):
                self.name = name
                self.description = description
    class NPC:
        class Friendly:
            def __init__(self, name, description, health, interacted_name, sound=None, dialogue=None):
                self.name = name
                self.description = description
                self.dialogue = dialogue
                self.hp = health
                self.sound = sound
                self.interacted_name = interacted_name
                self.item_list = []
                self.talked_to = False
        class Foe:
            def __init__(self, name, description, max_health, health, max_damage, min_damage, accuracy, sound=None, dialogue=None):
                self.name = name
                self.description = description
                self.max_hp = max_health
                self.hp = health
                self.max_damage = max_damage
                self.min_damage = min_damage
                self.accuracy = accuracy
                self.sound = sound
                self.dialogue = dialogue
                self.item_list = []