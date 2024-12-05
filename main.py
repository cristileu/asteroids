import pygame
import sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS, PLAYER_RADIUS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print( "Starting asteroids!" )

    print( f"Screen width: {SCREEN_WIDTH}" )
    print( f"Screen height: {SCREEN_HEIGHT}" )

    pygame.init()
    dt = 0

    updatableGroup = pygame.sprite.Group()
    drawableGroup = pygame.sprite.Group()
    asteroidGroup = pygame.sprite.Group()
    shotGroup = pygame.sprite.Group()

    Player.containers = ( updatableGroup, drawableGroup )
    Asteroid.containers = ( asteroidGroup, updatableGroup, drawableGroup )
    Shot.containers = ( shotGroup, updatableGroup, drawableGroup )
    AsteroidField.containers = ( updatableGroup )

    player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )
    # asteroid = Asteroid( SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4 , 10 )
    asteroidField = AsteroidField( )
    # shot = Shot( SCREEN_WIDTH / 6, SCREEN_HEIGHT / 6 )

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode( ( SCREEN_WIDTH, SCREEN_HEIGHT ) )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill( "#000000" )

        for updatableEntity in updatableGroup:
            updatableEntity.update( dt )
        # asteroid.update( dt )
        # player.update( dt )

        for asteroid in asteroidGroup:
            if asteroid.collidesWith( player ):
                print( "Game over!" )
                sys.exit()

            for shot in shotGroup:
                if shot.collidesWith( asteroid ):
                    shot.kill()
                    asteroid.split()


        for drawableEntity in drawableGroup:
            drawableEntity.draw( screen )
        # player.draw( screen )
        # asteroid.draw( screen )
        
        pygame.display.flip()

        dt = clock.tick( 60 ) / 1000



if __name__ == "__main__":
    main()