
# import pygame module in this program 
import unittest
from utils.pygame import handle_events, play_song_with_clicks  
class BeatExtractTests(unittest.TestCase):
    def test_beats_visual_travis(self):
        play_song_with_clicks(song_filepath="assets/songs/Travis Scott - 5 TINT (Audio).mp3")


if __name__ == "__main__":
    unittest.main()