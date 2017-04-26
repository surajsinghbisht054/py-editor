#!/usr/bin/python

# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This Script Is Created For http://bitforestinfo.blogspot.com
# This Script is Written By
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
__author__='''

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.com/

    Note: We Feel Proud To Be Indian
######################################################
'''
# For Dialog Box

from Tkinter import *
import tkFileDialog

ExtType=[
    ('All Files ', '*.*'),
    ('.py (With Console)', '*.py'),
    ('.pyw (Without Console) ', '*.pyw')
    ]
def Save_as_txt(txtbox=None,mode='a', filepath=None, rt=None):
    path=tkFileDialog.asksaveasfile(title='Save As', defaultextension='*.py',filetypes=ExtType)
    storeobj=txtbox.get('1.0', END)
    print path
    if filepath:
        filepath.set(path.name)
        rt.title(path.name)
        filetmp=open(path.name,mode)
        filetmp.write(storeobj)
        filetmp.close()
def open_txt(txtbox=None, rt=None,filepath=None):
    path=tkFileDialog.askopenfilename(title="Open Script")
    if path:
        storefile=open(path,'r')
        storechar=storefile.read()
        rt.title(str('pyEditor -  '+path))
        filepath.set(path)
        txtbox.insert('1.0', storechar)
        storefile.close()
def save_txt(txtbox=None, rt=None, filepath=None):
    if filepath.get()=="Unitled.py":
        Save_as_txt(txtbox=txtbox,mode='w',filepath=filepath,rt=rt)
    else:
        storeobjchar=txtbox.get('1.0',END)
        storefile=open(filepath.get(),'w')
        storefile.write(storeobjchar)
        storefile.close()        
def close_txt(txtbox=None, rt=None,filepath=None):
    save_txt(txtbox=txtbox, rt=rt, filepath=filepath)
    txtbox.delete('1.0',END)
    rt.title('Py-Editor')

def run_script(txtbox=None, rt=None,filepath=None):
    save_txt(txtbox=txtbox, rt=rt, filepath=filepath)
    from os import system as cm
    cm('python %s'%filepath.get())
def compile_script(txtbox=None, rt=None,filepath=None):
    save_txt(txtbox=txtbox, rt=rt, filepath=filepath)
    from os import system as cm
    cm('python -m compileall %s'%filepath.get())
def run_compile_script(txtbox=None, rt=None,filepath=None):
    compile_script(txtbox=txtbox, rt=rt, filepath=filepath)
    run_script(txtbox=txtbox, rt=rt, filepath=filepath)
"""root=Tk()
root.title('Dialog BOx')
tt=Text(root)
filepath=StringVar()
filepath.set('Unitled.py')
tt.pack(expand='yes')
Button(root, text='Click Me', command=lambda:close_txt(txtbox=tt, rt=root, filepath=filepath)).pack()
root.mainloop()
"""
