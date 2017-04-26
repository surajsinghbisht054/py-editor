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
import Tkinter as tk 


class LineNumberCanvas(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.text_widget = None
        self.breakpoints = []

    def connect(self,text_widget):
        self.text_widget = text_widget

    def re_render(self):
        """Re-render the line canvas"""
        self.delete('all') # To prevent drawing over the previous canvas

        temp = self.text_widget.index("@0,0")
        while True :
            dline= self.text_widget.dlineinfo(temp)
            if dline is None: 
                break
            y = dline[1]
            x = dline[0]
            linenum = str(temp).split(".")[0]

            id = self.create_text(2,y,anchor="nw", text=linenum)

            if int(linenum) in self.breakpoints:                
                x1,y1,x2,y2 = self.bbox(id)
                self.create_oval(x1,y1,x2,y2,fill='red')
                self.tag_raise(id)

            temp = self.text_widget.index("%s+1line" % temp)

    def get_breakpoint_number(self,event):
         if self.find_withtag('current'):
            i = self.find_withtag('current')[0]
            linenum = int(self.itemcget(i,'text'))

            if linenum in self.breakpoints:
                self.breakpoints.remove(linenum)
            else:
                self.breakpoints.append(linenum)
            self.re_render()
            
            



class Text(tk.Text):
     def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

        self.tk.eval('''
            proc widget_interceptor {widget command args} {

                set orig_call [uplevel [linsert $args 0 $command]]

              if {
                    ([lindex $args 0] == "insert") ||
                    ([lindex $args 0] == "delete") ||
                    ([lindex $args 0] == "replace") ||
                    ([lrange $args 0 2] == {mark set insert}) || 
                    ([lrange $args 0 1] == {xview moveto}) ||
                    ([lrange $args 0 1] == {xview scroll}) ||
                    ([lrange $args 0 1] == {yview moveto}) ||
                    ([lrange $args 0 1] == {yview scroll})} {

                    event generate  $widget <<Changed>>
                }

                #return original command
                return $orig_call
            }
            ''')
        self.tk.eval('''
            rename {widget} new
            interp alias {{}} ::{widget} {{}} widget_interceptor {widget} new
        '''.format(widget=str(self)))


class EditorWindow(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = Text(self)
        self.scrollbar = tk.Scrollbar(orient="vertical", command=self.text.yview)

        self.text.configure(yscrollcommand=self.scrollbar.set)   

        self.linenumbers = LineNumberCanvas(self, width=40)
        self.linenumbers.connect(self.text)

 

        
        self.scrollbar.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")

        self.text.bind('<Down>',self.changed)
        self.text.bind('<Up>',self.changed)
        self.text.bind("<<Changed>>", self.changed)
        self.text.bind("<Configure>", self.changed)
        self.linenumbers.bind('<Button-1>',self.linenumbers.get_breakpoint_number)
        self.text.pack(side="right", fill="both", expand=True)




    def changed(self, event):
        self.linenumbers.re_render()


if __name__ == '__main__':
    root = tk.Tk()
    l = EditorWindow(root)
    l.pack()
    root.mainloop()

