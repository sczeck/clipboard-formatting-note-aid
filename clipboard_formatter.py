print 'hello is this script running?'
import HtmlClipboard
from Tkinter import Tk

r = Tk()
#r.withdraw()
txt = r.clipboard_get()

#for c in txt:
#	print c
r.destroy()

#r.clipboard_clear()
#r.clipboard_append('i can has clipboardz?')
#r.destroy()


#input = "bullet.txt"
#output = "bullet.html"

#f = open(input)

out = "<html><body>"

"""
<ul>
<li>Coffee</li>
<li>Milk</li>
</ul> 
"""

"""
<table border="1">
<tr>
<td>row 1, cell 1</td>
<td>row 1, cell 2</td>
</tr>
<tr>
<td>row 2, cell 1</td>
<td>row 2, cell 2</td>
</tr>
</table> 
"""

txt = txt.replace('<', '&lt;')
txt = txt.replace('>', '&gt;')

#left double quote
txt = txt.replace(u'\u201c', '&ldquo;')
#right double quote
txt = txt.replace(u'\u201d', '&rdquo;')
#english dash
txt = txt.replace(u'\u2013', '&ndash;')
#right single quote
txt = txt.replace(u'\u2019', '&rsquo;')
#left single quote
txt = txt.replace(u'\u2018', '&lsquo;')

#this script only works if the data is an ascii string
txt = str(txt)

indent = 0
#for line in f.read().split("\n"):
intable = 0
for line in txt.split("\n"):
	line = line.strip()

	outlength = len(out)
	if line.startswith('['):
		intable = 1
		out += '<table border="1"><tr>'
		endtable = ""
		if line.endswith(']'):
			endtable = "</table>"
			intable = 0
		for seg in line.split('|'):
			seg = seg.strip('\t []')
			out += "<td>" + seg + "</td>"
		out += "</tr>"
		out += endtable
	elif intable:
		out += "<tr>"
		for seg in line.split('|'):
			seg = seg.strip('\t []')
			out += "<td>" + seg + "</td>"
		out += "</tr>"
		if line.endswith(']'):
			intable = 0
			out += "</table>"
	elif line.startswith('*'):
		curindent = line.count('*')
		if curindent < indent:
			out += "</ul>" * (indent - curindent)
		elif curindent > indent:
			out += "<ul>" * (curindent - indent)

	     	indent = curindent
		line = line.lstrip('* ')
		out += "<li>" + line + "</li>"

	elif line == "":
		pass
	else:
		while indent > 0:
			out += "</ul>"
			indent -= 1
		out += "\n<p>" + line
	#print out[outlength:]

while indent > 0:
	out += "</ul>"
	indent -= 1

out += "</body></html>"
f = open("output.htm", "w")
f.write(out)
f.close()
HtmlClipboard.PutHtml(out)



