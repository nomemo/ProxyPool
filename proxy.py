import urllib2
import json
import random
import threading
import Queue
import sys
from bs4 import BeautifulSoup



QWorkerCount = 12

if len(sys.argv) > 1:
	proxyForTest = sys.argv[1]
else: 
	print "Add target url for testing proxy"
	exit()

send_headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
}

USER_AGENTS = [
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
  "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
  "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
  "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
  "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
  "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
  "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
  "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]




#Bad quality
def fetchXicidaili():
	requestURL = 'http://www.xicidaili.com/nn/'
	proxyOri = []

	request = urllib2.Request(requestURL, headers=send_headers)
	page = urllib2.urlopen(request)
	soup = BeautifulSoup(page)
	# print soup.prettify()
	trs = soup.select('tr')
	count = len(trs)
	for index in range(1, count):
		tr = trs[index]
		tds = tr.select('td')

		a = float(tds[7].select('div')[0]['title'].replace(u'\u79d2',u''))
		b = float(tds[8].select('div')[0]['title'].replace(u'\u79d2',u''))
		proxy = {tds[6].text.lower() : tds[2].text + ":" + tds[3].text}
		proxyOri.append(proxy)
	return proxyOri


def fetchIP84():
	proxyArray = []
	requestURLs = [
		"http://ip84.com/gn/1",
		"http://ip84.com/gn/2",
		"http://ip84.com/gn/3",
		"http://ip84.com/gn/4",
		"http://ip84.com/gn/5",
		"http://ip84.com/gn/6",
 	]
	for requestURL in requestURLs:
		request = urllib2.Request(requestURL, headers=send_headers)
		page = urllib2.urlopen(request)
		soup = BeautifulSoup(page)
		trs = soup.select('tr')
		count = len(trs)
		for index in range(1, count):
			tr = trs[index]
			tds = tr.select('td')
			proxy = {tds[4].text.lower() : tds[0].text + ":" + tds[1].text}
			# print proxy
			proxyArray.append(proxy)
	return proxyArray


def fetchMimiIP():
	proxyArray = []
	requestURLs = [
		"http://www.mimiip.com/gngao/1",
		"http://www.mimiip.com/gngao/2",
		"http://www.mimiip.com/gngao/3",
	]
	for requestURL in requestURLs:
		request = urllib2.Request(requestURL, headers=send_headers)
		page = urllib2.urlopen(request)
		soup = BeautifulSoup(page)
		trs = soup.select('tr')
		count = len(trs)
		for index in range(1, count):
			tr = trs[index]
			tds = tr.select('td')
			proxy = {tds[4].text.lower() : tds[0].text + ":" + tds[1].text}
		# 	# print proxy
			proxyArray.append(proxy)
	return proxyArray



def makeRequest(proxy):
	print "makeRequest: "
	print proxy
	proxy_support = urllib2.ProxyHandler(proxy)
	opener = urllib2.build_opener(proxy_support)
	urllib2.install_opener(opener)
	i_headers = {'User-Agent':random.choice(USER_AGENTS)}
	req = urllib2.Request(proxyForTest)

	try:
		html = urllib2.urlopen(req, timeout = 5)
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



couldUse = []

workQueue = Queue.Queue(0)
proxyOri =  fetchIP84()
print "IP84 Get %d" %(len(proxyOri))

for word in proxyOri: 
	workQueue.put(word) 

proxyOri = fetchMimiIP()
print "MimiIP Get %d" %(len(proxyOri))

for word in proxyOri: 
	workQueue.put(word) 

for i in range(QWorkerCount): 
	name = "Thread " + str(i)
	thread = WorkThread(name, workQueue)
	thread.start() 
workQueue.join()

with open('proxy.json', 'w') as f:
  f.write(json.dumps(couldUse))
print "Exiting Main Thread"



# For Proxy Test.
# makeRequest({"http":"106.2.78.15:80"})


