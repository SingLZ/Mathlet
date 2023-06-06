from .problem import Problem, Step
from .Fraction import Fraction as Frac

problems = [
    Problem(Equation=f'{Frac(1,2)} + {Frac(1,3)}', 
        Steps=[Step(result = rf'{Frac(3, 6)} + {Frac(2, 6)}', 
                    step = f'Multiply {Frac(1,2)} by {Frac(3,3)}\nand {Frac(1,3)} by {Frac(2,2)}',
                    feedback='Correct. Before adding, we need to multiply both fraction\nto be under the same denominator.',
                    wrong_steps=
                        (Step(step= f'Multiply {Frac(1,2)} by {Frac(2,2)}\nand {Frac(1,3)} by {Frac(3,3)}',
                              feedback='Incorrect. This will not result in the same denominators.'),
                         Step(step= f'Multiply {Frac(1,2)} by {Frac(2,1)}\nand {Frac(1,3)} by {Frac(3,1)}',
                              feedback='Incorrect. Find the least common denomintor (LCD) by listing out mutiples of both denominators to find the LCD.'),
                         Step(step= f'Divide {Frac(1,2)} by {Frac(3,3)}\nand {Frac(1,3)} by {Frac(2,1)}',
                              feedback='Incorrect. Instead of dividing, try multiplying to get both fractions under a common denominator.')
                        ),
                    ),
                Step(result = r'$\frac{3+2}{6}$', 
                     step = r'$\frac{3+2}{6}$', 
                     feedback = 'Correct. We can combine the fractions because they have the same denominator ',
                     wrong_steps=
                        (Step(step=r'$\frac{3+2}{6+6}$',
                              feedback = 'Incorrect. The denominator are the same, so you can combine the fractions under one denominator.'),
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
                              feedback = 'Incorrect. Does not need further multiplication, fractions are already under the same denominator.'),
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
                    feedback='Correct. Multiplying fractions does not require fractions to be under the same denominator, we can multiply across.',
                    wrong_steps=
                        (Step(step= r'$\frac{10+1}{2*3}$',
                              feedback='Incorrect. We solve for multiplication before addition.'),
                         Step(step= r'$\frac{10+1}{2+3}$',
                              feedback='Incorrect. We solve for multiplication before subtraction.'),
                         Step(step= rf'Multiply {Frac(10,2)} by {Frac(3,3)} and {Frac(1,3)} by {Frac(2,2)}',
                              feedback='Incorrect. We are not subtracting or adding the fractions, they do not need to be under the same denominator.')
                        ),
                    ),
                Step(result = f'{Frac(10,6)}', 
                     step = f'{Frac(10,6)}', 
                     feedback = 'Correct. We multiply the denominator together.',
                     wrong_steps=
                        (Step(step=f'{Frac(10,5)}',
                              feedback = 'Incorrect. Check your calculations, you added the denominators insead of multiplying.'),
                         Step(step = f'{Frac(10,2)}', 
                              feedback = 'Incorrect. Check your calculations, you multiplied the denominator wrong.'),
                         Step(step = f'{Frac(10,9)}',
                              feedback = 'Incorrect. Check your calculations, you multiplied the denominator wrong.')
                        ),
                    ), 
                Step(result = repr(Frac(5,3)), 
                     step = f'Simplify = {Frac(5,3)}', 
                     feedback = f'Correct. 10 = 5x2 and 6 = 3x2. Greatest common factor is 2 so we divide the num and den by 2 to get {Frac(5,3)}',
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
                    feedback='Correct. We can factor the numberator to simplify the fraction',
                    wrong_steps=
                        (Step(step= r'$\frac{(x+8)(x+1)}{x^{2} + 7x + 10}$',
                              feedback='Incorrect. 8x + 1x does not equal 6x.'),
                         Step(step= r'$\frac{(x-4)(x-2)}{x^{2} + 7x + 10}$',
                              feedback=r'Incorrect. This is equal to $x^{2}-6x+8$'' which is not the same numerator'),
                         Step(step= r'$\frac{(x+4)(x+4)}{x^{2} + 7x + 10}$',
                              feedback='You factored incorrectly.')
                        ),
                    ),
                Step(result = r'$\frac{(x+4)(x+2)}{(x+5)(x+2)}$', 
                     step = r'$\frac{(x+4)(x+2)}{(x+5)(x+2)}$', 
                     feedback = 'Correct. We can factor the denominator to simplify the fraction',
                     wrong_steps=
                        (Step(step=r'$\frac{(x+4)(x+2)}{(x+5)(x+5)}$',
                              feedback = 'You factored incorrectly. 5x + 5x does not equal 7x'),
                         Step(step = r'$\frac{(x+4)(x+2)}{(x+10)(x+1)}$', 
                              feedback = 'Incorrect. 10x + x does not equal 7x'),
                         Step(step = r'$\frac{(x+4)(x+2)}{(x-5)(x-2)}$',
                              feedback = r'Incorrect. This is equal to $x^{2}-7x+10$'' which is not the same denominator')
                        ),
                    ), 
                Step(result = r'$\frac{(x+4)}{(x+5)}$', 
                     step = r'Simplify: $\frac{(x+4)}{(x+5)}$', 
                     feedback = 'Correct. (x+2) on both the num and denominator, cancel them out', 
                     wrong_steps=
                        (Step(step = f'Simplify: {Frac(4,5)}', 
                              feedback = 'Incorrect. You cannot cancel out the x'),
                         Step(step = r'Simplify: $\frac{(x+2)}{(x+2)}$', 
                              feedback = 'Incorrect. Are you sure you can cancel out (x+4) with (x+5)?'), 
                         Step(step = 'No more work can be done', 
                              feedback = 'Incorrect. You can simplify the fraction more')
                        )
                    )
                ]
            )
        ]