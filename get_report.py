from threading import Thread
from Queue import Queue
import urllib2
import MySQLdb
import os.path

q = Queue() # Queue
NUM = 10
# 5203
JOBS = 134

def get_report(arguments):   
    filename = str(arguments[0])
    url = str(arguments[1])    
    path = 'report/' + filename + '.html'
    
    if os.path.isfile(path) == False :    
        opener = urllib2.build_opener()
        opener.addheaders.append(('Cookie', 'csrftoken=5VgBrCS2js54dliRESusfmlWsbEzmh7h; sessionid=pssdtr9zn5wmw1ugymdodgplbyekzke0'))
        content = opener.open(url).read()   
    
        f = open(path, 'w') 
        f.write(content)
        f.close()
        
        print "[DONE]..." + filename
    else:
        print "[PASS]..." + filename 

def working():
    while True:
        arguments = q.get()
        get_report(arguments)

        q.task_done()

for i in range(NUM):   
    t = Thread(target=working)    
    t.setDaemon(True)    
    t.start()

db = MySQLdb.connect(host="localhost", user="root", passwd="XXXXX", db="malware")
cur = db.cursor() 
cur.execute("SELECT * FROM `malwr` WHERE is_getreport = false")

for row in cur.fetchall() :
    q.put([row[0], row[7]])

q.join()
