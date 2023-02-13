from dataclasses import dataclass

@dataclass
class Problem:
    Equation: str
    Steps: list | set
    Answer: float # includes inf/-inf

    CurrentStep = 0 # index in Steps