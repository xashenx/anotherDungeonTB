#!/usr/bin/env python3
from .creatures import Enemy, Player, Boss
from .enemies import *
from .items import *
from .abilities import *
import random


def retrieve_enemies_for_difficulty(enemy_table, difficulty, last_room):
    right = clamp(difficulty + 0.2 * difficulty, 0, 100)
    left = clamp(difficulty - 0.2 * difficulty, 0, 100)
    # total_len = 100
    # candidates = []
    temp_list = sorted([int(x) for x in list(enemy_tables[enemy_table].keys())
                        if right >= int(x) > left])

    if len(temp_list) == 0:
        left = 0
        temp_list = sorted([int(x) for x in
                            list(enemy_tables[enemy_table].keys()) if right >= int(x) > left])

    random_float = random_in_range_for_coolity(0, len(temp_list), 0.8)

    random_enemy = temp_list[int(math.floor(random_float))]

    enemies = enemy_tables[enemy_table][str(random_enemy)]
    if not last_room:
        # print(enemies)
        return enemies[0](*enemies[1])
    else:
        boss = boss_tables[enemy_table]["0"]
        minions = enemies[0](*enemies[1])
        boss = boss(int(left), int(right))
        # print("boss stats: ",boss[0][0].level, boss[0][0].characteristics["dexterity"],
        #       boss[0][0].level * boss[0][0].characteristics["vitality"], boss[0][0].health)
        enemies = []
        # adding the boss
        enemies.append(boss[0][0])
        boss[0].append(boss[0][0])
        for minion in minions[0]:
            # adds each minion to the pack
            enemies.append(minion)
        # add the description of the boss
        enemies = (enemies, boss[1])
        # print(enemies)
        return enemies


default_boss_characteristics = {
    "strength": 7,  # how hard you hit
    "vitality": 6,  # how much hp you have
    "dexterity": 4,  # how fast you act, your position in turn queue
    "intelligence": 4,  # how likely you are to strike a critical
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
                 characteristics=default_boss_characteristics, stats=None,
                 description="The Mighty Farting T., a two-headed ogre which is famous for is 'poisoning' attacks..",
                 inventory=[], equipment=default_equipment, tags=["living", "animate", "humanoid", "big"], abilities=[],
                 modifiers=[], exp_value=500):
        characteristics['strength'] += math.floor(level / 20)
        characteristics['vitality'] += math.floor(level / 10)
        characteristics['dexterity'] += math.floor(level / 25)
        characteristics['intelligence'] += math.floor(level / 30)
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


class Uddu(Enemy):
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

    def __init__(self, level=1, name="Uddu, King of Thugs",
                 characteristics=default_boss_characteristics, stats=None,
                 description="Uddu, the King of Thugs",
                 inventory=[], equipment=default_equipment, tags=["living", "animate", "humanoid", "big"], abilities=[],
                 modifiers=[], exp_value=500):
        characteristics['strength'] += math.floor(level / 15)
        characteristics['vitality'] += math.floor(level / 25)
        characteristics['dexterity'] += math.floor(level / 20)
        characteristics['intelligence'] += math.floor(level / 35)
        self.thugs_call = 3
        self.low_hp = False
        self.thugs = []
        Enemy.__init__(self, name, level, characteristics, stats, description, inventory, equipment, tags, abilities,
                       modifiers, exp_value)
        items = [get_item_by_name("mace", 0)]
        items += [get_item_by_name("buckler", 0)]
        items += [get_item_by_name("leather armor", 0)]
        for item in items:
            if self.add_to_inventory(item):
                self.equip(item, True)
        self.base_abilities.append(CallThugs("call thugs", None))

    def act(self, combat_event):
        attack_info = []
        if not self.target or self.target.dead:
            self.select_target(combat_event)
        if not self.low_hp and self.health / self.stats['max_health'] < .60:
            self.thugs_call = 0
            self.low_hp = True
        if self.target and not self.target.dead:
            for ability in self.abilities:
                if ability.__class__ == CallThugs and self.thugs_call > 0:
                    self.thugs_call -= 1
                    continue
                while self.energy >= ability.energy_required:
                    if ability.__class__ == CallThugs:
                        self.thugs_call = 3
                        alive_players = [c for c in combat_event.players if not c.dead]
                        number_of_thugs = max(len(alive_players), 2)
                        self.thugs = []
                        for i in range(0, number_of_thugs):
                            self.thugs += [Thug(self.level - 5)]
                        attack_info.append(CallThugs.use(self, self.target, ability.granted_by, combat_event))
                        break
                    else:
                        attack_info.append(ability.__class__.use(self, self.target, ability.granted_by, combat_event))
                    if not self.target or self.target.dead:
                        break
                if not self.target or self.target.dead:
                    break
        return attack_info


