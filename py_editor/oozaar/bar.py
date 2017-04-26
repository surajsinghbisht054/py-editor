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
try:
    import Tkinter
except:
    import tkinter as Tkinter
import ttk, _findwm,Font,tkFont,filect,os,_info
try:
    import tkinter.messagebox as tmb
except:
    import tkMessageBox as tmb




# MENU  
class menu:

    # Menu GUI
    def __init__(self, root=None, text_bx=None,shortcut_bar=None, linebar=None,cursurbar=None):
        self.shortcut_bar=shortcut_bar
        self.root=root
        self.root.content_text=text_bx
        self.fontvar=tkFont.Font()
        self.root.content_text.configure(font=self.fontvar)
        self.show_cursor_info=Tkinter.IntVar()
        self.to_highlight_line = Tkinter.BooleanVar()
        self.cursurbar=cursurbar
        # Create Main Menu Bar
        self.root.bar=Tkinter.Menu(self.root)

        # Main Menu Sub Class
        self.root.m_menu=Tkinter.Menu(self.root.bar, tearoff=0)
        
        self.root.m_menu.add_command(label='New', accelerator='Ctrl+N', compound='left', underline=0, command=self.new_file)
        self.root.m_menu.add_separator()
        
        self.root.m_menu.add_command(label='Open', accelerator='Ctrl+O', compound='left', underline=0, command=self.open_txt)
        self.root.m_menu.add_command(label='Save', accelerator='Ctrl+S', compound='left', underline=0, command=self.save_txt)
        self.root.m_menu.add_command(label='Save as', accelerator='Ctrl+Shift+S', compound='left', underline=0,command=self.save_as_txt)
        self.root.m_menu.add_separator()
        
        self.root.m_menu.add_command(label='New Windows', accelerator='Ctrl+W', compound='left', underline=0, command=self.new_file)
        self.root.m_menu.add_separator()
        
        self.root.m_menu.add_command(label='Print', accelerator='Ctrl+P', compound='left', underline=0)
        self.root.m_menu.add_separator()
        
        self.root.m_menu.add_command(label='Close', accelerator='Ctrl+X', compound='left', underline=0, command=self.close_txt)
        self.root.m_menu.add_separator()
        
        self.root.m_menu.add_command(label='Exit', accelerator='Alt+F4', compound='left', underline=0, command=self.out)
        # Main Menu Sub Class
        self.root.m_menu1=Tkinter.Menu(self.root.bar, tearoff=0)
        self.root.m_menu1.add_command(label='Undo', accelerator='Ctrl+Z', compound='left', underline=0, command=self.undo)
        self.root.m_menu1.add_command(label='Redo', accelerator='Ctrl+Shift+z', compound='left', underline=0, command=self.redo)
        self.root.m_menu1.add_separator()
        self.root.m_menu1.add_command(label='Cut', accelerator='Ctrl+X', compound='left', underline=0, command=self.cut)
        self.root.m_menu1.add_command(label='Copy', accelerator='Ctrl+C', compound='left', underline=0, command=self.copy)
        self.root.m_menu1.add_command(label='Paste', accelerator='Ctrl+V', compound='left', underline=0, command=self.paste)
        self.root.m_menu1.add_separator()
        
        self.root.m_menu1.add_command(label='Find', accelerator='Ctrl+F', compound='left', underline=0, command=self.find_wm)
        self.root.m_menu1.add_command(label='Replace', accelerator='Ctrl+R', compound='left', underline=0, command=self.replace_wm)
        self.root.m_menu1.add_separator()
        
        self.root.m_menu1.add_command(label='Select All', accelerator='Ctrl+A', compound='left', underline=0, command=self.selectall)

        # Also Editing Small Menu At Context box
        self.popup_menu = Tkinter.Menu(self.root.content_text)
        self.popup_menu.add_command(label='Cut',command=self.cut)
        self.popup_menu.add_command(label='Copy',command=self.copy)
        self.popup_menu.add_command(label='Paste',command=self.paste)
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label='Undo',command=self.undo)
        self.popup_menu.add_command(label='Redo',command=self.redo)
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label='Select All',command=self.selectall)

        # Main Menu Sub Class
        self.root.m_menu2=Tkinter.Menu(self.root.bar, tearoff=0)
        
        self.root.m_menu2.add_checkbutton(label='Highlight Current Line',onvalue=1, offvalue=0, variable=self.to_highlight_line,command=self.toggle_highlight)
        self.root.m_menu2.add_command(label='Font', compound='left', underline=0, command=self.font__)
        self.root.m_menu2.add_separator()
        self.root.m_menu2.add_command(label='Full Screen', compound='left', underline=0)    
        self.root.m_menu3=Tkinter.Menu(self.root.bar, tearoff=0)
        self.root.m_menu3.add_command(label='Run', accelerator='F5', compound='left', underline=0,command=self.run_script)
        self.root.m_menu3.add_command(label='Compile', accelerator='F6', compound='left', underline=0,command=self.compile_script)
        self.root.m_menu3.add_separator()
        self.root.m_menu3.add_command(label='Compile&Run', accelerator='F7', compound='left', underline=0,command=self.run_compile_script)

        # Main Menu Sub Class
        self.root.m_menu4=Tkinter.Menu(self.root.bar, tearoff=0)
        info=_info.window()
        self.root.m_menu4.add_command(label='Help', accelerator='F1', compound='left', underline=0,command=info.helps)
        self.root.m_menu4.add_separator()
        self.root.m_menu4.add_command(label='About', accelerator='F2', compound='left', underline=0,command=info.about)

        # Main Menu Sub Class configureurations
        self.root.m_menu5=Tkinter.Menu(self.root.bar, tearoff=0)
        self.root.bar.add_cascade(label='File', menu=self.root.m_menu)
        self.root.bar.add_cascade(label='Edit', menu=self.root.m_menu1)
        self.root.bar.add_cascade(label='View', menu=self.root.m_menu2)
        self.root.bar.add_cascade(label='Run', menu=self.root.m_menu3)
        self.root.bar.add_cascade(label='About', menu=self.root.m_menu4)

        # Main Bar Activated
        self.root.configure(menu=self.root.bar)

        # Main Functions Binds (triggers)
        self.root.bind('<Control-A>', self.selectall)
        self.root.bind('<Control-a>', self.selectall)
        self.root.bind('<Control-Shift-z>', self.redo)
        self.root.bind('<Control-Shift-Z>', self.redo)
        self.root.bind('<Control-F>', self.find_wm)
        self.root.bind('<Control-f>', self.find_wm)
        self.root.bind('<Control-R>', self.replace_wm)
        self.root.bind('<Control-r>', self.replace_wm)
	self.root.bind('<Control-w>', self.new_file)
	self.root.bind('<Control-W>', self.new_file)
	self.root.bind('<Control-n>', self.new_file)
	self.root.bind('<Control-N>', self.new_file)
        self.root.bind_all('<Control-H>',self.Enter_line)
        self.root.bind('<Control-s>', self.save_txt)
        self.root.bind('<Control-S>', self.save_txt)
        self.root.bind('<Control-o>', self.open_txt)
        self.root.bind('<Control-O>', self.open_txt)
        self.root.bind('<Control-Shift-S>', self.save_as_txt)
        self.root.bind('<Control-Shift-s>', self.save_as_txt)
        self.root.bind('<Control-X>', self.close_txt)
        self.root.bind('<Control-x>', self.close_txt)
        self.root.bind('<KeyPress-F1>', info.helps)
        self.root.bind('<KeyPress-F2>', info.about)
        self.root.bind('<KeyPress-F5>', self.run_script)
        self.root.bind('<KeyPress-F6>', self.compile_script)
        self.root.bind('<KeyPress-F7>', self.run_compile_script)
        self.root.bind('<Any-KeyPress>',self.linenotrigger)
	self.root.bind('<Button-1>',self.linenotrigger)
        self.root.content_text.tag_configure('active_line', background='ivory2')
        self.root.content_text.bind('<Button-3>', self.show_popup_menu)
        self.root.protocol('WM_DELETE_WINDOW', self.out)


        shortcut_cmd=("self.open_txt:Icons/text_editor.gif",
                      "self.undo:Icons/edit_undo.gif",
                      "self.redo:Icons/edit_redo.gif",
                      "self.cut:Icons/edit_cut.gif",
                      "self.copy:Icons/edit_copy.gif",
                      "self.paste:Icons/edit_paste.gif",
                      "self.find_wm:Icons/edit_find.gif",
                      "self.replace_wm:Icons/edit_find_replace.gif",
                      "self.selectall:Icons/edit_select_all.gif")
        for i in shortcut_cmd:
            j=i[i.find(':')+1:]
            i=i[0:i.find(':')]
            #j=os.getcwd()+'\\'+j
	    try:
		storeimg=Tkinter.PhotoImage(file=j)
	    except:
		j=j.replace('/','\\')
		storeimg=Tkinter.PhotoImage(file=j)
            
            storebutton=ttk.Button(self.shortcut_bar,command=eval(i))
            storebutton.image=storeimg
            storebutton.configure(image=storeimg)
            storebutton.pack(side='left',fill='y')
    # Main Function Mechanizem

    

    #++++++++++++ Events Functions +++++++++++++++++++++++++++++++ 
    def cut(self, event=None):
        self.root.content_text.event_generate("<<Cut>>")
    def copy(self, event=None):
        self.root.content_text.event_generate("<<Copy>>")
    def paste(self, event=None):
        self.root.content_text.event_generate("<<Paste>>")
    def undo(self, event=None):
        self.root.content_text.event_generate('<<Undo>>')
    def redo(self, event=None):
        self.root.content_text.event_generate("<<Redo>>")
    def selectall(self, event=None):
        self.root.content_text.tag_add('sel','1.0','end')
    def out(self, event=None):
        store=tmb.askyesnocancel(title='Save On Close',message='Do You Want To Save This File Before Closing?')
        if store:
            self.save_txt()
            self.root.destroy()
        elif store==None:
            print store
            pass
        else:
            self.root.destroy()
    def find_wm(self, event=None):
        _findwm.Find_wm(self.root,win=self.root.content_text)
    def replace_wm(self, event=None):
        _findwm.replace_wm(self.root,win=self.root.content_text)
    def font__(self):
        Font.Font_wm(Font=self.fontvar)
    def Enter_line(self,event=None):
        print self.root.content_text.grid_size()
    def new_file(self, event=None):
	from os import system
	system('python main.py')

    def open_txt(self,event=None):
        filect.open_txt(txtbox=self.root.content_text, rt=self.root,filepath=self.root.filepath)
    def save_as_txt(self,event=None):
        filect.Save_as_txt(txtbox=self.root.content_text, rt=self.root,filepath=self.root.filepath)
    def save_txt(self,event=None):
        filect.save_txt(txtbox=self.root.content_text, rt=self.root,filepath=self.root.filepath)
    def run_script(self,event=None):
        filect.run_script(txtbox=self.root.content_text, rt=self.root,filepath=self.root.filepath)
    def compile_script(self, event=None):
        filect.compile_script(txtbox=self.root.content_text, rt=self.root,filepath=self.root.filepath)
    def run_compile_script(self, event=None):
        filect.run_compile_script(txtbox=self.root.content_text, rt=self.root,filepath=self.root.filepath)
    def close_txt(self,event=None):    
        filect.close_txt(txtbox=self.root.content_text, rt=self.root,filepath=self.root.filepath)
    def linenotrigger(self,event=None):
        self.update_cursor_info_bar()
    def highlight_line(self, interval=100):
        self.root.content_text.tag_remove("active_line", '1.0', "end")
        self.root.content_text.tag_add("active_line", "insert linestart","insert lineend+1c")
        self.root.content_text.after(interval, self.toggle_highlight)
    def undo_highlight(self):
        self.root.content_text.tag_remove("active_line", '1.0', "end")
    def toggle_highlight(self,event=None):
        if self.to_highlight_line.get():
            self.highlight_line()
        else:
            self.undo_highlight()
    def show_cursor_info_bar(self):
        show_cursor_info_checked = self.show_cursor_info.get()
        if show_cursor_info_checked:
            self.cursurbar.pack(expand='no', fill=None, side='right',anchor='se')
        else:
            self.cursurbar.pack_forget()
    def update_cursor_info_bar(self, event=None):
        row, col = self.root.content_text.index(Tkinter.INSERT).split('.')
        line_num, col_num = str(int(row)), str(int(col)+1) # colstarts at 0
        infotext = "Line: {0} | Column: {1}".format(line_num, col_num)
        self.cursurbar.configure(text=infotext)
        
    def show_popup_menu(self,event):
        self.popup_menu.tk_popup(event.x_root, event.y_root)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""root=Tkinter.Tk()
te=Tkinter.Text(root, wrap='none', undo=1)
te.pack()
menu(root, te)
root.mainloop()
"""
