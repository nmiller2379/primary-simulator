from simulator.candidate import Candidate

def test_candidate_initialization():
    # Test basic initialization
    candidate = Candidate(name="Alice", age=35, home_state="California", ethnicity="Asian", support=0.75)
    assert candidate.name == "Alice"
    assert candidate.age == 35
    assert candidate.home_state == "California"
    assert candidate.ethnicity == "Asian"
    assert candidate.support == 0.75

def test_candidate_repr():
    # Test the string representation
    candidate = Candidate(name="Bob", age=40, home_state="Texas", ethnicity="Black", support=0.60)
    assert repr(candidate) == "<Candidate:Bob, age=40, home_state=Texas, support=0.6)>"

    
