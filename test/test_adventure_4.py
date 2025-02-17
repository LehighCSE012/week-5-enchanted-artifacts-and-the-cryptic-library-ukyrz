import pytest
from adventure import acquire_item, display_inventory
import io
import sys

def test_acquire_item_adds_item():
    inventory = []
    updated_inventory = acquire_item(inventory, "potion")
    assert "potion" in updated_inventory
    assert updated_inventory == ["potion"]

def test_acquire_item_prints_message(capsys):
    inventory = []
    acquire_item(inventory, "sword")
    captured = capsys.readouterr()
    assert "You acquired a sword!" in captured.out

def test_display_inventory_empty(capsys):
    inventory = []
    display_inventory(inventory)
    captured = capsys.readouterr()
    assert "Your inventory is empty." in captured.out

def test_display_inventory_items(capsys):
    inventory = ["potion", "key", "map"]
    display_inventory(inventory)
    captured = capsys.readouterr()
    assert "Your inventory:" in captured.out
    assert "1. potion" in captured.out
    assert "2. key" in captured.out
    assert "3. map" in captured.out
