import pygame

pygame.init()
pygame.joystick.init()

# get first joystick on system
joystick = pygame.joystick.Joystick(0)

COLOR_BLACK = (255, 255, 255)

# screen
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PongOut")
background = pygame.image.load("assets/background.png")

# player
player_2 = pygame.image.load("assets/player_2.png")
player_2_y = 300 - (56 / 2)
player_2_x = 400
player_2_move_up = False
player_2_move_down = False
player_2_move_left = False
player_2_move_right = False
shot = False

# player aim
aim = pygame.image.load("assets/aim2.png")
aim_x = 400 - 14
aim_y = 300 - 14
aim_up = False
aim_down = False
aim_left = False
aim_right = False

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:
    screen.fill(COLOR_BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        # joystick listener
        if event.type == pygame.JOYBUTTONDOWN:
            button_shot = joystick.get_button(5)
            if button_shot == 1:
                shot = True
        if event.type == pygame.JOYBUTTONUP:
            button_shot = joystick.get_button(5)
            if button_shot == 0:
                shot = False

        if event.type == pygame.JOYAXISMOTION:
            axis_0 = joystick.get_axis(2)
            if axis_0 < -0.5:
                player_2_move_left = True
            if axis_0 > 0.5:
                player_2_move_right = True
            if -0.5 < axis_0 < 0.5:
                player_2_move_left = False
                player_2_move_right = False
            axis_1 = joystick.get_axis(3)
            if axis_1 < -0.5:
                player_2_move_up = True
            if axis_1 > 0.5:
                player_2_move_down = True
            if -0.5 < axis_1 < 0.5:
                player_2_move_up = False
                player_2_move_down = False

            # aim listener
            axis_2 = joystick.get_axis(0)
            if axis_2 < -0.5:
                aim_left = True
            if axis_2 > 0.5:
                aim_right = True
            if -0.5 < axis_2 < 0.5:
                aim_left = False
                aim_right = False
            axis_3 = joystick.get_axis(1)
            if axis_3 < -0.5:
                aim_up = True
            if axis_3 > 0.5:
                aim_down = True
            if -0.5 < axis_3 < 0.5:
                aim_up = False
                aim_down = False

    # players movement
    if shot:
        print("SHOT")
    else:
        print("NULL")
    if player_2_move_left:
        player_2_x -= 10
    if player_2_move_right:
        player_2_x += 10
    if player_2_move_up:
        player_2_y -= 10
    if player_2_move_down:
        player_2_y += 10
    if aim_up:
        aim_y -= 10
    if aim_down:
        aim_y += 10
    if aim_left:
        aim_x -= 10
    if aim_right:
        aim_x += 10

    # drawing objects
    screen.blit(background, (0, 0))  # first in drawing order
    screen.blit(aim, (aim_x, aim_y))
    screen.blit(player_2, (player_2_x, player_2_y))

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
