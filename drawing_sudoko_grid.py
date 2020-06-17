import pygame,sys # it is used for graphics

WIDTH = 600
HEIGHT = 600

#colours
WHITE = (255,255,255)
BLACK = (0,0,0)

# Positions and sizes
gridPos = (75,100)
cellSize = 50


class App:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        self.running = True

    def run(self):
        while self.running:
            self.events()
            self.draw()
        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.window.fill(WHITE)
        self.drawGrid(self.window)
        pygame.display.update()
            

    def drawGrid(self,window):
        pygame.draw.rect(window, BLACK, (gridPos[0], gridPos[1], WIDTH-150, HEIGHT-150), 2)
        for x in range(9):
            if x%3 != 0:
                pygame.draw.line(window, BLACK, (gridPos[0]+(x*cellSize), gridPos[1]), (gridPos[0]+(x*cellSize), gridPos[1]+450))
                pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1]+(x*cellSize)), (gridPos[0]+450, gridPos[1]+(x*cellSize)))
            else:
                pygame.draw.line(window, BLACK, (gridPos[0]+(x*cellSize), gridPos[1]), (gridPos[0]+(x*cellSize), gridPos[1]+450),2)
                pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1]+(x*cellSize)), (gridPos[0]+450, gridPos[1]+(x*cellSize)),2)

app = App()
app.run() 
