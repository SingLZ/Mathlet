class ProblemsFeedback:
    def __init__(self, problem, steps):
        self.problem = problem
        self.steps = steps

steps01 = {
    "uno": {
        "A": {
            "step": "2*2=4",
            "correctness": True,
            "feedback": "absolute genius you are"
        },
        "B": {
            "step": "2+2=4",
            "correctness": False,
            "feedback": "not correct!!"
        },
        "C": {
            "step": "2+2=4",
            "correctness": False,
            "feedback": "not correct!!!"
        },
        "D": {
            "step": "2+2=4",
            "correctness": False,
            "feedback": "not correct!!!"
        }
    },
    "dos": {
        "A": {
            "step": "4*2=8",
            "correctness": False,
            "feedback": "second wrong step"
        },
        "B": {
            "step": "4/2=2",
            "correctness": True,
            "feedback": "good job!!"
        },
        "C": {
            "step": "4/1=4",
            "correctness": False,
            "feedback": "second wrong step!"
        },
        "D": {
            "step": "2-2=0",
            "correctness": False,
            "feedback": "second wrong step!!"
        }
    },
    "tres":{
        "2+4=6": {
        "correctness": True
        },
        "4-2=2": {
            "correctness": False
        },
        "3+3=6": {
            "correctness": False
        },
        "5-5=0": {
            "correctness": False
        }
    },
    "cuatro": {
        "Final: 6+2=8": {
            "correctness": True,
            "id": "last"
        },
        "Final: 2+2=4": {
            "correctness": False,
            "id": "lastnot"
        },
        "Final: 1+1=2": {
            "correctness": False,
            "id": "lastnot"        
        },
        "Final: 1+1=3": {
            "correctness": False,
            "id": "lastnot"
        }
    }
}

steps02 = {
    "problem02": {
        "name": "3+3*3/3+3",
        "steps": {
            "uno": {
                "A": {
                    "step": "3*3=9",
                    "correctness": True,
                    "feedback": "absolute genius you are"
                },
                "B": {
                    "step": "2+2=4",
                    "correctness": False,
                    "feedback": "not correct!!"
                },
                "C": {
                    "step": "3+3=6",
                    "correctness": False,
                    "feedback": "not correct!!!"
                },
                "D": {
                    "step": "4+4=4",
                    "correctness": False,
                    "feedback": "not correct!!!"
                }
            },
            "dos": {
                "4*2=8": {
                    "correctness": False,
                    "feedback": "second wrong step"
                },
                "9/3=3": {
                    "correctness": True,
                    "feedback": "good job!!"
                },
                "4/1=4": {
                    "correctness": False,
                    "feedback": "second wrong step!"
                },
                "2-2=0": {
                    "correctness": False,
                    "feedback": "second wrong step!!"
                }
            },
            "tres":{
                "3+3=6": {
                    "correctness": True
                },
                "4-2=2": {
                    "correctness": False
                },
                "3+3=6": {
                    "correctness": False
                },
                "5-5=0": {
                    "correctness": False
                }
            },
            "cuatro": {
                "Final: 6+3=9": {
                    "correctness": True
                },
                "Final: 2+2=4": {
                    "correctness": False
                },
                "Final: 1+1=2": {
                    "correctness": False
                },
                "Final: 1+1=3": {
                    "correctness": False
                }
            }
        }
    }
}
