import pygame

from .imports import Number, draw3DLine, rotate3DPoint, combineTuple, project3DPoint, Point3D, Point2D, pointBehindRect


# noinspection PyTypeChecker
class Cube():
    def __init__(self,pos: Point3D, dims: Point3D, color = "red", rotation=(0, 0, 0), fillColor = None):
        self.pos = pos
        self.rotation = rotation
        self.dims = dims
        self.width = dims[0]
        self.height = dims[1]
        self.depth = dims[2]
        self.color = color
        self.fillColor = fillColor
        self.frontPoints = (
            combineTuple(pos, (- self.width / 2, - self.height / 2, - self.depth / 2), mode="sum"),
            combineTuple(pos, (- self.width / 2, self.height / 2, - self.depth / 2), mode="sum"),
            combineTuple(pos, (self.width / 2, self.height / 2, - self.depth / 2), mode="sum"),
            combineTuple(pos, (self.width / 2, - self.height / 2, - self.depth / 2), mode="sum")
        )
        self.backPoints = (
            combineTuple(pos, (- self.width / 2, - self.height / 2, self.depth / 2), mode="sum"),
            combineTuple(pos, (- self.width / 2, self.height / 2, self.depth / 2), mode="sum"),
            combineTuple(pos, (self.width / 2, self.height / 2, self.depth / 2), mode="sum"),
            combineTuple(pos, (self.width / 2, - self.height / 2, self.depth / 2), mode="sum"),
        )

    def update(self):
        pos = self.pos
        self.frontPoints = (
            combineTuple(pos, (- self.width / 2, - self.height / 2, - self.depth / 2), mode="sum"),
            combineTuple(pos, (- self.width / 2, self.height / 2, - self.depth / 2), mode="sum"),
            combineTuple(pos, (self.width / 2, self.height / 2, - self.depth / 2), mode="sum"),
            combineTuple(pos, (self.width / 2, - self.height / 2, - self.depth / 2), mode="sum")
        )
        self.backPoints = (
            combineTuple(pos, (- self.width / 2, - self.height / 2, self.depth / 2), mode="sum"),
            combineTuple(pos, (- self.width / 2, self.height / 2, self.depth / 2), mode="sum"),
            combineTuple(pos, (self.width / 2, self.height / 2, self.depth / 2), mode="sum"),
            combineTuple(pos, (self.width / 2, - self.height / 2, self.depth / 2), mode="sum"),
        )
        self.frontPoints = tuple(map(lambda point: rotate3DPoint(self.pos, point, self.rotation), self.frontPoints))
        self.backPoints = tuple(map(lambda point: rotate3DPoint(self.pos, point, self.rotation), self.backPoints))


    def draw(self, screen, debug=False, origin: Point2D | Point3D | None = None, angle: Point3D = (0,0,0)):
        playerPos = origin
        origin = (screen.get_width()/2, screen.get_height()/2)
        '''zOffset = 0
        if len(origin) == 3:
            zOffset = origin[2]
            origin = origin[:2]
        
        if zOffset != 0:
            self.frontPoints = tuple(map(lambda i : combineTuple(i, (0,0,zOffset), mode="subtract"), self.frontPoints))
            self.backPoints = tuple(map(lambda i : combineTuple(i, (0,0,zOffset), mode="subtract"), self.backPoints))
            print(self.frontPoints)'''
        pointsBackup = [self.pos]

        pointsBackup += (self.frontPoints, self.backPoints)
        if len(playerPos) == 3:
            rotateOrigin = combineTuple((0,0,0), origin + (-500,), mode="sum")
            self.pos = combineTuple(self.pos, combineTuple(playerPos, origin+(0,), mode="subtract"), mode="subtract")
            self.pos = rotate3DPoint(rotateOrigin, self.pos, angle)

        self.update()
        self.frontPoints = tuple(map(lambda point: rotate3DPoint(self.pos, point, angle), self.frontPoints))
        self.backPoints = tuple(map(lambda point: rotate3DPoint(self.pos, point, angle), self.backPoints))
        if len(playerPos) == 3:
            '''self.frontPoints = tuple(map(lambda i: combineTuple(i, playerPos, mode="subtract"), self.frontPoints))
            self.backPoints = tuple(map(lambda i: combineTuple(i, playerPos, mode="subtract"), self.backPoints))
            self.frontPoints = tuple(map(lambda i: rotate3DPoint(origin+(0,), i, angle), self.frontPoints))
            self.backPoints = tuple(map(lambda i: rotate3DPoint(origin+(0,),i, angle), self.backPoints))'''
        topPoints = (self.frontPoints[0], self.frontPoints[-1], self.backPoints[-1], self.backPoints[0])
        bottomPoints = self.frontPoints[1:3] + self.backPoints[1:3][::-1]
        leftPoints = self.frontPoints[:2] + self.backPoints[:2][::-1]
        rightPoints = self.frontPoints[2:] + self.backPoints[2:][::-1]
        drawnPoints = []
        for point in self.frontPoints+self.backPoints:
            if point not in topPoints:
                 if pointBehindRect(origin, point, topPoints):
                     continue
            if point not in bottomPoints:
                if pointBehindRect(origin, point, bottomPoints):
                    continue
            if point not in leftPoints:
                if pointBehindRect(origin, point, leftPoints):
                    continue
            if point not in rightPoints:
                if pointBehindRect(origin, point, rightPoints):
                    continue
            if point not in self.frontPoints:
                if pointBehindRect(origin, point, self.frontPoints):
                    continue
            if point not in self.backPoints:
                if pointBehindRect(origin, point, self.backPoints):
                    continue
            drawnPoints.append(point)

        if self.fillColor:
            for face in [topPoints, bottomPoints, leftPoints, rightPoints, self.frontPoints, self.backPoints]:
                if all(point in drawnPoints for point in face):
                    pygame.draw.polygon(screen, self.fillColor, list(map(lambda x: project3DPoint(origin, x), face)))
        for i in range(4):
            if debug:
                pygame.draw.circle(screen, self.color if self.frontPoints[i] in drawnPoints else "white", project3DPoint(origin, self.frontPoints[i]), 5)
                pygame.draw.circle(screen, self.color if self.backPoints[i] in drawnPoints else "white", project3DPoint(origin, self.backPoints[i]), 5)
            if self.frontPoints[i] in drawnPoints and self.backPoints[i] in drawnPoints:
                draw3DLine(screen, self.frontPoints[i], self.backPoints[i], 2, self.color, origin=origin)
            if self.frontPoints[i] in drawnPoints and self.frontPoints[i-1] in drawnPoints:
                draw3DLine(screen, self.frontPoints[i], self.frontPoints[i - 1], 2, self.color, origin=origin)
            if self.backPoints[i] in drawnPoints and self.backPoints[i - 1] in drawnPoints:
                draw3DLine(screen, self.backPoints[i], self.backPoints[i - 1], 2, self.color, origin=origin)
        if len(playerPos) == 3:
            #draw3DLine(screen, self.pos, rotateOrigin, 4, "yellow", origin)
            self.pos, self.frontPoints, self.backPoints = pointsBackup


        if debug:
            draw3DLine(screen, self.pos, rotate3DPoint(self.pos,combineTuple(self.pos, (0,0,-300), mode="sum"), self.rotation), 2, "blue", origin=origin)


