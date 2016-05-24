# -*- coding: utf-8 -*-


def get_exp_ladder(players):
    ladder = []
    # print("exp ladder")
    for uid in players:
        # print("------ " + players[uid].name)
        position = 0
        goon = True
        ladder_en = len(ladder)
        pl_level = players[uid].level
        pl_exp = players[uid].experience
        while position < 3 and goon:
            if ladder_en >= position + 1:
                # we already have a player at this position
                if pl_level >= players[ladder[position]].level:
                    if pl_level > players[ladder[position]].level or \
                            pl_exp > players[ladder[position]].experience:
                        index = position + 1
                        uid_to_move = ladder[position]
                        ladder[position] = uid
                        # print(position, players[uid].name,
                        # players[uidToMove].name)
                        while index < 3 and goon:
                            if ladder_en == index:
                                # (index, players[uid_to_move].name, "append")
                                ladder.append(uid_to_move)
                                ladder_en += 1
                                goon = False
                            else:
                                tmp = ladder[index]
                                ladder[index] = uid_to_move
                                # print(index, players[uid_to_move].name,
                                # players[tmp].name)
                                uid_to_move = tmp
                            index += 1
                        goon = False
            elif position == ladder_en < 3:
                # elif ladder_en < 3 and position == ladder_en:
                # print(position, players[uid].name, "append")
                ladder.append(uid)
                goon = False
            position += 1
    return ladder


def get_kb_ladder(players):
    ladder = []
    # print("exp ladder")
    for uid in players:
        # print("------ " + players[uid].name)
        position = 0
        goon = True
        ladder_len = len(ladder)
        pl_kb = players[uid].killing_blows
        pl_lvl = players[uid].level
        while position < 3 and goon:
            if ladder_len >= position + 1:
                # we already have a player at this position
                if pl_kb >= players[ladder[position]].killing_blows:
                    if pl_kb > players[ladder[position]].killing_blows or \
                                    pl_lvl > players[ladder[position]].level:
                        index = position + 1
                        uid_to_move = ladder[position]
                        ladder[position] = uid
                        # print(position, players[uid].name,
                        # players[uid_to_move].name)
                        while index < 3 and goon:
                            if ladder_len == index:
                                ladder.append(uid_to_move)
                                ladder_len += 1
                                # print(index, players[uid_to_move].name, "append")
                                goon = False
                            else:
                                tmp = ladder[index]
                                ladder[index] = uid_to_move
                                # print(index, players[uid_to_move].name,
                                # players[tmp].name)
                                uid_to_move = tmp
                            index += 1
                        goon = False
            elif position == ladder_len < 3:
                # elif ladder_len < 3 and position == ladder_len:
                # print(position, players[uid].name, "append")
                ladder.append(uid)
                goon = False
            position += 1
    return ladder


def get_deaths_ladder(players):
    ladder = []
    for uid in players:
        position = 0
        goon = True
        ladder_len = len(ladder)
        pl_deaths = players[uid].deaths
        pl_lvl = players[uid].level
        while position < 3 and goon:
            if ladder_len >= position + 1:
                # we already have a player at this position
                if pl_deaths <= players[ladder[position]].deaths:
                    if pl_deaths < players[ladder[position]].deaths or \
                                    pl_lvl > players[ladder[position]].level:
                        index = position + 1
                        uid_to_move = ladder[position]
                        ladder[position] = uid
                        while index < 3 and goon:
                            if ladder_len == index:
                                ladder.append(uid_to_move)
                                ladder_len += 1
                                goon = False
                            else:
                                tmp = ladder[index]
                                ladder[index] = uid_to_move
                                uid_to_move = tmp
                            index += 1
                        goon = False
            elif position == ladder_len < 3:
                # elif ladder_len < 3 and position == ladder_len:
                ladder.append(uid)
                goon = False
            position += 1
    return ladder
