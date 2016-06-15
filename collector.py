
from bs4 import BeautifulSoup
from settings import USER_AGENTS as USER_AGENTS
import random
import urllib2

def fetchBigdaili():
	proxyArray = []
	requestURLs = [
		"http://www.bigdaili.com/dailiip/1/1.html#ip",
		"http://www.bigdaili.com/dailiip/1/2.html#ip",
		"http://www.bigdaili.com/dailiip/1/3.html#ip",
		"http://www.bigdaili.com/dailiip/1/4.html#ip",
		"http://www.bigdaili.com/dailiip/1/5.html#ip",
		"http://www.bigdaili.com/dailiip/1/6.html#ip",
		"http://www.bigdaili.com/dailiip/1/7.html#ip",
		"http://www.bigdaili.com/dailiip/1/8.html#ip",
		"http://www.bigdaili.com/dailiip/1/9.html#ip",
		"http://www.bigdaili.com/dailiip/1/10.html#ip",
		"http://www.bigdaili.com/dailiip/3/1.html",
		"http://www.bigdaili.com/dailiip/3/2.html",
		"http://www.bigdaili.com/dailiip/3/3.html",
		"http://www.bigdaili.com/dailiip/3/4.html",
		"http://www.bigdaili.com/dailiip/3/5.html",
		"http://www.bigdaili.com/dailiip/3/6.html",
		"http://www.bigdaili.com/dailiip/3/7.html",
		"http://www.bigdaili.com/dailiip/3/8.html",
		"http://www.bigdaili.com/dailiip/3/9.html",
		"http://www.bigdaili.com/dailiip/3/10.html",
    ]
	for requestURL in requestURLs:
		i_headers = {'User-Agent':random.choice(USER_AGENTS)}
		request = urllib2.Request(requestURL, headers=i_headers)
		page = urllib2.urlopen(request)
		soup = BeautifulSoup(page)
		trs = soup.select('tr')
		count = len(trs)
		for index in range(1, count):
			tr = trs[index]
			tds = tr.select('td')
			proxy = {tds[3].text.lower() : tds[0].text + ":" + tds[1].text}
			# print proxy
			proxyArray.append(proxy)
	return proxyArray

def fetchXsdaili():
	proxyArray = []
	requestURLs = [
		"http://www.xsdaili.com/index.php?s=/index/mfdl/type/3/p/1.html",
		"http://www.xsdaili.com/index.php?s=/index/mfdl/type/3/p/2.html",
		"http://www.xsdaili.com/index.php?s=/index/mfdl/type/3/p/3.html",
		"http://www.xsdaili.com/index.php?s=/index/mfdl/type/3/p/4.html",
		"http://www.xsdaili.com/index.php?s=/index/mfdl/type/3/p/5.html",
		"http://www.xsdaili.com/index.php?s=/index/mfdl/type/3/p/6.html",
		"http://www.xsdaili.com/index.php?s=/index/mfdl/type/3/p/7.html",
		"http://www.xsdaili.com/index.php?s=/index/mfdl/type/3/p/8.html",
		"http://www.xsdaili.com/index.php?s=/index/mfdl/type/3/p/9.html",
		"http://www.xsdaili.com/index.php?s=/index/mfdl/type/3/p/10.html",
		"http://www.xsdaili.com/mfdl?type=1",
		"http://www.xsdaili.com/mfdl?type=2",
		"http://www.xsdaili.com/mfdl?type=3",
		"http://www.xsdaili.com/mfdl?type=4",
		"http://www.xsdaili.com/mfdl?type=5",
		"http://www.xsdaili.com/mfdl?type=6",
		"http://www.xsdaili.com/mfdl?type=7",
		"http://www.xsdaili.com/mfdl?type=8",
		"http://www.xsdaili.com/mfdl?type=9",
		"http://www.xsdaili.com/mfdl?type=10",
    ]
	for requestURL in requestURLs:
		i_headers = {'User-Agent':random.choice(USER_AGENTS)}
		request = urllib2.Request(requestURL, headers=i_headers)
		page = urllib2.urlopen(request)
		soup = BeautifulSoup(page)
		trs = soup.select('tr')
		count = len(trs)
		for index in range(1, count):
			tr = trs[index]
			tds = tr.select('td')
			proxy = {tds[3].text.lower() : tds[0].text + ":" + tds[1].text}
			# print proxy
			proxyArray.append(proxy)
	return proxyArray

