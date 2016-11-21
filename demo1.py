# coding:utf-8

from Tkinter import *
import tkMessageBox
import urllib
import json
import mp3play
import time


music_list = []  # 用于收集歌曲播放地址


def music():
    name = entry.get()
    name = urllib.quote(name.encode('utf-8'))
    if not name:
        tkMessageBox.showinfo('Tips:', '请输入歌曲名！')
        return
    html = urllib.urlopen('http://s.music.163.com/search/get/?type=1&s=%s&limit=9' % name).read()  # 从网易音乐上搜索音乐
    text = json.loads(html)  # 将html由字符串转换成字典
    list_songs = text['result']['songs']
    for i in range(len(list_songs)):
        listbox.insert(i, list_songs[i]['name'] + '(' + list_songs[i]['artists'][0]['name'] + ')')  # 将结果加入到搜索列表中
        music_list.append(list_songs[i]['audio'])  # 收集歌曲播放地址


def play_music(event):
    index = listbox.curselection()[0]
    music_url = music_list[index]
    urllib.urlretrieve(music_url, '1.mp3')
    mp3 = mp3play.load('1.mp3')
    mp3.play()
    time.sleep(mp3.seconds())  # 设置播放时间

root = Tk()  # 创建一个窗口
root.title("Leo's Music-Box")  # change the window's tile
root.geometry("320x260+500+200")  # 'x' 窗口的大小, '+' 窗口的位置
entry = Entry(root)  # 创建输入窗口
entry.pack()  # grid = 网格布局
button = Button(root, text="搜  索", command=music)  # 创建按钮
button.pack()
var = StringVar()
listbox = Listbox(root, width=50, listvariable=var)  # 列表
listbox.bind('<Double-Button-1>', play_music)  # 绑定鼠标双击动作
listbox.pack()
Label(text="Thanks for using My Music-Box", fg='red').pack()
root.mainloop()  # 运行窗口 一个循环发送消息的进程
