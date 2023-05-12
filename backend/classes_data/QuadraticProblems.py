from .problem import Problem, Step
from .Quadratic import QuadraticEquation


problems = [
    Problem(Equation='$x^2 + 3x + 2 = 0$', 
        Steps=[Step(result = '$a = 1$,  $b = 3$,  $c = 2$', 
                    step ='Identify the a, b, c values', 
                    feedback="Correct and in this case: \n a = 1, b = 3, c = 2",
                    wrong_steps =(
                         Step(step ='Subtract 2 from both side',
                              feedback = "Incorrect: always set the equation to zero"),
                         Step(step ='Apply distributive property', 
                              feedback = "Incorrect: there is nothing to distribute"),
                         Step(step ='Divide by x for both side',
                              feedback = "Incorrect: not all terms have an x")
                         )
                     ),
               Step(result = f'$x = {QuadraticEquation(1, 3, 2).stepThree()}$', 
                    step ='Plug values for quadratic formula', 
                    feedback='Correct: make sure to \n plug in the correct values',
                    wrong_steps =(
                         Step(step='Answer is the sum of a, b, c values',
                              feedback = "Insteporrect: values can not be added with different x terms"),
                         Step(step ='Answer is a and b', 
                              feedback = "Incorrect: Take consideration if the c value as well"),
                         Step(step ='Answer is the product of a, b, and c',
                              feedback = "Incorrect: The product of a, b and c does not make the equation true")
                         )
                     ),
                Step(result = '$ x = -1$ and $x = -2$', 
                    step ='x = -1, x = -2', 
                    feedback='Correct: Congrats you have \n solve the problem',
                    wrong_steps = (
                         Step(step='x = 1, x = 2',
                              feedback = "Incorrect: check your signs"),
                         Step(step ='x = 3, x = 4', 
                              feedback = "Incorrect: check your arithmetics"),
                         Step(step =' x = 0, x = 1',
                              feedback = "Incorrect: check your arithmetics")
                         )
                    )
               ]
          ),

     Problem(Equation='$-3 + 5x + 2x^2 = 0$', 
        Steps=[Step(result = '$a = 2$, $b = 5$, $c = -3$', 
                    step ='a = 2, b = 5, c = -3', 
                    feedback="Correct and in this case: \n a = 2, b = 5, c = -3",
                    wrong_steps =
                    (Step(step='a = 5 b = -3 c = 2',
                          feedback = "Incorrect: a, b, and c values are assign by the degree of x terms"),
                     Step(step ='a = -3, b = 5, c = 2', 
                          feedback = "Incorrect:  a, b, and c values are assign by the degree of x terms"),
                     Step(step ='a = 2, b = 5, c =3',
                          feedback = "Incorrect:  a, b, and c values are assign by the degree of x terms")
                     ),
                     ),
               Step(result = f'${QuadraticEquation(5, -3, 2)}$', 
                    step ='Use quadratic formula', 
                    feedback='Correct: make sure to \n plug in the correct values',
                    wrong_steps =
                    (Step(step='Add 3 to both side',
                          feedback = "Incorrect:always set the equation to zero "),
                     Step(step ='Factor out x', 
                          feedback = "Incorrect: there are no like terms"),
                     Step(step ='Subtract 5x from both side',
                          feedback = "Incorrect: always set the equation to zero")
                     ),
                     ),
                Step(result = '$ x = 1/2$ or $x = -3$', 
                    step ='x = 1/2, x = -3', 
                    feedback='Correct: Congrats you have \n solve the problem',
                    wrong_steps =
                    (Step(step='x = 1/4, x = 1',
                          feedback = "Incorrect: Check your arithematics"),
                     Step(step ='x = 0, x =3', 
                          feedback = "Incorrect:Check your arithematics "),
                     Step(step ='x = -1/2, x = 3',
                          feedback = "Incorrect: Check your signs")
                     )
                    ),

               ],
               ),
     
     Problem(Equation='$6x + 2x^2 + 4$', 
        Steps=[Step(result = '$a = 2$, $b = 6$, $c = 4$', 
                    step ='a = 2, b = 6, c = 4', 
                    feedback="Correct: a, b, and c are \n identify base on \n their corresponding x term",
                    wrong_steps =
                    (Step(step='a = 4 b = 6 c = 2',
                          feedback = "Incorrect: a, b, and c values are assign by the degree of x terms "),
                     Step(step ='a = a = 2 b = 4 c = 6', 
                          feedback = "Incorrect: a, b, and c values are assign by the degree of x terms"),
                     Step(step ='a = 6 b = 2 c = 4',
                          feedback = "Incorrect: a, b, and c values are assign by the degree of x terms")
                     ),
                     ),
               Step(result = f'${QuadraticEquation(4, 6, 2)}$', 
                    step ='Use quadratic formula', 
                    feedback='Correct: make surestepto \n plug in the correct values',
                    wrong_steps =
                    (Step(step='Divide everything by x',
                          feedback = "Incorrect: not all values contain x"),
                     Step(step ='Divide both side by 4', 
                          feedback = "Incorrect: 4 is not a common factor"),
                     Step(step ='Subtract 6x from both side',
                          feedback = "Incorrect: always set the equation to zero")
                     ),
                     ),
                Step(result = '$x = -1$ or $x = -2$', 
                    step ='x = -1, x = -2', 
                    feedback='Correct: Congrats you have \n solve the problem',
                    wrong_steps =
                    (Step(step='x = 1, x = 2',
                          feedback = "Incorrect: check your signs"),
                     Step(step ='x = -1/2, x = -2', 
                          feedback = "Incorrect: check your arithmetics"),
                     Step(step ='x = -1, x = -3',
                          feedback = "Incorrect: check your arithmetics")
                     ),
                    )
                ]
     
               )
          ]