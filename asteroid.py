import pygame
import random

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS


class Asteroid ( CircleShape ):
    def __init__( self, x, y, radius ):
        super().__init__( x, y, radius )

    def draw( self, screen ):
        pygame.draw.circle( screen, "white", self.position, self.radius, 2 )
    
    def update( self, dt ):
        # velo  = pygame.Vector2(10, 10)

        self.position += self.velocity * dt
        # self.position += velo * dt
    
    def split( self ):
        self.kill()

        if( self.radius < ASTEROID_MIN_RADIUS ):
            return
        
        randomAngle = random.uniform( 20, 50 )

        velocity1 = self.velocity.rotate( randomAngle ) * 1.2
        velocity2 = self.velocity.rotate( -randomAngle ) * 1.2

        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid1.velocity = velocity1

        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid2.velocity = velocity2
        
        