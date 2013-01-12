print("What is p, s and d?\n")
p = float(raw_input('> '))
s = float(raw_input('> '))
d = float(raw_input('> '))

def fare(p,s,d):
	Y1 = p + 5*0.01*s
	#print "Y1 is %f\n" % Y1
	Y2 = 5*0.01*d/12;
	#print "Y2 is %f\n" % Y2
	return Y1 + Y2;
#print "p is %f\n" %p
#print "s is %f\n" %s
#print "d is %f\n" %d

X = fare(p,s,d)
print "The fare is: %f" % X

