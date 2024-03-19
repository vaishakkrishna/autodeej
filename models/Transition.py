from .Song import Song
from models.enums import TransitionType 
from __future__ import annotations

class Transition:
    song_from: Song
    song_to: Song
    # start/end times of transitions in ms
    song_from_end_time: int
    song_to_start_time: int
    # transition type
    transition_type: TransitionType = TransitionType.XFADE
    # transition length (bars) 
    transition_length: int
    
    
    def __init__(self, 
                 song_from: Song,
                 song_to: Song,
                 song_from_end_time: int,
                 song_to_start_time: int,
                 transition_length: int, 
                 transition_type: TransitionType = TransitionType.XFADE) -> None:
        self.song_from = song_from
        self.song_to = song_to
        self._process_transition()
    
    @staticmethod
    def from_songs(song_from: Song, song_to: Song):
        return Transition(song_from, song_to, len(song_from), len(song_to), 
                          0, TransitionType.NONE)