def uddu(left, right):
    levels = list(range(left, right))
    boss = Uddu(random.choice(levels))
    return [boss], boss.description


class Gianpymir(Enemy):
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

    def __init__(self, level=1, name="Gianpymir",
                 characteristics=default_boss_characteristics, stats=None,
                 description="Count Gianpymir, the Vampire",
                 inventory=[], equipment=default_equipment, tags=["undead", "animate", "humanoid"], abilities=[],
                 modifiers=[], exp_value=500):
        characteristics['strength'] = 4 + math.floor(level / 40)
        characteristics['vitality'] = 4 + math.floor(level / 35)
        characteristics['dexterity'] = 6 + math.floor(level / 20)
        characteristics['intelligence'] = 7 + math.floor(level / 10)
        # self.thugs_call = 3
        # self.low_hp = False
        # self.thugs = []
        self.summons = []
        self.channeling = True
        Enemy.__init__(self, name, level, characteristics, stats, description, inventory, equipment, tags, abilities,
                       modifiers, exp_value)
        items = [get_item_by_name("ritual cloak", 0)]
        items += [get_item_by_name("golden ring", 0)]
        for item in items:
            if self.add_to_inventory(item):
                self.equip(item, True)

        spells = ["lightning", "summon"]
        self.creatures = []
        self.priority_list = [(0, "summon"), (1, "lightning")]
        self.max_priority = 1
        for spell in spells:
            self.base_abilities.append(abilities_listing[spell](spell, None))

    def act(self, combat_event):
        attack_info = []
        if not self.target or self.target.dead:
            self.select_target(combat_event)
        # if "intoxicated" in [x.name for x in player.modifiers]
        for priority_level in range(0, self.max_priority + 1):
            abilities = [ability_name for (priority, ability_name) in self.priority_list if
                         priority == priority_level]
            chosen = random.choice(abilities)
            ability = [x for x in self.abilities if x.name == chosen][0]
            if ability.__class__ == Summon:
                if self.channeling:
                    alive_players = [c for c in combat_event.players if not c.dead]
                    number_of_summons = len(alive_players) + 1
                    self.summons = []
                    for i in range(0, number_of_summons):
                        creature = Rat(self.level - 5)
                        creature.name = "familiar"
                        creature.description = "A familiar"
                        self.summons += [creature]
                    attack_info.append(ability.__class__.use(self, self.target, ability.granted_by, combat_event))
                continue
            if self.target and not self.target.dead:
                    if priority_level == self.max_priority:
                        while self.energy >= ability.energy_required:
                            attack_info.append(ability.__class__.use(self, self.target, ability.granted_by,
                                                                     combat_event))
                            if not self.target or self.target.dead:
                                break
        return attack_info

    def channeling_action(self):
        combat_event = self.event
        alive_players = [c for c in combat_event.players if not c.dead]
        number_of_summons = len(alive_players) + 1
        summons = []
        for i in range(0, number_of_summons):
            creature = Rat(self.level - 5)
            creature.event = combat_event
            summons += creature
        combat_event.enemies += summons
        combat_event.turn_queue += summons
        combat_event.turn_queue = combat_event.update_turn_queue()


def count_gianpymir(left, right):
    levels = list(range(left, right))
    boss = Gianpymir(random.choice(levels))
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
        "0": uddu,
    },
}