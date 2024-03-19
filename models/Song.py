from feature_extraction import detect_sections, Tonal_Fragment, extract_downbeats
import librosa
import logging

class Song:
    def __init__(self, song_filepath: str) -> None:
        self.name = song_filepath
        logging.info("Initializing song: %s", song_filepath)
        
        logging.info("Detecting sections...")
        self.sections = detect_sections(song_filepath)*1000
        logging.info("DONE!")
        
        logging.info("Detecting key...")
        y, sr = librosa.load(song_filepath)
        self.data = y
        self.sample_rate = sr
        y_harmonic, y_percussive = librosa.effects.hpss(y)
        fragment = Tonal_Fragment(y_harmonic, sr)
        # fragment.chromagram(filename)
        
        self.key = max(fragment.key_dict, key=fragment.key_dict.get)
        logging.info("DONE!")
        logging.info("Detecting downbeats...")
        
        self.beats = extract_downbeats(song_filepath, mode="BeatNet")
        logging.info("DONE!")


    
    def get_key(self):
        return self.key
    
    def get_sections(self):
        return self.sections
    
    def __len__(self):
        return len(self.data)