class Candidate:
    def __init__(self, name: str, age: int, home_state: str, ethnicity: str, support: float = 0.0):
        self.name = name
        self.age = age
        self.home_state = home_state
        self.ethnicity = ethnicity
        self.support = support

    def __repr__(self):
        return f"<Candidate:{self.name}, age={self.age}, home_state={self.home_state}, support={self.support})>"
