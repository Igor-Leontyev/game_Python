import pygame
import random


clock = pygame.time.Clock()

speed_player = 6
bg_x = 0
player_x = 80
player_y = 200
is_jump = False
jump_count = 7
player_anim_count = 0
tic_tac = 11

zombie_y = 210
zombie_x = 610

zombie_anim_count = 0
zombie_speed = 10

pygame.init()
screen = pygame.display.set_mode((600, 360))
pygame.display.set_caption('Game')
icon = pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)
bg = pygame.image.load('img/fo.png')
main_sound = pygame.mixer.Sound('sounds/Roy Jones Jr.mp3')
main_sound.set_volume(0.25)
main_sound.play()

zombie_list = []

walk_stop = [
    pygame.image.load('Sprite\sprite_stop.png').convert_alpha(),
    pygame.image.load('Sprite\sprite_stop2.png').convert_alpha(),
]

walk_right = [
    pygame.image.load('Sprite\sprite_go1.png').convert_alpha(),
    pygame.image.load('Sprite\sprite_go2.png').convert_alpha(),
    pygame.image.load('Sprite\sprite_go3.png').convert_alpha(),
    pygame.image.load('Sprite\sprite_go4.png').convert_alpha(),
]

walk_run = [
    pygame.image.load('Sprite\sprite_go5.png').convert_alpha(),
    pygame.image.load('Sprite\sprite_go6.png').convert_alpha(),
    pygame.image.load('Sprite\go7.png').convert_alpha(),
    pygame.image.load('Sprite\go8.png').convert_alpha(),
    pygame.image.load('Sprite\go9.png').convert_alpha(),
    pygame.image.load('Sprite\go10.png').convert_alpha(),
]
zombie_run = [
    pygame.image.load('Sprite\zzombie1.png').convert_alpha(),
    pygame.image.load('Sprite\zzombie2.png').convert_alpha(),
    pygame.image.load('Sprite\zzombie3.png').convert_alpha(),
    pygame.image.load('Sprite\zzombie4.png').convert_alpha(),
    pygame.image.load('Sprite\zzombie5.png').convert_alpha(),
]


def Run_left():
    global player_x
    if player_x > 20:
        player_x -= speed_player


def Run_right():
    global player_x
    if player_x < 260:
        player_x += speed_player


 
zombie_create_timer = pygame.USEREVENT + 1
pygame.time.set_timer(zombie_create_timer, random.randint(1000, 3500))

running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 600, 0))
    player_rect = walk_right[0].get_rect(topleft=(player_x, player_y))
    zombie_rect = zombie_run[0].get_rect(topleft=(zombie_x,zombie_y))
    

   

    if zombie_list:
        for(j, i) in enumerate( zombie_list):
            screen.blit(zombie_run[zombie_anim_count], i)
            i.x -= zombie_speed
            if zombie_anim_count == (len(zombie_run))-1:
                zombie_anim_count = 0
            if i.x < -40:
                zombie_list.pop(j)    
            else:
                zombie_anim_count += 1
        if player_rect.colliderect(zombie_rect):
            print("YOUR LOSER")        

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        screen.blit(walk_run[player_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))

    if keys[pygame.K_LEFT]:
        Run_left()
    elif keys[pygame.K_RIGHT]:
        Run_right()

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -7:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 7

    if player_anim_count == (len(walk_right))-1:
        player_anim_count = 0
    else:
        player_anim_count += 1

    bg_x -= speed_player
    

    if bg_x == -600:
        bg_x = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == zombie_create_timer:
            zombie_list.append(zombie_run[0].get_rect(topleft=(610, 210)))

    clock.tick(tic_tac)
