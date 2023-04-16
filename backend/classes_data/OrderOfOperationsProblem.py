from .problem import Problem, Step

problems = [
    Problem(Equation='2 + 4 - 9 * 2 = ?',
            Steps=[Step(result='2 + 4 - 18 = ?',
                        step='9 * 2 = 18',
                        feedback='Correct! We use PEMDAS and start with multiplication.',
                        wrong_steps=
                        (Step(result='2 + 4 = 6',
                              feedback='Incorrect. We solve for multiplication before addition.'),
                         Step(result='4 - 9 = -5',
                              feedback='Incorrect. We solve for multiplication before subtraction.'),
                         Step(result='9 - 4 = 5',
                              feedback='Incorrect. We solve for multiplication before subtraction.')
                        ),
                        ),
                    Step(result='6 - 18 = ?',
                        step='2 + 4 = 6',
                        feedback='Correct! We calculate addition and subtraction from left to right, neither takes priority.',
                        wrong_steps=
                        (Step(result='2 + 4 = -2',
                              feedback='Incorrect'),
                         Step(result='2 + 18 = 20',
                              feedback='Incorrect - Check the numbers\' signs'),
                         Step(result='2 - 4 = -2',
                              feedback='Incorrect - Check the numbers\' signs')
                        ),
                        ),
                    Step(result='-12',
                        step='-12',
                        feedback='Correct! We add the two numbers to find the sum. You have completed the problem!', #feedback for the correct answer
                        wrong_steps=
                        (Step(result='24',
                              feedback='Incorrect - Check the numbers\' signs'),
                         Step(result='12',
                              feedback='Incorrect - Check the numbers\' signs'),
                         Step(result='2',
                              feedback='Incorrect - Check the numbers\' signs')
                        ),
                    )
                ],
            ),
    Problem(Equation='4 * 5 - 3 + (2 + 4) = ?',
            Steps=[Step(result='4 * 5 - 3 + 6 = ?',
                        step='2 + 4 = 6',
                        feedback='Correct! We use PEMDAS and start with parentheses',
                        wrong_steps=
                        (Step(result='5 - 3 = 2',
                              feedback='Incorrect. We solve for parentheses before subtraction.'),
                         Step(result='3 + 2 = 5',
                              feedback='Incorrect. We solve for parentheses before addition.'),
                         Step(result='5 + 2 = 7',
                              feedback='Incorrect. We solve for parentheses before addition.')
                        ),
                        ),
                    Step(result='20 - 3 + 6 = ?',
                        step='4 * 5 = 20',
                        feedback='Correct! We move onto multiplication after parentheses',
                        wrong_steps=
                        (Step(result='5 - 3 = 2',
                              feedback='Incorrect. We solve for multiplication before subtraction.'),
                         Step(result='5 + 6 = 11',
                              feedback='Incorrect. We solve for multiplication before addition.'),
                         Step(result='3 - 5 = -2',
                              feedback='Incorrect. We solve for multiplication before subtraction.')
                        ),
                        ),
                    Step(result='17 + 6 = ?',
                        step='20 - 3 = 17',
                        feedback='Correct! We calculate addition and subtraction from left to right, neither takes priority.',
                        wrong_steps=
                        (Step(result='20 - 3 = 23',
                              feedback='Incorrect - Check the numbers\' signs.'),
                         Step(result='20 + 3 = 23',
                              feedback='Incorrect - Check the numbers\' signs.'),
                         Step(result='20 - 3 = -17',
                              feedback='Incorrect - Check the numbers\' signs.')
                        ),
                        ),
                    Step(result='23',
                        step='23',
                        feedback='Correct! We add the two numbers to find the sum. You have completed the problem!',
                        wrong_steps=
                        (Step(result='17',
                              feedback='Incorrect - Check the numbers\' signs.'),
                         Step(result='22',
                              feedback='Incorrect - Check the numbers\' signs.'),
                         Step(result='24',
                              feedback='Incorrect - Check the numbers\' signs.')
                        ),
                        ), 
                ]  
            ),
    Problem(Equation='2 - 6 * (5 - 1) / 2 = ?',
            Steps=[Step(result='2 - 6 * 4 / 2 = ?',
                        step='(5 - 1) = 4',
                        feedback='Correct! We use PEMDAS and start with parentheses',
                        wrong_steps=
                        (Step(result='2 - 6 = -4',
                              feedback='Incorrect. We solve for parentheses before subtraction.'),
                         Step(result='6 * 5 = 30',
                              feedback='Incorrect. We solve for parentheses before multiplication.'),
                         Step(result='1 / 2 = 0.5',
                              feedback='Incorrect. We solve for parentheses before division.')
                        ),
                        ),
                    Step(result='2 - 24 / 2 = ?',
                        step='6 * 4 = 24',
                        feedback='Correct! We calculate addition and subtraction from left to right, neither takes priority.',
                        wrong_steps=
                        (Step(result='2 - 6 = -4',
                              feedback='Incorrect. We solve for multiplication before subtraction.'),
                         Step(result='2 * 4 = 8',
                              feedback='Incorrect - Check the values that should be multiplied.'),
                         Step(result='2 / 2 = 1',
                              feedback='Incorrect - Check the values that we should operate on.')
                        ),
                        ),
                    Step(result='2 - 12 = ?',
                        step='24 / 2 = 12',
                        feedback='Correct! We calculate addition and subtraction from left to right, neither takes priority.',
                        wrong_steps=
                        (Step(result='2 - 24 = -22',
                              feedback='Incorrect - We solve for division before subtraction.'),
                         Step(result='2 - 24 = 26',
                              feedback='Incorrect - We solve for division before subtraction.'),
                         Step(result='2 / 2 = 1',
                              feedback='Incorrect - Check the values that we should operate on.')
                        ),
                        ),
                    Step(result='-10',
                        step='-10',
                        feedback='Correct! We subtract the two numbers to find the difference. You have completed the problem!',
                        wrong_steps=
                        (Step(result='14',
                              feedback='Incorrect - Check the numbers\' signs.'),
                         Step(result='20',
                              feedback='Incorrect - Check the numbers\' signs.'),
                         Step(result='-14',
                              feedback='Incorrect - Check the numbers\' signs.')
                        ),
                        ), 
                ]  
            ),
]
