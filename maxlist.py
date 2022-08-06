mylist = []
size = int(input('enter the elements'))

print('Enter',str(size),'positive numbers')

for i in range(size):
    data = int(input())
    mylist.append(data)

max = 0
for data in mylist:
    if data > max:
        max = data

print('The largest number in list is', max)
