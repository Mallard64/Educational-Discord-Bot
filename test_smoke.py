"""Smoke tests: the data files load and the stats table is well-formed.

These intentionally avoid importing main.py, which starts the Discord bot
on import. They cover the data the bot reads at startup.
"""
import json
import os

import globals

HERE = os.path.dirname(os.path.abspath(__file__))

# Save/config files the bot opens at startup.
DATA_FILES = [
    "OwO.json",
    "bal.json",
    "items.json",
    "levels.json",
    "select.json",
    "moves.json",
]


def test_data_files_are_valid_json_objects():
    for name in DATA_FILES:
        with open(os.path.join(HERE, name)) as f:
            data = json.load(f)
        assert isinstance(data, dict), f"{name} should hold a JSON object"


def test_stats_table_is_well_formed():
    assert isinstance(globals.stats, dict)
    assert globals.stats, "stats table should not be empty"
    for name, line in globals.stats.items():
        # Each entry is [HP, Def, Atk].
        assert isinstance(line, list) and len(line) == 3, f"{name} is malformed"
        assert all(isinstance(n, int) for n in line), f"{name} has non-int stats"
