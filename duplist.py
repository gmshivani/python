l=[1,1,2,2,3,4,5]
dup=[]
for i in l:
	if i not in dup:
		dup.append(i)


dup=[]
i=1
1 not in dup->true
dup=[1]
i=1
1 not in dup->false
i=2
2 not in dup->true
dup=[1,2]
i=2
2 not in dup->false
i=3
3 not in dup->true
dup=[1,2,3]
i=4
4 not in dup->true
dup=[1,2,3,4]
i=5
5 not in dup->true
dup=[1,2,3,4,5]