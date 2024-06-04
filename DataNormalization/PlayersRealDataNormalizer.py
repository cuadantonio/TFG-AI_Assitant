import pymongo
import numpy as np
client = pymongo.MongoClient(
    "mongodb+srv://root:eODi!SbR5Xqo@cluster0.e9hmo.mongodb.net/footballdata?retryWrites=true&w=majority")
db = client["footballdata"]
playersRealData = db["PlayersRealData"]
playersRealNormalizedData = db["PlayersRealNormalizedData"]


players = playersRealData.find()

teamList = []
teamIdList = []
numberList = []
nameList = []
nicknameList = []
dateList = []
ageList = []
assistsList = []
blocksList = []
concededGoalsList = []
dribblesAttemptsList = []
dribblesSuccessList = []
duelsWonList = []
firstnameList = []
foulsCommittedList = []
foulsDrawnList = []
fullnameList = []
goalsList = []
heightList = []
interceptionsList = []
isInjuredList = []
keyPassesList = []
lastnameList = []
nationalityList = []
passesList = []
passesAccuracyList = []
penaltiesCommitedList = []
penaltiesMissedList = []
penaltiesSavedList = []
penaltiesScoredList = []
penaltiesWonList = []
photoList = []
playerIdList = []
positionList = []
ratingList = []
redCardsList = []
savesList = []
tacklesList = []
teamIdAuxList = []
totalDuelsList = []
totalShotsList = []
weightList = []
yellowCardsList = []
yellowredCardsList = []
biwengerPointsList = []
biwengerPriceList = []
biwengerPointsByMatchList = []
matchesList = []
minutesList = []
assistsByMatchesList = []
assistsByMinutesList = []
blocksByMatchesList = []
blocksByMinutesList = []
concededGoalsByMatchesList = []
concededGoalsByMinutesList = []
dribblesAttemptsByMatchesList = []
dribblesAttemptsByMinutesList = []
dribblesSuccessByMatchesList = []
dribblesSuccessByMinutesList = []
duelsWonByMatchesList = []
duelsWonByMinutesList = []
foulsCommittedByMatchesList = []
foulsCommittedByMinutesList = []
foulsDrawnByMatchesList = []
foulsDrawnByMinutesList = []
goalsByMatchesList = []
goalsByMinutesList = []
interceptionsByMatchesList = []
interceptionsByMinutesList = []
keyPassesByMatchesList = []
keyPassesByMinutesList = []
passesAccuracyByMatchesList = []
passesAccuracyByMinutesList = []
passesByMatchesList = []
passesByMinutesList = []
penaltiesCommitedByMatchesList = []
penaltiesCommitedByMinutesList = []
penaltiesMissedByMatchesList = []
penaltiesMissedByMinutesList = []
penaltiesSavedByMatchesList = []
penaltiesSavedByMinutesList = []
penaltiesScoredByMatchesList = []
penaltiesScoredByMinutesList = []
penaltiesWonByMatchesList = []
penaltiesWonByMinutesList = []
redCardsByMatchesList = []
redCardsByMinutesList = []
savesByMatchesList = []
savesByMinutesList = []
shotsOnByMatchesList = []
shotsOnByMinutesList = []
tacklesByMatchesList = []
tacklesByMinutesList = []
totalDuelsByMatchesList = []
totalDuelsByMinutesList = []
totalShotsByMatchesList = []
totalShotsByMinutesList = []
yellowCardsByMatchesList = []
yellowCardsByMinutesList = []
yellowRedCardsByMatchesList = []
yellowRedCardsByMinutesList = []
biwengerPointsByMinutesList = []

