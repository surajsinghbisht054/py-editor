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
#from oozaar import bar,linenumber,scroll,linenumber
import Tkinter, ttk
from oozaar import scrollingtext,bar,ColorLight
class Main(Tkinter.Tk):
    def __init__(self):
        # Creating Windows
        Tkinter.Tk.__init__(self)

        # Title
        self.title('Python Text Editor')
        
        self.filepath=Tkinter.StringVar() # For File Name
        self.filepath.set('BOND - Unitled.py') # Blank File Name
        self.minsize(400,600)

        # [Shortcut Bar Main Frame]
        self.shortcut_bar=ttk.Frame(self)
        self.shortcut_bar.pack(expand='no', fill='x')

        # +++++++++++++++++++++++++ Text Box System ++++++++++++++++++++++++++++++++++++++++++++++
        # Frame For [Text Box]
        frame=ttk.Frame(self, borderwidth=5)
        frame.pack(expand='yes', fill='both')
        frame1=ttk.Frame(frame)
        frame1.pack(side='top', expand='yes', fill='both')
        self.text_box=Tkinter.Text(frame1, wrap='none', undo=1)
        self.text_box.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
        self.text_box.pack()

        # Adding Features On Text Box
        self.box=scrollingtext.featured_text(root=frame1, textbox=self.text_box, main=frame)

        #++++++++++++++++++++++++ [System Close] ++++++++++++++++++++++++++++++++++++++++++++++

        # Function For Scrolling Text widget number line Together
        cursurinfo=ttk.Label(self.text_box, text='Line 1 | Column 1')
        cursurinfo.pack(expand='no', fill=None, side='right',anchor='se')

        # Adding Functions and Features
        storeobj=bar.menu(root=self, text_bx=self.text_box,shortcut_bar=self.shortcut_bar,cursurbar=cursurinfo)


        # Adding Syntax Highlighting Feature
        self.syntax_color=ColorLight.ColorLight(txtbox=self.text_box)


        # Binding Triggers
        self.bind_all('<Any-KeyPress>',self.trigger)

    # All-Key Trigger
    def trigger(self, event):
        self.box.changed()
        self.syntax_color.trigger()
        

      

if __name__=='__main__':
    Main().mainloop()
