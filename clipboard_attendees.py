print 'hello attendee script is running'
import re
from Tkinter import Tk

r = Tk()
#r.withdraw()
txt = r.clipboard_get()

#for c in txt:
#	print c
#r.destroy()

#r.clipboard_clear()
#r.clipboard_append('i can has clipboardz?')
#r.destroy()


#txt = """Mark A. Hubbard; Chad A. Sclavi <casclavi@spscommerce.com>; Anthony Sarumi <asarumi@spscommerce.com>; Laura L. Johnson <lljohnson@spscommerce.com>; Elaina Perleberg <eperleberg@spscommerce.com>; John P. Myers <jpmyers@spscommerce.com>; Paul M. Jorde <pmjorde@spscommerce.com>; Nathaniel R. Andersen <nrandersen@spscommerce.com>; Sean Curran <scurran@spscommerce.com>; Ashlie Olslund <aolslund@spscommerce.com>; John Caneday <jcaneday@spscommerce.com>; Katie A. Fisher <kafisher@spscommerce.com>; Shannon Schulte <sschulte@spscommerce.com>; Tyler G. Berndt <tgberndt@spscommerce.com>"""


txt = re.sub('<.*?>','',txt)
txt = txt.replace(' ;',';')
txt = txt.replace('; ',';')
txt = txt.strip()


output = "Attendees\n"
for name in txt.split(';'):
   if name == "Steve Czeck":
      continue

   if name.count(' ') == 2:
      first,middle,last = name.split(' ') 
      if middle != 'St.':
         name = first + " " + last
   elif name.count(' ') == 3:
      first,middle,lastA,lastB = name.split(' ') 
      name = first + " " + lastA + " " + lastB
   output += "*" + name + "\n"

output += "*Steve Czeck <note taker>\n"
output += "\nNotes\n*"

#print output

r.clipboard_append(output)
r.destroy()

