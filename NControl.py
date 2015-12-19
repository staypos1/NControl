import subprocess
import os,sys,ttk
from Tkinter import *
import win32com.shell.shell as shell
ASADMIN = 'asadmin'
#restarts program with admin rights
if sys.argv[-1] != ASADMIN:
		script = os.path.abspath(sys.argv[0])
		params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
		shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
		sys.exit(0)
def WifiOff():
	subprocess.call('netsh interface set interface Wi-Fi admin=DISABLED')
	print 'wifi off'
def WifiOn():
	subprocess.call('netsh interface set interface Wi-Fi admin=ENABLED')
	print 'wifi on'
ASADMIN = 'asadmin'
root = Tk()
root.geometry("400x90")
root.resizable(0,0)
root.title('N CONTROL')
w=ttk.Frame(root,relief=GROOVE,borderwidth=2,padding=(5,5))
w.pack(fill=BOTH)
title = ttk.Label(w,text='Network Adapter Controller',anchor=CENTER)
title.pack(fill=X)
wOn=ttk.Button(w,width=30,text="Turn wifi adapter off",command=WifiOff)
wOn.pack(fill=X)
wOff=ttk.Button(w,width=30,text="Turn wifi adapter on",command=WifiOn)
wOff.pack(fill=X)
s = ttk.Style()
s.configure('.', font=('Helvetica', 12))
s.theme_use('clam')
root.mainloop()
