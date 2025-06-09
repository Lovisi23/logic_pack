from logpack.core.parser import parse_expression


class Evaluator:
    def __init__(self, expr: str):
        self.original_expr = expr
        self.parsed_expr = parse_expression(expr)

    def evaluate(self, values: dict) -> bool:

        try:
            return eval(self.parsed_expr, {}, values)
        except NameError as e:
            raise ValueError(f"Missing variable in input: {e}")
        except Exception as e:
            raise ValueError(f"Error while evaluating expression: {e}")

    def __str__(self):
        return f"Original: {self.original_expr} | Parsed: {self.parsed_expr}"
