from Assets import pygame, Number, Cube, draw3DLine




def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    testCube = Cube((200,400,154),300)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEWHEEL:
                if event.y == 1:
                    testCube.pos = tuple(map(sum, zip(testCube.pos, (0,0,40))))
                elif event.y == -1:
                    testCube.pos = tuple(map(sum, zip(testCube.pos, (0,0,-40))))
                testCube.update()
        testCube.pos = pygame.mouse.get_pos() + (testCube.pos[2],)
        testCube.update()
        
        screen.fill("#000000")

        '''for i in range(0,1281,40):
            draw3DLine(screen, (i, 720, 0), (i, 720, 400), 2, (255, 0, 0))
        for i in range(0,1281,40):
            draw3DLine(screen, (i, 0, 0), (i, 0, 400), 2, (255, 0, 0))
        for i in range(0, 400, 10):
            draw3DLine(screen, (0, 720, i), (0, 0, i), 2, (255, 0, 0))
        for i in range(0, 400, 10):
            draw3DLine(screen, (1280, 720, i), (1280, 0, i), 2, (255, 0, 0))'''

        testCube.draw(screen)

        
        pygame.display.flip()
        
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()