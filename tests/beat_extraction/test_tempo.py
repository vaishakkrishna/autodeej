
# import pygame module in this program 
import time
import pygame 
from feature_extraction import extract_beats_timestamps  

def test_beats_visual(song_filepath):  

    pygame.init() 
    
    colors = [ (0, 255, 0) ,
    (0, 0, 128) ,
    (0, 0, 0) ,
    (255, 0, 0) ]
    
    # assigning values to X and Y variable 
    X = 400
    Y = 400
    
    screen = pygame.display.set_mode((X, Y )) 
    
    pygame.display.set_caption('Drawing') 
    
    screen.fill((255, 255, 255)) 

    # Create a surface and pass in a tuple containing its length and width
    surf_1 = pygame.Surface((50, 50))

    # Give the surface a color to separate it from the background
    surf_1.fill(colors[3])
    surf_1.get_rect()

    # Create a surface and pass in a tuple containing its length and width
    surf_2 = pygame.Surface((50, 50))

    # Give the surface a color to separate it from the background
    surf_2.fill((0, 0, 0))
    surf_2.get_rect()
    beats = extract_beats_timestamps(song_filepath)
    clock = pygame.time.get_ticks()
    counter = 0
    track1_move_next_time = beats[counter]

    while True :     
        # iterate over the list of Event objects 
        # that was returned by pygame.event.get() method. 
        for event in pygame.event.get() : 
            
            # if event object type is QUIT 
            # then quitting the pygame 
            # and program both. 
            if event.type == pygame.QUIT : 
    
                # deactivates the pygame library 
                pygame.quit() 
    
                # quit the program. 
                quit() 
    
        clock = pygame.time.get_ticks()
        
        if clock > track1_move_next_time:
            screen.blit(surf_1 if counter%2 else surf_2, (X/2, Y/2))
            counter +=1 
            track1_move_next_time = beats[counter]
        pygame.display.flip()