for player in players:
    teamList.append(player["team"])
    teamIdList.append(player["teamId"])
    numberList.append(player["number"])
    nameList.append(player["name"])
    nicknameList.append(player["nickname"])
    dateList.append(player["date"])
    ageList.append(player["age"])
    assistsList.append(player["assists"])
    blocksList.append(player["blocks"])
    concededGoalsList.append(player["concededGoals"])
    dribblesAttemptsList.append(player["dribblesAttempts"])
    dribblesSuccessList.append(player["dribblesSuccess"])
    duelsWonList.append(player["duelsWon"])
    firstnameList.append(player["firstname"])
    foulsCommittedList.append(player["foulsCommitted"])
    foulsDrawnList.append(player["foulsDrawn"])
    fullnameList.append(player["fullname"])
    goalsList.append(player["goals"])
    heightList.append(player["height"])
    interceptionsList.append(player["interceptions"])
    isInjuredList.append(player["isInjured"])
    keyPassesList.append(player["keyPasses"])
    lastnameList.append(player["lastname"])
    nationalityList.append(player["nationality"])
    passesList.append(player["passes"])
    passesAccuracyList.append(player["passesAccuracy"])
    penaltiesCommitedList.append(player["penaltiesCommited"])
    penaltiesMissedList.append(player["penaltiesMissed"])
    penaltiesSavedList.append(player["penaltiesSaved"])
    penaltiesScoredList.append(player["penaltiesScored"])
    penaltiesWonList.append(player["penaltiesWon"])
    photoList.append(player["photo"])
    playerIdList.append(player["playerId"])
    positionList.append(player["position"])
    ratingList.append(player["rating"])
    redCardsList.append(player["redCards"])
    savesList.append(player["saves"])
    tacklesList.append(player["tackles"])
    teamIdAuxList.append(player["teamIdAux"])
    totalDuelsList.append(player["totalDuels"])
    totalShotsList.append(player["totalShots"])
    weightList.append(player["weight"])
    yellowCardsList.append(player["yellowCards"])
    yellowredCardsList.append(player["yellowredCards"])
    biwengerPointsList.append(player["biwengerPoints"])
    biwengerPriceList.append(player["biwengerPrice"])
    biwengerPointsByMatchList.append(player["biwengerPointsByMatch"])
    matchesList.append(player["matches"])
    minutesList.append(player["minutes"])
    assistsByMatchesList.append(player["assistsByMatches"])
    assistsByMinutesList.append(player["assistsByMinutes"])
    blocksByMatchesList.append(player["blocksByMatches"])
    blocksByMinutesList.append(player["blocksByMinutes"])
    concededGoalsByMatchesList.append(player["concededGoalsByMatches"])
    concededGoalsByMinutesList.append(player["concededGoalsByMinutes"])
    dribblesAttemptsByMatchesList.append(player["dribblesAttemptsByMatches"])
    dribblesAttemptsByMinutesList.append(player["dribblesAttemptsByMinutes"])
    dribblesSuccessByMatchesList.append(player["dribblesSuccessByMatches"])
    dribblesSuccessByMinutesList.append(player["dribblesSuccessByMinutes"])
    duelsWonByMatchesList.append(player["duelsWonByMatches"])
    duelsWonByMinutesList.append(player["duelsWonByMinutes"])
    foulsCommittedByMatchesList.append(player["foulsCommittedByMatches"])
    foulsCommittedByMinutesList.append(player["foulsCommittedByMinutes"])
    foulsDrawnByMatchesList.append(player["foulsDrawnByMatches"])
    foulsDrawnByMinutesList.append(player["foulsDrawnByMinutes"])
    goalsByMatchesList.append(player["goalsByMatches"])
    goalsByMinutesList.append(player["goalsByMinutes"])
    interceptionsByMatchesList.append(player["interceptionsByMatches"])
    interceptionsByMinutesList.append(player["interceptionsByMinutes"])
    keyPassesByMatchesList.append(player["keyPassesByMatches"])
    keyPassesByMinutesList.append(player["keyPassesByMinutes"])
    passesAccuracyByMatchesList.append(player["passesAccuracyByMatches"])
    passesAccuracyByMinutesList.append(player["passesAccuracyByMinutes"])
    passesByMatchesList.append(player["passesByMatches"])
    passesByMinutesList.append(player["passesByMinutes"])
    penaltiesCommitedByMatchesList.append(player["penaltiesCommitedByMatches"])
    penaltiesCommitedByMinutesList.append(player["penaltiesCommitedByMinutes"])
    penaltiesMissedByMatchesList.append(player["penaltiesMissedByMatches"])
    penaltiesMissedByMinutesList.append(player["penaltiesMissedByMinutes"])
    penaltiesSavedByMatchesList.append(player["penaltiesSavedByMatches"])
    penaltiesSavedByMinutesList.append(player["penaltiesSavedByMinutes"])
    penaltiesScoredByMatchesList.append(player["penaltiesScoredByMatches"])
    penaltiesScoredByMinutesList.append(player["penaltiesScoredByMinutes"])
    penaltiesWonByMatchesList.append(player["penaltiesWonByMatches"])
    penaltiesWonByMinutesList.append(player["penaltiesWonByMinutes"])
    redCardsByMatchesList.append(player["redCardsByMatches"])
    redCardsByMinutesList.append(player["redCardsByMinutes"])
    savesByMatchesList.append(player["savesByMatches"])
    savesByMinutesList.append(player["savesByMinutes"])
    shotsOnByMatchesList.append(player["shotsOnByMatches"])
    shotsOnByMinutesList.append(player["shotsOnByMinutes"])
    tacklesByMatchesList.append(player["tacklesByMatches"])
    tacklesByMinutesList.append(player["tacklesByMinutes"])
    totalDuelsByMatchesList.append(player["totalDuelsByMatches"])
    totalDuelsByMinutesList.append(player["totalDuelsByMinutes"])
    totalShotsByMatchesList.append(player["totalShotsByMatches"])
    totalShotsByMinutesList.append(player["totalShotsByMinutes"])
    yellowCardsByMatchesList.append(player["yellowCardsByMatches"])
    yellowCardsByMinutesList.append(player["yellowCardsByMinutes"])
    yellowRedCardsByMatchesList.append(player["yellowRedCardsByMatches"])
    yellowRedCardsByMinutesList.append(player["yellowRedCardsByMinutes"])
    biwengerPointsByMinutesList.append(player["biwengerPointsByMinutes"])


