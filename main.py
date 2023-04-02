import keyboard
import pygame
import random


from pygame import mixer


pygame.init()
width, height = 900, 600
screen = pygame.display.set_mode((width, height))
mainscreen=pygame.image.load('assets/main.jpg')
mainscreen = pygame.transform.scale(mainscreen,(width, height))
display_bar = pygame.image.load('assets/dialoguebox.png')
display_bar = pygame.transform.scale(display_bar, (1000, 200))
display_barX = 30
display_barY = 400

myfont = pygame.font.Font('assets/Cardinal.ttf', 18)
luck = random.randint(0, 10)
if luck<5:
    textsurface = myfont.render("You are Geralt of Rivia. The famed White Haired Hunter. Roaming about the land you heard of the \n"
    "castle of imilrith who is stealing  gold and valuables from the locals. You decide to pay him a \n"
    " visit. You look to your horse to retrieve your weapons. You take out your sword that looks \n"
    "quiet beaten up", False, (255, 255, 255))

if luck<7:
    textsurface = myfont.render("You are Geralt of Rivia. The famed White Haired Hunter. Roaming about the land you heard of the \n" \
    "castle of imilrith who is stealing  gold and valuable from the locals. You decide to pay him a \n"
    " visit. You look to your horse to retrieve your weapons. You take out your sword that looks \n"
    "newly polished", False, (255, 255, 255))
if luck>7:
    textsurface = myfont.render("You are Geralt of Rivia. The famed White Haired Hunter. Roaming about the land you heard of the \n"
    "castle of imilrith who is stealing  gold and valuable from the locals. You decide to pay him a \n"
    " visit. You look to your horse to retrieve your weapons. You take out your sharp silver sword  \n" , False, (255, 255, 255))


mixer.music.load("assets/06 Last Battle.mp3")
mixer.music.play(-1)

pygame.display.set_caption("The Geralt")
icon=pygame.image.load('assets/spears.png')
pygame.display.set_icon(icon)




