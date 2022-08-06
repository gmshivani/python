def perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n


num = int(input("Enter number:"))
if perfect(num):
    print("number is perfect")
else:
    print("number is not perfect")
