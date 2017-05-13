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
import ttk


def search_(te, var,num):
    if len(var)==0:
        return
    te.tag_remove('match','1.0','end')
    startpos=te.search(var, num.get(),forwards=None, backwards=None, exact=None, regexp=None, nocase=None, count=True, elide=None)
    if len(startpos)==0:
        return 'None'
    start=int(startpos.split('.')[0])
    end=len(var)+int(startpos.split('.')[1])
    indax='{}.{}'.format(start, end)
    print startpos
    print indax
    te.tag_add('match', startpos, indax)
    te.tag_config('match',foreground='red', background='yellow')

    num.set(indax)
def replace_(te, var,num, char='st'):
    if len(var)==0:
        return
    te.tag_remove('match','1.0','end')
    startpos=te.search(var, num.get(),forwards=None, backwards=None, exact=None, regexp=None, nocase=None, count=True, elide=None)
    if len(startpos)==0:
        return 'None'
    start=int(startpos.split('.')[0])
    end=len(var)+int(startpos.split('.')[1])
    indax='{}.{}'.format(start, end)
    print startpos
    print indax
    te.tag_add('match', startpos, indax)
    te.tag_config('match',foreground='red', background='yellow')
    te.delete(startpos, indax)
    te.insert(startpos,char)
    num.set(indax)
    
def searchall_(te, var):
    if len(var)==0:
        return
    startpoint='1.0'
    while True:
        startpos=te.search(var, startpoint,stopindex=Tkinter.END ,forwards=None, backwards=None, exact=None, regexp=None, nocase=None, elide=None)
        if startpos=='':
            print 'break'
            break
        start=int(startpos.split('.')[0])
        end=len(var)+int(startpos.split('.')[1])
        indax='{}.{}'.format(start, end)
        print startpos
        te.tag_add('match', startpos, indax)
        te.tag_config('match',foreground='red', background='yellow')
        startpoint=indax
    return


def replaceall_(te, var,char='st'):
    if len(var)==0:
        return
    startpoint='1.0'
    while True:
        startpos=te.search(var, startpoint,stopindex=Tkinter.END ,forwards=None, backwards=None, exact=None, regexp=None, nocase=None, elide=None)
        if startpos=='':
            print 'break'
            break
        elif startpos==None:
            break
        start=int(startpos.split('.')[0])
        end=len(var)+int(startpos.split('.')[1])
        indax='{}.{}'.format(start, end)
        print startpos
        te.tag_add('match', startpos, indax)
        te.tag_config('match',foreground='red', background='yellow')
        te.delete(startpos, indax)
        te.insert(startpos,char)
        startpoint=indax
    return

class Find_wm:
    def __init__(self, root, win=None):
        storeobj=Tkinter.Toplevel(root)
        storeobj.int=Tkinter.StringVar()
        storeobj.int.set('1.0')
        storeobj.title('Find..')
        storeobj.transient(root)
        storeobj.focus_set()
        self.entry=Tkinter.StringVar()
        ttk.Label(storeobj, text='Find    : ').grid(row=0, column=0, padx=10, pady=10)
        ttk.Entry(storeobj, textvariable=self.entry, width=55).grid(row=0, column=1, padx=10, pady=10)
        ttk.Button(storeobj, text='Find',command=lambda: search_(win, self.entry.get(),num=storeobj.int)).grid(column=2, row=0, padx=10, pady=10)
        ttk.Button(storeobj, text='Close', command=lambda: storeobj.destroy()).grid(row=1, column=0, padx=10, pady=10)
        ttk.Button(storeobj, text='Find All',command=lambda: searchall_(win, self.entry.get())).grid(column=2, row=1, padx=10, pady=10)


class replace_wm:
    def __init__(self, root, win=None):
        storeobj=Tkinter.Toplevel(root)
        storeobj.int=Tkinter.StringVar()
        storeobj.int.set('1.0')
        storeobj.title('Replace')
        storeobj.transient(root)
        storeobj.focus_set()
        self.entry=Tkinter.StringVar()
        self.entry1=Tkinter.StringVar()
        ttk.Label(storeobj, text='Find         : ').grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(storeobj, text='Replace With :').grid(row=1, column=0, padx=10, pady=10)
        ttk.Entry(storeobj, textvariable=self.entry, width=55).grid(row=0, column=1, padx=10, pady=10)
        ttk.Entry(storeobj, textvariable=self.entry1, width=55).grid(row=1, column=1, padx=10, pady=10)
        ttk.Button(storeobj, text='Replace',command=lambda: replace_(win, self.entry.get(),num=storeobj.int, char=self.entry1.get())).grid(column=2, row=0, padx=10, pady=10)
        ttk.Button(storeobj, text='Replace All',command=lambda: replaceall_(win, self.entry.get(), char=self.entry1.get())).grid(column=2, row=1, padx=10, pady=10)
        ttk.Button(storeobj, text='Close ', command=lambda: storeobj.destroy()).grid(row=2, column=2, padx=10, pady=10)
"""
root=Tkinter.Tk()
te=Tkinter.Text(root)
te.pack()
b=ttk.Button(root, text='trigger rr',command=lambda:replace_wm(root,win=te))
b.pack()
b1=ttk.Button(root, text='trigger ff',command=lambda:Find_wm(root,win=te))
b1.pack()
root.mainloop()
"""
