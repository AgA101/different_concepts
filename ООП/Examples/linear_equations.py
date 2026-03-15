class Equation:
    def __init__(self, k: float, b: float):
        self.k = k
        self.b = b

    def output(self):
        if k == 0:
            print(f'y = {self.b}')
        elif b == 0:
            print(f'y = {self.k} * x')
        else:
            print(f'y ={self.k} * x + {self.b}')

    def intersection(self, equation):
        if self.k == equation.k:
            return None, None
        x = (equation.b - self.b) / (self.k - equation.k)
        y = self.k * x + self.b
        return x, y
    
if __name__ == '__main__':
    k, b = map(int,input().split())
    equation = Equation(k,b)
    equation_2 = Equation(2,2)
    equation.output()
    equation_2.output()
    x,y = equation.intersection(equation_2)
    print('x =',x,'y =',y)
        
