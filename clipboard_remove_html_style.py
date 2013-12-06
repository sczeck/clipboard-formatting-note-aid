from Tkinter import Tk
import re 

r = Tk()
r.withdraw()
txt = r.clipboard_get()
txt = re.sub(' style=".*?"', "", txt)
txt = re.sub(' class=.*?>', ">", txt)
txt = re.sub(' type=.*?>', ">", txt)
txt = re.sub('<FONT.*?>', "", txt)
txt = re.sub('</FONT>', "", txt)
txt = re.sub('<DIV.*?>', "", txt)
txt = re.sub('</DIV>', "", txt)
txt = re.sub('<TR.*?>', "<TR>", txt)
txt = re.sub('<TD.*?>', "<TD>", txt)
txt = re.sub('<P.*?>', "<P>", txt)
txt = re.sub('<SPAN.*?>', "", txt)
txt = re.sub('</SPAN>', "", txt)
txt = re.sub('&nbsp;', " ", txt)
txt = re.sub(' +', " ", txt)
txt = txt.replace('<P> </P>','')
txt = txt.replace('<BR>','<BR>\n')
txt = txt.strip(' \t\n')
r.clipboard_clear()
r.clipboard_append(txt)
r.destroy()


