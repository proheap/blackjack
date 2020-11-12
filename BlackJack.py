######################################
# BLACKJACK 
# AUTOR: MARTIN MIŠÍK
# DATUM: 27.12.2018
# VERZIA: 2.0
######################################

import pygame, sys, random, time, os
from pygame.locals import *

             #R      G       B
BIELA =      (255,   255,    255)
MODRA =      (0,     128,    255) 
CERVENA =    (255,   0,      0)
SIVA =       (75,    75,     75)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
SIRKA_KARTY = 58
D_TEXT_SUM = (460, 150)
P_TEXT_SUM = (460, 500)

def drawText(text, font, surface, x, y, color):
    textObject = font.render(text, 1, color)
    textRect = textObject.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textObject, textRect)

def startGame():
    pygame.init()
    WindowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('BLACKJACK')
    WindowSurface.fill(MODRA)

    logo = pygame.image.load('assets/logo.png')
    logoRect = logo.get_rect()
    logoRect.center = (640, 180)

    startButton = pygame.image.load('assets/button_play-game.png')
    startButtonRect = startButton.get_rect()
    startButtonRect.center = (640, 350)

    quitButton = pygame.image.load('assets/button_quit-game.png')
    quitButtonRect = quitButton.get_rect()
    quitButtonRect.center = (640, 450)

    WindowSurface.blit(logo, logoRect)
    WindowSurface.blit(startButton, startButtonRect)
    WindowSurface.blit(quitButton, quitButtonRect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(0)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if startButtonRect.collidepoint(event.pos):
                        balicek = vytvorBalicek('assets/karty.txt')
                        dajVklad(100, balicek)
                    if quitButtonRect.collidepoint(event.pos):
                        pygame.quit()
                        os._exit(0)

def vytvorBalicek(menoSuboru):
    subor = open(menoSuboru, 'r')
    balicek = [ln.strip() for ln in subor]
    random.shuffle(balicek)
    return balicek

def rozdajKarty(balicek):
    dealer = []
    hrac = []
    dealer.append(balicek.pop(0))
    dSumStart, pom = zistiHodnoty(dealer)
    hrac.append(balicek.pop(0))   
    dealer.append(balicek.pop(0))
    hrac.append(balicek.pop(0))  

    return dealer, hrac, dSumStart

def dajKartu(ruka, balicek):
    ruka.append(balicek[0])
    balicek.pop(0)

def dajVklad(balance, balicek):
    pygame.init()
    width = 1280;
    height = 720;
    WindowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('BLACKJACK')

    background = pygame.image.load('assets/table.png')
    backgroundRect = background.get_rect()
    backgroundRect.topleft = (0, 0)
    WindowSurface.blit(background, backgroundRect)
    
    menuButton = pygame.image.load('assets/button_main-menu.png')
    menuButtonRect = menuButton.get_rect()
    menuButtonRect.topleft = (80, 10)
    WindowSurface.blit(menuButton, menuButtonRect)

    font = pygame.font.SysFont(None, 30)
    drawText('Balance: ' + str(balance) + '€', font, WindowSurface, 10, 620, BIELA)

    chip5 = pygame.image.load('assets/chip5.png')
    chip5Rect = chip5.get_rect()
    chip5Rect.bottomleft = (10, 700)
    chip10 = pygame.image.load('assets/chip10.png')
    chip10Rect = chip10.get_rect()
    chip10Rect.bottomleft = (70, 700)
    chip20 = pygame.image.load('assets/chip20.png')
    chip20Rect = chip20.get_rect()
    chip20Rect.bottomleft = (130, 700)
    chip50 = pygame.image.load('assets/chip50.png')
    chip50Rect = chip50.get_rect()
    chip50Rect.bottomleft = (190, 700)
    chip100 = pygame.image.load('assets/chip100.png')
    chip100Rect = chip100.get_rect()
    chip100Rect.bottomleft = (250, 700)

    WindowSurface.blit(chip5, chip5Rect)
    WindowSurface.blit(chip10, chip10Rect)
    WindowSurface.blit(chip20, chip20Rect)
    WindowSurface.blit(chip50, chip50Rect)
    WindowSurface.blit(chip100, chip100Rect)
   
    if balance < 5:
        gameOver()
    vlozenyVklad = False

    vklad = 0
    chip = 0
    fontDealer = pygame.font.SysFont(None, 40)
    drawText('PLACE YOUR BET, PLEASE!', fontDealer, WindowSurface, 450, 120, CERVENA)
    pygame.display.update()

    #VLOZENIE VKLADU
    while vlozenyVklad is False:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(0)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if menuButtonRect.collidepoint(event.pos):
                        startGame()

                    if chip5Rect.collidepoint(event.pos):
                        if balance >= 5:
                            vklad = 5
                            balance -= 5
                            vlozenyVklad = True     
                            chip = chip5
                    if chip10Rect.collidepoint(event.pos):
                        if balance >= 10:
                            vklad = 10
                            balance -= 10
                            vlozenyVklad = True
                            chip = chip10
                    if chip20Rect.collidepoint(event.pos):
                        if balance >= 20:
                            vklad = 20
                            balance -= 20
                            vlozenyVklad = True
                            chip = chip20
                    if chip50Rect.collidepoint(event.pos):
                        if balance >= 50:
                            vklad = 50
                            balance -= 50
                            vlozenyVklad = True
                            chip = chip50
                    if chip100Rect.collidepoint(event.pos):
                        if balance >= 100:
                            vklad = 100
                            balance -= 100
                            vlozenyVklad = True
                            chip = chip100

    pygame.display.update()

    #PO VLOZENI VKLADU
    while vlozenyVklad is True:
        if len(balicek) < 25:
            balicek = vytvorBalicek('karty.txt')
        dealerHand, playerHand, dSumStart = rozdajKarty(balicek)
        balance += playHand(vklad, chip, balance, playerHand, dealerHand, dSumStart, balicek)
        pygame.display.update()
        dajVklad(balance, balicek)

def playHand(vklad, chip, balance, playerHand, dealerHand, dSumStart, balicek):
    pygame.init()
    width = 1280;
    height = 720;
    WindowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('BLACKJACK')

    background = pygame.image.load('assets/table.png')
    backgroundRect = background.get_rect()
    backgroundRect.topleft = (0, 0)
    WindowSurface.blit(background, backgroundRect)

    menuButton = pygame.image.load('assets/button_main-menu.png')
    menuButtonRect = menuButton.get_rect()
    menuButtonRect.topleft = (80, 10)
    WindowSurface.blit(menuButton, menuButtonRect)

    fontDealer = pygame.font.SysFont(None, 40)
    font = pygame.font.SysFont(None, 30)
    drawText('Balance: ' + str(balance) + '€', font, WindowSurface, 10, 620, BIELA)

    chip5 = pygame.image.load('assets/chip5.png')
    chip5Rect = chip5.get_rect()
    chip5Rect.bottomleft = (10, 700)
    chip10 = pygame.image.load('assets/chip10.png')
    chip10Rect = chip10.get_rect()
    chip10Rect.bottomleft = (70, 700)
    chip20 = pygame.image.load('assets/chip20.png')
    chip20Rect = chip20.get_rect()
    chip20Rect.bottomleft = (130, 700)
    chip50 = pygame.image.load('assets/chip50.png')
    chip50Rect = chip50.get_rect()
    chip50Rect.bottomleft = (190, 700)
    chip100 = pygame.image.load('assets/chip100.png')
    chip100Rect = chip100.get_rect()
    chip100Rect.bottomleft = (250, 700)

    WindowSurface.blit(chip5, chip5Rect)
    WindowSurface.blit(chip10, chip10Rect)
    WindowSurface.blit(chip20, chip20Rect)
    WindowSurface.blit(chip50, chip50Rect)
    WindowSurface.blit(chip100, chip100Rect)

    chipOnTable = chip.get_rect()
    chipOnTable.center = (640, 464)
    WindowSurface.blit(chip, chipOnTable)

    hitButton = pygame.image.load('assets/button_hit-card.png')
    hitButtonRect = hitButton.get_rect()
    hitButtonRect.bottomright = (1270, 625)
    WindowSurface.blit(hitButton, hitButtonRect)

    standButton = pygame.image.load('assets/button_stand.png')
    standButtonRect = standButton.get_rect()
    standButtonRect.bottomright = (1270, 710)
    WindowSurface.blit(standButton, standButtonRect)

    #VYKRESLENIE ROZDANYCH KARIET
    pCardX = 580
    pCardY = 500
    dCardX = 580
    dCardY = 150
    WindowSurface.blit(pygame.image.load('assets/cards/' + playerHand[0] +  '.png'), (pCardX, pCardY)) 
    pCardX += SIRKA_KARTY
    pygame.display.update()
    WindowSurface.blit(pygame.image.load('assets/cards/' + dealerHand[0] + '.png'), (dCardX, dCardY))
    dCardX += SIRKA_KARTY
    time.sleep(0.5)
    pygame.display.update()
    WindowSurface.blit(pygame.image.load('assets/cards/' + playerHand[1] +  '.png'), (pCardX, pCardY)) 
    time.sleep(0.5)
    pygame.display.update()
    WindowSurface.blit(pygame.image.load('assets/cards/back.png'), (dCardX, dCardY))
    dCard2 = pygame.image.load('assets/cards/' + dealerHand[1] + '.png')
    time.sleep(0.5)

    #VYPISANIE SKORE PO ROZDANI KARIET
    pHardSum, pSoftSum = zistiHodnoty(playerHand)
    if pHardSum > 21:
        pSumText = font.render('PLAYER: ' + str(pSoftSum), False, BIELA)
        pOldSum = pSoftSum
    else:
        pSumText = font.render('PLAYER: ' + str(pHardSum), False, BIELA)
        pOldSum = pHardSum
    dHardSum, dSoftSum = zistiHodnoty(dealerHand)
    dSumText = font.render('DEALER: ' + str(dSumStart), False, BIELA)
    WindowSurface.blit(pSumText, P_TEXT_SUM)
    WindowSurface.blit(dSumText, D_TEXT_SUM)

    #KONTROLA BLACKJACK-OV
    blackjack = False
    doublePrize = False

    if pHardSum == 21:
        fontVklad = pygame.font.SysFont(None, 50)
        drawText('YOU HIT BLACKJACK! CONGRATULATION, YOU WIN!', fontDealer, WindowSurface, 310, 120, CERVENA)
        blackjack = True
        doublePrize = True
    if dHardSum == 21:
        fontVklad = pygame.font.SysFont(None, 50)
        drawText('DEALER HIT BLACKJACK! DEALER WINS!', fontDealer, WindowSurface, 350, 120, CERVENA)
        WindowSurface.blit(dCard2, (dCardX + SIRKA_KARTY, dCardY))
        blackjack = True

    pygame.display.update()

    stand = False
    handDone = False
    dealerBust = False
    playerBust = False
    playerWins = False
    dealerWins = False
    push = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(0)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if menuButtonRect.collidepoint(event.pos):
                        startGame()

                    #TAHANIE KARIET A KONTROLA BUST
                    if hitButtonRect.collidepoint(event.pos) and pSoftSum <= 21 and pHardSum !=21 and stand is False:
                        dajKartu(playerHand, balicek)
                        pCardX += SIRKA_KARTY
                        WindowSurface.blit(pygame.image.load('assets/cards/' + playerHand[-1] + '.png'), (pCardX, pCardY))                                            
                        pSumText = font.render('PLAYER: ' + str(pOldSum), False, SIVA)
                        WindowSurface.blit(pSumText, P_TEXT_SUM)
                        pHardSum, pSoftSum = zistiHodnoty(playerHand)
                        if pHardSum > 21:
                            pSumText = font.render('PLAYER: ' + str(pSoftSum), False, BIELA)
                            pOldSum = pSoftSum
                        else:
                            pSumText = font.render('PLAYER: ' + str(pHardSum), False, BIELA)
                            pOldSum = pHardSum
                        WindowSurface.blit(pSumText, P_TEXT_SUM)
                        if pSoftSum > 21:
                            drawText('YOU BUST! DEALER WINS!', fontDealer, WindowSurface, 450, 120, CERVENA)
                            playerBust = True
                    if standButtonRect.collidepoint(event.pos) and pSoftSum <= 21 and blackjack is False and stand is False:
                        dSumText = font.render('DEALER: ' + str(dSumStart), False, SIVA)
                        WindowSurface.blit(dSumText, D_TEXT_SUM)
                        if dHardSum > 21:
                            dSumText = font.render('DEALER: ' + str(dSoftSum), False, BIELA)
                            dOldSum = dSoftSum
                        else:
                            dSumText = font.render('DEALER: ' + str(dHardSum), False, BIELA)
                            dOldSum = dHardSum
                        WindowSurface.blit(dSumText, D_TEXT_SUM)
                        WindowSurface.blit(dCard2, (dCardX, dCardY))
                        pygame.display.update()
                        stand = True
                        while dSoftSum < 17 and stand is True and handDone is False:
                            time.sleep(0.5)
                            dajKartu(dealerHand, balicek)
                            dHardSum, dSoftSum = zistiHodnoty(dealerHand)
                            dSumText = font.render('DEALER: ' + str(dOldSum), False, SIVA)
                            WindowSurface.blit(dSumText, D_TEXT_SUM)
                            if dHardSum > 21:
                                dSumText = font.render('DEALER: ' + str(dSoftSum), False, BIELA)
                                dOldSum = dSoftSum
                            else:
                                dSumText = font.render('DEALER: ' + str(dHardSum), False, BIELA)
                                dOldSum = dHardSum
                            WindowSurface.blit(dSumText, D_TEXT_SUM)
                            WindowSurface.blit(dCard2, (dCardX, dCardY))
                            dCardX += SIRKA_KARTY
                            WindowSurface.blit(pygame.image.load('assets/cards/' + dealerHand[-1] + '.png'), (dCardX, dCardY))        
                            pygame.display.update()
                            if dSoftSum > 21:
                                drawText('DEALER BUSTS! CONGRATULATION, YOU WIN!', fontDealer, WindowSurface, 345, 120, CERVENA)
                                dealerBust = True 
                        dSumText = font.render('DEALER: ' + str(dSoftSum), False, BIELA)
                        WindowSurface.blit(dSumText, D_TEXT_SUM)

                    #KONTROLA BEZ BUST + VYPISANIE VYHERCU
                    if dHardSum >= 17 and dHardSum <= 21 or dSoftSum >= 17 and dSoftSum <= 21:
                        handDone = True
                    if dealerBust is False and playerBust is False and stand is True and blackjack is False and handDone is True:
                        if pHardSum <= 21 and dHardSum <= 21:
                            if pHardSum > dHardSum:
                                drawText('CONGRATULATION, YOU WIN!', fontDealer, WindowSurface, 420, 120, CERVENA)
                                playerWins = True
                            if pHardSum < dHardSum:
                                drawText('DEALER WINS!', fontDealer, WindowSurface, 535, 120, CERVENA)
                                dealerWins = True
                            if pHardSum == dHardSum:
                                drawText('PUSH!', fontDealer, WindowSurface, 600, 120, CERVENA)
                                push = True
                        elif pHardSum > 21 and dHardSum <= 21:
                            if pSoftSum > dHardSum:
                                drawText('CONGRATULATION, YOU WIN!', fontDealer, WindowSurface, 420, 120, CERVENA)
                                playerWins = True
                            if pSoftSum < dHardSum:
                                drawText('DEALER WINS!', fontDealer, WindowSurface, 535, 120, CERVENA)
                                dealerWins = True
                            if pSoftSum == dHardSum:
                                drawText('PUSH!', fontDealer, WindowSurface, 600, 120, CERVENA)
                                push = True
                        elif pHardSum <= 21 and dHardSum > 21:
                            if pHardSum > dSoftSum:
                                drawText('CONGRATULATION, YOU WIN!', fontDealer, WindowSurface, 420, 120, CERVENA)
                                playerWins = True
                            if pHardSum < dSoftSum:
                                drawText('DEALER WINS!', fontDealer, WindowSurface, 535, 120, CERVENA)
                                dealerWins = True
                            if pHardSum == dSoftSum:
                                drawText('PUSH!', fontDealer, WindowSurface, 600, 120, CERVENA)
                                push = True
                        elif pHardSum > 21 and dHardSum > 21:
                            if pSoftSum > dSoftSum:
                                drawText('CONGRATULATION, YOU WIN!', fontDealer, WindowSurface, 420, 120, CERVENA)
                                playerWins = True
                            if pSoftSum < dSoftSum:
                                drawText('DEALER WINS!', fontDealer, WindowSurface, 535, 120, CERVENA)
                                dealerWins = True
                            if pSoftSum == dSoftSum:
                                drawText('PUSH!', fontDealer, WindowSurface, 600, 120, CERVENA)
                                push = True
                    pygame.display.update() 
            
            ## VRATENIE VYHRY
            if blackjack is True:
                time.sleep(5)
                if doublePrize is True:
                    return vklad * 3
                else:
                    return 0
            if playerBust is True or dealerWins is True:
                time.sleep(3)
                return 0;
            if dealerBust is True or playerWins is True:
                time.sleep(3)
                return vklad * 2
            if push is True:
                time.sleep(3)
                return vklad

def zistiHodnoty(karty):
    hardSum = 0
    softSum = 0

    for karta in karty:
        if karta[-1].isdigit() and int(karta[-1]) != 10:
            hardSum += int(karta[-1])
            softSum += int(karta[-1])
        if karta[-1] in 'JQK' or karta[-2:].isdigit():
            hardSum += 10
            softSum += 10
        if karta[-1] == 'A':
            hardSum += 11
            softSum += 1
    if softSum == 2:
        hardSum += 12

    return hardSum, softSum

def gameOver():
    pygame.init()
    width = 1280;
    height = 720;
    WindowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('BLACKJACK')
    WindowSurface.fill(MODRA)

    gameOver = pygame.image.load('assets/game-over.png')
    gameOverRect = gameOver.get_rect()
    gameOverRect.center = (640, 360)

    menuButton = pygame.image.load('assets/button_main-menu.png')
    menuButtonRect = menuButton.get_rect()
    menuButtonRect.center = (640, 600)

    WindowSurface.blit(gameOver, gameOverRect)
    WindowSurface.blit(menuButton, menuButtonRect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(0)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if menuButtonRect.collidepoint(event.pos):
                        startGame()

if __name__ == "__main__":
    startGame()