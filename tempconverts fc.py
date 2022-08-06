class temperature:
    t = 0
    def __init__(self,t):
        self.t = t
    def celsius(self):
        c = float((self.t-32)*5/9)
        return(c)
fahren = 98
temp = temperature(fahren)
print(temp.celsius())