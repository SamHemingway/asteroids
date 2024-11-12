import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
  pygame.init()

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (updatable, drawable, asteroids)
  AsteroidField.containers = updatable

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroid_field = AsteroidField()
  dt = 0

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    screen.fill("black")

    for sprite in updatable:
      sprite.update(dt)
    
    for sprite in drawable:
      sprite.draw(screen)
    
    pygame.display.flip()

    for asteroid in asteroids:
      if asteroid.is_colliding_with(player):
        print("Game over!")
        exit()

    dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()