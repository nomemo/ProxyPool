
from bs4 import BeautifulSoup
from settings import USER_AGENTS as USER_AGENTS


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