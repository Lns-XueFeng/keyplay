from pynput.keyboard import Key


key_all_note = {
    Key.f1: "C2",
    Key.f2: "D2",
    Key.f3: "E2",
    Key.f4: "F2",
    Key.f5: "G2",
    Key.f6: "A2",
    Key.f7: "B2",
    Key.f8: "C3",
    Key.f9: "D3",
    Key.f10: "E3",
    Key.f11: "F3",
    Key.f12: "G3",
    Key.print_screen: "A3",
    Key.delete: "B3",
    "`": "C7",
    "1": "C2",
    "2": "D2",
    "3": "E2",
    "4": "F2",
    "5": "G2",
    "6": "A2",
    "7": "B2",
    "8": "C3",
    "9": "D3",
    "0": "E3",
    "-": "C7",
    "=": "C7",
    Key.backspace: "C7",
    Key.page_up: "C7",
    Key.tab: "C7",
    "q": "F3",
    "w": "G3",
    "e": "A3",
    "r": "B3",
    "t": "C4",
    "y": "D4",
    "u": "E4",
    "i": "F4",
    "o": "G4",
    "p": "A4",
    "[": "C4",
    "]": "D4",
    "\\": "E4",
    Key.page_down: "F4",
    Key.caps_lock: "G4",
    "a": "B4",
    "s": "C5",
    "d": "D5",
    "f": "E5",
    "g": "F5",
    "h": "G5",
    "j": "A5",
    "k": "B5",
    "l": "C6",
    ";": "C7",
    "'": "C7",
    Key.enter: "C7",
    Key.home: "C7",
    Key.shift: "C7",
    "z": "D6",
    "x": "E6",
    "c": "F6",
    "v": "G6",
    "b": "A6",
    "n": "B6",
    "m": "C7",
    ",": "C7",
    ".": "C7",
    "/": "C6",
    Key.shift_r: "D6",
    Key.up: "E6",
    Key.end: "F6",
    Key.ctrl_l: "G6",
    Key.cmd: "A6",
    Key.alt_l: "B6",
    Key.space: "C7",
    Key.alt_gr: "C4",
    Key.ctrl_r: "D4",
    Key.left: "E4",
    Key.down: "F4",
    Key.right: "G4",
}

# 25键钢琴
key_small_note = {
    "w": "C4",
    "e": "D4",
    "r": "E4",
    "t": "F4",
    "y": "G4",
    "u": "A4",
    "i": "B4",
    "s": "C5",
    "d": "D5",
    "f": "E5",
    "g": "F5",
    "h": "G5",
    "j": "A5",
    "k": "B5",

    "1": "C#4",
    "2": "D#4",
    "3": "F#4",
    "4": "G#4",
    "5": "A#4",
    "6": "C#5",
    "7": "D#5",
    "8": "F#5",
    "9": "G#5",
    "0": "A#5",
}

sounds_dict = {
    "a": "asound.mp3",
    "b": "bsound.mp3",
    "c": "csound.mp3",
    "d": "dsound.mp3",
    "e": "esound.mp3",
    "f": "fsound.mp3",
    "g": "gsound.mp3",
    "h": "hsound.mp3",
    "i": "isound.mp3",
    "j": "jsound.mp3",
    "k": "ksound.mp3",
    "l": "lsound.mp3",
    "m": "msound.mp3",
    "n": "nsound.mp3",
    "o": "osound.mp3",
    "p": "psound.mp3",
    "q": "qsound.mp3",
    "r": "rsound.mp3",
    "s": "ssound.mp3",
    "t": "tsount.mp3",
    "u": "usound.mp3",
    "v": "vsound.mp3",
    "w": "wsound.mp3",
    "x": "xsound.mp3",
    "y": "ysound.mp3",
    "z": "zsound.mp3",
    Key.f1: "asound.mp3",
    Key.f2: "bsound.mp3",
    Key.f3: "csound.mp3",
    Key.f4: "dsound.mp3",
    Key.f5: "esound.mp3",
    Key.f6: "fsound.mp3",
    Key.f7: "gsound.mp3",
    Key.f8: "hsound.mp3",
    Key.f9: "isound.mp3",
    Key.f10: "jsound.mp3",
    Key.f11: "ksound.mp3",
    Key.f12: "lsound.mp3",
    Key.print_screen: "msound.mp3",
    Key.delete: "nsound.mp3",
    "`": "osound.mp3",
    "1": "asound.mp3",
    "2": "bsound.mp3",
    "3": "csound.mp3",
    "4": "dsound.mp3",
    "5": "esound.mp3",
    "6": "fsound.mp3",
    "7": "gsound.mp3",
    "8": "hsound.mp3",
    "9": "isound.mp3",
    "0": "zsound.mp3",
    "-": "ksound.mp3",
    "=": "lsound.mp3",
    Key.backspace: "msound.mp3",
    Key.page_up: "nsound.mp3",
    Key.tab: "osound.mp3",
    "[": "psound.mp3",
    "]": "qsound.mp3",
    "\\": "rsound.mp3",
    Key.page_down: "ssound.mp3",
    Key.caps_lock: "tsound.mp3",
    Key.enter: "usound.mp3",
    Key.home: "vsound.mp3",
    Key.shift: "wsound.mp3",
    Key.shift_r: "xsound.mp3",
    Key.up: "ysound.mp3",
    Key.end: "zsound.mp3",
    "key": "ztsound.mp3",
    "key": "zusound.mp3",
    "key": "zvsound.mp3",
    "key": "zwsound.mp3",
    "key": "zxsound.mp3",
    "key": "zysound.mp3",
    Key.ctrl_l: "ztsound.mp3",
    Key.cmd: "ztsound.mp3",
    Key.alt_l: "zusound.mp3",
    Key.space: "zwsound.mp3",
    Key.alt_gr: "zxsound.mp3",
    Key.ctrl_r: "zysound.mp3",
    Key.left: "ztsound.mp3",
    Key.down: "zusound.mp3",
    Key.right: "zwsound.mp3",
}
