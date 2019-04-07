t=int(input())
for i in range(1,t+1):
	n=int(input())
	s=list(str(input()))
	for j in range(len(s)):
		if s[j]=='S':
			s[j]='E'
		elif(s[j]=='E'):
			s[j]='S'
	print("Case #%d: "%i+(''.join(s)))
