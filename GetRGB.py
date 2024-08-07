from PIL import Image
import cv2
import numpy as np
import os
import time
import shutil
import sys
from queue import LifoQueue
temp_img=0
def mouse_callback(event, x, y, flags, param):
    global temp_img
    canvas = temp_img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True#按下鼠标开始画画
        ix, iy = x, y
        r, g, b = canvas[y, x]
        print(f"Pixel at ({x}, {y}): R={r}, G={g}, B={b}")

class GetRGB:
    def __init__(self, path):
        self.imgqueue=LifoQueue()
        self.cap = cv2.VideoCapture(1)
        self.path = path
        self.color_hop=32
        self.width=640
        self.height=480
        self.num_images = 0
        self.load_image(path)
        self.temp_img=0
        
   
   
    def load_image(self,path):
        if path.endswith('.jpg') or path.endswith('.png') or path.endswith('.jpeg'):
            if os.path.isfile(path)==True:
                image=cv2.imread(path)
                self.imgqueue.put(image)
            else:
                for file in os.listdir(path):
                        image=cv2.imread(os.path.join(path, file))
                        self.imgqueue.put(image)
                        self.num_images = len(os.listdir(self.path))
                        #os.remove(os.path.join(path, file))
        else:
            print('Please input a image file')

    def create_rgb_image(self):
        for r in range(0,257,self.color_hop):
            for g in range(0,257,self.color_hop):
                for b in range(0,257,self.color_hop):
                    if r==256 :
                        r=255
                    elif g==256 :
                        g=255
                    elif b==256 :
                        b=255
                    img = Image.new('RGB', (self.width, self.height), (r, g, b))
                    img.save(os.path.join(self.path, f'{r}_{g}_{b}.jpg'))
                    print(f'Creating RGB image with R={r}, G={g}, B={b}')

    def get_rgb(self):
        image = self.imgqueue.get(timeout=1)
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.temp_img=image.copy()
        global temp_img
        temp_img=image.copy()
        cv2.namedWindow('color_picker')
        cv2.setMouseCallback('color_picker', mouse_callback)
        # 显示图片
        while True:
            cv2.imshow('color_picker', image)#名字一样可以同步成一个画布
            if cv2.waitKey(1) & 0xFF == 27:  # 按下 ESC 键退出
                break
        # 销毁所有窗口
        cv2.destroyAllWindows() 

        

if __name__ == '__main__':
    getrgb=GetRGB('img')
    getrgb.create_rgb_image()

