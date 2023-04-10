from dataclasses import dataclass

@dataclass
class Limit():
    function: str
    variable: str
    limit: int | float | str # use 'inf' or '-inf' for infinities
    sided_limit: any = None # use -1 for negative, 1 for positive, or None

    def latexify(self):
        latex_limit = (self.limit == 'inf' and '\infty' or self.limit == '-inf' and '-\infty' or self.limit)
        if self.sided_limit and latex_limit == self.limit: # ignore infinity
            latex_limit = latex_limit + r'^{'+ (self.sided_limit == -1 and '-' or self.sided_limit == 1 and '+') +'}'
        return r'$\lim_{' + self.variable + r'\to' + latex_limit + '} ' + self.function + r'$'

    def __str__(self) -> str:
        return self.latexify()

@dataclass
class Integral():
    function: str
    lower: str
    upper: str
    variable: str # for dx/dy/du, etc

    def latexify(self):
        return r'$\[ \int_{' + self.lower + r'}^{' + self.upper + r'}' + function + r'\,' + ('d'+self.variable) + r' \]$'
    
    def __str__(self) -> str:
        return self.latexify()

@dataclass
class E_Sum():
    function: str = ''
    index_variable: str = 'n'
    index_start: str = '1'
    index_limit: str = '\infty' # can use 'inf'

    def latexify(self):
        latex_limit = self.index_limit == 'inf' and '\infty' or self.index_limit
        return r'$\[ \sum_{' + self.index_variable + '=' + self.index_start + r' }^{' + latex_limit + r'} ' + self.function + r'\]$'

    def __str__(self) -> str:
        return self.latexify()
    
@dataclass
class Derivative():
    function: str
    variable_respect_to: str
    order: int = 1 # > 0

    def latexify_quotient(self):
        if self.order == 1:
            return r'$\frac{' + 'd'+self.function + '}{' + 'd'+self.variable_respect_to +'}$'
        else:
            return r'$\frac{' + r'd^{' + str(self.order) + '}'+self.function + '}{' + 'd'+self.variable_respect_to+r'^{' + str(self.order) + '}' +'}$'
    
    def latexify_partial(self):
        if self.order == 1:
            return r'$\frac{' + r'\partial'+self.function + '}{' + r'\partial'+self.variable_respect_to +'}$'
        else:
            return r'$\frac{' + r'\partial^{' + str(self.order) + '}'+self.function + '}{' + r'\partial'+self.variable_respect_to+r'^{' + str(self.order) + '}' +'}$'

    def latexify_function(self):
        return r'$\[ ' + self.function + r"' (" + self.variable_respect_to + r')]$'
    
    def __str__(self) -> str:
        return self.latexify_quotient()

if __name__ == '__main__':
    # test
    import sys
    sys.path.append(r'C:\Users\steve\Documents\CS\ci102_repositories\my_branch')
    from mathimg import make_img
    
    # change here to do your test and look at output.png (run this file)
    make_img( Limit('x^2 + 4', 'x', 'inf').latexify(), 'output', 'png' )