import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D # ３Dグラフ作成のため

class App:
    #windowの作成と描画
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        # self.fig = plt.Figure()
        # self.ax1 = self.fig.add_subplot(111)

        # open video source
        #カメラ画像の取得
        self.vid = MyVideoCapture(video_source)
        # Create a canvas that can fit the above video source size
        #画像サイズに合わせたcanvasの作成
        self.canvas = tkinter.Canvas(window, width=640, height=self.vid.height)
        self.canvas2 = tkinter.Canvas(window, width=640, height=self.vid.height)
        #self.canvas.pack(side=tkinter.LEFT)
        #self.canvas2.pack(side=tkinter.LEFT)
        self.canvas.grid(column=0,row=0)
        self.canvas2.grid(column=1,row=0)
        #graph camvasの配置
        self.fig = plt.figure()  # figureオブジェクトを作る
        self.ax = Axes3D(self.fig)
        self.canvasg = FigureCanvasTkAgg(self.fig, master=self.canvas2)  # Generate canvas instance, Embedding fig in root
        # 位置の調整
        self.canvasg.get_tk_widget().pack(side=tkinter.RIGHT,
                                     expand=True,
                                     anchor=tkinter.E)

        # close button
        def f_close(event):
            window.destroy()
        frame = tkinter.Frame(window)
        button = tkinter.Button(frame, text='Close')
        button.grid(row=0, column=10, padx=5, sticky='e')
        button.bind('<Button-1>', f_close)
        #frame.pack(side=tkinter.BOTTOM)
        frame.grid(column=1,row=1)

        # After it is called once, the update method will be automatically called every delay milliseconds
        #self.delay = 15
        self.delay = 0
        self.update()

        self.window.mainloop()

    #更新
    def update(self):
        #ここに繰り返したい処理を書く
        # Get a frame from the video source
        #ビデオ情報からフレーム番号の取得
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
            #self.canvas2.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

            #makegraph
            #グラフの変数代入
            x = np.arange(0, 10, 1)  # 0 ~ 10 の１次元配列
            y = np.arange(0, 10, 1)  # 0 ~ 10 の１次元配列
            z = np.random.rand(10)  # 0 ~ 10 の１次元乱数配列
            self.ax.cla()
            self.ax.plot(x, y, z)
            #graph camvasの再配置
            self.canvasg.draw()
        self.window.after(self.delay, self.update)

#opencvを使ったカメラ画像の取得と画像のデータの取得
class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
        # Get video source width and height
        #画像の縦横の取得
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # Release the video source when the object is destroyed
    #クリーンアップ
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
        self.window.mainloop()
    #フレーム番号の取得
    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

#実行
App(tkinter.Tk(), "Tkinter and OpenCV")


