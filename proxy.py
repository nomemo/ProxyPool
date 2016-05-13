import json
import threading
import Queue
import sys
import collector
from tester import makeRequest

QWorkerCount = 12
result = []

class WorkThread(threading.Thread):
	def __init__(self, name, queue, target):
		super(WorkThread, self).__init__()
		self.queue = queue
		self.name = name
		self.target = target

	def run(self):
		print "Starting " + self.name

		while True:
			if self.queue.empty():
				print "Exiting " + self.name
				break

			proxy = self.queue.get()
			if proxy != None:
				print "Thread: " + self.name + " Size: " + str(self.queue.qsize())
				couldUse = makeRequest(proxy, self.target)
				if couldUse == True:
					result.append(proxy)
			self.queue.task_done()

if __name__ == '__main__':
	if len(sys.argv) > 1:
		targetURL = sys.argv[1]
	else: 
		print "Add target url for testing proxy"
		exit()

	print "begin...."

	proxies = []



	proxyOri =  collector.fetchIP84()
	print "IP84 Get %d" %(len(proxyOri))
	proxies.extend(proxyOri)
	proxyOri = collector.fetchMimiIP()
	print "MimiIP Get %d" %(len(proxyOri))
	proxies.extend(proxyOri)
	proxyOri = collector.fetchNianShao()
	print "NianShao Get %d" % (len(proxyOri))
	proxies.extend(proxyOri)

	workQueue = Queue.Queue(0)
	for proxy in proxies:
		workQueue.put(proxy)


	for i in range(QWorkerCount):
		name = "Thread " + str(i)
		thread = WorkThread(name, workQueue, targetURL)
		thread.start()
	workQueue.join()

	print "result %d" %(len(result))
	with open('proxy.json', 'w') as f:
	  f.write(json.dumps(result))
	print "work done"
