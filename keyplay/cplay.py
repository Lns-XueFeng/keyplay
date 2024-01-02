import os

from musicpy import read, play, write, chord

from keyplay.map import key_all_note


"""cplay.py
这个模块提供了从midi音乐文件中分离出主旋律和和弦的函数、
提供将基于用户提供的代码文件进行转换与生成midi旋律音乐的函数、提供了一个播放midi音乐的函数
"""


"""convert函数:
目前仅是一个实验性质的功能，仅是遍历代码文件中的字符转换得到音符
随着研究乐理，后续会丰富逻辑，尽量实现有节奏、韵律、好听的音乐
"""


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
    try:
        a, bpm, start_time = read(midifile).merge()
        melody = a.split_melody(mode='chord')

        if not os.path.exists(midi_dir):
            os.mkdir(midi_dir)
            
        temp_file = midifile.split("/")[-1]
        final_file = midi_dir + MELODY + temp_file
        write(melody, name=final_file, save_as_file=True, bpm=bpm)
        print("在当前目录生成完毕")
    except Exception as e:
        print(f"Error: {e}")


def split_as_chord(midifile):
    """ 
    Split a midi file into a chord 

    Parameters
    midifile: str
        midifile is a code file
    """
    try:
        a, bpm, start_time = read(midifile).merge()
        chord = a.split_chord(mode='chord')
        
        if not os.path.exists(midi_dir):
            os.mkdir(midi_dir)
    
        temp_file = midifile.split("/")[-1]
        final_file = midi_dir + CHORD + temp_file
        write(chord, name=final_file, save_as_file=True, bpm=bpm)
        print("在当前目录生成完毕")
    except Exception as e:
        print(f"Error: {e}")


def convert(codefile):
    """ 
    Convert a code file into a rhythm, code into music

    Parameters
    orgin_file: str
        orgin_file is a code file
    """
    try:
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
        print("在当前目录生成完毕")
    except Exception as e:
        print(f"Error: {e}")


def listen_midi(filename):
    """ 
    Play a midi file

    Parameters
    filename: str
        filename is a midi file
    """
    try:
        play(read(filename), wait=True, save_as_file=False)
        print("播放完毕")
    except Exception as e:
        print(f"Error: {e}")


def look_functions():
    print("\033c", end="")
    print("函数1: 运行`split_as_melody`从一个midi音乐文件中分离出主旋律")
    print("函数2: 运行`split_as_chord`从一个midi音乐文件中分离出和弦")
    print("函数3: 运行`convert`将一个代码文件转化生成为midi音乐文件")
    print("函数4: 运行`listen_midi`可以播放一个midi音乐文件")
    print("输入`q`可以退出子程序")
    while True:
        mode = input("请选择一个模式数字(1-4):")
        if mode == "1":
            midifile = input("请输入一个midi文件路径:")
            split_as_melody(midifile)
        elif mode == "2":
            midifile = input("请输入一个midi文件路径:")
            split_as_chord(midifile)
        elif mode == "3":
            codefile = input("请输入一个代码文件路径:")
            convert(codefile)
        elif mode == "4":
            midifile = input("请输入一个midi文件路径:")
            listen_midi(midifile)
        elif mode == "q":
            print("成功退出子程序")
            break
        else: 
            print("模式数字不在(1, 2, 3, 4)之中, 请再次尝试...")


if __name__ == "__mian__":
    split_as_melody("./midi/torikago.mid")
    split_as_chord("./midi/torikago.mid")
    convert("bind.py")
    listen_midi("bind.mid")
