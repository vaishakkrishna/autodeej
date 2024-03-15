import pygame
import numpy as np
from pydub import AudioSegment

def init_pygame(screen_size=(400,400)):

    pygame.init() 
    
    X = screen_size[0]
    Y = screen_size[1]
    
    screen = pygame.display.set_mode((X, Y )) 
    
    screen.fill((255, 255, 255)) 
    return screen
    
    
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

def add_clicks_to_song(beat_timestamps:np.array, song_filepath:str="assets/songs/Drake - Pain 1993 (Audio) ft. Playboi Carti.mp3"):
    click_filepath = "assets/sounds/click.mp3"
    song_segment = AudioSegment.from_mp3(song_filepath).apply_gain(-12)
    click_segment = AudioSegment.from_mp3(click_filepath)
    for b in beat_timestamps:
        song_segment = song_segment.overlay(click_segment, position=b)
    return song_segment

def play_song_with_clicks(beat_timestamps: np.array, song_filepath:str="assets/songs/Drake - Pain 1993 (Audio) ft. Playboi Carti.mp3",  visual=True):
    '''_summary_

    :param beat_timestamps: array of timestamps in ms
    :type beat_timestamps: np.array
    :param song_filepath: path to song mp3
    :type song_filepath: str, optional
    '''        
    print(f"Testing song: {song_filepath}")
    X, Y = 400, 400
    screen = init_pygame((X, Y))
    surf_1, surf_2 = pygame.Surface((50, 50)), pygame.Surface((50, 50))
    
    surf_1.fill((255, 0, 0))
    surf_2.fill((0, 0, 0))
    
    song_segment = add_clicks_to_song(beat_timestamps, song_filepath)
    export_filepath = "output.mp3"
    song_segment.export(export_filepath)
    pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=256)
    pygame.mixer.music.load(export_filepath)
    pygame.mixer.music.play()
    
    clock_offset = pygame.time.get_ticks()
    clock = 0
    counter = 0
    track1_move_next_time = beat_timestamps[counter]
    if visual:
        while True :
            # iterate over the list of Event objects 
            # that was returned by pygame.event.get() method. 
                
            handle_events(pygame.event.get())
        
            clock = pygame.time.get_ticks() - clock_offset
            
            if clock > track1_move_next_time:
                screen.blit(surf_1 if counter%2 else surf_2, (X/2, Y/2))
                counter +=1 
                track1_move_next_time = beat_timestamps[counter]
                
                pygame.display.flip()