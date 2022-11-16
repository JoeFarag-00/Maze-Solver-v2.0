import pygame

class Grid_Node:

    def __init__(self, row, col, width, total_rows):

        self.row = row
        self.col = col
        self.width = width
        self.Row_Tot = total_rows
        self.X = row * width
        self.Y = col * width
        self.neighbours = []
        self.color = "White"

    def get_pos(self):
        return self.row, self.col

    def is_wall(self):
        return self.color == WALL_COLOR
   
    def make_wall(self):
        self.color = WALL_COLOR

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.X, self.Y, self.width, self.width))

    def update_neighbour(self, grid):

        if self.row < self.Row_Tot - 1 and not grid[self.row + 1][self.col].is_wall():
            self.neighbours.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_wall(): 
            self.neighbours.append(grid[self.row - 1][self.col])

        if self.col < self.Row_Tot - 1 and not grid[self.row][self.col + 1].is_wall():
            self.neighbours.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_wall():
            self.neighbours.append(grid[self.row][self.col - 1])

    def __lt__(self, other):

        return False


def Create_Grid(rows, width):
   
    grid = []
    gap = width // rows  
    for i in range(rows):
        grid.append([])  
        for j in range(rows):
            node = Grid_Node(i, j, gap, rows)
            grid[i].append(node)

    return grid


def Create_Grid_Lines(win, rows, width):
   
    gap = width // rows
    for i in range(rows):
        
        pygame.draw.line(win, "Black", (0, i * gap), (width, i * gap),width=3)
        for j in range(rows):
           
            pygame.draw.line(win, "Black", (j * gap, 0), (j * gap, width),width=3)


def Draw_Maze(win, grid, rows, width):
    
    win.fill("White")  

    for row in grid: 
        for node in row:
            node.draw(win)

    Create_Grid_Lines(win, rows, width)  
    pygame.display.update() 


def Mouse_Down_Node(pos, rows, width):
   
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

WALL_COLOR = (0, 0, 0)