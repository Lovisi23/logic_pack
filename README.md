# package_name

The Logic Expressions Package is used to:

- Parse logical expressions using symbols like ¬, ∧, ∨, →, ↔ and convert them to valid Python syntax.
- Evaluate logical expressions given a set of truth assignments.
- Classify logical formulas as tautology, contradiction, or satisfiable.
- Generate and display truth tables for logical formulas.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package_name

```bash
pip install Logic_Package
```

## Usage

```python
from logic_pack.core.parser import parse_expression
from logic_pack.core.evaluator import Evaluator
from logic_pack.core.classification import FormulaClassifier
from logic_pack.tools.truth_table import TruthTable
from logic_pack.tools.utils import normalize_expression, extract_variables, is_valid_expression

# 1. Parse an expression
parsed = parse_expression("¬p ∨ q")
print(parsed)  # Output: not p or q

# 2. Evaluate the expression with variable values
evaluator = Evaluator("¬p ∨ q")
result = evaluator.evaluate({'p': False, 'q': False})  # True

# 3. Classify the expression
classifier = FormulaClassifier("¬p ∨ p")
print(classifier.classify())  # Tautology

# 4. Display the truth table
table = TruthTable("p → q")
table.display()

# 5. Utilities
print(normalize_expression("¬p∨q"))       # "¬ p ∨ q"
print(extract_variables("¬p∨q"))          # ['p', 'q']
print(is_valid_expression("¬p ∨ q"))      # True


```

## Author
Guilherme Caputo Lovisi

## License
[MIT](https://choosealicense.com/licenses/mit/)