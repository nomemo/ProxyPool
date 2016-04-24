import urllib2
import json
import random
import threading
import Queue
import sys
from bs4 import BeautifulSoup

from settings import USER_AGENTS as USER_AGENTS

QWorkerCount = 12

def makeRequest(proxy):
	print "makeRequest: "
	print proxy
	i_headers = {'User-Agent':random.choice(USER_AGENTS)}

	proxy_support = urllib2.ProxyHandler(proxy)
	opener = urllib2.build_opener(proxy_support)
	urllib2.install_opener(opener)
	
	req = urllib2.Request(proxyForTest, headers=i_headers)

	try:
		html = urllib2.urlopen(req, timeout = 10)
	except Exception, e:
		print e
	else:
		if proxyForTest == html.geturl():
			for key, value in proxy.items():  
				print "\"%s\":\"%s\" checked" % (key, value)  
			# couldUse.append(proxy)
			# doc = html.read()
			# print doc 
			return proxy
		else: 
			return None

class WorkThread(threading.Thread):
	def __init__(self, name, q):
		super(WorkThread, self).__init__()
		self.queue = q
		self.name = name 

	def run(self):
		print "Starting " + self.name

		while True:
			if self.queue.empty():
				print "Exiting " + self.name
				break

			proxy = self.queue.get()
			if proxy != None:
				print "Thread: " + self.name + " Size: " + str(self.queue.qsize())
				proxy = makeRequest(proxy)
				if proxy != None:
					couldUse.append(proxy) 
			self.queue.task_done()


if __name__ == '__main__':

	# if len(sys.argv) > 1:
	# 	proxyForTest = sys.argv[1]
	# else: 
	# 	print "Add target url for testing proxy"
	# 	exit()

	print "begin...."

	couldUse = []

	workQueue = Queue.Queue(0)
	proxyOri =  fetchIP84()
	print "IP84 Get %d" %(len(proxyOri))

	# for word in proxyOri: 
	# 	workQueue.put(word) 
	couldUse.extend(proxyOri)

	proxyOri = fetchMimiIP()
	print "MimiIP Get %d" %(len(proxyOri))

	# for word in proxyOri: 
	# 	workQueue.put(word) 

	couldUse.extend(proxyOri)

	# for i in range(QWorkerCount): 
	# 	name = "Thread " + str(i)
	# 	thread = WorkThread(name, workQueue)
	# 	thread.start() 
	# workQueue.join()

	with open('proxy.json', 'w') as f:
	  f.write(json.dumps(couldUse))
	print "work done"
