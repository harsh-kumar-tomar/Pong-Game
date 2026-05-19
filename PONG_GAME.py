import pygame
import random



pygame.init()

running = True
WIDTH = 500
HEIGHT = 500

#BOARD
BOARD_WIDTH = 10
BOARD_HEIGHT = 50
BOARD_MOVEMENT_SPEED = 4

# BALL
BALL_SPEED = 1
BALL_RADIUS = 10
BALL_SPEED_X = BALL_SPEED
BALL_SPEED_Y = BALL_SPEED
BALL_X = WIDTH//2
BALL_Y = HEIGHT//2


# PLAYERS 
PLAYER1_DIRECTION = "STOP"
PLAYER1_LAST_DIRECTION = "STOP"
PLAYER2_DIRECTION = "STOP"
PLAYER2_LAST_DIRECTION = "STOP"

PLAYER1_BOARD_X = 0
PLAYER1_BOARD_Y = 0

PLAYER2_BOARD_X = WIDTH-BOARD_WIDTH
PLAYER2_BOARD_Y = 0



screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()



while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT :
                running = False
                
        if event.type == pygame.KEYDOWN:
        
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                if event.key == pygame.K_UP:
                    PLAYER1_DIRECTION = "UP"
                    PLAYER1_LAST_DIRECTION = "UP"
                if event.key == pygame.K_DOWN:
                    PLAYER1_DIRECTION = "DOWN"  
                    PLAYER1_LAST_DIRECTION = "DOWN"              
            
            if event.key == pygame.K_w or event.key == pygame.K_s:
                if event.key == pygame.K_w:
                    PLAYER2_DIRECTION = "UP"
                    PLAYER2_LAST_DIRECTION = "UP"
                if event.key == pygame.K_s:
                    PLAYER2_DIRECTION = "DOWN"
                    PLAYER2_LAST_DIRECTION = "DOWN"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                PLAYER1_DIRECTION = "STOP"
            
            if event.key == pygame.K_w or event.key == pygame.K_s:
                PLAYER2_DIRECTION = "STOP"
    
    # UPDATE PLAYER MOVEMENT
    
    if PLAYER1_DIRECTION == "UP" :
        if (PLAYER1_BOARD_Y - BOARD_MOVEMENT_SPEED)  >= 0 :
            PLAYER1_BOARD_Y -= BOARD_MOVEMENT_SPEED
        else:
            PLAYER1_BOARD_Y = 0
    elif PLAYER1_DIRECTION == "DOWN":
        if (PLAYER1_BOARD_Y + BOARD_MOVEMENT_SPEED + BOARD_HEIGHT) <= HEIGHT:
            PLAYER1_BOARD_Y += BOARD_MOVEMENT_SPEED
        else:
            PLAYER1_BOARD_Y = HEIGHT - BOARD_HEIGHT
        
    if PLAYER2_DIRECTION == "UP" :
        if (PLAYER2_BOARD_Y - BOARD_MOVEMENT_SPEED)  >= 0 :
            PLAYER2_BOARD_Y -= BOARD_MOVEMENT_SPEED
        else:
            PLAYER2_BOARD_Y = 0 
    elif PLAYER2_DIRECTION == "DOWN":
        if (PLAYER2_BOARD_Y + BOARD_MOVEMENT_SPEED + BOARD_HEIGHT) <= HEIGHT:
            PLAYER2_BOARD_Y += BOARD_MOVEMENT_SPEED
        else:
            PLAYER2_BOARD_Y = HEIGHT - BOARD_HEIGHT

    
    # UPDATE BALL MOVEMENT

    BALL_X += BALL_SPEED_X

    # for TOP and BOTTOM
    if 0 <= BALL_Y + BALL_SPEED_Y <= HEIGHT: 
        BALL_Y += BALL_SPEED_Y
    else:
        if BALL_Y < 0 :
            BALL_Y = 0
        elif BALL_Y > HEIGHT:
            BALL_Y = HEIGHT
        BALL_SPEED_Y = -1 * BALL_SPEED_Y

    # ball interaction with player 1
    if BALL_X  <= PLAYER1_BOARD_X + BOARD_WIDTH and PLAYER1_BOARD_Y  <= BALL_Y <= PLAYER1_BOARD_Y + BOARD_HEIGHT :
        BALL_SPEED_X = -1 * BALL_SPEED_X

        random_number = random.randint(1,4)
        
        if PLAYER1_LAST_DIRECTION == "UP":

            if random_number == 1:
                BALL_SPEED_Y = BALL_SPEED
            elif random_number == 2 :
                BALL_SPEED_Y = 0
            elif random_number == 3 or random_number == 4:
                BALL_SPEED_Y = -1 * BALL_SPEED

        if PLAYER1_LAST_DIRECTION == "DOWN":

            if random_number == 1:
                BALL_SPEED_Y = -1 * BALL_SPEED
            elif random_number == 2 :
                BALL_SPEED_Y = 0
            elif random_number == 3 or random_number == 4:
                BALL_SPEED_Y = BALL_SPEED

        
    
    
    
# --------
#|        |
#|        |
# --------
    # ball interation with player 2    
    if BALL_X + BALL_RADIUS >= PLAYER2_BOARD_X and PLAYER2_BOARD_Y <= BALL_Y <= PLAYER2_BOARD_Y + BOARD_HEIGHT :
        BALL_SPEED_X = -1 * BALL_SPEED_X

        random_number = random.randint(1,4)


        if PLAYER2_LAST_DIRECTION == "UP":

            if random_number == 1:
                BALL_SPEED_Y = BALL_SPEED
            elif random_number == 2 :
                BALL_SPEED_Y = 0
            elif random_number == 3 or random_number == 4:
                BALL_SPEED_Y = -1 * BALL_SPEED

        if PLAYER2_LAST_DIRECTION == "DOWN":

            if random_number == 1:
                BALL_SPEED_Y = -1 * BALL_SPEED
            elif random_number == 2 :
                BALL_SPEED_Y = 0
            elif random_number == 3 or random_number == 4:
                BALL_SPEED_Y = BALL_SPEED

    # window collision 
    # TOP , BOTTOM
    if BALL_Y == 0 or BALL_Y  == HEIGHT: 
        BALL_SPEED_Y = -1 * BALL_SPEED_Y

    
    
    # LEFT , RIGHT
    # if BALL_X < 0 or BALL_X > WIDTH?



    
    screen.fill((0,0,0))

    pygame.draw.rect(screen ,  (211, 211, 211), (PLAYER1_BOARD_X, PLAYER1_BOARD_Y, BOARD_WIDTH, BOARD_HEIGHT))
    pygame.draw.rect(screen ,  (0, 255, 0), (PLAYER2_BOARD_X, PLAYER2_BOARD_Y, BOARD_WIDTH, BOARD_HEIGHT))
    pygame.draw.rect(screen ,  (211, 211, 211), (BALL_X,BALL_Y, BALL_RADIUS, BALL_RADIUS))

    pygame.display.update()
    clock.tick(120)


pygame.quit()


# input
# update movement 
# detect collision 
# draw










