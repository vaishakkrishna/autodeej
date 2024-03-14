import librosa

def extract_tempo_and_beats(song_filename: str):
    y, sr = librosa.load(song_filename)
    # Run the default beat tracker
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    print(f'Estimated tempo: {tempo} beats per minute')

    # Convert the frame indices of beat events into timestamps
    return tempo, librosa.frames_to_time(beat_frames, sr=sr)