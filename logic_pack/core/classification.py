import itertools

from logic_pack.core.evaluator import Evaluator


class FormulaClassifier:
    def __init__(self, expr: str):
        self.evaluator = Evaluator(expr)
        self.variables = self._extract_variables(expr)

    @staticmethod
    def _extract_variables(expr: str):
        # Simple extraction: all lowercase alphabetic characters (like p, q, r...)
        return sorted(set(filter(str.isalpha, expr)))

    def _generate_combinations(self):
        # All possible True/False combinations for the variables
        return list(itertools.product([True, False], repeat=len(self.variables)))

    def classify(self) -> str:
        results = []
        combinations = self._generate_combinations()

        for values in combinations:
            assignment = dict(zip(self.variables, values))
            result = self.evaluator.evaluate(assignment)
            results.append(result)

        if all(results):
            return "Tautology"
        elif not any(results):
            return "Contradiction"
        else:
            return "Contingency"
