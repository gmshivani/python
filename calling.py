a = 5
def func():
    c = 10
    d = c + a

    # Calling globals()
    globals()['a'] = d
    print(a)
# Driver Code
func()