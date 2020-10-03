import tkinter as tk
from PIL import Image, ImageTk
import urllib.request as req
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk

#tkinterのメイン
root = tk.Tk()

root.geometry('1200x560')
root.title('IMG')

canvas = tk.Canvas(
    root,  # 親要素をメインウィンドウに設定
    width=1200,  # 幅を設定
    height=560  # 高さを設定
    # relief=tk.RIDGE  # 枠線を表示
    # 枠線の幅を設定
)

canvas.place(x=0, y=0)  # メインウィンドウ上に配置

#画像の描画
# PILでjpgを使用
img1 = Image.open(open('luccica_0.jpg', 'rb'))
img1.thumbnail((500, 500), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)  # 表示するイメージを用意

canvas.create_image(  # キャンバス上にイメージを配置
    0,  # x座標
    0,  # y座標
    image=img1,  # 配置するイメージオブジェクトを指定
    tag="illust",  # タグで引数を追加する。
    anchor=tk.NW  # 配置の起点となる位置を左上隅に指定
)

#canvas.get_tk_widget().grid(row=0, column=1)
#canvas.get_tk_widget().pack()

frame = ttk.Frame(root, padding=10)

#グラフの描画
#グラフの計算
x1 = np.linspace(0.0, 5.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
x2 = np.linspace(0.0, 3.0)
y2 = np.cos(2 * np.pi * x2) * np.exp(-x1)
# Figure instance
fig = plt.Figure()
# ax1
ax1 = fig.add_subplot(111)
ax1.plot(x1, y1)
ax1.set_title('line plot')
ax1.set_ylabel('Damped oscillation')

canvasg = FigureCanvasTkAgg(fig, master=root)  # Generate canvas instance, Embedding fig in root
#canvasg.draw()
#位置の調整
canvasg.get_tk_widget().grid(row=0, column=0)
canvasg.get_tk_widget().grid(row=0, column=1)

#描画
root.mainloop()