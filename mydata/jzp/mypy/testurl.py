import urllib2


url = "http://www.baidu.com"

u = urllib2.urlopen(url)
localFile = open('res.txt','w')
localFile.write(u.read())
localFile.close()
print "end"

