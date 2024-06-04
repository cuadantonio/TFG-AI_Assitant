import pymongo
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

client = pymongo.MongoClient(
    "mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
playersCollection = db["PlayersRealNormalizedData"]
pos = input("Position: ")
sort = "biwengerPoints"
limit = int(input("Limit: "))

players = playersCollection.find({"position": pos}).sort(sort, -1).limit(limit)

#players = playersCollection.find().sort(sort,-1).limit(limit)

assistsByMatches = []
assistsByMinutes = []
blocksByMatches = []
blocksByMinutes = []
concededGoalsByMatches = []
concededGoalsByMinutes = []
dribblesAttemptsByMatches = []
dribblesAttemptsByMinutes = []
dribblesSuccessByMatches = []
dribblesSuccessByMinutes = []
duelsWonByMatches = []
duelsWonByMinutes = []
foulsCommittedByMatches = []
foulsCommittedByMinutes = []
foulsDrawnByMatches = []
foulsDrawnByMinutes = []
goalsByMatches = []
goalsByMinutes = []
interceptionsByMatches = []
interceptionsByMinutes = []
keyPassesByMatches = []
keyPassesByMinutes = []
passesAccuracyByMatches = []
passesAccuracyByMinutes = []
passesByMatches = []
passesByMinutes = []
penaltiesCommitedByMatches = []
penaltiesCommitedByMinutes = []
penaltiesMissedByMatches = []
penaltiesMissedByMinutes = []
penaltiesSavedByMatches = []
penaltiesSavedByMinutes = []
penaltiesScoredByMatches = []
penaltiesScoredByMinutes = []
penaltiesWonByMatches = []
penaltiesWonByMinutes = []
redCardsByMatches = []
redCardsByMinutes = []
savesByMatches = []
savesByMinutes = []
shotsOnByMatches = []
shotsOnByMinutes = []
tacklesByMatches = []
tacklesByMinutes = []
totalDuelsByMatches = []
totalDuelsByMinutes = []
points = []
pointsByMatches = []
pointsByMinutes = []
for player in players:
    assistsByMatches.append(player["assistsByMatches"])
    assistsByMinutes.append(player["assistsByMinutes"])
    blocksByMatches.append(player["blocksByMatches"])
    blocksByMinutes.append(player["blocksByMinutes"])
    concededGoalsByMatches.append(player["concededGoalsByMatches"])
    concededGoalsByMinutes.append(player["concededGoalsByMinutes"])
    dribblesAttemptsByMatches.append(player["dribblesAttemptsByMatches"])
    dribblesAttemptsByMinutes.append(player["dribblesAttemptsByMinutes"])
    print(player["fullname"])
    dribblesSuccessByMatches.append(player["dribblesSuccessByMatches"])
    dribblesSuccessByMinutes.append(player["dribblesSuccessByMinutes"])
    duelsWonByMatches.append(player["duelsWonByMatches"])
    duelsWonByMinutes.append(player["duelsWonByMinutes"])
    foulsCommittedByMatches.append(player["foulsCommittedByMatches"])
    foulsCommittedByMinutes.append(player["foulsCommittedByMinutes"])
    foulsDrawnByMatches.append(player["foulsDrawnByMatches"])
    foulsDrawnByMinutes.append(player["foulsDrawnByMinutes"])
    goalsByMatches.append(player["goalsByMatches"])
    goalsByMinutes.append(player["goalsByMinutes"])
    interceptionsByMatches.append(player["interceptionsByMatches"])
    interceptionsByMinutes.append(player["interceptionsByMinutes"])
    keyPassesByMatches.append(player["keyPassesByMatches"])
    keyPassesByMinutes.append(player["keyPassesByMinutes"])
    passesAccuracyByMatches.append(player["passesAccuracyByMatches"])
    passesAccuracyByMinutes.append(player["passesAccuracyByMinutes"])
    passesByMatches.append(player["passesByMatches"])
    passesByMinutes.append(player["passesByMinutes"])
    penaltiesCommitedByMatches.append(player["penaltiesCommitedByMatches"])
    penaltiesCommitedByMinutes.append(player["penaltiesCommitedByMinutes"])
    penaltiesMissedByMatches.append(player["penaltiesMissedByMatches"])
    penaltiesMissedByMinutes.append(player["penaltiesMissedByMinutes"])
    penaltiesSavedByMatches.append(player["penaltiesSavedByMatches"])
    penaltiesSavedByMinutes.append(player["penaltiesSavedByMinutes"])
    penaltiesScoredByMatches.append(player["penaltiesScoredByMatches"])
    penaltiesScoredByMinutes.append(player["penaltiesScoredByMinutes"])
    penaltiesWonByMatches.append(player["penaltiesWonByMatches"])
    penaltiesWonByMinutes.append(player["penaltiesWonByMinutes"])
    redCardsByMatches.append(player["redCardsByMatches"])
    redCardsByMinutes.append(player["redCardsByMinutes"])
    savesByMatches.append(player["savesByMatches"])
    savesByMinutes.append(player["savesByMinutes"])
    tacklesByMatches.append(player["tacklesByMatches"])
    tacklesByMinutes.append(player["tacklesByMinutes"])
    totalDuelsByMatches.append(player["totalDuelsByMatches"])
    totalDuelsByMinutes.append(player["totalDuelsByMinutes"])
    points.append(player["biwengerPoints"])
    pointsByMatches.append(player["biwengerPointsByMatch"])
    pointsByMinutes.append(player["biwengerPointsByMinutes"])
    print(player["name"])
    print(pointsByMatches)



dataOriginal = {"assistsByMatches": assistsByMatches,
                "assistsByMinutes": assistsByMinutes,
                "blocksByMatches": blocksByMatches,
                "blocksByMinutes": blocksByMinutes,
                "concededGoalsByMatches": concededGoalsByMatches,
                "concededGoalsByMinutes": concededGoalsByMinutes,
                "dribblesAttemptsByMatches": dribblesAttemptsByMatches,
                "dribblesAttemptsByMinutes": dribblesAttemptsByMinutes,
                "dribblesSuccessByMatches": dribblesSuccessByMatches,
                "dribblesSuccessByMinutes": dribblesSuccessByMinutes,
                "duelsWonByMatches": duelsWonByMatches,
                "duelsWonByMinutes": duelsWonByMinutes,
                "foulsCommittedByMatches": foulsCommittedByMatches,
                "foulsCommittedByMinutes": foulsCommittedByMinutes,
                "foulsDrawnByMatches": foulsDrawnByMatches,
                "foulsDrawnByMinutes": foulsDrawnByMinutes,
                "goalsByMatches": goalsByMatches,
                "goalsByMinutes": goalsByMinutes,
                "interceptionsByMatches": interceptionsByMatches,
                "interceptionsByMinutes": interceptionsByMinutes,
                "keyPassesByMatches": keyPassesByMatches,
                "keyPassesByMinutes": keyPassesByMinutes,
                "passesAccuracyByMatches": passesAccuracyByMatches,
                "passesAccuracyByMinutes": passesAccuracyByMinutes,
                "passesByMatches": passesByMatches,
                "passesByMinutes": passesByMinutes,
                "penaltiesCommitedByMatches": penaltiesCommitedByMatches,
                "penaltiesCommitedByMinutes": penaltiesCommitedByMinutes,
                "penaltiesMissedByMatches": penaltiesMissedByMatches,
                "penaltiesMissedByMinutes": penaltiesMissedByMinutes,
                "penaltiesSavedByMatches": penaltiesSavedByMatches,
                "penaltiesSavedByMinutes": penaltiesSavedByMinutes,
                "penaltiesScoredByMatches": penaltiesScoredByMatches,
                "penaltiesScoredByMinutes": penaltiesScoredByMinutes,
                "penaltiesWonByMatches": penaltiesWonByMatches,
                "penaltiesWonByMinutes": penaltiesWonByMinutes,
                "redCardsByMatches": redCardsByMatches,
                "redCardsByMinutes": redCardsByMinutes,
                "savesByMatches": savesByMatches,
                "savesByMinutes": savesByMinutes,
                "tacklesByMatches": tacklesByMatches,
                "tacklesByMinutes": tacklesByMinutes,
                "totalDuelsByMatches": totalDuelsByMatches,
                "totalDuelsByMinutes": totalDuelsByMinutes,
                "points": points,
                "pointsByMatches":pointsByMatches,
                "pointsByMinutes": pointsByMinutes}


originalDataFrame = pd.DataFrame(dataOriginal)

originalMatrix = originalDataFrame.corr()

originalMatrix.to_csv("matrix.csv",sep=";")

# sn.heatmap(originalMatrix)
# plt.show()
#
# sn.heatmap(matrix1, annot=True)
# plt.show()
#
# sn.heatmap(matrix2, annot=True)
# plt.show()
#
# sn.heatmap(matrix3, annot=True)
# plt.show()
#
# sn.heatmap(matrix4, annot=True)
# plt.show()
#
# sn.heatmap(matrix5, annot=True)
# plt.show()
