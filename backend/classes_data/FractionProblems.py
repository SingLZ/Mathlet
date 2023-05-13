from .problem import Problem, Step
from .Fraction import Fraction as Frac

problems = [
    Problem(Equation=f'{Frac(1,2)} + {Frac(1,3)}', 
        Steps=[Step(result = rf'{Frac(3, 6)} + {Frac(2, 6)}', 
                    step = f'Multiply {Frac(1,2)} by {Frac(3,3)}\nand {Frac(1,3)} by {Frac(2,2)}',
                    feedback='Correct. Before adding,\nwe need to multiply both fraction\nto be under the same denominator.',
                    wrong_steps=
                        (Step(step= f'Multiply {Frac(1,2)} by {Frac(2,2)}\nand {Frac(1,3)} by {Frac(3,3)}',
                              feedback='Incorrect. This will not result in the same denominators.'),
                         Step(step= f'Multiply {Frac(1,2)} by {Frac(2,1)}\nand {Frac(1,3)} by {Frac(3,1)}',
                              feedback='Incorrect. Find the least common denomintor (LCD) by\n listing out mutiples of both denominators\nto find the LCD.'),
                         Step(step= f'Divide {Frac(1,2)} by {Frac(3,3)}\nand {Frac(1,3)} by {Frac(2,1)}',
                              feedback='Incorrect. Instead of dividing, try multiplying to\nget both fractions under a common denominator.')
                        ),
                    ),
                Step(result = r'$\frac{3+2}{6}$', 
                     step = r'$\frac{3+2}{6}$', 
                     feedback = 'Correct. We can combine the fractions because they have the same denominator ',
                     wrong_steps=
                        (Step(step=r'$\frac{3+2}{6+6}$',
                              feedback = 'Incorrect. The denominator are the same,\nso you can combine the fractions\nunder one denominator.'),
                         Step(step = f'Multiply {Frac(1,2)} by {Frac(3,3)}\nand {Frac(1,3)} by {Frac(2,2)}', 
                              feedback = 'Incorrect. Same denominator, do not multiply.'),
                         Step(step = 'No more work can be done',
                              feedback = 'Incorrect. You can simplify.')
                        ),
                    ), 
                Step(result = repr(Frac(5,6)), 
                     step = f'Complete Sum: {Frac(5,6)}', 
                     feedback = 'Correct. Add the numerator.', 
                     wrong_steps=
                        (Step(step = rf'Multiply by {Frac(6,6)}', 
                              feedback = 'Incorrect. Does not need\nfurther multiplication, fractions are\nalready under the same denominator.'),
                         Step(step = rf'Convert into {Frac(3,6)} + {Frac(2,6)}', 
                              feedback = 'Incorrect. Add the factions together.'), 
                         Step(step = 'No more work can be done', 
                              feedback = 'Incorrect. You can simplify this.')
                        )
                    )
                ]
            ), 
    Problem(Equation=f'{Frac(10,2)} * {Frac(1,3)}', 
        Steps=[Step(result = r'$\frac{10}{2*3}$', 
                    step = r'$\frac{10}{2*3}$',
                    feedback='Correct. Multiplying fractions\ndoes not require fractions to be\nunder the same denominator,\nwe can multiply across.',
                    wrong_steps=
                        (Step(step= r'$\frac{10+1}{2*3}$',
                              feedback='Incorrect. We solve for multiplication before addition.'),
                         Step(step= r'$\frac{10+1}{2+3}$',
                              feedback='Incorrect. We solve for multiplication before subtraction.'),
                         Step(step= rf'Multiply {Frac(10,2)} by {Frac(3,3)} and {Frac(1,3)} by {Frac(2,2)}',
                              feedback='Incorrect. We are not subtracting or adding the fractions,\nthey do not need to be under the same denominator.')
                        ),
                    ),
                Step(result = f'{Frac(10,6)}', 
                     step = f'{Frac(10,6)}', 
                     feedback = 'Correct. We multiply the denominator together.',
                     wrong_steps=
                        (Step(step=f'{Frac(10,5)}',
                              feedback = 'Incorrect. Check your calculations,\nyou added the denominators\ninsead of multiplying.'),
                         Step(step = f'{Frac(10,2)}', 
                              feedback = 'Incorrect. Check your calculations,\nyou multiplied the denominator wrong.'),
                         Step(step = f'{Frac(10,9)}',
                              feedback = 'Incorrect. Check your calculations,\nyou multiplied the denominator wrong.')
                        ),
                    ), 
                Step(result = repr(Frac(5,3)), 
                     step = f'Simplify = {Frac(5,3)}', 
                     feedback = f'Correct. 10 = 5 * 2 and 6 = 3 * 2\nGreatest common factor is 2\nso we divide the num and den by 2 to get {Frac(5,3)}',
                     wrong_steps=
                        (Step(step = f'Simplify = {Frac(10,6)}', 
                              feedback = 'Incorrect. Further simplification can be done.'),
                         Step(step = f'Simplify = {Frac(5,6)}', 
                              feedback = 'Incorrect. Remember to simplify the denominator as well using the GCF.'), 
                         Step(step = f'Simplify = {Frac(10,3)}', 
                              feedback = 'Incorrect. Remember to simplify the numerator as well using the GCF.')
                        )
                    )
                ]
            ), 
            #r'$\frac{3+2}{6}$'
    Problem(Equation=r'$\frac{x^{2} + 6x + 8}{x^{2} + 7x + 10}$', 
        Steps=[Step(result = r'$\frac{(x+4)(x+2)}{x^{2} + 7x + 10}$',
                    step = r'$\frac{(x+4)(x+2)}{x^{2} + 7x + 10}$',
                    feedback='Correct. We can factor the numberator\nto simplify the fraction',
                    wrong_steps=
                        (Step(step= r'$\frac{(x+8)(x+1)}{x^{2} + 7x + 10}$',
                              feedback='Incorrect. 8x + 1x does not equal 6x.'),
                         Step(step= r'$\frac{(x-4)(x-2)}{x^{2} + 7x + 10}$',
                              feedback=r'Incorrect. This is equal to $x^{2}-6x+8$''\nwhich is not the same numerator'),
                         Step(step= r'$\frac{(x+4)(x+4)}{x^{2} + 7x + 10}$',
                              feedback='You factored incorrectly.')
                        ),
                    ),
                Step(r'$\frac{3+2}{6}$', 'Combine fractions due to same denominator',
                     ('Add denominators and numerators', rf'Multiply {Frac(1,2)} by {Frac(3,3)} and {Frac(1,3)} by {Frac(2,2)}', 'No more work can be done'),
                     feedback='Step 2'),
                Step(repr(Frac(5,6)), 'Complete sum', 
                     (rf'Multiply by {Frac(6,6)}', rf'Convert into {Frac(3,6)} + {Frac(2,6)}', r'No more work can be done'),
                     feedback='Step 3')
                ],
        )
    #Problem([f'{Frac(1, 2)} + {Frac(1, 3)}', f'{Frac(3, 6)} + {Frac(2, 6)}', r'$\frac{3+2}{6}$', repr(Frac(5, 6))], 
            #[r'Multiply $\frac{1}{2}$ by $\frac{3}{3}$ and $\frac{1}{3}$ by $\frac{2}{2}$', 'Combine fractions due to same denominator', 'Complete sum'],
            #[(r'Multiply $\frac{1}{2}$ by $\frac{2}{2}$ and $\frac{1}{3}$ by $\frac{3}{3}$', r'Multiply $\frac{1}{2}$ by $\frac{2}{1}$ and $\frac{1}{3}$ by $\frac{3}{1}$', r'Divide $\frac{1}{2}$ by $\frac{3}{3}$ and $\frac{1}{3}$ by $\frac{2}{1}$'), ('Add denominators and numerators', r'Multiply $\frac{1}{2}$ by $\frac{3}{3}$ and $\frac{1}{3}$ by $\frac{2}{2}$', 'No more work can be done'), (r'Multiply by $\frac{6}{6}$', r'Convert into $\frac{3}{6}$ + $\frac{2}{6}$', r'No more work can be done')])
]

trial = problems[0]