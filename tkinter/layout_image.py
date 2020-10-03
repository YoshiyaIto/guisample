from tkinter import *
from tkinter import ttk
import urllib.request as req
import tkinter as tk
from PIL import Image, ImageTk

#window
root = Tk()
root.minsize(width=1000, height=500)
#frame
#topframe
frame = ttk.Frame(root, padding=10)

#subframe
frame2 = ttk.Frame(
    frame, width=450, height=500,
    borderwidth=10, relief='sunken')
frame3 = ttk.Frame(
    frame, width=450, height=500,
    borderwidth=10, relief='sunken')

#picture
canvas = tk.Canvas(frame)
# PILでjpgを使用
img1 = Image.open(open('luccica_0.jpg', 'rb'))
img1.thumbnail((400, 400), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)  # 表示するイメージを用意

canvas.create_image(  # キャンバス上にイメージを配置
    0,  # x座標
    0,  # y座標
    image=img1,  # 配置するイメージオブジェクトを指定
    tag="illust",  # タグで引数を追加する。
    anchor=tk.NW  # 配置の起点となる位置を左上隅に指定
)



frame.pack()
frame2.grid(row=0, column=0)
frame3.grid(row=0, column=1)
canvas.grid(row=0, column=0, sticky=tk.NSEW)

root.mainloop()