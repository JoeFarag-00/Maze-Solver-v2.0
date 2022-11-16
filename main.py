import pygame
import tkinter
import grid
import algorithms
import sys
from pygame.locals import *

class Start_Buttons:
    def __init__(self, x, y, width, height, text=" "):
        self.width = width
        self.height = height
        self.X = x
        self.Y = y
        self.Txt = text
        self.Rect = pygame.Rect(self.X, self.Y, self.width, self.height)
        self.color = Btn_Color

    def Make_Text(self):
        text = FONT.render(self.Txt, True, (255, 255, 255))
        WIN.blit(text,(self.X + (self.width / 2 - text.get_width() / 2), self.Y + (self.height / 2 - text.get_height() / 2)))

    def Draw_Btn(self):
        pygame.draw.rect(WIN, self.color, self.Rect)
        self.Make_Text()


def Create_Text(text, local_font, color, Txt_Win, x, y):
    
    Txt_Type = local_font.render(text, 1, color)
    Txt_Rect = Txt_Type.get_rect()
    Txt_Rect.topleft = (x, y)
    Txt_Win.blit(Txt_Type, Txt_Rect)


def Main_GUI():
   
    contrastBtn_DFS = None
    contrastBtn_BFS = None
    Mouse_Down = False
    Msg = None
    
    while True:
        WIN.fill("white")
        Create_Text('Choose Your Algorithm: ', FONT, "black", WIN, 190, 180)

        mx, my = pygame.mouse.get_pos()
        DFS_Btn = Start_Buttons(185, 250, 350, 50, "DFS")
        contrastBtn_DFS = Start_Buttons(175, 242, 370, 65)
        contrastBtn_DFS.color = "black"
        
        BFS_Btn = Start_Buttons(185, 350, 350, 50, "BFS")
        contrastBtn_BFS = Start_Buttons(175, 342, 370, 65)
        contrastBtn_BFS.color = "black"
        
        if DFS_Btn.Rect.collidepoint((mx, my)):
            DFS_Btn.color = "Red"
            if Mouse_Down:
                Msg = Maze_Plat(WIN, WIDTH, Algo=DFS_Btn.Txt)
                
        if BFS_Btn.Rect.collidepoint((mx, my)):
            BFS_Btn.color = "Red"
            if Mouse_Down:
                Msg = Maze_Plat(WIN, WIDTH, Algo=BFS_Btn.Txt)
      

        contrastBtn_DFS.Draw_Btn()
        contrastBtn_BFS.Draw_Btn()
        DFS_Btn.Draw_Btn()
        BFS_Btn.Draw_Btn()

        if Msg is not None:
            text = "Final Result : " + Msg
            Create_Text(text, FONT, Btn_Color, WIN, 30, 50)

        Mouse_Down = False
        for Event in pygame.event.get():
            if Event.type == QUIT:
                pygame.quit()
                sys.exit()
            if Event.type == KEYDOWN:
                if Event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if Event.type == MOUSEBUTTONDOWN:
                if Event.button == 1:
                    Mouse_Down = True

        pygame.display.update()
        Clock.tick(ticks)


def Maze_Plat(win, width, Algo):

    Pulse = pygame.time.Clock()
    Rows = Size_Row
    Main_Grid = grid.Create_Grid(Rows, width)
    Start = None 
    End = None
    Search_Start = False
    Is_Run = True
    
    while Is_Run:
        Pulse.tick(ticks)
        grid.Draw_Maze(win, Main_Grid, Rows, width)
        
        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                
                ND_Pos = pygame.mouse.get_pos()
                row, col = grid.Mouse_Down_Node(ND_Pos, Rows, width)
                node = Main_Grid[row][col]
                if not Start and node != End:
                    Start = node
                    Start.color = "chartreuse3"
                elif not End and node != Start:
                    End = node
                    End.color = "Red"
                elif node != End and node != Start:
                    node.make_wall()

            elif pygame.mouse.get_pressed(num_buttons=3)[2]: 
                ND_Pos = pygame.mouse.get_pos()
                row, col = grid.Mouse_Down_Node(ND_Pos, Rows, width)
                node = Main_Grid[row][col]
                node.reset()
                if node == Start:
                    Start = None
                elif node == End:
                    End = None

            if Event.type == pygame.KEYDOWN:
               
                if Event.key == pygame.K_RETURN and Start and End:
                    # start algorithm
                    Search_Start = True
                    for row in Main_Grid:
                        for node in row:
                            node.update_neighbour(Main_Grid)

                    Is_Found = False

                    if Algo == "BFS":
                        Is_Found = algorithms.BFS(lambda: grid.Draw_Maze(win, Main_Grid, Rows, width), Start,End)
                    elif Algo == "DFS":
                        Is_Found = algorithms.DFS(lambda: grid.Draw_Maze(win, Main_Grid, Rows, width), Start,End)
        
                    if not Is_Found: 
                        print("No Path Found")
                        message = "No Path Found"
                        pygame.time.delay(1000)
                        return message

                if Event.key == pygame.K_r:
                    Search_Start = False
                    Start = None
                    End = None
                    Main_Grid = grid.Create_Grid(Rows, width)
                    
pygame.init()
pygame.display.set_caption('Pathfinder Maze')
icon = pygame.image.load('Assets/Maze1.png')
pygame.display.set_icon(icon)

ticks = 144 
Size_Row = 35 
WIDTH = 700
WIN = pygame.display.set_mode((WIDTH, WIDTH))  
FONT = pygame.font.SysFont('Time New Roman', 42) 
Clock = pygame.time.Clock() 

Btn_Color = (10, 4, 60)
Btn_Hover = (254, 152, 1)

Main_GUI()
pygame.quit()
