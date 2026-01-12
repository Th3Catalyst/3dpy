from Assets import pygame, Number, Cube, draw3DLine, math, rotate3DPoint, combineTuple




def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    playerPos = [0,0, 0]
    playerAngle = [0, 0, 0]

    testCube = Cube((0,0, 0),(200,200,200), "cyan", fillColor=(0,0,255))
    oldMousePos = pygame.mouse.get_pos()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.mouse.get_pressed()[0]:
                print(testCube.rotation)
                testCube.rotation = combineTuple(testCube.rotation, (0,(oldMousePos[0]-pygame.mouse.get_pos()[0])/500,-(oldMousePos[1]-pygame.mouse.get_pos()[1])/500), mode="sum")
                if event.type == pygame.MOUSEWHEEL:
                    if event.y == 1:
                        testCube.rotation = combineTuple(testCube.rotation, (math.pi/20,0,0), mode="sum")
                    elif event.y == -1:
                        testCube.rotation = combineTuple(testCube.rotation, (-math.pi/20,0,0), mode="sum")
            else:
                testCube.pos = combineTuple(pygame.mouse.get_pos(), (screen.get_width()/2,screen.get_height()/2), mode="subtract") + (testCube.pos[2],)
                if event.type == pygame.MOUSEWHEEL:
                    if event.y == 1:
                        testCube.pos = combineTuple(testCube.pos, (0,0,40), mode="sum")
                    elif event.y == -1:
                        testCube.pos = combineTuple(testCube.pos, (0,0,-40), mode="sum")
        oldMousePos = pygame.mouse.get_pos()


        screen.fill("#000000")


        testCube.draw(screen, debug=0, origin=tuple(playerPos), angle=playerAngle)

        pygame.display.flip()
        
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()