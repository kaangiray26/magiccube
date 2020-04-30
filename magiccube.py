#!/usr/bin/python
#-*- encoding: utf-8 -*-
import os
import sys
import random
from random import shuffle

if "w32" in sys.platform:
    os.system("cls")
else:
    os.system("clear && printf '\e[3J'")
#alpha=u'abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ0123456789!@#%^&*:-_+"[]/().,?= '
alpha=u'123456789'
print "ALPHA LENGTH:",len(alpha)
def get():
    tables=[]
    for i in range(0,len(alpha)):
        tables.append("t%d" %(i))
        exec("t%d = []" %(i))
        #exec('t0.append(u"".join(alpha[i]))')
        exec('t0.append(alpha[i])')
    shuffle(t0)
    output=[]
    for t in tables:
        ind=tables.index(t)
        #print "INDEX:",ind
        #print "NOW IN:",t
        if t=="t0":
            pass
        else:
            for i in range(0,len(alpha)):
                hst=t0[:]
                #print "I:%d" %i
                for s in range(0,ind):
                    #exec('print "table:t%s","TO BE DELETED:",t%s[i]' %(s,s))
                    exec('hst.remove(t%s[i])' %(s))
                    #print "HST:[%s]" %("".join(hst))
                exec("ext=list(set(hst) - set(t%s))" %(tables.index(t)))
                try:
                    ft=random.randint(0,len(ext)-1)
                except ValueError:
                    return output
                #print "ft:",ft,"Len:",len(ext),"EXT:","".join(ext)
                exec("t%s.append(ext[ft])" %(tables.index(t)))
                #exec('print "LEN:",len(t%s),"".join(t%s)' %(tables.index(t),tables.index(t)))
        exec('output.append("".join(t%s))' %(tables.index(t)))
        #exec('print "\'".join(t%s)' %(tables.index(t)))
    return output
    print "done."
tryout=input("How long should the output table be?:")
if tryout>len(alpha) or tryout<1:
    print "Error: Length of Output Table must be between 1 and %d!" %(len(alpha))
    exit()
count=0
while True:
    hikey=get()
    sys.stdout.write('\rTry:(%d) LENGTH: %d %s' %(count,len(hikey),""*20))
    sys.stdout.flush()
    if len(hikey)==tryout:
        print "KEY TABLE CREATED SUCCESFULLY!"
        print ""
        print "\n".join(hikey)
        break
    elif len(hikey)>=tryout/1.5:# and len(hikey)<tryout:
        pass
        #print'Try:(%d) LENGTH: %d %s' %(count,len(hikey),""*20)
        #print "\n".join(hikey)
        #print ""
    count+=1
exit()
