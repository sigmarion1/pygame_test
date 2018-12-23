import pygame

class Character:
    vHP = 100
    vMP = 100
    vATK = 100
    vDEF = 100
    vImage = 'warrior.png'

    def getStatus(self):
        print('HP = ' + str(self.vHP) )

    def putImg(self, x, y):
        screen.blit(carimg, (x, y))


BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

pygame.init()

displayWidth = 700
displayHeight= 500

screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('pyFantasy')
clock = pygame.time.Clock()

carimg = pygame.image.load('img/warrior.png')

done = False

player1 = Character()

pygame.font.init()

text = 'human warrior'
font = pygame.font.SysFont('Arial',100)
textsurface = font.render(text, True, (100,0,10))
screen.blit(textsurface,(0,0))



while not done:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    player1.putImg(200, 200)


    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()






