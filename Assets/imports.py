from typing import Literal, Iterable
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import pygame, math
from math import sin, cos


Number = int | float
Point3D = tuple[Number, Number, Number]
Point2D = tuple[Number, Number]

def combineTuple(a: tuple[Number, ...],b: tuple[Number, ...], mode: Literal["sum", "subtract"]) -> tuple[Number, ...]:
    def subtract(a):
        return a[0]-a[1]
    if mode == "sum":
        return tuple(map(sum, zip(a, b)))
    elif mode == "subtract":
        return tuple(map(subtract, zip(a, b)))
    raise ValueError("Invalid mode. Valid modes: sum, subtract.")


def rotate3DPoint(center: Point3D, point: Point3D, rotation: Point3D) -> Point3D:
    """

    :param center: origin of the rotation
    :param point: point to be rotated
    :param rotation: rotation angles (roll, yaw, pitch)
    :return: point post-rotation
    """

    relPos = combineTuple(point, center, mode="subtract")
    rotMatrix = [
        [cos(rotation[1])*cos(rotation[0]),sin(rotation[2])*sin(rotation[1])*cos(rotation[0])-sin(rotation[0])*cos(rotation[2]),sin(rotation[1])*cos(rotation[0])*cos(rotation[2]) + sin(rotation[0])*sin(rotation[2])],
        [cos(rotation[1])*sin(rotation[0]),sin(rotation[2])*sin(rotation[1])*sin(rotation[0])+cos(rotation[2])*cos(rotation[0]),sin(rotation[1])*sin(rotation[0])*cos(rotation[2]) - cos(rotation[0])*sin(rotation[2])],
        [-sin(rotation[1]),sin(rotation[2])*cos(rotation[1]),cos(rotation[2])*cos(rotation[1])]
    ]
    relEndPoint = []
    for row in rotMatrix:
        val = 0
        for output, pos in zip(row, relPos):
            val += output*pos
        relEndPoint.append(val)
    endPoint = combineTuple(center, tuple(relEndPoint), mode="sum")
    return endPoint

def pointBehindRect(origin: Point2D, point: Point3D, rect: Iterable[Point3D]) -> bool:
    return not all(point[2] < topPoint[2] for topPoint in rect) and Polygon(list(map(lambda x: project3DPoint(origin, x), rect))).contains(Point(project3DPoint(origin, point)))

def project3DPoint(origin: tuple[Number,Number], point: Point3D) -> Point2D:
    fov = 0.002
    projZ = (fov * (point[2]) / (fov * (point[2]) + 1)) if point[2] > -500 else 2 * point[2]

    return (point[0] + (origin[0] - point[0]) * projZ, point[1] + (origin[1] - point[1]) * projZ)

def draw3DLine(screen, start: Point3D, end: Point3D, width: int, color, origin: Point2D | None = None) -> None:
    if origin is None:
        origin = (screen.get_width() / 2, screen.get_height() / 2)
    projectedStart = project3DPoint(origin, start)
    projectedEnd = project3DPoint(origin, end)
    pygame.draw.line(screen, color, projectedStart, projectedEnd, width)

def castRay(screen: pygame.Surface, start: Point3D, direction: Number, collisionObjects: Iterable[pygame.Rect]) -> tuple[tuple[Number, Number], Number]:
    distance = 0
    testPoint = start
    while True:

        if any(o.collidepoint(testPoint) for o in collisionObjects):
            return (testPoint, distance)
        testPoint = combineTuple(testPoint, (math.cos(direction), math.sin(direction)), mode="sum")
        distance += 1
        if not screen.get_rect().collidepoint(testPoint):
            return (testPoint, distance)