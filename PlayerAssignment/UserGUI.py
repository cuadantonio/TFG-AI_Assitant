import PySimpleGUI as sg
import time
import pygame
import requests
from io import BytesIO
import sys
from AssignPlayers import *


round = 0
lastRounds = -1
lineup = []
positionLimits = {}
priceLimit = 0
timeLimit = 0

inputListColumn = [
    [
        sg.Text('Jornada Actual', font="Calibri"),
        sg.Push(),
        sg.In(size=(25,1), enable_events = True, key="-JOR-", font="Calibri"),
    ],
    [
        sg.Text('Últimas jornadas', font="Calibri"),
        sg.Push(),
        sg.In(size=(25,1), enable_events = True, key="-LIMJOR-", font="Calibri"),
    ],
    [
        sg.Text('Límite de precio', font="Calibri"),
        sg.Push(),
        sg.In(size=(25,1), enable_events = True, key="-LIMPRE-", font="Calibri"),
    ],
    [
        sg.Text('Formación', font="Calibri"),
        sg.Push(),
        sg.Combo(
            values=["1. 3-4-3", "2. 3-5-2", "3. 4-3-3", "4. 4-4-2", "5. 4-5-1", "6. 5-3-2", "7. 5-4-1"], enable_events=True, size=(24,1), key="-FORMS-", font="Calibri"
        )
    ],
    [
        sg.Text('Límite de tiempo', font="Calibri"),
        sg.Push(),
        sg.In(size=(25,1), enable_events = True, key="-LIMTIE-", font="Calibri"),
    ],
    [
        sg.Button(button_text="Calcular", enable_events=True, key="-BUTTON-", border_width=3)
    ]
]

layout = [
    [
        sg.Column(inputListColumn, element_justification='c'),
    ]
]

