# read midi file and convert it into rhythm
# read code file and convert it into a rhythm
import os

from musicpy import read, play, write, chord

from keyplay.map import key_all_note


midi_dir = "./midi/"
MELODY = "melody_"
RHYTHM = "rhythm_"
CHORD = "chord_"


def split_as_melody(midifile):
    """ 
    Split a midi file into a melody 

    Parameters
    midifile: str
        midifile is a midi file
    """
    a, bpm, start_time = read(midifile).merge()
    melody = a.split_melody(mode='chord')

    if not os.path.exists(midi_dir):
        os.mkdir(midi_dir)
    temp_file = midifile.split("/")[-1]
    final_file = midi_dir + MELODY + temp_file
    write(melody, name=final_file, save_as_file=True, bpm=bpm)


def split_as_chord(midifile):
    """ 
    Split a midi file into a chord 

    Parameters
    midifile: str
        midifile is a code file
    """
    a, bpm, start_time = read(midifile).merge()
    chord = a.split_chord(mode='chord')
    
    if not os.path.exists(midi_dir):
        os.mkdir(midi_dir)
    temp_file = midifile.split("/")[-1]
    final_file = midi_dir + CHORD + temp_file
    write(chord, name=final_file, save_as_file=True, bpm=bpm)


def convert(codefile):
    """ 
    Convert a code file into a rhythm, code into music

    Parameters
    orgin_file: str
        orgin_file is a code file
    """
    with open(codefile, 'r', encoding='utf-8') as fp:
        code = fp.read()

    note_list = []
    for c in code:
        n = key_all_note.get(c, "")
        if n != "":
            note_list.append(n)
    
    if not os.path.exists(midi_dir):
        os.mkdir(midi_dir)
    
    temp_file = codefile.split("/")[-1]
    final_file = midi_dir + RHYTHM + temp_file + ".mid"
    write(chord(note_list, interval=0.2, duration=2), 
        name=final_file, 
        save_as_file=True,
        bpm=120)
    

def listen_midi(filename):
    """ 
    Play a midi file

    Parameters
    filename: str
        filename is a midi file
    """
    play(read(filename), wait=True, save_as_file=False)


split_as_melody("./midi/torikago.mid")
split_as_chord("./midi/torikago.mid")
convert("bind.py")
# listen_midi("bind.mid")