def fetchSwei360():
	proxyArray = []
	requestURLs = [
		"http://www.swei360.com/free/?page=1",
		"http://www.swei360.com/free/?page=2",
		"http://www.swei360.com/free/?page=3",
		"http://www.swei360.com/free/?page=4",
		"http://www.swei360.com/free/?page=5",
		"http://www.swei360.com/free/?page=6",
		"http://www.swei360.com/free/?page=7",
		"http://www.swei360.com/free/?stype=3&page=1",
		"http://www.swei360.com/free/?stype=3&page=2",
		"http://www.swei360.com/free/?stype=3&page=3",
		"http://www.swei360.com/free/?stype=3&page=4",
		"http://www.swei360.com/free/?stype=3&page=5",
		"http://www.swei360.com/free/?stype=3&page=6",
		"http://www.swei360.com/free/?stype=3&page=7",
    ]
	for requestURL in requestURLs:
		i_headers = {'User-Agent':random.choice(USER_AGENTS)}
		request = urllib2.Request(requestURL, headers=i_headers)
		page = urllib2.urlopen(request)
		soup = BeautifulSoup(page)
		trs = soup.select('tr')
		count = len(trs)
		for index in range(1, count):
			tr = trs[index]
			tds = tr.select('td')
			proxy = {tds[3].text.lower() : tds[0].text + ":" + tds[1].text}
			# print proxy
			proxyArray.append(proxy)
	return proxyArray


def fetchGoubanjia():
	# http://proxy.goubanjia.com/dayip_1.shtml
	proxyArray = []
	requestURLs = [
		"http://proxy.goubanjia.com/free/gngn/index.shtml",
		"http://proxy.goubanjia.com/free/gwgn/index.shtml",
    ]
	for requestURL in requestURLs:
		i_headers = {'User-Agent':random.choice(USER_AGENTS)}
		request = urllib2.Request(requestURL, headers=i_headers)
		page = urllib2.urlopen(request)
		soup = BeautifulSoup(page)
		trs = soup.select('tr')
		count = len(trs)
		for index in range(1, count):
			tr = trs[index]
			tds = tr.select('td')
			# print tds[0]
			ip = ""
			for child in tds[0].children:
				if child.has_attr('style') and (child['style'] == "display: none;" or child['style'] == "display:none;"):
						# print "JUMP:"
						# print child
						continue
				else:
					# print child.attrs
					ip += child.text
			# print ip
			# print " "
			schemes = tds[3].text.lower().split(',')
			if len(schemes) == 1:
				proxy = { schemes[0] : ip + ":" + tds[1].text}
				proxyArray.append(proxy)
			else:
				proxy = { schemes[0] : ip + ":" + tds[1].text}
				proxyArray.append(proxy)
				proxy = { schemes[1] : ip + ":" + tds[1].text}
				proxyArray.append(proxy)

	return proxyArray


def fetchXicidaili():
	proxyArray = []
	requestURLs = [
		"http://www.xicidaili.com/wn/",
		"http://www.xicidaili.com/wn/2",
		"http://www.xicidaili.com/wn/3",
		"http://www.xicidaili.com/wn/4",
		"http://www.xicidaili.com/wn/5",
    ]
	for requestURL in requestURLs:
		i_headers = {'User-Agent':random.choice(USER_AGENTS)}
		request = urllib2.Request(requestURL, headers=i_headers)
		page = urllib2.urlopen(request)
		soup = BeautifulSoup(page)
		trs = soup.select('tr')
		count = len(trs)
		for index in range(1, count):
			tr = trs[index]
			tds = tr.select('td')
			proxy = {tds[4].text.lower() : tds[0].text + ":" + tds[5].text}
			# print proxy
			proxyArray.append(proxy)
	return proxyArray


# urllib2.HTTPError: HTTP Error 521: 

