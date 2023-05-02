from .problem import Problem, Step
from .Fraction import Fraction as Frac

problems = [
    Problem(Equation=f'{Frac(1,2)} + {Frac(1,3)}', 
        Steps=[Step(result=rf'{Frac(3, 6)} + {Frac(2, 6)}', 
                    step=rf'Multiply {Frac(1,2)} by {Frac(3,3)} and {Frac(1,3)} by {Frac(2,2)}', 
                    wrong_steps=(
                        Step(step=rf'Multiply {Frac(1,2)} by {Frac(2,2)} and {Frac(1,3)} by {Frac(3,3)}', feedback='Wrong Step'), 
                        Step(step=rf'Multiply {Frac(1,2)} by {Frac(2,1)} and {Frac(1,3)} by {Frac(3,1)}', feedback='Wrong Step'), 
                        Step(step=rf'Divide {Frac(1,2)} by {Frac(3,3)} and {Frac(1,3)} by {Frac(2,1)}', feedback='Wrong Step')
                    ),
                    feedback='Step 2'
                    ),
                Step(result=r'$\frac{3+2}{6}$', step='Combine fractions due to same denominator',
                     wrong_steps=(
                        Step(step='Add denominators and numerators', feedback='Wrong Step'), 
                        Step(step=rf'Multiply {Frac(1,2)} by {Frac(3,3)} and {Frac(1,3)} by {Frac(2,2)}', feedback='Wrong Step'), 
                        Step(step='No more work can be done', feedback='Wrong Step')
                        ),
                     feedback='Step 3'),
                Step(result=repr(Frac(5,6)), step='Complete sum', 
                     wrong_steps=(Step(rf'Multiply by {Frac(6,6)}', feedback='Wrong Step'), 
                                  Step(rf'Convert into {Frac(3,6)} + {Frac(2,6)}', feedback='Wrong Step'), 
                                  Step(r'No more work can be done', feedback='Wrong Step')
                                  ),
                     feedback='Step 4')
                ],
        )
    #Problem([f'{Frac(1, 2)} + {Frac(1, 3)}', f'{Frac(3, 6)} + {Frac(2, 6)}', r'$\frac{3+2}{6}$', repr(Frac(5, 6))], 
            #[r'Multiply $\frac{1}{2}$ by $\frac{3}{3}$ and $\frac{1}{3}$ by $\frac{2}{2}$', 'Combine fractions due to same denominator', 'Complete sum'],
            #[(r'Multiply $\frac{1}{2}$ by $\frac{2}{2}$ and $\frac{1}{3}$ by $\frac{3}{3}$', r'Multiply $\frac{1}{2}$ by $\frac{2}{1}$ and $\frac{1}{3}$ by $\frac{3}{1}$', r'Divide $\frac{1}{2}$ by $\frac{3}{3}$ and $\frac{1}{3}$ by $\frac{2}{1}$'), ('Add denominators and numerators', r'Multiply $\frac{1}{2}$ by $\frac{3}{3}$ and $\frac{1}{3}$ by $\frac{2}{2}$', 'No more work can be done'), (r'Multiply by $\frac{6}{6}$', r'Convert into $\frac{3}{6}$ + $\frac{2}{6}$', r'No more work can be done')])
]

trial = problems[0]
if __name__ == "__main__": # test only
    for part in trial.getCurrentWrongSteps():
        print(part.feedback)