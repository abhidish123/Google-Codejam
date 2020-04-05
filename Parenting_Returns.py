from collections import namedtuple as ndd
import sys
sys.setrecursionlimit(10**6)
Ivl = ndd("Ivl", ["start", "end"])


def go(cameron, jamie, rmn):
    if not rmn:
        return cameron, jamie, rmn
    if not cameron or cameron[-1].end <= rmn[0].start:
        new_cameron = cameron + [rmn[0]]
        new_rmn = rmn[1:]
        r = go(new_cameron, jamie, new_rmn)
        if r:
            return r
    if not jamie or jamie[-1].end <= rmn[0].start:
        new_jamie = jamie + [rmn[0]]
        new_rmn = rmn[1:]
        r = go(cameron, new_jamie, new_rmn)
        if r:
            return r
    return None


tt=int(input())
for t in range(1,tt+1):
	N=int(input())
	lns=str(N)+"\n"
	for i in range(N):
		l=list(input().split())
		lns+=str(l[0])+" "+str(l[1])+"\n"
	lns = lns.split("\n")
	orgTime = list(Ivl(*map(int, lns[i].split(" "))) for i in range(1, int(lns[0]) + 1))
	times = sorted(orgTime, key=lambda x: x.start)
	r = go([], [], times)
	if not r:
	    print("Case #"+str(t)+": IMPOSSIBLE")
	else:
	    schedule = "".join(y[0] for y in sorted([("C", orgTime.index(x)) for x in r[0]] + [("J", orgTime.index(x)) for x in r[1]], key=lambda x: x[1]))
	    print("Case #"+str(t)+": "+str(schedule))
