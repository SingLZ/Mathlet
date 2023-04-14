from .problem import Problem, Step

problems = [
    Problem(Equation='2 + 4 - 9 * 2 = ?',
            Steps=[Step('2 + 4 - 18 = ?',
                        '9 * 2 = 18',
                        ('2 + 4 = 6', '4 - 9 = -5', '?'),
                        feedback='Use PEMDAS: start with multiplication.'
                        ),
                    Step('6 - 18 = ?',
                        '2 + 4 = 6',
                        ('2 + 4 = -2', '2 + 18 = 20', '2 - 4 = -2'),
                        feedback='Start from the beginning of the problem and solve.'
                        ),
                    Step('-12',
                        '-12',
                        ('24', '12', '2'),
                        feedback='You completed the problem!'
                    )
                ],
            ),
    Problem(Equation='4 * 5 - 3 + (2 + 4) = ?',
            Steps=[Step('4 * 5 - 3 + 6 = ?',
                        '2 + 4 = 6',
                        ('5 - 3 = 2', '3 + 2 = 5', '5 + 2 = 7'),
                        feedback="Use PEMDAS and start with parentheses"
                        ),
                    Step('20 - 3 + 6 = ?',
                        '4 * 5 = 20',
                        ('5 - 3 = 2', '5 + 6 = 11', '3 - 5 = -2'),
                        feedback='Move onto the multiplication'
                        ),
                    Step('17 + 6 = ?',
                        '20 - 3 = 17',
                        ('20 - 3 = 23', '20 + 3 = 23', '20 - 3 = -17'),
                        feedback='Solve for the rest of the problem'
                        ),
                    Step('23',
                        '23',
                        ('17', '22', '24'),
                        feedback='You completed the problem!'
                        ),    
                ]  
            ),
    Problem(Equation='2 - 6 * (5 - 1) / 2 = ?',
            Steps=[Step('2 - 6 * 4 / 2 = ?',
                        '(5 - 1) = 4',
                        ('2 - 6 = -4', '6 * 5 = 30', '1 / 2 = 0.5'),
                        feedback="PEMDAS: solve inside the parentheses first"
                        ),
                    Step('2 - 24 / 2 = ?',
                        '6 * 4 = 24',
                        ('2 - 6 = -4', '2 * 4 = 8', '2 / 2 = 1'),
                        feedback='Move onto the multiplication.'
                        ),
                    Step('2 - 12 = ?',
                        '24 / 2 = 12',
                        ('2 - 24 = -22', '2 - 24 = 26', '2 / 2 = 1'),
                        feedback='Solve for the rest of the problem'
                        ),
                    Step('-10',
                        '-10',
                        ('14', '10', '-14'),
                        feedback='You completed the problem!'
                        ),    
                ]  
            )
]
