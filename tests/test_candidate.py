from simulator.candidate import Candidate

def test_candidate_initialization():
    # Test basic initialization
    candidate = Candidate(name="Alice", age=35, home_state="California", ethnicity="Asian", support=0.75, delegate_count=3)
    assert candidate.name == "Alice"
    assert candidate.age == 35
    assert candidate.home_state == "California"
    assert candidate.ethnicity == "Asian"
    assert candidate.support == 0.75
    assert candidate.delegate_count == 3

def test_candidate_repr():
    # Test the string representation
    candidate = Candidate(name="Bob", age=40, home_state="Texas", ethnicity="Black", support=0.60)
    assert repr(candidate) == "<Candidate:Bob, age=40, home_state=Texas, support=0.6 delegate_count=0>"

def test_delegate_accumulation():
    # Test delegate accumulation method
    candidate = Candidate(name="Charlie", age=30, home_state="Florida", ethnicity="Hispanic", support=0.80)
    candidate.delegate_accumulation(1)
    assert candidate.delegate_count == 1

def test_delegate_accumulation_negative():
    # Test delegate accumulation with negative value
    candidate = Candidate(name="Diana", age=45, home_state="New York", ethnicity="White", support=0.70)
    try:
        candidate.delegate_accumulation(-1)
    except ValueError as e:
        assert str(e) == "Number of delegates cannot be negative"