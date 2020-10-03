import tkinter
import cv2
import PIL.Image, PIL.ImageTk

class App:
    #windowの作成と描画
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        # open video source
        #カメラ画像の取得
        self.vid = MyVideoCapture(video_source)

        # Create a canvas that can fit the above video source size
        #画像サイズに合わせたcanvasの作成
        # self.canvas = tkinter.Canvas(window, width=self.vid.width, height=self.vid.height)
        self.canvas = tkinter.Canvas(window, width=1280, height=self.vid.height)
        print(self.vid.width)
        print(self.vid.height)
        self.canvas.pack()

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
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
            self.canvas.create_image(640, 0, image=self.photo, anchor=tkinter.NW)

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


