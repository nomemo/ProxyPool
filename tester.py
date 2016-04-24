import urllib2
from socket import p

import settings
import random
import threading
import Queue
import json
import requests

def makeAProxyRequest(proxy, testTarget):
    i_headers = {'User-Agent':random.choice(settings.USER_AGENTS)}
    url = testTarget
    print("\n")
    try:
        r = requests.get(url, proxies=proxy, headers = i_headers, timeout=5)
    except Exception, e:
        print "Test Failed: %s By %s \nException: %s" % (testTarget, str(proxy), str(e))
        return False
    else:
        print "Test Successed: %s By %s" % (testTarget, str(proxy))
        return True

def makeFullTestForOneProxy(proxy, type = 'ALL'):
	checkedCount = 0
	for testTarget in settings.TestTargetsCN:
		connected = makeAProxyRequest(proxy, testTarget)
		if connected == True:
			checkedCount += 1

	quality = checkedCount * 1.0 / len(settings.TestTargetsCN)
	return quality


class WorkThread(threading.Thread):

	def __init__(self, name, workQueue, aa=None):
		super(WorkThread, self).__init__()
		self.queue = workQueue
		self.name = name
		self.aa = aa

	def run(self):
		print "Starting " + self.name

		while True:
			if self.queue.empty():
				print "Exiting " + self.name
				break

			proxy = self.queue.get()
			if proxy != None:
				print "Thread: " + self.name + " Size: " + str(self.queue.qsize())
				if self.aa == None:
					makeFullTestForOneProxy(proxy)
				else:
					makeAProxyRequest(proxy, self.aa)

			self.queue.task_done()

# makeFullTestForOneProxy({"http":"115.218.126.59:9000"})

# makeAProxyRequest({"http":"115.218.216.90:9000"}, 'http://www.woshipm.com/')
# makeAProxyRequest({"http":"115.218.216.90:9000"}, 'https://www.baidu.com/')
# makeAProxyRequest({"http":"115.218.216.90:9000"}, 'http://www.v2ex.com/')

jsonFile = "proxy.json"
f = open(jsonFile)
fileData = f.read()
f.close()
proxys = json.loads(fileData)


workQueue = Queue.Queue(0)

for proxy in proxys:
	workQueue.put(proxy)

for i in range(10):
	name = "Thread " + str(i)
	thread = WorkThread(name, workQueue)
	thread.start()
workQueue.join()


