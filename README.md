## keyplay
### Function
keyplay: to play rhythm by keyboard input, when you code or typing.

该程序启动后会监控用户键盘事件，当用户在写代码或者打字的时候会根据键盘输入的字符来生成旋律并播放，以达到编写代码或者是边打字边听音乐的效果。

- 监控用户键盘事件并生成旋律 -已实现
- 依靠musicpy提取midi歌曲之中的主旋律 -已实现
- 读取代码文件并生成旋律 -待实现
- 可切换为终端字符显示钢琴进行演奏 -待实现 

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
# 通过外部脚本运行
python run.py
# 通过模块包来运行
python -m keyplay
```
