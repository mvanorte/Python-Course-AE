""" Background planets"""
import numpy as np
import pygame as pg
import os
import math

from pygame import font
#import  movement_function
#import force_function
pg.init()
player=[450, 300]
position_new_planet=[]



# constants:
G = 6.67*10**(-11)
M = 6*10**3  # kg
m_player = 65  # kg
m_newplanet = 6*10**17 # kg
k = 0

positions = [[450, 600],
             [450, 0],
             [0, 300],
             [900, 300]]  # the position of the planets
distance = np.zeros((4, 2))  # distance between the planets and the player
forces = np.zeros((4, 2))  # the force that acts on the player due to the planet


# calculate the forces n x and y direction

mx=-1 
my=-1

#couldn't figure out how to block positions of planets and obstacles for mouse command so game is in 3D
#forbidden_positions=[[list(range(0, 100)), list(range(250, 350))], [list(range(400, 500)), list(range(550, 650))], [list(range(400, 500)), list(range(0, 100))], [list(range(825, 925)), list(range(250, 350))], [list(range(675, 725)), list(range(175, 225))], [list(range(675, 775)), list(range(195, 225))], [list(range(650, 700)), list(range(155, 205))]]
#keys=pg.key.get_pressed()







# game screen set up
scr=pg.display.set_mode((1000, 700))
background=pg.image.load(r"background2.jpg")
mercury=pg.image.load(r"mercury-removebg-preview.png")
mercury_scaled=pg.transform.scale(mercury, (100, 100))
mars=pg.image.load(r"mars-no_back-removebg-preview.png")
mars_scaled=pg.transform.scale(mars, (100, 100))
earth=pg.image.load(r"The_Earth_seen_from_Apollo_17-removebg-preview.png")
earth_scaled=pg.transform.scale(earth, (100, 100))
venus=pg.image.load(r"venus_no_back-removebg-preview.png")
venus_scaled=pg.transform.scale(venus, (125, 100))
astronaut=pg.image.load(r"astronaut-removebg-preview.png")
astronaut_scaled=pg.transform.scale(astronaut, (100, 100))
prize=pg.image.load(r"Raspberry_Pi_4_Model_B_-_Side-removebg-preview.png")
prize_scaled=pg.transform.scale(prize, (75, 75))
white = (255,255,255)
red=(255, 0, 0)
obstacle=pg.Rect(700, 200, 75, 50)
# obstacle2=pg.Rect(725, 220, 50, 25)
# obstacle3=pg.Rect(675, 180, 25, 50)
pg.display.set_caption("Gravity Master")

scr.fill((0, 0, 0))
# scr.blit(background, (0,0))

#start screen

#display_surface = pg.display.set_mode((450, 300))
font=pg.font.Font(r"AUTOMANI.ttf",30)
text = font.render('Press Enter to Play', True, (255, 255, 255))
textRect = text.get_rect()
playing=False
# set the center of the rectangular object.
textRect.center = (300, 200)
scr.blit(text, textRect.center)



#if playing==True:
    # pg.draw.rect(scr, white, obstacle)
    # pg.draw.rect(scr, white, obstacle2)
    # pg.draw.rect(scr, white, obstacle3)
    # scr.blit(mercury_scaled, (450, 600))
    # scr.blit(mars_scaled, (450, 0))
    # scr.blit(earth_scaled, (0, 300))
    # scr.blit(venus_scaled, (875, 300))
    # scr.blit(astronaut_scaled, player)
    # scr.blit(prize_scaled, (875, 0))

    # pg.display.flip()

#game loop


