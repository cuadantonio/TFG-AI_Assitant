#delanteros
import pymongo

def calcGoalkeeperPoints(player):
    saves = player["saves"]
    penaltiesSaved = player["penaltiesSaved"]
    totalPasses = player["totalPasses"]
    totalDuels = player["totalDuels"]
    duelsWon = player["duelsWon"]

    concededGoals = player["concededGoals"]
    yellowCards = player["yellowCards"]
    redCards = player["redCards"]
    penaltiesCommited = player["penaltiesCommited"]
    penaltiesMissed = player["penaltiesMissed"]

    points = 0.3 * saves + 0.1 * penaltiesSaved + 0.05 * totalPasses + 0.03 * totalDuels + 0.07 * duelsWon - 0.08 * concededGoals - 0.05 * yellowCards - 0.06 * redCards - 0.05 * penaltiesCommited - 0.03 * penaltiesMissed
    points = points * 100
    return points

def calcDefenderPoints(player):
    totalTackles = player["totalTackles"]
    blockTackles = player["blockTackles"]
    interceptionTackles = player["interceptionTackles"]
    totalDuels = player["totalDuels"]
    duelsWon = player["duelsWon"]
    totalPasses = player["totalPasses"]
    keyPasses = player["keyPasses"]

    concededGoals = player["concededGoals"]
    yellowCards = player["yellowCards"]
    redCards = player["redCards"]
    penaltiesCommited = player["penaltiesCommited"]

    points = 0.05 * totalTackles + 0.07 * blockTackles + 0.07 * interceptionTackles + 0.04 * totalDuels + 0.075 * duelsWon + 0.03 * totalPasses + 0.05 * keyPasses - 0.05 * concededGoals - 0.05 * yellowCards - 0.1 * redCards - 0.05 * penaltiesCommited
    points = points * 100
    return points

def calcMidfielderPoints(player):
    totalPasses = player["totalPasses"]
    keyPasses = player["keyPasses"]
    assists = player["assists"]
    totalDuels = player["totalDuels"]
    duelsWon = player["duelsWon"]
    interceptionTackles = player["interceptionTackles"]
    totalTackles = player["totalTackles"]
    blockTackles = player["blockTackles"]
    foulsDrawn = player["foulsDrawn"]
    dribblesSuccess = player["dribblesSuccess"]

    foulsCommitted = player["foulsCommited"]
    yellowCards = player["yellowCards"]
    redCards = player["redCards"]
    penaltiesCommited = player["penaltiesCommited"]

    points = 0.05 * totalPasses + 0.08 * keyPasses + 0.1 * assists + 0.03 * totalDuels + 0.05 * duelsWon + 0.1 * interceptionTackles + 0.03 * totalTackles + 0.05 * blockTackles + 0.05 * foulsDrawn + 0.05 * dribblesSuccess - 0.05 * foulsCommitted - 0.03 * yellowCards - 0.05 * redCards - 0.02 * penaltiesCommited
    points = points * 100
    return points

def calcAttackerPoints(player):
    totalGoals = player["totalGoals"]
    assists = player["assists"]
    shotsOn = player["shotsOn"]
    keyPasses = player["keyPasses"]
    dribblesSuccess = player["dribblesSuccess"]
    penaltiesScored = player["penaltiesScored"]
    foulsDrawn = player["foulsDrawn"]
    penaltiesWon = player["penaltiesWon"]

    offsides = player["offsides"]
    yellowCards = player["yellowCards"]
    redCards = player["redCards"]
    penaltiesMissed = player["penaltiesMissed"]
    penaltiesCommited = player["penaltiesCommited"]

    points = 0.2 * totalGoals + 0.1 * assists + 0.05 * shotsOn + 0.07 * keyPasses + 0.1 * dribblesSuccess + 0.06 * penaltiesScored + 0.03 * foulsDrawn + 0.05 * penaltiesWon - 0.05 * offsides - 0.03 * yellowCards - 0.05 * redCards - 0.05 * penaltiesMissed - 0.03 * penaltiesCommited

    points = points * 100
    return points

client = pymongo.MongoClient(
    "mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
playersNormalizedDataByMatch = db["PlayersNormalizedDataByMatch"]
playersRealData = db["PlayersRealData"]

players = playersNormalizedDataByMatch.find()
for player in players:
    playerId = player["playerId"]
    fixtureId = player["fixtureId"]
    playerPosAux = playersRealData.find_one({"playerId":playerId})
    if(playerPosAux==None):
        print()
    else:
        playerPos = playerPosAux["position"]
        if (playerPos == "Goalkeeper"):
            points = calcGoalkeeperPoints(player)
            playerUpdate = {"points": points}
            playerUpdateSet = {"$set": playerUpdate}
            playerQuery = playersNormalizedDataByMatch.find_one({"playerId": playerId, "fixtureId": fixtureId})
            playersNormalizedDataByMatch.update_one(playerQuery, playerUpdateSet)
        elif (playerPos == "Defender"):
            points = calcDefenderPoints(player)
            playerUpdate = {"points": points}
            playerUpdateSet = {"$set": playerUpdate}
            playerQuery = playersNormalizedDataByMatch.find_one({"playerId": playerId, "fixtureId": fixtureId})
            playersNormalizedDataByMatch.update_one(playerQuery, playerUpdateSet)
        elif (playerPos == "Midfielder"):
            points = calcMidfielderPoints(player)
            playerUpdate = {"points": points}
            playerUpdateSet = {"$set": playerUpdate}
            playerQuery = playersNormalizedDataByMatch.find_one({"playerId": playerId, "fixtureId": fixtureId})
            playersNormalizedDataByMatch.update_one(playerQuery, playerUpdateSet)
        elif (playerPos == "Attacker"):
            points = calcAttackerPoints(player)
            playerUpdate = {"points": points}
            playerUpdateSet = {"$set": playerUpdate}
            playerQuery = playersNormalizedDataByMatch.find_one({"playerId": playerId, "fixtureId": fixtureId})
            playersNormalizedDataByMatch.update_one(playerQuery, playerUpdateSet)

