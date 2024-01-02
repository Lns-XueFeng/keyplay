from musicpy import N, play, chord


serial_number = """
    1.大钢琴         2.明亮的钢琴     3.电子大钢琴     4.酒吧钢琴      
    5.电子钢琴1      6.电子钢琴2      7.大键琴         8.克拉维科特    
    9.钢片琴         10.钟琴          11.八音盒        12.颤音琴       
    13.木琴          14.木片琴        15.管钟          16.扬琴         
    17.拉杆风琴      18.打击风琴      19.摇滚风琴      20.教堂风琴     
    21.簧风琴        22.手风琴        23.口琴          24.探戈手风琴   
    25.尼龙弦吉他    26.钢弦吉他      27.爵士电吉他    28.清音电吉他   
    29.弱音电吉他    30.过载吉他      31.失真吉他      32.吉他泛音     
    33.原声贝斯      34.指拨电贝斯    35.拨片电贝斯    36.无品贝斯     
    37.拍打贝斯1     38.拍打贝斯2     39.合成贝斯1     40.合成贝斯2    
    41.小提琴        42.中提琴        43.大提琴        44.低音提琴     
    45.颤音弦乐      46.拨弦弦乐      47.竖琴          48.定音鼓       
    49.弦乐合奏1     50.弦乐合奏2     51.合成弦乐1     52.合成弦乐2    
    53.人声“啊”      54.人声“哦”      55.合成人声      56.打击乐合奏   
    57.小号          58.长号          59. 大号         60.弱音小号     
    61.法国号        62.铜管乐器合奏  63.合成铜管1     64.合成铜管2    
    65.高音萨克斯    66.中音萨克斯    67.低音萨克斯    68.上低音萨克斯 
    69.双簧管        70.英国管        71.巴松管        72.黑管         
    73.短笛          74.长笛          75.竖笛          76.排箫         
    77.吹瓶          78.尺八          79.口哨          80.奥卡里纳     
    81.方波          82.锯齿波        83.呼叫          84.吹口哨       
    85.吉他          86.人声          87.五度          88.贝斯加主音   
    89.新世纪        90.温暖          91.多音合成      92.合唱         
    93.弓弦          94.金属          95.光环          96.扫掠         
    97.雨            98.声轨          99.水晶          100.大气        
    101.明亮         102.小精灵       103.回声         104.科幻        
    105.锡塔琴       106.班卓琴       107.三弦琴       108.十三弦琴    
    109.卡林巴       110.风笛         111.提琴         112.喇叭        
    113.铃铛         114.阿哥哥       115.钢鼓         116.木块        
    117.太鼓         118.旋律鼓       119.合成鼓       120.反向钹      
    121.吉他品格噪音  122.呼吸噪音     123.海浪声       124.鸟鸣        
    125.电话铃声     126.直升机       127.掌声         128.枪声  
"""


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
            play(chord(notes, interval=interval, duration=duration), 
                bpm=bpm, 
                instrument=1,
                wait=True)
        # else:
            # print("Please input vaild key")
