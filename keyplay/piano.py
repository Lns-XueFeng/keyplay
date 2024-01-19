from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor

import numpy as np
from pynput import keyboard
from pynput.keyboard import Key

from keyplay.play import play_note
from keyplay.map import key_small_note as key_note
from keyplay.ascii import ascii_piano


"""piano.py
这个模块可以在终端模拟一个25键的字符钢琴, 随着用户键盘对应键的按下而按下释放而释放, 
当按下时便会播放对应的音符, 此模块目前还不支持多键同时按下, 后续会进行优化
"""


wkey_dict = {"w": (0, 5), "e": (5, 10), "r": (10, 15), "t": (15, 20), 
            "y": (20, 25), "u": (25, 30), "i": (30, 35), "s": (35, 40), 
            "d": (40, 45), "f": (45, 50), "g": (50, 55), 
            "h": (55, 60), "j": (60, 65), "k": (65, 70)}

bkey_dict = {"1": (3, 7), "2": (8, 12), "3": (18, 22), "4": (23, 27), 
            "5": (28, 32), "6": (38, 42), "7": (43, 47), "8": (53, 57), 
            "9": (58, 62), "0": (63, 67)}


def show_piano(piano_matrix):
    for r in piano_matrix:
        for c in r:
            print(c, end="")
        print("")


def gen_marix():
    com_piano = []
    for line in ascii_piano.split("\n"):
        if len(line) == 0:
            continue
        splited_piano = []
        for c in line:
            splited_piano.append(c)
        com_piano.append(splited_piano)
    return np.array(com_piano)


piano_matrix = gen_marix()
copy_piano_matrix = np.copy(piano_matrix)
executor = ThreadPoolExecutor(max_workers=10)
lock = Lock()


def change_pianowkey(start, end, c1, c2):
    with lock:
        copy_piano_matrix = np.copy(piano_matrix)
        index_row = 0
        for r in piano_matrix:
            index_col = start
            for c in r[start:end]:
                if c == c1:
                    copy_piano_matrix[index_row][index_col] = c2
                index_col = index_col + 1
            index_row = index_row + 1
        return copy_piano_matrix


def change_pianobkey(start, end, c1, c2):
    with lock:
        copy_piano_matrix = np.copy(piano_matrix)
        index_row = 0
        for r in piano_matrix[:8]:
            index_col = start
            for c in r[start:end]:
                if c == c1:
                    copy_piano_matrix[index_row][index_col] = c2
                index_col = index_col + 1
            index_row = index_row + 1
        return copy_piano_matrix


def piano_keydown(key):
    """ 模拟字符钢琴的key键被按下 """
    print("\033c", end="")
    for k, v in wkey_dict.items():
        if key == k:
            try:
                changed_piano_marix = change_pianowkey(v[0], v[1], " ", "█")
                show_piano(changed_piano_marix)
            except IndexError:
                pass

            play_note(key_note.get(key))
            break
  
    for k, v in bkey_dict.items():
        if key == k:
            try:
                changed_piano_marix = change_pianobkey(v[0], v[1], "█", " ")
                show_piano(changed_piano_marix)
            except IndexError:
                pass

            play_note(key_note.get(key))
            break


def piano_keyup(key):
    """ 模拟字符钢琴的key键被释放 """
    print("\033c", end="")
    show_piano(piano_matrix)


def on_press(key):
    try:
        if key.char in wkey_dict or key.char in bkey_dict:
            executor.submit(piano_keydown, key.char)
    except AttributeError:
        pass


def on_release(key):
    try:
        if key.char in wkey_dict or key.char in bkey_dict:
            executor.submit(piano_keyup, key.char)
    except AttributeError:       
        if key == Key.esc:
            return False


def bind():
    with keyboard.Listener(
        on_press=on_press, 
        on_release=on_release) as listener:
        listener.join()


def run_asciipiano():
    print("\033c", end="")
    show_piano(copy_piano_matrix)
    print("程序正在运行中, 您可通过键盘按键来演奏25键字符钢琴, 产生美妙的旋律")
    print("按下esc键可以退出子程序")
    bind()
