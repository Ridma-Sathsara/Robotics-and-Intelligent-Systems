import pygame
import numpy as np

#initialize pygame
pygame.init()

#Set up the drawing window
size = width, height = 1200, 800
screen = pygame.display.set_mode(size)

#clock
clock = pygame.time.Clock()

#load the image
image = pygame.image.load('robotImage.png').convert_alpha()

robot_size = (150,150)

image = pygame.transform.scale(image, robot_size)

# Frame counter
i = 0

solutionArray = np.load('simulationData.npy')

x = solutionArray[:,0]
y = solutionArray[:,1]
angle = -1*(360/(2*np.pi))*solutionArray[:,2]

cordinates = []

color_trajectory = (255,255,153)

while( i < len(x)):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0,0,0))

    image1 = pygame.transform.rotate(image, angle[i])

    image1_rect = image1.get_rect(center=(x[i],y[i]))

    screen.blit(image1, image1_rect)

    cordinates.append((x[i],y[i]))

    if i > 1:
        pygame.draw.lines(screen, color_trajectory, False, cordinates, 6)
    
    pygame.display.flip()

    pygame.time.delay(10)

    clock.tick(100)
    i = i + 1
    