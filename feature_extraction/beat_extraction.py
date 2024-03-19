from typing import Literal
import librosa
from BeatNet.BeatNet import BeatNet
from madmom.features.downbeats import RNNDownBeatProcessor, DBNDownBeatTrackingProcessor
import numpy as np

def extract_downbeats(song_filename: str, mode:Literal["madmom_RNN", "BeatNet"]="BeatNet") -> np.array:
    '''Extracts times of downbeats in ms from start of song.

    :param song_filename: path to song
    :type song_filename: str
    :param mode: _description_, defaults to "BeatNet"
    :type mode: Literal[&quot;madmom_RNN&quot;, &quot;BeatNet&quot;], optional
    :return: Array of beat times
    :rtype: _type_
    '''    
    if mode == "BeatNet":
        estimator = BeatNet(1, mode='offline', inference_model='DBN', plot=[])
        stamps_and_beats = estimator.process(song_filename)
    elif mode == "madmom_RNN":
        res = RNNDownBeatProcessor()(song_filename)

        proc = DBNDownBeatTrackingProcessor(beats_per_bar=[4], fps=100, correct=True)
        stamps_and_beats = proc(res)
    
    stamps, beats = stamps_and_beats[:, 0], stamps_and_beats[:, 1]
    stamps = stamps[beats == 1]
    return stamps * 1000

def extract_beats(song_filename: str, mode:Literal["madmom_RNN", "BeatNet", "librosa"]="librosa") -> np.array:
    '''Extracts timestamps of the beats of a song in ms

    :param song_filename: path to song file (mp3)
    :type song_filename: str
    :param mode: _description_, defaults to "librosa"
    :type mode: Literal[&quot;madmom_RNN&quot;, &quot;BeatNet&quot;, &quot;librosa&quot;], optional
    :return: array of beat timestamps in milliseconds
    :rtype: _type_
    '''    
    if mode == "librosa":
        return extract_beats_librosa(song_filename)
    
    elif mode == "BeatNet":
        return extract_beats_beatnet(song_filename)
    elif mode == "madmom":
        return extract_beats_madmom(song_filename)
    
    
def extract_beats_librosa(song_filename:str):
    y, sr = librosa.load(song_filename)
    print(sr)
    # Run the default beat tracker
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    print(f'Estimated tempo: {tempo} beats per minute')

    # Convert the frame indices of beat events into timestamps
    return librosa.frames_to_time(beat_frames, sr=sr)*1000

def extract_beats_beatnet(song_filename:str):
    estimator = BeatNet(1, mode='offline', inference_model='DBN', plot=[], thread=False)
    stamps_and_beats = estimator.process(song_filename)
    return stamps_and_beats[:, 0]*1000


def extract_beats_madmom(song_filename:str):
    proc = RNNDownBeatProcessor()
    res = proc(song_filename)
    proc = DBNDownBeatTrackingProcessor(beats_per_bar=[3,4], fps=100)
    stamps_and_beats = proc(res)
    return stamps_and_beats[:, 0]*1000