# -*- coding: utf-8 -*-

# Python + PyQt4 By Skylar 
#
# Creado: 29 - sep - 2013
#      Por: xskylarx
# xskyofx@gmail.com
# Por favor si modificas algo haz referencia al autor.
import subprocess
import re

def enLinea(host):

	

	ping = subprocess.Popen(
	    ["ping", "-n", "2", host],
	    stdout = subprocess.PIPE,
	    stderr = subprocess.PIPE
	)

	out, error = ping.communicate()
	m = re.search('bytes=', str(out))



	if m:
		#print ("OK")
		return True
		    
		           
	else:
	    #print ("OFF")
	    return False

#enLinea('www.google.om')