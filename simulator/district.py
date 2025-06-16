class District:
    def __init__(self, name: str, state: str, population: int, delegates: int):
        self.name = name
        self.state = state
        self.population = population
        self.delegates = delegates
        self.support_percentages = {}

    def assign_support(self, candidate_name: str, support: float):
        """Assign support percentage to a candidate in this district."""
        if support < 0 or support > 1:
            raise ValueError("Support must be between 0 and 1.")
        self.support_percentages[candidate_name] = support

    def get_support(self, candidate_name: str) -> float:
        """Get the support percentage for a candidate in this district."""
        return self.support_percentages.get(candidate_name, 0.0)
    def calculate_delegates(self, threshold: float = 0.15) -> dict:
        """Calculate delegate allocation based on support percentages and viability threshold."""
        total_support = sum(self.support_percentages.values())
        if total_support == 0:
            return {}

        # Filter candidates who meet the viability threshold
        viable_candidates = {
            name: support for name, support in self.support_percentages.items()
            if support / total_support >= threshold
        }

        if not viable_candidates:
            return {}

        # Calculate delegates for each viable candidate
        delegates_distribution = {}
        for name, support in viable_candidates.items():
            delegates_distribution[name] = round(
                (support / total_support) * self.delegates
            )

        return delegates_distribution