assistsNormList = (assistsList-np.min(assistsList))/(np.max(assistsList)-np.min(assistsList))
blocksNormList = (blocksList-np.min(blocksList))/(np.max(blocksList)-np.min(blocksList))
concededGoalsNormList = (concededGoalsList-np.min(concededGoalsList))/(np.max(concededGoalsList)-np.min(concededGoalsList))
dribblesAttemptsNormList = (dribblesAttemptsList-np.min(dribblesAttemptsList))/(np.max(dribblesAttemptsList)-np.min(dribblesAttemptsList))
dribblesSuccessNormList = (dribblesSuccessList-np.min(dribblesSuccessList))/(np.max(dribblesSuccessList)-np.min(dribblesSuccessList))
duelsWonNormList = (duelsWonList-np.min(duelsWonList))/(np.max(duelsWonList)-np.min(duelsWonList))
foulsCommittedNormList = (foulsCommittedList-np.min(foulsCommittedList))/(np.max(foulsCommittedList)-np.min(foulsCommittedList))
foulsDrawnNormList = (foulsDrawnList-np.min(foulsDrawnList))/(np.max(foulsDrawnList)-np.min(foulsDrawnList))
goalsNormList = (goalsList-np.min(goalsList))/(np.max(goalsList)-np.min(goalsList))
interceptionsNormList = (interceptionsList-np.min(interceptionsList))/(np.max(interceptionsList)-np.min(interceptionsList))
keyPassesNormList = (keyPassesList-np.min(keyPassesList))/(np.max(keyPassesList)-np.min(keyPassesList))
passesNormList = (passesList-np.min(passesList))/(np.max(passesList)-np.min(passesList))
passesAccuracyNormList = (passesAccuracyList-np.min(passesAccuracyList))/(np.max(passesAccuracyList)-np.min(passesAccuracyList))
penaltiesMissedNormList = (penaltiesMissedList-np.min(penaltiesMissedList))/(np.max(penaltiesMissedList)-np.min(penaltiesMissedList))
penaltiesSavedNormList = (penaltiesSavedList-np.min(penaltiesSavedList))/(np.max(penaltiesSavedList)-np.min(penaltiesSavedList))
penaltiesScoredNormList = (penaltiesScoredList-np.min(penaltiesScoredList))/(np.max(penaltiesScoredList)-np.min(penaltiesScoredList))
redCardsNormList = (redCardsList-np.min(redCardsList))/(np.max(redCardsList)-np.min(redCardsList))
savesNormList = (savesList-np.min(savesList))/(np.max(savesList)-np.min(savesList))
tacklesNormList = (tacklesList-np.min(tacklesList))/(np.max(tacklesList)-np.min(tacklesList))
totalDuelsNormList = (totalDuelsList-np.min(totalDuelsList))/(np.max(totalDuelsList)-np.min(totalDuelsList))
totalShotsNormList = (totalShotsList-np.min(totalShotsList))/(np.max(totalShotsList)-np.min(totalShotsList))
yellowCardsNormList = (yellowCardsList-np.min(yellowCardsList))/(np.max(yellowCardsList)-np.min(yellowCardsList))
yellowredCardsNormList = (yellowredCardsList-np.min(yellowredCardsList))/(np.max(yellowredCardsList)-np.min(yellowredCardsList))
biwengerPointsNormList = (biwengerPointsList-np.min(biwengerPointsList))/(np.max(biwengerPointsList)-np.min(biwengerPointsList))
biwengerPointsByMatchNormList = (biwengerPointsByMatchList-np.min(biwengerPointsByMatchList))/(np.max(biwengerPointsByMatchList)-np.min(biwengerPointsByMatchList))
assistsByMatchesNormList = (assistsByMatchesList-np.min(assistsByMatchesList))/(np.max(assistsByMatchesList)-np.min(assistsByMatchesList))
assistsByMinutesNormList = (assistsByMinutesList-np.min(assistsByMinutesList))/(np.max(assistsByMinutesList)-np.min(assistsByMinutesList))
blocksByMatchesNormList = (blocksByMatchesList-np.min(blocksByMatchesList))/(np.max(blocksByMatchesList)-np.min(blocksByMatchesList))
blocksByMinutesNormList = (blocksByMinutesList-np.min(blocksByMinutesList))/(np.max(blocksByMinutesList)-np.min(blocksByMinutesList))
concededGoalsByMatchesNormList = (concededGoalsByMatchesList-np.min(concededGoalsByMatchesList))/(np.max(concededGoalsByMatchesList)-np.min(concededGoalsByMatchesList))
concededGoalsByMinutesNormList = (concededGoalsByMinutesList-np.min(concededGoalsByMinutesList))/(np.max(concededGoalsByMinutesList)-np.min(concededGoalsByMinutesList))
dribblesAttemptsByMatchesNormList = (dribblesAttemptsByMatchesList-np.min(dribblesAttemptsByMatchesList))/(np.max(dribblesAttemptsByMatchesList)-np.min(dribblesAttemptsByMatchesList))
dribblesAttemptsByMinutesNormList = (dribblesAttemptsByMinutesList-np.min(dribblesAttemptsByMinutesList))/(np.max(dribblesAttemptsByMinutesList)-np.min(dribblesAttemptsByMinutesList))
dribblesSuccessByMatchesNormList = (dribblesSuccessByMatchesList-np.min(dribblesSuccessByMatchesList))/(np.max(dribblesSuccessByMatchesList)-np.min(dribblesSuccessByMatchesList))
dribblesSuccessByMinutesNormList = (dribblesSuccessByMinutesList-np.min(dribblesSuccessByMinutesList))/(np.max(dribblesSuccessByMinutesList)-np.min(dribblesSuccessByMinutesList))
duelsWonByMatchesNormList = (duelsWonByMatchesList-np.min(duelsWonByMatchesList))/(np.max(duelsWonByMatchesList)-np.min(duelsWonByMatchesList))
duelsWonByMinutesNormList = (duelsWonByMinutesList-np.min(duelsWonByMinutesList))/(np.max(duelsWonByMinutesList)-np.min(duelsWonByMinutesList))
foulsCommittedByMatchesNormList = (foulsCommittedByMatchesList-np.min(foulsCommittedByMatchesList))/(np.max(foulsCommittedByMatchesList)-np.min(foulsCommittedByMatchesList))
foulsCommittedByMinutesNormList = (foulsDrawnByMinutesList-np.min(foulsDrawnByMinutesList))/(np.max(foulsDrawnByMinutesList)-np.min(foulsDrawnByMinutesList))
foulsDrawnByMatchesNormList = (foulsDrawnByMatchesList-np.min(foulsDrawnByMatchesList))/(np.max(foulsDrawnByMatchesList)-np.min(foulsDrawnByMatchesList))
foulsDrawnByMinutesNormList = (foulsDrawnByMinutesList-np.min(foulsDrawnByMinutesList))/(np.max(foulsDrawnByMinutesList)-np.min(foulsDrawnByMinutesList))
goalsByMatchesNormList = (goalsByMatchesList-np.min(goalsByMatchesList))/(np.max(goalsByMatchesList)-np.min(goalsByMatchesList))
goalsByMinutesNormList = (goalsByMinutesList-np.min(goalsByMinutesList))/(np.max(goalsByMinutesList)-np.min(goalsByMinutesList))
interceptionsByMatchesNormList = (interceptionsByMatchesList-np.min(interceptionsByMatchesList))/(np.max(interceptionsByMatchesList)-np.min(interceptionsByMatchesList))
interceptionsByMinutesNormList = (interceptionsByMinutesList-np.min(interceptionsByMinutesList))/(np.max(interceptionsByMinutesList)-np.min(interceptionsByMinutesList))
keyPassesByMatchesNormList = (keyPassesByMatchesList-np.min(keyPassesByMatchesList))/(np.max(keyPassesByMatchesList)-np.min(keyPassesByMatchesList))
keyPassesByMinutesNormList = (keyPassesByMinutesList-np.min(keyPassesByMinutesList))/(np.max(keyPassesByMinutesList)-np.min(keyPassesByMinutesList))
passesAccuracyByMatchesNormList = (passesAccuracyByMatchesList-np.min(passesAccuracyByMatchesList))/(np.max(passesAccuracyByMatchesList)-np.min(passesAccuracyByMatchesList))
passesAccuracyByMinutesNormList = (passesAccuracyByMinutesList-np.min(passesAccuracyByMinutesList))/(np.max(passesAccuracyByMinutesList)-np.min(passesAccuracyByMinutesList))
passesByMatchesNormList = (passesByMatchesList-np.min(passesByMatchesList))/(np.max(passesByMatchesList)-np.min(passesByMatchesList))
passesByMinutesNormList = (passesByMinutesList-np.min(passesByMinutesList))/(np.max(passesByMinutesList)-np.min(passesByMinutesList))
penaltiesMissedByMatchesNormList = (penaltiesMissedByMatchesList-np.min(penaltiesMissedByMatchesList))/(np.max(penaltiesMissedByMatchesList)-np.min(penaltiesMissedByMatchesList))
penaltiesMissedByMinutesNormList = (penaltiesMissedByMinutesList-np.min(penaltiesMissedByMinutesList))/(np.max(penaltiesMissedByMinutesList)-np.min(penaltiesMissedByMinutesList))
penaltiesSavedByMatchesNormList = (penaltiesSavedByMatchesList-np.min(penaltiesSavedByMatchesList))/(np.max(penaltiesSavedByMatchesList)-np.min(penaltiesSavedByMatchesList))
penaltiesSavedByMinutesNormList = (penaltiesSavedByMinutesList-np.min(penaltiesSavedByMinutesList))/(np.max(penaltiesSavedByMinutesList)-np.min(penaltiesSavedByMinutesList))
penaltiesScoredByMatchesNormList = (penaltiesScoredByMatchesList-np.min(penaltiesScoredByMatchesList))/(np.max(penaltiesScoredByMatchesList)-np.min(penaltiesScoredByMatchesList))
penaltiesScoredByMinutesNormList = (penaltiesScoredByMinutesList-np.min(penaltiesScoredByMinutesList))/(np.max(penaltiesScoredByMinutesList)-np.min(penaltiesScoredByMinutesList))
redCardsByMatchesNormList = (redCardsByMatchesList-np.min(redCardsByMatchesList))/(np.max(redCardsByMatchesList)-np.min(redCardsByMatchesList))
redCardsByMinutesNormList = (redCardsByMinutesList-np.min(redCardsByMinutesList))/(np.max(redCardsByMinutesList)-np.min(redCardsByMinutesList))
savesByMatchesNormList = (savesByMatchesList-np.min(savesByMatchesList))/(np.max(savesByMatchesList)-np.min(savesByMatchesList))
savesByMinutesNormList = (savesByMinutesList-np.min(savesByMinutesList))/(np.max(savesByMinutesList)-np.min(savesByMinutesList))
shotsOnByMatchesNormList = (shotsOnByMatchesList-np.min(shotsOnByMatchesList))/(np.max(shotsOnByMatchesList)-np.min(shotsOnByMatchesList))
shotsOnByMinutesNormList = (shotsOnByMatchesList-np.min(shotsOnByMatchesList))/(np.max(shotsOnByMatchesList)-np.min(shotsOnByMatchesList))
tacklesByMatchesNormList = (tacklesByMatchesList-np.min(tacklesByMatchesList))/(np.max(tacklesByMatchesList)-np.min(tacklesByMatchesList))
tacklesByMinutesNormList = (tacklesByMinutesList-np.min(tacklesByMinutesList))/(np.max(tacklesByMinutesList)-np.min(tacklesByMinutesList))
totalDuelsByMatchesNormList = (totalDuelsByMatchesList-np.min(totalDuelsByMatchesList))/(np.max(totalDuelsByMatchesList)-np.min(totalDuelsByMatchesList))
totalDuelsByMinutesNormList = (totalDuelsByMinutesList-np.min(totalDuelsByMinutesList))/(np.max(totalDuelsByMinutesList)-np.min(totalDuelsByMinutesList))
totalShotsByMatchesNormList = (totalShotsByMatchesList-np.min(totalShotsByMatchesList))/(np.max(totalShotsByMatchesList)-np.min(totalShotsByMatchesList))
totalShotsByMinutesNormList = (totalShotsByMinutesList-np.min(totalShotsByMinutesList))/(np.max(totalShotsByMinutesList)-np.min(totalShotsByMinutesList))
yellowCardsByMatchesNormList = (yellowCardsByMatchesList-np.min(yellowCardsByMatchesList))/(np.max(yellowCardsByMatchesList)-np.min(yellowCardsByMatchesList))
yellowCardsByMinutesNormList = (yellowCardsByMinutesList-np.min(yellowCardsByMinutesList))/(np.max(yellowCardsByMinutesList)-np.min(yellowCardsByMinutesList))
yellowRedCardsByMatchesNormList = (yellowRedCardsByMatchesList-np.min(yellowRedCardsByMatchesList))/(np.max(yellowRedCardsByMatchesList)-np.min(yellowRedCardsByMatchesList))
yellowRedCardsByMinutesNormList = (yellowRedCardsByMinutesList-np.min(yellowRedCardsByMinutesList))/(np.max(yellowRedCardsByMinutesList)-np.min(yellowRedCardsByMinutesList))
biwengerPointsByMinutesNormList = (biwengerPointsByMinutesList-np.min(biwengerPointsByMinutesList))/(np.max(biwengerPointsByMinutesList)-np.min(biwengerPointsByMinutesList))

