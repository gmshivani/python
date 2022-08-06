import array as arr
a=arr.array('i',[1,2,3,4,5])
#append method
a.append(6)
for i in range(0,6):
    print(a[i],end=" ")
print()
#insert method
a.insert(3,7)
for i in range(0,7):
    print(a[i])