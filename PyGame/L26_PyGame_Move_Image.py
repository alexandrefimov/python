import pygame

MAX_X = 1920
MAX_Y = 1080
image_lenght = 400
image_height = image_lenght//2
x = (MAX_X - image_lenght)//2
y = (MAX_Y - image_height)//2

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
pygame.display.set_caption("INTEL")

myimage = pygame.image.load("./files/intel.png").convert()
myimage = pygame.transform.scale(myimage, (image_lenght, image_height))

gameover = False
bg_color = (110, 110, 110)
move_right = False
move_left = False
move_up = False
move_down = False

while gameover == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameover = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if x < 0:
                x = 0
            if x > MAX_X - image_lenght:
                x = MAX_X - image_lenght
            if y < 0:
                y = 0
            if y > MAX_Y - image_height:
                y = MAX_Y - image_height

    if move_left:
           x -= 3
           if x < 0:
               x = 0
    if move_right:
           x += 3
           if x > MAX_X - image_lenght:
               x = MAX_X - image_lenght
    if move_up:
           y -= 3
           if y < 0:
               y = 0
    if move_down:
           y += 3
           if y > MAX_Y - image_height:
               y = MAX_Y - image_height

    screen.fill(bg_color)
    screen.blit(myimage, (x, y))
    pygame.display.flip()