class Fraction:
	def __init__(self, a, b=1):
		self.__num = a
		if b == 0:
			raise ZeroDivisionError
		self.__den = b
		self.simplify()
		
	def getNum(self):
		return self.__num
		
	def getDen(self):
		return self.__den

	def approximate(self, digitPlaces: int = None):
		val = self.__num / self.__den
		if digitPlaces:
			return f"%.{digitPlaces}f" % val
		return val
		
	def simplify(self):
		x = self.gcd(self.__num, self.__den)
		self.__num = self.__num // x
		self.__den = self.__den // x

	def gcd(self, a, b):
		if b == 0:
			return a
		else:
			return self.gcd(b, a % b)
	
	def __eq__(self,other):
		return self.getNum() == other.getNum() and self.getDen() == other.getDen()

	def __add__(self, other):
		a = self.getNum() # a/b
		b = self.getDen()
		x = other.getNum() # x/y
		y = other.getDen()
		return Fraction(a*y + x*b, b*y)
	
	def __sub__(self, other):
		x = other.getNum() # x/y
		y = other.getDen()
		return self + Fraction(-x, y) # invoke __add__
	
	def __mul__(self, other):
		return Fraction(self.getNum() * other.getNum(), self.getDen() * other.getDen())
	
	def __truediv__(self, other):
		return Fraction(self.getNum() * other.getDen(), other.getNum() * self.getDen())
	
	def __pow__(self, exp):
		if exp == 0:
			return Fraction(1, 1) # 1
		elif exp < 0:
			return Fraction(self.getDen(), self.getNum())**exp
		else:
			return self * self**(exp-1)
		
	def __repr__(self):
		if self.__den == 1 :
			return str(self.__num)
		else:
			return str(self.__num) + "/" + str(self.__den)
		
# TEST
if __name__ == "__main__":
	while True:
		inp = int(input('enter numerator > '))
		if inp == 'quit' or inp == 'exit':
			exit()
		den = int(input('enter denominator > '))
		if den == 'quit' or den == 'exit':
			exit()
		if den == 0:
			print("Can't have denominator as 0, division by 0 is not allowed.")
			continue
		print(Fraction(inp, den))
	# below are test cases that worked, just delete the loop above to access
	print(Fraction(81, 9)) # expecting 9
	print(Fraction(7, 3)) # expecting 7/3
	print(Fraction(2, 4) * Fraction(4, 2)) # expecting 1
	print(Fraction(4, 2) / Fraction(4, 2)) # expecting 1 
	print(Fraction(10, 2) + Fraction(5, 1)) # expecting 10
	print(Fraction(4, 2) - Fraction(2, 1)) # expecting 0