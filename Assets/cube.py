from .imports import Number, draw3DLine, math


# noinspection PyTypeChecker
class Cube():
    def __init__(self,pos: tuple[Number, Number, Number], width: Number, color = "red", heading=(math.pi/2, -math.pi/2, 0)):
        self.pos = pos
        self.width = width
        self.heading = heading
        self.color = color
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
            tuple(map(sum, zip(pos, ((width/math.sqrt(4/3))
                                        *math.cos(self.heading[1] + math.pi/4)
                                        *math.cos(self.heading[2] + math.pi/4),
                                     (width/math.sqrt(4/3))
                                         * math.cos(self.heading[0] - math.pi / 4)
                                         * math.sin(self.heading[2] + math.pi / 4),
                                     (width/math.sqrt(4/3))
                                        *math.sin(self.heading[0] - math.pi/4)
                                        *math.sin(self.heading[1] + math.pi/4))))),
            tuple(map(sum, zip(pos, ((width/math.sqrt(4/3))
                                        *math.cos(self.heading[1] + math.pi/4)
                                        *math.cos(self.heading[2] - math.pi/4),
                                    (width/math.sqrt(4/3))
                                        *math.cos(self.heading[0] + math.pi/4)
                                        *math.sin(self.heading[2] - math.pi/4),
                                    (width/math.sqrt(4/3))
                                        *math.sin(self.heading[0] + math.pi/4)
                                        *math.sin(self.heading[1] + math.pi/4))))),
            tuple(map(sum, zip(pos, ((width/math.sqrt(4/3))
                                        *math.cos(self.heading[1] - math.pi/4)
                                        *math.cos(math.pi + self.heading[2] + math.pi/4),
                                    (width/math.sqrt(4/3))
                                     * math.cos(self.heading[0] + math.pi / 4)
                                     * math.sin(math.pi + self.heading[2] + math.pi / 4),
                                    (width/math.sqrt(4/3))
                                        *math.sin(self.heading[0] + math.pi/4)
                                        *math.sin(self.heading[1] - math.pi/4))))),
            tuple(map(sum, zip(pos, ((width/math.sqrt(4/3))
                                        *math.cos(self.heading[1] - math.pi/4)
                                        *math.cos(math.pi + self.heading[2] - math.pi/4),
                                     (width/math.sqrt(4/3))
                                        *math.cos(self.heading[0] - math.pi/4)
                                        *math.cos(math.pi + self.heading[2] - math.pi/4),
                                     (width/math.sqrt(4/3))
                                        *math.sin(self.heading[0] - math.pi/4)
                                        *math.sin(self.heading[1] - math.pi/4)))))
        )
        self.backPoints = (
            tuple(map(sum, zip(pos, ((width / math.sqrt(4 / 3))
                                        * math.cos(math.pi + self.heading[1] - math.pi / 4)
                                        * math.cos(self.heading[2] + math.pi / 4),
                                     (width/math.sqrt(4/3))
                                        * math.cos(math.pi + self.heading[0] + math.pi / 4)
                                        * math.sin(self.heading[2] + math.pi / 4),
                                     (width / math.sqrt(4 / 3))
                                        * math.sin(math.pi + self.heading[0] + math.pi / 4)
                                        * math.sin(math.pi + self.heading[1] - math.pi / 4))))),
            tuple(map(sum, zip(pos, ((width / math.sqrt(4 / 3))
                                        * math.cos(math.pi + self.heading[1] - math.pi / 4)
                                        * math.cos(self.heading[2] - math.pi / 4),
                                     (width/math.sqrt(4/3))
                                        * math.cos(math.pi + self.heading[0] - math.pi / 4)
                                        * math.sin(self.heading[2] - math.pi / 4),
                                     (width / math.sqrt(4 / 3))
                                        * math.sin(math.pi + self.heading[0] - math.pi / 4)
                                        * math.sin(math.pi + self.heading[1] - math.pi / 4))))),
            tuple(map(sum, zip(pos, ((width / math.sqrt(4 / 3))
                                        * math.cos(math.pi + self.heading[1] + math.pi / 4)
                                        * math.cos(math.pi + self.heading[2] + math.pi / 4),
                                     (width/math.sqrt(4/3))
                                        * math.cos(math.pi + self.heading[0] - math.pi / 4)
                                        * math.sin(math.pi + self.heading[2] + math.pi / 4),
                                     (width / math.sqrt(4 / 3))
                                        * math.sin(math.pi + self.heading[0] - math.pi / 4)
                                        * math.sin(math.pi + self.heading[1] + math.pi / 4))))),
            tuple(map(sum, zip(pos, ((width / math.sqrt(4 / 3))
                                        * math.cos(math.pi + self.heading[1] + math.pi / 4)
                                        * math.cos(math.pi + self.heading[2] - math.pi / 4),
                                     (width/math.sqrt(4/3))
                                        * math.cos(math.pi + self.heading[0] + math.pi / 4)
                                        * math.sin(math.pi + self.heading[2] - math.pi / 4),
                                     (width / math.sqrt(4 / 3))
                                        * math.sin(math.pi + self.heading[0] + math.pi / 4)
                                        * math.sin(math.pi + self.heading[1] + math.pi / 4)))))
        )

    def draw(self, screen, debug=False):
        for i in range(4):
            draw3DLine(screen, self.frontPoints[i], self.backPoints[i], 2, self.color)
            draw3DLine(screen, self.frontPoints[i], self.frontPoints[i-1], 2, self.color)
            draw3DLine(screen, self.backPoints[i], self.backPoints[i-1], 2, self.color)
        if debug:
            draw3DLine(screen, self.pos, (self.pos[0] + 500*math.cos(self.heading[1])*math.cos(self.heading[2]), self.pos[1] + 500*math.cos(self.heading[0])*math.sin(self.heading[2]), self.pos[2] + 500*math.sin(self.heading[1])*math.sin(self.heading[0])), 2, "blue")


