#!/usr/bin/python3
#print("content-type: text/html")
#print()
import cgi
import os
import cgitb;cgitb.enable(display=1)
form  = cgi.FieldStorage()
fileitem= form.getvalue('filename')
if fileitem.filename:
    fn=os.path.basename(fileitem.filename.replace("\\","/"))
    open('/tmp/'+fn,'wb').write(fileitem.file.read())
    message='The file "'+fn+'" was uploaded successfully'
else:
    message='No file was uploaded'
#message=fileitem
#print(message)
print( """\
content-type:text/html\n
<html>
<body>
<p>%s</p>
</body>
</html>
""" % (message,i))