def level1():
    # 1screen
    bg = pygame.image.load('assets/images.jpg')
    bg = pygame.transform.scale(bg, (width, height))
    display_bar = pygame.image.load('assets/newdp_bg.jpeg')
    display_bar = pygame.transform.scale(display_bar, (1000, 100))
    playerImg1 = pygame.image.load('assets/geralt1.png')
    playerImg1 = pygame.transform.scale(playerImg1, (300, 300))
    stamina = 10
    enemy_hp = 100
    player_hp = 110
    staminat = pygame.font.Font('assets/Cardinal.ttf', 20)
    staminatext = staminat.render(
        "Your Stamina is "+ str(stamina) +" and HP is "+ str(player_hp)+ " while enemy HP is "+ str(enemy_hp) +" .Press Spacebar to Continue!", False, (210,105,30))

    screen.blit(bg, (0, 0))
    screen.blit(display_bar, (-20, 500))
    screen.blit(staminatext, (150, 520))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
            pygame.quit()
        if keyboard.is_pressed('SPACE'):
            print("Tapped", stage)

            if luck > 7:
                print(luck)
                critical_dmg = random.uniform(1.4, 1.7)
            else:
                print(luck)
                critical_dmg = random.uniform(1.0, 1.5)
            strength_bsd_dmg = strength * 10
            print(strength_bsd_dmg)
            total_dmg = round((weapon + (round((strength_bsd_dmg / 100) * weapon))) * critical_dmg)
            print(total_dmg)
            while player_hp > 0 and enemy_hp > 0:
                print(player_hp)
                print(enemy_hp)
                attack_typ = pygame.font.Font('assets/Cardinal.ttf', 18)
                print("Rendering")
                attack_type = attack_typ.render(
                    "Enter attack type \n Enter 1 for light Attack (2 stamina) \n Enter 2 for heavy attack (4 Stamina)\n Enter 3 to rest and gain stamina(+2 stamina )\n" + str(
                        player_hp), False, (210, 105, 30))
                screen.blit(bg, (0, 0))
                screen.blit(display_bar, (-20, 500))
                screen.blit(attack_type, (100, 535))
                pygame.display.update()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit();  # sys.exit() if sys is imported
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_1 and stamina >= 2:
                                enemy_hp = enemy_hp - (total_dmg) - 5
                                stamina = stamina - 2
                                player_hp = player_hp - enemy_dmg
                                bg = pygame.image.load('assets/image01.jpg')
                                bg = pygame.transform.scale(bg, (width, height))
                                playerImg1 = pygame.image.load('assets/witcher1.png')
                                playerImg1 = pygame.transform.scale(playerImg1, (300, 300))

                                # enemy1update
                                enemyImg1 = pygame.image.load('assets/lashen2.png')
                                enemyImg1 = pygame.transform.scale(enemyImg1, (200, 200))
                                staminat = pygame.font.Font('assets/Cardinal.ttf', 20)
                                staminatext = staminat.render(
                                    "Your Stamina is " + str(stamina) + " and HP is " + str(
                                        player_hp) + " while enemy HP is " + str(
                                        enemy_hp) + " .Press keys to fight again!", False, (210, 105, 30))

                                screen.blit(bg, (0, 0))
                                screen.blit(display_bar, (-20, 500))
                                screen.blit(playerImg1, (-40, 400))
                                screen.blit(staminatext, (150, 520))
                                # screen.blit(enemyImg1, (690, 30))
                                pygame.display.update()
                                print("Light Attack initiated")
                            elif event.key == pygame.K_2 and stamina >= 4:
                                print("Heavy Attack initiated")
                                enemy_hp = enemy_hp - (total_dmg) - 5
                                stamina = stamina - 4
                                player_hp = player_hp - enemy_dmg
                                bg = pygame.image.load('assets/image02.jpg')
                                bg = pygame.transform.scale(bg, (width, height))
                                staminat = pygame.font.Font('assets/Cardinal.ttf', 20)
                                staminatext = staminat.render(
                                    "Your Stamina is " + str(stamina) + " and HP is " + str(
                                        player_hp) + " while enemy HP is " + str(
                                        enemy_hp) + " .Press keys to fight again!", False, (210, 105, 30))

                                screen.blit(bg, (0, 0))
                                screen.blit(display_bar, (-20, 500))
                                screen.blit(playerImg1, (-40, 400))
                                screen.blit(staminatext, (150, 520))
                                # screen.blit(enemyImg1, (690, 30))
                                pygame.display.update()

                            else:
                                print("You Do Not Attack")
                                stamina = stamina + 2
                                player_hp = player_hp - enemy_dmg + random.randint(3, 8)
                                bg = pygame.image.load('assets/fight03.png')
                                bg = pygame.transform.scale(bg, (width, height))
                                staminat = pygame.font.Font('assets/Cardinal.ttf', 20)
                                staminatext = staminat.render(
                                    "Your Stamina is " + str(stamina) + " and HP is " + str(
                                        player_hp) + " while enemy HP is " + str(
                                        enemy_hp) + " .Press keys to fight again!", False, (210, 105, 30))
                                screen.blit(bg, (0, 0))
                                screen.blit(display_bar, (-20, 500))
                                screen.blit(playerImg1, (-40, 400))
                                screen.blit(staminatext, (150, 520))
                                # screen.blit(enemyImg1, (690, 30))
                                pygame.display.update()
                            if enemy_hp <=0 and player_hp >0:
                                print('enemy dead')
                                level2()
                                break


                            if player_hp <= 0:
                                print('player dead')
                                


