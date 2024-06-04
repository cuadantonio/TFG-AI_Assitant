import time

import pymongo
import random
import csv
client = pymongo.MongoClient(
    "mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
playersNormalizedDataByMatch = db["PlayersNormalizedDataByMatch"]
playersRealData = db["PlayersRealData"]


def calcPlayers(lineup, round, lastRounds):
    finalGkId = 0
    finalDfIds = []
    finalMfIds = []
    finalAtIds = []

    finalGk = ""
    finalDf = []
    finalMf = []
    finalAt = []

    numGk = 1
    numDf = lineup[0]
    numMf = lineup[1]
    numAt = lineup[2]

    if (numGk + numDf + numMf + numAt != 11):
        exit()
    else:
        goalkeepers = playersRealData.find({"position": "Goalkeeper"})
        defenders = playersRealData.find({"position": "Defender"})
        midfielders = playersRealData.find({"position": "Midfielder"})
        attackers = playersRealData.find({"position": "Attacker"})

        gkDict = {}
        dfDict = {}
        mfDict = {}
        atDict = {}

        # Goalkeepers
        for goalkeeper in goalkeepers:
            gkId = goalkeeper["playerId"]
            if (lastRounds == -1):
                gkGames = playersNormalizedDataByMatch.find({"playerId": gkId, "round": {"$lt": round}})
            else:
                lastRoundsAux = round - lastRounds
                gkGames = playersNormalizedDataByMatch.find(
                    {"playerId": gkId, "round": {"$lt": round, "$gte": lastRoundsAux}})
            gkPoints = 0
            for gkGame in gkGames:
                gkPoints += int(gkGame["points"])
            gkToAddToDict = {gkId: gkPoints}
            gkDict.update(gkToAddToDict)
        sortedGkDict = dict(sorted(gkDict.items(), key=lambda item: item[1], reverse=True))
        finalGkId = list(sortedGkDict.keys())[0]

        # Defenders
        for defender in defenders:
            dfId = defender["playerId"]
            if (lastRounds == -1):
                dfGames = playersNormalizedDataByMatch.find({"playerId": dfId, "round": {"$lt": round}})
            else:
                lastRoundsAux = round - lastRounds
                dfGames = playersNormalizedDataByMatch.find(
                    {"playerId": dfId, "round": {"$lt": round, "$gte": lastRoundsAux}})
            dfPoints = 0
            for dfGame in dfGames:
                dfPoints += int(dfGame["points"])
            dfToAddToDict = {dfId: dfPoints}
            dfDict.update(dfToAddToDict)
        sortedDfDict = dict(sorted(dfDict.items(), key=lambda item: item[1], reverse=True))
        for i in range(0, numDf):
            finalDfIds.append(list(sortedDfDict.keys())[i])

        # Midfielders
        for midfielder in midfielders:
            mfId = midfielder["playerId"]
            if (lastRounds == -1):
                mfGames = playersNormalizedDataByMatch.find({"playerId": mfId, "round": {"$lt": round}})
            else:
                lastRoundsAux = round - lastRounds
                mfGames = playersNormalizedDataByMatch.find(
                    {"playerId": mfId, "round": {"$lt": round, "$gte": lastRoundsAux}})
            mfPoints = 0
            for mfGame in mfGames:
                mfPoints += int(mfGame["points"])
            mfToAddToDict = {mfId: mfPoints}
            mfDict.update(mfToAddToDict)
        sortedMfDict = dict(sorted(mfDict.items(), key=lambda item: item[1], reverse=True))
        for i in range(0, numMf):
            finalMfIds.append(list(sortedMfDict.keys())[i])

        # Attackers
        for attacker in attackers:
            atId = attacker["playerId"]
            if (lastRounds == -1):
                atGames = playersNormalizedDataByMatch.find({"playerId": atId, "round": {"$lt": round}})
            else:
                lastRoundsAux = round - lastRounds
                atGames = playersNormalizedDataByMatch.find(
                    {"playerId": atId, "round": {"$lt": round, "$gte": lastRoundsAux}})
            atPoints = 0
            for atGame in atGames:
                atPoints += int(atGame["points"])
            atToAddToDict = {atId: atPoints}
            atDict.update(atToAddToDict)
        sortedAtDict = dict(sorted(atDict.items(), key=lambda item: item[1], reverse=True))
        for i in range(0, numAt):
            finalAtIds.append(list(sortedAtDict.keys())[i])

        finalGk = playersRealData.find_one({"playerId": finalGkId})["playerId"]
        for finalDfId in finalDfIds:
            finalDf.append(playersRealData.find_one({"playerId": finalDfId})["playerId"])
        for finalMfId in finalMfIds:
            finalMf.append(playersRealData.find_one({"playerId": finalMfId})["playerId"])
        for finalAtId in finalAtIds:
            finalAt.append(playersRealData.find_one({"playerId": finalAtId})["playerId"])

        finalList = []
        finalList.append([finalGk])
        finalList.append(finalDf)
        finalList.append(finalMf)
        finalList.append(finalAt)

        return finalList
        # print("Alineacion final: ")
        # print("Portero: " + finalGk)
        # print("Defensas: " + str(finalDf))
        # print("Mediocentros: " + str(finalMf))
        # print("Delanteros " + str(finalAt))


def calcRandomPlayers(lineup):
    finalGk = ""
    finalDf = []
    finalMf = []
    finalAt = []

    numDf = lineup[0]
    numMf = lineup[1]
    numAt = lineup[2]

    dfRandomNums = []
    mfRandomNums = []
    atRandomNums = []

    goalkeepers = playersRealData.find({"position": "Goalkeeper"})
    goalkeepersNum = playersRealData.count_documents({"position": "Goalkeeper"})
    goalKeeperRandom = random.randint(0, goalkeepersNum - 1)
    finalGk = goalkeepers[goalKeeperRandom]["name"]

    defenders = playersRealData.find({"position": "Defender"})
    defendersNum = playersRealData.count_documents({"position": "Defender"})
    dfCountAux = 0
    while (dfCountAux < numDf):
        defenderRandom = random.randint(0, defendersNum - 1)
        if (defenderRandom not in dfRandomNums):
            dfRandomNums.append(defenderRandom)
            dfCountAux += 1
            finalDf.append(defenders[defenderRandom]["name"])

    midfielders = playersRealData.find({"position": "Midfielder"})
    midfieldersNum = playersRealData.count_documents({"position": "Midfielder"})
    mfCountAux = 0
    while (mfCountAux < numMf):
        midfielderRandom = random.randint(0, midfieldersNum - 1)
        if (midfielderRandom not in mfRandomNums):
            mfRandomNums.append(midfielderRandom)
            mfCountAux += 1
            finalMf.append(midfielders[midfielderRandom]["name"])

    attackers = playersRealData.find({"position": "Attacker"})
    attackersNum = playersRealData.count_documents({"position": "Attacker"})
    atCountAux = 0
    while (atCountAux < numAt):
        attackerRandom = random.randint(0, attackersNum - 1)
        if (attackerRandom not in atRandomNums):
            atRandomNums.append(attackerRandom)
            atCountAux += 1
            finalAt.append(attackers[attackerRandom]["name"])

    finalList = []
    finalList.append(finalGk)
    finalList.append(finalDf)
    finalList.append(finalMf)
    finalList.append(finalAt)

    return finalList

    # print("Alineacion final aleatoria: ")
    # print("Portero: " + finalGk)
    # print("Defensas: " + str(finalDf))
    # print("Mediocentros: " + str(finalMf))
    # print("Delanteros " + str(finalAt))


def realLineup(lineup, round):
    finalGkId = 0
    finalDfIds = []
    finalMfIds = []
    finalAtIds = []

    finalGk = ""
    finalDf = []
    finalMf = []
    finalAt = []

    numGk = 1
    numDf = lineup[0]
    numMf = lineup[1]
    numAt = lineup[2]

    goalkeepers = playersRealData.find({"position": "Goalkeeper"})
    defenders = playersRealData.find({"position": "Defender"})
    midfielders = playersRealData.find({"position": "Midfielder"})
    attackers = playersRealData.find({"position": "Attacker"})

    gkDict = {}
    dfDict = {}
    mfDict = {}
    atDict = {}

    for goalkeeper in goalkeepers:
        gkId = goalkeeper["playerId"]
        gkGame = playersNormalizedDataByMatch.find_one({"playerId": gkId, "round": round})
        if gkGame != None:
            gkPoints = gkGame["points"]
            gkToAddToDict = {gkId: gkPoints}
            gkDict.update(gkToAddToDict)
    sortedGkDict = dict(sorted(gkDict.items(), key=lambda item: item[1], reverse=True))
    finalGkId = list(sortedGkDict.keys())[0]

    for defender in defenders:
        dfId = defender["playerId"]
        dfGame = playersNormalizedDataByMatch.find_one({"playerId": dfId, "round": round})
        if dfGame != None:
            dfPoints = dfGame["points"]
            dfToAddToDict = {dfId: dfPoints}
            dfDict.update(dfToAddToDict)
    sortedDfDict = dict(sorted(dfDict.items(), key=lambda item: item[1], reverse=True))
    for i in range(0, numDf):
        finalDfIds.append(list(sortedDfDict.keys())[i])

    for midfielder in midfielders:
        mfId = midfielder["playerId"]
        mfGame = playersNormalizedDataByMatch.find_one({"playerId": mfId, "round": round})
        if mfGame != None:
            mfPoints = mfGame["points"]
            mfToAddToDict = {mfId: mfPoints}
            mfDict.update(mfToAddToDict)
    sortedMfDict = dict(sorted(mfDict.items(), key=lambda item: item[1], reverse=True))
    for i in range(0, numMf):
        finalMfIds.append(list(sortedMfDict.keys())[i])

    for attacker in attackers:
        atId = attacker["playerId"]
        atGame = playersNormalizedDataByMatch.find_one({"playerId": atId, "round": round})
        if atGame != None:
            atPoints = atGame["points"]
            atToAddToDict = {atId: atPoints}
            atDict.update(atToAddToDict)
    sortedAtDict = dict(sorted(atDict.items(), key=lambda item: item[1], reverse=True))
    for i in range(0, numAt):
        finalAtIds.append(list(sortedAtDict.keys())[i])

    finalGk = playersRealData.find_one({"playerId": finalGkId})["name"]
    for finalDfId in finalDfIds:
        finalDf.append(playersRealData.find_one({"playerId": finalDfId})["name"])
    for finalMfId in finalMfIds:
        finalMf.append(playersRealData.find_one({"playerId": finalMfId})["name"])
    for finalAtId in finalAtIds:
        finalAt.append(playersRealData.find_one({"playerId": finalAtId})["name"])

    finalList = []
    finalList.append(finalGk)
    finalList.append(finalDf)
    finalList.append(finalMf)
    finalList.append(finalAt)

    return finalList

    # print("Alineacion final real: ")
    # print("Portero: " + finalGk)
    # print("Defensas: " + str(finalDf))
    # print("Mediocentros: " + str(finalMf))
    # print("Delanteros " + str(finalAt))


def getGoalkeepers(round, lastRounds):
    goalkeepers = playersRealData.find({"position": "Goalkeeper"})
    gkDict = {}
    for goalkeeper in goalkeepers:
        gkId = goalkeeper["playerId"]
        if (lastRounds == -1):
            gkGames = playersNormalizedDataByMatch.find({"playerId": gkId, "round": {"$lt": round}})
        else:
            lastRoundsAux = round - lastRounds
            gkGames = playersNormalizedDataByMatch.find(
                {"playerId": gkId, "round": {"$lt": round, "$gte": lastRoundsAux}})
        gkPoints = 0
        for gkGame in gkGames:
            gkPoints += int(gkGame["points"])
        gkToAddToDict = {gkId: gkPoints}
        gkDict.update(gkToAddToDict)
    sortedGkDict = dict(sorted(gkDict.items(), key=lambda item: item[1], reverse=True))
    return list(sortedGkDict.keys())


def getDefenders(round, lastRounds):
    defenders = playersRealData.find({"position": "Defender"})
    dfDict = {}
    for defender in defenders:
        dfId = defender["playerId"]
        if (lastRounds == -1):
            dfGames = playersNormalizedDataByMatch.find({"playerId": dfId, "round": {"$lt": round}})
        else:
            lastRoundsAux = round - lastRounds
            dfGames = playersNormalizedDataByMatch.find(
                {"playerId": dfId, "round": {"$lt": round, "$gte": lastRoundsAux}})
        dfPoints = 0
        for dfGame in dfGames:
            dfPoints += int(dfGame["points"])
        dfToAddToDict = {dfId: dfPoints}
        dfDict.update(dfToAddToDict)
    sortedDfDict = dict(sorted(dfDict.items(), key=lambda item: item[1], reverse=True))
    return list(sortedDfDict.keys())


def getMidfielders(round, lastRounds):
    midfielders = playersRealData.find({"position": "Midfielder"})
    mfDict = {}
    for midfielder in midfielders:
        mfId = midfielder["playerId"]
        if (lastRounds == -1):
            mfGames = playersNormalizedDataByMatch.find({"playerId": mfId, "round": {"$lt": round}})
        else:
            lastRoundsAux = round - lastRounds
            mfGames = playersNormalizedDataByMatch.find(
                {"playerId": mfId, "round": {"$lt": round, "$gte": lastRoundsAux}})
        mfPoints = 0
        for mfGame in mfGames:
            mfPoints += int(mfGame["points"])
        mfToAddToDict = {mfId: mfPoints}
        mfDict.update(mfToAddToDict)
    sortedMfDict = dict(sorted(mfDict.items(), key=lambda item: item[1], reverse=True))
    return list(sortedMfDict.keys())


def getAttackers(round, lastRounds):
    attackers = playersRealData.find({"position": "Attacker"})
    atDict = {}
    for attacker in attackers:
        atId = attacker["playerId"]
        if (lastRounds == -1):
            atGames = playersNormalizedDataByMatch.find({"playerId": atId, "round": {"$lt": round}})
        else:
            lastRoundsAux = round - lastRounds
            atGames = playersNormalizedDataByMatch.find(
                {"playerId": atId, "round": {"$lt": round, "$gte": lastRoundsAux}})
        atPoints = 0
        for atGame in atGames:
            atPoints += int(atGame["points"])
        atToAddToDict = {atId: atPoints}
        atDict.update(atToAddToDict)
    sortedAtDict = dict(sorted(atDict.items(), key=lambda item: item[1], reverse=True))
    return list(sortedAtDict.keys())


def getPlayersBySum(round, lastRounds):
    players = playersRealData.find()
    playersDict = {}
    for player in players:
        id = player["playerId"]
        if (lastRounds == -1):
            playerGames = playersNormalizedDataByMatch.find({"playerId": id, "round": {"$lt": round}})
        else:
            lastRoundsAux = round - lastRounds
            playerGames = playersNormalizedDataByMatch.find(
                {"playerId": id, "round": {"$lt": round, "$gte": lastRoundsAux}})
        playerPoints = 0
        for playerGame in playerGames:
            playerPoints += int(playerGame["points"])
        playerToAddToDict = {id: playerPoints}
        playersDict.update(playerToAddToDict)
    sortedDict = dict(sorted(playersDict.items(), key=lambda item: item[1], reverse=True))
    return list(sortedDict.keys())

def getPlayersByAverage(round, lastRounds):
    players = playersRealData.find()
    playersDict = {}
    for player in players:
        id = player["playerId"]
        if (lastRounds == -1):
            playerGames = playersNormalizedDataByMatch.find({"playerId": id, "round": {"$lt": round}})
        else:
            lastRoundsAux = round - lastRounds
            playerGames = playersNormalizedDataByMatch.find(
                {"playerId": id, "round": {"$lt": round, "$gte": lastRoundsAux}})
        playerPoints = 0
        matchCount = 0
        for playerGame in playerGames:
            playerPoints += int(playerGame["points"])
            matchCount += 1
        if matchCount != 0:
            playerPointsAux = int(playerPoints / matchCount)
            playerToAddToDict = {id: playerPointsAux}
            playersDict.update(playerToAddToDict)
        else:
            playerPointsAux = 0
            playerToAddToDict = {id: playerPointsAux}
            playersDict.update(playerToAddToDict)
    sortedDict = dict(sorted(playersDict.items(), key=lambda item: item[1], reverse=True))
    return list(sortedDict.keys())

def getPlayersInRound(round):
    players = playersRealData.find()
    playersDict = {}
    for player in players:
        id = player["playerId"]
        playerGame = playersNormalizedDataByMatch.find_one({"playerId": id, "round": round})
        if playerGame is not None:
            playerPoints = playerGame["points"]
            playerToAddToDict = {id: playerPoints}
            playersDict.update(playerToAddToDict)
    sortedDict = dict(sorted(playersDict.items(), key=lambda item: item[1], reverse=True))
    return list(sortedDict.keys())

def getPlayersPrice(players):
    prices = []
    for player in players:
        playerAux = playersRealData.find_one({"playerId": player})
        price = playerAux["biwengerPrice"]
        prices.append(price)
    return prices

def getPlayersPointsBySum(players, round, lastRounds):
    points = []
    for player in players:
        if lastRounds == -1:
            playerGames = playersNormalizedDataByMatch.find({"playerId": player, "round": {"$lt": round}})
        else:
            lastRoundsAux = round - lastRounds
            playerGames = playersNormalizedDataByMatch.find(
                {"playerId": player, "round": {"$lt": round, "$gte": lastRoundsAux}})
        playerPoints = 0
        for playerGame in playerGames:
            playerPoints += int(playerGame["points"])
        points.append(playerPoints)
    return points

def getPlayersPointsByAverage(players, round, lastRounds):
    points = []
    for player in players:
        if lastRounds == -1:
            playerGames = playersNormalizedDataByMatch.find({"playerId": player, "round": {"$lt": round}})
        else:
            lastRoundsAux = round - lastRounds
            playerGames = playersNormalizedDataByMatch.find(
                {"playerId": player, "round": {"$lt": round, "$gte": lastRoundsAux}})
        playerPoints = 0
        matchCount = 0
        for playerGame in playerGames:
            playerPoints += int(playerGame["points"])
            matchCount += 1
        if matchCount != 0:
            playerPointsAux = int(playerPoints / matchCount)
            points.append(playerPointsAux)
        else:
            playerPointsAux = 0
            points.append(playerPointsAux)
    return points

def getPlayersPointsInRound(players, round):
    points = []
    for player in players:
        playerGame = playersNormalizedDataByMatch.find_one({"playerId": player, "round": round})
        if playerGame is not None:
            playerPoints = playerGame["points"]
            points.append(playerPoints)
        else:
            playerPoints = 0
            points.append(playerPoints)
    return points
def getPositions(players):
    positions = []
    for player in players:
        playerAux = playersRealData.find_one({"playerId": player})
        position = playerAux["position"]
        positions.append(position)
    return positions

def reformatPlayers(players):
    newPlayers = [[],[],[],[]]
    for player in players:
        playerAux = playersRealData.find_one({"playerId": player})
        position = playerAux["position"]
        match position:
            case "Goalkeeper":
                newPlayers[0].append(player)
            case "Defender":
                newPlayers[1].append(player)
            case "Midfielder":
                newPlayers[2].append(player)
            case "Attacker":
                newPlayers[3].append(player)
    return newPlayers
def getPlayersNicknames(players):
    nicknames = [[],[],[],[]]
    for i, position in enumerate(players):
        for player in position:
            playerAux = playersRealData.find_one({"playerId": player})
            nickname = playerAux["nickname"]
            nicknames[i].append(nickname)
    return nicknames

def getPlayersImages(players):
    images = [[],[],[],[]]
    for i, position in enumerate(players):
        for player in position:
            playerAux = playersRealData.find_one({"playerId": player})
            image = playerAux["photo"]
            images[i].append(image)
    return images


print()

optPointsPod = 0
optSolutionPod = []


def calcPlayersWithPrice(players, prices, points, positions, positionLimits, priceLimit, playerIndex, currentSolution, currentPrice, currentPoints, currentPositions,startTime,timeLimit):
    global optPointsPod, optSolutionPod

    if time.time() - startTime > timeLimit:
        return

    if playerIndex == 0:
        optPointsPod = 0
        optSolutionPod = []

    if currentPrice > priceLimit:
        return

    if len(currentSolution) == 11 or playerIndex == len(players):
        if len(currentSolution) == 11 and currentPrice <= priceLimit and currentPoints > optPointsPod:
            optPointsPod = currentPoints
            optSolutionPod = currentSolution[:]
        return

    if currentPositions[positions[playerIndex]]< positionLimits[positions[playerIndex]] and priceLimit > prices[playerIndex] and priceLimit > currentPrice + prices[playerIndex]:
        currentPositions[positions[playerIndex]] += 1
        calcPlayersWithPrice(players, prices, points, positions, positionLimits, priceLimit, playerIndex + 1,
                             currentSolution + [players[playerIndex]], currentPrice + prices[playerIndex],
                             currentPoints + points[playerIndex], currentPositions,startTime, timeLimit)
        currentPositions[positions[playerIndex]] -= 1
    if len(currentSolution) == 10 and currentPrice + prices[playerIndex] <= priceLimit and currentPositions[positions[playerIndex]]<= positionLimits[positions[playerIndex]]:
        return
    calcPlayersWithPrice(players, prices, points, positions, positionLimits, priceLimit, playerIndex + 1,
                         currentSolution, currentPrice, currentPoints, currentPositions,startTime,timeLimit)

    return optSolutionPod, optPointsPod


optPointsNoPod = 0
optSolutionNoPod = []
def calcPlayersWithPriceNoPod(players, prices, points, positions, positionLimits, priceLimit, playerIndex, currentSolution, currentPrice, currentPoints, currentPositions, startTime, timeLimit):
    global optPointsNoPod, optSolutionNoPod

    if playerIndex == 0:
        optPointsNoPod = 0
        optSolutionNoPod = []

    if time.time() - startTime > timeLimit:
        return

    if len(currentSolution) == 11 or playerIndex == len(players):
        if len(currentSolution) == 11 and currentPrice <= priceLimit and currentPoints > optPointsNoPod:
            optPointsNoPod = currentPoints
            optSolutionNoPod = currentSolution[:]
        return

    if currentPositions[positions[playerIndex]]< positionLimits[positions[playerIndex]]:
        currentPositions[positions[playerIndex]] += 1
        calcPlayersWithPriceNoPod(players, prices, points, positions, positionLimits, priceLimit, playerIndex + 1,
                             currentSolution + [players[playerIndex]], currentPrice + prices[playerIndex],
                             currentPoints + points[playerIndex], currentPositions, startTime, timeLimit)
        currentPositions[positions[playerIndex]] -= 1

    calcPlayersWithPriceNoPod(players, prices, points, positions, positionLimits, priceLimit, playerIndex + 1,
                         currentSolution, currentPrice, currentPoints, currentPositions,startTime, timeLimit)

    return optSolutionNoPod, optPointsNoPod


currentPositions = {'Goalkeeper':0, 'Defender': 0, 'Midfielder': 0, 'Attacker': 0}
currentPositions2 = {'Goalkeeper':0, 'Defender': 0, 'Midfielder': 0, 'Attacker': 0}
positionLimits433 = {'Goalkeeper':1, 'Defender': 4, 'Midfielder': 3, 'Attacker': 3}
positionLimits343 = {'Goalkeeper':1, 'Defender': 3, 'Midfielder': 4, 'Attacker': 3}
positionLimits352 = {'Goalkeeper':1, 'Defender': 3, 'Midfielder': 5, 'Attacker': 2}
positionLimits442 = {'Goalkeeper':1, 'Defender': 4, 'Midfielder': 4, 'Attacker': 2}
positionLimits451 = {'Goalkeeper':1, 'Defender': 4, 'Midfielder': 5, 'Attacker': 1}
positionLimits532 = {'Goalkeeper':1, 'Defender': 5, 'Midfielder': 3, 'Attacker': 2}
positionLimits541 = {'Goalkeeper':1, 'Defender': 5, 'Midfielder': 4, 'Attacker': 1}


def getAveragePrice(players):
    price = 0
    count = 0

    for player in players:
        playerAux = playersRealData.find_one({"playerId":player})
        playerPrice = playerAux["biwengerPrice"]
        price += playerPrice
        count += 1
    return int(price/count)



