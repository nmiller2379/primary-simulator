class Candidate:
    def __init__(self, name: str, age: int, home_state: str, ethnicity: str, support: float = 0.0, delegate_count: int = 0):
        self.name = name
        self.age = age
        self.home_state = home_state
        self.ethnicity = ethnicity
        self.support = support
        self.delegate_count = delegate_count

    def delegate_accumulation(self, delegates: int):
        # Method to accumulate delegates for the candidate
        if delegates < 0:
            raise ValueError("Number of delegates cannot be negative")
        self.delegate_count += delegates

    def __repr__(self):
        return f"<Candidate:{self.name}, age={self.age}, home_state={self.home_state}, support={self.support} delegate_count={self.delegate_count}>"