def level2():
    print('Reached level 2')
    # 1screen
    mixer.music.load("assets/castle_ambience.wav")
    mixer.music.play(-1)
    bg = pygame.image.load('assets/castle2.jpg')
    bg = pygame.transform.scale(bg, (900, 500))
    display_bar = pygame.image.load('assets/newdp_bg.jpeg')
    display_bar = pygame.transform.scale(display_bar, (1000, 100))
    myfont = pygame.font.Font('assets/Cardinal.ttf', 20)
    luck = random.randint(0, 10)
    textsurface = myfont.render(
            "Your journey continues...... Your stamina nd HP has been filled again. Fight your next enemy to reach your final destination.", False, (210, 105, 30))
    # playerupdate
    playerImg1 = pygame.image.load('assets/geralt1.png')
    playerImg1 = pygame.transform.scale(playerImg1, (300, 300))
    print("Before defining lvl2 char")
    stamina = 10
    enemy_hp = 100
    player_hp = 110
    screen.blit(bg, (0, 0))
    screen.blit(display_bar, (-20, 500))
    screen.blit(textsurface, (120, 520))
    pygame.display.update()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if keyboard.is_pressed('SPACE'):
            print("Tapped lvl2", stage)

            if luck > 7:
                print(luck,"luck is defined >7 lvl2")
                critical_dmg = random.uniform(1.4, 1.7)
            else:
                print(luck, "luck is defined else")
                critical_dmg = random.uniform(1.0, 1.5)
            strength_bsd_dmg = strength * 10
            print(strength_bsd_dmg)
            total_dmg = round((weapon + (round((strength_bsd_dmg / 100) * weapon))) * critical_dmg)
            print(total_dmg)
            while player_hp > 0 and enemy_hp > 0:
                attack_typ = pygame.font.Font('assets/Cardinal.ttf', 18)
                print("Rendering")
                attack_type = attack_typ.render(
                    "Enter attack type \n Enter 1 for light Attack (2 stamina) \n Enter 2 for heavy attack (4 Stamina)\n Enter 3 to rest and gain stamina(+2 stamina )\n" + str(
                        player_hp), False, (210, 105, 30))
                screen.blit(bg, (0, 0))
                screen.blit(display_bar, (-20, 500))
                screen.blit(attack_type, (120, 535))
                pygame.display.update()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit();  # sys.exit() if sys is imported
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_1 and stamina > 1:
                                enemy_hp = enemy_hp - (total_dmg) - 5
                                stamina = stamina - 2
                                player_hp = player_hp - enemy_dmg
                                bg = pygame.image.load('assets/image02.jpg')
                                bg = pygame.transform.scale(bg, (width, height))
                                playerImg1 = pygame.image.load('assets/witcher1.png')
                                playerImg1 = pygame.transform.scale(playerImg1, (300, 300))

                                # enemy1update
                                enemyImg1 = pygame.image.load('assets/lashen2.png')
                                enemyImg1 = pygame.transform.scale(enemyImg1, (200, 200))
                                staminat = pygame.font.Font('assets/Cardinal.ttf', 20)
                                staminatext = staminat.render(
                                    "Your Stamina is " + str(stamina) + " and HP is " + str(
                                        player_hp) + " while enemy HP is " + str(
                                        enemy_hp) + " .Press keys to fight again!", False, (210, 105, 30))

                                screen.blit(bg, (0, 0))
                                screen.blit(display_bar, (-20, 500))
                                screen.blit(playerImg1, (-40, 400))
                                screen.blit(staminatext, (150, 520))
                                # screen.blit(enemyImg1, (690, 30))
                                pygame.display.update()
                                print("Light Attack initiated")
                            elif event.key == pygame.K_2 and stamina >= 4:
                                print("Heavy Attack initiated")
                                enemy_hp = enemy_hp - (total_dmg) - 5
                                stamina = stamina - 4
                                player_hp = player_hp - enemy_dmg
                                bg = pygame.image.load('assets/fight03.png')
                                bg = pygame.transform.scale(bg, (width, height))
                                staminat = pygame.font.Font('assets/Cardinal.ttf', 20)
                                staminatext = staminat.render(
                                    "Your Stamina is " + str(stamina) + " and HP is " + str(
                                        player_hp) + " while enemy HP is " + str(
                                        enemy_hp) + " .Press keys to fight again!", False, (210, 105, 30))

                                screen.blit(bg, (0, 0))
                                screen.blit(display_bar, (-20, 500))
                                screen.blit(playerImg1, (-40, 400))
                                screen.blit(staminatext, (150, 520))
                                # screen.blit(enemyImg1, (690, 30))
                                pygame.display.update()

                            else:
                                print("You Do Not Attack")
                                stamina = stamina + 2
                                player_hp = player_hp - enemy_dmg + random.randint(3, 8)
                                staminat = pygame.font.Font('assets/Cardinal.ttf', 20)
                                staminatext = staminat.render(
                                    "Your Stamina is " + str(stamina) + " and HP is " + str(
                                        player_hp) + " while enemy HP is " + str(
                                        enemy_hp) + " .Press keys to fight again!", False, (210, 105, 30))
                                screen.blit(bg, (0, 0))
                                screen.blit(display_bar, (-20, 500))
                                screen.blit(playerImg1, (-40, 400))
                                screen.blit(staminatext, (150, 520))
                                # screen.blit(enemyImg1, (690, 30))
                                pygame.display.update()
                            if enemy_hp <= 0 and player_hp > 0:
                                print('enemy dead')
                                break
                            if player_hp <= 0:
                                print('player dead')
                                bg = pygame.image.load('assets/dead.jpeg')
                                bg = pygame.transform.scale(bg, (width, height))
                                screen.blit(bg, (0, 0))
                                pygame.display.update()



