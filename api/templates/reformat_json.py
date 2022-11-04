import os, sys

text=open('read.txt').read()
text=text.replace("\n  ","").replace("'",'"')
new=open('write.txt','w')
new.write(text)
new.close()