def run():
    while True:
        print("\033c", end="")
        print("欢迎使用KeyPlay, 它有三个模式") 
        print("请选择一个模式(1是随敲随听, 2是模拟钢琴, 3是一些实用函数)")
        print("模式1: 当你在写代码或者是打字时产生相对应的旋律达到随敲随听效果")
        print("模式2: 在终端中模拟一个25键字符钢琴, 你可以通过键盘来对它进行演奏")
        print("模式3: 提供从midi音乐文件中分离出主旋律或和弦的功能、将代码文件转换为旋律音乐的功能、一个播放midi音乐的功能")
        print("输入`q`可以退出主程序")
        mode = input("请选择一个模式数字(1-3):")
        if mode == "1":
            from keyplay.bind import run_keymonitor
            run_keymonitor()
            print("成功退出子程序")
        elif mode == "2":
            from keyplay.piano import run_asciipiano
            run_asciipiano()
            print("成功退出子程序")
        elif mode == "3":
            from keyplay.cplay import look_functions
            look_functions()
            print("成功退出子程序")
        elif mode == "q":
            print("成功退出主程序, 欢迎下次使用！")
            break
        else:
            print("模式数字不在(1, 2, 3)之中, 请再次尝试...")
