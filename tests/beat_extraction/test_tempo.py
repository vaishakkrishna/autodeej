
# import pygame module in this program 
import unittest
from feature_extraction import extract_downbeats, extract_tempo_and_beats
from utils.pygame import handle_events, play_song_with_clicks  
class BeatExtractTests(unittest.TestCase):
    def test_beats_visual_travis(self):
        songs_dir = "assets/songs"
        song = "Pop Smoke - Creature ft. Swae Lee.mp3"
        song_filepath=f"{songs_dir}/{song}"
        # beats = extract_tempo_and_beats(song_filepath)[1] * 1000
        beats = extract_downbeats(song_filepath, mode="BeatNet") 
        play_song_with_clicks(beats, song_filepath)


if __name__ == "__main__":
    unittest.main()