mouse=pg.mouse.get_pressed()
running=True
while running:
    #force_act=force_function.force(positions, distance, forces, position_astronaut)
    #movement=movement_function.movement(force_act, position_astronaut)
    for i in range(np.shape(positions)[0]):
        for j in range(np.shape(positions)[1]):
            distance[i][j] = positions[i][j] - player[j]
            if distance[i][j] != 0:  # To avoid dividing by zero
                if i < 4:
                    forces[i][j] = G*M*m_player/(distance[i][j]**2)
                else:
                    forces[i][j] = G * m_newplanet * m_player / (distance[i][j] ** 2)

            if j == 0 and distance[i][j] < 0:  # to check a negative force in the x direction
                forces[i][j] = -forces[i][j]

            if j == 1 and distance[i][j] > 0:
                forces[i][j] = -forces[i][j]

    #print("All the forces acting are: ", forces)
    force_sum = np.sum(forces, axis=0)
    # force_sum = np.round(force_sum, 7)
    #print("The sum of the forces is: ", force_sum)
    #print("The distances are: ", distance)

    # Adding the movement which depends on the sum of forces:
    if position_new_planet != []:
        totalforce = math.sqrt(force_sum[1]**2 + force_sum[0]**2)
        x_step = 0.4*(abs(force_sum[0])/totalforce)
        y_step = 0.4*(abs(force_sum[1])/totalforce)
    prize = [875, 0]

    click = True

    while click:
        # In case the player is going to move in the x and y direction:

        if force_sum[0] > 0 and force_sum[1] > 0: #  and player[0]>0 and player[0]<1000 and player[1]>0 and player[1]<700: #added conditions to keep him inside the screen
            player = [player[0]+x_step, player[1]-y_step]
            # display the player with its new position in pygame

        elif force_sum[0] < 0 and force_sum[1] < 0: # and player[0]>0 and player[0]<1000 and player[1]>0 and player[1]<700:
            player = [player[0] - x_step, player[1] + y_step]
            # display the player with its new position in pygame

        elif force_sum[0] > 0 and force_sum[1] < 0: # and player[0]>0 and player[0]<1000 and player[1]>0 and player[1]<700:
            player = [player[0] + x_step, player[1] + y_step]
            # display the player with its new position in pygame

        elif force_sum[0] < 0 and force_sum[1] > 0: # and player[0]>0 and player[0]<1000 and player[1]>0 and player[1]<700:
            player = [player[0] - x_step, player[1] - y_step]
                # display the player with its new position in pygame

        # In case the player is going to move only in the x direction:
        if force_sum[0] != 0 and force_sum[1] == 0: # and player[0]>0 and player[0]<1000:
            #while click:
            if force_sum[0] > 0:
                player = [player[0] + x_step, player[1]]
                # display the player with its new position in pygame

            elif force_sum[0] < 0:
                player = [player[0] - x_step, player[1]]
                # display the player with its new position in pygame

        # In case the player is going to move only in the y direction:
        if force_sum[0] == 0 and force_sum[1] != 0: #  and player[1]>0 and player[1]<700:
            #while click:
            if force_sum[0] > 0:
                player = [player[0], player[1] + y_step]
                # display the player with its new position in pygame

            elif force_sum[0] < 0:
                player = [player[0], player[1] - y_step]
                # display the player with its new position in pygame

        print("The new position of the player is: ", player)

        scr.blit(astronaut_scaled, player)
        pg.display.flip()
        # add new planet
        if mx != -1 and my != -1:  # and [mx, my] not in forbidden_positions:

            pg.draw.circle(scr, red, (mx, my), 10)

            # pg.draw.circle(scr, red, position_new_planet[0], position_new_planet[1], 10)

        # input
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key==pg.K_ESCAPE):
                pg.quit()
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                mx, my = event.pos
                position_new_planet=[mx, my]
                if k ==0:
                    positions.append([0, 0])
                    k += 1
                positions[4][0] = position_new_planet[0]
                positions[4][1] = position_new_planet[1]
                distance = np.zeros((np.shape(positions)[0], 2))
                forces = np.zeros((np.shape(positions)[0], 2))
                click = False
            elif event.type == pg.KEYDOWN and event.key==pg.K_RETURN :
                playing=True
                
                scr.fill((0, 0, 0))
                pg.display.flip()
                pg.draw.rect(scr, white, obstacle)
                # pg.draw.rect(scr, white, obstacle2)
                # pg.draw.rect(scr, white, obstacle3)
                scr.blit(mercury_scaled, (450, 600))
                scr.blit(mars_scaled, (450, 0))
                scr.blit(earth_scaled, (0, 300))
                scr.blit(venus_scaled, (875, 300))
                scr.blit(astronaut_scaled, player)
                scr.blit(prize_scaled, (875, 0))

                pg.display.flip()
        pg.display.flip()

            # If the user clicks then the coordinates of the new planet has to appended to the array positions and call the function force
    print(obstacle.collidepoint(player))
    if player[0]>837 and player[1]<75:
        scr.fill((0, 0, 0))
        pg.display.flip()
        text2 = font.render('You won', True, (255, 255, 255))
        scr.blit(text2, (450, 300))
        pg.display.flip()
        pg.time.wait(1000)
        running=False
    # elif (player[0] in range(600, 750) and player[1] in range(175, 250)) or (player[0] in range(675, 775) and player[1] in range(195, 245)) or (player[0] in range(650, 700) and player[1] in range(130, 230)):
    #     #click=False
    #     scr.fill((0, 0, 0))
    #     pg.display.flip()
    #     text2 = font.render('You lost', True, (255, 255, 255))
    #     scr.blit(text2, (450, 300))
    #     pg.display.flip()
    #     pg.time.wait(1000)
    #     running=False
    elif player[0] > 1020 or player[1] > 720 or player[0] < -20 or player[1] < -20:
        scr.fill((0, 0, 0))
        pg.display.flip()
        text2 = font.render('You lost', True, (255, 255, 255))
        scr.blit(text2, (450, 300))
        pg.display.flip()
        pg.time.wait(1000)
        running = False

    elif player[0] > 650 and player[0] < 750 and player[1] < 225 and player[1] > 175:
        scr.fill((0, 0, 0))
        pg.display.flip()
        text2 = font.render('You lost', True, (255, 255, 255))
        scr.blit(text2, (450, 300))
        pg.display.flip()
        pg.time.wait(1000)
        running = False
    # elif obstacle.collidepoint(player) or obstacle2.collidepoint(player) or obstacle3.collidepoint(player):
    #     scr.fill((0, 0, 0))
    #     pg.display.flip()
    #     text2 = font.render('You lost', True, (255, 255, 255))
    #     scr.blit(text2, (450, 300))
    #     pg.display.flip()
    #     pg.time.wait(1000)
    #     running=False

    # for event in pg.event.get():
    #     if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
    #         pg.quit()
    #         running = False
    
    #     elif event.type == pg.KEYDOWN and event.key==pg.K_SPACE :
    #         playing=True
    #         print("Starting")
    #         scr.fill(255, 255, 255)
    #         pg.display.flip()
      
    #pg.event.pump()
    pg.display.flip()
pg.time.wait(1100)
for event in pg.event.get():
    if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:

        pg.quit()
    
