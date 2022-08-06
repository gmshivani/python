class calculation1:
    def summation(self,a,b):
        return a+b

class calculation2:
    def multiplication(self,a,b):
        return a*b

class derived(calculation1,calculation2):
    def divide(selfself,a,b):
        return a/b

d=derived()
print(d.summation(10,20))
print(d.multiplication(10,20))
print(d.divide(10,20))

print(issubclass(calculation2,calculation1))
print(issubclass(derived,calculation2))
print(isinstance(d,derived))




