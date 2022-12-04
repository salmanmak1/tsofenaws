class calc():
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        #fix
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def mul(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b
#end of class

def sum(args):
    sum = 0
    for num in args:
        sum += num
    return sum

def main():
    a = 50
    b = 20
    calc1 = calc(a,b)
    print(str(a) + '+' + str(b) + ' =', calc1.add())
    print(str(a) + '-' + str(b) + ' =', calc1.sub())
    print(str(a) + '*' + str(b) + ' =', calc1.mul())
    print(str(a) + '/' + str(b) + ' =', calc1.div())


if __name__ == '__main__':
    main()
