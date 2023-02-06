import pygame,sys

pygame.init()

SCREEN_Width, SCREEN_Hight = 600, 500

Screen = pygame.display.set_mode((SCREEN_Width ,SCREEN_Hight))

class Grid():
    def __init__(self):

        # Colors
        self.Lines_Color = (46, 38, 51)
        self.Shape_Color = (255, 189, 66)
        self.Points_Color = (255,0 , 0)

        # Setting
        self.Size = 50
        self.LineSize = 10
        self.PointRadius = 5
        self.Hover_Point = pygame.Vector2(0,0)

        # Line
        self.Lines = []
        self.Hover_line = False
        self.Hover_line_point = pygame.Vector2(0,0)

        # Intersect
        self.FixIntersect = []
        self.Intersect = []

    def update(self):
        for x in range(int(SCREEN_Width/self.Size)):
            for y in range(int(SCREEN_Hight/self.Size)):
                if pygame.draw.circle(Screen, (0,0,0), (x*self.Size,self.Size*y), 5).collidepoint(XMouse, YMouse):
                    self.Hover_Point = pygame.Vector2(x,y)
                    return
                else:
                    self.Hover_Point = pygame.Vector2(-1,-1)

    def draw(self):
        for x in range(int(SCREEN_Width/self.Size)):
            pygame.draw.line(Screen, self.Lines_Color, (x*self.Size,0), (x*self.Size,SCREEN_Hight), self.LineSize)
        
        for y in range(int(SCREEN_Hight/self.Size)):
            pygame.draw.line(Screen, self.Lines_Color, (0,y*self.Size), (SCREEN_Width,y*self.Size), self.LineSize)

    def draw_Hover_point(self):
        pygame.draw.circle(Screen, self.Points_Color, (self.Hover_Point.x*self.Size,self.Hover_Point.y*self.Size), self.PointRadius)

    def Hover_Line(self):
        for Line in self.Lines:
            if pygame.draw.line(Screen, self.Shape_Color, (Line[0][0]*self.Size,Line[0][1]*self.Size), (Line[1][0]*self.Size,Line[1][1]*self.Size),self.LineSize).collidepoint(XMouse, YMouse):
                pygame.draw.line(Screen, self.Shape_Color, (Line[0][0]*self.Size,Line[0][1]*self.Size), (Line[1][0]*self.Size,Line[1][1]*self.Size),20)

    def draw_Hover_line(self):
        if self.Hover_line:
            pygame.draw.line(Screen, self.Shape_Color, (self.Hover_line_point.x*self.Size,self.Hover_line_point.y*self.Size), (XMouse,YMouse),self.LineSize)
            pygame.draw.circle(Screen, self.Points_Color, (XMouse,YMouse), self.PointRadius)
            pygame.draw.circle(Screen, self.Points_Color, (self.Hover_line_point.x*self.Size,self.Hover_line_point.y*self.Size), self.PointRadius)

    def draw_line(self):
        for Line in self.Lines:
            pygame.draw.line(Screen, self.Shape_Color, (Line[0][0]*self.Size,Line[0][1]*self.Size), (Line[1][0]*self.Size,Line[1][1]*self.Size),self.LineSize)
            pygame.draw.circle(Screen, self.Points_Color, (Line[0][0]*self.Size,Line[0][1]*self.Size), self.PointRadius)
            pygame.draw.circle(Screen, self.Points_Color, (Line[1][0]*self.Size,Line[1][1]*self.Size), self.PointRadius)

    def Find_Intersect(self):
        self.FixIntersect.clear()
        self.Intersect.clear()
        for LineNum in range(len(self.Lines)):
            for LineNum2 in range(len(self.Lines)):
                if not LineNum == LineNum2:
                    if self.Lines[LineNum2][0] == self.Lines[LineNum][0]:
                        self.FixIntersect.append(self.Lines[LineNum][0])

                    if self.Lines[LineNum2][1] == self.Lines[LineNum][1]:
                        self.FixIntersect.append(self.Lines[LineNum][1])

                    if self.Lines[LineNum2][0] == self.Lines[LineNum][1]:
                        self.FixIntersect.append(self.Lines[LineNum][1])

                    if self.Lines[LineNum2][1] == self.Lines[LineNum][0]:
                        self.FixIntersect.append(self.Lines[LineNum][0])

        for ver in self.FixIntersect:
            if ver not in self.Intersect:
                self.Intersect.append(ver)

    def Find_triangles(self): 
        pass

grid = Grid()

while True:
    (XMouse, YMouse) = pygame.mouse.get_pos()

    grid.update()
    

    Screen.fill((1, 157, 224))

    grid.Hover_Line()

    grid.draw()
    
    grid.draw_line()
    

    grid.draw_Hover_line()

    grid.draw_Hover_point()
    

    grid.Find_Intersect()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not grid.Hover_Point == [-1,-1] and not grid.Hover_Point == [-1,-1]:

                grid.Hover_line = True
                grid.Hover_line_point = pygame.Vector2(grid.Hover_Point.x,grid.Hover_Point.y)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                grid.Hover_line = False
                if not grid.Hover_Point == [-1,-1] and not grid.Hover_Point == [-1,-1]:
                    grid.Lines.append([grid.Hover_line_point,grid.Hover_Point])

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                grid.Lines.clear()

    pygame.display.update()