def level3():
    # 1screen
    bg = pygame.image.load('assets/images.jpg')
    bg = pygame.transform.scale(bg, (width, height))
    display_bar = pygame.image.load('assets/newdp_bg.jpeg')
    display_bar = pygame.transform.scale(display_bar, (1000, 100))
    # playerupdate
    playerImg1 = pygame.image.load('assets/geralt1.png')
    playerImg1 = pygame.transform.scale(playerImg1, (300, 300))

    # enemy1update
    enemyImg1 = pygame.image.load('assets/lashen1.png')
    enemyImg1 = pygame.transform.scale(enemyImg1, (200, 200))
    stamina = 10
    enemy_hp = 100
    player_hp = 110
    staminat = pygame.font.Font('assets/Cardinal.ttf', 20)
    staminatext = staminat.render(
        "Your Stamina is " + str(stamina) + " and HP is " + str(player_hp) + " while enemy HP is " + str(
            enemy_hp) + " .Press Spacebar to Continue!", False, (210, 105, 30))

    screen.blit(bg, (0, 0))
    screen.blit(display_bar, (-20, 500))
    screen.blit(staminatext, (150, 520))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if keyboard.is_pressed('SPACE'):
            print("Tapped", stage)

            if luck > 7:
                print(luck)
                critical_dmg = random.uniform(1.4, 1.7)
            else:
                print(luck)
                critical_dmg = random.uniform(1.0, 1.5)
            strength_bsd_dmg = strength * 10
            print(strength_bsd_dmg)
            total_dmg = round((weapon + (round((strength_bsd_dmg / 100) * weapon))) * critical_dmg)
            print(total_dmg)
            while player_hp > 0 and enemy_hp > 0:
                attack_typ = pygame.font.Font('assets/Cardinal.ttf', 18)
                print("Rendering")
                attack_type = attack_typ.render(
                    "Enter attack type \n Enter 1 for light Attack (2 stamina) \n Enter 2 for heavy attack (4 Stamina)\n Enter 3 to rest and gain stamina(+2 stamina )\n" + str(
                        player_hp), False, (210, 105, 30))
                screen.blit(bg, (0, 0))
                screen.blit(display_bar, (-20, 500))
                screen.blit(attack_type, (120, 535))
                pygame.display.update()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit();  # sys.exit() if sys is imported
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_1 and stamina > 1:
                                enemy_hp = enemy_hp - (total_dmg) - 5
                                stamina = stamina - 2
                                player_hp = player_hp - enemy_dmg
                                bg = pygame.image.load('assets/image02.jpg')
                                bg = pygame.transform.scale(bg, (width, height))
                                playerImg1 = pygame.image.load('assets/witcher1.png')
                                playerImg1 = pygame.transform.scale(playerImg1, (300, 300))

                                # enemy1update
                                enemyImg1 = pygame.image.load('assets/lashen2.png')
                                enemyImg1 = pygame.transform.scale(enemyImg1, (200, 200))
                                staminat = pygame.font.Font('assets/Cardinal.ttf', 20)
                                staminatext = staminat.render(
                                    "Your Stamina is " + str(stamina) + " and HP is " + str(
                                        player_hp) + " while enemy HP is " + str(
                                        enemy_hp) + " .Press keys to fight again!", False, (210, 105, 30))

                                screen.blit(bg, (0, 0))
                                screen.blit(display_bar, (-20, 500))
                                screen.blit(playerImg1, (-40, 400))
                                screen.blit(staminatext, (150, 520))
                                # screen.blit(enemyImg1, (690, 30))
                                pygame.display.update()
                                print("Light Attack initiated")
                            elif event.key == pygame.K_2 and stamina >= 4:
                                print("Heavy Attack initiated")
                                enemy_hp = enemy_hp - (total_dmg) - 5
                                stamina = stamina - 4
                                player_hp = player_hp - enemy_dmg
                                staminat = pygame.font.Font('assets/Cardinal.ttf', 20)
                                staminatext = staminat.render(
                                    "Your Stamina is " + str(stamina) + " and HP is " + str(
                                        player_hp) + " while enemy HP is " + str(
                                        enemy_hp) + " .Press keys to fight again!", False, (210, 105, 30))

                                screen.blit(bg, (0, 0))
                                screen.blit(display_bar, (-20, 500))
                                screen.blit(playerImg1, (-40, 400))
                                screen.blit(staminatext, (150, 520))
                                # screen.blit(enemyImg1, (690, 30))
                                pygame.display.update()

                            else:
                                print("You Do Not Attack")
                                stamina = stamina + 2
                                player_hp = player_hp - enemy_dmg + random.randint(3, 8)
                                staminat = pygame.font.Font('assets/Cardinal.ttf', 20)
                                staminatext = staminat.render(
                                    "Your Stamina is " + str(stamina) + " and HP is " + str(
                                        player_hp) + " while enemy HP is " + str(
                                        enemy_hp) + " .Press keys to fight again!", False, (210, 105, 30))
                                screen.blit(bg, (0, 0))
                                screen.blit(display_bar, (-20, 500))
                                screen.blit(playerImg1, (-40, 400))
                                screen.blit(staminatext, (150, 520))
                                # screen.blit(enemyImg1, (690, 30))
                                pygame.display.update()
                            if enemy_hp <= 0 and player_hp > 0:
                                print('enemy dead')
                                level2()
                            if player_hp <= 0:
                                print('player dead')
                                bg = pygame.image.load('assets/dead.jpeg')
                                bg = pygame.transform.scale(bg, (width, height))
                                screen.blit(bg, (0, 0))
                                pygame.display.update()




running = True
stage = 1
while running:
    print(stage)
    if stage == 1:

        screen.blit(mainscreen,(0, 0))
        screen.blit(display_bar, (-20, 500))
        screen.blit(textsurface, (5, 550))
    elif stage == 3:
        strength = 5
        weapon = 10
        enemy_dmg = 14
        print(stage,"446")
        level1()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if keyboard.is_pressed('SPACE'):
                print("Mewo", stage)
                stage += 1


    pygame.display.update()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
            pygame.quit()
        if keyboard.is_pressed('SPACE'):
            print("Mewo", stage)
            stage += 1






#luck = random.randint(5,10)
# #You are Geralt of Rivia. The famed White Haired Hunter. Roaming about the land you heard of the castle of
#imilrith who is stealing  gold and valueable from the locals. You decide to pay him a visit. You look to your horse
#to retrive your weapons
#if luck <7 :
#you find a mace
#if luck >8 but <9:
#You find your sword which had been damaged in the previous battle
#if luck>9:
#You spot a chest out of the corner of your eye and find a silver sword inside.
#As you move further into the jungle you hear a noise.
#"A Leshen" you say under your breath