window = sg.Window("User GUI", layout)
while True:
    pyGuiEvent, values = window.read()
    if pyGuiEvent == "Exit" or pyGuiEvent == sg.WIN_CLOSED:
        break
    if pyGuiEvent == "-JOR-":
        round = values["-JOR-"]
        print(round)

    if pyGuiEvent == "-LIMJOR-":
        lastRounds = values["-LIMJOR-"]
        print(lastRounds)

    if pyGuiEvent == "-LIMPRE-":
        priceLimit = values["-LIMPRE-"]

    if pyGuiEvent == "-LIMTIE-":
        timeLimit = int(values["-LIMTIE-"])
        timeLimit = timeLimit * 60

    if pyGuiEvent == "-FORMS-":
        print(lastRounds)
        print(values["-FORMS-"])
        option = int(str(values["-FORMS-"][0]).split(".")[0])
        match option:
            case 1:
                lineup = [3, 4, 3]
                positionLimits = positionLimits343
            case 2:
                lineup = [3, 5, 2]
                positionLimits = positionLimits352
            case 3:
                lineup = [4, 3, 3]
                positionLimits = positionLimits433
            case 4:
                lineup = [4, 4, 2]
                positionLimits = positionLimits442
            case 5:
                lineup = [4, 5, 1]
                positionLimits = positionLimits451
            case 6:
                lineup = [5, 3, 2]
                positionLimits = positionLimits532
            case 7:
                lineup = [5, 4, 1]
                positionLimits = positionLimits541
    if pyGuiEvent == "-BUTTON-" and lineup is not None and round is not None :
        print(lineup)
        print(round)
        print(lastRounds)
        print(type(lineup))
        print(type(round))
        print(type(lastRounds))

        priceLimit = int(priceLimit)
        round = int(round)

        if lastRounds == "":
            lastRounds = -1
        elif lastRounds is not None and type(lastRounds) == str:
            lastRounds = int(lastRounds)
            if lastRounds > round:
                continue

        inicioC = time.time()
        players = getPlayersBySum(round, lastRounds)
        prices = getPlayersPrice(players)
        points = getPlayersPointsBySum(players, round, lastRounds)
        positions = getPositions(players)
        print('Got it')
        startTime = time.time()
        currentPositions = {'Goalkeeper':0, 'Defender': 0, 'Midfielder': 0, 'Attacker': 0}
        optPlayersSol, optPointsSol = calcPlayersWithPrice(players,prices,points,positions,positionLimits,priceLimit,
                                                           0,[],0,0,
                                                           currentPositions, startTime, timeLimit)
        finC = time.time()
        execTime = str(int(finC - inicioC))
        execTimeText = 'Tiempo de ejecucion: ' + execTime + ' segundos'
        optPointsSol = str(optPointsSol)
        newPoints = str(int(sum(getPlayersPointsInRound(optPlayersSol,round))))
        pointsText = 'Puntos obtenidos: ' + newPoints

        if optPlayersSol != []:
            pygame.init()

            WHITE = (255, 255, 255)
            BLACK = (0, 0, 0)

            WIDTH = 800
            HEIGHT = 600
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Alineación de Fútbol")

            fieldImage = pygame.image.load("campo_futbol.jpg")
            fieldImage = pygame.transform.scale(fieldImage, (WIDTH, HEIGHT))

            optPlayersSol = reformatPlayers(optPlayersSol)

            playerNames = getPlayersNicknames(optPlayersSol)
            playerPhotos = getPlayersImages(optPlayersSol)


            def loadImageFromUrl(url):
                response = requests.get(url)
                image = pygame.image.load(BytesIO(response.content))
                return image
            def drawPlayer(position, name, imageURL):
                font = pygame.font.SysFont("Gill Sans", 20)
                text = font.render(name, True, BLACK, WHITE)
                rectangle = text.get_rect()
                rectangle.center = (
                    position[0], position[1] - 20)  # Modificado para que el nombre esté encima del jugador
                screen.blit(text, rectangle)

                image = loadImageFromUrl(imageURL)
                image = pygame.transform.scale(image, (50, 50))
                imageRectangle = image.get_rect()
                imageRectangle.center = (position[0], position[1] + 20)
                screen.blit(image, imageRectangle)

            def draw343(players, imagesUrls, points, execTime):
                basePositions = {
                    "Goalkeeper": (WIDTH // 2, HEIGHT // 7),
                    "Defender": [(WIDTH // 4, HEIGHT // 3), (WIDTH // 2, HEIGHT // 3), (3 * WIDTH // 4, HEIGHT // 3)],
                    "Midfielder": [(WIDTH // 4, 1.75 * HEIGHT // 3), (1.6 * WIDTH // 4, 1.75 * HEIGHT // 3),
                                       (2.4 * WIDTH // 4, 1.75 * HEIGHT // 3), (3 * WIDTH // 4, 1.75 * HEIGHT // 3)],
                    "Attacker": [(WIDTH // 4, 5 * HEIGHT // 6), (WIDTH // 2, 5 * HEIGHT // 6),
                                  (3 * WIDTH // 4, 5 * HEIGHT // 6)]
                }

                screen.fill(BLACK)
                screen.blit(fieldImage, (0, 0))

                for i, row in enumerate(players):
                    for j, player in enumerate(row):
                        name = player
                        imageUrl = imagesUrls[i][j]
                        if i == 0:
                            basePosition = basePositions["Goalkeeper"]
                        elif i == 1:
                            basePosition = basePositions["Defender"][j]
                        elif i == 2:
                            basePosition = basePositions["Midfielder"][j]
                        else:
                            basePosition = basePositions["Attacker"][j]
                        drawPlayer(basePosition, name, imageUrl)

                pointsFont = pygame.font.SysFont("Gill Sans", 20)
                pointsText = pointsFont.render(points, True, BLACK, WHITE)
                pointsRect = pointsText.get_rect()
                pointsRect.center = (
                    WIDTH // 2, HEIGHT-10)
                screen.blit(pointsText, pointsRect)

                execTimeFont = pygame.font.SysFont("Gill Sans", 20)
                execTimeText = execTimeFont.render(execTime, True, BLACK, WHITE)
                execTimeRect = execTimeText.get_rect()
                execTimeRect.center = (
                    WIDTH // 2, HEIGHT - 31)
                screen.blit(execTimeText, execTimeRect)
                # Manejo de eventos

                pygame.display.flip()
            def draw442(players, imagesUrls):
                basePositions = {
                    "Goalkeeper": (WIDTH // 2, HEIGHT // 7),
                    "Defender": [(WIDTH // 4, HEIGHT // 3), (1.6 * WIDTH // 4, HEIGHT // 3),
                                (2.4 * WIDTH // 4, HEIGHT // 3), (3 * WIDTH // 4, HEIGHT // 3)],
                    "Midfielder": [(WIDTH // 4, 1.75 * HEIGHT // 3), (1.6 * WIDTH // 4, 1.75 * HEIGHT // 3),
                                       (2.4 * WIDTH // 4, 1.75 * HEIGHT // 3), (3 * WIDTH // 4, 1.75 * HEIGHT // 3)],
                    "Attacker": [(1.5* WIDTH // 4, 5 * HEIGHT // 6), (2.5*WIDTH // 4, 5 * HEIGHT // 6)]
                }

                screen.fill(BLACK)
                screen.blit(fieldImage, (0, 0))

                # Dibujar jugadores en las posiciones correspondientes
                for i, row in enumerate(players):
                    for j, player in enumerate(row):
                        name = player
                        imageUrl = imagesUrls[i][j]
                        if i == 0:
                            basePosition = basePositions["Goalkeeper"]
                        elif i == 1:
                            basePosition = basePositions["Defender"][j]
                        elif i == 2:
                            basePosition = basePositions["Midfielder"][j]
                        else:
                            basePosition = basePositions["Attacker"][j]
                        drawPlayer(basePosition, name, imageUrl)

                pygame.display.flip()
            def draw541(players, imagesUrls):
                basePositions = {
                    "Goalkeeper": (WIDTH // 2, HEIGHT // 7),
                    "Defender": [(WIDTH // 4, HEIGHT // 3), (1.5 * WIDTH // 4, HEIGHT // 3), (2 * WIDTH // 4, HEIGHT // 3),
                                (2.5 * WIDTH // 4, HEIGHT // 3), (3 * WIDTH // 4, HEIGHT // 3)],
                    "Midfielder": [(WIDTH // 4, 1.75 * HEIGHT // 3), (1.6 * WIDTH // 4, 1.75 * HEIGHT // 3),
                                       (2.4 * WIDTH // 4, 1.75 * HEIGHT // 3), (3 * WIDTH // 4, 1.75 * HEIGHT // 3)],
                    "Attacker": [(WIDTH // 2, 5 * HEIGHT // 6)]
                }

                screen.fill(BLACK)
                screen.blit(fieldImage, (0, 0))

                for i, row in enumerate(players):
                    for j, player in enumerate(row):
                        name = player
                        imageUrl = imagesUrls[i][j]
                        if i == 0:
                            basePosition = basePositions["Goalkeeper"]
                        elif i == 1:
                            basePosition = basePositions["Defender"][j]
                        elif i == 2:
                            basePosition = basePositions["Midfielder"][j]
                        else:
                            basePosition = basePositions["Attacker"][j]
                        drawPlayer(basePosition, name, imageUrl)

                pygame.display.flip()
            def draw451(players, imagesUrls):
                basePositions = {
                    "Goalkeeper": (WIDTH // 2, HEIGHT // 7),
                    "Defender": [(WIDTH // 4, HEIGHT // 3), (1.6 * WIDTH // 4, HEIGHT // 3),
                                (2.4 * WIDTH // 4, HEIGHT // 3), (3 * WIDTH // 4, HEIGHT // 3)],
                    "Midfielder": [(WIDTH // 4, 1.75 * HEIGHT // 3), (1.5 * WIDTH // 4, 1.75 * HEIGHT // 3),
                                       (2 * WIDTH // 4, 1.75 * HEIGHT // 3),
                                       (2.5 * WIDTH // 4, 1.75 * HEIGHT // 3), (3 * WIDTH // 4, 1.75 * HEIGHT // 3)],
                    "Attacker": [(WIDTH // 2, 5 * HEIGHT // 6)]
                }

                screen.fill(BLACK)
                screen.blit(fieldImage, (0, 0))

                for i, row in enumerate(players):
                    for j, player in enumerate(row):
                        name = player
                        imageUrl = imagesUrls[i][j]
                        if i == 0:
                            basePosition = basePositions["Goalkeeper"]
                        elif i == 1:
                            basePosition = basePositions["Defender"][j]
                        elif i == 2:
                            basePosition = basePositions["Midfielder"][j]
                        else:
                            basePosition = basePositions["Attacker"][j]
                        drawPlayer(basePosition, name, imageUrl)

                pygame.display.flip()
            def draw352(players, imagesUrls):
                basePositions = {
                    "Goalkeeper": (WIDTH // 2, HEIGHT // 7),
                    "Defender": [(WIDTH // 4, HEIGHT // 3), (WIDTH // 2, HEIGHT // 3), (3 * WIDTH // 4, HEIGHT // 3)],
                    "Midfielder": [(WIDTH // 4, 1.75 * HEIGHT // 3), (1.5 * WIDTH // 4, 1.75 * HEIGHT // 3),
                                       (2 * WIDTH // 4, 1.75 * HEIGHT // 3),
                                       (2.5 * WIDTH // 4, 1.75 * HEIGHT // 3), (3 * WIDTH // 4, 1.75 * HEIGHT // 3)],
                    "Attacker": [(1.5* WIDTH // 4, 5 * HEIGHT // 6), (2.5*WIDTH // 4, 5 * HEIGHT // 6)]
                }

                screen.fill(BLACK)
                screen.blit(fieldImage, (0, 0))

                for i, row in enumerate(players):
                    for j, player in enumerate(row):
                        name = player
                        imageUrl = imagesUrls[i][j]
                        if i == 0:
                            basePosition = basePositions["Goalkeeper"]
                        elif i == 1:
                            basePosition = basePositions["Defender"][j]
                        elif i == 2:
                            basePosition = basePositions["Midfielder"][j]
                        else:
                            basePosition = basePositions["Attacker"][j]
                        drawPlayer(basePosition, name, imageUrl)

                pygame.display.flip()
            def draw433(players, imagesUrls):
                basePositions = {
                    "Goalkeeper": (WIDTH // 2, HEIGHT // 7),
                    "Defender": [(WIDTH // 4, HEIGHT // 3), (1.6 * WIDTH // 4, HEIGHT // 3),
                                (2.4 * WIDTH // 4, HEIGHT // 3), (3 * WIDTH // 4, HEIGHT // 3)],
                    "Midfielder": [(WIDTH // 4, 1.75 * HEIGHT // 3), (2 * WIDTH // 4, 1.75 * HEIGHT // 3),
                                       (3 * WIDTH // 4, 1.75 * HEIGHT // 3)],
                    "Attacker": [(WIDTH // 4, 5 * HEIGHT // 6), (WIDTH // 2, 5 * HEIGHT // 6),
                                  (3 * WIDTH // 4, 5 * HEIGHT // 6)]
                }

                screen.fill(BLACK)
                screen.blit(fieldImage, (0, 0))

                for i, row in enumerate(players):
                    for j, player in enumerate(row):
                        name = player
                        imageUrl = imagesUrls[i][j]
                        if i == 0:
                            basePosition = basePositions["Goalkeeper"]
                        elif i == 1:
                            basePosition = basePositions["Defender"][j]
                        elif i == 2:
                            basePosition = basePositions["Midfielder"][j]
                        else:
                            basePosition = basePositions["Attacker"][j]
                        drawPlayer(basePosition, name, imageUrl)

                pygame.display.flip()
            def draw532(players, imagesUrls):
                basePositions = {
                    "Goalkeeper": (WIDTH // 2, HEIGHT // 7),
                    "Defender": [(WIDTH // 4, HEIGHT // 3), (1.5 * WIDTH // 4, HEIGHT // 3), (2 * WIDTH // 4, HEIGHT // 3),
                                (2.5 * WIDTH // 4, HEIGHT // 3), (3 * WIDTH // 4, HEIGHT // 3)],
                    "Midfielder": [(WIDTH // 4, 1.75 * HEIGHT // 3), (2 * WIDTH // 4, 1.75 * HEIGHT // 3),
                                       (3 * WIDTH // 4, 1.75 * HEIGHT // 3)],
                    "Attacker": [(1.5* WIDTH // 4, 5 * HEIGHT // 6), (2.5*WIDTH // 4, 5 * HEIGHT // 6)]
                }

                screen.fill(BLACK)
                screen.blit(fieldImage, (0, 0))

                for i, row in enumerate(players):
                    for j, player in enumerate(row):
                        name = player
                        imageUrl = imagesUrls[i][j]
                        if i == 0:
                            basePosition = basePositions["Goalkeeper"]
                        elif i == 1:
                            basePosition = basePositions["Defender"][j]
                        elif i == 2:
                            basePosition = basePositions["Midfielder"][j]
                        else:
                            basePosition = basePositions["Attacker"][j]
                        drawPlayer(basePosition, name, imageUrl)

                pygame.display.flip()

            match option:
                case 1:
                    draw343(playerNames, playerPhotos,pointsText,execTimeText)
                case 2:
                    draw352(playerNames, playerPhotos)
                case 3:
                    draw433(playerNames, playerPhotos)
                case 4:
                    draw442(playerNames, playerPhotos)
                case 5:
                    draw451(playerNames, playerPhotos)
                case 6:
                    draw532(playerNames, playerPhotos)
                case 7:
                    draw541(playerNames, playerPhotos)


            pyGameRunning = True
            while pyGameRunning:
                for pyGameEvent in pygame.event.get():
                    if pyGameEvent.type == pygame.QUIT:
                        pyGameRunning = False


            pygame.quit()
            sys.exit()
