import librosa

def extract_beats_timestamps(song_filepath: str):
    y, sr = librosa.load(song_filepath)
    # Run the default beat tracker
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    print(f'Estimated tempo: {tempo} beats per minute')

    # Convert the frame indices of beat events into timestamps
    return librosa.frames_to_time(beat_frames, sr=sr)