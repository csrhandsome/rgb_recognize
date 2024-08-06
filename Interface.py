import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from GetRGB import GetRGB
def drop(event):
    # 处理拖放的文件路径
    file_path = event.data
    print("Dropped file:", file_path)
    getrgb=GetRGB(file_path)
    getrgb.get_rgb()

root = TkinterDnD.Tk()
root.title("Drag and Drop Example")
root.geometry("800x600")  # 设置窗口的初始大小
# 创建一个文本标签，用于显示拖放的文件路径
label = tk.Label(root, text="Drag a photo here", bg="white", fg="black", font=("Helvetica", 16))
label.place(x=0, y=0, width=800, height=600)  # 设置标签的位置和大小
# 绑定拖放事件
label.drop_target_register(DND_FILES)
label.dnd_bind('<<Drop>>', drop)
root.mainloop()
