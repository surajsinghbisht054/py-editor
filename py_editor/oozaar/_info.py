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
import Tkinter,ttk

class helps(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self, className='About')
        Tkinter.Label(self, text='https://hackworldwithssb.blogspot.in\nsurajsinghbisht054@gmail.com\nS.S.B', foreground='SkyBlue', borderwidth=4, background='black').pack(pady=10,padx=10, ipady=10,ipadx=10,expand='yes', fill='both')
        ttk.Button(self, text='Close', command=lambda:self.destroy()).pack(side='bottom')
class about(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self, className='About')
        Tkinter.Label(self, text='This Editor is Written in Python Language\n And This Editor is Cross-Platform Supported \n Only For Practise And Educational Purpose Only \n By S.S.B', foreground='SkyBlue', borderwidth=4, background='black').pack(pady=10,padx=10, ipady=10,ipadx=10,expand='yes', fill='both')
        ttk.Button(self, text='Close', command=lambda:self.destroy()).pack(side='bottom')
class window:
    def __init__(self):
        pass
    def helps(self,event=None):
        storeobj=helps()
        storeobj.mainloop()
    def about(self,event=None):
        storeobj=about()
        storeobj.mainloop()
