def parse_expression(expr: str) -> str:
    """
    Converts logical symbols to Python operators.

    Examples:
    - '¬p ∨ q' → 'not p or q'
    - 'p ∧ q' → 'p and q'
    - 'p → q' → 'not p or q'
    - 'p ↔ q' → '(p and q) or (not p and not q)'
    """

    expr = expr.replace('¬', 'not ')
    expr = expr.replace('∧', ' and ')
    expr = expr.replace('∨', ' or ')

    # Simple replacement for implication: p → q becomes not p or q
    while '→' in expr:
        expr = replace_conditional(expr)

    # Simple replacement for biconditional: p ↔ q becomes (p and q) or (not p and not q)
    while '↔' in expr:
        expr = replace_biconditional(expr)

    return expr


def replace_conditional(expr: str) -> str:
    parts = expr.split('→', 1)
    left = parts[0].strip().split()[-1]  # last variable before →
    right = parts[1].strip().split()[0]  # first variable after →
    return expr.replace(f'{left} → {right}', f'not {left} or {right}')


def replace_biconditional(expr: str) -> str:
    parts = expr.split('↔', 1)
    left = parts[0].strip().split()[-1]
    right = parts[1].strip().split()[0]
    return expr.replace(f'{left} ↔ {right}', f'({left} and {right}) or (not {left} and not {right})')
