import shutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter import * 
import os

__path_of_dir__ = ""
__path_of_file__ = ""

def browse():
    global __path_of_dir__
    __path_of_dir__ = filedialog.askdirectory(initialdir='/')

def browsefile():
    global __path_of_file__
    __path_of_file__ = filedialog.askopenfilename(filetypes=[
        ("Plain Zip","*.zip"),
        ("X-Zipped Tar-Archive","*.tar.xz"),
        ("G-Zipped Tar-Archive","*.tar.gz"),
        ("B-Zipped Tar-Archive","*.tar.bz"),
        ("All Files","*.*"),
    ])


def getRadioButtonValue():
	buttonSelected = frmt.get()
	return buttonSelected

def getRadioButtonValue2():
	buttonSelected = frmt.get()
	return buttonSelected

def startcompress():
    value = getRadioButtonValue()
    if not __path_of_dir__:
        browse()
    shutil.make_archive(__path_of_dir__.split("\\")[-1],value,__path_of_dir__)
    messagebox.showinfo("Success",f'Successfully compressed 1 Directory')

def startdecompress():
    if not __path_of_file__:
        browsefile()
    types = {
        "tar":"tar",
        "gz":"gztar",
        "bz":"bztar",
        "xz":"xztar",
        "zip":"zip",
    }
    pathname = os.path.splitext(os.path.splitext(os.path.basename(__path_of_file__))[0])[0]
    shutil.unpack_archive(os.path.basename(__path_of_file__),pathname,types.get(os.path.splitext(__path_of_file__)[1]))
    messagebox.showinfo("Success",f'Successfully decompressed {__path_of_file__}')


root = Tk()
frmt = tk.StringVar()

root.geometry('700x377')
root.configure(background='#F0F8FF')
root.title('WinTAR')
tabControl = ttk.Notebook(root)
compress = Frame(tabControl)
decompress = Frame(tabControl)
tabControl.add(compress,text="Compress Directory")
tabControl.add(decompress,text="Decompress Directory")
tabControl.pack(expand=1, fill="both")

Button(compress, text='Select Folder', bg='#F0F8FF', font=('arial', 12, 'normal'), command=browse).place(x=17, y=24)


frame=Frame(compress, width=0, height=0, bg='#F0F8FF')
frame.place(x=19, y=112)
ARBEES=[
('Tar-Archive', 'tar'), 
('GZipped Tar Archive', 'gztar'), 
('XZipped Tar Archive', 'xztar'), 
('BZipped Tar Archive', 'bztar'), 
('Plain Zipfile', 'zip'), 
]
for text, mode in ARBEES:
	formt=Radiobutton(frame, text=text, variable=frmt, value=mode, bg='#F0F8FF', font=('arial', 12, 'normal')).pack(side='left', anchor = 'w')


Label(compress, text='Select Format', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=19, y=89)


Button(compress, text='Compress', bg='#F0F8FF', font=('arial', 12, 'normal'), command=startcompress).place(x=20, y=174)
Button(decompress, text='Select Archive', bg='#F0F8FF', font=('arial', 12, 'normal'), command=browsefile).place(x=17, y=24)

Button(decompress, text='Extract', bg='#F0F8FF', font=('arial', 12, 'normal'), command=startdecompress).place(x=20, y=174)


root.mainloop()
