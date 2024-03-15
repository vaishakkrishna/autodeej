from feature_extraction import detect_sections, Tonal_Fragment, extract_downbeats
import librosa
import logging

class Song:
    def __init__(self, song_filename: str) -> None:
        self.name = song_filename
        logging.info("Initializing song: %s", song_filename)
        
        logging.info("Detecting sections...")
        self.sections = detect_sections(song_filename)
        logging.info("DONE!")
        
        logging.info("Detecting key...")
        y, sr = librosa.load(song_filename)
        y_harmonic, y_percussive = librosa.effects.hpss(y)
        fragment = Tonal_Fragment(y_harmonic, sr)
        # fragment.chromagram(filename)
        
        self.key = max(fragment.key_dict, key=fragment.key_dict.get)
        logging.info("DONE!")
        logging.info("Detecting beats...")
        
        self.tempo, self.beats = extract_downbeats(song_filename)
        logging.info("DONE!")
        
    def get_tempo(self):
        return self.tempo
    
    def get_key(self):
        return self.key
    
    def get_sections(self):
        return self.sections
    