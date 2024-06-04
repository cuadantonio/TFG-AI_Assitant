import pymongo
import numpy as np
client = pymongo.MongoClient(
    "mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
playersDataByMatch = db["PlayersDataByMatch"]
playersNormalizedDataByMatch = db["PlayersNormalizedDataByMatch"]


players = playersDataByMatch.find()

fixtureIdList = []
roundList = []
teamList = []
teamIdList = []
rivalTeamList = []
rivalTeamIdList = []
playerIdList = []
playerNameList = []
playerPhotoList = []
minutesList = []
offsidesList = []
totalShotsList = []
shotsOnList = []
totalGoalsList = []
concededGoalsList = []
assistsList = []
savesList = []
totalPassesList = []
keyPassesList = []
passesAccuracyList = []
totalTacklesList = []
blockTacklesList = []
interceptionTacklesList = []
totalDuelsList = []
duelsWonList = []
dribblesAttemptsList = []
dribblesSuccessList = []
dribblesPastList = []
foulsDrawnList = []
foulsCommittedList = []
yellowCardsList = []
redCardsList = []
penaltiesWonList = []
penaltiesCommittedList = []
penaltiesScoredList = []
penaltiesMissedList = []
penaltiesSavedList = []
winnerIdList = []
scoreList = []
dateList = []

for player in players:
    fixtureIdList.append(player["fixtureId"])
    roundList.append(player["round"])
    teamList.append(player["team"])
    teamIdList.append(player["teamId"])
    rivalTeamList.append(player["rivalTeam"])
    rivalTeamIdList.append(player["rivalTeamId"])
    playerIdList.append(player["playerId"])
    playerNameList.append(player["playerName"])
    playerPhotoList.append(player["playerPhoto"])
    minutesList.append(player["minutes"])
    offsidesList.append(player["offsides"])
    totalShotsList.append(player["totalShots"])
    shotsOnList.append(player["shotsOn"])
    totalGoalsList.append(player["totalGoals"])
    concededGoalsList.append(player["concededGoals"])
    assistsList.append(player["assists"])
    savesList.append(player["saves"])
    totalPassesList.append(player["totalPasses"])
    keyPassesList.append(player["keyPasses"])
    passesAccuracyList.append(player["passesAccuracy"])
    totalTacklesList.append(player["totalTackles"])
    blockTacklesList.append(player["blockTackles"])
    interceptionTacklesList.append(player["interceptionTackles"])
    totalDuelsList.append(player["totalDuels"])
    duelsWonList.append(player["duelsWon"])
    dribblesAttemptsList.append(player["dribblesAttempts"])
    dribblesSuccessList.append(player["dribblesSuccess"])
    dribblesPastList.append(player["dribblesPast"])
    foulsDrawnList.append(player["foulsDrawn"])
    foulsCommittedList.append(player["foulsCommitted"])
    yellowCardsList.append(player["yellowCards"])
    redCardsList.append(player["redCards"])
    penaltiesWonList.append(player["penaltiesWon"])
    penaltiesCommittedList.append(player["penaltiesCommitted"])
    penaltiesScoredList.append(player["penaltiesScored"])
    penaltiesMissedList.append(player["penaltiesMissed"])
    penaltiesSavedList.append(player["penaltiesSaved"])
    winnerIdList.append(player["winnerId"])
    scoreList.append(player["score"])


offsidesNormList = (offsidesList-np.min(offsidesList))/(np.max(offsidesList)-np.min(offsidesList))
totalShotsNormList = (totalShotsList-np.min(totalShotsList))/(np.max(totalShotsList)-np.min(totalShotsList))
shotsOnNormList = (shotsOnList-np.min(shotsOnList))/(np.max(shotsOnList)-np.min(shotsOnList))
totalGoalsNormList = (totalGoalsList-np.min(totalGoalsList))/(np.max(totalGoalsList)-np.min(totalGoalsList))
concededGoalsNormList = (concededGoalsList-np.min(concededGoalsList))/(np.max(concededGoalsList)-np.min(concededGoalsList))
assistsNormList = (assistsList-np.min(assistsList))/(np.max(assistsList)-np.min(assistsList))
savesNormList = (savesList-np.min(savesList))/(np.max(savesList)-np.min(savesList))
totalPassesNormList = (totalPassesList-np.min(totalPassesList))/(np.max(totalPassesList)-np.min(totalPassesList))
keyPassesNormList = (keyPassesList-np.min(keyPassesList))/(np.max(keyPassesList)-np.min(keyPassesList))
totalTacklesNormList = (totalTacklesList-np.min(totalTacklesList))/(np.max(totalTacklesList)-np.min(totalTacklesList))
blockTacklesNormList = (blockTacklesList-np.min(blockTacklesList))/(np.max(blockTacklesList)-np.min(blockTacklesList))
interceptionTacklesNormList = (interceptionTacklesList-np.min(interceptionTacklesList))/(np.max(interceptionTacklesList)-np.min(interceptionTacklesList))
totalDuelsNormList = (totalDuelsList-np.min(totalDuelsList))/(np.max(totalDuelsList)-np.min(totalDuelsList))
duelsWonNormList = (duelsWonList-np.min(duelsWonList))/(np.max(duelsWonList)-np.min(duelsWonList))
dribblesAttemptsNormList = (dribblesAttemptsList-np.min(dribblesAttemptsList))/(np.max(dribblesAttemptsList)-np.min(dribblesAttemptsList))
dribblesSuccessNormList = (dribblesSuccessList-np.min(dribblesSuccessList))/(np.max(dribblesSuccessList)-np.min(dribblesSuccessList))
dribblesPastNormList = (dribblesPastList-np.min(dribblesPastList))/(np.max(dribblesPastList)-np.min(dribblesPastList))
foulsDrawnNormList = (foulsDrawnList-np.min(foulsDrawnList))/(np.max(foulsDrawnList)-np.min(foulsDrawnList))
foulsCommittedNormList = (foulsCommittedList-np.min(foulsCommittedList))/(np.max(foulsCommittedList)-np.min(foulsCommittedList))
yellowCardsNormList = (yellowCardsList-np.min(yellowCardsList))/(np.max(yellowCardsList)-np.min(yellowCardsList))
redCardsNormList = (redCardsList-np.min(redCardsList))/(np.max(redCardsList)-np.min(redCardsList))
penaltiesWonNormList = (penaltiesWonList-np.min(penaltiesWonList))/(np.max(penaltiesWonList)-np.min(penaltiesWonList))
penaltiesCommittedNormList = (penaltiesCommittedList-np.min(penaltiesCommittedList))/(np.max(penaltiesCommittedList)-np.min(penaltiesCommittedList))
penaltiesScoredNormList = (penaltiesScoredList-np.min(penaltiesScoredList))/(np.max(penaltiesScoredList)-np.min(penaltiesScoredList))
penaltiesMissedNormList = (penaltiesMissedList-np.min(penaltiesMissedList))/(np.max(penaltiesMissedList)-np.min(penaltiesMissedList))
penaltiesSavedNormList = (penaltiesSavedList-np.min(penaltiesSavedList))/(np.max(penaltiesSavedList)-np.min(penaltiesSavedList))

for i in range(len(playerIdList)):
    fixtureId = fixtureIdList[i]
    round = roundList[i]
    team = teamList[i]
    teamId = teamIdList[i]
    rivalTeam = rivalTeamList[i]
    rivalTeamId = rivalTeamIdList[i]
    playerId = playerIdList[i]
    playerName = playerNameList[i]
    playerPhoto = playerPhotoList[i]
    minutes = minutesList[i]
    offsides = offsidesNormList[i]
    totalShots = totalShotsNormList[i]
    shotsOn = shotsOnNormList[i]
    totalGoals = totalGoalsNormList[i]
    concededGoals = concededGoalsNormList[i]
    assists = assistsNormList[i]
    saves = savesNormList[i]
    totalPasses = totalPassesNormList[i]
    keyPasses = keyPassesNormList[i]
    passesAccuracy = passesAccuracyList[i]
    totalTackles = totalTacklesNormList[i]
    blockTackles = blockTacklesNormList[i]
    interceptionTackles = interceptionTacklesNormList[i]
    totalDuels = totalDuelsNormList[i]
    duelsWon = duelsWonNormList[i]
    dribblesAttempts = dribblesAttemptsNormList[i]
    dribblesSuccess = dribblesSuccessNormList[i]
    dribblesPast = dribblesPastNormList[i]
    foulsDrawn = foulsDrawnNormList[i]
    foulsCommitted = foulsCommittedNormList[i]
    yellowCards = yellowCardsNormList[i]
    redCards = redCardsNormList[i]
    penaltiesWon = penaltiesWonNormList[i]
    penaltiesCommitted = penaltiesCommittedNormList[i]
    penaltiesScored = penaltiesScoredNormList[i]
    penaltiesMissed = penaltiesMissedNormList[i]
    penaltiesSaved = penaltiesSavedNormList[i]
    winnerId = winnerIdList[i]
    score = scoreList[i]

    player = {"fixtureId":fixtureId, "round":round, "team":team,"teamId":teamId,"rivalTeam":rivalTeam, "rivalTeamId":rivalTeamId, "playerId":playerId, "playerName":playerName,
              "playerPhoto":playerPhoto, "minutes":minutes, "offsides":offsides, "totalShots":totalShots, "shotsOn":shotsOn, "totalGoals":totalGoals, "concededGoals": concededGoals, "assists": assists,
              "saves":saves, "totalPasses":totalPasses, "keyPasses": keyPasses, "passesAccuracy":passesAccuracy, "totalTackles":totalTackles, "blockTackles":blockTackles, "interceptionTackles":interceptionTackles,
              "totalDuels":totalDuels,"duelsWon":duelsWon, "dribblesAttempts":dribblesAttempts,"dribblesSuccess":dribblesSuccess,"dribblesPast":dribblesPast, "foulsDrawn":foulsDrawn,
              "foulsCommited":foulsCommitted,"yellowCards": yellowCards,"redCards": redCards,"penaltiesWon":penaltiesWon,"penaltiesCommited":penaltiesCommitted, "penaltiesScored":penaltiesScored,"penaltiesMissed":penaltiesMissed,
              "penaltiesSaved":penaltiesSaved, "score":score}

    print(player)

    playersNormalizedDataByMatch.insert_one(player)