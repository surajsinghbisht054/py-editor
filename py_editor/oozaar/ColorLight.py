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

import __builtin__,re,keyword, Tkinter


def any(name, alternates):
    "Return a named group pattern matching list of alternates."
    return "(?P<%s>" % name + "|".join(alternates) + ")"
def ty():
    kw = r"\b" + any("KEYWORD", keyword.kwlist) + r"\b"
    print kw
    builtinlist = [str(name) for name in dir(__builtin__)
                                        if not name.startswith('_')]
    # We don't know whether "print" is a function or a keyword,
    # so we always treat is as a keyword (the most common case).
    builtinlist.remove('print')
    # self.file = file("file") :
    # 1st 'file' colorized normal, 2nd as builtin, 3rd as string
    builtin = r"([^.'\"\\#]\b|^)" + any("BUILTIN", builtinlist) + r"\b"
    comment = any("COMMENT", [r"#[^\n]*"])
    stringprefix = r"(\br|u|ur|R|U|UR|Ur|uR|b|B|br|Br|bR|BR)?"
    sqstring = stringprefix + r"'[^'\\\n]*(\\.[^'\\\n]*)*'?"
    dqstring = stringprefix + r'"[^"\\\n]*(\\.[^"\\\n]*)*"?'
    sq3string = stringprefix + r"'''[^'\\]*((\\.|'(?!''))[^'\\]*)*(''')?"
    dq3string = stringprefix + r'"""[^"\\]*((\\.|"(?!""))[^"\\]*)*(""")?'
    string = any("STRING", [sq3string, dq3string, sqstring, dqstring])
    return kw + "|" + builtin + "|" + comment + "|" + string +\
           "|" + any("SYNC", [r"\n"])

def _coordinate(start,end,string):
    srow=string[:start].count('\n')+1 # starting row
    scolsplitlines=string[:start].split('\n')
    if len(scolsplitlines)!=0:
        scolsplitlines=scolsplitlines[len(scolsplitlines)-1]
    scol=len(scolsplitlines)# Ending Column
    lrow=string[:end+1].count('\n')+1
    lcolsplitlines=string[:end].split('\n')
    if len(lcolsplitlines)!=0:
        lcolsplitlines=lcolsplitlines[len(lcolsplitlines)-1]
    lcol=len(lcolsplitlines)+1# Ending Column
    return '{}.{}'.format(srow, scol),'{}.{}'.format(lrow, lcol)#, (lrow, lcol)

def coordinate(pattern, string,txt):
    line=string.splitlines()
    start=string.find(pattern)  # Here Pattern Word Start
    end=start+len(pattern) # Here Pattern word End
    srow=string[:start].count('\n')+1 # starting row
    scolsplitlines=string[:start].split('\n')
    if len(scolsplitlines)!=0:
        scolsplitlines=scolsplitlines[len(scolsplitlines)-1]
    scol=len(scolsplitlines)# Ending Column
    lrow=string[:end+1].count('\n')+1
    lcolsplitlines=string[:end].split('\n')
    if len(lcolsplitlines)!=0:
        lcolsplitlines=lcolsplitlines[len(lcolsplitlines)-1]
    lcol=len(lcolsplitlines)# Ending Column
    #txt.tag_add('red','{}.{}'.format(srow, scol),'{}.{}'.format(lrow, lcol))
    #txt.tag_configure('red',foreground='red')
    return '{}.{}'.format(srow, scol),'{}.{}'.format(lrow, lcol)#, (lrow, lcol)
# Color Configuration

def check(k={}):
    if k['COMMENT']!=None:
    	return 'comment','red'
    elif k['BUILTIN']!=None:
    	return 'builtin','VioletRed'
    elif k['STRING']!=None:
    	return 'string','green'
    elif k['KEYWORD']!=None:
    	return 'keyword','orange'
    else:
    	return 'ss','NILL'
#    print _coordinate(start,end,c,txt)
txtfilter=re.compile(ty(),re.S)
#idprog = re.compile(r"\s+(\w+)", re.S)
class ColorLight:
    def __init__(self, txtbox=None):
        self.txt=txtbox
    def trigger(self):
        val=self.txt.get('1.0','end')
        if len(val)==1:
            return
        for i in ['comment','builtin','string','keyword']:
            self.txt.tag_remove(i,'1.0','end')
        for i in txtfilter.finditer(val):
            start=i.start()
            end=i.end()-1
            #print start,end
            tagtype,color=check(k=i.groupdict())
            if color!='NILL':
                ind1,ind2=_coordinate(start,end,val)
                #print ind1, ind2
                self.txt.tag_add(tagtype,ind1, ind2)
                self.txt.tag_config(tagtype,foreground=color)
                #Tkinter.Text.tag_configure
#        for i in idprog.finditer(val):
#            start=i.start()
#            end=i.end()-1
#            ind1,ind2=_coordinate(start,end,val)
#            self.txt.tag_add('BLUE',ind1, ind2)
#            self.txt.tag_config("BLUE",foreground='grey')
#            #Tkinter.Text.tag_configure

"""
root=Tkinter.Tk()
txt=Tkinter.Text(root)
txt.pack(expand='yes')
store=ColorLight(txtbox=txt)
Tkinter.Button(root, text='Click me', command=lambda:store.trigger()).pack()
root.mainloop()
"""
