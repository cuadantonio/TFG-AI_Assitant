from AssignPlayers import *

gks = getGoalkeepers(10,-1)[:5]
dfs = getDefenders(10,-1)[:25]
mfs = getMidfielders(10,-1)[:20]
ats = getAttackers(10,-1)[:5]

players = gks + dfs + mfs + ats
playersPoints = getPlayersPointsBySum(players,10,-1)
playersPrices = getPlayersPrice(players)
playerPositions = getPositions(players)

playersAveragePrice = getAveragePrice(players)
priceLimitBase = playersAveragePrice*11
priceLimitBase *= 1

#Prueba 1: tiempo cambio numero jugadores (Cambiar numero de jugadores por posicion)

startNoPod = time.time()
optPointsNoPod = 0
optSolutionNoPod = []
optPlayersSolNoPod, optPointsSolNoPod = calcPlayersWithPriceNoPod(players, playersPrices, playersPoints, playerPositions, positionLimits541, 100000000000, 0, [], 0, 0, currentPositions2, startNoPod, 3600)
finishNoPod = time.time()

noPodTime = finishNoPod - startNoPod
print(optPlayersSolNoPod, optPointsSolNoPod)
print("No poda",noPodTime)



startPod = time.time()
optPlayersSolLPod, optPointsSolLPod = calcPlayersWithPrice(players, playersPrices, playersPoints, playerPositions, positionLimits541, 100000000000, 0, [], 0, 0, currentPositions, startPod, 3600)
finishPod = time.time()

podTime = finishPod - startPod
print(optPlayersSolLPod, optPointsSolLPod)
print("Poda",podTime)

#Prueba 2: tiempo cambio presupuesto (Cambiar multiplicador de priceLimitBase)

startNoPod = time.time()
optPointsNoPod = 0
optSolutionNoPod = []
optPlayersSolNoPod, optPointsSolNoPod = calcPlayersWithPriceNoPod(players, playersPrices, playersPoints, playerPositions, positionLimits541, priceLimitBase, 0, [], 0, 0, currentPositions2, startNoPod, 3600)
finishNoPod = time.time()

noPodTime = finishNoPod - startNoPod
print(optPlayersSolNoPod, optPointsSolNoPod)
print("No poda",noPodTime)



startPod = time.time()
optPlayersSolLPod, optPointsSolLPod = calcPlayersWithPrice(players, playersPrices, playersPoints, playerPositions, positionLimits541, priceLimitBase, 0, [], 0, 0, currentPositions, startPod, 3600)
finishPod = time.time()

podTime = finishPod - startPod
print(optPlayersSolLPod, optPointsSolLPod)
print("Poda",podTime)

#Prueba 3: comprobacion si merece la pena dejar ejecutando o parar (Cambiar el timeLimit)
timeLimit = 3600
startTime = time.time()
print("Start")
optPlayersSolLPod, optPointsSolLPod = calcPlayersWithPrice(players, playersPrices, playersPoints, playerPositions,
                                                           positionLimits541, 100000000000, 0, [], 0, 0,
                                                           currentPositions, startTime, timeLimit)

print("End")
print("Players",optPlayersSolLPod)
print("Points",optPointsSolLPod)


startTime = time.time()
print("Start")
optPlayersSolNoPod, optPointsSolNoPod = calcPlayersWithPriceNoPod(players, playersPrices, playersPoints, playerPositions,
                                                           positionLimits541, 100000000000, 0, [], 0, 0,
                                                           currentPositions, startTime, timeLimit)

print("End")
print("Players",optPlayersSolNoPod)
print("Points",optPointsSolNoPod)