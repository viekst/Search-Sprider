#!/usr/bin/env python

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


def get(url):

	user_agent = 'User-Agent: Mozilla/5.0 ' \
			+ '(Windows; U; Windows NT 5.1; en-GB;) ' \
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
		#2
		#url = 'https://www.google.com/search?'
		p 	= i - 1 
		#2
		#query = urllib.urlencode({'q':q, 'start':p, 'num':'100','gws_rd':'ssl'})
		url = 'https://www.google.com/?q='+q+'&start='+str(p) +'&num=50&gws_rd=ssl#safe=strict&q='+q
		#query = urllib.urlencode({'q':q, 'start':p, 'num':'50','gws_rd':'ssl','safe':'strict'})
		print(url)
		result = get(url)
		content = result.read()
		type=sys.getfilesystemencoding()
		content=content.decode("UTF-8").encode(type)
		#print content
		tokens = re.findall('<div\s+class="rc"\s+data-hveid="(.*?)"><h3 class="r"><a\s+href="(.*?)"',content)
		#1 
		#tokens = re.findall('<li class="g"><h3 class="r"><a\s+href="(.*?)">(.*?)<\/a><\/h3>',content)
		#2
		#tokens = re.findall('<li class="g"><h3 class="r"><a\s+href="(.*?)&amp;(.*?)">(.*?)<\/a><\/h3>',content)
		
		#'<div\s+class="rc"\s+data-hveid="29"><h3 class="r"><a\s+href="(.*?)"\s+monmousedown="return\s+rwt('
		results = []
		#print tokens
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
			url = token[0].replace('/url?q=','')
			#title = token[2]
			print url

			results.append((urllib.unquote(url)))


	#print results