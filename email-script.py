import os
import base64
while(true):
	os.system("rm text")
	os.system("wget http://35.193.111.112:9000/status/text")
	#change the url as needed
	#This saves the status file in the file named "text"
	os.system("rm status-file.txt")
	os.system("touch status-file.txt")
	os.system("cat text | grep -A 1 Mode: > status-file.txt")
	os.system("cat text | grep -A 1 Unreachable_nodes: >> status-file.txt")
	email_text=open("status-file.txt","r")
	msg=email_text.read()
	email_text.close()
	encoded2=str(base64.b64encode(bytes(msg,"utf-8")))
	mnp = encoded2.lstrip("b")
	mp=mnp.lstrip("'")
	mp=mp.rstrip("'")
	mp2="".join(('"',mp))
	mp2="".join((mp2,'"'))
	# need to create and save a commd.txt file in the same directory as this python file
	newfl=open("commd.txt","r")
	dataa=newfl.read()
	newfl.close()
	mp3="".join((dataa, mp2))
	mp4="}'"
	mp3="".join((mp3, mp4))
	os.system(mp3)
	
	##### checks every 6 hours, so you will get atmost 4 emails per day 
	sleep(21600)

	



	

	
	
	
	
		
