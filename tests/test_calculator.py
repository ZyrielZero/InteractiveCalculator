import builtins
from src.calculator import calculator


def run_repl(monkeypatch, capsys, inputs):
    answers = iter(inputs)
    monkeypatch.setattr(builtins, "input", lambda _: next(answers))
    calculator()
    return capsys.readouterr().out


def test_addition(monkeypatch, capsys):
    out = run_repl(monkeypatch, capsys, ["add 8 5", "exit"])
    assert "Result: 13.0" in out


def test_subtraction(monkeypatch, capsys):
    out = run_repl(monkeypatch, capsys, ["subtract 20 7", "exit"])
    assert "Result: 13.0" in out


def test_multiplication(monkeypatch, capsys):
    out = run_repl(monkeypatch, capsys, ["multiply 6 4", "exit"])
    assert "Result: 24.0" in out


def test_division(monkeypatch, capsys):
    out = run_repl(monkeypatch, capsys, ["divide 27 3", "exit"])
    assert "Result: 9.0" in out


def test_division_by_zero(monkeypatch, capsys):
    out = run_repl(monkeypatch, capsys, ["divide 7 0", "exit"])
    assert "Division by zero is not allowed." in out


def test_unknown_operation(monkeypatch, capsys):
    out = run_repl(monkeypatch, capsys, ["times 2 8", "exit"])
    assert "Unknown operation" in out


def test_invalid_format(monkeypatch, capsys):
    out = run_repl(monkeypatch, capsys, ["add five six", "exit"])
    assert "Invalid input" in out


def test_exit_message(monkeypatch, capsys):
    out = run_repl(monkeypatch, capsys, ["exit"])
    assert "Exiting..." in out