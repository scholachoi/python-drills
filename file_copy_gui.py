from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import shutil
import time

class FileApp:
    def __init__(self, master):
        self.header = ttk.Label(root, text = "Copy files modified in the last 24 hours")
        self.header.grid(row=0)

        self.src = StringVar()
        self.src.set("Choose a folder to check for new files")
        self.dst = StringVar()
        self.dst.set("Choose a folder to copy files into")

        self.src_label = ttk.Label(root, textvariable = self.src)
        self.src_label.grid(row=1, column=0, columnspan=2, sticky=W)

        self.browse1 = ttk.Button(root, text = "Browse", command = lambda: self.src.set(filedialog.askdirectory()))
        self.browse1.grid(row=1, column=3)                            

        self.dst_label = ttk.Label(root, textvariable = self.dst)
        self.dst_label.grid(row=2, column=0, columnspan=2, sticky=W)

        self.browse2 = ttk.Button(root, text = "Browse", command = lambda: self.dst.set(filedialog.askdirectory()))
        self.browse2.grid(row=2, column=3)
        
        ttk.Button(root, text = "Copy", command = self.copy).grid(row=3, column=1)
        ttk.Button(root, text = "Reset", command = self.clear).grid(row=3, column=2)
            
    def copy(self):             
        src = self.src.get()
        dst = self.dst.get()
        filesInSrc = os.listdir(src)
        for file in filesInSrc:
            fileModTime = os.path.getmtime(src+'/'+file)
            if time.time() - fileModTime <= 86400:
                shutil.copy2(src+'/'+file, dst)

    def clear(self):
        self.src.set("Choose a folder to check for new files")
        self.dst.set("Choose a folder to copy files into")
        
                

if __name__ == "__main__":
    root = Tk()
    app = FileApp(root)
    root.title("Copy New Files")
    root.mainloop()
    
    
