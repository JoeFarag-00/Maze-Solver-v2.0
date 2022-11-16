from queue import PriorityQueue
import pygame

def BFS(draw, start, End):
   
    Queue = [start]
    Temp_List = []
    Touch_List = {}
    
    while len(Queue) > 0:
        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        Curr = Queue.pop(0)
        if Curr == End:
            Animate_Path(Touch_List, start, End, draw)
            End.color = "Red"
            start.color = "chartreuse3"
            return True

        for NBs in Curr.neighbours:  
            if Curr not in Queue:
             
                if NBs in Temp_List:
                  
                    continue
                Touch_List[NBs] = Curr  
                Queue.append(NBs)
                if NBs != start and NBs != End:
                    NBs.color = "Blue"
                    Temp_List.append(NBs)

        pygame.time.delay(BFS_Speed)
        draw()
        if Curr != start:
            Curr.color="DeepSkyBlue"

    return False


def DFS(draw, Start, End):
   
    Stack = [Start]
    Path_List = {}
    Touch_List = []

    while len(Stack) > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        Curr = Stack.pop()

        if Curr == End:
            Animate_Path(Path_List, Start, End, draw)
            End.color = "Red"
            Start.color = "chartreuse3"
            return True

        for NBs in Curr.neighbours: 
            if Curr not in Stack:
               
                if NBs in Touch_List:
          
                    continue
                Path_List[NBs] = Curr 
                Stack.append(NBs)
                if NBs != Start and NBs != End:
                    NBs.color = "blue"
                    Touch_List.append(NBs)

        pygame.time.delay(DFS_Speed)
        draw()
        if Curr != Start:
            Curr.color="DeepSkyBlue"

    return False


def Animate_Path(path_dict, start, end, draw):
   
    Path = [end]
    while Path[-1] != start:
        node = path_dict[Path[-1]]
        Path.append(node)

    Path = Path[::-1]
    for node in Path:
        node.color = "green4"
        pygame.time.delay(Path_Speed)
        draw()
        

Path_Speed = 5
BFS_Speed = 1
DFS_Speed = 1

