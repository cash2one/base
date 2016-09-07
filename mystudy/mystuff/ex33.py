i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)


    i = i + 1
    print "Number now:", numbers
    print  "At the bottle i is %d" % i


print "The numbers:"

for num in numbers:
    print num


# function rewrite the shell above.
def fun_while(num):
    i = 0
    numbers = []
    while i < num:
        print "At the top i is %d" % i
        numbers.append(i)


        i = i + 1
        print "Number now:", numbers
        print  "At the bottle i is %d" % i


    print "The numbers:"

    for num in numbers:
        print num

print "Please enter a number to start:"
num_input = input("> ")
fun_while(num_input)
