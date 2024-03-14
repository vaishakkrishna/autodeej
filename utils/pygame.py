import pygame

from feature_extraction.beat_extraction import extract_tempo_and_beats


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
            
def play_song_with_clicks(song_filepath:str="assets/songs/Drake - Pain 1993 (Audio) ft. Playboi Carti.mp3"):
        print(f"Testing song: {song_filepath}")
        init_pygame()
        surf_1 = pygame.Surface((50, 50))
        surf_1.fill((255, 255, 255))
        surf_1.get_rect()
        click = pygame.mixer.Sound("assets/sounds/click.mp3")
        offset = 75
        beats = (extract_tempo_and_beats(song_filepath)[1] * 1000) - offset
        pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=256)
        pygame.mixer.music.load(song_filepath)
        pygame.mixer.music.play()
        clock_offset = pygame.time.get_ticks()
        clock = 0
        counter = 0
        track1_move_next_time = beats[counter]

        while True :     
            # iterate over the list of Event objects 
            # that was returned by pygame.event.get() method. 
                
            handle_events(pygame.event.get())
        
            clock = pygame.time.get_ticks() - clock_offset
            
            if clock > track1_move_next_time:
                # screen.blit(surf_1 if counter%2 else surf_2, (X/2, Y/2))
                pygame.draw.circle(surf_1, (0, 0, 0), (200, 200), 50)
                pygame.display.update()
                click.play()
                counter +=1 
                track1_move_next_time = beats[counter]
                
            pygame.display.flip()