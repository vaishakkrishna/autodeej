import pygame


def init_pygame():

    pygame.init() 
    
    X = 400
    Y = 400
    
    screen = pygame.display.set_mode((X, Y )) 
    
    screen.fill((255, 255, 255)) 
    
    
def handle_events(events):
    for event in events:
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 

            # deactivates the pygame library 
            pygame.quit() 

            # quit the program. 
            quit()