
# import pygame module in this program 
import unittest
import pygame 
from feature_extraction import extract_beats_timestamps
from utils import init_pygame
from utils.pygame import handle_events  
class BeatExtractTests(unittest.TestCase):
    def test_beats_visual_drake(self):  
        song_filepath = "assets/songs/Drake - Pain 1993 (Audio) ft. Playboi Carti.mp3"
        print(f"Testing song: {song_filepath}")
        init_pygame()
        surf_1 = pygame.Surface((50, 50))
        surf_1.fill((255, 255, 255))
        surf_1.get_rect()
        click = pygame.mixer.Sound("assets/sounds/click.mp3")
        offset = 90
        beats = (extract_beats_timestamps(song_filepath) * 1000) - offset
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

if __name__ == "__main__":
    unittest.main()