from sys import argv

script, filename = argv

print "Now, I will open the file %r:" % filename

txt = open(filename)
print txt.read()

print "And finally, close it."
txt.close()
