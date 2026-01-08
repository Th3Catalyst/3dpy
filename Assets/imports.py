import pygame

from math import sin, cos

Number = int | float

def rotate3DPoint(center: tuple[Number,Number,Number], point: tuple[Number,Number,Number], rotation: tuple[Number,Number,Number]) -> tuple[Number,Number,Number]:
    relPos = tuple(map(sum, zip(-center, point)))
    rotMatrix = [
        [cos(rotation[1])*cos(rotation[0]),sin(rotation[2])*sin(rotation[1])*cos(rotation[0])-sin(rotation[0])*cos(rotation[2]),sin(rotation[1])*cos(rotation[0])*cos(rotation[2]) + sin(rotation[0])*sin(rotation[2])],
        [cos(rotation[1])*sin(rotation[0]),sin(rotation[2])*sin(rotation[1])*sin(rotation[0])+cos(rotation[2])*cos(rotation[0]),sin(rotation[1])*sin(rotation[0])*cos(rotation[2]) - cos(rotation[0])*sin(rotation[2])],
        [-sin(rotation[1]),sin(rotation[2])*cos(rotation[1]),cos(rotation[2])*cos(rotation[1])]
    ]
    endPoint = []
    for row in rotMatrix:
        val = 0
        for output, pos in zip(row, relPos):
            val += output*pos
        endPoint.append(val)
    return endPoint




def draw3DLine(screen, start: tuple[Number, Number, Number], end: tuple[Number, Number, Number], width: int, color) -> None:
    fov = 0.002
    origin = (screen.get_width()/2, screen.get_height()/2)
    projectedStart = (start[0] + (origin[0]-start[0])*(fov*(start[2])/(fov*(start[2])+1)), start[1] + (origin[1]-start[1])*(fov*(start[2])/(fov*(start[2])+1)))
    projectedEnd = (end[0] + (origin[0]-end[0])*(fov*(end[2])/(fov*(end[2])+1)), end[1] + (origin[1]-end[1])*(fov*(end[2])/(fov*(end[2])+1)))
    pygame.draw.line(screen, color, projectedStart, projectedEnd, width)