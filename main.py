from calculator import add, subtract, multiply, divide

OPERATIONS = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}


def evaluate(expression):
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError("Expected Format: <number> <operator> <number>")
    left, op, right = parts
    if op not in OPERATIONS:
        raise ValueError(f"Unknown Operator: {op}")
    a, b = float(left), float(right)
    return OPERATIONS[op](a, b)


def repl():
    print("Calculator REPL. Enter expressions like '3 + 4'. Type 'quit' to exit.")
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if line.lower() in {"quit", "exit"}:
            break
        if not line:
            continue
        try:
            print(evaluate(line))
        except (ZeroDivisionError, ValueError) as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    repl()