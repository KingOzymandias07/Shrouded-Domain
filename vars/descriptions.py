from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
ASSET_DIR = BASE_DIR / "assets"
TEXT_DIR = ASSET_DIR / "text"
MONSTER_DESC_DIR = TEXT_DIR / "monsters"
ITEM_DESC_DIR = TEXT_DIR / "items"
WEAPON_DESC_DIR = TEXT_DIR / "weapons"
AUDIO_DIR = ASSET_DIR / "audio"
DIALOGUE_DIR = TEXT_DIR / "dialogue"
NPC_DESC_DIR = TEXT_DIR / "NPCs"
INTERACTABLE_DIR = TEXT_DIR / "interactables"

def get_room_desc(txt_file):
    return (TEXT_DIR / "rooms" / txt_file).read_text(encoding="utf=8").strip()
def get_monster_desc(txt_file):
    return (MONSTER_DESC_DIR / txt_file).read_text(encoding="utf-8").strip()

def get_item_desc(txt_file):
    return (ITEM_DESC_DIR / txt_file).read_text(encoding="utf-8").strip()

def get_weapon_desc(txt_file):
    return (WEAPON_DESC_DIR / txt_file).read_text(encoding="utf-8").strip()

def get_npc_desc(txt_file):
    return (NPC_DESC_DIR / txt_file).read_text(encoding="utf-8").strip()

def get_desc(txt_file):
    return (INTERACTABLE_DIR / txt_file).read_text(encoding="utf-8").strip()