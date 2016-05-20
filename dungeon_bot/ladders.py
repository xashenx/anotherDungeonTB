# -*- coding: utf-8 -*-


def get_exp_ladder(players):
    ladder = []
    #print("exp ladder")
    for uid in players:
        #print("------ " + players[uid].name)
        position = 0
        goon = True
        ladderLen = len(ladder)
        plLevel = players[uid].level
        plExp = players[uid]._experience
        while position < 3 and goon:
            if ladderLen >= position + 1:
                # we already have a player at this position
                if plLevel >= players[ladder[position]].level:
                    if plLevel > players[ladder[position]].level or \
                    plExp > players[ladder[position]]._experience:
                        index = position + 1
                        uidToMove = ladder[position]
                        ladder[position] = uid
                        #print(position, players[uid].name,
                        #players[uidToMove].name)
                        while index < 3 and goon:
                            if ladderLen == index:
                                #print(index, players[uidToMove].name, "append")
                                ladder.append(uidToMove)
                                ladderLen += 1
                                goon = False
                            else:
                                tmp = ladder[index]
                                ladder[index] = uidToMove
                                #print(index, players[uidToMove].name,
                                #players[tmp].name)
                                uidToMove = tmp
                            index += 1
                        goon = False
            elif ladderLen < 3 and position == ladderLen:
                #print(position, players[uid].name, "append")
                ladder.append(uid)
                goon = False
            position += 1
    return ladder


def get_kb_ladder(players):
    ladder = []
    #print("exp ladder")
    for uid in players:
        #print("------ " + players[uid].name)
        position = 0
        goon = True
        ladderLen = len(ladder)
        plKb = players[uid].killing_blows
        plLvl = players[uid].level
        while position < 3 and goon:
            if ladderLen >= position + 1:
                # we already have a player at this position
                if plKb >= players[ladder[position]].killing_blows:
                    if plKb > players[ladder[position]].killing_blows or \
                    plLvl > players[ladder[position]].level:
                        index = position + 1
                        uidToMove = ladder[position]
                        ladder[position] = uid
                        #print(position, players[uid].name,
                        #players[uidToMove].name)
                        while index < 3 and goon:
                            if ladderLen == index:
                                ladder.append(uidToMove)
                                ladderLen += 1
                                #print(index, players[uidToMove].name, "append")
                                goon = False
                            else:
                                tmp = ladder[index]
                                ladder[index] = uidToMove
                                #print(index, players[uidToMove].name,
                                #players[tmp].name)
                                uidToMove = tmp
                            index += 1
                        goon = False
            elif ladderLen < 3 and position == ladderLen:
                #print(position, players[uid].name, "append")
                ladder.append(uid)
                goon = False
            position += 1
    return ladder


def get_deaths_ladder(players):
    ladder = []
    for uid in players:
        position = 0
        goon = True
        ladderLen = len(ladder)
        plDeaths = players[uid].deaths
        plLvl = players[uid].level
        while position < 3 and goon:
            if ladderLen >= position + 1:
                # we already have a player at this position
                if plDeaths >= players[ladder[position]].deaths:
                    if plDeaths > players[ladder[position]].deaths or \
                    plLvl > players[ladder[position]].level:
                        index = position + 1
                        uidToMove = ladder[position]
                        ladder[position] = uid
                        while index < 3 and goon:
                            if ladderLen == index:
                                ladder.append(uidToMove)
                                ladderLen += 1
                                goon = False
                            else:
                                tmp = ladder[index]
                                ladder[index] = uidToMove
                                uidToMove = tmp
                            index += 1
                        goon = False
            elif ladderLen < 3 and position == ladderLen:
                ladder.append(uid)
                goon = False
            position += 1
    return ladder