#pip install pygame

import pygame
from pygame.locals import *
import random
import time

pygame.init()
clock = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont("MS Comic Sans", 30)
myfont2 = pygame.font.SysFont("MS Comic Sans", 90)


window_width = 800
window_height = 600
points = 0
level = 1
player_width = 100
player_height = 100
ring_width = 100
ring_height = 100
rice_width = 100
rice_height = 100

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Retro Wedding Game")
pygame.display.set_icon(pygame.image.load('images/ring_small.jpg'))

RED, GREEN, BLUE, WHITE, BLACK = (255,0,0), (0,255,0), (0,0,255), (255,255,255), (0,0,0)

bird_img = pygame.image.load("images/raven.png")
bird_img = pygame.transform.scale(bird_img, (ring_height, ring_width))
player_img = pygame.image.load("images/bride.png")
player_img = pygame.transform.scale(player_img, (player_width, player_height))
player_point_img = pygame.image.load("images/brideflower.png")
player_point_img = pygame.transform.scale(player_point_img, (player_width, player_height))
ring_img = pygame.image.load("images/ring.png")
ring_img = pygame.transform.scale(ring_img, (ring_width, ring_height))
bg_img = pygame.image.load("images/curtain-enface.jpg")
bg_img = pygame.transform.scale(bg_img, (window_width, window_height))
wedding_blame_img = pygame.image.load("images/brideraven.png")
wedding_blame_img = pygame.transform.scale(wedding_blame_img, (player_width, player_height))
win_img = pygame.image.load("images/hearts.png")
rice_img = pygame.image.load("images/rice.png")
rice_img = pygame.transform.scale(rice_img, (rice_width, rice_height))

player = pygame.Rect(250,500,player_width,player_height)
player_point = pygame.Rect(250,500,player_width,player_height)
player_blame = pygame.Rect(250,500,player_width,player_height)
pygame.draw.rect(window, RED, player)

velocity = 40

rings = []
birds = []
riceA = []
win_text = myfont2.render("YOU WON!!!", False, RED)
while True:
    window.blit(bg_img, (0,0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s] or keys[pygame.K_DOWN] and player.bottom < 600:
        player.bottom += velocity
    if keys[pygame.K_w] or keys[pygame.K_UP] and player.top > 0:
        player.top -= velocity
    if keys[pygame.K_a] or keys[pygame.K_LEFT] and player.left > 0:
        player.left -= velocity
    if keys[pygame.K_d] or keys[pygame.K_RIGHT] and player.right <800:
        player.right += velocity
    window.blit(player_img, player)
    x = random.randint(0,100)
    if points < 10:
        if x >= 99:
            new_ring = pygame.Rect(random.randint(10,window_width-10),20,ring_width,ring_height)
            rings.append(new_ring)
    if points >= 10 and points < 50:
        level = 2
        if x >= 90 :
            new_ring = pygame.Rect(random.randint(5,window_width-5),0,ring_width,ring_height)
            new_bird = pygame.Rect(random.randint(5,window_width-5),0,ring_width,ring_height)
            rings.append(new_ring)
            birds.append(new_bird)
    if points >= 50 and points <= 100 :
        level = 3
        if x >= 75 :
            new_ring = pygame.Rect(random.randint(1, window_width-1), 0, ring_width, ring_height)
            new_bird = pygame.Rect(random.randint(1, window_width-1), 0, ring_width, ring_height)
            new_rice = pygame.Rect(random.randint(1, window_width-5), 0, rice_width, rice_height)
            rings.append(new_ring)
            birds.append(new_bird)
            riceA.append(new_rice)
    if points>=100 and points<=105:
        window.blit(win_text,(window_width*0.4, window_height*0.5))
        window.blit(win_img,(window_width*0.05, window_height*0.4))

    if points>105 and points<110:
        time.sleep(1)
        pygame.quit()

    if points<0 and points>-5:
        window.blit(game_over_text,(window_width * 0.5, window_height * 0.5))

    if points <= -5:
        time.sleep(1)
        pygame.quit()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()


    for ring in rings[:]:
        ring.bottom +=10
        if player.colliderect(ring):
            points +=1
            window.blit(player_point_img,player)
            rings.remove(ring)
        elif ring.bottom >= window_height:
            points -=1
            rings.remove(ring)
        else:
            window.blit(ring_img,ring)

    for bird in birds[:]:
        bird.bottom +=10
        if player.colliderect(bird):
            points -=1
            window.blit(wedding_blame_img, player)
            birds.remove(bird)
        else:
            window.blit(bird_img, bird)

    for rice in riceA[:]:
        rice.bottom +=10
        if player.colliderect(rice):
            points +=1
            window.blit(player_point_img,player)
            riceA.remove(rice)
        else:
            window.blit(rice_img,rice)

    points_text = myfont.render("POINTS: " + str(points),False,BLACK)
    level_text = myfont.render("LEVEL: " + str(level),False,BLACK)

    window.blit(points_text, (window_width*0.1,window_height-50))
    window.blit(level_text, (window_width * 0.1,window_height-30))
    game_over_text = myfont2.render("GAME OVER", False, RED)
    pygame.display.update()
    clock.tick(10)