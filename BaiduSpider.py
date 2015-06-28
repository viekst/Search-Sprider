#!/usr/bin/env python


__version__ = '1.0'
__author__ = 'BaCde'

__doc__ = """
Baidu Search http://www.bacdewu.com

by BaCde # Insight-labs
email:glacier@insight-labs.org
for Python 2.7
"""

import re
import urllib
import urllib2
import logging
import math


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

	pages = 10
	q = sys.argv[1]

	for i in range(1, pages):
		#url = 'https://www.bing.com/search?'
		url = 'http://www.baidu.com.eg/s?'
		p 	= (i - 1) * 10
		#query = urllib.urlencode({'q':q, 'go':'%E6%8F%90%E4%BA%A4', 'form':'QBLH','pq':q,'first':p})
		query = urllib.urlencode({'tn':'SE_garhome_a2zqeeas', 'wd':q , 'ie':'utf-8','pn':p})
		#print(url+query)
		result = get(url + query)
		content = result.read()
		type=sys.getfilesystemencoding()
		content=content.decode("UTF-8").encode(type)
		print content
		
		#tokens = re.findall('<li\s+class="b_algo"><div class="b_title"><h2><a\s+href="(.*?)"\s+target="_blank"\s+h="(.*?)">(.*?)</a></h2>',content)
		tokens = re.findall('<a\s+dir=\\"ltr\\"\s+href=\\"(.*?)\\"\s*>(.*?)<\\\/a>',content)
		print tokens
		results = []
		
		"""
		j = 0
		# find current domain
		TempD=re.findall('<cite>(.*?)<\/cite>',content)
		print TempD
		for item in TempD:
			item=item.split('/')[0]
			item=item.rstrip('<')
			item=item.replace('<strong>','')
			domains.append(item)
		"""

		for token in tokens:			
			url = token[0]
			#title = token[2]
			print url

			results.append((urllib.unquote(url)))


	#print results