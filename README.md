## keyplay
### Function
keyplay: to play rhythm by keyboard input, when you code or typing.

该程序启动后会监控用户键盘事件，当用户在写代码或者打字的时候会根据键盘输入的字符来生成旋律并播放，以达到编写代码或者是边打字边听音乐的效果。

- 监控用户键盘事件达到随敲随听的效果 -已实现
- 可切换为终端25键字符钢琴进行演奏 -已实现
- 基于musicpy提取midi歌曲之中的主旋律 -已实现
- 基于musicpy提取midi歌曲之中的和弦 -已实现
- 将你的代码生成为音乐旋律 -已实现
- 提供一个函数播放midi音乐文件 - 已实现

### Usage
#### 1.克隆项目
```bash
# 克隆keyplay
git clone https://github.com/Lns-XueFeng/keyplay.git
```

#### 2.安装依赖
```bash
# 进入项目目录
cd keyplay
# 创建虚拟环境
python -m venv venv
# powershell下激活虚拟环境
./venv/Scripts/activate.ps1
# 安装依赖
pip install -r requirements.txt
```

#### 3.运行程序
```bash
cd keyplay
python easy_to_run.py
```

#### 4.程序截图
主程序界面：
<img src="./screenshot/keyplay.png" alt="keyplay" title="keyplay">
程序模式一：
<img src="./screenshot/keyplay_mode1.png" alt="keyplay_mode1" title="keyplay_mode1">
程序模式二：
<img src="./screenshot/keyplay_mode2.png" alt="keyplay_mode2" title="keyplay_mode2">
程序模式三：
<img src="./screenshot/keyplay_mode3.png" alt="keyplay_mode3" title="keyplay_mode3">
