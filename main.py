import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    # to make the game render in 60FPS
    clock = pygame.time.Clock()
    dt = 0

    # player
    x= SCREEN_WIDTH/2
    y= SCREEN_HEIGHT/2
    player = Player(x,y)
    while True:
        # to check wheather the player has quit(if did then it will make window close button work)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black") # set the screen color to black
        player.draw(screen)
        pygame.display.flip() # refreshes the screen
        # 60FPS- so it will use lesser resourses
        # it will pause the loop until 1/60th of a seconde
        deltaTime = clock.tick(60)
        dt = deltaTime/1000



    print("Sartting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen Height: {SCREEN_HEIGHT}")





if __name__== "__main__":
    main()