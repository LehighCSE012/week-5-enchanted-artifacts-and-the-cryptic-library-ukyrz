import pytest
from adventure import find_clue

def test_find_clue_new_clue():
    clues = set()
    updated_clues = find_clue(clues, "clue 1")
    assert "clue 1" in updated_clues
    assert len(updated_clues) == 1

def test_find_clue_duplicate_clue(capsys):
    clues = {"clue 1"}
    find_clue(clues, "clue 1")
    captured = capsys.readouterr()
    assert "You already know this clue." in captured.out
    assert len(clues) == 1 # Set should still have only one clue

def test_find_clue_prints_discovery_message(capsys):
    clues = set()
    find_clue(clues, "new clue")
    captured = capsys.readouterr()
    assert "You discovered a new clue: new clue" in captured.out
