from threading import Thread, Lock

from pynput import keyboard
from pynput.keyboard import Key

from keyplay.map import key_all_note as key_note
from keyplay.play import play_chord


"""bind.py
这个模块监控键盘输入，将输入的键符转换为音符并且合成成一个和弦进行播放,
其最终能呈现的效果是：当用户写代码或者打字时，会基于其输入的键符生成旋律并播放，
达到边听音乐编写代码或者是打字的效果，且音乐均基于用户的输入进行合成。
"""


class KeyStack:
    def __init__(self):
        self.stack = []

    def push(self, key):
        self.stack.append(key)

    def pop(self):
        if self.is_empty():
            return
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


class NoteChord:
    def __init__(self):
        self.note_chord = []

    def append(self, key):
        if key is None:
            return
    
        note = key_note.get(key, "")
        if note == "":
            return
        else:
            self.note_chord.append(key_note.get(key, ""))

    def clear(self):
        self.note_chord.clear()


class PlayQueue:
    def __init__(self):
        self.queue = []

    def get(self, key):
        self.queue.append(key)

    def put(self):
        if self.is_empty():
            return
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0
    

lock = Lock()
key_stack = KeyStack()
play_queue = PlayQueue()


def rhythm_play():
    nc = NoteChord()
    while not key_stack.is_empty():
        key_release = key_stack.pop()
        nc.append(key_release)

    thread = Thread(target=play_chord, args=(nc.note_chord,lock,))
    thread.start()


def on_press(key):
    try:
        key_stack.push(key.char)
    except AttributeError:
        key_stack.push(key)


def on_release(key):
    if key == "." or key == ";":
        rhythm_play()
    elif key == Key.enter:
        rhythm_play()  
    elif key == Key.esc:
        return False


def show_key_to_note():
    print("\033c", end="")
    # print("以下是所有键盘的键对应的音符:")
    # for k, v in key_note.items():
    #     if v != "":
    #         print(f"key:{k} => note:{v}")
    print("该程序启动后, 将该程序挂于后台, 便可与随心所欲的去敲代码或打字, 享受边敲边听的乐趣")
    print("按下esc键可以退出子程序")


def bind():
    with keyboard.Listener(
        on_press=on_press, 
        on_release=on_release) as listener:
        listener.join()


def run_keymonitor():
    show_key_to_note()
    bind()
