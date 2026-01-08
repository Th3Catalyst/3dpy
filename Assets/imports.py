import pygame, math

Number = int | float

def draw3DLine(screen, start: tuple[Number, Number, Number], end: tuple[Number, Number, Number], width: int, color) -> None:
    fov = 0.002
    origin = (screen.get_width()/2, screen.get_height()/2)
    projectedStart = (start[0] + (origin[0]-start[0])*(fov*(start[2])/(fov*(start[2])+1)), start[1] + (origin[1]-start[1])*(fov*(start[2])/(fov*(start[2])+1)))
    projectedEnd = (end[0] + (origin[0]-end[0])*(fov*(end[2])/(fov*(end[2])+1)), end[1] + (origin[1]-end[1])*(fov*(end[2])/(fov*(end[2])+1)))
    pygame.draw.line(screen, color, projectedStart, projectedEnd, width)