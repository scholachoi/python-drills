from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import shutil
import time
import datetime
import sqlite3

conn = sqlite3.connect('filecheck.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS filecheck(ID INTEGER PRIMARY KEY, LastCopied TIMESTAMP)')

create_table()

def insert_data():
    c.execute('INSERT INTO filecheck(LastCopied) VALUES(?)', (datetime.datetime.now().replace(microsecond=0),))
    conn.commit()
    

def last_filecheck():
    c.execute('SELECT LastCopied FROM filecheck ORDER BY LastCopied DESC LIMIT 1')
    return c.fetchone()[0]
    
    
class FileApp:
    def __init__(self, master):

        ttk.Label(root, text = "Copy files modified in the last 24 hours").grid(row=0)
        ttk.Label(root, text = "Last checked date/time: ").grid(row=1, column=0, sticky=W)

        self.lastcheck = StringVar()
        try:
            self.lastcheck.set(last_filecheck())
        except:
            self.lastcheck.set("No data in database")
        ttk.Label(root, textvariable = self.lastcheck).grid(row=1, column=2)
        
        
        
        self.src = StringVar()
        self.src.set("Choose a folder to check for new files")
        self.dst = StringVar()
        self.dst.set("Choose a folder to copy files into")

        self.src_label = ttk.Label(root, textvariable = self.src)
        self.src_label.grid(row=2, column=0, sticky=W)

        self.browse1 = ttk.Button(root, text = "Browse", command = lambda: self.src.set(filedialog.askdirectory()))
        self.browse1.grid(row=2, column=2)                            

        self.dst_label = ttk.Label(root, textvariable = self.dst)
        self.dst_label.grid(row=3, column=0, sticky=W)

        self.browse2 = ttk.Button(root, text = "Browse", command = lambda: self.dst.set(filedialog.askdirectory()))
        self.browse2.grid(row=3, column=2)

        ttk.Button(root, text = "Reset", command = self.clear).grid(row=4, column=0, sticky=E)
        ttk.Button(root, text = "Copy", command = self.copy).grid(row=4, column=1, sticky=W)
        
            
    def copy(self):             
        src = self.src.get()
        dst = self.dst.get()
        filesInSrc = os.listdir(src)
        for file in filesInSrc:
            fileModTime = os.path.getmtime(src+'/'+file)
            if time.time() - fileModTime <= 86400:
                shutil.copy2(src+'/'+file, dst)
        insert_data()

    def clear(self):
        self.src.set("Choose a folder to check for new files")
        self.dst.set("Choose a folder to copy files into")
        
                

if __name__ == "__main__":
    root = Tk()
    app = FileApp(root)
    root.title("Copy New Files")
    root.mainloop()
    c.close()
    conn.close()
    