print()
print(len(playerIdList))

for i in range(len(playerIdList)):
    team = teamList[i]
    teamId = teamIdList[i]
    number = numberList[i]
    name =nameList[i]
    nickname =nicknameList[i]
    date =dateList[i]
    age =ageList[i]
    assists =assistsNormList[i]
    blocks =blocksNormList[i]
    concededGoals =concededGoalsNormList[i]
    dribblesAttempts =dribblesAttemptsNormList[i]
    dribblesSuccess =dribblesSuccessNormList[i]
    duelsWon =duelsWonNormList[i]
    firstname =firstnameList[i]
    foulsCommitted =foulsCommittedNormList[i]
    foulsDrawn =foulsDrawnNormList[i]
    fullname =fullnameList[i]
    goals =goalsNormList[i]
    height =heightList[i]
    interceptions =interceptionsNormList[i]
    isInjured =isInjuredList[i]
    keyPasses =keyPassesNormList[i]
    lastname =lastnameList[i]
    nationality =nationalityList[i]
    passes =passesNormList[i]
    passesAccuracy =passesAccuracyNormList[i]
    penaltiesCommited =penaltiesCommitedList[i]
    penaltiesMissed =penaltiesMissedNormList[i]
    penaltiesSaved =penaltiesSavedNormList[i]
    penaltiesScored =penaltiesScoredNormList[i]
    penaltiesWon =penaltiesWonList[i]
    photo =photoList[i]
    playerId =playerIdList[i]
    position = positionList[i]
    rating = ratingList[i]
    redCards = redCardsNormList[i]
    saves =savesNormList[i]
    tackles = tacklesNormList[i]
    teamIdAux = teamIdAuxList[i]
    totalDuels = totalDuelsNormList[i]
    totalShots = totalShotsNormList[i]
    weight = weightList[i]
    yellowCards = yellowCardsNormList[i]
    yellowredCards =yellowredCardsNormList[i]
    biwengerPoints =biwengerPointsNormList[i]
    biwengerPrice =biwengerPriceList[i]
    biwengerPointsByMatch =biwengerPointsByMatchNormList[i]
    matches =matchesList[i]
    minutes =minutesList[i]
    assistsByMatches =assistsByMatchesNormList[i]
    assistsByMinutes =assistsByMinutesNormList[i]
    blocksByMatches =blocksByMatchesNormList[i]
    blocksByMinutes =blocksByMinutesNormList[i]
    concededGoalsByMatches =concededGoalsByMatchesNormList[i]
    concededGoalsByMinutes =concededGoalsByMatchesNormList[i]
    dribblesAttemptsByMatches =dribblesAttemptsByMatchesNormList[i]
    dribblesAttemptsByMinutes =dribblesAttemptsByMinutesNormList[i]
    dribblesSuccessByMatches =dribblesSuccessByMatchesNormList[i]
    dribblesSuccessByMinutes =dribblesSuccessByMinutesNormList[i]
    duelsWonByMatches =duelsWonByMatchesNormList[i]
    duelsWonByMinutes =duelsWonByMinutesNormList[i]
    foulsCommittedByMatches =foulsCommittedByMatchesNormList[i]
    foulsCommittedByMinutes =foulsCommittedByMinutesNormList[i]
    foulsDrawnByMatches =foulsDrawnByMatchesNormList[i]
    foulsDrawnByMinutes =foulsDrawnByMinutesNormList[i]
    goalsByMatches =goalsByMatchesNormList[i]
    goalsByMinutes =goalsByMinutesNormList[i]
    interceptionsByMatches =interceptionsByMatchesNormList[i]
    interceptionsByMinutes =interceptionsByMinutesNormList[i]
    keyPassesByMatches =keyPassesByMatchesNormList[i]
    keyPassesByMinutes =keyPassesByMinutesNormList[i]
    passesAccuracyByMatches =passesAccuracyByMatchesNormList[i]
    passesAccuracyByMinutes =passesAccuracyByMinutesNormList[i]
    passesByMatches =passesByMatchesNormList[i]
    passesByMinutes =passesByMinutesNormList[i]
    penaltiesCommitedByMatches =penaltiesCommitedByMatchesList[i]
    penaltiesCommitedByMinutes =penaltiesCommitedByMinutesList[i]
    penaltiesMissedByMatches =penaltiesMissedByMatchesNormList[i]
    penaltiesMissedByMinutes = penaltiesMissedByMinutesNormList[i]
    penaltiesSavedByMatches =penaltiesSavedByMatchesNormList[i]
    penaltiesSavedByMinutes =penaltiesSavedByMinutesNormList[i]
    penaltiesScoredByMatches =penaltiesScoredByMatchesNormList[i]
    penaltiesScoredByMinutes =penaltiesScoredByMinutesNormList[i]
    penaltiesWonByMatches =penaltiesWonByMatchesList[i]
    penaltiesWonByMinutes =penaltiesWonByMinutesList[i]
    redCardsByMatches =redCardsByMatchesNormList[i]
    redCardsByMinutes =redCardsByMinutesNormList[i]
    savesByMatches =savesByMatchesNormList[i]
    savesByMinutes =savesByMinutesNormList[i]
    shotsOnByMatches =shotsOnByMatchesNormList[i]
    shotsOnByMinutes =shotsOnByMinutesNormList[i]
    tacklesByMatches =tacklesByMatchesNormList[i]
    tacklesByMinutes =tacklesByMinutesNormList[i]
    totalDuelsByMatches =totalDuelsByMatchesNormList[i]
    totalDuelsByMinutes =totalDuelsByMinutesNormList[i]
    totalShotsByMatches =totalShotsByMatchesNormList[i]
    totalShotsByMinutes =totalShotsByMinutesNormList[i]
    yellowCardsByMatches =yellowCardsByMatchesNormList[i]
    yellowCardsByMinutes =yellowCardsByMinutesNormList[i]
    yellowRedCardsByMatches =yellowRedCardsByMatchesNormList[i]
    yellowRedCardsByMinutes =yellowRedCardsByMinutesNormList[i]
    biwengerPointsByMinutes =biwengerPointsByMinutesNormList[i]
    player = {"team": team, "teamId":teamId, "number": number, "name": name, "nickname": nickname, "date": date, "age": age, "assists":assists,
              "blocks": blocks, "concededGoals": concededGoals, "dribblesAttempts":dribblesAttempts, "dribblesSuccess": dribblesSuccess, "duelsWon":duelsWon,
              "firstname": firstname,"foulsCommitted":foulsCommitted, "foulsDrawn":foulsDrawn, "fullname":fullname, "goals":goals, "height": height,
              "interceptions": interceptions, "isInjured": isInjured, "keyPasses": keyPasses, "lastname":lastname, "nationality": nationality, "passes": passes,
              "passesAccuracy": passesAccuracy, "penaltiesCommitted":penaltiesCommited, "penaltiesMissed":penaltiesMissed, "penaltiesSaved":penaltiesSaved, "penaltiesScored": penaltiesScored,
              "penaltiesWon":penaltiesWon,"photo":photo, "playerId":playerId, "position":position, "rating":rating, "redCards":redCards, "saves":saves, "tackles":tackles, "teamIdAux":teamIdAux,
              "totalDuels":totalDuels, "weight":weight, "yellowCards":yellowCards, "yellowRedCards": yellowredCards, "biwengerPoints":biwengerPoints, "biwengerPrice": biwengerPrice, "biwengerPointsByMatch":biwengerPointsByMatch,
              "matches":matches, "minutes":minutes, "assistsByMatches":assistsByMatches, "assistsByMinutes":assistsByMinutes, "blocksByMatches":blocksByMatches, "blocksByMinutes":blocksByMinutes,
              "concededGoalsByMatches":concededGoalsByMatches, "concededGoalsByMinutes":concededGoalsByMinutes,"dribblesAttemptsByMatches":dribblesAttemptsByMatches, "dribblesAttemptsByMinutes":dribblesAttemptsByMinutes,
              "dribblesSuccessByMatches":dribblesSuccessByMatches, "dribblesSuccessByMinutes":dribblesSuccessByMinutes, "duelsWonByMatches":duelsWonByMatches, "duelsWonByMinutes":duelsWonByMinutes, "foulsCommittedByMatches":foulsCommittedByMatches,
              "foulsCommittedByMinutes": foulsCommittedByMinutes, "foulsDrawnByMatches":foulsDrawnByMatches, "foulsDrawnByMinutes":foulsDrawnByMinutes, "goalsByMatches":goalsByMatches,
              "goalsByMinutes":goalsByMinutes,"interceptionsByMatches":interceptionsByMatches, "interceptionsByMinutes":interceptionsByMinutes, "keyPassesByMatches":keyPassesByMatches, "keyPassesByMinutes":keyPassesByMinutes,
              "passesAccuracyByMatches":passesAccuracyByMatches, "passesAccuracyByMinutes":passesAccuracyByMinutes, "passesByMatches":passesByMatches, "passesByMinutes":passesByMinutes,
              "penaltiesCommitedByMatches":penaltiesCommitedByMatches, "penaltiesCommitedByMinutes":penaltiesCommitedByMinutes, "penaltiesMissedByMatches":penaltiesMissedByMatches, "penaltiesMissedByMinutes":penaltiesMissedByMinutes,
              "penaltiesSavedByMatches":penaltiesSavedByMatches, "penaltiesSavedByMinutes":penaltiesSavedByMinutes, "penaltiesScoredByMatches":penaltiesScoredByMatches, "penaltiesScoredByMinutes":penaltiesScoredByMinutes,
              "penaltiesWonByMatches":penaltiesWonByMatches, "penaltiesWonByMinutes":penaltiesWonByMinutes,"redCardsByMatches":redCardsByMatches, "redCardsByMinutes":redCardsByMinutes, "savesByMatches":savesByMatches, "savesByMinutes":savesByMinutes,
              "tacklesByMatches":tacklesByMatches, "tacklesByMinutes":tacklesByMinutes,"totalDuelsByMatches":totalDuelsByMatches,"totalDuelsByMinutes":totalDuelsByMinutes, "totalShotsByMatches":totalShotsByMatches,
              "totalShotsByMinutes":totalShotsByMinutes, "yellowCardsByMatches":yellowCardsByMatches, "yellowCardsByMinutes":yellowCardsByMinutes, "yellowRedCardsByMatches":yellowRedCardsByMatches, "yellowRedCardsByMinutes":yellowRedCardsByMinutes,
              "biwengerPointsByMinutes":biwengerPointsByMinutes}
    playersRealNormalizedData.insert_one(player)



