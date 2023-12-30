from musicpy import N, play, chord


def play_note(note_name):
    """
    Plays a note.

    Parameters
    note_name : str
        The name of the note to play.
    """
    if note_name != "":
        play(N(note_name), wait=True)
    else:
        print(f'Current key not define note')


def  play_chord(notes, interval=0.2, duration=2, bpm=120):
    """
    Plays a list of notes.

    Parameters
    notes: list
        A list of notes to play.
    interval: float
        The interval of the note in notes.
    duration: int
        The duration of the note in seconds.
    bpm: int, optional
        The bpm of the note, in beats per minute. The default is 120.
    """
    if notes:
        play(chord(notes, interval=interval, duration=duration), 
            bpm=bpm, 
            wait=True)
    else:
        print(f'Please input vaild key')
