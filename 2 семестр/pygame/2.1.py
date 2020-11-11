import pygame

screen = pygame.display.set_mode([1024,768])
pygame.display.set_caption('Текущее расширение: 1024 x 768')
pygame.time.delay(2000)

screen = pygame.display.set_mode([800,600])
pygame.display.set_caption('Текущее расширение: 800 x 600')
pygame.time.delay(2000)

screen = pygame.display.set_mode([640,480])
pygame.display.set_caption('Текущее расширение: 640 x 480')
pygame.time.delay(2000)

screen = pygame.display.set_mode([1024,768], pygame.FULLSCREEN)
pygame.time.delay(2000)

screen = pygame.display.set_mode([800,600], pygame.FULLSCREEN)
pygame.time.delay(2000)

screen = pygame.display.set_mode([640,480], pygame.FULLSCREEN)
pygame.time.delay(2000)

pygame.quit()


