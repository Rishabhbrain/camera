import cv2
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog


class CameraApp:
    def __init__(self, window, cap):
        self.window = window
        self.cap = cap
        self.canvas = tk.Canvas(window, width=640, height=480)
        self.canvas.pack()
        self.btn_snapshot = tk.Button(window, text="Capture", command=self.snapshot)
        self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)

    def update_frame(self):
        _, frame = self.cap.read()
        self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(15, self.update_frame)

    def snapshot(self):
        _, frame = self.cap.read()
        filename = tk.filedialog.asksaveasfilename(defaultextension=".jpg")
        if filename:
            cv2.imwrite(filename, frame)

    def run(self):
        self.update_frame()
        self.window.mainloop()

cap = cv2.VideoCapture(0)
root = tk.Tk()
app = CameraApp(root, cap)
app.run()
cap.release()
