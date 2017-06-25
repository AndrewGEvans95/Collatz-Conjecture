i = 1000000
count = 0
longestrunsteps=0
longestrunvalue=0
dynamic = {0:0}
while(i>1):
	x=i
	while(x!=1):
		if dynamic.has_key(x):
			count = dynamic.get(x, None)+count
			x=1
		elif x%2==0:
			x = x/2
			count+=1
		else:
			x = (3*x)+1
			count+=1

	#print "Steps taken to solve " + str(i) + ": " + str(count)
	if longestrunsteps<count:
		longestrunsteps=count
		longestrunvalue=i
	dynamic.update({i:count})
	count = 0
	i-=1
print str(longestrunvalue) + " had the longest run with " + str(longestrunsteps) + " steps"