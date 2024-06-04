import pymongo
import pandas as pd

client = pymongo.MongoClient(
    "mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
playersRealData = db["PlayersRealData"]
playersNormalizedDataByMatch = db["PlayersNormalizedDataByMatch"]

biwengerPoints=[]
biwengerPointsByMatch=[]
customPoints=[]
customPointsByMatch=[]

players = playersRealData.find({})
for player in players:
    auxCustomPoints = 0
    auxMatchCount = 0
    playerId = player["playerId"]
    playerGames = playersNormalizedDataByMatch.find({"playerId":playerId})
    if playerGames is not None:
        for playerGame in playerGames:
            auxCustomPoints += playerGame["points"]
            auxMatchCount += 1
        auxCustomPointsByMatch = round((auxCustomPoints/auxMatchCount), 8)
        biwengerPoints.append(player["biwengerPoints"])
        biwengerPointsByMatch.append(player["biwengerPointsByMatch"])
        customPoints.append(auxCustomPoints)
        customPointsByMatch.append(auxCustomPointsByMatch)

data = {"biwengerPoints": biwengerPoints,
        "biwengerPointsByMatch": biwengerPointsByMatch,
        "customPoints": customPoints,
        "customPointsByMatch": customPointsByMatch}

dataframe = pd.DataFrame(data)
matrix = dataframe.corr()
matrix.to_csv("matrix.csv",sep=";")