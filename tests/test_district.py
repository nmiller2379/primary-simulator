from simulator.district import District
def test_district_initialization():
    # Test basic initialization
    district = District(name="District 1", state="California", population=700000, delegates=5)
    assert district.name == "District 1"
    assert district.state == "California"
    assert district.population == 700000
    assert district.delegates == 5

def test_assign_support():
    district = District(name="District 2", state="Texas", population=800000, delegates=6)
    district.assign_support("Alice", 0.6)
    assert district.get_support("Alice") == 0.6

def test_get_support_nonexistent_candidate():
    district = District(name="District 3", state="Florida", population=600000, delegates=4)
    assert district.get_support("Bob") == 0.0

# def test_calculate_delegates():
#     district = District(name="District 4", state="New York", population=900000, delegates=8)
#     district.assign_support("Charlie", 0.5)
#     district.assign_support("Diana", 0.3)
#     district.assign_support("Eve", 0.2)
#     assert district.calculate_delegates() == {"Charlie": 4, "Diana": 2, "Eve": 1}

# def test_calculate_delegates_no_viable_candidates():
#     district = District(name="District 5", state="Illinois", population=500000, delegates=3)
#     district.assign_support("Frank", 0.1)
#     district.assign_support("Grace", 0.05)
#     assert district.calculate_delegates() == {}