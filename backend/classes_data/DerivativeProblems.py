from .problem import Problem, Step
from .CalculusNotation import Derivative as Deri
from .Fraction import Fraction as Frac

# $x^{2} + xy + y^{2} = 7$
problems = [
    Problem(Equation=f'Solve for {Deri("y", "x")}: $x^{2} + y = 4$', # this displays on main question button
           Steps=[Step(result = f'{Deri("", "x")}$(x^{2})$ + {Deri("", "x")}(y) = {Deri("", "x")}(4)', #this displays when you click on right answer
                        step=f'{Deri("", "x")}$(x^{2})$ + {Deri("", "x")}(y) = {Deri("", "x")}(4)',
                        feedback=f'Correct! We need to take the derivative of each term first, with respect to x.',
                        wrong_steps=
                        (Step(step=f'{Deri("", "x")}$(x^{2})$ + {Deri("", "x")}(y) = 4',
                              feedback=f'Incorrect. Whatever we do on one side, do the operation on the other side as well.\nTake the derivative of each term.'),
                         Step(step=f'$x^{2}$ + y = {Deri("", "x")}(4)',
                              feedback=f'Incorrect. Whatever we do on one side, do the operation on the other side as well.\nTake the derivative of each term.'),
                         Step(step=f'y = 4 - $x^{2}$',
                              feedback=f'Incorrect. Solve for {Deri("y", "x")} not y.')
                        ),
                    ), # end of step 1  
                    Step(result = f'2x + {Deri("", "x")}(y) = {Deri("", "x")}(4)',
                        step=f'{Deri("", "x")}$(x^{2})$ = 2x',
                        feedback=f'Correct! You used the Power Rule: \n{Deri("", "x")}$(x^{{n}})$ = $nx^{{(n-1)}}$',
                        wrong_steps=
                        (Step(step=f'{Deri("", "x")}$(x^{2})$ = {Frac(1,3)}$x^{3}$',
                              feedback=f'Incorrect. Take the derivative not the integral.\nUse the derivative\'s Power Rule.'),
                         Step(step=f'{Deri("", "x")}$(x^{2})$ = $x^{2}$',
                              feedback=f'Incorrect. Use the Power Rule: {Deri("", "x")}$(x^{{n}})$ = $nx^{{(n-1)}}$'),
                         Step(step=f'{Deri("", "x")}$(x^{2})$ = 2',
                              feedback=f'Incorrect. Use the Power Rule: {Deri("", "x")}$(x^{{n}})$ = $nx^{{(n-1)}}$')
                        ),
                    ), # end of step 2
                    Step(result = f'2x + {Deri("y", "x")} = {Deri("", "x")}(4)',
                        step=f'{Deri("", "x")}(y) = {Deri("y", "x")}',
                        feedback=f'Correct! Use the chain rule:\n{Deri("", "x")}(y) = {Deri("", "y")}(y){Deri("y", "x")}\n{Deri("", "x")}(y) = {Deri("y", "x")}',
                        wrong_steps=
                        (Step(step=f'{Deri("", "x")}(y) = {Deri("x", "y")}',
                              feedback=f'Incorrect. Use the chain rule: (Differentiate outer function)*(Differentiate inner function)'),
                         Step(step=f'{Deri("", "x")}(y) = 1',
                              feedback=f'Incorrect. Take the derivative with respect to x, not y'),
                         Step(step=f'{Deri("", "x")}(y) = x',
                              feedback=f'Incorrect. Use the chain rule: (Differentiate outer function)*(Differentiate inner function)')
                        ),
                    ), # end of step 3
                    Step(result = f'2x + {Deri("y", "x")} = 0',
                        step=f'{Deri("", "x")}(4) = 0',
                        feedback=f'Correct! The derivative of a constant is always 0',
                        wrong_steps=
                        (Step(step=f'{Deri("", "x")}(4) = {Frac(1,4)}x',
                              feedback=f'Incorrect. Recall what the derivative of a constant is'),
                         Step(step=f'{Deri("", "x")}(4) = 4x',
                              feedback=f'Incorrect. Take the derivative not the integral'),
                         Step(step=f'{Deri("", "x")}(4) = $x^{4}$',
                              feedback=f'Incorrect. Recall what the derivative of a constant is')
                        ),
                    ), # end of step 4
                    Step(result = f'{Deri("y", "x")} = -2x',
                        step=f'{Deri("y", "x")} = -2x',
                        feedback=f'Correct! We move the variable to the right-hand side to solve for {Deri("y", "x")}.\nYou have completed the problem!',
                        wrong_steps=
                        (Step(step=f'{Deri("y", "x")} = 2x',
                              feedback=f'Incorrect. Remember to change its sign when\nmoving the variable to the right-hand side.'),
                         Step(step=f'{Deri("y", "x")} = -{Frac(1,2)}x',
                              feedback=f'Incorrect. Solve for {Deri("y", "x")} by\n subtracting, not dividing.'),
                         Step(step=f'{Deri("y", "x")} = 0',
                              feedback=f'Incorrect. What happened to the 2x on the left-hand side?')
                        ),
                    ) # end of step 5
            ]
        ), # end of Problem 1
    # start of Problem 2
    Problem(Equation=f'Solve for {Deri("","x")}($e^{{x}}$sin(5x))', # this displays on main question button
           Steps=[Step(result = f'{Deri("","x")}($e^{{x}}$)sin(5x) + $e^{{x}}${Deri("","x")}(sin(5x))', #this displays when you click on right answer
                        step=f'{Deri("","x")}($e^{{x}}$)sin(5x) + $e^{{x}}${Deri("","x")}(sin(5x))',
                        feedback=f'Correct! We use the differentiation product rule:\n{Deri("","x")}(f(x))g(x) = \n{Deri("","x")}(f(x))g(x)\n+f(x){Deri("","x")}(g(x))',
                        wrong_steps=
                        (Step(step=f'{Deri("","x")}($e^{{x}}$)sin(5x) - $e^{{x}}${Deri("","x")}(sin(5x))',
                              feedback=f'Incorrect. Review the product rule. We add, not subtract.'),
                         Step(step=f'{Deri("","x")}($e^{{x}}$)sin(5x)',
                              feedback=f'Incorrect. You are missing the second half of the product rule.'),
                         Step(step=f'{Deri("","x")}($e^{{x}}$)sin(5x) + {Deri("","x")}($e^{{x}}$)sin(5x)',
                              feedback=f'Incorrect. Review the product rule.\nYou have to take the derivative of sin(5x) as well.')
                        ),
                    ), # end of step 1  
                    Step(result = f'$e^{{x}}$sin(5x) + $e^{{x}}${Deri("","x")}(sin(5x))',
                        step=f'{Deri("", "x")}$(e^{{x}})$ = $e^{{x}}$',
                        feedback=f'Correct! Derivative of\n$e^{{x}}$ is $e^{{x}}$',
                        wrong_steps=
                        (Step(step=f'{Deri("", "x")}$(e^{{x}})$ = x$e^{{x}}$',
                              feedback=f'Incorrect. The derivative of $e^{{x}}$ is itself.'),
                         Step(step=f'{Deri("", "x")}$(e^{{x}})$ = e',
                              feedback=f'Incorrect. The derivative of $e^{{x}}$ is itself.'),
                         Step(step=f'{Deri("", "x")}$(e^{{x}})$ = $e^{{x}}$ + C',
                              feedback=f'Incorrect. Find the derivative, not the integral')
                        ),
                    ), # end of step 2
                    Step(result = f'$e^{{x}}$sin(5x) + 5$e^{{x}}$cos(5x)',
                        step=f'{Deri("","x")}(sin(5x)) = 5cos(5x)',
                        feedback=f'Correct, you have completed the problem!\n{Deri("","x")}(sin(5x)) = cos(5x)\n{Deri("","x")}(5x) = 5\nUse Chain Rule to get 5cos(5x)',
                        wrong_steps=
                        (Step(step=f'{Deri("","x")}(sin(5x)) = cos(5x)',
                              feedback=f'Incorrect. Take the derivative of the inner function as well\nReference the chain rule.'),
                         Step(step=f'{Deri("","x")}(sin(5x)) = -{Frac(1,5)}cos(5x)',
                              feedback=f'Incorrect. Find the derivative, not the integral'),
                         Step(step=f'{Deri("","x")}(sin(5x)) = 5sin(5x)',
                              feedback=f'Incorrect. The derivative of sin(x) is not sin(x).')
                        ),
                    ) # end of step 3
            ]
        ), # end of Problem 2
    # start of Problem 3
    Problem(Equation=f'F(x) = $cos^{2}(x)$, find $F^{{\'}}$(x)', # this displays on main question button
           Steps=[Step(result = f'$F^{{\'}}$(x) = {Deri("","x")}($g^{2}$){Deri("","x")}(cos(x)), let g = cos(x)', #this displays when you click on right answer
                        step=f'{Deri("","x")}($g^{2}$){Deri("","x")}(cos(x))',
                        feedback=f'Correct! We use the chain rule:\n(Differentiate outer function)*(Differentiate inner function)',
                        wrong_steps=
                        (Step(step=f'{Deri("","x")}(cos(x))',
                              feedback=f'Incorrect. Review the chain rule.\nWhat about the outer function $g^{2}$'),
                         Step(step=f'{Deri("","x")}(2x)',
                              feedback=f'Incorrect. Review the chain rule:\n(Differentiate outer function)*(Differentiate inner function)'),
                         Step(step=f'{Deri("","x")}($cos(x)^{2}$)',
                              feedback=f'Incorrect. This step is the same as the question. No progression.')
                        ),
                    ), # end of step1  
                    Step(result = f'= 2cos(x){Deri("","x")}(cos(x))',
                        step=f'{Deri("","x")}($g^{2}$) = 2g = 2cos(x)',
                        feedback=f'Correct! You used the Power Rule: {Deri("", "x")}$(x^{{n}})$ = $nx^{{(n-1)}}$\nand then substitute g back in',
                        wrong_steps=
                        (Step(step=f'{Deri("","x")}($g^{2}$) = {Frac(1,3)}$g^{3}$ = {Frac(1,3)}$cos(x)^{3}$',
                              feedback=f'Incorrect. Take the derivative not the integral.\nUse the derivative\'s Power Rule.'),
                         Step(step=f'{Deri("","x")}($g^{2}$) = 2g = 2sin(x)',
                              feedback=f'Incorrect. g = cos(x), substitute g back in.'),
                         Step(step=f'{Deri("","x")}($g^{2}$) = 2$g^{2}$ = 2$cos(x)^{2}$',
                              feedback=f'Incorrect. Use the Power Rule: {Deri("", "x")}$(x^{{n}})$ = $nx^{{(n-1)}}$')
                        ),
                    ), # end of step 2
                    Step(result = f'= -2cos(x)sin(x)',
                        step=f'{Deri("","x")}(cos(x)) = -sin(x)',
                        feedback=f'Correct! Derivative of cos(x) is -sin(x).',
                        wrong_steps=
                        (Step(step=f'{Deri("","x")}(cos(x)) = cos(x)',
                              feedback=f'Incorrect. Derivative of cos(x) is not itself.'),
                         Step(step=f'{Deri("","x")}(cos(x)) = sin(x) + C',
                              feedback=f'Incorrect. Find the derivative, not the integral'),
                         Step(step=f'{Deri("","x")}(cos(x)) = sin(x)',
                              feedback=f'Incorrect. Derivative of cos(x) is negative.')
                        ),
                    ), # end of step 3
                    Step(result = f'$F^{{\'}}$(x) = -sin(2x)',
                        step=f'-2cos(x)sin(x) = -sin(2x)',
                        feedback=f'Correct, you have completed the problem!\nSimplify using double angle trig indentity:\nsin(2x)=2cos(x)sin(x)',
                        wrong_steps=
                        (Step(step=f'-2cos(x)sin(x) = sin(2x)',
                              feedback=f'Incorrect. Where did the negative go?'),
                         Step(step=f'-2cos(x)sin(x) = -cos(2x)',
                              feedback=f'Incorrect. Simplify using double angle indentity:\nsin(2x)=2cos(x)sin(x)'),
                         Step(step=f'-2cos(x)sin(x) = -2sin(2x)',
                              feedback=f'Incorrect. Simplify using double angle trig indentity:\nsin(2x)=2cos(x)sin(x)')
                        ),
                    ) # end of step 4
            ]
        ) # end of Problem 3
]