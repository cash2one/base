# _*_ coding:utf-8 _*_

print "How old are you?",
age = raw_input()   #注意和input（）的区别
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So,you're %r old, %r tall and %r heavy." % (age, height, weight)

print "Test input() and raw_input():"
print "How much the egg?",
price = input()
print "are you tall?",
tall = raw_input()

print "the egg is %r, and I am %r tall." % (price, tall)
