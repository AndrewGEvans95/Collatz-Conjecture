#Solution to Find Longest Collatz Sequence

A dynamic progrmaming solution inspired by Project Euler Problem 14 to 
find the longest Collatz sequence 
given any starting integer.

##Project Euler Problem 14

>The following iterative sequence is defined for >the set of positive integers:
>n → n/2 (n is even)
>n → 3n + 1 (n is odd)
>Using the rule above and starting with 13, we >generate the following sequence:
>13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
>It can be seen that this sequence (starting at >13 and finishing at 1) contains 10 terms. >Although it has not been proved yet (Collatz 
>Problem), it is thought that all starting >numbers finish at 1.
>Which starting number, under one million, >produces the longest chain?

##Solution

Code 
```python
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
print str(longestrunvalue) + " had the longest run with " + 
str(longestrunsteps) + " steps"
```