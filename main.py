from Assets import pygame, Number, Cube, draw3DLine, math, rotate3DPoint, combineTuple




def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    playerPos = [screen.get_width() / 2, screen.get_height() / 2, 0]
    playerAngle = [0, 0, 0]

    testCube = Cube((1200,700) + (0,),(30,400,200), "cyan", fillColor=(0,0,255))
    ground = Cube((0,900,0), (4000,40,4000), "red", fillColor=(255,0,0))
    oldMousePos = pygame.mouse.get_pos()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                testCube.update()
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

        #pygame.draw.circle(screen, "red",
        #                  playerPos[:2], 5)

        ground.draw(screen, debug=0, origin=tuple(playerPos), angle=playerAngle)
        testCube.draw(screen, debug=0, origin=tuple(playerPos), angle=playerAngle)
        
        pygame.display.flip()
        
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()