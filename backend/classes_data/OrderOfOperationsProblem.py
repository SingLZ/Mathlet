from .problem import Problem, Step

problems = [
    Problem(Equation='2 + 4 - 9 * 2 = ?',
            Steps=[Step(result='2 + 4 - 18 = ?',
                        step='9 * 2 = 18',
                        feedback='Correct! We use PEMDAS and start with multiplication.',
                        wrong_steps=
                        (Step(step='2 + 4 = 6',
                              feedback='Incorrect. We solve for multiplication before addition.'),
                         Step(step='4 - 9 = -5',
                              feedback='Incorrect. We solve for multiplication before subtraction.'),
                         Step(step='9 - 4 = 5',
                              feedback='Incorrect. We solve for multiplication before subtraction.')
                        ),
                        ),
                    Step(result='6 - 18 = ?',
                        step='2 + 4 = 6',
                        feedback='Correct! We calculate addition and subtraction from left to right, neither takes priority.',
                        wrong_steps=
                        (Step(step='2 + 4 = -2',
                              feedback='Incorrect'),
                         Step(step='2 + 18 = 20',
                              feedback='Incorrect - Check the numbers\' signs'),
                         Step(step='2 - 4 = -2',
                              feedback='Incorrect - Check the numbers\' signs')
                        ),
                        ),
                    Step(result='-12',
                        step='-12',
                        feedback='Correct! We add the two numbers to find the sum. You have completed the problem!', #feedback for the correct answer
                        wrong_steps=
                        (Step(step='24',
                              feedback='Incorrect - Check the numbers\' signs'),
                         Step(step='12',
                              feedback='Incorrect - Check the numbers\' signs'),
                         Step(step='2',
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
                        (Step(step='5 - 3 = 2',
                              feedback='Incorrect. We solve for parentheses before subtraction.'),
                         Step(step='3 + 2 = 5',
                              feedback='Incorrect. We solve for parentheses before addition.'),
                         Step(step='5 + 2 = 7',
                              feedback='Incorrect. We solve for parentheses before addition.')
                        ),
                        ),
                    Step(result='20 - 3 + 6 = ?',
                        step='4 * 5 = 20',
                        feedback='Correct! We move onto multiplication after parentheses',
                        wrong_steps=
                        (Step(step='5 - 3 = 2',
                              feedback='Incorrect. We solve for multiplication before subtraction.'),
                         Step(step='5 + 6 = 11',
                              feedback='Incorrect. We solve for multiplication before addition.'),
                         Step(step='3 - 5 = -2',
                              feedback='Incorrect. We solve for multiplication before subtraction.')
                        ),
                        ),
                    Step(result='17 + 6 = ?',
                        step='20 - 3 = 17',
                        feedback='Correct! We calculate addition and subtraction from left to right, neither takes priority.',
                        wrong_steps=
                        (Step(step='20 - 3 = 23',
                              feedback='Incorrect - Check the numbers\' signs.'),
                         Step(step='20 + 3 = 23',
                              feedback='Incorrect - Check the numbers\' signs.'),
                         Step(step='20 - 3 = -17',
                              feedback='Incorrect - Check the numbers\' signs.')
                        ),
                        ),
                    Step(result='23',
                        step='23',
                        feedback='Correct! We add the two numbers to find the sum. You have completed the problem!',
                        wrong_steps=
                        (Step(step='17',
                              feedback='Incorrect - Check the numbers\' signs.'),
                         Step(step='22',
                              feedback='Incorrect - Check the numbers\' signs.'),
                         Step(step='24',
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
                        (Step(step='2 - 6 = -4',
                              feedback='Incorrect. We solve for parentheses before subtraction.'),
                         Step(step='6 * 5 = 30',
                              feedback='Incorrect. We solve for parentheses before multiplication.'),
                         Step(step='1 / 2 = 0.5',
                              feedback='Incorrect. We solve for parentheses before division.')
                        ),
                        ),
                    Step(result='2 - 24 / 2 = ?',
                        step='6 * 4 = 24',
                        feedback='Correct! We calculate addition and subtraction from left to right, neither takes priority.',
                        wrong_steps=
                        (Step(step='2 - 6 = -4',
                              feedback='Incorrect. We solve for multiplication before subtraction.'),
                         Step(step='2 * 4 = 8',
                              feedback='Incorrect - Check the values that should be multiplied.'),
                         Step(step='2 / 2 = 1',
                              feedback='Incorrect - Check the values that we should operate on.')
                        ),
                        ),
                    Step(result='2 - 12 = ?',
                        step='24 / 2 = 12',
                        feedback='Correct! We calculate addition and subtraction from left to right, neither takes priority.',
                        wrong_steps=
                        (Step(step='2 - 24 = -22',
                              feedback='Incorrect - We solve for division before subtraction.'),
                         Step(step='2 - 24 = 26',
                              feedback='Incorrect - We solve for division before subtraction.'),
                         Step(step='2 / 2 = 1',
                              feedback='Incorrect - Check the values that we should operate on.')
                        ),
                        ),
                    Step(result='-10',
                        step='-10',
                        feedback='Correct! We subtract the two numbers to find the difference. You have completed the problem!',
                        wrong_steps=
                        (Step(step='14',
                              feedback='Incorrect - Check the numbers\' signs.'),
                         Step(step='20',
                              feedback='Incorrect - Check the numbers\' signs.'),
                         Step(step='-14',
                              feedback='Incorrect - Check the numbers\' signs.')
                        ),
                        ), 
                ]  
            ),
]

if __name__ == "__main__":
    print(problems[0].getTotalNumSteps())
    print(problems[0].getStepNum())
    