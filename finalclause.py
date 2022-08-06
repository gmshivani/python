# Python code to show the use of finally clause

# Raising an exception in try block
try:
    div = 4 // 1
    print(div)
# this block will handle the exception raised
except ZeroDivisionError:
    print("Attepting to divide by zero")
# this will always be executed no matter exception is raised or not
finally:
    print('This is code of finally clause')
