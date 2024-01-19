from musicpy import N, play, chord


def play_note(note_name):
    """
    Plays a note.

    Parameters
    note_name : str
        The name of the note to play.
    """
    if note_name != "":
        try:
            play(N(note_name, duration=1/4), 
                    instrument=1,
                    wait=False)
        except Exception as e:
            pass


def  play_chord(notes, lock, interval=0.2, duration=2, bpm=120):
    """
    Plays a list of notes.

    Parameters
    notes: list
        A list of notes to play.
    lock: threading.Lock
        A lock to control the thread.
    interval: float, optional
        The interval of the note in notes. The default is 0.2.
    duration: int, optional
        The duration of the note in seconds. The default is 2.
    bpm: int, optional
        The bpm of the note, in beats per minute. The default is 120.
    """
    with lock:
        if notes:
            try:
                play(chord(notes, interval=interval, duration=duration), 
                    bpm=120, 
                    instrument=47,
                    wait=True)
            except Exception as e:
                pass
