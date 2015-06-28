#!/usr/bin/env python
# -*- coding: utf-8 -*-  

__version__ = '1.0'
__author__ = 'BaCde'

__doc__ = """
Bing Search http://www.bacdewu.com

by BaCde # Insight-labs
email:glacier@insight-labs.org
for Python 2.7
"""

import re
import urllib
import urllib2
import logging
import math
import urlparse

def get(url):

	user_agent = 'User-Agent: Mozilla/5.0 ' \
			+ '(Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.4) ' \
			+ 'Gecko/20070515 Firefox/2.0.0.4'
	try:
		request = urllib2.Request(url)
		request.add_header('User-Agent', user_agent)

		logging.debug('Get.get - getting url ' + url)

		result = urllib2.urlopen(request)

	except: raise RuntimeError('unable to open url')

	return result


if __name__ == '__main__':
	import os
	import sys
	import time

	import signal
	signal.signal(signal.SIGINT, lambda signum, frame: sys.exit())

	if len(sys.argv) < 2:
		print 'usage:', os.path.basename(sys.argv[0]), 'query'

		sys.exit()

	pages = 30
	q = sys.argv[1]
	url_list = []
	fileh=open('./result/Bing.txt','w')
	for i in range(1, pages):
		p 	= (i - 1) * 10 + 1 
		#url = 'https://www.bing.com/search?q='+ q + '&go=%E6%8F%90%E4%BA%A4&form=QBLH' + '&pq='+q + '&first=' + str(p)  
		url = 'https://www.bing.com/search?' 
		#print url
		query = urllib.urlencode({'q':q, 'go':'%E6%8F%90%E4%BA%A4', 'form':'QBLH','pq':q,'first':p})
		#print(url+query)
		result = get(url + query)
		#result = get(url)
		content = result.read()
		#print content
		type=sys.getfilesystemencoding()
		content=content.decode("UTF-8").encode(type)
		

		tokens = re.findall('<li\s+class="b_algo"><div class="b_title"><h2><a\s+href="(.*?)"\s+target="_blank"\s+h="(.*?)">(.*?)</a></h2>',content)
		tokens2 = re.findall('<li\s+class="b_algo"><h2><a\s+href="(.*?)"\s+target="_blank"\s+h="(.*?)">',content)
		#result.close
		for token in tokens:			
			url = token[0]
			#title = token[2]
			url= url.strip()
			#print url
			url_list.append((urllib.unquote(url)))
			#fileh.write(url+"\n")
			#print item
		
		for token2 in tokens2:			
			url = token2[0]
			#title = token[2]
			url= url.strip()
			#print url

			url_list.append((urllib.unquote(url)))
			#fileh.write(url+"\n")
			#print item	
	domain_list = []
	url_lists={}.fromkeys(url_list).keys()
	for item in url_lists:
		parsedTuple = urlparse.urlparse(item)
		domain = parsedTuple[1]
		if domain not in domain_list:
			domain_list.append(domain)
			fileh.write(item+"\n")
			#print item

		#domain_list.append(parsedTuple[1])	

	fileh.close()