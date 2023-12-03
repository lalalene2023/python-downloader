from tkinter import filedialog
from requests import get
import tkinter as tk
from tkinter import filedialog,messagebox

gui = tk.Tk()
gui.title("Downloader")

text_http = tk.Label(gui,text="URL:")
input_http = tk.Entry(gui,width=30)

text_http.pack()
input_http.pack()

def getfile():
    path_ = filedialog.askdirectory(title="Choose File")
    url = input_http.get()
    try:
        filename = url[url.rindex('/')+1:]
    except ValueError:
        tk.messagebox.showinfo('Info','Please fill in the URL first to fill in the file name!')
    filepath = path_+'/'+filename
    path.set(filepath)
path = tk.StringVar()
text_path = tk.Label(gui,text="Download Path：")
input_path = tk.Entry(gui,textvariable=path,width=30)
button_path = tk.Button(gui,text="Choose Download Folder",width=20,command=getfile)

text_path.pack()
input_path.pack()
button_path.pack()

def start():
    URL = input_http.get()
    path = input_path.get()
    if URL or path == '':
        messagebox.showerror('Error',"'path' or 'URL' cannot none!")
    elif URL or path == '.!Entry':
        messagebox.showerror('Error', 'Unknown Reason.')
    else:
        url = get(URL)
        with open(path,'w') as file:
            file.write(url.content)

button_download = tk.Button(text='Start Download',width=12,command=start)
button_download.pack()

gui.resizable(width=False, height=False)
gui.mainloop()