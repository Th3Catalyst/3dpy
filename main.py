from Assets import pygame, Number, Cube, draw3DLine, math, rotate3DPoint, combineTuple




def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    playerPos = [0,0, 0]
    playerAngle = [0, 0, 0]

    testCube = Cube((500,0, 0),(200,200,500), "cyan", fillColor=(0,0,255))
    testCube2 = Cube((-200,0, 0),(200,200,200), "cyan", fillColor=(0,0,255))
    ground = Cube((0,500,0), (4000,40,4000), "red", fillColor=(255,0,0))
    oldMousePos = pygame.mouse.get_pos()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.mouse.get_pressed()[2]:
                print(testCube.rotation)
                testCube.rotation = combineTuple(testCube.rotation, (0,(oldMousePos[0]-pygame.mouse.get_pos()[0])/500,-(oldMousePos[1]-pygame.mouse.get_pos()[1])/500), mode="sum")
                if event.type == pygame.MOUSEWHEEL:
                    if event.y == 1:
                        testCube.rotation = combineTuple(testCube.rotation, (math.pi/20,0,0), mode="sum")
                    elif event.y == -1:
                        testCube.rotation = combineTuple(testCube.rotation, (-math.pi/20,0,0), mode="sum")
            else:
                #testCube.pos = pygame.mouse.get_pos() + (testCube.pos[2],)
                if event.type == pygame.MOUSEWHEEL:
                    if event.y == 1:
                        testCube.pos = combineTuple(testCube.pos, (0,0,40), mode="sum")
                    elif event.y == -1:
                        testCube.pos = combineTuple(testCube.pos, (0,0,-40), mode="sum")
            if pygame.key.get_pressed()[pygame.K_w]:
                playerPos[2] += 4
            if pygame.key.get_pressed()[pygame.K_s]:
                playerPos[2] -= 4
            if pygame.key.get_pressed()[pygame.K_d]:
                playerPos[0] += 4
            if pygame.key.get_pressed()[pygame.K_a]:
                playerPos[0] -= 4
            if pygame.key.get_pressed()[pygame.K_UP]:
                playerAngle[2] -= math.pi/20
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                playerAngle[2] += math.pi/20
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                playerAngle[1] -= math.pi/20
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                playerAngle[1] += math.pi/20
        oldMousePos = pygame.mouse.get_pos()


        screen.fill("#000000")



        ground.draw(screen, debug=0, origin=tuple(playerPos), angle=playerAngle)
        testCube.draw(screen, debug=0, origin=tuple(playerPos), angle=playerAngle)
        testCube2.draw(screen, debug=0, origin=tuple(playerPos), angle=playerAngle)
        pygame.draw.circle(screen, "yellow", combineTuple(tuple(playerPos)[:2], (screen.get_width() / 2, screen.get_height() / 2), mode="subtract"), 5)

        pygame.display.flip()
        
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()