# def fetchKuaidaili():
# 	proxyArray = []
# 	requestURLs = [
# 		"http://www.kuaidaili.com/free/outha/",
#     ]
# 	for requestURL in requestURLs:
# 		i_headers = {'User-Agent':random.choice(USER_AGENTS)}
# 		request = urllib2.Request(requestURL, headers=i_headers)
# 		page = urllib2.urlopen(request)
# 		soup = BeautifulSoup(page)
# 		trs = soup.select('tr')
# 		count = len(trs)
# 		for index in range(1, count):
# 			tr = trs[index]
# 			tds = tr.select('td')
# 			proxy = {tds[4].text.lower() : tds[0].text + ":" + tds[5].text}
# 			# print proxy
# 			proxyArray.append(proxy)
# 	return proxyArray

# print fetchKuaidaili()	

def fetchNianShao():
	proxyArray = []
	requestURLs = [
        "http://www.nianshao.me/?stype=1&page=1",
        "http://www.nianshao.me/?stype=1&page=2",
        "http://www.nianshao.me/?stype=1&page=3",
        "http://www.nianshao.me/?stype=1&page=4",
        "http://www.nianshao.me/?stype=1&page=5",
        "http://www.nianshao.me/?stype=1&page=6",
        "http://www.nianshao.me/?stype=1&page=7",
        "http://www.nianshao.me/?stype=1&page=8",
        "http://www.nianshao.me/?stype=1&page=9",
        "http://www.nianshao.me/?stype=1&page=10",
        "http://www.nianshao.me/?stype=2&page=1",
        "http://www.nianshao.me/?stype=2&page=2",
        "http://www.nianshao.me/?stype=2&page=3",
        "http://www.nianshao.me/?stype=2&page=4",
        "http://www.nianshao.me/?stype=2&page=5",
        "http://www.nianshao.me/?stype=2&page=6",
        "http://www.nianshao.me/?stype=2&page=7",
        "http://www.nianshao.me/?stype=2&page=8",
        "http://www.nianshao.me/?stype=2&page=9",
        "http://www.nianshao.me/?stype=2&page=10",
    ]
	for requestURL in requestURLs:
		i_headers = {'User-Agent':random.choice(USER_AGENTS)}
		request = urllib2.Request(requestURL, headers=i_headers)
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

# result = fetchNianShao()
# print "result %d" %(len(result))

def fetchIp84():
	proxyArray = []
	requestURLs = [
		"http://ip84.com/gn",
		"http://ip84.com/gn/2",
		"http://ip84.com/gn/3",
		"http://ip84.com/gn/4",
		"http://ip84.com/gn/5",
		"http://ip84.com/gn/6",
		"http://ip84.com/gn/7",
		"http://ip84.com/gn/8",
		"http://ip84.com/gn/9",
		"http://ip84.com/gn/10",
 	]
	for requestURL in requestURLs:
		i_headers = {'User-Agent':random.choice(USER_AGENTS)}
		request = urllib2.Request(requestURL, headers=i_headers)
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
		i_headers = {'User-Agent':random.choice(USER_AGENTS)}
		request = urllib2.Request(requestURL, headers=i_headers)
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


def fetchIP():
	result = []
	temp = fetchIp84()
	result.extend(temp)
	print "fetchIp84: " + str(len(temp))

	temp = fetchBigdaili()
	result.extend(temp)
	print "fetchBigdaili: " + str(len(temp))

	temp = fetchXsdaili()
	result.extend(temp)
	print "fetchXsdaili: " + str(len(temp))

	temp = fetchSwei360()
	result.extend(temp)
	print "fetchSwei360: " + str(len(temp))

	temp = fetchGoubanjia()
	result.extend(temp)
	print "fetchGoubanjia: " + str(len(temp))

	temp = fetchXicidaili()
	result.extend(temp)
	print "fetchXicidaili: " + str(len(temp))

	temp = fetchNianShao()
	result.extend(temp)
	print "fetchNianShao: " + str(len(temp))

	temp = fetchMimiIP()
	result.extend(temp)
	print "fetchMimiIP: " + str(len(temp))

	print len(result)
	return result

fetchIP()