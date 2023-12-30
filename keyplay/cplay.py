# read midi file and convert it into rhythm
# read code file and convert it into a rhythm

from musicpy import read, play, write


def split(filename, savefile=False):
    """ 
    Split a midi file into a melody 

    Parameters
    filename: str
        filename is a midi file
    savefile: bool
        savefile is a boolean value, if True, save the file, if False, play the file 
    """
    a, bpm, start_time = read(filename).merge()
    melody = a.split_melody(mode='chord')
    if savefile:
        write(melody, bpm, name='example melody.mid')
    else:
        play(melody, bpm, name='example melody.mid')


def convert(filename, savefile=False):
    """ 
    Convert a code file into a rhythm, code into music

    Parameters
    filename: str
        filename is a code file
    savefile: bool
        savefile is a boolean value, if True, save the file, if False, play the file 
    """
    pass
