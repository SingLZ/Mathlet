class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_discriminant(self):
        return self.b**2 - 4*self.__a*self.__c

    def get_roots(self):
        discriminant = self.get_discriminant()
        if discriminant < 0:
            return None
        elif discriminant == 0:
            root = -self.__b / (2*self.__a)
            return root, None
        else:
            root1 = (-self.__b + discriminant**0.5) / (2*self.__a)
            root2 = (-self.__b - discriminant**0.5) / (2*self.__a)
            return root1, root2
    def __str__(self):
        stepOne = r'\frac{{-({0}) \pm \sqrt{{{0}^2 - 4({1})({2})}}}}{{2({1})}}'.format(self.__b, self.__a, self.__c)
        return stepOne
    
    def stepTwo(self):
        stepTwo = r'\frac{{-{0} \pm \sqrt{{{0}^2 - {1}}}}}{{{2}}}'.format(self.__b, 4*self.__a*self.__c, 2*self.__a)
        return stepTwo
    
    def stepThree(self):
        stepThree = r'\frac{{-({0}) \pm \sqrt{{{1}}}}}{{{2}}}'.format(self.__b, (self.__b**2)-(4*self.__a*self.__c), 2*self.__a)
        return stepThree
    
if __name__=="__main__":
    quad1 = QuadraticEquation(2, -16, -18)
    print(quad1.stepThree())

