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
import Tkinter, bar,linenumber,scroll,linenumber






class Main(Tkinter.Tk):
    def __init__(self):
        # Creating Windows
        Tkinter.Tk.__init__(self)

        # Title
        self.title('Python Text Editor')
        self.filepath=Tkinter.StringVar()
        self.filepath.set('Unitled.py')
        self.minsize(400,600)

        # shortcut Frame, line number and Main text
        self.shortcut_bar=Tkinter.Frame(self)
        self.shortcut_bar.pack(expand='no', fill='x')
        
        # Text Box
        self.content_box=Tkinter.Text(self, wrap='none', undo=1,width=40)
        self.content_box.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
        


        # scroll Bar x For width
        self.scroll_x=Tkinter.Scrollbar(self, orient='horizontal')
        self.scroll_x.config(command=self.content_box.xview)
        self.content_box.configure(xscrollcommand=self.scroll_x.set)
        self.scroll_x.pack(side='bottom', fill='x')
        
        # Scroll Bar y For Height
        self.scroll_y=Tkinter.Scrollbar(self.content_box)
        self.scroll_y.config(command=self.content_box.yview)
        self.content_box.configure(yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side='right', fill='y')

        # Function For Scrolling Text widget number line Together
        #scroll.ScrolledTextPair(master=self, textbox1=self.linenumber_bar, textbox2=self.content_box,scrollbar=self.scroll_y)
        cursurinfo=Tkinter.Label(self.content_box, text='Line 1 | Column 1')
        cursurinfo.pack(expand='no', fill=None, side='right',anchor='se')

        self.linenumbers = linenumber.LineNumberCanvas(self, width=40)
        self.linenumbers.connect(self.content_box)
        self.linenumbers.pack(side="left", fill="y")
        self.linenumbers.bind('<Button-1>',self.linenumbers.get_breakpoint_number)
        #self.content_box.bind('<Any-KeyPress>',self.changed)
        self.bind_all('<Any-KeyPress>',self.changed)
        self.content_box.pack(expand='yes', fill='both')

        # Using Bar Module For Other widgets
        bar.menu(root=self, text_bx=self.content_box,shortcut_bar=self.shortcut_bar,cursurbar=cursurinfo)

    def changed(self, event):
        self.linenumbers.re_render()
        

if __name__=='__main__':
    Main().mainloop()


