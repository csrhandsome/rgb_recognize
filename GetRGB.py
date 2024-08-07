from PIL import Image
import cv2
import numpy as np
import os
import time
import shutil
import sys
from queue import LifoQueue

class GetRGB:
    
    def __init__(self, path):
        self.imgqueue=LifoQueue()
        self.cap = cv2.VideoCapture(1)
        self.path = path
        self.color_hop=32
        self.width=640
        self.height=480
        if os.path.isfile(self.path)==True:
            print(f'self.path is {self.path}')
            image=cv2.imread(self.path)
            cv2.imshow('RGB', image)
            self.imgqueue.put(image)
        else:
            for file in os.listdir(self.path):
                if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
                    image=cv2.imread(os.path.join(self.path, file))
                    self.imgqueue.put(image)
                    #os.remove(os.path.join(self.path, file))
            self.num_images = len(os.listdir(self.path))

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
                    img.save(os.path.join(self.path, f'rgb_{r}_{g}_{b}.jpg'))
                    print(f'Creating RGB image with R={r}, G={g}, B={b}')

    def get_rgb(self):
        image = self.imgqueue.get(timeout=1)
        cv2.imshow('color image', image)
        image = image.convert('RGB')
        width, height = image.size
        image = np.array(image)
        cv2.imshow('color image', image)
        for x in range(width):
            for y in range(height):
                r, g, b = image.getpixel((x, y))
                print(f"Pixel at ({x}, {y}): R={r}, G={g}, B={b}")
        

if __name__ == '__main__':
    getrgb=GetRGB('img')
    getrgb.create_rgb_image()

