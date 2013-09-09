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