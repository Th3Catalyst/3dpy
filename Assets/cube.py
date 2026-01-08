from .imports import pygame, Number, namedtuple
class Cube(pygame.sprite.Sprite):
    def __init__(self,pos: tuple[Number, Number, Number], width: Number, color = "red"):
        frontPoints = (
            pos + (- width / 2, - width / 2, width / 2),
            pos + (- width / 2, width / 2, width / 2),
            pos + (width / 2, - width / 2, width / 2),
            pos + (width / 2, width / 2, width / 2)
        )
        backPoints = (
            pos + (- width / 2, - width / 2, width / 2),
            pos + (- width / 2, width / 2, width / 2),
            pos + (width / 2, - width / 2, width / 2),
            pos + (width / 2, width / 2, width / 2)
        )


