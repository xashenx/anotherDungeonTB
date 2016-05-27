#!/usr/bin/env python3
from .creatures import Enemy, Player, Boss
from .enemies import *
from .items import *
from .abilities import *
import random


default_equipment = {
    "armor": None,
    "primary weapon": None,
    "secondary weapon": None,
    "ring": None,
    "talisman": None,
    "headwear": None
}


farting_t_characteristics = {
    "strength": 10,  # how hard you hit
    "vitality": 14,  # how much hp you have
    "dexterity": 6,  # how fast you act, your position in turn queue
    "intelligence": 5,  # how likely you are to strike a critical
}


class FartingT(Enemy):
    drop_table = {
        "chainmail": 3,
        "plate armor": 3,
        "steel spear": 6,
        "steel halberd": 6,
        "targe shield": 4,
        "bone amulet": 10,
        "ring": 3,
        "talisman": 10,
        "headwear": 5,
        "random": 10,
        "rapier": 3,
        "bone ring": 10,
        "petrified eye": 15,
        "crowned skull": 15,
    }
    loot_coolity = 0.9

    def __init__(self, level=1, name="Farting T.",
                 characteristics=farting_t_characteristics, stats=None,
                 description="The Mighty Farting T., a two-headed ogre which is famous for is 'poisoning' attacks..",
                 inventory=[], equipment=default_equipment, tags=["animate", "humanoid", "big"], abilities=[],
                 modifiers=[], exp_value=500):
        # print('vit', characteristics['vitality'])
        # characteristics['vitality'] = 0.28 * self.level
        # print('vit', characteristics['vitality'])
        Enemy.__init__(self, name, level, characteristics, stats, description, inventory, equipment, tags, abilities,
                       modifiers, exp_value)
        items = [get_item_by_name("a very very big maul", 0)]
        for item in items:
            if self.add_to_inventory(item):
                self.equip(item, True)

        self.base_abilities.append(FartingAttack("farting attack", None))

    def act(self, combat_event):
        attack_info = []
        perform_intoxication = True
        if not self.target or self.target.dead:
            self.select_target(combat_event)

        for player in combat_event.players:
            if "intoxicated" in [x.name for x in player.modifiers] and not player.dead:
                perform_intoxication = False
        if self.target and not self.target.dead:
            for ability in self.abilities:
                if ability.__class__ == FartingAttack and not perform_intoxication:
                    continue
                while self.energy >= ability.energy_required:
                    if ability.__class__ == FartingAttack:
                        attack_info.append(FartingAttack.use(self, self.target, ability.granted_by, combat_event))
                        break
                    else:
                        attack_info.append(ability.__class__.use(self, self.target, ability.granted_by, combat_event))
                    if not self.target or self.target.dead:
                        break
                if not self.target or self.target.dead:
                    break
        return attack_info


def farting_t(left, right):
    levels = list(range(left, right))
    boss = FartingT(random.choice(levels))
    return [boss], boss.description

boss_tables = {
    # difficulty rating: (function to get enemy or enemy group, params)
    "common": {
        "0": farting_t,
    },
    "animal": {
        "0": farting_t,
    },
    "undead": {
        "0": farting_t,
    },
    "demon": {
        "0": farting_t,
    },
    "human": {
        "0": farting_t,
    },
}