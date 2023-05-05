from tkinter import *
from formation import AppBuilder
from tkinter.filedialog import askopenfilename
import os


def selectFile():
	global file_path
	file_path=askopenfilename()
	with open(file_path,'r') as f:
		content = f.read()
	app.t1.delete(1.0,END)
	app.t1.insert(END,content)

def addFile():
	text = app.e1.get()
	os.system(f'touch {text}')
def deleteFile():
	text = app.e1.get()
	os.system(f'rm -rf {text}')
def updateFile():
	app.tree1.delete(*app.tree1.get_children())
	file_path = os.listdir()
	for file in file_path:
		app.tree1.insert('',END,text=file)
def saveFile():
	content = app.t1.get(1.0,END)
	with open(file_path,'w') as f:
		f.write(content)

app = AppBuilder(path="nottaker.xml")
app._root.master.title('Not Düzenleyici')
app.connect_callbacks(globals())
app.mainloop()
