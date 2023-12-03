from tkinter import filedialog
from requests import get
import tkinter as tk
from tkinter import filedialog,messagebox

gui = tk.Tk()
gui.title("下载器")

text_http = tk.Label(gui,text="下载链接：")
input_http = tk.Entry(gui,width=30)

text_http.pack()
input_http.pack()

def getfile():
    path_ = filedialog.askdirectory(title="选择路径")
    url = input_http.get()
    try:
        filename = url[url.rindex('/')+1:]
    except ValueError:
        tk.messagebox.showinfo('提示','请先填写网址以提供文件名！')
    filepath = path_+'/'+filename
    path.set(filepath)
path = tk.StringVar()
text_path = tk.Label(gui,text="下载路径：")
input_path = tk.Entry(gui,textvariable=path,width=30)
button_path = tk.Button(gui,text="选择下载路径",width=10,command=getfile)

text_path.pack()
input_path.pack()
button_path.pack()

def start():
    URL = input_http.get()
    path = input_path.get()
    if URL or path == '':
        messagebox.showerror('错误','路径或网址不可为空！')
    elif URL or path == '.!Entry':
        messagebox.showerror('错误', '未知原因')
    else:
        url = get(URL)
        with open(path,'w') as file:
            file.write(url.content)

button_download = tk.Button(text='开始下载',width=8,command=start)
button_download.pack()

gui.resizable(width=False, height=False)
gui.mainloop()
