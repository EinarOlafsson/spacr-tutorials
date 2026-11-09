"""A tutorial recording must never read or write the user's real chaining pins.

Chaining pins are the paths a user typed into a module (Mask's `src`, say),
kept in XDG state storage so they survive a restart. Until 2026-09-15 no
sandbox covered that store: the real `~/.local/state/spacr/chaining/pins.json`
on the maintainer's machine pinned Mask to a deleted pytest directory, the
app opened Mask there, and a tutorial recording showed the path in its Source
field. The test-suite sandbox is pinned in spaCR by
tests/test_the_chaining_pin_store_is_sandboxed.py; this half checks the
matching XDG_STATE_HOME isolation in tools/tutorials/capture_refresh.py and
moved here with the recording tools.
"""
from __future__ import annotations

import ast
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]


def test_the_tutorial_capture_isolates_state_storage_too():
    # XDG_CONFIG_HOME moves QSettings only; the pins follow XDG_STATE_HOME.
    source = (REPO / "tools" / "tutorials" / "capture_refresh.py").read_text(
        encoding="utf-8")
    environment_keys = set()
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Dict):
            keys = {k.value for k in node.keys
                    if isinstance(k, ast.Constant) and isinstance(k.value, str)}
            if "XDG_CONFIG_HOME" in keys:
                environment_keys |= keys
    assert "XDG_CONFIG_HOME" in environment_keys
    assert "XDG_STATE_HOME" in environment_keys
    assert "os.environ.pop('SPACR_CHAINING_PINS', None)" in source
