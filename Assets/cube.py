from .imports import pygame, Number, draw3DLine
class Cube():
    def __init__(self,pos: tuple[Number, Number, Number], width: Number, color = "red"):
        self.pos = pos
        self.width = width
        self.frontPoints = (
            tuple(map(sum, zip(pos, (- width / 2, - width / 2, - width / 2)))),
            tuple(map(sum, zip(pos, (- width / 2, width / 2, - width / 2)))),
            tuple(map(sum, zip(pos, (width / 2, width / 2, - width / 2)))),
            tuple(map(sum, zip(pos, (width / 2, - width / 2, - width / 2))))
        )
        self.backPoints = (
            tuple(map(sum, zip(pos, (- width / 2, - width / 2, width / 2)))),
            tuple(map(sum, zip(pos, (- width / 2, width / 2, width / 2)))),
            tuple(map(sum, zip(pos, (width / 2, width / 2, width / 2)))),
            tuple(map(sum, zip(pos, (width / 2, - width / 2, width / 2)))),
        )

    def update(self):
        pos = self.pos
        width = self.width
        self.frontPoints = (
            tuple(map(sum, zip(pos, (- width / 2, - width / 2, - width / 2)))),
            tuple(map(sum, zip(pos, (- width / 2, width / 2, - width / 2)))),
            tuple(map(sum, zip(pos, (width / 2, width / 2, - width / 2)))),
            tuple(map(sum, zip(pos, (width / 2, - width / 2, - width / 2))))
        )
        self.backPoints = (
            tuple(map(sum, zip(pos, (- width / 2, - width / 2, width / 2)))),
            tuple(map(sum, zip(pos, (- width / 2, width / 2, width / 2)))),
            tuple(map(sum, zip(pos, (width / 2, width / 2, width / 2)))),
            tuple(map(sum, zip(pos, (width / 2, - width / 2, width / 2)))),
        )

    def draw(self, screen):
        for i in range(4):
            draw3DLine(screen, self.frontPoints[i], self.backPoints[i], 2, (255,0,0))
            draw3DLine(screen, self.frontPoints[i], self.frontPoints[i-1], 2, (255, 0, 0))
            draw3DLine(screen, self.backPoints[i], self.backPoints[i-1], 2, (255, 0, 0))


