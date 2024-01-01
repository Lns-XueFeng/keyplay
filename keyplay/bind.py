from threading import Thread, Lock

from pynput import keyboard
from pynput.keyboard import Key

from keyplay.map import key_all_note as key_note
from keyplay.play import play_chord


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
    else:
        print("record a key to note")


def show_in_terminal():
    print("Welecome to the keyplay:")
    print("keyplay aim to play music when you are playing the keyboard")
    print("it is has defined all the key map:")
    for k, v in key_note.items():
        if v != "":
            print(f"key:{k} => note:{v}")
    print("when you code or write passage, you can get a rhythm by press")
    print("press esc to exit")


def bind():
    with keyboard.Listener(
        on_press=on_press, 
        on_release=on_release) as listener:
        listener.join()
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()


def run():
    show_in_terminal()
    bind()
