import pytest
from adventure import enter_dungeon

def test_tuple_immutability_error_handling(capsys):
    dungeon_rooms = [("Room 1", "item1", "none", None)]
    player_stats = {'health': 100, 'attack': 5}
    inventory = []
    clues = set()
    artifacts = {}

    enter_dungeon(player_stats, inventory, dungeon_rooms, clues, artifacts)
    captured = capsys.readouterr()
    assert "Error: Cannot modify room tuples - they are immutable." in captured.out

def test_enter_dungeon_runs_without_crash():
    dungeon_rooms = [
        ("Room 1", "item1", "none", None),
        ("Room 2", None, "puzzle", ("success", "fail", -5))
    ]
    player_stats = {'health': 100, 'attack': 5}
    inventory = []
    clues = set()
    artifacts = {}
    try:
        player_health, inventory_out, clues_out = enter_dungeon(player_stats, inventory, dungeon_rooms, clues, artifacts)
        assert isinstance(player_health, int)
        assert isinstance(inventory_out, list)
        assert isinstance(clues_out, set)
    except Exception as e:
        pytest.fail(f"enter_dungeon raised an exception: {e}")
