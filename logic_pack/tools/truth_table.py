import itertools
from logic_pack.core.evaluator import Evaluator


class TruthTable:
    def __init__(self, expr: str):
        self.evaluator = Evaluator(expr)
        self.variables = self._extract_variables(expr)

    def _extract_variables(self, expr: str):
        return sorted(set(filter(str.isalpha, expr)))

    def _generate_combinations(self):
        return list(itertools.product([True, False], repeat=len(self.variables)))

    def display(self):
        combinations = self._generate_combinations()
        col_width = max(len(var) for var in self.variables + ['Result'])

        # Header
        header = ' | '.join(var.center(col_width) for var in self.variables) + ' | ' + 'Result'.center(col_width)
        print(header)
        print('-' * len(header))

        # Rows
        for values in combinations:
            assignment = dict(zip(self.variables, values))
            result = self.evaluator.evaluate(assignment)
            values_str = ' | '.join(str(val).center(col_width) for val in values)
            print(f"{values_str} | {str(result).center(col_width)}")
