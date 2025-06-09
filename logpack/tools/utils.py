import re


def extract_variables(expr: str) -> list:
    return sorted(set(filter(str.isalpha, expr)))


def normalize_expression(expr: str) -> str:
    expr = expr.replace(" ", "")
    expr = expr.replace("¬", "¬ ")
    expr = expr.replace("∧", " ∧ ")
    expr = expr.replace("∨", " ∨ ")
    expr = expr.replace("→", " → ")
    expr = expr.replace("↔", " ↔ ")
    return expr.strip()


def is_valid_expression(expr: str) -> bool:
    pattern = re.compile(r'^[¬∧∨→↔()\s a-zA-Z]+$')
    return bool(pattern.match(expr))
