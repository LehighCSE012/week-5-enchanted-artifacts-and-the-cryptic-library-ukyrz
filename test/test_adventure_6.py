import pytest
from adventure import discover_artifact

def test_discover_artifact_existing():
    artifacts = {
        "amulet_of_vitality": {"description": "amulet", "power": 10, "effect": "increases health"}
    }
    player_stats = {'health': 50, 'attack': 5}
    updated_stats, updated_artifacts = discover_artifact(player_stats, artifacts, "amulet_of_vitality")
    assert updated_stats['health'] == 60
    assert "amulet_of_vitality" not in updated_artifacts

def test_discover_artifact_non_existing(capsys):
    artifacts = {}
    player_stats = {'health': 50, 'attack': 5}
    discover_artifact(player_stats, artifacts, "non_existent_artifact")
    captured = capsys.readouterr()
    assert "You found nothing of interest." in captured.out

def test_discover_artifact_health_effect():
    artifacts = {
        "amulet_of_vitality": {"description": "amulet", "power": 10, "effect": "increases health"}
    }
    player_stats = {'health': 50, 'attack': 5}
    updated_stats, _ = discover_artifact(player_stats, artifacts, "amulet_of_vitality")
    assert updated_stats['health'] == 60

def test_discover_artifact_attack_effect():
    artifacts = {
        "ring_of_strength": {"description": "ring", "power": 5, "effect": "enhances attack"}
    }
    player_stats = {'health': 50, 'attack': 5}
    updated_stats, _ = discover_artifact(player_stats, artifacts, "ring_of_strength")
    assert updated_stats['attack'] == 10

def test_discover_artifact_prints_description(capsys):
    artifacts = {
        "amulet_of_vitality": {"description": "A glowing amulet.", "power": 10, "effect": "increases health"}
    }
    player_stats = {'health': 50, 'attack': 5}
    discover_artifact(player_stats, artifacts, "amulet_of_vitality")
    captured = capsys.readouterr()
    assert "A glowing amulet." in captured.out
